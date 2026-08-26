---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1412.0744v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1412.0744v2_Extraction_of_Pharmacokinetic_Evidence_of_Drug-drug_Interactions_from_the_Litera

> Source: 1412.0744v2_Extraction_of_Pharmacokinetic_Evidence_of_Drug-drug_Interactions_from_the_Litera.pdf

> Pages: 34

---


## Page 1


1
Extraction of Pharmacokinetic Evidence of Drug-drug
Interactions from the Literature
Artemy Kolchinsky1,2, Anália Lourenço3,4, Heng-Yi Wu,5, Lang Li,5, Luis M. Rocha,1,2,∗
1 School of Informatics and Computing, Indiana University, Bloomington, IN, USA
2 Instituto Gulbenkian de Ciência, Oeiras, Portugal
3 ESEI: Escuela Superior de Ingeniería Informática, University of Vigo, Ediﬁcio
Politécnico, Campus Universitario As Lagoas s/n 32004, Ourense, Spain
4 CEB - Centre of Biological Engineering, University of Minho, Campus de Gualtar,
4710-057 Braga, Portugal
5 Center for Computational Biology and Bioinformatics and Department of Medical &
Molecular Genetics, Indiana University School of Medicine, Indianapolis, IN, USA
∗E-mail: rocha@indiana.edu
Abstract
Drug-drug interaction (DDI) is a major cause of morbidity and mortality and a subject of intense scien-
tiﬁc interest. Biomedical literature mining can aid DDI research by extracting evidence for large numbers
of potential interactions from published literature and clinical databases. Though DDI is investigated
in domains ranging in scale from intracellular biochemistry to human populations, literature mining
has not been used to extract speciﬁc types of experimental evidence, which are reported diﬀerently for
distinct experimental goals.
We focus on pharmacokinetic evidence for DDI, essential for identifying
causal mechanisms of putative interactions and as input for further pharmacological and pharmaco-
epidemiology investigations. We used manually curated corpora of PubMed abstracts and annotated
sentences to evaluate the eﬃcacy of literature mining on two tasks: ﬁrst, identifying PubMed abstracts
containing pharmacokinetic evidence of DDIs; second, extracting sentences containing such evidence from
abstracts. We implemented a text mining pipeline and evaluated it using several linear classiﬁers and
a variety of feature transforms. The most important textual features in the abstract and sentence clas-
siﬁcation tasks were analyzed. We also investigated the performance beneﬁts of using features derived
from PubMed metadata ﬁelds, various publicly available named entity recognizers, and pharmacokinetic
dictionaries. Several classiﬁers performed very well in distinguishing relevant and irrelevant abstracts
(reaching F1≈0.93, MCC≈0.74, iAUC≈0.99) and sentences (F1≈0.76, MCC≈0.65, iAUC≈0.83).
We
found that word bigram features were important for achieving optimal classiﬁer performance and that
features derived from Medical Subject Headings (MeSH) terms signiﬁcantly improved abstract classiﬁca-
tion. We also found that some drug-related named entity recognition tools and dictionaries led to slight
but signiﬁcant improvements, especially in classiﬁcation of evidence sentences. Based on our thorough
analysis of classiﬁers and feature transforms and the high classiﬁcation performance achieved, we demon-
strate that literature mining can aid DDI discovery by supporting automatic extraction of speciﬁc types
of experimental evidence.
Introduction
Drug-drug interaction (DDI) is one of the major causes of adverse drug reaction (ADR) and a threat
to public health. Pharmaco-epidemiology studies [1] and recent National Health Statistics Report pub-
lications [2,3] indicate that each year an estimated 195,000 hospitalizations and 74,000 emergency room
visits are the result of DDI in the United States alone [4]. DDI has been implicated in nearly 3% of
all hospital admissions [5] and 4.8% of admissions among the elderly [1] and is a common consequence
of medical error, representing 3% to 5% of all inpatient medication errors [6]. With increasing rates of
polypharmacy, which refers to the use of multiple medications or more medications than are clinically
arXiv:1412.0744v2  [stat.ML]  18 May 2015


## Page 2


2
indicated [7], the incidence of DDI will likely increase in the coming years.
Researchers link molecular mechanisms underlying DDI to their clinical consequences through three
types of studies: in vitro, in vivo, and clinical [8–10]. In vitro pharmacology experiments use intact
cells (e.g. hepatocytes), microsomal protein fractions, or recombinant systems to investigate molecular
interaction mechanisms within the cell (i.e.
metabolic, transport- or target-based).
In vivo studies
evaluate whether such interactions impact drug exposure in humans.
Finally, clinical studies use a
population-based approach and large electronic medical record databases to investigate the contribution
of DDI to drug eﬃcacy and ADR.
Automated biomedical literature mining (BLM) methods oﬀer a promising approach for uncovering
evidence of possible DDI in published literature and clinical databases [11]. BLM is a biomedical infor-
matics methodology that holds the promise of tapping into the biomedical collective knowledge [12] by
extracting information from large-scale literature repositories and by integrating information scattered
across various domain-speciﬁc databases and ontologies [13–15]. It has been used for knowledge dis-
covery in many biomedical domains, including extraction of protein-protein interactions [16,17], protein
structure prediction [18], identiﬁcation of genomic locations associated with cancer [19], and mining drug
targets [20]. In the domain of DDI, putative interactions uncovered by BLM can serve as targets for
subsequent investigation by in vitro pharmacological methods as well as in vivo and clinical studies [11].
BLM has previously been used for DDI information extraction [21–26], as overviewed by the literature
on recent DDI challenges [27–29] and Paciﬁc Symposium on Biocomputing sessions [30, 31]. However,
much remains to be done in automatic extraction of experimental evidence of DDI from text. Impor-
tantly, experimental evidence of DDI is reported diﬀerently for the diﬀerent types of studies described
above. For instance, in vivo pharmacokinetic experiments report parameters such as the ‘area under the
concentration-time curve’, while clinical studies may instead report population-level statistics of adverse
drug reactions. It is important for BLM pipelines to be able to identify these diﬀerent kinds of evidence
independently.
To address this situation, we demonstrate the use BLM for reliable extraction of pharmacokinetic
evidence for DDI from reports of in vitro and in vivo experiments. Pharmacokinetic experimental evidence
refers to measures of pharmacokinetic parameters such as the inhibition constant (Ki), the 50% inhibitory
concentration (IC50), and the area under the plasma concentration-time curve (AUCR). Such evidence
is particularly important in identifying or dismissing causal mechanisms behind DDIs and in providing
support for putative DDIs extracted from mining patient records, where biases and confounds in reporting
often give rise to non-causal correlations [32]. In order to pursue the goal of using BLM to uncover
pharmacokinetic DDI evidence, a collaboration was developed between Rocha’s lab, working on literature
mining, and Li’s lab, working on pharmacokinetics. Though this work is focused on pharmacokinetic
evidence, in subsequent studies we will approach other types of DDI evidence (e.g. clinical evidence).
Our approach is diﬀerent from previous BLM approaches to DDI information extraction [21–26, 28]
because our ultimate goal is not to identify interacting drugs themselves but rather abstracts and sentences
containing a speciﬁc type of evidence of drug interaction. Existing DDI-extraction methods and corpora
— including those evaluated under the DDI Extraction challenges [27–29, 33, 34] — are not well suited
for this task because they do not attempt to extract experimental evidence of drug interactions, nor
speciﬁcally label distinct kinds of evidence. For instance, the DDI Extraction challenge ‘11 [33] used
a corpus of several hundred documents from DrugBank [35], but interacting drug pairs were annotated
without regard for the presence of experimental evidence. More recently, the DDI Extraction challenge
‘13 [34] provided a corpus annotated with pharmacokinetic and pharmacodynamic interactions [29], but
the goal of the text mining task was the extraction and classiﬁcation of interacting drug pairs, not the
extraction of the experimental evidence of interactions. Other related work has used DrugBank data for
large-scale extraction of drug-gene and drug-drug relationships [22, 36], and for predicting DDI using a
drug-drug network based on phenotypic, therapeutic, chemical, and genomic feature similarity [37], but
neither study aimed to identify or extract speciﬁc kinds experimental evidence of DDI.


## Page 3


3
We have previously shown that BLM can be used for automatic extraction of numerical pharmacoki-
netics (PK) parameters from the literature [38]. However, that work was not oriented speciﬁcally toward
the extraction of evidence of DDI. Recently, we reported high performance in a preliminary work on
automatically classifying PubMed abstracts that contain pharmacokinetic evidence of DDI [39] (details
below). Because identifying relevant abstracts is only a ﬁrst step in the process of extracting pharma-
cokinetic evidence of DDI, in this work we consider both the problem of identifying abstracts containing
pharmacokinetic evidence of DDI and that of extracting from abstracts sentences that contain this spe-
ciﬁc kind of evidence. In addition to evidence sentence extraction, we also provide a new assessment of
abstract classiﬁcation using an updated version of a separately published corpus [26], leading to substan-
tially better classiﬁcation performance than reported in our preliminary study [39]. The updated corpus
is described below and is publicly available. Finally, we provide a new comparison of classiﬁers, a new
evaluation methodology using permutation-based signiﬁcance tests and Principal Component Analysis
(PCA) [40] of feature weights, and a detailed study of the beneﬁts of including features derived from
PubMed metadata, named entity recognition tools and specialized dictionaries.
We created abstract and sentence corpora using annotation criteria for identifying pharmacokinetic
evidence of DDI. We consider positive (indicating the presence of interactions) and negative (indicating
the absence) DDI evidence as relevant (see “Materials and Methods” section), since both provide important
information about possible DDI. Because the criteria considered here are diﬀerent from those used in
previously available DDI corpora, our results are not directly comparable to other BLM approaches to
DDI. Therefore, we pursued a thorough evaluation of the performance of diﬀerent types of classiﬁers,
feature transforms, and normalization techniques. For both abstract and sentence classiﬁcation tasks
we tested several linear classiﬁers: logistic regression, support vector machines (SVM), binomial Naive
Bayes, linear discriminant analysis, and a modiﬁcation of the Variable Trigonometric Threshold (VTT)
classiﬁer, previously developed by Rocha’s lab and found to perform well on protein-protein interaction
text mining tasks [12,41,42]. As we describe in the results and discussion sections, classiﬁers fall into two
main classes based on whether or not they take into account feature covariances. In addition, we compared
diﬀerent feature transform methods, including normalization techniques such as ‘Term Frequency, Inverse
Document Frequency’ (TFIDF) and dimensionality reduction based on Principle Component Analysis
(PCA). We also compared performance when including features generated by several Named Entity
Recognition (NER) tools and specialized dictionaries.
In the experiments reported, our goal is to measure the quality of automated methods in identifying
pharmacokinetic evidence of DDIs reported in the literature. More generally, we seek to demonstrate
that literature mining can be successful in automatically extracting experimental evidence of interactions
as part of DDI workﬂows. We show that many classiﬁer conﬁgurations achieve high performance on this
task, demonstrating the robustness and eﬃcacy of BLM on extracting pharmacokinetic evidence of DDI.
Materials and Methods
The following sections describe the methods used in our literature mining pipeline. Its basic steps are
visually diagrammed in Fig. 1. They include the selection of corpus documents, hand-labeling of ground
truth assignments, extraction and normalization of textual features, and computation of unigram/bigram
occurrences matrices. Cross-validation folds are used to estimate generalization performance of classi-
ﬁer and feature transform conﬁgurations, while nested (inner) cross-validation folds are used to choose
classiﬁer hyperparameters. The software consisted of custom Python scripts unless otherwise noted.


## Page 4


4
Figure 1. Literature mining pipeline: The basic steps of the literature mining pipeline include
selection of corpus documents, hand-labeling of ground truth assignments, extraction and normalization
of textual features, and computation of unigram/bigram occurrences matrices. Cross-validation folds
are used to estimate generalization performance of classiﬁer and feature transform conﬁgurations, while
nested (inner) cross-validation folds are used to choose classiﬁer hyperparameters.
Abstract Corpus
For the training corpus, Li’s lab selected 1203 pharmacokinetics-related abstracts by searching PubMed
using terms from a previously developed ontology for PK pharmacokinetic parameters [38]. Therefore, all
retrieved articles describe and contain some form of pharmacokinetic evidence, though not necessarily of
DDI. We kept in vitro studies but removed any animal in vivo studies. Abstracts were labeled according
to the following criteria: abstracts that reported the presence or absence of drug interaction supported
by explicit experimental evidence of pharmacokinetic parameter data were labeled as DDI-relevant (909
abstracts) while the rest were labeled as DDI-irrelevant (294 abstracts). DDI-relevance was established
regardless of whether the relevant enzymes were presented or not. Importantly, the concept of DDI-
relevance employed here updates the criteria used in a previous preliminary study [39].
Interactions
between a drug and food, fruit, smoking, alcohol, and natural products are now classiﬁed as drug interac-
tions because their pharmacokinetics studies are designed similarly. For the same reason, studies dealing
with interactions between drug metabolites (instead of parent compounds) are now also considered rele-
vant, as well as studies reporting inhibition of induction of a drug on a drug metabolism enzyme or drug
transporter. Classiﬁcation was done by three graduate students with M.S. degrees and one postdoctoral
annotator; any inter-annotator conﬂicts were checked by a Pharm D. and an M.D. scientist with extensive


## Page 5


5
pharmacological training. The corpus is publicly available as “Pharmacokinetics DDI-Relevant Abstracts
V0” in [43] (see also [26]).
We extracted textual features from PubMed article title and abstract text ﬁelds as well as the following
metadata ﬁelds: the author names, the journal title, the Medical Subject Heading (MeSH) terms, the
‘registry number/EC number’ (RN) ﬁeld, and the ‘secondary source’ ﬁeld (SI) (the latter two ﬁelds
contain identiﬁcation codes for relevant chemical and biological substances). For each PubMed entry,
the content of the above ﬁelds was tokenized, processed by Porter stemming [44], and converted into
textual features (unigrams and, in certain runs, bigrams). Strings of numbers were converted into ‘#’,
short textual features (with length of less than 2 characters) and infrequent features (that occurred in
less than 2 documents) were omitted. Author names, journal titles, substance names, and MeSH terms
were treated as single textual tokens.
The corpus was represented as binary term-document occurrence matrices. We evaluated classiﬁcation
performance under two diﬀerent conditions: in the ﬁrst — referred to as ‘unigram runs’ — only word
unigram features were used; in the second — referred to as ‘bigram runs’ — word bigram features were
used in addition to unigram features. Bigram runs included a much larger number of parameters (i.e. the
bigram feature coeﬃcients) that needed to be estimated from training data, which can potentially increase
generalization error arising from increased model complexity [45].
Testing the classiﬁers exclusively
with unigram features as well as with both unigram and bigram features evaluated whether the class
information provided by bigrams outweighed their cost in complexity.
Sentence Corpus
The evidence sentence task consisted in identifying those sentences within a PubMed abstract that re-
ported experimental evidence for the presence or absence of a speciﬁc DDI. For this purpose, Li’s group
developed a training corpus of 4600 sentences extracted from 428 PubMed abstracts. All abstracts con-
tained (positive or negative) pharmacokinetic evidence of DDIs. Sentences were manually labeled as
DDI-relevant (1396 sentences) if they explicitly mentioned pharmacokinetic evidence for the presence or
absence of drug-drug interactions, and as DDI-irrelevant (3204 sentences) otherwise.
The same pre-
processing and annotation procedures were followed for the sentence corpus as for the abstract corpus
(see section “Abstract Corpus”). This corpus is publicly available as “Deep Annotated PK Corpus V1”
in [43] (see also [26]).
Classiﬁers
Six diﬀerent linear classiﬁers were tested:
1. VTT: a simpliﬁed, angle-domain version of the Variable Trigonometric Threshold Classiﬁer, pre-
viously developed in Rocha’s lab [12,41,42]. Given a document vector x=<x1,...,xK> with features (i.e.
dimensions) indexed by i, the separating hyperplane is deﬁned as
X
i
ϕixi −λ = 0
Here, λ is a threshold (bias) and φi is the ‘angle’ of feature i in binary class space:
ϕi = arctan pi
ni
−π
4
where pi is the probability of occurrence of feature i in relevant-class documents and ni is the probability
of occurrence of feature i in irrelevant-class documents. The threshold parameter λ is chosen so that a
neutral ‘pseudo-document’ deﬁned by xi=(pi+ni)/2 falls exactly onto the separating hyperplane.
The full version of VTT, which includes additional parameters to account for named entity occurrences
and which we have previously used in protein-protein interaction classiﬁcation, is evaluated in combination


## Page 6


6
with various NER tools in section “Impact of NER and PubMed metadata on abstract classiﬁcation”
below. VTT performs best on sparse, positive datasets; for this reason, we do not evaluate it on dense
dimensionality-reduced datasets. Notice that in previous work, we used a diﬀerent version of VTT with
a cross-validated threshold parameter; its performance on the tasks was very similar, and is reported in
the Supporting Information as the ‘VTTcv’ classiﬁer (section 1 and 2 in S1 Text).
2. SVM : a linear Support Vector Machine with a cross-validated regularization parameter (imple-
mented using the sklearn [46] library’s interface to the LIBLINEAR package [47]).
3.
Logistic regression classiﬁer with a cross-validated regularization parameter (also implemented
using sklearn’s interface to LIBLINEAR).
4. Naive Bayes classiﬁer with smoothing provided by a Beta-distributed prior with a cross-validated
concentration parameter.
5. LDA: a regularized Linear Discriminant Analysis classiﬁer, following [48]. Singular value decompo-
sition (SVD), a dimensionality reduction technique, is ﬁrst used to reduce any rank-deﬁciency, after which
the covariance matrix is shrunk toward a diagonal, equal-variance structured estimate. The shrinkage
parameter is determined by cross-validation.
6. dLDA: a ‘diagonal’ LDA, where only the diagonal entries of the covariance matrix are estimated
and the oﬀ-diagonal entries are set to 0. A cross-validated parameter determines shrinkage toward a
diagonal, equal-variance estimate. This classiﬁer can oﬀer a more robust estimate of feature variances; it
is equivalent to a Naive Bayes classiﬁer with Gaussian features [49].
Generally, linear classiﬁers fall into one of two types. Classiﬁers of the ﬁrst type — sometimes called
‘naive’ in the literature, which in our case include VTT, dLDA, and Naive Bayes — learn feature weights
without considering feature covariances. While covariance information can be useful for distinguishing
classes, naive classiﬁers often perform well with small amounts of training data, when covariances are
diﬃcult to estimate accurately. Classiﬁers of the second type — which we refer to as ‘non-naive’, and
which in our case included SVM, LDA, and Logistic Regression — do consider feature covariances (often
in combination with regularization techniques to smooth covariance estimates) and can achieve superior
performance when provided with suﬃcient training data.
Feature Transforms
For both unigram and bigram runs, we evaluated classiﬁcation performance on several transforms of the
document matrices:
1. No transform: raw binary occurrence matrices (see section “Abstract Corpus”).
2. IDF: occurrences of feature i were transformed to its Inverse Document Frequency (IDF) value:
idf (i) = log
N
ci+1, where ci is the total number of occurrences of feature i among all documents. This
reduced the inﬂuence of common features on classiﬁcation.
3. TFIDF: the Term Frequency, Inverse Document Frequency transform (TFIDF); same as above,
but subsequently divided by the total number of features that occur in each document. This reduced the
impact of document size diﬀerences.
4. Normalization: the non-transformed, IDF, and TFIDF document matrices underwent a length-
normalization transform, where each document vector was inversely scaled by its L2 norm. L2 normal-
ization has been argued to be important for good SVM performance [50].
5. PCA: The above matrices were run through a Principal Component Analysis (PCA) dimensionality
reduction step. Projections onto the ﬁrst 100, 200, 400, 600, 800, and 1000 components were tested.
Feature transforms can improve classiﬁcation performance by making the surfaces that separate doc-
uments in diﬀerent classes more linear and by decreasing the weight of non-discriminating features. PCA,
on the other hand, reduces the number of parameters that need to be estimated from training data. If
class membership information is contained in the subspace spanned by the largest principal components,
then this kind of dimensionality reduction can improve generalization performance by reducing noise and
model complexity.


## Page 7


7
Performance evaluation
The abstract and sentence corpora described above were used both for training classiﬁers and for es-
timating generalization performance on out-of-sample documents. In order to estimate out-of-sample
performance, we used the following cross-validation procedure for each possible classiﬁer and feature
transform:
1. Each corpus was randomly partitioned into 4 document folds (75%-25% splits). This was repeated
4 times, yielding 16 outer folds. All classiﬁers and transforms were evaluated using the same partitions.
2. For each fold, the 75% split was treated as the ‘training’ split and the 25% split was treated as
the ‘testing split’. If a feature transform was used, it was applied to both splits but was computed using
statistics (such as IDF or principal components) from the training split. Finally, classiﬁers were trained
on the training split and evaluated based on their prediction performance on the testing split.
3. Measures of classiﬁcation performance (see below) on the testing split were collected. The 16 sets
of performance measures were averaged to produce an estimate of generalization performance.
Because training and testing documents are always separated, for each cross-validation fold the above
procedure is equivalent to calculating performance on an independent testing corpus.
Except for VTT, the classiﬁers listed in section “Classiﬁers” used cross-validated regularization pa-
rameters. These parameters were not chosen using cross-validation on the outer folds because this would
lead to a biased estimate of out-of-sample performance. Instead, regularization parameters were chosen
using nested cross-validation within each of the 75% blocks of the above outer folds:
1. The 75%-block was itself partitioned into 4 folds (75%-25% splits of the outer 75% block). This is
repeated 4 times, producing a total of 16 inner folds for each outer fold training split.
2. Over a range of values of the cross-validated parameter, the procedure described in step 2 above
was used, but now applied to the 75%/25% splits of each inner fold. Mean performance on inner fold
testing splits were measured using the Matthews Correlation Coeﬃcient [51] (MCC), which is particularly
well-suited for the unbalanced scenarios of our corpora [52].
3. The parameter value giving the highest mean MCC was chosen as the regularization parameter
value for training the classiﬁer in the outer fold.
We evaluated the performance of the classiﬁers using three diﬀerent measures: the balanced F1 score
(the harmonic mean of precision and recall), the iAUC or ‘area under the interpolated precision/recall
curve’ [53], and the MCC. In addition, we computed and reported the rank product of these three
measures (RP3) as a single inclusive metric of classiﬁcation performance. The RP3 measure provides a
well-rounded assessment of classiﬁer performance, as it combines the ranking of the diﬀerent individual
measures [12,41].
For displaying results, we focus primarily on the iAUC measure (in cases where only plots of iAUC
performance are provided, F1 and MCC plots are found in the Supporting Information, S1 Text). iAUC
does not depend on predicted class assignments but rather on the ranking of test set documents ac-
cording to classiﬁer conﬁdence scores from most relevant to most irrelevant. iAUC oﬀers three major
advantages as a measure of classiﬁcation performance. First, it provides a more comprehensive measure
of classiﬁer performance because it evaluates the entire ranking of documents, as opposed to just class
assignments. Second, iAUC is less sensitive to variation driven by random-sampling diﬀerences in the
training corpus, which may lead to ﬂuctuations in the class assignments of low conﬁdence documents
and, correspondingly, high variability in measures such as F1 and MCC. Finally, it is more relevant
in a frequently-encountered situation where a human practitioner uses a BLM pipeline to retrieve only
the most relevant documents (which should have high positive-class conﬁdence scores) or to identify
likely-to-be-misclassiﬁed documents (which should have low conﬁdence scores).
Both the abstract and sentence classiﬁcation tasks are characterized by imbalanced datasets, with
more relevant-class abstracts and more irrelevant-class sentences respectively. For simplicity, and because
we are primarily concerned how ranking performance (as measured by iAUC) changes between diﬀerent
machine learning conﬁgurations on the same dataset, we do not perform resampling or re-weighting


## Page 8


8
of training items. We also report MCC values, a measure which is known to be stable in the face of
unbalanced classes [52].
The performance of a classiﬁer and feature transform conﬁguration varies both due to random sampling
of folds and due to the inherent performance bias of the conﬁguration over the entire distribution of folds.
Since we are only interested in the latter, observed performance diﬀerences between pairs of conﬁgurations
were tested for statistical signiﬁcance using a non-parametric paired-sample permutation test.
First,
the assignments of performance scores for each of the 16 outer folds were permuted between the two
classiﬁer/transform conﬁgurations under consideration. For each of the 216 possible permutations, the
diﬀerence in across-fold mean performance was calculated; this formed the distribution of performance
diﬀerences under the null hypothesis that the two conﬁgurations have equal performance. Finally, the
p-value was computed as the probability (one- or two-tailed, as indicated) of observing a diﬀerence under
the null hypothesis distribution equal to or greater than the actual diﬀerence.
Results
Abstract classiﬁcation performance
Fig. 2 shows classiﬁer performance on the abstract task for the unigram and bigram runs with no feature
transform applied.
The best classiﬁer conﬁguration, as well as those conﬁgurations not signiﬁcantly
diﬀerent from the best (p>0.05, one-tailed test), are marked with an asterisk. In addition, the performance
results, ranks, and the rank-product (RP3) measure are reported in Table 1. The best classiﬁer achieves
F1≈0.93, iAUC≈0.98, MCC≈0.73, which constitutes a substantial and signiﬁcant improvement over our
previous preliminary results reported in [39], where we had reached F1≈0.8, iAUC≈0.88, MCC≈0.6
(notice that these performance values would be well below the lowest reported levels in Fig. 2). This
demonstrates that the corpus used in this work — which is more carefully curated and now also considers
interactions between drugs and food, fruit, smoking, alcohol, and natural products to be relevant (details
in “Materials and Methods Section”) — improves the classiﬁcation of abstracts with pharmacokinetic
evidence of DDI. The levels of performance achieved are excellent when compared to similar abstract
classiﬁcation tasks in other biomedical domains. For instance, in the BioCreative Challenge III, considered
one of the premier forums for assessment of text mining methods, the best classiﬁers of abstracts with
Protein-Protein Interaction yielded performances of F1≈0.61, iAUC≈0.68, MCC≈0.55 [17]. Naturally,
our results are not directly comparable to results obtained on diﬀerent corpora and on a diﬀerent problem;
rather, these numbers provide guidance on what is typically considered good results in biomedical article
classiﬁcation.


## Page 9


9
Figure 2. Classiﬁcation performance on abstracts: Performance for both unigram and bigram
runs on non-transformed features. Left: F1 measure. Middle: MCC measure. Right: iAUC measure.
The best classiﬁer conﬁguration, and conﬁgurations not signiﬁcantly diﬀerent (p>0.05, one-tailed test)
from it, marked with asterisk ‘*’.
Classiﬁer
Type
F1
MCC
iAUC
RP3
LDA
Bigram
.931 (1)
.728 (1)
.984 (1)
1
Log Reg
Bigram
.929 (2)
.698 (3)
.984 (1)
6
SVM
Bigram
.928 (3)
.693 (4)
.983 (3)
36
LDA
Unigram
.926 (6)
.719 (2)
.983 (3)
36
Log Reg
Unigram
.927 (4)
.689 (5)
.980 (6)
120
SVM
Unigram
.927 (4)
.689 (5)
.980 (6)
120
Naive Bayes
Bigram
.920 (7)
.661 (10)
.981 (5)
350
Naive Bayes
Unigram
.919 (8)
.672 (7)
.978 (9)
504
VTT
Bigram
.919 (8)
.656 (12)
.980 (6)
576
VTT
Unigram
.918 (10)
.662 (9)
.977 (10)
900
dLDA
Bigram
.909 (11)
.670 (8)
.975 (11)
968
dLDA
Unigram
.908 (12)
.658 (11)
.974 (12)
1584
Table 1. Classiﬁcation performance on abstracts: Performance for both unigram and bigram
runs on non-transformed features according to F1, MCC, and iAUC performance measures. The rank of
the classiﬁers according to each measure is reported in parenthesis in the respective column. Classiﬁers
are ordered according to the rank product (RP3) of the three measures (last column).
For each classiﬁer, the inclusion of bigram features improved performance according to the RP3
measure. The best classiﬁer according to all measures was LDA using bigrams. The performance of this
classiﬁer was signiﬁcantly better than all others for the MCC, but not signiﬁcantly better that Logistic
Regression according to iAUC, and not signiﬁcantly better that Logistic Regression and SVM according to
F1 score. According to RP3, these three classiﬁers using bigrams yield the best performance. Naive Bayes,
VTT, and dLDA — classiﬁers that make a ‘naive’ independence assumption about features (see “Materials
and Methods” section) — performed below the top three. However, the performance levels they achieved
are still quite high, which indicates that such simple classiﬁers are also capable of classifying documents
with pharmacokinetic DDI evidence in our corpus. The in-house VTT classiﬁer is the only classiﬁer
among these that does not use cross-validated parameters; when used with NER features and cross-
validated parameters (the conﬁguration for which it was originally designed [12,41,42]), its performance
improved (see below).


## Page 10


10
Feature Transforms and Dimensionality Reduction
The diﬀerent feature transforms and PCA-based dimensionality reductions (section “Materials and Meth-
ods”) signiﬁcantly improved performance for several classiﬁers, though they could not beat the perfor-
mance of the best non-transformed classiﬁer. Details are provided in Supporting Information (section
1.1 in S1 Text). To summarize, according to most measures only dLDA and SVM improved performance
signiﬁcantly with either an IDF or TFIDF transform plus L2 normalization and dimensionality reduction
(top n principal components). For instance, the best iAUC for SVM (0.984) occurs with a dimensionality
reduction to the top 800 principal components and no feature transform; this is a signiﬁcant improvement
over the no-transform, no dimensionality reduction SVM classiﬁer reported in Table 1 and Fig. 2, but not
a signiﬁcant improvement over the overall best classiﬁers reported there (LDA and Logistic regression).
The dLDA classiﬁer signiﬁcantly improves its iAUC performance with almost all feature transform and
dimensionality reduction combinations, but not above that of the top performing classiﬁers. We conclude
that feature transforms and dimensionality reduction does not lead to the best classiﬁcation performance
on the abstract task.
Pharmacokinetics DDI Features in abstract classiﬁcation
We looked at which textual features play the largest role in the abstract classiﬁcation task. A linear
classiﬁer separates document classes with a hyperplane deﬁned by a set of feature coeﬃcients.
The
impact of a feature on classiﬁcation is quantiﬁed by the sign and amplitude of its hyperplane coeﬃcient. A
feature with a large positive coeﬃcient contributes strongly to a document’s propensity to be classiﬁed as
relevant, while a feature with a large negative coeﬃcient contributes strongly to a document’s propensity
to be classiﬁed as irrelevant. In Table 2, we show the top 20 most distinctive features of the relevant
and irrelevant classes in the abstract task, as chosen in the bigrams runs by the LDA classiﬁer (left) and
Logistic Regression classiﬁer (right), the two top-performing classiﬁers in this task according to the RP3
measure (see Table 1). Notice that textual features are stemmed.


## Page 11


11
LDA (Bigram)
Relevant
Irrelevant
MeSH:Drug Interactions
area
interact
rate
inhibit
diﬀer
interact between
polymorph
oral
activ
day
genotyp
decreas
higher
receiv
patient with
mg
conclus
increas
to the
auc
Substance:Hydrocarb. Hydroxylas.
inhibitor
that the
MeSH:Male
lower
treatment
patient
chang
allel
increas the
among
dure
extens
on the
MeSH:Female
alon
of the
combin
analysi
Logistic Regression (Bigram)
Relevant
Irrelevant
MeSH:Drug Interactions
area
interact
rate
inhibit
diﬀer
interact between
MeSH:Reference Values
oral
activ
decreas
that the
mg
conclus
Substance:Enzyme Inhibitors
clearanc of
receiv
higher
auc
patient
determin
MeSH:Female
treatment
patient with
day
MeSH:Injections, Intravenous
inhibitor
polymorph
chang
genotyp
dure
MeSH:Phenotype
alon
among
MeSH:Male
healthi subject
administ
MeSH:Half-life
chang in
lower
Table 2. Top 20 relevant and irrelevant abstract features: The stemmed textual features most
discriminative of relevant and irrelevant classes on the abstract task, as chosen by two of the
top-performing classiﬁers according to the RP3 measure: LDA with bigrams (left) and Logistic
Regression with bigrams (right).
Some of the most relevant features come from MeSH term metadata (such as the MeSH term Drug
interactions) and terms that explicitly indicate interactions (‘interact’, ‘inhibit’, ‘interact between’, ‘de-
creas’, ‘increas’). Other relevant terms deal with administration protocols and study design (‘oral’, ‘day’,
‘receiv’, ‘mg’, ‘treatment’, ‘alon’, ‘combin’). Some of the irrelevant features concern genetics terminology
(‘allel’, ‘genotyp’, ‘polymorph’, and MeSH term Phenotype), indicating that the irrelevant class was en-
riched with genetics or pharmacogenetics vocabulary. Several generic biomedical terms (such as ‘patient’,
‘healthi subject’, ‘higher’) terms are also highly irrelevant. In addition, highly irrelevant features also
contain some non-DDI-speciﬁc pharmacokinetic terms (for example, ‘area’, ‘rate’, ‘clearance of’), which is
not surprising given that both relevant and irrelevant articles were drawn from pharmacokinetics-related
literature. One surprising result is the observation that while the MeSH term Male is one of the top
relevant features, the MeSH term Female is one of the top irrelevant features. We have no explanation
for the cause of this gender imbalance since the corpus was built from automatic searches to PubMed
without any gender-speciﬁc query terms.
Further analysis of highly relevant and irrelevant features across all classiﬁers and feature transforms
was performed and reported in the Supporting Information (section 1.2 in S1 Text).
We quantiﬁed
and plotted the contribution of standardized coeﬃcients [54] of diﬀerent features and show the most
positively and negatively loaded features for diﬀerent classiﬁer and transform conﬁgurations. Top tex-
tual features obtained from all classiﬁers include additional terms falling under the categories described
above, with features derived from PubMed metadata (MeSH, chemical substances) also appearing among
both the most relevant and irrelevant sets. Other relevant MeSH terms, besides Drug Interactions, in-
clude Cimetidine/pharmacology, Cross-Over Studies, Enzyme Inhibitors/PK, Kinetics, and Proton Pump
Inhibitors. Additionally, a PubMed author entry corresponding to a prominent researcher in the phar-
macokinetics DDI ﬁeld (‘PJ Neuvonen’) appears as highly relevant, as well as three substances from
the RN ﬁeld (see also section “Impact of NER and PubMed metadata on abstract classiﬁcation” below):
Cimetidine, Enzyme Inhibitors, and Proton Pump Inhibitors. For the irrelevant set, additional MeSH


## Page 12


12
(Anti-Ulcer Agents/adm&dos; Injections, Intravenous; Phenotype; Protein Binding; Reference Values)
and Substance terms also appear (Anti-ulcer agents; Hydrocarb. Hydroxylas). The Supporting Informa-
tion S1 Text contains details of the analysis and lists of features. It also shows the results of a Principal
Component Analysis of feature weight coeﬃcients chosen by diﬀerent classiﬁers.
Impact of NER and PubMed metadata on abstract classiﬁcation
We have previously demonstrated improved classiﬁcation performance on protein-protein interaction BLM
tasks by supplementing textual features (such as the word unigram and bigram occurrences) with features
built using Named Entity Recognition (NER) and domain-speciﬁc dictionary tools [12, 41, 42]. To test
if similar techniques are useful in the DDI domain, we counted mentions of named biochemical species
(e.g.
proteins, compounds and drugs) and concepts (e.g.
pharmacokinetic terms) in each document
and then included these counts as document features in addition to the bigram and unigram textual
features. Counts were extracted using biomedical-speciﬁc NER extraction tools and dictionaries, with
dictionary matches identiﬁed by internally-developed software. A preliminary study of the impact of
NER/Dictionary features was reported in [39] using a previous less-reﬁned DDI corpus. Here, in addition
to using the more ﬁne-tuned corpus (see “Methods and Data” section), we study the impact of PubMed
metadata features on classiﬁcation performance. We also provide a new comprehensive analysis of the
performance impact of including features from several publicly-available NER and metadata resources:
• OSCAR4 [55]: NER tool for chemical species, reaction names, enzymes, chemical preﬁxes and
adjectives.
• ABNER [56]: NER tool for genes, proteins, cell lines and cell types.
• BICEPP [57]: NER tool for clinical characteristics associated with drugs.
• DrugBank database [58]: a dictionary list of drug names
• Dictionaries provided by Li’s lab. i-CYPS: cytochrome P450 [CYP] protein names, a group of
enzymes centrally involved in drug metabolism; i-PkParams: terms relevant to pharmacokinetic
parameters and studies; i-Transporters: proteins involved in transport; i-Drugs: Food and Drug
Administration’s drug names. The dictionaries are available for download from [43].
For each of these NER tools and dictionaries, we counted the number of occurrences of any of its en-
tities/entries in a given abstract.
These counts were treated as any other feature for SVM, Logistic
Regression, diagonal LDA, and LDA classiﬁers. Naive Bayes was omitted since NER count features are
non-binary. VTT incorporates NER features via a modiﬁed separating hyperplane equation:
X
i
ϕixi −
X
j
βj −cj
βj
−λ = 0
where xi represents the occurrence of textual feature i, φi and λ are textual feature and bias parameters
as described in section “Classiﬁers”, cj is the count of NER/Dictionary feature from resource j, and βj is
a weight for resource j, which is chosen by cross-validation.
In Fig.
3 (left), we plot the relative iAUC changes over the respective classiﬁers without
NER/Dictionary count features (results for MCC and F1 in Supporting Information; section 1.3 in S1
Text). Signiﬁcant performance changes are indicated with an asterisk (p<0.05, two-tailed test). Some
NER/Dictionary features improved performance signiﬁcantly for several classiﬁers. However, the inclu-
sion of two dictionary features (DrugBank, and i-CYPS) actually decreased performance signiﬁcantly for
several classiﬁers, suggesting that these features contain little class information and instead contribute to
over-ﬁtting. Table 3 lists performance for conﬁgurations in which NER and dictionary features gave a sig-
niﬁcant performance increase for at least one of the three measures (F1, MCC, or iAUC), along with best


## Page 13


13
classiﬁer performance using only textual features (bigram runs). The BICEPP tool consistently yielded
the best improvement for every classiﬁer tested, followed by the i-Drugs dictionary. The OSCAR4 tool
also signiﬁcantly improved the performance of the VTT classiﬁer (especially for the MCC measure as
shown in Supporting Information, S1 Text). With the inclusion of NER and dictionary features, the over-
all top classiﬁers (LDA and Logistic Regression), signiﬁcantly improved their performance, now reaching
F1≈0.93, MCC≈0.74, iAUC≈0.99. Among the set of naive classiﬁers, VTT improved performance sig-
niﬁcantly with the inclusion of NER features, ranking above the other naive classiﬁers according to the
RP3 measure.
Figure 3. Performance impact of abstract NER and metadata features: Left: Relative
changes in iAUC scores on non-transformed bigram runs in combination with diﬀerent NER/Dictionary
features. Signiﬁcant changes (p<0.05, two-tailed test) in performance over the respective classiﬁers
without NER features are indicated with asterisk ‘*’. Right: Relative changes in iAUC when features
from a given PubMed metadata ﬁeld are included versus omitted (while including features from the
other 4 metadata ﬁelds). Signiﬁcant changes (p<0.05, two-tailed test) in performance are indicated
with asterisk ‘*’.


## Page 14


14
Classiﬁer
NER
F1
MCC
iAUC
RP3
LDA
BICEPP
.933 (2)
.737 (1)
.985 (1)
2
LDA
i-Drugs
.934 (1)
.736 (2)
.985 (1)
2
Log Reg
BICEPP
.933 (2)
.714 (3)
.985 (1)
8
Log Reg
i-Drugs
.930 (6)
.700 (6)
.985 (1)
36
LDA
−
.931 (5)
.728 (3)
.984 (5)
75
SVM
BICEPP
.932 (4)
.710 (5)
.984 (5)
100
Log Reg
−
.929 (8)
.698 (7)
.984 (5)
280
SVM
i-Drugs
.930 (6)
.687 (10)
.984 (5)
300
SVM
−
.928 (9)
.693 (8)
.983 (9)
648
VTT
BICEPP
.922 (11)
.692 (9)
.980 (12)
1188
VTT
OSCAR4
.923 (10)
.683 (11)
.979 (14)
1540
VTT
i-Drugs
.920 (12)
.670 (14)
.981 (10)
1680
Naive Bayes
−
.920 (12)
.661 (16)
.981 (10)
1920
dLDA
BICEPP
.911 (15)
.680 (12)
.976 (15)
2700
VTT
−
.919 (14)
.656 (17)
.980 (12)
2856
dLDA
i-Drugs
.911 (15)
.678 (13)
.975 (16)
2700
dLDA
−
.909 (17)
.670 (14)
.975 (16)
3808
Table 3. Abstract classiﬁcation performance using NER features: Performance of the best
classiﬁers when speciﬁc NER and dictionary features are added; original (bigram runs) classiﬁers also
listed with no NER features (indicated by -). F1, MCC, and iAUC performance measures are listed; the
rank of the classiﬁers according to each measure is reported in parenthesis in the respective column.
Classiﬁers are ordered according to the rank product (RP3) of the three measures (last column).
As mentioned, word unigram and bigram features were extracted not only from article abstracts and
titles, but also from ﬁve PubMed metadata ﬁelds: author names, journal titles, MeSH terms, and two
ﬁelds referring to standardized substance names: the ‘registry number/EC number’ [RN] ﬁeld and the
‘secondary source’ ﬁeld [SI]. In fact, some PubMed metadata features were among those most distinguish-
ing of relevant and irrelevant abstracts (for greater detail, see Table 2 and section “Pharmacokinetics DDI
Features in abstract classiﬁcation”, as well Supporting Information; section 1.2 in S1 Text). We tested the
impact of PubMed metadata ﬁelds on abstract classiﬁcation performance. In Fig. 3 (right), we plot the
relative iAUC changes when features from a given PubMed metadata ﬁeld are included versus omitted
(while including features from the other 4 metadata ﬁelds). Signiﬁcant changes (p<0.05, two-tailed test)
in performance are indicated with an asterisk; results for MCC and F1 can be found in Supporting In-
formation (S1 Text). MeSH terms was the only metadata source whose omission decreased performance
signiﬁcantly. However, the performance increase of including MeSH data is rather small. Therefore, the
methodology does not require the availability of human-annotated metadata such as MeSH terms and
can still be deployed on recent articles that have not yet been annotated with MeSH terms.
Evidence sentence extraction performance
Fig. 4 shows classiﬁcation performance on the sentence task of the unigram and bigram runs without any
feature transforms applied, according to F1, MCC, and iAUC measures. The best classiﬁer conﬁguration,
as well as those conﬁgurations not signiﬁcantly diﬀerent from the best (p>0.05, one-tailed test), are
marked with an asterisk. In addition, the numerical results, ranks, and the rank-product (RP3) measure
are reported in Table 4.


## Page 15


15
Figure 4. Sentence classiﬁcation performance: Performance for both unigram and bigram runs
on non-transformed features. Left: F1 measure. Middle: MCC measure. Right: iAUC measure. The
best classiﬁer conﬁguration, and conﬁgurations not signiﬁcantly diﬀerent (p>0.05, one-tailed test) from
it, marked with asterisk ‘*’.
Classiﬁer
Type
F1
MCC
iAUC
RP3
LDA
Bigram
.752 (1)
.642 (1)
.826 (1)
1
LDA
Unigram
.750 (2)
.636 (2)
.819 (4)
16
SVM
Bigram
.736 (3)
.633 (3)
.824 (2)
18
Log Reg
Bigram
.734 (7)
.630 (4)
.823 (3)
84
SVM
Unigram
.735 (6)
.630 (4)
.819 (4)
96
VTT
Bigram
.736 (3)
.617 (8)
.797 (7)
168
Naive Bayes
Unigram
.736 (3)
.617 (8)
.791 (10)
240
Log Reg
Unigram
.734 (7)
.629 (6)
.818 (6)
252
Naive Bayes
Bigram
.734 (7)
.619 (7)
.796 (8)
392
dLDA
Unigram
.732 (11)
.613 (10)
.790 (11)
1210
dLDA
Bigram
.710 (12)
.600 (12)
.794 (9)
1296
VTT
Unigram
.733 (10)
.606 (11)
.789 (12)
1320
Table 4. Sentence classiﬁcation performance: Performance for both unigram and bigram runs on
non-transformed features according to F1, MCC, and iAUC performance measures. The rank of the
classiﬁers according to each measure is reported in parenthesis in the respective column. Classiﬁers are
ordered according to the rank product (RP3) of the three measures (last column).
As with abstracts, including bigram features tended to improve sentence classiﬁcation performance.
LDA performed best, having the highest RP3 and being the best classiﬁer according to the F1 and MCC
measures and one of the two best classiﬁers (along with SVM) on the iAUC measure. Generally, the
classiﬁers that performed well on the sentence task were those that took into account feature covariances:
SVM, Logistic Regression, and LDA. The top classiﬁer (LDA with bigrams) on the evidence sentence
task reached performance of F1≈0.75, MCC≈0.64, iAUC≈0.83.
We measured sentence classiﬁcation performance in combination with diﬀerent feature transforms
and dimensionality reductions (see section 2.1 in Text S1).
In general, the three classiﬁers that do
best on non-transformed features (SVM, Logistic Regression, and LDA) show decreased performance
with dimensionality reduction according to all measures, with more extreme dimensionality reduction
leading to larger performance decreases. On the other hand, for dLDA (a ‘naive’ classiﬁer that treats
features as independent), PCA-based dimensionality reduction — which uses feature covariances to choose
optimal projections — led to signiﬁcant improvements in all measures, with more dimensions giving better
performance. These ﬁndings indicate that the pattern of feature covariance carries important information
about class membership in the sentence task, and that this pattern is distributed across a large number of
dimensions. Generally, the LDA classiﬁer achieved the best performance according to all three measures.


## Page 16


16
Its baseline performance according to the iAUC measure was further improved signiﬁcantly by an IDF-
transform, and — according to the F1 measure — by any transform containing an L2 normalization.
In Table 5, we show the top 20 features most distinctive of the relevant and irrelevant classes in
the sentence task as chosen by the LDA classiﬁer on bigrams (the top performing classiﬁer according
to the RP3 measure; features of other top classiﬁers are not shown because they were highly similar).
Numerical features (indicated by ‘#.#’) were highly indicative of the relevant class, along with expressions
of quantitative changes (‘decreas’, ‘increas’) and interaction (‘inhibit’, ‘catalyz’, ‘interact with’) as well
as adverbs expressing signiﬁcance of evidence (‘signiﬁcantli’). Also highly relevant were features referring
to the area under the concentration-time curve (‘auc’), which is often employed in pharmacokinetics to
measure diﬀerences in drug clearance rates under diﬀerent experimental conditions. Names of several
drugs (‘ketoconazol’, ‘itraconazol’, ‘quiindin’) were relevant in predicting DDI evidence sentences. These
drugs are frequently used probe inhibitors for metabolism enzymes CYP3A4/5, CYP3A4/5 and CYP2D6
respectively and are routinely used in drug interaction studies.
LDA (Bigram)
Relevant
Irrelevant
inhibit
day
increas
investig
#.#
determin
ketoconazol
vitro
decreas
evalu
microm
enzym
rifampin
use
format
diﬀer
catalyz
cytochrom p450
auc
studi
signiﬁcantli
dose
coadministr
examin
itraconazol
measur
quinidin
subject
clearanc
assess
reduc
interact
#.#-fold
compar
show
drug
co-administr
genotyp
interact with
cytochrom
Table 5. Top 20 relevant and irrelevant sentence features: The most discriminative features of
relevant and irrelevant classes in the sentence task, as chosen by the top-performing classiﬁers according
to the RP3 measure: LDA on bigrams.
Highly irrelevant features refer to more generic pharmacokinetic or biomedical concepts such as ‘in-
vestig’, ‘dose’, ‘enzym’, ‘studi’, etc. Interestingly, some terms that are highly relevant in the abstract task
are highly irrelevant in the sentence task (e.g., ‘day’). Notably, the unigram ‘interact’ is highly irrelevant
for sentences, whereas the bigram ‘interact with’ is highly relevant. This may be because all sentences in
this corpus come from abstracts containing pharmacokinetic DDI evidence (see “Materials and Methods”
section). Thus, general administration protocols and drug interaction terms are likely to occur in the
abstract as a whole but not necessarily in the evidence sentences that actually report outcomes of the
pharmacokinetic drug interaction experiments. Similar patterns are observed in the more extensive anal-
ysis provided in Supporting Information (section 2.2 in S1 Text), where relevant and irrelevant features
are analyzed across a wide range of classiﬁer and feature transform conﬁgurations. There we also show
the results of a Principal Component Analysis of feature weight coeﬃcients chosen by diﬀerent classiﬁers.
Finally, we tested the impact of additional features on sentence classiﬁcation. Though there is no


## Page 17


17
metadata available in the sentence corpus, features from NER tools can still be computed. Six NER
features were tested: BICEPP, DrugBank, i-CYPS, i-Drugs, i-PkParams, i-Transporters (see section
“Impact of NER and PubMed metadata on abstract classiﬁcation” for details). As before, we counted
mentions of named biochemical species and concepts speciﬁed by diﬀerent NER tools in each sentence and
then included such counts as sentence features in addition to the bigram and unigram textual features.
Fig. 5 shows relative iAUC changes when features from each of these NER tools were included. Signiﬁcant
improvements (p<0.05, two-tailed test) above the corresponding classiﬁer’s performance without NER
features are indicated by an asterisk; performance according to MCC and F1 measures is shown in
Supporting Information (section 2.3 of S1 Text). Notice that Naive Bayes was omitted since NER count
features are non-binary.
Figure 5. Performance impact of sentence NER features: Relative changes in iAUC scores on
sentence bigram runs (without transforms or dimensionality reductions) in combination with diﬀerent
NER features. Signiﬁcant changes (p<0.05, two-tailed test) in performance over respective classiﬁers
without NER features are indicated with asterisk ‘*’.
As in the abstract task, a few NER/Dictionary features improved performance for several classiﬁers.
The iAUC scores of nearly all classiﬁers were signiﬁcantly improved by three NER features: BICEPP,
DrugBank, and our internally developed i-Drugs dictionary. These three features represent counts of
drugs names, showing that drug name counts are helpful for classifying sentences as DDI-relevant vs.
DDI-irrelevant. Use of features from the BICEPP tool yielded the largest improvement for every classi-
ﬁer. Table 6 lists the performance according to all measures for classiﬁers using the BICEPP features;
also listed are the corresponding best classiﬁers using only textual features (bigram runs). The overall
top classiﬁers (LDA and SVM) showed signiﬁcantly improved performance with the inclusion of these
NER features, reaching F1≈0.76, MCC≈0.65, iAUC≈0.83. In addition, VTT performance improved sig-
niﬁcantly for all three measures with the inclusion of NER features. Here VTT with bigrams performs
better than other naive classiﬁers, as expected given that this classiﬁer was designed speciﬁcally to handle


## Page 18


18
such NER features [12, 41, 42]. In contrast, dLDA (another naive classiﬁer) did not beneﬁt much from
the inclusion of NER features.
Classiﬁer
Type
F1
MCC
iAUC
RP3
LDA
BICEPP
.757 (1)
.650 (1)
.831 (1)
1
SVM
BICEPP
.741 (4)
.639 (3)
.831 (1)
12
LDA
−
.752 (2)
.642 (2)
.826 (4)
16
Log Reg
BICEPP
.738 (5)
.634 (4)
.828 (3)
60
VTT
BICEPP
.742 (3)
.629 (7)
.805 (7)
147
SVM
−
.736 (6)
.633 (5)
.824 (5)
150
Log Reg
−
.734 (8)
.630 (6)
.823 (6)
288
VTT
−
.736 (6)
.617 (8)
.797 (8)
432
Naive Bayes
−
.734 (8)
.619 (8)
.796 (10)
640
dLDA
BICEPP
.711 (10)
.603 (10)
.797 (8)
800
dLDA
−
.710 (11)
.600 (11)
.794 (11)
1331
Table 6. Sentence classiﬁcation performance with NER features: Performance of diﬀerent
sentence classiﬁers with the count features obtained via the BICEPP NER tool; also listed are the
corresponding best classiﬁers using only textual features (bigram runs; indicated by -). F1, MCC, and
iAUC performance measures are listed; the rank of the classiﬁers according to each measure is reported
in parenthesis in the respective column. Classiﬁers are ordered according to the rank product (RP3) of
the three measures (last column).
Discussion
We have demonstrated that current BLM methods for text classiﬁcation can reliably identify PubMed ab-
stracts containing pharmacokinetic evidence of drug-drug interactions, as well as extract speciﬁc sentences
that mention such evidence from relevant abstracts. The performance reached on a corpus of carefully
annotated pharmacokinetics literature is quite high for both abstract classiﬁcation (reaching F1≈0.93,
MCC≈0.74, iAUC≈0.99) and evidence sentence extraction (F1≈0.76, MCC≈0.65, iAUC≈0.83). To ex-
plore the capability of BLM in the pharmacokinetics DDI context, where there are no existing directly-
relevant corpora or experiments, we pursued a thorough comparison of the performance of several linear
classiﬁers using diﬀerent combinations of unigrams, bigrams, PubMed metadata, and NER features. We
also tested the eﬀects of applying feature transforms and dimensionality reduction.
From a classiﬁcation performance perspective, some results are noteworthy: in terms of textual fea-
tures, bigrams in combination with unigrams performed signiﬁcantly better than unigrams alone. How-
ever, performance in unigram versus bigram runs for the same classiﬁer diﬀered by no more than one
percent for iAUC and MCC. Thus, while bigram features did contain some additional information about
class membership, the amount of this information was not large.
In our experiments, feature transforms and PCA-based dimensionality reduction signiﬁcantly im-
proved performance for several classiﬁers (especially “naive” classiﬁers such as dLDA, which assume
feature independence), but did not signiﬁcantly improve the overall best performance. We also found
that a sophisticated version of the LDA classiﬁer dominated performance in both the abstract and sen-
tence tasks. This classiﬁer used SVD to eliminate rank-deﬁciency in the feature occurrence matrices and
performed shrinkage of the feature covariance matrix for regularization (see “Materials and Methods”).
From the drug-interaction domain perspective, feature analysis in the abstract task revealed that
pharmacokinetic DDI evidence in the literature is highly correlated with terms that explicitly indicate
interaction (including MeSH terms), enzyme inhibitors (including substance names via the RN metadata
ﬁeld in PubMed), DDI administration protocols, and study design. At the sentence level, drug interaction
evidence from a pharmacokinetics perspective is highly correlated with terms that express experimental
results, such as numerical values, measures of drug clearance, expressions of quantitative changes, as


## Page 19


19
well as adverbs expressing signiﬁcance of evidence. Feature analysis at the abstract level also revealed
that lack of DDI evidence in the pharmacokinetics literature (irrelevant class) is highly correlated with
some terms from PubMed metadata ﬁelds, as well as those pertaining to genomic or general medical
terminology. At the sentence level, sentences in relevant abstracts but without DDI evidence tend to
include terminology relevant to pharmacokinetics protocols, as well as more generic interaction discourse
or biomedical concepts.
Since many important features came from PubMed metadata ﬁelds, we looked at changes in iAUC
scores when features from diﬀerent PubMed metadata ﬁelds were omitted.
We found that only the
omission of MeSH terms signiﬁcantly aﬀected abstract classiﬁcation performance. Nonetheless, while
statistically signiﬁcant, the drop in performance was rather small (aﬀecting only millesimals of the iAUC,
iAUC≈0.98 without), indicating that abstract classiﬁcation does not depend strongly on the inclusion
of MeSH term features. This is an important consideration since MeSH terms may not be immediately
added to publications, with statistics indicating that only 50% of citations are annotated within 60 days
of inclusion in PubMed [59]. Therefore, classiﬁcation and evidence extraction from brand new articles
should not rely on such metadata.
We also tested the eﬀect of including features extracted using named entity recognition (NER) and
dictionary tools, namely those for detecting possibly-relevant chemical, genomic, metabolomic, drug, and
pharmacokinetic entities. Generally, dictionaries like BICEPP, i-Drugs, and DrugBank, which counted
the number of times drug names appeared, signiﬁcantly improved performance for several classiﬁers on
both the abstract classiﬁcation and evidence sentence extraction tasks (an exception to this was the lack of
improvement on abstracts when including DrugBank features, an eﬀect that needs further investigation).
Nonetheless, as for MESH term features in abstract classiﬁcation, the resulting performance increases
were modest, even if statistically signiﬁcant. This again demonstrates that relevant-class information
can be extracted from abstracts and sentences using solely the statistics of unigram and bigram textual
features.
Notably, relevant and irrelevant documents and sentences both derive from the pharmacokinetics
literature and therefore share similar feature statistics. This makes distinguishing between them a non-
trivial text classiﬁcation problem, though also a more practically relevant one (e.g. for a researcher who
needs to automatically label potentially relevant documents retrieved from PubMed). Nonetheless, sev-
eral classiﬁers reached high performance; for example, the abstract ranking performance (iAUC≈0.99)
has little room for further improvement, though the classiﬁcation performance — while high for this type
of problem — can still be improved.
We observed that many diﬀerent pipeline conﬁgurations reached near-optimal performance. Even
though some performance diﬀerences between conﬁgurations were statistically signiﬁcant, they were small.
For instance, iAUC diﬀerences between best and worst classiﬁers varied by no more than 1 percent in the
abstract task and 5 percent in the sentence task. This demonstrates that classiﬁcation performance in our
experiments was robust to the classiﬁer utilized, and that a BLM pipeline for this problem would do sim-
ilarly well independently of classiﬁer chosen. In particular, while “non-naive” classiﬁers (which consider
feature covariances) performed better than naive classiﬁers, the latter are still capable of competitive
performance. These results suggest a fundamental limit on the amount of statistical signal present in the
labels and feature distributions of the corpora as extractable by linear classiﬁers. However, it is worth
noticing that an analysis of both abstract- and sentence-trained feature weight coeﬃcients shows system-
atic diﬀerences between weights selected by naive and non-naive classiﬁers (see Supporting Information,
S1 Text), indicating that diﬀerent classiﬁers emphasize distinct semantic features. Furthermore, it is
possible that performance could be improved by the use of non-linear classiﬁers or features produced by
more ﬁnely DDI-tuned NER tools, relation extraction or NLP methods, or other sophisticated feature-
generation techniques. Indeed, the larger performance variation observed in the sentence task suggests
that sentence extraction performance may improve with larger amounts of training data (which would
permit better estimates of feature covariances).


## Page 20


20
It is not trivial to compare our performance results with those previously reported in the literature.
First, there is no gold standard for DDI evidence sentence extraction, especially for a speciﬁc evidence-
type such as pharmacokinetics. Second, most sentence extraction tasks in the biomedical domain involve
extraction of passages which can contain several sentences (e.g. the protein-protein interaction subtask in
Biocreative II) or passages relevant for a set of speciﬁc targets (e.g. Gene Ontology annotations for speciﬁc
gene names in Biocreative I [60] and IV [61]). Due to these diﬃculties, the performance on those tasks has
been comparatively low, e.g. in BioCreative IV the best F1 score in the gene ontology evidence extraction
task was 0.27 [61] (in Biocreative II, due to possible overlap and multiple accepted passages, the preferred
performance measure was the mean reciprocal rank which reached 0.87 [12, 62]). Considering that our
performance on the sentence task is higher than what is typically reported for the abstract classiﬁcation in
the biomedical domain (e.g. PPI abstract classiﬁcation in the BioCreative Challenge III reached F1≈0.61,
MCC≈0.55, iAUC≈0.68 [17]), the classiﬁers trained on our sentence corpus reached a very good level of
performance, indicating that the corpus is well annotated and that the task is highly feasible. Given the
performance of our approach in extracting pharmacokinetic evidence, the classiﬁcation methodology and
associated corpus may be useful in the previously explored task of extracting interacting drug pairs from
the literature. For example, it may be more eﬀective to ﬁrst identify DDI sentences containing speciﬁc
types of evidence and then extract the interacting drug names from them, using automated methods or
human expertise tailored to that speciﬁc type of DDI evidence.
To conclude, we provide a thorough report of the capability of linear classiﬁers to automatically
extract pharmacokinetics evidence of DDI from an abstract- and sentence-level annotated corpus. Given
the high performance observed on both abstract and sentence classiﬁcation for all classiﬁers, including
the simplest ones, we conclude that under realistic classiﬁcation scenarios automatic BLM techniques can
identify PubMed abstracts reporting DDI backed by pharmacokinetic evidence, as well as extract evidence
sentences from relevant abstracts. These results are important because pharmacokinetic evidence can be
essential in identifying causal mechanics of putative DDI and as input for further pharmacological and
pharmaco-epidemiology investigation. More generally, our work shows that BLM can be safely included
in DDI discovery pipelines where attention to distinct types of evidence is necessary. In future work, we
intend to use our methodology to mine large corpora for both pharmacokinetic and other types of DDI
experimental evidence. Such evidence can help ﬁll knowledge gaps that exist in the DDI domain, with
the ultimate goal of reducing the incidence of adverse drug reactions and contributing to the development
of alternative safe treatments.
Acknowledgments
The authors thank Shreyas Karnik for help with the preparation of the corpora.
References
1. Becker ML, Kallewaard M, Caspers PWJ, Visser LE, Leufkens HGM, Stricker BHC. Hospitalisa-
tions and emergency department visits due to drug–drug interactions: a literature review. Phar-
macoepidemiol Drug Saf. 2007;16(6):641–651.
2. Hall JM, DeFrances CJ, Williams SN, Golosinskiy A, Schwartzman A. National Hospital Discharge
Survey: 2007 Summary. National Health Statistics Reports. 2010;(29):1–20.
3. Nisha R, Bhuiya F, Xu J. National Hospital Ambulatory Medical Care Survey: 2007 Emergency
Department Summary. National Health Statistics Reports. 2010;(26):1–32.
4. Percha B, Altman RB. Informatics confronts drug-drug interactions. Trends in Pharmacological
Sciences. 2013;34(3):178–184.


## Page 21


21
5. Jankel C, Fitterman L. Epidemiology of drug-drug interactions as a cause of hospital admissions.
Drug safety. 1993;9(1):51.
6. Leape LL, Bates DW, Cullen DJ, Cooper J, Demonaco HJ, Gallivan T, et al. Systems analysis of
adverse drug events. JAMA. 1995;274(1):35–43.
7. Hajjar ER, Caﬁero AC, Hanlon JT. Polypharmacy in elderly patients. Am J Geriatr Pharmacother.
2007;5(4):345–351.
8. Boyce R, Collins C, Horn J, Kalet I. Computing with evidence Part I: A drug-mechanism evidence
taxonomy oriented toward conﬁdence assignment. J Biomed Inform. 2009;42(6):979–989.
9. Boyce R, Collins C, Horn J, Kale I. Computing with evidence Part II: An evidential approach
to predicting metabolic drug-drug interactionComputing with evidence Part II: An evidential ap-
proach to predicting metabolic drug-drug interactions. J Biomed Inform. 2009;42(6):990–1003.
10. Hennessy S, Flockhart DA. The need for translational research on drug-drug interactions. Clinical
Pharmacology and Therapeutics. 2012;91(5):771–773.
11. Tatonetti N, Denny J, Murphy S, Fernald G, Krishnan G, Castro V, et al. Detecting drug interac-
tions from adverse-event reports: interaction between paroxetine and pravastatin increases blood
glucose levels. Clinical Pharmacology & Therapeutics. 2011;90(1):133–142.
12. Abi-Haidar A, Kaur J, Maguitman A, Radivojac P, Retchsteiner A, Verspoor K, et al. Uncovering
protein interaction in abstracts and text using a novel linear model and word proximity networks.
Genome Biology. 2008;9(2):S11.
13. Shatkay H, Feldman R. Mining the biomedical literature in the genomic era: an overview. Journal
of Computational Biology. 2003;10(6):821–855.
14. Jensen LJ, Saric J, Bork P.
Literature mining for the biologist: from information retrieval to
biological discovery. Nature Reviews Genetics. 2006;7(2):119–129.
15. Cohen KB, Hunter L. Getting started in text mining. PLoS Comput Biol. 2008;4(1):e20.
16. Leitner F, Chatr-aryamontri A, Mardis SA, Ceol A, Krallinger M, Licata L, et al. The FEBS Let-
ters/BioCreative II. 5 experiment: making biological information accessible. Nature Biotechnology.
2010;28(9):897–899.
17. Krallinger M, Vazquez M, Leitner F, Salgado D, Chatr-aryamontri A, Winter A, et al.
The
Protein-Protein Interaction tasks of BioCreative III: classiﬁcation/ranking of articles and linking
bio-ontology concepts to full text. BMC bioinformatics. 2011;12(Suppl 8):S3.
18. Rechtsteiner A, Luinstra J, Rocha LM, Strauss CE.
Use of text mining for protein structure
prediction and functional annotation in lack of sequence homology. In: Joint BioLINK and Bio-
Ontologies Meeting (ISMB Special Interest Group); 2006. .
19. McDonald RT, Winters RS, Mandel M, Jin Y, White PS, Pereira F. An entity tagger for recognizing
acquired genomic variations in cancer literature. Bioinformatics. 2004;20(17):3249–3251.
20. El-Shishiny H, Soliman TH, El-Asmar M. Mining drug targets based on microarray experiments.
In: Computers and Communications, IEEE Symposium on. IEEE; 2008. p. 175–181.
21. Segura-Bedmar I, Crespo M, de Pablo-Sánchez C, Martínez P. Resolving anaphoras for the extrac-
tion of drug-drug interactions in pharmacological documents. BMC Bioinformatics. 2010;11(Suppl
2):S1.


## Page 22


22
22. Percha B, Garten Y, Altman R. Discovery and explanation of drug-drug interactions via text
mining. In: Paciﬁc Symposium on Biocomputing; 2012. p. 410.
23. Duke JD, Han X, Wang Z, Subhadarshini A, Karnik SD, Li X, et al. Drug Interaction Prediction
from Literatures and Clinical Signiﬁcance Assessment in Medical Records. PLoS Comput Biol.
2012;8(8):e1002614.
24. Segura-Bedmar I, MartÃŋnez P, de Pablo-SÃąnchez C. A linguistic rule-based approach to ex-
tract drug-drug interactions from pharmacological documents. BMC Bioinformatics. 2011;12(suppl
2):S1.
25. Segura-Bedmar I, MartÃŋnez P, de Pablo-SÃąnchez C. Using a shallow linguistic kernel for drug-
drug interaction extraction. J Biomed Inform. 2011;44(5):789–804.
26. Wu H, Karnik SD, Subhadarshini A, Wang Z, Philips S, Han X, et al. An Integrated Pharmacoki-
netics Ontology and Corpus for Text Mining. BMC Bioinformatics (In Press). 2013;.
27. Segura-Bedmar I, Martınez P, Sánchez-Cisneros D. The 1st DDIExtraction-2011 challenge task:
Extraction of Drug-Drug Interactions from biomedical texts. Challenge Task on Drug-Drug Inter-
action Extraction. 2011;2011:1–9.
28. Segura-Bedmar I, Martínez P, Herrero-Zazo M. Lessons learnt from the DDIExtraction-2013 shared
task. Journal of biomedical informatics. 2014;.
29. Herrero-Zazo M, Segura-Bedmar I, Martínez P, Declerck T. The DDI corpus: An annotated corpus
with pharmacological substances and drug–drug interactions. Journal of biomedical informatics.
2013;46(5):914–920.
30. Gonzalez G, Cohen K, Greene C, Kann M, Leaman R, Shah N, et al.
Text and data mining
for biomedical discovery-session introduction. In: Paciﬁc Symposium on Biocomputing. Paciﬁc
Symposium on Biocomputing. vol. 19; 2013. p. 312–315.
31. Gonzalez G, Cohen KB, Greene CS, Hahn U, Kann MG, Leaman R, et al. Text and data min-
ing for biomedical discovery.
In: Paciﬁc Symposium on Biocomputing. Paciﬁc Symposium on
Biocomputing. World Scientiﬁc; 2012. p. 368–372.
32. Tatonetti NP, Patrick PY, Daneshjou R, Altman RB. Data-driven prediction of drug eﬀects and
interactions. Sci Transl Med. 2012;4(125).
33. DDIExtraction 2011 Task;
2011.
Accessed:
2015-03-04.
http://labda.inf.uc3m.es/
DDIExtraction2011.
34. DDIExtraction 2013 Task;
2013.
Accessed:
2015-03-04.
http://www.cs.york.ac.uk/
semeval-2013/task9/.
35. Wishart DS, Knox C, Guo AC, Cheng D, Shrivastava S, Tzur D, et al. DrugBank: a knowledgebase
for drugs, drug actions and drug targets. Nucleic acids research. 2008;36(suppl 1):D901–D906.
36. Tari L, Anwar S, Liang S, Cai J, Baral C. Discovering drug-drug interactions: a text-mining and
reasoning approach based on properties of drug metabolism. Bioinformatics. 2010;26(18):i547–553.
37. Cheng F, Zhao Z.
Machine learning-based prediction of drug-drug interactions by integrating
drug phenotypic, therapeutic, chemical, and genomic properties. Journal of the American Medical
Informatics Association. 2014;21(e2):e278–e286.


## Page 23


23
38. Wang Z, Kim S, Quinney SK, Guo Y, Hall SD, Rocha LM, et al. Literature mining on pharma-
cokinetics numerical data: A feasibility study. J Biomed Inform. 2009;42(4):726–735.
39. Kolchinsky A, et al. Evaluation of linear classiﬁers on articles containing pharmacokinetic evidence
of drug-drug interactions. Paciﬁc Symposium on Biocomputing. 2013;18:409–420.
40. Wall ME, Rechtsteiner A, Rocha LM.
Singular value decomposition and principal component
analysis.
In: D P Berrar MG W Dubitzky, editor. A Practical Approach to Microarray Data
Analysis. KluwerKluwer: Norwell, MA; 2003. p. 91–109.
41. Lourenço A, Conover M, Wong A, Nematzadeh A, Pan F, Shatkay H, et al. A linear classiﬁer based
on entity recognition tools and a statistical approach to method extraction in the protein-protein
interaction literature. BMC Bioinformatics. 2011;12(Suppl 8):S12.
42. Kolchinsky A, Abi-Haidar A, Kaur J, Hamed AA, Rocha LM. Classiﬁcation of protein-protein in-
teraction full-text documents using text and citation network features. IEEE/ACM Trans Comput
Biol Bioinf. 2010;7(3):400–411.
43. Pharmacokinetic Corpus; 2014.
Accessed:
2015-03-04.
http://rweb.compbio.iupui.edu/
corpus/downloads.html.
44. Porter MF. An algorithm for suﬃx stripping. Program. 1980;14(3):130–137.
45. Bishop CM. Pattern Recognition and Machine Learning. Springer; 2006.
46. Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, et al. Scikit-learn: Machine
Learning in Python . JMLR. 2011;12:2825–2830.
47. Fan RE, Chang KW, Hsieh CJ, Wang XR, Lin CJ. LIBLINEAR: A library for large linear classi-
ﬁcation. JMLR. 2008;9:1871–1874.
48. Ye J, Xiong T, Li Q, Janardan R, Bi J, Cherkassky V, et al. Eﬃcient model selection for regu-
larized linear discriminant analysis. In: Proceedings of the 15th ACM international conference on
Information and knowledge management. ACM; 2006. p. 532–539.
49. Bickel PJ, Levina E. Some theory for Fisher’s linear discriminant function, ‘naive Bayes’, and some
alternatives when there are many more variables than observations. Bernoulli. 2004;10(6):989–1010.
50. Leopold E, Kindermann J. Text categorization with support vector machines. how to represent
texts in input space? Machine Learning. 2002;46(1):423–444.
51. Matthews BW, et al. Comparison of the predicted and observed secondary structure of T4 phage
lysozyme. Biochimica et biophysica acta. 1975;405(2):442.
52. Baldi P. Assessing the accuracy of prediction algorithms for classiﬁcation: an overview. Bioinfor-
matics. 2000 May;16(5):412–424.
53. Davis J, Goadrich M. The relationship between Precision-Recall and ROC curves. In: Proc of the
23rd International Conference on Machine Learning. ACM; 2006. p. 233–240.
54. Agresti A. An introduction to categorical data analysis. vol. 423. Wiley-Interscience; 2007.
55. Jessop DM, Adams SE, Willighagen EL, Hawizy L, Murray-Rust P. OSCAR4: a ﬂexible architec-
ture for chemical text-mining. J Cheminf. 2011;3(1):1–12.


## Page 24


24
56. Settles B. ABNER: an open source tool for automatically tagging genes, proteins and other entity
names in text. Bioinformatics. 2005;21(14):3191–3192.
57. Lin F, Anthony S, Polasek T, Tsafnat G, Doogue M.
BICEPP: an example-based statistical
text mining method for predicting the binary characteristics of drugs.
BMC Bioinformatics.
2011;12(1):112.
58. Wishart DS, Knox C, Guo AC, Shrivastava S, Hassanali M, Stothard P, et al. DrugBank: a compre-
hensive resource for in silico drug discovery and exploration. Nucleic Acids Research. 2006;34(suppl
1):D668–D672.
59. Huang M, Névéol A, Lu Z. Recommending MeSH terms for annotating biomedical articles. Journal
of the American Medical Informatics Association. 2011;18(5):660–667.
60. Hirschman L, Yeh A, Blaschke C, Valencia A. Overview of BioCreAtIvE: critical assessment of
information extraction for biology. BMC bioinformatics. 2005;6(Suppl 1):S1.
61. Mao Y, Van Auken K, Li D, Arighi CN, Lu Z. The gene ontology task at biocreative IV. In:
Proceedings of the Fourth Biocreative Challenge Evaluation Workshop. vol. 1; 2013. p. 119–127.
62. Krallinger M, Leitner F, Rodriguez-Penagos C, Valencia A, et al. Overview of the protein-protein
interaction annotation extraction task of BioCreative II. Genome biology. 2008;9(Suppl 2):S4.


## Page 25


Extraction of Pharmacokinetic Evidence of Drug-drug
Interactions from the Literature:
SUPPORTING INFORMATION
Artemy Kolchinsky, Anália Lourenço, Heng-Yi Wu, Lang Li, Luis M. Rocha
1
Abstract performance
The following table lists classiﬁcation performance according to F1, MCC, iAUC, and Accuracy measures
for diﬀerent classiﬁers on unigram and bigram abstract runs. It includes the VTTcv classiﬁer (VTT with a
cross-validated threshold), which is not discussed in the main article.
Classiﬁer
Type
F1
MCC
iAUC
Accuracy
Log Reg
Bigram
.929
.698
.984
.891
Log Reg
Unigram
.927
.689
.980
.888
Naive Bayes
Bigram
.920
.661
.981
.878
Naive Bayes
Unigram
.919
.672
.978
.878
SVM
Bigram
.928
.693
.983
.890
SVM
Unigram
.927
.689
.980
.888
VTTcv
Bigram
.916
.697
.980
.877
VTTcv
Unigram
.911
.663
.977
.868
dLDA
Bigram
.909
.670
.975
.868
dLDA
Unigram
.908
.658
.974
.865
LDA
Bigram
.931
.728
.984
.897
LDA
Unigram
.926
.719
.983
.891
VTTcv
Bigram
.916
.697
.980
.877
VTTcv
Unigram
.911
.663
.977
.868
VTT
Bigram
.919
.656
.980
.876
VTT
Unigram
.918
.662
.977
.876
1


## Page 26


1 Abstract performance
2
1.1
Abstract performance: Feature transforms and dimensionality reduction
The following charts show iAUC, F1, and MCC performance on abstract bigram runs when feature trans-
forms and dimensionality reductions are applied. Stars indicate conﬁgurations that performed signiﬁcantly
better (p<0.05, one-tailed test) than the no-transform, no-dimensionality-reduction conﬁguration of the same
classiﬁer (indicated with larger circles). Naive Bayes was not tested since it is only applicable to binary data,
and VTT was only tested on the sparse transforms (i.e., without PCA-based dimensionality reduction).
-
IDF+
Norm
IDF
Norm
TFIDF+
Norm
TFIDF
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
0.976
0.978
0.980
0.982
0.984
iAUC
Log Reg
SVM
dLDA
LDA
VTT
-
IDF+
Norm
IDF
Norm
TFIDF+
Norm
TFIDF
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
0.86
0.87
0.88
0.89
0.90
0.91
0.92
0.93
F1
Log Reg
SVM
dLDA
LDA
VTT
-
IDF+
Norm
IDF
Norm
TFIDF+
Norm
TFIDF
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
0.55
0.60
0.65
0.70
0.75
MCC
Log Reg
SVM
dLDA
LDA
VTT


## Page 27


1 Abstract performance
3
1.2
Abstract Performance: Most relevant and irrelevant features
A linear classiﬁer separates classes using a hyperplane deﬁned by a set of feature coeﬃcients. The impact of a
given feature on classiﬁcation is naturally quantiﬁed by the sign and amplitude of its hyperplane coeﬃcient.
The increase of the value of a feature with a large positive (negative) coeﬃcient produces a large increase in
a document’s propensity to be classiﬁed as relevant (irrelevant). Coeﬃcients for diﬀerent features are made
comparable by an appropriate normalization: we multiply each feature’s coeﬃcient by the standard devia-
tion of the feature’s values in the training data, producing what is referred to as a ‘standardized coeﬃcient’
in the linear regression literature. For the abstract bigram runs, the following ﬁgure shows the ranks of
the most relevant and the reverse rank of the most irrelevant features. RELEVANT FEATURES includes
any feature whose standardized coeﬃcient was among the top 5 most positive standardized coeﬃcients for
any transform/classiﬁer combination, while IRRELEVANT FEATURES includes any feature whose stan-
dardized coeﬃcient was among the top 5 most negative standardized coeﬃcients for any transform/classiﬁer
combination. Transforms are organized in the vertical columns, while classiﬁers are distinguished by color
and marker style. For relevant (irrelevant) features, markers are positioned according to their rank (reverse
rank) among the most positive (negative) features for a given classiﬁer and transform combination.
RELEVANT FEATURES
-
Author:Neuvonen,PJ
MeSH:Cimetidine/pharmacology
MeSH:Cross-Over Studies
MeSH:Drug Interactions
MeSH:Enzyme Inhibitors/PK
MeSH:Kinetics
MeSH:Proton Pump Inhibitors
Substance:Cimetidine
Substance:Enzyme Inhibitors
Substance:Proton Pump Inhibitors
alon
alon and
cimetidin mg
cimetidin treatment
coadministr
coadministr of
crossov studi
day
decreas
drug interact
inhibit
inhibit the
interact
interact between
mg
of cimetidin
on day
oral
pharmacokinet interact
the interact
100 101 102 103 104
Rank
IDF
100 101 102 103 104
Rank
IDF+Norm
100 101 102 103 104
Rank
Norm
100 101 102 103 104
Rank
TFIDF
100 101 102 103 104
Rank
TFIDF+Norm
100 101 102 103 104
Rank
IRRELEVANT FEATURES
-
MeSH:Anti-Ulcer Agents/adm&dos
MeSH:Injections, Intravenous
MeSH:Phenotype
MeSH:Protein Binding
MeSH:Reference Values
Substance:Anti-ulcer agents
Substance:Hydrocarb. Hydroxylas.
activ
allel
among
area
clearanc of
differ
genet
genet polymorph
genotyp
higher
homozyg
polymorph
rate
skin
that the
variant
wheal
100 101 102 103 104
Rank
IDF
100 101 102 103 104
Rank
IDF+Norm
100 101 102 103 104
Rank
Norm
100 101 102 103 104
Rank
TFIDF
100 101 102 103 104
Rank
TFIDF+Norm
100 101 102 103 104
Rank
Log Reg
dLDA
VTT
SVM
LDA


## Page 28


1 Abstract performance
4
To further compare the importance that diﬀerent classiﬁer/transform combinations gave to diﬀerent
features, we performed principal component analysis on a matrix composed of the hyperplane coeﬃcients
of all such combinations. The following ﬁgure shows each transform-classiﬁer hyperplane in terms of its
loading on the ﬁrst two principal components (PCs). This projection separates classiﬁers that use feature
covariance information (LDA, SVM, and Logistic Regression) and those that don’t (Naive Bayes, dLDA,
VTT). It also groups conﬁgurations according to feature transforms, with conﬁgurations that included
IDF-like transforms clustering separately from those that used no transforms or a simple L2-normalization.
In general, SVM and Logistic Regression produce very similar feature loadings, likely due to the fact that
they optimize similar cost functions during training.
−2
−1
0
1
2
PC 1
−2
−1
0
1
2
PC 2
Log Reg(TFIDF+Norm)
dLDA(TFIDF+Norm)
VTT(TFIDF+Norm)
SVM(TFIDF+Norm)
LDA(TFIDF+Norm)
VTT(-)
dLDA(-)
SVM(-)
Naive Bayes(-)
Log Reg(-)
LDA(-)
Log Reg(TFIDF)
dLDA(TFIDF)
VTT(TFIDF)
SVM(TFIDF)
LDA(TFIDF)
Log Reg(IDF+Norm)
dLDA(IDF+Norm)
VTT(IDF+Norm)
SVM(IDF+Norm)
LDA(IDF+Norm)
Log Reg(IDF)
dLDA(IDF)
VTT(IDF)
SVM(IDF)
LDA(IDF)
Log Reg(Norm)
dLDA(Norm)
VTT(Norm)
SVM(Norm)
LDA(Norm)


## Page 29


1 Abstract performance
5
1.3
Abstract Performance: NER and Metadata Features
The following ﬁgures plot the relative changes in F1 and MCC performance when including vs. not-including
metadata and NER-derived features on abstract bigram runs with feature transforms. Signiﬁcant changes
(p<0.05, two-tailed test) are indicated by asterisks. For metadata, changes in performance are measured
while still including features from the other 4 metadata ﬁelds.
ABNER
BICEPP
DrugBank
OSCAR4
i-CYPS
i-Drugs
i-PkParams
i-Transporters
NER
0.002
0.001
0.000
0.001
0.002
0.003
0.004
∆F1
**
*
Author
Journal
MeSH
RN Field
SI Field
Metadata Field
0.001
0.000
0.001
0.002
0.003
*
Log Reg
SVM
dLDA
LDA
VTT
ABNER
BICEPP
DrugBank
OSCAR4
i-CYPS
i-Drugs
i-PkParams
i-Transporters
NER
0.01
0.00
0.01
0.02
0.03
∆MCC
**
*
*
*
*
*
Author
Journal
MeSH
RN Field
SI Field
Metadata Field
0.005
0.000
0.005
0.010
0.015
*
Log Reg
SVM
dLDA
LDA
VTT


## Page 30


2 Sentence performance
6
2
Sentence performance
The following table lists classiﬁcation performance according to F1, MCC, iAUC, and Accuracy measures
for diﬀerent classiﬁers on unigram and bigram sentence runs. It includes the VTTcv classiﬁer (VTT with a
cross-validated threshold), which is not discussed in the main article.
Classiﬁer
Type
F1
MCC
iAUC
Accuracy
Log Reg
Bigram
.734
.630
.823
.848
Log Reg
Unigram
.734
.629
.818
.847
Naive Bayes
Unigram
.736
.617
.791
.835
Naive Bayes
Bigram
.734
.619
.796
.839
SVM
Unigram
.735
.630
.819
.847
SVM
Bigram
.736
.633
.824
.848
VTTcv
Bigram
.733
.608
.797
.822
VTTcv
Unigram
.729
.608
.789
.831
dLDA
Bigram
.710
.600
.794
.836
dLDA
Unigram
.732
.613
.790
.834
LDA
Bigram
.752
.642
.826
.848
LDA
Unigram
.750
.636
.819
.843
VTTcv
Bigram
.733
.608
.797
.822
VTTcv
Unigram
.729
.608
.789
.831
VTT
Bigram
.736
.617
.797
.836
VTT
Unigram
.733
.606
.789
.822


## Page 31


2 Sentence performance
7
2.1
Sentence performance: Feature transforms and dimensionality reduction
The following charts show the F1 and MCC performance performance on bigram runs when feature trans-
forms and dimensionality reductions are applied. Signiﬁcant improvements (p<0.05, one-tailed test) com-
pared to the same classiﬁer applied to non-transformed data are indicated by stars.
-
IDF+
Norm
IDF
Norm
TFIDF+
Norm
TFIDF
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
0.76
0.77
0.78
0.79
0.80
0.81
0.82
0.83
iAUC
Log Reg
SVM
dLDA
LDA
VTT
-
IDF+
Norm
IDF
Norm
TFIDF+
Norm
TFIDF
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
0.69
0.70
0.71
0.72
0.73
0.74
0.75
0.76
F1
Log Reg
SVM
dLDA
LDA
VTT
-
IDF+
Norm
IDF
Norm
TFIDF+
Norm
TFIDF
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
-
100
200
400
600
800
1000
0.58
0.59
0.60
0.61
0.62
0.63
0.64
0.65
MCC
Log Reg
SVM
dLDA
LDA
VTT


## Page 32


2 Sentence performance
8
2.2
Sentence Performance: Most relevant and irrelevant features
We analyzed which features were most relevant and irrelevant for identifying evidence sentences using the
same methodology as for abstracts (described in section 1.2). In the following ﬁgure, RELEVANT FEA-
TURES includes any feature whose standardized coeﬃcient was among the top 5 most positive standard-
ized coeﬃcients for any transform/classiﬁer combination, while IRRELEVANT FEATURES includes any
whose standardized coeﬃcient was among the top 5 most negative standardized coeﬃcients for any trans-
form/classiﬁer combination. Transforms are organized in the vertical columns, while classiﬁers are distin-
guished by color and marker style. For relevant (irrelevant) features, markers are positioned according to
their rank (reverse rank) among the most positive (negative) features for a given classiﬁer and transform
combination.
RELEVANT FEATURES
-
#.#
#.# #.#
area
area under
auc
concentration-tim curv
curv
decreas
elimin half-lif
half-lif
increas
inhibit
ketoconazol
microm
signiﬁcantli
100 101 102 103 104
Rank
IDF
100 101 102 103 104
Rank
IDF+Norm
100 101 102 103 104
Rank
Norm
100 101 102 103 104
Rank
TFIDF
100 101 102 103 104
Rank
TFIDF+Norm
100 101 102 103 104
Rank
IRRELEVANT FEATURES
-
administ oral
are
crossov
day
determin
dose
enzym
evalu
healthi
intervent
investig
random
research
singl
studi
use
vitro
100 101 102 103 104
Rank
IDF
100 101 102 103 104
Rank
IDF+Norm
100 101 102 103 104
Rank
Norm
100 101 102 103 104
Rank
TFIDF
100 101 102 103 104
Rank
TFIDF+Norm
100 101 102 103 104
Rank
Log Reg
dLDA
VTT
SVM
LDA


## Page 33


2 Sentence performance
9
As in section 1.2, we perform principal component analysis of separating hyperplanes produced by diﬀer-
ent transforms and classiﬁers trained on the sentence corpus. Hyperplanes are generally grouped by classiﬁer
in this projection, with those corresponding to ‘naive’ classiﬁers that do not use feature covariances (VTT,
dLDA, Naive Bayes) clustering separately from those that do (LDA, SVM, Logistic Regression).
−2
−1
0
1
2
PC 1
−2
−1
0
1
2
PC 2
Log Reg(TFIDF+Norm)
dLDA(TFIDF+Norm)
VTT(TFIDF+Norm)
SVM(TFIDF+Norm)
LDA(TFIDF+Norm)
VTT(-)
dLDA(-)
SVM(-)
Naive Bayes(-)
Log Reg(-)
LDA(-)Log Reg(TFIDF)
dLDA(TFIDF)
VTT(TFIDF)
SVM(TFIDF)
LDA(TFIDF)
Log Reg(IDF+Norm)
dLDA(IDF+Norm)
VTT(IDF+Norm)
SVM(IDF+Norm)
LDA(IDF+Norm)
Log Reg(IDF)
dLDA(IDF)
VTT(IDF)
SVM(IDF)
LDA(IDF)
Log Reg(Norm)
dLDA(Norm)
VTT(Norm)
SVM(Norm)
LDA(Norm)


## Page 34


2 Sentence performance
10
2.3
Sentence Performance: Impact of NER Features
The following ﬁgures plot the relative changes in F1 and MCC performance when including vs. not-including
NER-derived features on non-transformed sentence bigram runs. Signiﬁcant changes (p<0.05, two-tailed test)
indicated by asterisks.
BICEPP
DrugBank
i-CYPS
i-Drugs
i-PkParams
i-Transporters
NER
0.001
0.000
0.001
0.002
0.003
0.004
0.005
0.006
∆F1
*
*
*
BICEPP
DrugBank
i-CYPS
i-Drugs
i-PkParams
i-Transporters
NER
0.005
0.000
0.005
0.010
∆MCC
*
*
*
Log Reg
SVM
dLDA
LDA
VTT

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1412_0744v2_extraction_of_pharmacokinetic_evidence_of_drug_drug_interactions_from_the_litera
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1412_0744V2_EXTRACTION_OF_PHARMACOKINETIC_EVIDENCE_OF_DRUG_DRUG_INTERACTIONS_FROM_THE_LITERA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

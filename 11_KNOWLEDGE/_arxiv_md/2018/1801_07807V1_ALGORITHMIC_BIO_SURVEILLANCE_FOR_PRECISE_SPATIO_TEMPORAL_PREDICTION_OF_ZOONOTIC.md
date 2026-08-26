---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.07807v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1801.07807v1_Algorithmic_Bio-surveillance_For_Precise_Spatio-temporal_Prediction_of_Zoonotic_

> Source: 1801.07807v1_Algorithmic_Bio-surveillance_For_Precise_Spatio-temporal_Prediction_of_Zoonotic_.pdf

> Pages: 8

---


## Page 1


1
Algorithmic Bio-surveillance For Precise
Spatio-temporal Prediction of Zoonotic Emergence
Jaideep Dhanoa†
Balaji Manicassamy§
Ishanu Chattopadhyay†‡⋆
†Department of Medicine, University of Chicago, Chicago IL, USA
§Department of Microbiology, University of Chicago, Chicago IL, USA
‡Institute for Genomics & Systems Biology, University of Chicago, Chicago IL, USA
⋆Corresponding Author. (ishanu@uchicago.edu)
Abstract—Viral zoonoses have emerged as the key drivers of re-
cent pandemics. Human infection by zoonotic viruses are either
spillover events – isolated infections that fail to cause a widespread
contagion – or species jumps, where successful adaptation to the
new host leads to a pandemic. Despite expensive bio-surveillance
efforts, historically emergence response has been reactive, and
post-hoc. Here we use machine inference to demonstrate a high
accuracy predictive bio-surveillance capability, designed to pro-
actively localize an impending species jump via automated interro-
gation of massive sequence databases of viral proteins. Our results
suggest that a jump might not purely be the result of an isolated
unfortunate cross-infection localized in space and time; there are
subtle yet detectable patterns of genotypic changes accumulating
in the global viral population leading up to emergence. Using tens
of thosands of protein sequences simultaneously, we train models
that track maximum achievable accuracy for disambiguating host
tropism from the primary structure of surface proteins, and show
that the inverse classiﬁcation accuracy is a quantitative indicator of
jump risk. We validate our claim in the context of the 2009 swine ﬂu
outbreak, and the 2004 emergence of H5N1 subspecies of Inﬂuenza
A from avian reservoirs; illustrating that interrogation of the global
viral population can unambiguously track a near monotonic risk
elevation over several preceding years leading to eventual emer-
gence.
Index Terms—bio-surveillance, Inﬂuenza A, antigenic shift, pandemic
E
MERGING human diseases are often infections caused by
pathogens of animal origin[1], [2] (zoonoses). Identiﬁcation of
high-risk pathogens within animal hosts can be used to pro-
actively trigger mitigation strategies, potentially reducing the
risk of a successful jump to humans. However, our incomplete
understanding of host-pathogen interaction hinders preemptive
recognition of subtle signals that elevate the jump risk. A com-
plex interplay of the standing viral population, animal and human
hosts, environmental and socio-economic factors, make the task
of identifying viruses of high zoonotic or pandemic risk, before
emergence, difﬁcult to uncertain at best.[2]–[9]
Here we present an efﬁcient, data-driven approach to persistent
predictive bio-surveillance. At the core of our approach is an
inference algorithm to estimate dissimilarity between distinct
viral populations, viewed as ensembles of protein sequences.
In contrast to distance calculations in phylogenetic analyses,
where one computes a distance between two individual se-
quences,[10]–[14] here we compute the dissimilarity or distance
between two sequence ensembles. Unlike static distance for-
mulae, our measure adapts to the evolving populations to back
out the most important set of disambiguating residues (features)
for the two populations. Computing, in this manner, the instanta-
neous dissimilarity between the host-speciﬁc viral quasi-species
leads us to a time-varying measure of jump risk. As an example,
we claim that greater the similarity between the population of
human inﬂuenza viruses and those currently prevalent in swines,
higher the possibility of a species jump.
In machine learning parlance, our algorithm trains a classiﬁer:
given two sets of amino acid sequences for a speciﬁc viral
protein corresponding to the two host species, it infers the
optimal set of decision rules that disambiguate the populations
with maximum achievable accuracy. Then, dissimilarity is simply
the inverse accuracy for the learned model. The interpreta-
tion here is the tautology that “similar” objects are harder to
distinguish, and hence lower classiﬁcation accuracy indicates
a higher degree of similarity. The inferred classiﬁer evolves
with time, always distilling the optimal set of disambiguating
rules to separate the populations. This adaptive tracking of the
evolutionary changes, along with the elimination of the choice
of which static distance to use, provides us with a more natural
framework to discern subtle changes across viral populations.
Key Insight
With the application of the inverse classiﬁcation accuracy in
estimating jump risk, we are putting forward (and eventually
validating) a key hypothesis: emergence risk may be estimated
accurately by looking for subtle sequence changes over time
in circulating strains. Underlying conventional post-hoc recon-
struction of emergence pathways, there is the assumption that
species jumps are the result of an unfortunate sequence of anti-
genic shifts — abrupt genetic rearrangements between distinct
strains co-infecting the same host cell, that dramatically alter the
antigenic makeup of the resultant virus. Our hypothesis, if true,
would imply that such reconstructions do not convey a complete
picture of the processes and interactions that foster emergence.
The 2009 pandemic strain (pH1N1) serves as a good exam-
ple. The emergent strain became known as “swine ﬂu”, on
account of pH1N1’s strong similarities with the then circulating
swine inﬂuenza viruses; phylogenetic analyses showed that the
pH1N1 genes clustered with those from swine viruses rather
than the seasonal human ﬂu strains. Further analysis suggested
that pH1N1 resulted from the re-assortment of 2, or even 3,
distinct viruses, namely the Eurasian swine H1N1, and the swine
H1N2; the latter itself having emerged from swine H1N1 and
the triple assortment swine strain trH3N2, which in turn had
contributions from the human H3N2 (related to the Hong Kong
ﬂu epidemic of 1968), and even had similarities to avian strains
circulating in north America.[17], [19] It is generally recognized that
such reconstructions of evolutionary pathways are not unique.
Alternate event sequences might have transpired in practice,
particularly since swine H1-containing viruses regularly spill-
over to humans without causing widespread infections. Addition-
ally, while all pH1N1 genes appear to have originated in swines,
they come from geographically widely distributed ancestors.
arXiv:1801.07807v1  [q-bio.PE]  23 Jan 2018


## Page 2


2
1998 2000 2002 2004 2006 2008 2010 2012 2014 2016
1
1.1
1.2
emergence
Normalized Risk
HA
1998 2000 2002 2004 2006 2008 2010 2012 2014 2016
1
1.02
1.04
1.06
1.08
emergence
HA
1998 2000 2002 2004 2006 2008 2010 2012 2014 2016
1
1.05
1.1
1.15
1.2
emergence
Normalized Risk
NA
1998 2000 2002 2004 2006 2008 2010 2012 2014 2016
1
1.02
1.04
1.06
1.08
emergence
NA
A. Risk indicator for swine inﬂuenza emergence (99% CI)
B. Risk indicator for avian inﬂuenza emergence (99% CI)
2004
2006
2008
2010
2012
2014
0
50
100
Counts
infected
deaths
1
1.02
1.04
1.06
Normalized risk
pred. risk
C. Reported H5N1 incidence (WHO) against predicted risk
(shifted 1 yr into future)
ρ = −0.48
p = 0.04
not signiﬁcant
ρ = 0.36
ρ = 0.56
p = 0.01
D. Correlation of standard deviation at inferred HA features
Fig. 1. Main Results. Automated inference of emergent patterns in host-speciﬁc HA and NA protein sequences (targeting human, swine and avian
hosts) from the Inﬂuenza Research Database (IRD), distills an algorithmic risk predictor for zoonotic emergence for inﬂuenza. Plates A and B
illustrate risk inference for the cases of the 2009 swine ﬂu and the 2004 H5N1 emergence events. In both cases, we see a near monotonic risk
elevation leading up to the event, with multiple years of actionable warning. Importantly, the inference algorithm only uses past information at each
predicted time-point. Except for small variations in accuracy, similar results are obtained for both HA and NA sequences. This is not surprising:
while NA is not directly implicated in cellular entry, it is known to assist in transmission via enabling release of progeny viruses.[15] Our algorithm
is not speciﬁc to inﬂuenza, and is applicable generally for predicting zoonotic emergence. Plate C compares the predicted H5N1 emergence risk
(appropriately scaled) to incidence reported by WHO.[16] We shifted the risk plot by 1 year into future to illustrate the close match, i.e., our prediction
closely pre-empted the overall incidence dynamics (positive correlation of 0.88 (with death counts) with p-value less than 0.0001). Plate D illustrates
the correlation between residue speciﬁc standard deviations for host pairs as they evolve over time, where we use the same set of residues (See
Table 2) as identiﬁed by our algorithm to have predictive value. We note that the swine-human and avian-human correlations are signiﬁcant, while
the avian-human is not; potentially corroborating the idea of domestic pigs as mixing vessels[17], [18] (See Discussion).
One explanation to this ancestral diversity is the possibility that
pH1N1 emerged over a span several years, cryptically circu-
lating in swines before pandemic recognition.[17] Irrespective
of the speciﬁc details, if antigenic shifts are solely responsible
for species jumps, then emergence is precipitated entirely by
chance events; and hence is categorically impossible to predict
— even with vast surveillance efforts. In contrast, our hypothesis
suggests that gradual processes, such as antigenic drift brought
about by point mutations continuously altering the transcribed
proteins over time, play a crucial role; in essence setting up the
stage for the re-assortment event that leads to emergence.
Our risk indicator does not require identiﬁcation of the speciﬁc
originating animal. Global sampling of the host-speciﬁc viral
populations sufﬁces to track the progressive similarity of the
populations, and a near monotonic risk elevation leading up to
the jump. If we need to somehow locate the speciﬁc animal(s)
in which a new virus emerges in time — every time — then, it is
ultimately a losing battle. For example, the 2009 pandemic strain
was isolated in a speciﬁc pig farm months after the ﬁrst reported
human infections.[19] However, if we can reliably estimate jump
risk in space, time and originating species by merely sampling
animals across the globe, and individual members of the host
species are less important, then we shift the odds in our favor.


## Page 3


3
TABLE 1
Classiﬁcation problem setup: Human & Swine Inﬂuenza A Viruses (HA Sequences, standard code for amino acids)
Species
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
· · ·
Swine
S
R
G
L
G
S
G
I
I
T
S
K
A
P
M
D
E
C
D
A
K
· · ·
Swine
S
R
G
L
G
S
G
I
I
T
S
K
A
P
M
D
E
C
D
A
K
· · ·
Swine
F
K
I
R
R
G
K
S
S
I
M
R
S
D
A
P
I
G
K
C
N
· · ·
Swine
G
R
G
L
G
S
G
I
I
T
S
K
A
P
M
D
E
C
D
A
K
· · ·
Swine
G
R
G
L
G
S
G
I
I
T
S
K
A
P
M
D
E
C
D
A
K
· · ·
Human
F
K
I
R
S
G
K
S
S
I
M
R
S
D
A
P
I
G
K
C
K
· · ·
Human
M
E
R
N
A
G
S
G
I
I
I
S
D
T
P
V
H
D
C
N
T
· · ·
Human
M
E
R
N
A
G
S
G
I
I
I
S
D
T
P
V
H
D
C
N
T
· · ·
Human
M
E
R
N
A
G
S
G
I
I
I
S
D
T
P
V
H
D
C
N
T
· · ·
Human
M
E
R
N
A
G
S
G
I
I
I
S
D
T
P
V
H
D
C
N
T
· · ·
TABLE 2
Inferred Predictive Features (Features are numbered in the sequential scheme)
Protein
Inferred Predictive Residues (Features)
Minimal Feature Set
HA
157, 158, 159
205, 207, 208
290, 291, 292
240, 241, 242
77, 78, 137, 400,
401, 402, 545
78, 137, 157, 187
207, 291, 241, 401
site A[20]
site B[20]
site C[20]
site D[20]
offsite
NA
204, 215, 219, 252, 343, 346, 372, 400
22, 48, 51, 81, 84, 97, 126, 140, 141
182, 309, 307, 417
48, 51, 97, 219, 307,
344
close to antigenic sites[15], [21]
offsite
Quantifying Jump Risk For Inﬂuenza A
Inﬂuenza is responsible for one of the most devastating epi-
demics in human history, decimating over 2% of the human
population in the H1N1 Spanish ﬂu outbreak of 1918-1920. In
addition to be implicated in tens of thousands of deaths every
year in US alone from the recurring seasonal ﬂu epidemic,
inﬂuenza continues to emerge again and again in humans from
strains circulating in animals, leading to severe to moderate
spikes in incidence and mortality rates. Two such recent pan-
demics are the 2004 emergence of the highly pathogenic H5N1
avian strain, and the pH1N1 swine ﬂu outbreak of 2009. Given
the fact that all known inﬂuenza subtypes have been isolated
in birds,[22]–[24] and that all pandemics with the exception of the
2009 event were caused by strains of avian origin,[19] surveilling
avian strains is of paramount importance. With the emergence of
pH1N1 with its complicated genetic ancestry causing between
151,700 and 575,400 deaths,[25] it is also imperative that we
closely monitor swines for future emergence. These recent
events, along with the availability of large databases of inﬂuenza
proteins (Inﬂuenza Research Database or IRD[26]), prompted
us to select avian and swine Inﬂuenza A viruses as validation
candidates for our general bio-surveillance algorithm.
Inﬂuenza A is a negative stranded RNA virus with an en-
capsulated segmented genome surrounded by the host cell-
derived lipid membrane. We focus on the two glycoproteins
embedded in the envelope membrane, hemagglutinin (HA) and
neuraminidase (NA), implicated respectively in cellular entry
and release of progeny viruses. Due to their surface exposure,
antigenicity of HA and NA categorizes inﬂuenza A viruses
into 17 currently known subtypes of HA (H1 to H17) and ten
of NA (N1 to N10). With segmented genome facilitating re-
assortment with different strains, the virus is able to emerge with
a new suite of segments and subtypes.[27], [28] We hypothesized
that the chances of these antigenic shifts are modulated, and
foreshadowed, by incipient patterns in the sequences of the
circulating strains. And that these patterns may be distilled from
the IRD via appropriate statistical analyses.
Querying the IRD for all relatively recent and complete HA and
NA sequences, we ended up with 26,635, 7696 and 16,696 HA,
and 22,488, 7662 and 14,205 NA sequences for human, swine
and avian hosts respectively, collected within the 17 year period
between 1999 and 2016. The restriction to this time period arose
from the necessity to have a minimum number of sequences
each year for reliable statistical analysis. With the objective
of modeling the differences between host-speciﬁc strains at
any given point in time, we did not distinguish between anti-
genic subtypes. We expected that our classiﬁcation algorithm to
automatically distinguish residue differences dictating sub-type
categorization if necessary. Additionally, we used sequential
numbering for referring to the residue positions, and did not
attempt to globally align the collected sequences. Not using
a standardized scheme (such as H3 numbering for HA, and
N2 numbering for NA) is driven by the idea that for a large
enough collection of sequences, the random variations at each
sequential position (which would be reduced by aligning to a
reference sequence in the standardized numbering process)
might be key to unraveling important predictive patterns.
A small excerpt of the HA sequences for human and swine
inﬂuenza between residues 275 and 295 (sequential numbering)
is shown in Table 1. For the majority of the residues, there are
variations within each species, as well as across. We asked if,
given a sufﬁciently large set of sequences collected within some
relatively short period of time (1 year), we can train a protein-
speciﬁc classiﬁer that accurately models these subtle patterns
of variation to reliably recognize the host species. We found that
relatively simple decision trees are able to adequately model
the species speciﬁc patterns with high out-of-sample accuracy
reaching 95%-99% (See Fig. 5, plates A-D). For example, a
couple of rules encoded by the decision tree shown in plate B
of Fig. 5 are: if residue 78 is I or K, and residue 292 is N, D or
T, then the HA sequence is from a human host with less than
1% error. On the other hand, if the residue 78 is I or K, and
the residue 292 is K or E, and the residue 400 is V, then the
host is swine with approximately 6% probability of error. The
tree encodes 5 such rules in total, each of which terminates
in a distinct leaf of the tree (the nodes at the bottom layer).
The structure of the inferred tree corresponds to the number
and complexity of the encoded decision rules, which vary with
the time period of collection of the sequences, the host species
involved, and the protein under study.
These decision trees are computed using unbiased recursive
partitioning[29] on sets of host-speciﬁc sequences drawn within
a period of 1 year. We measure model performance on the
training data with in-sample accuracy: which is the fraction of


## Page 4


4
63
67 70
78
122
124
137
144 146
159 (Site A)
172 174
187 (Site D)
192 194
207 (Site B)
226 228
241 (Site D)
276 277 278
292 (Site C)
55 56 57 58
401
A. H3 Numbering (HA)
H3 Numbering
B. HA Features
C. Off-Site Features
D. Top-view
site C
site A
site D
site B
off-site
544
137
78
401
site A
site D
off-site (137)
E. NA Top-view
F. NA Bottom-view
307
343
219
372
400
140
81
126
252
417
219
Fig. 2. Location of Inferred Residues of Predictive Value in 3D
Molecular Structure. As expected, a subset of the inferred residues
are close to known antigenic sites. For HA, the minimal list of such key
features consist of 9 residues, of which 5 correspond to the four classical
antigenic sites A,B,C,D,[20] while the rest are not in regions that generally
contribute to monoclonal antigenicity. We use sequential numbering for
these residues, and since we analyze sequence ensembles, individual
features map to a distribution in the H3 numbering scheme (shown in
Plate A). Plates B-D show our inferred HA features, and plates E-F
show the inferred features for NA. All of our inferred feature are not
surface residues; features 400-402, and 544 for HA, and 22, 48, 51,
97, 182, 204 for NA are not exposed on the surface of the trimer and
tetramer respectively (See Table 2 for complete list of inferred features).
The appearance of these residues are surprising; but too predictive to
be ignored.
correct classiﬁcations on the training data itself once the model
is inferred. We also test performance on data not used during
training, i.e., sets of sequences not from the same time period
within which a particular classiﬁer is trained, by computing the
out-of-sample accuracy.
The key computational challenge here arises from the existence
of many possible alternate choices of decision rule-sets that
disambiguate the host species. This redundancy partially arises
from dependencies among non-colocated residues required for
correct assembly and function.[30] Here we aim to curate the
minimal set of residues that disambiguate the hosts (irrespective
of the time period), and such dependencies imply that numerous
equally accurate sets of rules exist. We solve this issue via
iterative feature depletion: we construct a conditional inference
tree, identify the most important residue (one that has maximum
contribution in classiﬁcation accuracy), delete that feature from
the training algorithm, and re-run the tree inference. As we
continue to iterate in this manner, in each step we compute
the out-of-sample accuracy by applying the learned model on
sequences from all other one year time periods. We stop if
the out-of-sample accuracy falls below 90%, or if we run out of
features. Carrying out this iterated deletion for all time-periods,
we identify a sequence of decision trees, all of which are highly
accurate models of host tropism, irrespective of the time period
of analysis. Charting the number of times each residue appears
as the most important feature, we end up with a small set that
have maximal contribution in recognizing the target host. Once
this set is identiﬁed, we train a random forest classiﬁer[31] with
the residues as features, for each year. The in-sample accuracy
achieved by these forests are then inverted to compute the year-
speciﬁc jump risk. Our results for HA and NA, and for swine-
human and avian-human jumps is shown in Fig. 1 plates A-B.
The overall workﬂow of our algorithm is summarized in Fig. 5
plate E.
We can also restrict our algorithm to only access sequence
data collected from just one country at a time, to construct a
geospatial estimate of the time-varying jump risk (See Fig. 3).
Due to the severe sparsity of sequences in the IRD for many
countries (See Fig. 4 plate E), our geospatial predictions are rel-
atively patchy, incomplete and suffers from widened conﬁdence
intervals. Nevertheless, we are able to pinpoint correctly the time
and place of both the 2004 and 2009 events.
Discussion
To summarize our computational approach, we construct viral
host recognizers (for human, swine and avian Inﬂuenza A) by
using the primary structure of HA and NA proteins, to ﬁrst
identify a minimal set of residues that allow for good out-of-
sample classiﬁcation performance across the years, and then
using this invariant minimal feature set to estimate the maximum
in-sample classiﬁcation accuracy for individual years. Finally,
we interpret this time-varying accuracy as the inverse jump risk
indicator for selected host-pairs.
Viral populations evolve continuously; thus an invariant minimal
set of residues that disambiguate target hosts reﬂect the seats
of fundamental differences in molecular structures driving host-
speciﬁc infection and transmission processes. A known causal
factor is the speciﬁcity of HA binding to avian-like α-2,3-sialic
acid (SA) versus the mamalian-like α-2,6-SA receptors.[18], [32]
Therefore, substitutions in and around the HA Receptor Binding
Site (RBS) possibly could drive host speciﬁcity, and the HA min-
imal residue set we identiﬁed is consistent with this observation.
Structurally, the native HA is trimeric, and each monomer
is comprised of a distal domain of globular shape (HA1),
and a proximal stem anchoring into the viral lipid envelope
(HA2).[20], [33] It is well-recognized that antigenic drift is driven
by the accumulation of amino acid substitutions in HA epitopes
that block SA interaction.[34], [35] The antigenic sites recognized
by monoclonal antibodies with high neutralizing activity, tend to
be similar across subtypes,[33] and are generally categorized


## Page 5


5
Fig. 3. Geo-spatial Emergence Prediction. Our algorithm may be used to geographically localize the emergence risk, by feeding it geographically
stratiﬁed sequence data. The key challenge is the sparsity of sequences from around the world in the IRD, which degrades our accuracy.
Nevertheless, as shown in columns A and B, we correctly localize both the 2004 H5N1 and the 2009 swine ﬂu emergence. Note that we could
not predict the risk elevation in Mexico prior to 2009 due to the extreme sparsity of collected sequences for S. America. Additionally, the algorithm
also predicts correctly the risk elevation in the middle east in 2005 for the avian ﬂu emergence, and the SE Asia in 2009 immediately after the swine
ﬂu outbreak.
into 4 groups (A, B, C, D for H3, and Sa, Sb, Ca, Cb for H1
subtype[33], [36]). This number can change based on the speciﬁc
sub-type.[33] Nevertheless, the residues we identiﬁed for HA
have footprints in all four sites. Namely, in H3 numbering, the
inferred HA minimal feature set consists of residues 144 - 146
(site A, sequential index 159), 172 - 174 and 226 - 228 (site D,
sequential indices 187 and 241), 192-194 (site B, sequential
index 207), and 276-278 (site C, sequential index 292). In
addition to residues within the antigenic sites, 4 other features
appear in the minimal set: residues 63-70 (sequential index 78),
122-124 (sequential index 137), HA2 residue 55-58 (sequential
index 401) and sequential index 544 near the lower end of
the HA2 stem. The locations of these residues is shown in
Fig. 2 plates B-D. The occurrence of residues outside the RBS
is not surprising, as such mutations have been shown to be
determinants of receptor binding speciﬁcity.[37], [38]
Interestingly, not all residues in the minimal set have surface
exposure. Nevertheless, these residues have been identiﬁed to
have important roles in host speciﬁcity. HA-mediated membrane
fusion in acidic environment is necessary for cellular entry,[39]
and human viruses appear to fuse at a lower pH than avian and
swine counterparts.[40]–[45] The residue in HA2 corresponding to
sequential index 401 is near the tip of the fusion peptide, and
substitutions in this region have been observed in experiments
designed to characterize membrane fusion activity and virus sta-
bility.[46] Substitutions in the second HA2 residue at sequential
index 544 has also being implicated in maintenance of thermal
stability,[47] and proper expression of HA in cells.
Our second protein of interest, NA is a homotetramer with
each monomer consisting of a hydrophobic membrane anchor,
a stalk, and a head region with the catalytic and antigenic
domains.[15] NA cleaves SA receptors of host cells to enable


## Page 6


6
2000
2005
2010
2015
0.1
0.2
0.3
Human
Swine
Avian
A. Mean standard deviation over time
(selected features on HA)
2000
2005
2010
2015
0.2
0.4
Hu-Sw
Sw-Av
Av-Hu
B. Mean Shannon Divergence over time
(selected features on HA)
2000
2005
2010
2015
0.1
0.2
0.3
Hu-Sw
Sw-Av
Av-Hu
C. Mean Shannon Divergence over time
(selected features on NA)
1998
2000
2002
2004
2006
2008
2010
2012
2014
2016
101
102
103
104
avian
human
swine
D. Sequences collected over time (complete HA sequences, NA is similar)
2 × 104
E. Geographical distribution (human HA)
Fig. 4. Given the minimal set of predictive features identiﬁed by our algorithm, we computed the variance at these residues for the host-speciﬁc
strain ensembles, as the virus continues to evolve. As shown in plate A, we get a strong and signiﬁcant positive correlation between human and
swine speciﬁc strains, and a signiﬁcant strongly negative correlation between avian and swine speciﬁc strains. the correlation between human and
avian strains was also strongly negative, but not signiﬁcant. Plates B and C show the mean Shannon divergence at the identiﬁed features for each
pair of hosts. We see that for HA, the distance between human-swine and swine-avian roughly remains constant, whereas the distance between
the swine and avian strains continues to diverge. Plate D shows number of sequences collected in the IRD over time, and plate E illustrates the
geospatial imbalance in the database. The imbalance is more severe for swine and avian sequences. Importantly, we control for this imbalance, and
we do not predict risk spikes only for places or times with most sequences.
dissemination of progeny viruses,[48] and an optimal balance
between the HA and NA function is crucial: excess NA hinders
binding of HA to host cell receptors, whereas insufﬁcient NA
function limits viral spread.[49], [50] Similar to HA, NA has pref-
erential speciﬁcity for α-2,3-SA receptors in avian, and α-2,6-
SA receptors in mamalian viruses.[51] As such, the feature set
for NA has major footprints within its known antigenic sites.[21]
Of the initial set of residues identiﬁed, those at 204, 215, 219,
252, 343, 346, 372, 400 are near or at antigenic sites, whereas
those at 22, 48, 51, 81, 84, 97, 126, 140, 141 182, 309, 307,
417 are not. Pruning these residues to a minimal set such that
predictive performance is unaltered, we get a set consisting of
just 6 residues: 48, 51, 97, 219, 307, 344. Of these, 219 and
344 are on antigenic sites. Additionally, 97 is not exposed on
the surface, and 48, 51 are not even on the head region. While
the appearance of these later residues in the minimal feature
set might be surprising, they have signiﬁcant contributions in
prediction accuracy. (See Fig. 2 plates E and F).
The time-varying risk shown in Fig. 1 plates A-B illustrate that
an impending jump can be predicted years in advance from
observing the ever increasing risk elevation. The avian risk indi-
cator compares favorably, with appropriate scaling, against the
WHO report on H5N1 incidence since 2003 (See Fig. 1, plate
C). While, we do not make a direct case that jump risk should
translate to incidence rate, this close match is noteworthy.
We interpret these results suggest that the viral populations
circulating in the respective hosts are continuously interacting,
and driving each other’s molecular evolution. Without such
continuous interaction, it is difﬁcult to see how one would
get a gradual increase instead of the risk spiking just before
emergence. To investigate this claim further, we computed the
mean standard deviation at the residues in the minimal feature
set (for HA) over time (See Fig. 1 plate D and Fig. 4 plate
A). The results show that with respect to this measure the
human and swine strains are strongly and signiﬁcantly positively
correlated (ρ = 0.56, p = 0.01), and the swine and avian and
avian strains are strongly and signiﬁcantly negatively correlated
(ρ = −0.48, p = 0.04). The negative correlation between the
human and avian strains, on the other hand, is not statistically
signiﬁcant. While not conclusive, these results are consistent
with the suggestion that domestic pigs act as mixing ves-
sels.[17], [18] Additionally, these strong correlations also support
the thesis that the circulating strains interact continuously, and
drive antigenic change.
We also computed the time-varying distance between host-
pairs, measured as the average Shannon divergence at the
residues of the minimal sets (for HA, in Fig. 4, plate B and for
NA in Fig. 4, plate C). This distance for HA shows an intriguing
pattern, it appears that the swine strains are equidistant on
average from human and avian strains post 2004, whereas the
avian human distance is increasing. The results are shown with
99% conﬁdence intervals. We hope that these results would
spark new directions of research into the interaction dynamics
of the host-speciﬁc strains.
In summary, the principal contribution of this study is an algo-
rithmic approach to surveillance that exploits subtle patterns
of sequence changes. These results fundamentally challenge
how we think about bio-surveillance: we do not need to seek
out the individual animals in which a chance re-assortment
event gives rise to a pandemic strain, we can carry out random


## Page 7


7
157
157
 KRE
Swine
0.23%
 XG
78
 RE
Human
0.66%
 K
157
 IVEGN
Swine
0.65%
 K
Swine
37.0%
 E
291
 R
Human
0.0%
 SKCD
Human
48.72%
 G
78
Swine
39.71%
 EL
292
 IK
292
 CEK
Human
0.28%
 NDT
Human
17.95%
 C
400
 KE
Swine
6.25%
 V
Human
17.87%
 L
241
78
 ABEGNSX
Avian
3.83%
 D
Human
5.95%
 ELG
402
 IK
Avian
45.66%
 KM
400
 GV
Avian
16.67%
 N
Avian
1.36%
 L
241
78
 BEGNSX
187
 D
Human
4.5%
 EG 78
 IK
Avian
41.84%
 K
Human
42.31%
 I
Avian
1.49%
 XK
Avian
31.1%
 N
A. 2007
B. 2009
C. 2011
D. 2013
I. Querry IRD
for species-speciﬁc
protein sequences
II. Generate
Decision Trees using
Iterated Feature Deletion
III. Identify
Minimal
Feature Set
IV. Train
Random Forest Classiﬁer
with
Minimal Feature Set
Log
In-sample Accuracy
For Each Year
Generate
Risk Indicator Curve
E. Algorithm Steps
Fig. 5. Examples of Inferred Conditional Inference Trees. Plates A-D illustrate conditional inference trees that recognize HA sequences pertaining
to human vs swine (A,B) and human vs avian (C,D) for the respective years 2207,2009,2011, and 2013. The leaf nodes enumerate the majority
class, along with the percentage class error. The colors of the node depict the relative mixture of the host species. The numbers in the non-leaf
nodes denote the residue index (sequential numbering). These decision trees characterize the optimally inferred rules that allow one to decide the
host species given the amino acid sequence. Note that the number of rules vary from tree to tree and over the years. The in-sample accuracy of
these classiﬁers is over 93%, with out-sample accuracy greater than 90% for immediate future. Plate E enumerates a summarized sketch of the
algorithm, along with the key steps. Steps II and IV are the computational bottlenecks.
sampling of the host species globally and still construct an
accurate spatio-temporal picture of jump risk. While this study
focuses on Inﬂuenza A in human, swine and avian hosts, the
basic principles are expected to hold elsewhere: for other host
species, and other zoonotic pathogens.
References
[1]
Taylor, L. H., Latham, S. M. & Woolhouse, M. E. Risk factors for
human disease emergence. Philos. Trans. R. Soc. Lond., B, Biol.
Sci. 356, 983–989 (2001).
[2]
Flanagan, M. L. et al. Anticipating the Species Jump: Surveillance
for Emerging Viral Threats. Zoonoses and Public Health 59, 155–
163 (2012). 15334406.
[3]
Cleaveland, S., Laurenson, M. K. & Taylor, L. H.
Diseases of
humans and their domestic mammals: pathogen characteristics,
host range and the risk of emergence. Philos. Trans. R. Soc. Lond.,
B, Biol. Sci. 356, 991–999 (2001).
[4]
Wolfe, N. D., Daszak, P., Kilpatrick, A. M. & Burke, D. S. Bushmeat
hunting, deforestation, and prediction of zoonoses emergence.
Emerging Infect. Dis. 11, 1822–1827 (2005).
[5]
Holmes, E. C. & Drummond, A. J. The evolutionary genetics of viral
emergence. Curr. Top. Microbiol. Immunol. 315, 51–66 (2007).
[6]
Parrish, C. R. et al.
Cross-species virus transmission and the
emergence of new epidemic diseases. Microbiol. Mol. Biol. Rev.
72, 457–470 (2008).
[7]
Childs, J. E. & Gordon, E. R. Surveillance and control of zoonotic
agents prior to disease detection in humans. Mt. Sinai J. Med. 76,
421–428 (2009).
[8]
Pulliam, J. R. & Dushoff, J. Ability to replicate in the cytoplasm
predicts zoonotic transmission of livestock viruses. J. Infect. Dis.
199, 565–568 (2009).
[9]
Pepin, K. M., Lass, S., Pulliam, J. R., Read, A. F. & Lloyd-Smith,
J. O. Identifying genetic markers of adaptation for surveillance of
viral host jumps. Nat. Rev. Microbiol. 8, 802–813 (2010).
[10] Hannenhalli, S. & Pevzner, P.
Transforming cabbage into
turnip.(polynomial algorithm for sorting signed permutations by
reversals). dept. of computer science and engineering, penn state
university. Tech. Rep., Technical Report CSE-95-004 (1995).
[11] Jean, G. & Nikolski, M.
Genome rearrangements: a correct al-
gorithm for optimal capping. Information Processing Letters 104,
14–20 (2007).
[12] Ozery-Flato, M. & Shamir, R. Two notes on genome rearrange-
ment. Journal of Bioinformatics and Computational Biology 1, 71–


## Page 8


8
94 (2003).
[13] Tesler, G.
Efﬁcient algorithms for multichromosomal genome
rearrangements. Journal of Computer and System Sciences 65,
587–609 (2002).
[14] Shao, M. & Lin, Y. Approximating the edit distance for genomes
with duplicate genes under dcj, insertion and deletion.
BMC
bioinformatics 13, S13 (2012).
[15] Air, G., Els, M., Brown, L., Laver, W. & Webster, R. Location of
antigenic sites on the three-dimensional structure of the inﬂuenza
N2 virus neuraminidase. Virology 145, 237–248 (1985).
[16] (WHO),
W.
H.
O.
Avian
and
other
zoonotic
inﬂuenza.
http://www.who.int/inﬂuenza/human animal interface/2017
10 30 tableH5N1.pdf?ua=1 (2017).
[17] Smith, G. J. D. et al. Origins and evolutionary genomics of the 2009
swine-origin H1N1 inﬂuenza A epidemic. Nature 459, 1122–1125
(2009).
[18] Joseph, U., Su, Y. C., Vijaykrishna, D. & Smith, G. J. The ecology
and adaptive evolution of inﬂuenza A interspecies transmission
(2017).
[19] van der Meer, F. J. U. M., Orsel, K. & Barkema, H. W. The new
inﬂuenza A H1N1 virus: balancing on the interface of humans and
animals. The Canadian veterinary journal = La revue veterinaire
canadienne 51, 56–62 (2010).
[20] Weis, W. et al. Structure of the inﬂuenza virus haemagglutinin com-
plexed with its receptor, sialic acid. Nature (1988). NIHMS150003.
[21] Saito, T. et al.
Antigenicity of the N8 Inﬂuenza A Virus Neu-
raminidase: Existence of an Epitope at the Subunit Interface of
the Neuraminidase.
JOURNAL OF VIROLOGY 68, 1790–1796
(1994).
[22] Fouchier, R. A. et al. Characterization of a novel inﬂuenza A virus
hemagglutinin subtype (H16) obtained from black-headed gulls. J.
Virol. 79, 2814–2822 (2005).
[23] Webster, R. G., Bean, W. J., Gorman, O. T., Chambers, T. M.
& Kawaoka, Y.
Evolution and ecology of inﬂuenza A viruses.
Microbiol. Rev. 56, 152–179 (1992).
[24] Olsen, B. et al. Global patterns of inﬂuenza a virus in wild birds.
Science 312, 384–388 (2006).
[25] Wang, W. et al. Identiﬁcation of critical residues in the hemagglu-
tinin and neuraminidase of inﬂuenza virus H1N1pdm for vaccine
virus replication in embryonated chicken eggs. Journal of virology
87, 4642–9 (2013).
[26] NIH. Inﬂuenza Research Database (IRD). https://www.ncbi.nlm.
nih.gov/genomes/FLU/Database/ (2017).
[27] Ferguson, N. M., Galvani, A. P. & Bush, R. M.
Ecological and
immunological determinants of inﬂuenza evolution.
Nature 422,
428–433 (2003).
[28] Mair, C. M., Ludwig, K., Herrmann, A. & Sieben, C.
Receptor
binding and pH stability
How inﬂuenza A virus hemagglutinin
affects host-speciﬁc virus infection. Biochimica et Biophysica Acta
(BBA) - Biomembranes 1838, 1153–1168 (2014).
[29] Hothorn, T., Hornik, K. & Zeileis, A. Unbiased Recursive Partition-
ing: A Conditional Inference Framework. Journal of Computational
and Graphical Statistics 15, 651–674 (2006).
[30] Myers, J. L. et al. Compensatory hemagglutinin mutations alter
antigenic properties of inﬂuenza viruses. Journal of virology 87,
11168–72 (2013).
[31] Breiman, L. Random Forests. Machine Learning 45, 5–32 (2001).
[32] Li, Y. et al.
Single Hemagglutinin Mutations That Alter both
Antigenicity and Receptor Binding Avidity Inﬂuence Inﬂuenza Virus
Antigenic Clustering. Journal of Virology (2013).
[33] Caton, A. J., Brownlee, G. G., Yewdell, J. W. & Gerhard, W. The
antigenic structure of the inﬂuenza virus A/PR/8/34 hemagglutinin
(H1 subtype). Cell (1982).
[34] Dimmock, N. J. Mechanisms of neutralization of animal viruses. J.
Gen. Virol. 65 ( Pt 6), 1015–1022 (1984).
[35] Knossow, M. & Skehel, J. J. Variation and infectivity neutralization
in inﬂuenza. Immunology 119, 1–7 (2006).
[36] Hensley, S. E. et al. Hemagglutinin Receptor Binding Avidity Drives
Inﬂuenza A Virus Antigenic Drift .
[37] Jayaraman, A. et al. Glycosylation at Asn91 of H1N1 haemagglu-
tinin affects binding to glycan receptors. The Biochemical journal
444, 429–35 (2012).
[38] Imai, M. et al. Experimental adaptation of an inﬂuenza H5 HA con-
fers respiratory droplet transmission to a reassortant H5 HA/H1N1
virus in ferrets. Nature (2012).
[39] Han, X., Bushweller, J. H., Caﬁso, D. S. & Tamm, L. K. Membrane
structure and fusion-triggering conformational change of the fusion
domain from inﬂuenza hemagglutinin. Nat. Struct. Biol. 8, 715–720
(2001).
[40] Shelton, H., Roberts, K. L., Molesti, E., Temperton, N. & Barclay,
W. S. Mutations in haemagglutinin that affect receptor binding and
pH stability increase replication of a PR8 inﬂuenza virus with H5
HA in the upper respiratory tract of ferrets and may contribute to
transmissibility. J. Gen. Virol. 94, 1220–1229 (2013).
[41] Daidoji, T. et al. Avian Inﬂuenza Virus Infection of Immortalized Hu-
man Respiratory Epithelial Cells Depends upon a Delicate Balance
between Hemagglutinin Acid Stability and Endosomal pH. J. Biol.
Chem. 290, 10627–10642 (2015).
[42] Byrd-Leotis, L., Galloway, S. E., Agbogu, E. & Steinhauer, D. A.
Inﬂuenza hemagglutinin (HA) stem region mutations that stabilize
or destabilize the structure of multiple HA subtypes. J. Virol. 89,
4504–4516 (2015).
[43] Galloway, S. E., Reed, M. L., Russell, C. J. & Steinhauer, D. A. In-
ﬂuenza HA subtypes demonstrate divergent phenotypes for cleav-
age activation and pH of fusion: implications for host range and
adaptation. PLoS Pathog. 9, e1003151 (2013).
[44] Beyer, W. E., Ruigrok, R. W., van Driel, H. & Masurel, N. Inﬂuenza
virus strains with a fusion threshold of pH 5.5 or lower are inhibited
by amantadine. Brief report. Arch. Virol. 90, 173–181 (1986).
[45] Scholtissek, C. Stability of infectious inﬂuenza A viruses at low pH
and at elevated temperature. Vaccine 3, 215–218 (1985).
[46] Baumann, J., Kouassi, N. M., Foni, E., Klenk, H.-D. & Matrosovich,
M. H1N1 Swine Inﬂuenza Viruses Differ from Avian Precursors by
a Higher pH Optimum of Membrane Fusion .
[47] Xu, S. et al. Mutations of two transmembrane cysteines of hemag-
glutinin (HA) from inﬂuenza A H3N2 virus affect HA thermal stability
and fusion activity. Virus Genes (2013).
[48] Webster, R., Monto, A., Braciale, T. & Lamb, R.
Textbook of
Inﬂuenza (Wiley, 2013).
[49] Wagner, R., Matrosovich, M. & Klenk, H. D. Functional balance
between haemagglutinin and neuraminidase in inﬂuenza virus
infections. Rev. Med. Virol. 12, 159–166 (2002).
[50] Yen, H. L. et al.
Hemagglutinin-neuraminidase balance confers
respiratory-droplet transmissibility of the pandemic H1N1 inﬂuenza
virus in ferrets. Proc. Natl. Acad. Sci. U.S.A. 108, 14264–14269
(2011).
[51] de Graaf, M. & Fouchier, R. A. Role of receptor binding speciﬁcity
in inﬂuenza A virus transmission and pathogenesis. EMBO J. 33,
823–841 (2014).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1801_07807v1_algorithmic_bio_surveillance_for_precise_spatio_temporal_prediction_of_zoonotic
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1801_07807V1_ALGORITHMIC_BIO_SURVEILLANCE_FOR_PRECISE_SPATIO_TEMPORAL_PREDICTION_OF_ZOONOTIC.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

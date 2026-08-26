---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1510.01006v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1510.01006v2_Monitoring_Potential_Drug_Interactions_and_Reactions_via_Network_Analysis_of_Ins

> Source: 1510.01006v2_Monitoring_Potential_Drug_Interactions_and_Reactions_via_Network_Analysis_of_Ins.pdf

> Pages: 44

---


## Page 1


Monitoring Potential Drug Interactions and Reactions via Network Analysis of
Instagram User Timelines
Rion Brattig Correia1,2, Lang Li3 and Luis M. Rocha1,4,∗
1School of Informatics & Computing, Indiana University,
Bloomington, IN 47408 USA
∗rocha@indiana.edu
2CAPES Foundation, Ministry of Education of Brazil,
Bras´ılia, DF 70040-020, Brazil
3Department of Medical and Molecular Genetics, Indiana University School of Medicine,
Indianapolis, IN 46202 USA
4Instituto Gulbenkian de Ciˆencia,
Oeiras 2780-156, Portugal
Much recent research aims to identify evidence for Drug-Drug Interactions (DDI) and Adverse Drug
reactions (ADR) from the biomedical scientiﬁc literature. In addition to this “Bibliome”, the universe
of social media provides a very promising source of large-scale data that can help identify DDI and
ADR in ways that have not been hitherto possible. Given the large number of users, analysis of
social media data may be useful to identify under-reported, population-level pathology associated
with DDI, thus further contributing to improvements in population health. Moreover, tapping into
this data allows us to infer drug interactions with natural products—including cannabis—which
constitute an array of DDI very poorly explored by biomedical research thus far.
Our goal is to determine the potential of Instagram for public health monitoring and surveillance
for DDI, ADR, and behavioral pathology at large. Most social media analysis focuses on Twitter
and Facebook, but Instagram is an increasingly important platform, especially among teens, with
unrestricted access of public posts, high availability of posts with geolocation coordinates, and images
to supplement textual analysis.
Using drug, symptom, and natural product dictionaries for identiﬁcation of the various types of
DDI and ADR evidence, we have collected close to 7000 user timelines spanning from October 2010 to
June 2015. We report on 1) the development of a monitoring tool to easily observe user-level timelines
associated with drug and symptom terms of interest, and 2) population-level behavior via the analysis
of co-occurrence networks computed from user timelines at three diﬀerent scales: monthly, weekly,
and daily occurrences. Analysis of these networks further reveals 3) drug and symptom direct and
indirect associations with greater support in user timelines, as well as 4) clusters of symptoms and
drugs revealed by the collective behavior of the observed population.
This demonstrates that Instagram contains much drug- and pathology speciﬁc data for public
health monitoring of DDI and ADR, and that complex network analysis provides an important
toolbox to extract health-related associations and their support from large-scale social media data.
Keywords: Complex Network Analysis; Social Media; Drug Interaction; Public Health; Instagram;
relational inference
1. Introduction
The analysis of social media data has recently allowed unprecedented access to collective hu-
man behavior. The new ﬁeld of Computational Social Science has brought together Informatics
and Complex Systems methods to study society via social media and online data in a quanti-
arXiv:1510.01006v2  [cs.SI]  14 Jan 2016


## Page 2


tative manner not previously possible. From studying social protest1 to predicting the Stock
Market,2 most of the work has focused on Twitter—though Facebook 3 and Instagram4 have
also received some attention lately. This approach shows great promise in monitoring public
health, given the ability to measure the behavior of a very large number of human subjects.5
For instance, several studies have shown that social media analysis is useful to track and pre-
dict inﬂuenza spread,5–7 as well as the measurement of depression.8 In particular, the potential
for adverse drug reaction (ADR) extraction from Twitter has been recently demonstrated.9,10
There is still, however, much work to be done in order to fulﬁll the potential of social
media in the monitoring of public health. For instance, analysis of social media data may be
useful to identify under-reported pathology, particularly in the case of conditions associated
with a perceived social stigma, such as mental disorders.11 Given access to an extremely large
population, it is reasonable to expect that social media data may provide early warnings
about potential drug-drug interactions (DDI) and ADR.9 These unprecedented windows into
collective human behavior may also be useful to study the use and potential interactions and
eﬀects of natural products—including cannabis. The pharmacology of such products constitute
an array of DDI and ADR very poorly explored by biomedical research so far, and thus an
arena where social media mining could provide important novel discoveries and insight.
Most work on social media pertaining to public health monitoring that we are aware of
has relied on data from Twitter or Facebook. However, Instagram is an increasingly important
platform, with unrestricted access of public posts, high availability of posts with geolocation
coordinates, and images to supplement textual analysis. While Instagram has been used to
qualitatively observe the type of content people post regarding health situations such as Ebola
outbreaks,12 its potential for large-scale quantitative analysis in public health has not been
established. Instagram currently has more than 300 million users.13 It surpasses Twitter and
Facebook for preferred social network among teens (12-24) in the US. In 2014 there were
approximately more than 64 million active users in the US and this number is to surpass
111 million in 2019.14 Therefore, our goal here is to explore the potential of this very im-
portant social media platform for public health monitoring and surveillance of DDI, ADR,
and behavioral pathology at large. Speciﬁcally, we use literature mining and network science
methods to automatically characterize and extract temporal signals for DDI and ADR from
a sub-population of Instagram users.
We focused on posts and users with mentions of drugs known to treat depression (e.g.
fluoxetine). The methodology developed can be easily replicated for diﬀerent clinical inter-
ests (e.g. epilepsy drugs). The goal is to show that Instagram is a very rich source of data to
study drug interactions and reactions that may arise in a clinical context of choice, and not
depression per se. Using four diﬀerent multi-word dictionaries (drug and pharmacology, natu-
ral products, cannabis, and ADR terminology), we have collected close to 7000 user timelines
spanning from October 2010 to June 2015. We analyzed co-mentions in three distinct time-
windows: monthly, weekly and daily. This allows the potential extraction of ADR and DDI
that manifest at diﬀerent time scales. From this data, we demonstrate that Instagram user
timelines contain substantial data of interest to characterize DDI, ADR, and natural product
use. To explore this data we have developed a monitoring tool to easily observe user-level


## Page 3


timelines associated with drug and symptom terms of interest, which we describe below. To
explore population-level associations at the diﬀerent temporal scales, we compute knowledge
networks that our previous work has shown to be useful for automated fact-checking,15 protein-
protein interaction extraction,16 and recommender systems.17,18 To illustrate the potential of
data-driven, population-level associations, we use spectral methods to reveal network mod-
ules of symptoms and drugs, for instance those involved in psoriasis pathology. Our Instagram
analysis relies on the distance closure of complex networks18 built at distinct time resolutions,
which is a novel development from related approaches to uncover ADR in Twitter.9
2. Data and Methods
We harvested from Instagram all posts containing hashtags that matched 7 drugs known
to be used in the treatment of depression (# posts): fluoxetine (8,143), sertraline
(574), paroxetine (470), citalopram (426), trazodone (227), escitalopram (117), and
fluvoxamine (22). Synonyms were resolved to the same drug name according to DrugBank;19
for instance, Prozac is resolved to fluoxetine, see supporting information (SI) for table of
synonyms used. This resulted in a total of 9,975 posts from 6,927 users, whose complete time-
lines, spanning the period from October 2010 to June 2015, were collected. In total, these
timelines contain 5, 329, 720 posts, which is the depression timeline dataset we analyze below.
A subset of a previously developed pharmacokinetics ontology20 was used to obtain a drug
dictionary. The full ontology contains more than 100k drugs, proteins and pharmacokinetic
terms. Here we used only names of FDA-approved drugs, along with their generic name and
synonyms, resulting in 17,335 drug terms. The natural product (NP) dictionary was built
using terms from the list of herbal medicines and their synonyms provided by MedlinePlus.21
It contains 179 terms (see SI). The Cannabis dictionary was assembled by searching the web
for terms known to be used as synonyms for cannabis, resulting in 26 terms (see SI) optimized
for precision and recall on a subset of posts (data not shown). The symptom dictionary was
extracted from BICEPP22 by collecting all entities deﬁned as an Adverse Eﬀect, with a few
manual edits to include more synonyms; it is comprised of 250 terms.
Timeline posts were tagged with all dictionary terms (n-grams) for a total of 299,312
matches. Uppercase characters were converted to lowercase, and hashtag terms were treated
like all other harvested text for the purpose of dictionary matches. We found matches for
414 drugs, 133 of which with more than 10 matches. These numbers are 148/99 and 74/46
for symptoms and NP, respectively, for a total of 636 terms. This is a substantial number
of dictionary terms, given that only 7 drugs prescribed for depression were used to harvest
the set of timelines. The top 25 matches for each dictionary are provided in SI. Notice that
the term ‘depression’ was removed because of its expected high appearance. Matches in the
cannabis dictionary (e.g. 420, marijuana, hashish) were aggregated into the term cannabis to
be treated as a NP. The top 10 mentions are (counts shown): cannabis (66,540), anorexia
(26,872), anxiety (26,309), pain (15,677), suicide (11,616), mood (11,532), fluoxetine
(9,961), suicidal (8,909), ginger (7,289), insomnia (5,917).
Given the set X of all matched terms (|X| = 636), we ﬁrst compute a symmetric co-
occurrence graph Rw(X) for time-window resolutions w = 1 month, 1 week and 1 day. These


## Page 4


graphs are easily represented by adjacency matrices Rw, where entries rij denote the number of
time-windows where terms xi and xj co-occur, in all user timelines. A matrix Rw is computed
for each time-window resolution independently. To obtain a normalized strength of association
among the set of terms X, we computed proximity graphs,18 Pw(X) for each time-window
resolution w. Thus, the entries of the adjacency matrix Pw of a proximity graph are given by:
pij =
rij
rii + rjj −rij
,
∀xi,xj∈X
(1)
where pij ∈[0, 1] and pii = 1; pij = 0 for terms xi and xj that never co-occur in the same
time-window in any timeline, and pij = 1 when they always co-occur. This measure is the
probability that two terms are mentioned in the same time window, given that one of them
was mentioned.17,18 To ensure enough support exists in the data for proximity associations,
we computed proximity weights only when rii + rjj −rij ≥10; if rii + rjj −rij < 10, we set
pij = 0.
Proximity graphs are associative knowledge networks. As in any other co-occurrence
method, the assumption is that items that frequently co-occur are associated with a com-
mon phenomenon. These knowledge networks have been used successfully for automated fact-
checking,15 protein-protein interaction extraction,16 and recommender systems.17,18 Here we
use them to reveal strong associations of DDI-related terms for public health monitoring. We
also compute distance graphs Dw(X) for the same time-window resolutions, using the map:
dij = 1
pij
−1
(2)
In some of our analysis below, we compute the metric closure DC
w(X) of the distance
graphs, which is isomorphic to a speciﬁc transitive closure of the proximity graph.18 The
metric closure is equivalent to computing the shortest paths between every pair of nodes in
the distance graph. Thus, dC
ij is the length (sum of distance edge weights) of the shortest path
between terms xi and xj in the original distance graph Dw(X), and is known to scale well.15
Fig. 1.
Sample of images from collected posts related to fluoxetine.


## Page 5


3. A Monitoring tool for user-level behavior
From the analysis of user timelines, it is clear that Instagram is a social media platform with
much data relevant for public-health monitoring. Users often discuss personal health-related
information such as diagnoses and drugs prescribed. Photos posted (e.g. Figure 1) often depict
pills and packaging, along with discussions of intake schedules, expectations and feelings.
• User A on May 25, 2014:
“#notmypic .. Say hello to my new friend! Fluoxetina! Side eﬀects by now are a bit of nausea and inquietude.. Better than zoloft!
Yesterday night i started to cry while i was with my 2 friends because my ex, bulimia’s stress.. I’m sure they thought i’m crazy
so i felt like i had to explain my reasons with one of those friends.. Now i’m terriﬁed of his reaction, he is even a friend of my
ex.. Don’t know what to expect.. It’s so hard telling someone about ED and bulimia . I’m also thinking about a b/p session
today after 2 days clean, maybe it’s not the right solution. Idk. #bulimia #bulimic #mia #ed #edfamily #eatingdisorder
#prorecovery #bingepurge #purge #binge #fat #prozac #ﬂuoxetine #depression #meds”
• User B on May 13, 2015:
“I start ﬂuoxetine tomorrow, the doctor switched me from citalopram to this so let’s hope it goes better this time #anxietymeds
#depressionmeds #citalopram #ﬂuoxetine #anxiety #depression”
• User B on May 14, 2015 (one day later):
“ok so I don’t know if it’s the tablets that are doing this but I feel the lowest I’ve ever felt and I’m hoping it’s not the tablets.
Hopefully it’s just a bad day, not that there are many good days I hope tomorrow is a better day for everyone, especially if
you are feeling the same way I am. #ﬂuoxetine #depression #anxiety #depressionmeds #anxietymeds”
• User C on Feb 05 2014:
“i survived another trip to the clinic, saw a specialist, did a test that explained i’m an INFJ (introvert) which is apperently only
1% of the population. Added risperidone and upped ritalin as well as prozac. considering this keeps me ‘sane’ and able to
assimilate into the chaos of everyday life i think this counts as my #100happydays today #ﬁndhappinessineachday #bipolar
#borderlinepersonalitydisorder #INFJ #manicdepression #goinggovernment #prozac #lamotragine #ritalin #risperidone”
Fig. 2.
Instagram Drug Explorer. See text for explanation.
Given the rich data users post on Instagram, from the perspective of public-health monitor-
ing, it is useful to be able to quickly navigate and extract posts and user timelines associated
with drugs and symptoms of interest. For that purpose, we developed the Instagram Drug


## Page 6


Explorer a, a web application to explore, tag, and visualize the data. This tool also allows
downstream improvement of our dictionaries by observing important discourse features not
tagged. Figure 2 shows four screenshots with some of the current features: A) the possibility of
deﬁning multiple drugs of interest per project; B) a user timeline view that tags class-speciﬁc
dictionary matches and displays post frequency in time and where individual posts can be
quickly selected to be C) visualized separately; D) a summary of posts from user timelines of
interest. Another feature (not shown) is the display of geo-located posts using overlay maps,
which can be useful, for instance, to monitor users in places of interest, such as schools, clinics,
and hospitals. Using this tool to inspect and select timelines with high number of matches, we
were able to identify particularly relevant user timelines such as the one depicted in Figure 3,
which contains matches from all four dictionaries, and varying post frequency.
Fig. 3.
User timeline showing daily frequency of posts in time; dictionary terms from are tagged in time.
4. Network analysis of associations in population-level behavior
Using the proximity or the isomorphic distance graphs (§2), we can explore strong pairwise
term associations that arise from the collection of 5, 329, 720 posts from the population of 6, 927
users in the study. The assumption is that dictionary terms that tend to co-occur in a sub-
stantial number of user timelines may reveal important interactions among drugs, symptoms,
and natural products. Moreover, because we computed these knowledge networks at diﬀerent
time resolutions, we can explore term associations at diﬀerent time scales: day, week, and
month. Naturally, a statistical term correlation is not necessarily a causal interaction; also a
drug-symptom association may reveal a condition treated by the drug, rather than an adverse
reaction. But large-scale analysis of social media data for relational inference must start with
the identiﬁcation of multivariate correlations, which can be subsequently reﬁned, namely with
supervised classiﬁcation and NLP methods. Here, as a ﬁrst step in the analysis of Instagram
data for public health monitoring, we use unsupervised network science methods to extract
term associations of potential interest.
ahttp://informatics.indiana.edu/rocha/IDE.


## Page 7


Consider the proximity networks Pw(X) for time resolution w = 1 week. The full network
contains |X| = 636 terms (see Figure 5A for its largest connected component); Figure 4 (left)
lists the top 25 drug/NP vs symptom associations, as well as the adjacency matrix of the
distance subgraph Dw(X) for these drug/NP and symptom pairs (right). The proximity and
distance graphs are isomorphic (§2), but proximity edge weights (left) are directly interpretable
as a co-occurrence probability (eq. 1), while the isomorphic nonlinear map to distance (eq. 2)
provides greater discrimination in the visualization of the adjacency matrix (right).
Fig. 4.
drug/NP vs symptom subnetwork: (left) Top 25 pairs with largest proximity correlation. (right)
adjacency matrix of distance subnetwork; nearest (furthest) term pairs in red (black).
Of the 25 to associations listed in Figure 4 (left), 12 are known or very likely ADR, 7 do not
have conclusive studies but are deemed possible ADR from patient reports, 4 refer to associa-
tions between drugs/NP and symptoms they are indicated to treat, 1 has been shown to not
be ADR, and 1 is unknown (evidence in SI). Thus, the strongest edges in the 1 week resolution
network are relevant drug/NP-symptom associations. Furthermore, our methodology allows
an analyst to collect (via the Drug Explorer tool §3) all the individual timelines and posts that
support every association (edge) in the proximity networks, supporting a much more detailed
study of the aﬀected population—including for the purpose of ﬁne-tuning dictionaries and
mining techniques to better capture the semantics of speciﬁc populations.
The proximity networks Pw(X) also allow us to visualize, explore and search the “concep-
tual space” of drugs, symptoms, and NP as they co-occur in the depression timeline dataset.
The largest connected component of the proximity network for w = 1 week is shown in Figure
5A. The network representation allows us to ﬁnd clusters of associations, beyond term pairs,
which may be related via the same underlying phenomenon. Many multivariate and network
analysis methods can be used to uncover modular organization.23 To exemplify, here we use
the Principal Component Analysis (PCA)24 of the proximity network adjacency matrix, which
reveals potential phenomena of interest.
For instance, Figure 5, depicts a set of terms correlated with principal component (PC)


## Page 8


Fig. 5.
A. Largest connected component of the proximity network for 1 week time resolution; weights shown
only for pij ≥0.05 with unconnected terms removed. Edges are colored according to correlation with PC 4. B.
Spectrum of the PCA of the proximity network adjacency matrix. C. Biplot of correlation of terms with PC
3 and 4; red (green) terms are most (anti-) correlated with PC4. D. Subgraph depicting the network of terms
most correlated with PC4, which is related to Psoriasis; blue nodes depict conditions linked to this complex
disease (see text for details); weights shown only for pij ≥0.05.
4 (red)—others could be chosen (see SI). The subnetwork of these terms is depicted in Fig-
ure 5D. and it reveals a set of terms denoting a complex interaction of conditions which
are coherent with what is becoming known about Psoriasis. Several of the edges associate
terms related to heart disease, stroke, hypertension, hypotension, and diabetes which are high
risks for Psoriasis patients,25 including potential drug interactions (Metformin for Diabetes,
Verapimil for high blood pressure and Stroke). This subnetwork also reveals associations with
Psoriasis which are currently receiving some attention, such as with viral hepatitis26 and
seizure disorder.27 Naturally, the network also includes many terms associated with skin infec-
tions and immune reactions. The Psoriasis subnetwork is just an example of a multi-term
phenomenon of interest that is represented in the whole network; other PCA components are
shown in SI, including additional analysis of the Psoriasis subnetwork. Importantly, we can
identify users who may be experiencing this cluster of symptoms by following the posts and
timelines behind the weights in the subnetwork, which is useful for public health monitoring.
While the Psoriasis subnetwork was discovered purely by data-driven analysis, another
way to use these networks is to to query them for speciﬁc terms most associated with a set
of drugs or symptoms of interest. This problem of ﬁnding which other items A ⊆X are near
a set of query items Q ⊆X (including a subnetwork of interest) is common in recommender
systems and information retrieval.17 The answer set A can be computed as:


## Page 9


A ≡
(
xj : ∀xi∈Q
Φ
xj∈X−Q(pij) ≥α
)
(3)
where Φ is an operator of choice, pij is the proximity weight between terms xi and xj (§2),
and α is a desired threshold. If we are interested in a set of terms A which are strongly related
to every term in query set Q, then we use Φ = min. If we are interested in terms strongly
related to at least one term in Q, then Φ = max. For a compromise between the two, we
can use Φ = avg (average). Consider the query Q = {fluoxetine, anorexia} on the network
of Figure 5A (w = 1 week). Using Φ = min, we obtain an answer set with terms strongly
related to both query terms (ordered by relevance): A = {suicidal, suicide, anxiety, pain,
mood, cinnamon, insomnia, soy, headache, mania, chia, cannabis }. For the query Q =
{psoriasis, heart failure, stroke } using Φ = avg, we obtain (ordered by relevance): A =
{infections, diarrhea, hypertension, seizures, hepatitis, constipation, dermatitis,
glaucoma, vomiting }, which relates to the discussion above. Additional query examples and
details of the network search interface are shown in SI.
Proximity Pw(X) networks are useful to discover associations between terms which co-
occur in time windows w of user timelines (§4). But they are also useful to infer indirect
associations between terms. In other words, terms that do not co-occur much in user timelines,
but which tend to co-occur with the same other terms. In network science indirect associations
are typically obtained via the computation of shortest path algorithms on the isomorphic
distance graphs Dw(X).18 Terms which are very strongly connected via indirect paths, but
weakly connected via direct edges, break transitivity criteria.18 We have previously shown
that such indirect paths are useful to predict novel trends in recommender systems,18 and are
also instrumental to infer factual associations in knowledge networks.15 In this context, the
hypothesis is that strongly indirectly associated terms may reveal unknown DDI and ADR.
Fig. 6.
drug/NP vs symptom subnetwork after shortest path calculation. (left) Top 25 non-transitive term
pairs. (right) adjacency matrix of distance subnetwork after shortest path calculation.
To ﬁnd the term pairs that most break transitivity we compute all shortest paths in


## Page 10


the networks (via Dijkstra’s algorithm): the metric closure DC
w(X). Figure 6 lists the top 25
drug/NP vs symptom associations which most break transitivity. In other words, these are
term pairs which are very strongly associated via indirect paths, but very weakly associated
directly. Of the extracted associations listed in the table of Figure 6, 6 are known or likely
ADR, 3 are possible ADR from patient reports but no conclusive study, 2 refer to associations
between drugs/NP and symptoms they are indicated to treat, and all other 14 are unknown
(evidence provided in SI). Thus, unlike the case of direct associations (Figure 4), there is
less evidence for the indirect associations in the literature. This could be because they are
false associations, or because they have not been discovered yet. Validating these associations
empirically is left for forthcoming work; here the goal is to show how network analysis methods
can be used to select such latent associations which are highly implied by indirect paths
(transitivity) but are not directly observed in user post co-mentions.
Similarly to what was done with direct associations above, we can also query the proximity
network obtained after shortest path computation P C
w (X) (the isomorphic proximity graph to
DC
w(X) via eq. 2). For instance, if we query the original w = 1 week proximity network P C
w (X)
(the one depicted in Figure 5A) with Q = {psoriasis, metformin} (a type 2 diabetes drug),
using Φ = min, we obtain A = {montelukast , hypertension, dermatitis, hypotension,
hepatitis} as the top 5 terms—montelukast is a drug used to treat allergies. If we now
use the same query Q on the metric closure network P C
w (X) instead, the top 5 answer set
becomes AC = {montelukast, hypotension, naloxone, allopurinol, hypertension} (full
query results in SI). In other words, after computing shortest paths,naloxone (a synthetic
opiate antagonist used to reverse the eﬀects, including addiction, caused by narcorics) and
allopurinol (a drug used to treat gout, kidney stones, and decrease levels of uric acid in
cancer patients), become more strongly associated with the query terms. These indirect as-
sociations to do not occur very strongly in the observed Instagram timeline data, but are
strongly implied by indirect paths in the network of term proximity. In this case, the latent
associations may provide additional evidence supporting recent observations that psoriasis (an
autoimmune condition) is linked to heart disease, cancer, diabetes and depression.25
5. Discussion and Future Directions
Our preliminary analysis demonstrates that there exists a substantial health-related user com-
munity in Instagram who posts about their health conditions and medications. The drug, NP
and symptom dictionaries we employed extracted a large number of posts with such data,
enough to build knowledge networks of hundreds of terms representing the pharmacology and
symptomatic “conceptual space” of Instagram users posting about depression. Our results
and software further demonstrate that such space can be navigated for public health moni-
toring, whereby analysts can search and visualize user timelines of interest. Furthermore, the
network representation of this space allows us to extract population-level term associations
and subnetworks of terms arising from underlying (modular) phenomena of interest—such as
the Psoriasis network involving various related conditions. Thus, Instagram data shows great
potential for public health monitoring and surveillance for DDI and ADR.
Direct associations in the knowledge networks are substantiated by actual co-mentions in


## Page 11


posts from user timelines, which can subsequently be retrieved by public health analysts using
our drug explorer application. In our preliminary work, the top extracted direct associations
are shown to be backed by the literature, but we intend to pursue the systematic validation
of such associations in future work. Network methods also allow us to uncover indirect asso-
ciations among terms. These may reveal latent, yet unknown, associations, and as such, very
relevant for public health monitoring. Studying the network of indirect associations can be
further used to understand community structure as well as redundancy in the data, which we
intend to study next.
We have analyzed posts and user timelines related to depression only. Adding additional
conditions of interest (e.g. epilepsy or psoriasis) to extract additional posts would monitor
diﬀerent communities, and would likely improve the overall extraction of associations, which we
intend to test in the near future. While the drug dictionary is quite well developed already, the
NP and symptoms dictionaries need to be further developed, especially towards increasing the
terminology associated with symptoms as well as on catching particular linguistic expressions
of symptoms in Instagram. The development of named entity recognition tailored to Instagram
is another avenue we intend to pursue, starting from and expanding what has already been
done for Twitter.10
The methodology we describe here allows us to discern drug, NP and symptom associations
derived from user timeline co-mentions at diﬀerent timescales. All the results displayed pertain
to a one week window, however we also computed day and month windows. The comparison
of results at diﬀerent timescales would allow, in principle, the discovery of more immediate as
well as more delayed interactions. Such a comparison is also something we intend to pursue
in forthcoming work. Finally, the timeseries analysis of user timelines can be used to detect
discernible changes in behavior for users and groups of users. One could track, for instance,
critical changes in mood associated with the onset of depression,28 which constitutes yet
another exciting avenue to pursue with this line of research.
Our preliminary analysis demonstrates that Instagram is a very powerful source of data
of potential beneﬁt to monitor and uncover DDI and ADR. Moreover, our work shows that
complex network analysis provides an important toolbox to extract health-related associations
and their support from large-scale social media data.
Acknowledgments
This work was supported by a grant from the National Institutes of Health, National Library of
Medicine Program, grant 01LM011945-01“BLR: Evidence-based Drug-Interaction Discovery:
In-Vivo, In-Vitro and Clinical,” and a grant from Persistent Systems. RBC is supported by
CAPES Foundation Grant No. 18668127. The funders had no role in study design, data
collection and analysis, decision to publish, or preparation of the manuscript.
References
1. O. Varol, E. Ferrara, C. L. Ogan, F. Menczer and A. Flammini, Evolution of online user behavior
during a social upheaval, in Proc. 2014 ACM Conference on Web Science, WebSci ’142014.
2. J. Bollen, H. Mao and X. Zeng, Journal of Computational Science 2, 1 (2011).


## Page 12


3. E. Bakshy, S. Messing and L. A. Adamic, Science 348, 1130 (May 2015).
4. E. Ferrara, R. Interdonato and A. Tagarelli, Online popularity and topical interests through the
lens of instagram, in Proc. 25th ACM Conf. on Hypertext and Social Media, HT ’142014.
5. H. Kautz, Data mining social media for public health applications., in 23rd Int. Joint Conf. on
Artiﬁcial Intelligence (IJCAI 2013), (AAAI Press, 2013).
6. A. Signorini, A. M. Segre and P. M. Polgreen, PLoS ONE 6, p. e19467 (2011).
7. A. Sadilek, H. Kautz and V. Silenzio, Modeling spread of disease from social interactions, in
Sixth AAAI Int. Conf, on Weblogs and Social Media (ICWSM), (AAAI Press, 2012).
8. M. D. Choudhury, S. Counts and E. Horvitz, Social media as a measurement tool of depression
in populations, in Proc. 5th Annual ACM Web Science Conf., WebSci’13 (ACM, 2013).
9. A. A. Hamed, X. Wu, R. Erickson and T. Fandy, J. of biomedical informatics 56, 157 (2015).
10. A. Sarker and G. Gonzalez, Journal of biomedical informatics 53, 196 (2015).
11. B. A. Pescosolido, Annual Review of Sociology (2015).
12. E. Seltzer, N. Jean, E. Kramer-Golinkoﬀ, D. Asch and R. Merchant, Public Health 129, 1273
(September 2015).
13. Instagram Blog, 300 million. http://blog.instagram.com/post/104847837897.
14. Statista, Number of monthly active instagram users from january 2013 to december 2014 (in
millions). http://www.statista.com/statistics/253577/.
15. G. L. Ciampaglia, P. Shiralkar, L. M. Rocha, J. Bollen, F. Menczer and A. Flammini, PLoS ONE
10, p. e0128193 (2015).
16. A. Abi-Haidar, J. Kaur, A. Maguitman, P. Radivojac, A. Rechtsteiner, K. Verspoor, Z. Wang
and L. M. Rocha, Genome Biology 9, p. S:11 (September 2008).
17. L. M. Rocha, T. Simas, A. Rechtsteiner, M. D. Giacomo and R. Luce, Mylibrary@lanl: Prox-
imity and semi-metric networks for a collaborative and recommender web service, in 2005
IEEE/WIC/ACM International Conference on Web Intelligente (WI’05), (IEEE Press, 2005).
18. T. Simas and L. M. Rocha, Network Science 3, 227 (6 2015).
19. D. Wishart, C. Knox, A. Guo, D. Cheng, S. Shrivastava, D. Tzur, B. Gautam and M. Hassanali,
Nucleic Acids Res 36, D901 (January 2008).
20. H.-Y. Wu, S. Karnik, A. Subhadarshini, Z. Wang, S. Philips, X. Han, C. Chiang, L. Liu, M. Bous-
tani, L. M. Rocha, S. K. Quinney, D. Flockhart and L. Li, BMC Bioinformatics 14, 1 (2013).
21. MedlinePlus, Herbal medicine. http://1.usa.gov/1IF33ng.
22. F. P.-Y. Lin, S. Anthony, T. M. Polasek, G. Tsafnat and M. P. Doogue, BMC Bioinformatics
12, p. 112 (April 2011).
23. S. Fortunato, Physics Reports 486, 75 (2010).
24. M. E. Wall, A. Rechtsteiner and L. M. Rocha, Singular value decomposition and principal compo-
nent analysis, in A practical approach to microarray data analysis, (Springer, 2003) pp. 91–109.
25. WebMD, Psoriasis linked to heart disease, cancer. studies also show link to increased risk of
diabetes and depression. http://wb.md/1IF3hL3.
26. A. D. Cohen, D. Weitzman, S. Birkenfeld and J. Dreiher, Dermatology 220, 218 (2010).
27. O. M, K. IS, C. T, G. MP and M. KD, JAMA Neurology 71, 569 (2014).
28. I. A. van de Leemput, M. Wichers, A. O. Cramer, D. Borsboom, F. Tuerlinckx, P. Kuppens,
E. H. van Nes, W. Viechtbauer, E. J. Giltay, S. H. Aggen et al., PNAS 111, 87 (2014).


## Page 13


Supplemental Information 
Authors: Rion Brattig Correia, Lang Li & Luis M. Rocha* 
*rocha@indiana.edu 
 
 
Hashtags collected 
These are the drug names that were collected using the Instagram API. A post was collected if the user 
mentioned the name of the drug ­­ or its synonyms ­­ as a hashtag (#) in the post caption or comment with it. 
 
Drug 
# Posts 
Synonyms tags 
sertraline 
574 
sertralina 
fluoxetine 
8143 
fluoxetin, fluoxetina, fluoxetinum, fluoxétine, prozac 
citalopram 
426 
citadur, nitalapram 
escitalopram 
117 
escitalopramum, esertia 
paroxetine 
470 
paroxetina, paroxetinum 
fluvoxamine 
22 
fluvoxamina, fluvoxaminum 
trazodone 
227 
trazodona, trazodonum 
 
 
Herbal Medicine Terms 
The herbal medicine terms were extracted from the US National Library of Medicine. For each herb all it’s 
common names were included, for example: “açaí” (herb) and “amazonian palm berry” (synonym). 
reference: http://www.nlm.nih.gov/medlineplus/herbalmedicine.html 
 
acai, amazonian palm berry, aloe vera, aloe, burn plant, lily of the desert, elephants gall, aristolochic acids, 
aristolochia, asarum, asian ginseng, ginseng, chinese ginseng, korean ginseng, asiatic ginseng, astragalus, bei qi, 
huang qi, ogi, hwanggi, milk vetch, bilberry, european blueberry, whortleberry, huckleberry, bitter orange, seville 
orange, sour orange, zhi shi, black cohosh, black snakeroot, macrotys, bugbane, bugwort, rattleroot, rattleweed, 
butterbur, petasites, purple butterbur, petadolex, cats claw, una de gato, chamomile, german chamomile, 
chasteberry, chaste­tree berry, vitex, monks pepper, cinnamon, cinnamon bark, ceylon cinnamon, cassia 
cinnamon, chinese cinnamon, cranberry, american cranberry, bog cranberry, dandelion, lions tooth, blowball, 
echinacea, purple coneflower, coneflower, american coneflower, ephedra, chinese ephedra, ma huang, elderberry, 
european elder,  black elder, elder, elderberry, elder flower, sambucus, mistletoe, european mistletoe, epo, 
evening primrose oil, fenugreek, fenugreek seed, feverfew, bachelors buttons, featherfew, flaxseed, flaxseed oil, 
linseed, garlic, ginger, ginkgo, ginkgo biloba, fossil tree, maidenhair tree, japanese silver apricot, baiguo, bai guo 
ye, kew tree, yinhsing, goldenseal, yellow root, grape seed extract, green tea, chinese tea, japanese tea, 
hawthorn, english hawthorn, harthorne, hawthorne, haw, hoodia, kalahari cactus, xhoba, horse chestnut, buckeye, 
spanish chestnut, kava, kava kava, awa, kava pepper, lavender, english lavender, garden lavender, licorice,


## Page 14


licorice root, liquorice, sweet root, gan zao, chinese licorice, milk thistle, mary thistle, holy thistle, silymarin, 
silybinin, silibinin, silybin, noni, morinda, indian mulberry, hog apple, canary wood, passionflower, maypop, apricot 
vine, old field apricot, maracuja, water lemon, peppermint oil, red clover, cow clover, meadow clover, wild clover, 
red yeast rice, sage, black sage, broad­leafed sage, common sage, saw palmetto, american dwarf palm tree, 
cabbage palm, soy, st. johns wort, hypericum, klamath weed, goatweed, tea tree oil, australian tea tree oil, tea tree 
essential oil, melaleuca oil, thunder god vine, lei gong teng, turmeric, turmeric root, indian saffron, valerian, 
all­heal, garden heliotrope, chia, chia seeds, yohimbe, yohimbe bark. 
 
 
Cannabis Terms 
 
These are the dictionary of terms for Cannabis used in the analysis: 
cannabis, marijuana, marihuana, maryjane, mary jane, doobie, ganja, hashish, bhang, maconha, skunk, weed, 
dagga, hashish, pot, bud, herb, haze, joint, blunt, chronic, dank, hash, hierba, mota, 420. 
 
 
Top 25 Mentions 
 
Term 
# of mentions 
Dictionary Type 
cannabis 
66540 
cann 
anorexia 
26872 
adve 
anxiety 
26309 
adve 
pain 
15677 
adve 
suicide 
11616 
adve 
mood 
11532 
adve 
fluoxetine 
9961 
drug 
suicidal 
8909 
adve 
ginger 
7289 
herb 
insomnia 
5917 
adve 
soy 
4417 
herb 
garlic 
3804 
herb 
cinnamon 
3619 
herb 
caffeine 
2705 
drug 
burning 
2075 
adve


## Page 15


flu 
2011 
adve 
lavender 
1860 
herb 
headache 
1855 
adve 
chia 
1754 
herb 
arthritis 
1685 
adve 
 
Top 25 Mentions in each Dictionary 
 
 
Drugs 
# posts (# 
users) 
Herbs 
# posts (# 
users) 
Adverse Effect 
# posts (# 
users) 
fluoxetine 
9961 
cannabis 
66540 
anorexia 
26872 
caffeine 
2705 
ginger 
7289 
anxiety 
26309 
sertraline 
1195 
soy 
4417 
pain 
15677 
citalopram 
692 
garlic 
3804 
suicide 
11616 
epinephrine 
636 
cinnamon 
3619 
mood 
11532 
quetiapine 
480 
lavender 
1860 
suicidal 
8909 
acetaminophen 
440 
chia 
1754 
insomnia 
5917 
lorazepam 
410 
green tea 
957 
burning 
2075 
ibuprofen 
370 
cranberry 
784 
flu 
2011 
lithium 
306 
turmeric 
771 
headache 
1855 
nicotine 
304 
sage 
725 
arthritis 
1685 
prednisone 
269 
dandelion 
633 
pancreatitis 
1618 
methotrexate 
227 
aloe 
513 
mania 
1533 
ethanol 
217 
chamomile 
338 
fever 
1521 
acetylsalicylic 
acid 
212 
flaxseed 
312 
migraine 
1290 
cefpodoxime 
197 
acai 
295 
fatigue 
1014 
dopamine 
195 
licorice 
191 
psychosis 
961 
venlafaxine 
187 
elder 
167 
nightmares 
925 
duloxetine 
167 
mistletoe 
157 
cough 
865


## Page 16


zopiclone 
165 
ginseng 
130 
acne 
807 
zolpidem 
157 
passionflower 
113 
weight loss 
753 
adalimumab 
152 
liquorice 
97 
confusion 
711 
hydroxychloroqu
ine 
127 
echinacea 
95 
weakness 
699 
bupropion 
127 
huckleberry 
93 
allergic 
561 
diphenhydramin
e 
121 
kava 
82 
nausea 
556 
 
 
Statistics of the Network 
 
Full Network 
 
1 Week 
Edges in D 
34,935 
Edges in D^{MC} 
172,578 
Metric edges in D 
4,607 (13.19%) 
Edges with S>1 in D 
30,328 (86.81%) 
Edges with \inf distance in D 
166,995 
Edges with B>1 in D 
130,405 
Number of terms: 636 ­­ (n^2­n)/2 
Total number of possible edges: 201,930 
 
Colunas: #edges in original matrix (D), #edges in metric closure (D^mc),  # / % metric edges in original matrix (D), 
# / % s>1 parameter in original matrix (D), # edges with infinite distance in D, # of edges with b>1


## Page 17


Preliminary evidence for drug-symptoms associations (Figure 4) 
 
 
1) naloxone - hypotension (proximity: 0.4285) - ​
Symptom 
 
Indications: “For the complete or partial reversal of narcotic depression, including respiratory depression, 
induced by opioids including natural and synthetic narcotics, propoxyphene, methadone and the 
narcotic­antagonist analgesics: nalbuphine, pentazocine and butorphanol. It is also indicated for the 
diagnosis of suspected acute opioid overdose. It may also be used as an adjunctive agent to ​
increase 
blood pressure​
 in the management of septic shock.”[1] 
Pharmacodynamics: “Naloxone is an opiate antagonist and prevents or reverses the effects of opioids 
including respiratory depression, sedation and ​
hypotension​
”[1] 
 
references: 
1.
DrugBank 
2) allopurinol - hypotension (proximity: 0.4117) -  Possible ​
ADR 
 
Indication: “For the treatment of hyperuricemia associated with primary or secondary gout. Also indicated for 
the treatment of primary or secondary uric acid nephropathy, with or without the symptoms of gout, as well 
as chemotherapy­induced hyperuricemia and recurrent renal calculi.”[1] 
“Hyperuricemia is associated strongly with the development of hypertension, renal disease, and progression. 
Allopurinol decreases serum uric acid levels by inhibiting the enzyme xanthine oxidase.”[2] 
 
Evidence points against it in study of patients who take medication for arterial hypertension [3], however, 
some evidence for ADR exists from patient reports [4]. 
 
references: 
1.
DrugBank 
2.
http://www.sciencedirect.com/science/article/pii/S0272638605015180 
3.
http://www.ncbi.nlm.nih.gov/pubmed/21405957  
4.
http://factmed.com/study­ALLOPURINOL­causing­HYPOTENSION.php  
3) montelukast - hypotension (proximity: 0.3076) - Possible ​
ADR 
 
Indications: “For the treatment of asthma”[1] 
 
No study found, but some evidence of ADR especially with patients who take Lorazepam for anxiety and 
depression [2]. 
 
 
references: 
1.
DrugBank 
2.
http://www.ehealthme.com/ds/montelukast+sodium/hypotension


## Page 18


4) belimumab - neuropathy (proximity: 0.2989) - ​
Symptom 
 
Indications: “Adjunct treatment for auto­antibody­positive active systemic lupus erythematosus.”[1] 
Systemic lupus erythematosus (SLE) is an autoimmune disease in which the body's immune system 
mistakenly attacks healthy tissue. It can affect the skin, joints, kidneys, brain, and other organs. Other 
symptoms depend on which part of the body is affected: ​
Brain and nervous system​
: headaches, 
numbness​
, tingling, seizures, vision problems, personality changes[2] 
 
references: 
1.
DrugBank 
2.
http://www.nlm.nih.gov/medlineplus/ency/article/000435.htm 
5) lidocaine - hypotension (proximity: 0.2916) - ​
ADR 
 
Indications: “For production of local or regional anesthesia by infiltration techniques such as percutaneous 
injection and intravenous regional anesthesia by peripheral nerve block techniques such as brachial plexus 
and intercostal and by central neural techniques such as lumbar and caudal epidural blocks.”[1] 
“This paper reports the cardiovascular effects of intentionally toxic intravenous doses of ​
lidocaine​
 [...] and 
the mechanisms of death. In 4/4 lidocaine­treated animals, respiratory depression with bradycardia and 
hypotension​
 without arrhythmias were the causes of death.” 
 
references: 
1.
DrugBank 
2.
http://journals.lww.com/anesthesia­analgesia/Abstract/1989/09000/Myocardial_and_Cerebral_Drug
_Concentrations_and.2.aspx 
6) hydroxychloroquine - neuropathy (proximity: ) - Possible ​
ADR (unknown, 1 
case) 
 
Indications: “For the suppressive treatment and treatment of acute attacks of malaria due to Plasmodium 
vivax, P. malariae, P. ovale, and susceptible strains of P. falciparum. It is also indicated for the treatment of 
discoid and systemic ​
lupus erythematosus (LE)​
, and rheumatoid arthritis” [1]. 
Toxicity: “Symptoms of overdose include headache, drowsiness, visual disturbances, cardiovascular 
collapse, and convulsions, followed by sudden and early respiratory and cardiac arrest. The 
electrocardiogram may reveal atrial standstill, nodal rhythm, prolonged intraventricular conduction time, and 
progressive bradycardia leading to ventricular fibrillation and/or arrest.”[1] 
“Chloroquine and ​
hydroxychloroquine​
 (HCQ) are commonly prescribed antimalarial agents used for a 
variety of systemic diseases.  In this report, we describe ​
a patient​
 with rheumatoid arthritis and respiratory 
failure associated with proximal myopathy secondary to HCQ. Patients treated with HCQ in whom proximal 
myopathy, ​
neuropathy​
, or cardiomyopathy develop should be evaluated for possible ​
HCQ toxicity​
.”[2] 
 
references: 
1.
DrugBank 
2.
http://journal.publications.chestnet.org/article.aspx?articleid=1084931 
7) ribavirin - angina (proximity: 0.2894) - ​
ADR


## Page 19


Indications: “For the treatment of chronic hepatitis C and for respiratory syncytial virus (RSV).”[1] 
Contraindications to ribavirin include end­stage renal failure, anaemia, severe heart disease, pregnancy and 
inadequate contraception. The major side­effect of ​
ribavirin​
 is haemolytic anaemia, which can be severe. 
Cardiovascular disease should be carefully excluded in patients considered for combination therapy, as 
anaemia may lead to ​
angina​
 or ​
heart failure​
 in these patients.[2] 
 
references: 
1.
DrugBank 
2.
http://ar.iiarjournals.org/content/25/2B/1315.short 
8) ribavirin - hypotension (proximity: 0.2857) - ​
ADR 
 
Indications: “For the treatment of chronic hepatitis C and for respiratory syncytial virus (RSV).”[1] 
“Cardiovascular effects, particularly bradycardia, have been associated with ribavirin use. Bradycardia, 
hypotension, and cardiac arrest have been reported with inhaled ribavirin”[2] 
 
references: 
1.
DrugBank 
2.
http://onlinelibrary.wiley.com/doi/10.1592/phco.27.4.494/abstract 
9) tiotropium - angina (proximity: 0.2857) - ​
ADR 
 
Indications: “Used in the management of chronic obstructive pulmonary disease (COPD)”[1] 
“Cardiac angina was more common on active treatments than placebo”[2] 
 
references: 
1.
DrugBank 
10) tiotropium - hypotension (proximity: 0.2857) - Unknown, possible ADR 
 
Indications: “Used in the management of chronic obstructive pulmonary disease (COPD)”[1]. No studies with 
results found. Some evidence of possible ADR [2]. 
 
references: 
1.
DrugBank 
2.
http://factmed.com/study­TIOTROPIUM­causing­HYPOTENSION.php  
11) vasopressin - rhinitis (proximity: 0.2727) - ​
ADR 
 
Indications: “​
For the treatment of enuresis, polyuria, diabetes insipidus, polydipsia and 
oesophageal varices with bleeding​
”[1] 
“Also known as “desmopressin” (1­deamino­8­D­argininevasopressin)[2]. Nasal congestion and rhinitis have 
been reported with nasal spray formulations.”[1] 
references: 
1.
DrugBank 
2.
http://onlinelibrary.wiley.com/doi/10.1046/j.1475­097X.2002.00401.x/full


## Page 20


12) allopurinol - angina (proximity: 0.2631) - ​
ADR 
 
Indication: “For the treatment of hyperuricemia associated with primary or secondary gout. Also indicated for 
the treatment of primary or secondary uric acid nephropathy, with or without the symptoms of gout, as well 
as chemotherapy­induced hyperuricemia and recurrent renal calculi.”[1] 
Patients in the ​
allopurinol​
 group and in the highest uric acid quartile had indicators of more severe ​
Heart 
Failure​
[2] 
references: 
1.
DrugBank 
2.
http://www.sciencedirect.com/science/article/pii/S0002870310007337 
13) norethindrone-aggression (proximity: 0.2632)  - ​
ADR 
 
“Perinatal exposure to ​
norethindrone​
 influences morphology and ​
aggressive​
 behavior of female mice” [1]. 
“In the fighting fish Beta splenders it is associated with masculinization, normal growth and secondary 
sexual characteristics, yet no abnormal aggression behavior” [2]. 
 
references: 
1.
http://www.sciencedirect.com/science/article/pii/0018506X81900052 
2.
http://repository.ias.ac.in/39869/ 
14) liraglutide - rhinitis (proximity: 0.25) - Unknown, possible ADR 
 
Indications: “For use in/treatment of diabetes mellitus type 2.”[1] 
No studies found, some evidence from patient reports [2] 
 
references: 
1.
Drugbank 
2.
http://factmed.com/study­LIRAGLUTIDE%20(NN2211)­causing­RHINITIS%20ALLERGIC.php  
 
15) naloxone - angina (proximity: 0.25) - No evidence of ADR 
 
Indications: “For the complete or partial reversal of narcotic depression, including respiratory depression, 
induced by opioids including natural and synthetic narcotics, propoxyphene, methadone and the 
narcotic­antagonist analgesics: nalbuphine, pentazocine and butorphanol. It is also indicated for the 
diagnosis of suspected acute opioid overdose. It may also be used as an adjunctive agent to increase blood 
pressure in the management of septic shock.”[1] 
 
Small study on patients with coronary disease showed no evidence of ADR [2].  
 
references: 
 
1.
DrugBank 
2.
http://www.ncbi.nlm.nih.gov/pubmed/6496361


## Page 21


16) verapamil - hypotension (proximity: 0.2333) - ​
ADR 
 
Indications: “For the treatment of ​
hypertension​
, angina, and cluster headache prophylaxis.”[1] 
references: 
The use of ​
verapamil​
 in the treatment of cardiac disease is becoming more frequent. In general, it is used 
for the reversal of a supraver/tricular tachycardia and this can be achieved safely and effectively with the 
minimum of side effects [4], of which the most common one is transient, mild ​
hypotension​
. 
 
1.
DrugBank 
2.
http://link.springer.com/article/10.1007%2FBF01686855 
17) hydroxyurea - blurred vision (proximity: 0.2307) - ​
Symptom 
 
Indications: “For management of melanoma, resistant chronic myelocytic ​
leukemia​
, and recurrent, 
metastatic, or inoperable carcinoma of the ovary and Sickle­cell anemia.”[1] 
Leukostasis is a white blood cell count above 100,000/μL. It is most often seen in leukemia patients. The 
brain and lungs are the two most commonly affected organs. Occluded microcirculation causes local 
hypoxemia and hemorrage manifesting as headache, ​
blurred vision​
.[2] 
 
references: 
2.
DrugBank 
3.
https://en.wikipedia.org/wiki/Leukostasis 
18) adalimumab - gastritis (proximity: 0.2271) - ​
Symptom 
 
“Crohn's disease (CD) is an inflammatory bowel disease. It causes ​
inflammation of the lining of your 
digestive tract,​
 which can lead to abdominal pain, severe diarrhea, fatigue, weight loss and malnutrition”[2]. 
“CD most often manifests in late adolescence or early adulthood. ​
Adalimumab​
 is a fully human 
immunoglobulin G1 monoclonal antibody to tumour necrosis factor that is administered subcutaneously and 
is indicated for use in adults with CD who have had an inadequate response to conventional therapy. 
However,clinical trial experience with adalimumab in CD is limited to adults” [1]. “It was also found as an 
adverse reaction in one patient on a controlled experiment to evaluate the efficacy of adalimumab in juvenile 
idiopathic arthritis­associated uveitis” [3]. 
 
references: 
1.
http://journals.lww.com/jpgn/Fulltext/2008/02000/Adalimumab_Induces_and_Maintains_Remission_i
n.14.aspx 
2.
http://www.mayoclinic.org/diseases­conditions/crohns­disease/basics/definition/con­20032061 
3.
http://rheumatology.oxfordjournals.org/content/47/3/339.full 
19) histamine phosphate - hypotension (proximity: 0.1875) - ​
ADR 
 
“​
Side effects​
 can lead to hypertension, ​
hypotension​
, headache, dizziness, nervousness and tachycardia. 
Large overdoses can lead to seizures” [1]. 
 
references: 
1.
DrugBank


## Page 22


20) conjugated estrogens - dyspepsia (proximity: 0.2105) - ​
ADR 
 
Indications: “​
For the treatment of moderate to severe vasomotor symptoms associated with the 
menopause [...]​
”[1] 
 
“The most common adverse drug events (with an incidence of at least 5%) associated with ​
CE/BZA​
 have 
included muscle spasms, dizziness, nausea, diarrhea, ​
dyspepsia​
, upper abdominal pain, neck pain, and 
throat pain.” [2] 
 
references: 
1.
DrugBank 
2.
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4357350/  
21) donepezil - rhinitis (proximity: 0.2) - ​
ADR 
 
Indications: “For the palliative treatment of mild to moderate dementia of the Alzheimer's type.”[1] 
“The most common adverse events included nausea, diarrhoea, headache, insomnia, dizziness, ​
rhinitis​
, 
vomiting, asthenia/fatigue and anorexia.”[2] 
 
references: 
1.
DrugBank 
2.
http://www.ncbi.nlm.nih.gov/pubmed/12469988 
22) scopolamine - neurotoxicity (proximity: 0.2) - Possible ​
ADR 
 
Indications: “For the treatment of excessive salivation, colicky abdominal pain, bradycardia, sialorrhoea, 
diverticulitis, irritable bowel syndrome and motion sickness.”[1] 
Sopolamine is known and used for inducing amnesia and dementia in lab animals(e.g. rats and monkeys), 
though not clear it causes the same in humans [2].  
 
references: 
1.
DrugBank 
2.
http://jop.sagepub.com/content/6/3/382.abstract  
23) ribavirin - myopathy (proximity: 0.2) - Possible ​
ADR (unknown, 1 case) 
 
Indications: “For the treatment of chronic hepatitis C and for respiratory syncytial virus (RSV).”[1] 
“Adverse events induced by interferon therapy are numerous but myopathy is rare and has not been 
described with the use of pegylated interferon­a. We report the case of a 33­year­old Caucasian man who 
was successfully treated for acute hepatitis C with the combination of pegylated interferon­a2b and 
ribavirin​
, and who during treatment developed ​
myopathy​
 which proved reversible.”[2] 
 
references: 
1.
DrugBank 
2.
http://onlinelibrary.wiley.com/store/10.1046/j.1365­2893.2003.00478.x/asset/j.1365­2893.2003.0047
8.x.pdf?v=1&t=id69jh7g&s=1a95bda8c2380a01e0e8fe0b9ce4d1ea40619beb


## Page 23


24) tiotropium - myopathy (proximity: 0.2) - Nothing 
 
Indications: “Used in the management of chronic obstructive pulmonary disease (COPD).”[1] 
references: 
1.
DrugBank 
25) vardenafil - hypotension (proximity: 0.1875) - ​
ADR 
 
Indications: “Used for the treatment of erectile dysfunction”[1] 
Like sildenafil, ​
vardenafil​
 has a slightly ​
hypotensive effect​
, maximal 5­10 mmHg average[2] 
 
references: 
1.
DrugBank 
2.
http://www.ncbi.nlm.nih.gov/pubmed/12435622


## Page 24


Preliminary evidence for drug-symptoms associations in indirect associations 
(Figure 6) 
 
 
1) cinnarizine - hypotension (metric closure proximity: 0.21) - Nothing 
Indications: “For the treatment of vertigo/meniere's disease, nausea and vomiting, motion sickness and also 
useful for vestibular symptoms of other origins.”[1] 
 
references: 
1.
DrugBank 
 
2) bethanechol - hypotension (metric closure proximity: 0.21) - ​
ADR 
Indications: “For the treatment of acute postoperative and postpartum nonobstructive (functional) urinary 
retention and for neurogenic atony of the urinary bladder with retention.  It may cause ​
hypotension​
, cardiac 
rate changes, and bronchial spasms.”[1] 
 
references: 
1.
DrugBank 
3) cabergoline - hypotension (metric closure proximity: 0.21) - Possible ​
ADR 
Indications: “For the treatment of hyperprolactinemic disorders, either idiopathic or due to prolactinoma 
(prolactin­secreting adenomas). May also be used to manage symptoms of Parkinsonian Syndrome as 
monotherapy during initial symptomatic management or as an adjunct to levodopa therapy during advanced 
stages of disease.”[1] 
“Initial doses higher than 1.0 mg may produce ​
orthostatic hypotension​
. Care should be exercised when 
administering Cabergoline with other medications known to lower blood pressure.”[2] 
 
references: 
2.
DrugBank 
3.
http://www.drugs.com/pro/cabergoline.html 
 
4) primidone - hypotension (metric closure proximity: 0.196) - ​
ADR (overdose) 
Indications: “For the treatment of epilepsy”[1] 
Case: Laboratory studies demonstrated extremely high serum concentrations of methsuximide (98.5 
mg/liter) and ​
primidone​
 (62 mg/liter), and she was admitted to overdose of primidone. [...] she developed 
hypotension​
 with urine output decreased to 3ml/h and a systolic blood pressure of 50­60 mmHg [2]. 
Other cases, see [3] 
 
references: 
1.
DrugBank 
2.
http://www.clinchem.org/content/22/6/915.full.pdf 
3.
http://toxnet.nlm.nih.gov/cgi­bin/sis/search/a?dbs+hsdb:@term+@DOCNO+3169


## Page 25


5) desmopressin - hypotension (metric closure proximity: 0.196) - ​
ADR 
Indications: “Oral formulations may be used to manage primary nocturnal enuresis in adults and vasopressin 
sensitive diabetes insipidus, and for control of temporary polyuria and polydipsia following head trauma or 
surgery in the pituitary region. Intranasal and parenteral formulations may be used to manage spontaneous 
or trauma­induced bleeds (e.g. hemarthrosis, intramuscular hematoma, mucosal bleeding) in patients with 
hemophilia A or von Willebrand's disease Type I. May also be used parenterally to prevent or treat bleeding 
in patients with uremia.”[1] 
“​
Desmopressin acetate​
 is used to reduce blood loss after cardiac surgery. However, there have been 
reports that ​
hypotension​
 can occur with infusion of desmopressin and that postoperative blood loss is not 
reduced. [Results shows] a 20% or greater decrease in mean arterial pressure was observed in 7 of 20 
patients receiving desmopressin.” 
 
references: 
1.
DrugBank 
2.
http://europepmc.org/abstract/med/2042789 
 
6) sevelamer - hypotension (metric closure proximity: 0.196) - Possible ​
ADR (case) 
Indications: “For the control of serum phosphorus in patients with Chronic Kidney Disease (CKD) on 
hemodialysis.”[1] 
“A 62­year­old woman presented with bleeding per rectum for one day. She reported a history of 
constipation which occurred 1 mo ago when she started taking Sevelamer.[...] Besides Sevelamer, she was 
also taking Clopidogrel but never had similar episodes of bleeding before. Physical examination revealed 
tachycardia and ​
hypotension​
.” 
 
references: 
1.
DrugBank 
2.
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2708383/ 
 
7) atomoxetine - hypotension (metric closure proximity: 0.188) - Possible ​
ADR 
(case) 
Indications: “For the treatment of Attention­Deficit/Hyperactivity Disorder (ADHD) alone or in combination 
with behavioral treatment, as an adjunct to psychological, educational, social, and other remedial 
measures.”[1] 
Case: “The common side effects reported with the use of atomoxetine include mainly GI disturbances. 
Cardiovascular side effects are less commonly reported​
. The increase in the noradrenergic tone may 
explain some of the side effects noted with the use of this medication. Here, we present a case of a patient 
who presented with syncope, ​
orthostatic hypotension​
, and tachycardia and discuss the various clinical 
implications based on the pharmacokinetics and pharmacodynamics of the drug.” 
 
references: 
1.
DrugBank 
2.
http://www.hindawi.com/journals/crim/2011/952584/abs/


## Page 26


8) vasopressin - hypotension (metric closure proximity: 0.184) - Unknown 
Indications: “For the treatment of enuresis, polyuria, diabetes insipidus, polydipsia and oesophageal varices 
with bleeding”[1] 
 
references: 
1.
DrugBank 
 
9) montelukast - angina (metric closure proximity: 0.180) - ​
Symptom 
“​
Montelukast​
 is a leukotriene receptor antagonist (LTRA) used for the maintenance treatment of asthma 
and to relieve symptoms of seasonal allergies” [1] and are also “​
useful in treating angina​
, cerebral spasm, 
glomerular nephritis, hepatitis, endotoxemia, uveitis, and allograft rejection”.[2] 
 
references: 
1.
DrugBank 
2.
Patent: ​
https://www.google.com/patents/US5565473 
 
10) lidocaine - angina (metric closure proximity: 0.177) - ​
Symptom 
Indications: “Indications: “For production of local or regional anesthesia by infiltration techniques such as 
percutaneous injection and intravenous regional anesthesia by peripheral nerve block techniques such as 
brachial plexus and intercostal and by central neural techniques such as lumbar and caudal epidural 
blocks.”[1] 
“​
Lidocaine​
 is an anesthetic agent indicated for production of local or regional anesthesia and in the 
treatment of ventricular tachycardia​
 occurring during cardiac manipulation, such as surgery or 
catheterization, or which may occur during acute myocardial infarction, digitalis toxicity, or other cardiac 
diseases.”[1] 
 
references: 
1.
DrugBank 
 
11) liraglutide - hypotension (metric closure proximity: 0.174) - ​
ADR 
Indications: “For use in/treatment of diabetes mellitus type 2.”[1] 
Cardiovascular Side Effects: Very common (10% or more): Increases in mean resting heart rate; Common 
(1% to 10%): ​
Hypotension​
[2]. 
 
references: 
1.
DrugBank 
2.
http://www.drugs.com/sfx/liraglutide­side­effects.html 
 
12) naloxone - rhinitis (metric closure proximity: 0.167) - ​
ADR 
Indications: “For the complete or partial reversal of narcotic depression, including respiratory depression, 
induced by opioids including natural and synthetic narcotics, propoxyphene, methadone and the 
narcotic­antagonist analgesics: nalbuphine, pentazocine and butorphanol. It is also indicated for the


## Page 27


diagnosis of suspected acute opioid overdose. It may also be used as an adjunctive agent to increase blood 
pressure in the management of septic shock.”[1] 
“​
Naloxone​
 may precipitate withdrawal in patients receiving opioids. Withdrawal is characterized by nausea, 
vomiting, sweating, lacrimation, ​
rhinorrhea​
, cramping[...]”[2] 
 
references: 
1.
DrugBank 
2.
http://www.drugs.com/naloxone.html 
 
13) cinnarizine - angina (metric closure proximity: 0.163) - Unknown 
Indications: “For the treatment of vertigo/meniere's disease, nausea and vomiting, motion sickness and also 
useful for vestibular symptoms of other origins.”[1] 
 
references: 
1.
DrugBank 
 
14) bethanechol - angina (metric closure proximity: 0.163) - Unknown 
Indications: “For the treatment of acute postoperative and postpartum nonobstructive (functional) urinary 
retention and for neurogenic atony of the urinary bladder with retention.”[1] 
 
references: 
1.
DrugBank 
 
15) cabergoline - angina (metric closure proximity: 0.163) - Unknown 
Indications: “For the treatment of hyperprolactinemic disorders, either idiopathic or due to prolactinoma 
(prolactin­secreting adenomas). May also be used to manage symptoms of Parkinsonian Syndrome as 
monotherapy during initial symptomatic management or as an adjunct to levodopa therapy during advanced 
stages of disease.”[1] 
 
references: 
1.
DrugBank 
 
16) allopurinol - myopathy (metric closure proximity: 0.158) - Unknown 
Indications: “For the treatment of hyperuricemia associated with primary or secondary gout. Also indicated 
for the treatment of primary or secondary uric acid nephropathy, with or without the symptoms of gout, as 
well as chemotherapy­induced hyperuricemia and recurrent renal calculi.”[1] 
 
references: 
1.
DrugBank 
 
17) cilostazol - hypotension (metric closure proximity: 0.156) - ​
ADR (overdose) 
Indications: “For the reduction of symptoms of intermittent claudication (pain in the legs that occurs with 
walking and disappears with rest).”[1]


## Page 28


“Information on acute overdosage with cilostazol in humans is limited. The signs and symptoms of an ​
acute 
overdose​
 can be anticipated to be those of excessive pharmacologic effect: severe headache, diarrhea, 
hypotension​
, tachycardia, and possibly cardiac arrhythmias.”[1] 
 
references: 
1.
DrugBank 
 
18) follitropin beta - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “For treatment of female infertility”[1] 
 
references: 
4.
DrugBank 
 
19) tetrabenazine - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “Treatment of hyperkinetic movement disorders like chorea in Huntington's disease, 
hemiballismus, senile chorea, Tourette syndrome and other tic disorders, and tardive dyskinesia”[1] 
 
references: 
5.
DrugBank 
 
20) nevirapine - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “For use in combination with other antiretroviral drugs in the ongoing treatment of HIV­1 
infection.”[1] 
 
references: 
6.
DrugBank 
 
21) flumazenil - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “For the complete or partial reversal of the sedative effects of benzodiazepines in cases where 
general anesthesia has been induced and/or maintained with benzodiazepines, and where sedation has 
been produced with benzodiazepines for diagnostic and therapeutic procedures. Also for the management 
of benzodiazepine overdose as an adjunct for appropriate supportive and symptomatic measures.”[1] 
 
references: 
7.
DrugBank 
 
22) alendronate - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “For the treatment and prevention of osteoporosis in women and Paget's disease of bone in both 
men and women.”[1] 
 
references: 
8.
DrugBank


## Page 29


23) betahistine - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “For the reduction of episodes of vertigo association with Ménière's disease.”[1] 
 
references: 
9.
DrugBank 
 
24) natamycin - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “For the treatment of fungal blepharitis, conjunctivitis, and keratitis caused by susceptible 
organisms including Fusarium solani keratitis.”[1] 
 
references: 
10. DrugBank 
 
25) prasugrel - hypotension (metric closure proximity: 0.156) - Unknown 
Indications: “ndicated in combination with acetylsalicylic acid (ASA) to prevent atherothrombotic events in 
patients with acute coronary syndrome (ACS) who are to be managed with percutaneous coronary 
intervention (PCI)”[1] 
 
references: 
11. DrugBank


## Page 30


Psoriasis network identified with PC 4 and colored by PC5 
 
PC5 further characterizes the Psoriasis network identified with PC 4, uncovering two subnetwork clusters. Red 
(green) nodes are (anti­)correlated with PC5. Red nodes are associated with a number of drugs (such as metformin 
for Diabetes) as well as is related to hypotension, angina, and heart failure. The green nodes are, in turn,  associated 
hypertension as well as the cluster of conditions linked to psoriasis such as glaucoma, hepatitis, arthritis, seizures 
and stroke. Additionally, red nodes are associated with depression drugs citalopram and sertraline which are external 
to subnetwork of PC4 but strongly correlated with PC5, as well as psychosis and related conditions. Green nodes are 
also associated with many NP terms which are external to subnetwork of PC4 but strongly anti­correlated with PC5. 
 
Some of the NP anti­correlated with PC5 are: turmeric, aloe, acai, flaxseed, elderberry, echinacea,  
peppermint oil, licorice, chamomile, fenugreek, valerian.


## Page 31


Queries on the 1 Week Distance and Transitive Closure Network 
 
 
Query 1W: ‘​
pain​
’ and ‘​
cannabis​
’ 
Ordering: ​
avg 
 
Proximity Network Results 
             pain  cannabis  (max)  (min)  (avg) 
pain        1.000     0.058  1.000  0.058  0.529 
cannabis    0.058     1.000  1.000  0.058  0.529 
anxiety     0.160     0.034  0.160  0.034  0.097 
insomnia    0.170     0.019  0.170  0.019  0.095 
suicide     0.156     0.025  0.156  0.025  0.090 
mood        0.121     0.032  0.121  0.032  0.076 
suicidal    0.130     0.012  0.130  0.012  0.071 
fluoxetine  0.099     0.028  0.099  0.028  0.063 
ginger      0.083     0.025  0.083  0.025  0.054 
headache    0.086     0.013  0.086  0.013  0.050 
cinnamon    0.079     0.020  0.079  0.020  0.049 
garlic      0.068     0.023  0.068  0.023  0.046 
flu         0.067     0.018  0.067  0.018  0.042 
migraine    0.075     0.008  0.075  0.008  0.042 
burning     0.067     0.015  0.067  0.015  0.041 
arthritis   0.069     0.007  0.069  0.007  0.038 
fatigue     0.065     0.008  0.065  0.008  0.036 
soy         0.056     0.015  0.056  0.015  0.035 
caffeine    0.054     0.012  0.054  0.012  0.033 
lavender    0.050     0.012  0.050  0.012  0.031 
 
Transitive Closure (proximity) Networks Results 
             pain  cannabis  (max)  (min)  (avg) 
pain        1.000     0.058  1.000  0.058  0.529 
cannabis    0.058     1.000  1.000  0.058  0.529 
insomnia    0.170     0.045  0.170  0.045  0.108 
anxiety     0.160     0.045  0.160  0.045  0.102 
suicide     0.156     0.044  0.156  0.044  0.100 
suicidal    0.132     0.042  0.132  0.042  0.087 
mood        0.121     0.041  0.121  0.041  0.081 
anorexia    0.103     0.039  0.103  0.039  0.071 
fluoxetine  0.099     0.038  0.099  0.038  0.068 
headache    0.086     0.036  0.086  0.036  0.061 
 
 
Query 1W: ‘​
fluoxetine​
’ and ‘​
anorexia​
’ 
Ordering: ​
min 
 
Proximity Network Results 
            fluoxetine  anorexia  (max)  (min)  (avg) 
suicidal         0.075     0.111  0.111  0.075  0.093


## Page 32


suicide          0.073     0.093  0.093  0.073  0.083 
anxiety          0.071     0.225  0.225  0.071  0.148 
pain             0.099     0.041  0.099  0.041  0.070 
mood             0.089     0.028  0.089  0.028  0.058 
cinnamon         0.066     0.022  0.066  0.022  0.044 
fluoxetine       1.000     0.020  1.000  0.020  0.510 
anorexia         0.020     1.000  1.000  0.020  0.510 
insomnia         0.081     0.019  0.081  0.019  0.050 
soy              0.064     0.014  0.064  0.014  0.039 
headache         0.075     0.014  0.075  0.014  0.044 
mania            0.022     0.011  0.022  0.011  0.016 
chia             0.034     0.010  0.034  0.010  0.022 
cannabis         0.028     0.009  0.028  0.009  0.018 
ginger           0.070     0.008  0.070  0.008  0.039 
psychosis        0.017     0.008  0.017  0.008  0.012 
green tea        0.039     0.008  0.039  0.008  0.023 
burning          0.075     0.007  0.075  0.007  0.041 
appetite         0.037     0.006  0.037  0.006  0.022 
garlic           0.062     0.006  0.062  0.006  0.034 
 
Transitive Closure (proximity) Networks Results 
            fluoxetine  anorexia  (max)  (min)  (avg) 
pain             0.099     0.103  0.103  0.099  0.101 
insomnia         0.081     0.079  0.081  0.079  0.080 
suicidal         0.075     0.114  0.114  0.075  0.094 
suicide          0.073     0.116  0.116  0.073  0.094 
anxiety          0.071     0.225  0.225  0.071  0.148 
mood             0.089     0.059  0.089  0.059  0.074 
fluoxetine       1.000     0.057  1.000  0.057  0.529 
anorexia         0.057     1.000  1.000  0.057  0.529 
migraine         0.054     0.050  0.054  0.050  0.052 
headache         0.075     0.049  0.075  0.049  0.062 
 
 
Query 1W: ‘​
mood​
’, ‘​
cannabis​
’, ‘​
fluoxetine​
’ 
Ordering: ​
avg 
 
Proximity Network Results 
            cannabis   mood  fluoxetine  (max)  (min)  (avg) 
mood           0.032  1.000       0.089  1.000  0.032  0.373 
fluoxetine     0.028  0.089       1.000  1.000  0.028  0.372 
cannabis       1.000  0.032       0.028  1.000  0.028  0.353 
pain           0.058  0.121       0.099  0.121  0.058  0.092 
insomnia       0.019  0.083       0.081  0.083  0.019  0.061 
anxiety        0.034  0.071       0.071  0.071  0.034  0.059 
headache       0.013  0.086       0.075  0.086  0.013  0.058 
ginger         0.025  0.074       0.070  0.074  0.025  0.056 
cinnamon       0.020  0.082       0.066  0.082  0.020  0.056 
suicide        0.025  0.064       0.073  0.073  0.025  0.054


## Page 33


burning        0.015  0.066       0.075  0.075  0.015  0.052 
garlic         0.023  0.064       0.062  0.064  0.023  0.050 
suicidal       0.012  0.055       0.075  0.075  0.012  0.047 
flu            0.018  0.062       0.058  0.062  0.018  0.046 
caffeine       0.012  0.063       0.060  0.063  0.012  0.045 
soy            0.015  0.054       0.064  0.064  0.015  0.044 
fever          0.009  0.045       0.053  0.053  0.009  0.036 
cough          0.008  0.041       0.041  0.041  0.008  0.030 
lavender       0.012  0.039       0.035  0.039  0.012  0.029 
migraine       0.008  0.046       0.030  0.046  0.008  0.028 
 
Transitive Closure (proximity) Networks Results 
            cannabis   mood  fluoxetine  (max)  (min)  (avg) 
mood           0.041  1.000       0.089  1.000  0.041  0.377 
fluoxetine     0.038  0.089       1.000  1.000  0.038  0.376 
cannabis       1.000  0.041       0.038  1.000  0.038  0.360 
pain           0.058  0.121       0.099  0.121  0.058  0.092 
insomnia       0.045  0.083       0.081  0.083  0.045  0.070 
headache       0.036  0.086       0.075  0.086  0.036  0.066 
suicide        0.044  0.073       0.073  0.073  0.044  0.063 
anxiety        0.045  0.074       0.071  0.074  0.045  0.063 
suicidal       0.042  0.067       0.075  0.075  0.042  0.061 
cinnamon       0.035  0.082       0.066  0.082  0.035  0.061 
 
 
Query 1W: ​
‘hepatitis’ 
Ordering: ​
avg 
 
Proximity Network Results 
                      hepatitis  (max)  (min)  (avg) 
hepatitis                 1.000  1.000  1.000  1.000 
glaucoma                  0.195  0.195  0.195  0.195 
hypertension              0.171  0.171  0.171  0.171 
diarrhea                  0.169  0.169  0.169  0.169 
impotence                 0.169  0.169  0.169  0.169 
seizures                  0.163  0.163  0.163  0.163 
dermatitis                0.155  0.155  0.155  0.155 
irritability              0.145  0.145  0.145  0.145 
psoriasis                 0.144  0.144  0.144  0.144 
hypotension               0.130  0.130  0.130  0.130 
vomiting                  0.126  0.126  0.126  0.126 
constipation              0.124  0.124  0.124  0.124 
stroke                    0.122  0.122  0.122  0.122 
infections                0.122  0.122  0.122  0.122 
osteoporosis              0.114  0.114  0.114  0.114 
acetylsalicylic acid      0.113  0.113  0.113  0.113 
infertility               0.113  0.113  0.113  0.113 
histamine phosphate       0.107  0.107  0.107  0.107 
itching                   0.105  0.105  0.105  0.105 
stinging                  0.103  0.103  0.103  0.103


## Page 34


Transitive Closure (proximity) Networks Results 
              hepatitis  (max)  (min)  (avg) 
hepatitis         1.000  1.000  1.000  1.000 
glaucoma          0.195  0.195  0.195  0.195 
hypertension      0.171  0.171  0.171  0.171 
diarrhea          0.169  0.169  0.169  0.169 
impotence         0.169  0.169  0.169  0.169 
seizures          0.163  0.163  0.163  0.163 
dermatitis        0.155  0.155  0.155  0.155 
irritability      0.145  0.145  0.145  0.145 
psoriasis         0.144  0.144  0.144  0.144 
hypotension       0.130  0.130  0.130  0.130 
 
 
Query 1W:​
`psoriasis’,`heart failure’ 
Ordering: ​
min 
 
Proximity Network Results 
                      psoriasis  heart failure  (max)  (min)  (avg) 
dermatitis                0.125          0.115  0.125  0.115  0.120 
montelukast               0.083          0.114  0.114  0.083  0.099 
hypertension              0.159          0.068  0.159  0.068  0.113 
oxytocin                  0.060          0.066  0.066  0.060  0.063 
hypotension               0.058          0.100  0.100  0.058  0.079 
hepatitis                 0.144          0.057  0.144  0.057  0.101 
conjugated estrogens      0.051          0.065  0.065  0.051  0.058 
lidocaine                 0.050          0.091  0.091  0.050  0.071 
conjunctivitis            0.049          0.079  0.079  0.049  0.064 
drowsiness                0.048          0.050  0.050  0.048  0.049 
irritability              0.112          0.048  0.112  0.048  0.080 
itching                   0.109          0.046  0.109  0.046  0.077 
allopurinol               0.046          0.160  0.160  0.046  0.103 
heart failure             0.043          1.000  1.000  0.043  0.522 
psoriasis                 1.000          0.043  1.000  0.043  0.522 
bruising                  0.050          0.043  0.050  0.043  0.047 
histamine phosphate       0.043          0.083  0.083  0.043  0.063 
tachycardia               0.043          0.053  0.053  0.043  0.048 
verapamil                 0.042          0.077  0.077  0.042  0.060 
hydrocortisone            0.050          0.041  0.050  0.041  0.046 
 
Transitive Closure (proximity) Networks Results 
                psoriasis  heart failure  (max)  (min)  (avg) 
dermatitis          0.125          0.115  0.125  0.115  0.120 
montelukast         0.083          0.125  0.125  0.083  0.104 
dry skin            0.087          0.082  0.087  0.082  0.085 
hypotension         0.081          0.130  0.130  0.081  0.106 
elderberry          0.081          0.077  0.081  0.077  0.079 
irritability        0.112          0.077  0.112  0.077  0.094 
hypertension        0.159          0.074  0.159  0.074  0.116


## Page 35


naloxone            0.073          0.145  0.145  0.073  0.109 
allopurinol         0.072          0.160  0.160  0.072  0.116 
peppermint oil      0.075          0.072  0.075  0.072  0.074 
 
 
 
Query 1W:​
`psoriasis’,`hepatitis’ 
Ordering: ​
min 
 
Proximity Network Results 
                      psoriasis  hepatitis  (max)  (min)  (avg) 
diarrhea                  0.160      0.169  0.169  0.160  0.165 
hypertension              0.159      0.171  0.171  0.159  0.165 
psoriasis                 1.000      0.144  1.000  0.144  0.572 
hepatitis                 0.144      1.000  1.000  0.144  0.572 
glaucoma                  0.135      0.195  0.195  0.135  0.165 
dermatitis                0.125      0.155  0.155  0.125  0.140 
constipation              0.145      0.124  0.145  0.124  0.135 
stroke                    0.140      0.122  0.140  0.122  0.131 
infections                0.183      0.122  0.183  0.122  0.152 
irritability              0.112      0.145  0.145  0.112  0.128 
seizures                  0.108      0.163  0.163  0.108  0.135 
itching                   0.109      0.105  0.109  0.105  0.107 
osteoporosis              0.102      0.114  0.114  0.102  0.108 
irritation                0.105      0.100  0.105  0.100  0.103 
infertility               0.094      0.113  0.113  0.094  0.104 
vomiting                  0.091      0.126  0.126  0.091  0.108 
allergic                  0.088      0.084  0.088  0.084  0.086 
montelukast               0.083      0.094  0.094  0.083  0.088 
nausea                    0.076      0.080  0.080  0.076  0.078 
acetylsalicylic acid      0.073      0.113  0.113  0.073  0.093 
 
Transitive Closure (proximity) Networks Results 
              psoriasis  hepatitis  (max)  (min)  (avg) 
diarrhea          0.160      0.169  0.169  0.160  0.165 
hypertension      0.159      0.171  0.171  0.159  0.165 
psoriasis         1.000      0.144  1.000  0.144  0.572 
hepatitis         0.144      1.000  1.000  0.144  0.572 
glaucoma          0.135      0.195  0.195  0.135  0.165 
dermatitis        0.125      0.155  0.155  0.125  0.140 
constipation      0.145      0.124  0.145  0.124  0.135 
stroke            0.140      0.122  0.140  0.122  0.131 
infections        0.183      0.122  0.183  0.122  0.152 
irritability      0.112      0.145  0.145  0.112  0.128 
 
 
 
Query 1W:​
`psoriasis’,`seizures’ 
Ordering: ​
min


## Page 36


Proximity Network Results 
              psoriasis  seizures  (max)  (min)  (avg) 
infections        0.183     0.205  0.205  0.183  0.194 
hepatitis         0.144     0.163  0.163  0.144  0.153 
stroke            0.140     0.189  0.189  0.140  0.164 
diarrhea          0.160     0.122  0.160  0.122  0.141 
itching           0.109     0.109  0.109  0.109  0.109 
seizures          0.108     1.000  1.000  0.108  0.554 
psoriasis         1.000     0.108  1.000  0.108  0.554 
constipation      0.145     0.102  0.145  0.102  0.124 
osteoporosis      0.102     0.104  0.104  0.102  0.103 
glaucoma          0.135     0.101  0.135  0.101  0.118 
irritability      0.112     0.099  0.112  0.099  0.105 
infertility       0.094     0.150  0.150  0.094  0.122 
vomiting          0.091     0.150  0.150  0.091  0.120 
irritation        0.105     0.091  0.105  0.091  0.098 
hypertension      0.159     0.087  0.159  0.087  0.123 
dermatitis        0.125     0.084  0.125  0.084  0.104 
allergic          0.088     0.083  0.088  0.083  0.086 
acne              0.119     0.081  0.119  0.081  0.100 
ibuprofen         0.076     0.076  0.076  0.076  0.076 
appetite          0.076     0.078  0.078  0.076  0.077 
 
Transitive Closure (proximity) Networks Results 
              psoriasis  seizures  (max)  (min)  (avg) 
infections        0.183     0.205  0.205  0.183  0.194 
hepatitis         0.144     0.163  0.163  0.144  0.153 
stroke            0.140     0.189  0.189  0.140  0.164 
diarrhea          0.160     0.122  0.160  0.122  0.141 
constipation      0.145     0.121  0.145  0.121  0.133 
acne              0.119     0.113  0.119  0.113  0.116 
itching           0.109     0.109  0.109  0.109  0.109 
psoriasis         1.000     0.108  1.000  0.108  0.554 
seizures          0.108     1.000  1.000  0.108  0.554 
osteoporosis      0.102     0.104  0.104  0.102  0.103 
 
 
 
Query 1W:​
`psoriasis’,`heart failure’,`stroke’ 
Ordering: ​
min 
 
Proximity Network Results 
                      psoriasis  stroke  heart failure  (max)  (min)  (avg) 
hypertension              0.159   0.107          0.068  0.159  0.068  0.111 
dermatitis                0.125   0.065          0.115  0.125  0.065  0.102 
hepatitis                 0.144   0.122          0.057  0.144  0.057  0.108 
irritability              0.112   0.068          0.048  0.112  0.048  0.076 
itching                   0.109   0.080          0.046  0.109  0.046  0.078 
psoriasis                 1.000   0.140          0.043  1.000  0.043  0.394 
bruising                  0.050   0.052          0.043  0.052  0.043  0.048


## Page 37


montelukast               0.083   0.043          0.114  0.114  0.043  0.080 
oxytocin                  0.060   0.042          0.066  0.066  0.042  0.056 
glaucoma                  0.135   0.109          0.040  0.135  0.040  0.094 
drowsiness                0.048   0.039          0.050  0.050  0.039  0.046 
hydrocortisone            0.050   0.039          0.041  0.050  0.039  0.043 
diarrhea                  0.160   0.155          0.037  0.160  0.037  0.118 
vomiting                  0.091   0.131          0.035  0.131  0.035  0.086 
dizziness                 0.042   0.074          0.035  0.074  0.035  0.050 
lethargy                  0.035   0.045          0.043  0.045  0.035  0.041 
hypotension               0.058   0.034          0.100  0.100  0.034  0.064 
agitation                 0.040   0.033          0.041  0.041  0.033  0.038 
acetylsalicylic acid      0.073   0.064          0.032  0.073  0.032  0.056 
seizures                  0.108   0.189          0.030  0.189  0.030  0.109 
 
Transitive Closure (proximity) Networks Results 
              psoriasis  stroke  heart failure  (max)  (min)  (avg) 
irritability      0.112   0.086          0.077  0.112  0.077  0.091 
dermatitis        0.125   0.077          0.115  0.125  0.077  0.106 
hypertension      0.159   0.107          0.074  0.159  0.074  0.113 
dry skin          0.087   0.073          0.082  0.087  0.073  0.081 
itching           0.109   0.080          0.071  0.109  0.071  0.087 
hepatitis         0.144   0.122          0.071  0.144  0.071  0.112 
irritation        0.105   0.077          0.068  0.105  0.068  0.083 
hypotension       0.081   0.067          0.130  0.130  0.067  0.093 
elderberry        0.081   0.067          0.077  0.081  0.067  0.075 
montelukast       0.083   0.066          0.125  0.125  0.066  0.091 
 
 
 
Query 1W:​
`psoriasis’,`heart failure’,`stroke’ 
Ordering: ​
avg 
 
Proximity Network Results 
               psoriasis  stroke  heart failure  (max)  (min)  (avg) 
psoriasis          1.000   0.140          0.043  1.000  0.043  0.394 
stroke             0.140   1.000          0.027  1.000  0.027  0.389 
heart failure      0.043   0.027          1.000  1.000  0.027  0.357 
infections         0.183   0.213          0.024  0.213  0.024  0.140 
diarrhea           0.160   0.155          0.037  0.160  0.037  0.118 
hypertension       0.159   0.107          0.068  0.159  0.068  0.111 
seizures           0.108   0.189          0.030  0.189  0.030  0.109 
hepatitis          0.144   0.122          0.057  0.144  0.057  0.108 
constipation       0.145   0.141          0.020  0.145  0.020  0.102 
dermatitis         0.125   0.065          0.115  0.125  0.065  0.102 
glaucoma           0.135   0.109          0.040  0.135  0.040  0.094 
vomiting           0.091   0.131          0.035  0.131  0.035  0.086 
montelukast        0.083   0.043          0.114  0.114  0.043  0.080 
itching            0.109   0.080          0.046  0.109  0.046  0.078 
angina             0.031   0.021          0.179  0.179  0.021  0.077 
acne               0.119   0.099          0.010  0.119  0.010  0.076


## Page 38


irritability       0.112   0.068          0.048  0.112  0.048  0.076 
allopurinol        0.046   0.022          0.160  0.160  0.022  0.076 
infertility        0.094   0.121          0.008  0.121  0.008  0.074 
nausea             0.076   0.123          0.016  0.123  0.016  0.071 
 
Transitive Closure (proximity) Networks Results 
               psoriasis  stroke  heart failure  (max)  (min)  (avg) 
psoriasis          1.000   0.140          0.064  1.000  0.064  0.401 
stroke             0.140   1.000          0.048  1.000  0.048  0.396 
heart failure      0.064   0.048          1.000  1.000  0.048  0.371 
infections         0.183   0.213          0.052  0.213  0.052  0.149 
diarrhea           0.160   0.155          0.066  0.160  0.066  0.127 
seizures           0.108   0.189          0.052  0.189  0.052  0.116 
constipation       0.145   0.141          0.060  0.145  0.060  0.115 
hypertension       0.159   0.107          0.074  0.159  0.074  0.113 
hepatitis          0.144   0.122          0.071  0.144  0.071  0.112 
dermatitis         0.125   0.077          0.115  0.125  0.077  0.106 
 
 
 
 
Query 1W:​
`psoriasis’,`metformin’ 
Ordering: ​
min 
 
Proximity Network Results 
                      psoriasis  metformin  (max)  (min)  (avg) 
montelukast               0.083      0.098  0.098  0.083  0.091 
hypertension              0.159      0.070  0.159  0.070  0.114 
dermatitis                0.125      0.062  0.125  0.062  0.093 
hypotension               0.058      0.109  0.109  0.058  0.084 
hepatitis                 0.144      0.053  0.144  0.053  0.098 
oxytocin                  0.060      0.050  0.060  0.050  0.055 
lidocaine                 0.050      0.143  0.143  0.050  0.097 
vomiting                  0.091      0.049  0.091  0.049  0.070 
glaucoma                  0.135      0.047  0.135  0.047  0.091 
allopurinol               0.046      0.118  0.118  0.046  0.082 
heart failure             0.043      0.048  0.048  0.043  0.045 
verapamil                 0.042      0.111  0.111  0.042  0.077 
diarrhea                  0.160      0.042  0.160  0.042  0.101 
ibuprofen                 0.076      0.042  0.076  0.042  0.059 
naloxone                  0.040      0.128  0.128  0.040  0.084 
agitation                 0.040      0.040  0.040  0.040  0.040 
acetylsalicylic acid      0.073      0.038  0.073  0.038  0.056 
nicotine                  0.038      0.033  0.038  0.033  0.036 
angina                    0.031      0.070  0.070  0.031  0.051 
metformin                 0.031      1.000  1.000  0.031  0.516 
 
Transitive Closure (proximity) Networks Results 
                     psoriasis  metformin  (max)  (min)  (avg) 
montelukast              0.083      0.098  0.098  0.083  0.091


## Page 39


hypotension              0.081      0.109  0.109  0.081  0.095 
naloxone                 0.073      0.128  0.128  0.073  0.100 
allopurinol              0.072      0.118  0.118  0.072  0.095 
hypertension             0.159      0.070  0.159  0.070  0.114 
histamine phosphate      0.069      0.078  0.078  0.069  0.074 
dermatitis               0.125      0.068  0.125  0.068  0.097 
ribavirin                0.067      0.100  0.100  0.067  0.084 
tiotropium               0.067      0.100  0.100  0.067  0.084 
angina                   0.066      0.092  0.092  0.066  0.079 
 
 
 
 
Query 1W:​
`psoriasis’,`insulin glargine’ 
Ordering: ​
min 
 
Proximity Network Results 
                psoriasis  insulin glargine  (max)  (min)  (avg) 
lethargy            0.035             0.016  0.035  0.016  0.025 
metformin           0.031             0.013  0.031  0.013  0.022 
tenderness          0.019             0.010  0.019  0.010  0.014 
vomiting            0.091             0.009  0.091  0.009  0.050 
weakness            0.036             0.009  0.036  0.009  0.022 
bruising            0.050             0.007  0.050  0.007  0.029 
encephalopathy      0.006             0.024  0.024  0.006  0.015 
cranberry           0.057             0.006  0.057  0.006  0.032 
simvastatin         0.006             0.039  0.039  0.006  0.023 
licorice            0.036             0.006  0.036  0.006  0.021 
stroke              0.140             0.006  0.140  0.006  0.073 
liquorice           0.005             0.012  0.012  0.005  0.008 
sertraline          0.007             0.005  0.007  0.005  0.006 
diarrhea            0.160             0.005  0.160  0.005  0.082 
hydroxyzine         0.004             0.009  0.009  0.004  0.007 
hallucinations      0.030             0.004  0.030  0.004  0.017 
seizures            0.108             0.004  0.108  0.004  0.056 
migraine            0.043             0.004  0.043  0.004  0.023 
lithium             0.010             0.003  0.010  0.003  0.007 
sweating            0.033             0.003  0.033  0.003  0.018 
 
Transitive Closure (proximity) Networks Results 
                  psoriasis  insulin glargine  (max)  (min)  (avg) 
allopurinol           0.072             0.053  0.072  0.053  0.063 
anaphylaxis           0.048             0.048  0.048  0.048  0.048 
primidone             0.061             0.048  0.061  0.048  0.054 
sevelamer             0.061             0.048  0.061  0.048  0.054 
desmopressin          0.061             0.048  0.061  0.048  0.054 
rhinitis              0.048             0.056  0.056  0.048  0.052 
bethanechol           0.062             0.047  0.062  0.047  0.055 
cabergoline           0.062             0.047  0.062  0.047  0.055 
hypersensitivity      0.044             0.059  0.059  0.044  0.052


## Page 40


pharyngitis           0.044             0.046  0.046  0.044  0.045 
 
 
 
Query 1W:​
`psoriasis’,`stroke’ 
Ordering: ​
min 
 
Proximity Network Results 
              psoriasis  stroke  (max)  (min)  (avg) 
infections        0.183   0.213  0.213  0.183  0.198 
diarrhea          0.160   0.155  0.160  0.155  0.158 
constipation      0.145   0.141  0.145  0.141  0.143 
psoriasis         1.000   0.140  1.000  0.140  0.570 
stroke            0.140   1.000  1.000  0.140  0.570 
hepatitis         0.144   0.122  0.144  0.122  0.133 
glaucoma          0.135   0.109  0.135  0.109  0.122 
seizures          0.108   0.189  0.189  0.108  0.148 
hypertension      0.159   0.107  0.159  0.107  0.133 
acne              0.119   0.099  0.119  0.099  0.109 
infertility       0.094   0.121  0.121  0.094  0.108 
vomiting          0.091   0.131  0.131  0.091  0.111 
osteoporosis      0.102   0.090  0.102  0.090  0.096 
allergic          0.088   0.100  0.100  0.088  0.094 
weight loss       0.085   0.088  0.088  0.085  0.087 
itching           0.109   0.080  0.109  0.080  0.094 
appetite          0.076   0.111  0.111  0.076  0.093 
nausea            0.076   0.123  0.123  0.076  0.099 
ibuprofen         0.076   0.074  0.076  0.074  0.075 
rash              0.071   0.078  0.078  0.071  0.075 
 
Transitive Closure (proximity) Networks Results 
              psoriasis  stroke  (max)  (min)  (avg) 
infections        0.183   0.213  0.213  0.183  0.198 
diarrhea          0.160   0.155  0.160  0.155  0.158 
constipation      0.145   0.141  0.145  0.141  0.143 
psoriasis         1.000   0.140  1.000  0.140  0.570 
stroke            0.140   1.000  1.000  0.140  0.570 
hepatitis         0.144   0.122  0.144  0.122  0.133 
acne              0.119   0.115  0.119  0.115  0.117 
glaucoma          0.135   0.109  0.135  0.109  0.122 
seizures          0.108   0.189  0.189  0.108  0.148 
hypertension      0.159   0.107  0.159  0.107  0.133 
 
 
 
Query 1W:​
`glaucoma’ 
Ordering: ​
min 
 
Proximity Network Results 
                      glaucoma  (max)  (min)  (avg)


## Page 41


glaucoma                 1.000  1.000  1.000  1.000 
hepatitis                0.195  0.195  0.195  0.195 
hypertension             0.157  0.157  0.157  0.157 
psoriasis                0.135  0.135  0.135  0.135 
diarrhea                 0.120  0.120  0.120  0.120 
hypotension              0.111  0.111  0.111  0.111 
stroke                   0.109  0.109  0.109  0.109 
dermatitis               0.106  0.106  0.106  0.106 
montelukast              0.104  0.104  0.104  0.104 
vomiting                 0.101  0.101  0.101  0.101 
seizures                 0.101  0.101  0.101  0.101 
acetylsalicylic acid     0.095  0.095  0.095  0.095 
drowsiness               0.090  0.090  0.090  0.090 
allopurinol              0.079  0.079  0.079  0.079 
infections               0.078  0.078  0.078  0.078 
itching                  0.077  0.077  0.077  0.077 
irritability             0.076  0.076  0.076  0.076 
constipation             0.074  0.074  0.074  0.074 
osteoporosis             0.074  0.074  0.074  0.074 
lidocaine                0.073  0.073  0.073  0.073 
 
Transitive Closure (proximity) Networks Results 
              glaucoma  (max)  (min)  (avg) 
glaucoma         1.000  1.000  1.000  1.000 
hepatitis        0.195  0.195  0.195  0.195 
hypertension     0.157  0.157  0.157  0.157 
psoriasis        0.135  0.135  0.135  0.135 
diarrhea         0.120  0.120  0.120  0.120 
hypotension      0.111  0.111  0.111  0.111 
stroke           0.109  0.109  0.109  0.109 
dermatitis       0.106  0.106  0.106  0.106 
montelukast      0.104  0.104  0.104  0.104 
vomiting         0.101  0.101  0.101  0.101 
 
 
 
Query 1W:​
`glaucoma’,`psoriasis’ 
Ordering: ​
min 
 
Proximity Network Results 
                      psoriasis  glaucoma  (max)  (min)  (avg) 
hypertension              0.159     0.157  0.159  0.157  0.158 
hepatitis                 0.144     0.195  0.195  0.144  0.170 
glaucoma                  0.135     1.000  1.000  0.135  0.567 
psoriasis                 1.000     0.135  1.000  0.135  0.567 
diarrhea                  0.160     0.120  0.160  0.120  0.140 
stroke                    0.140     0.109  0.140  0.109  0.124 
dermatitis                0.125     0.106  0.125  0.106  0.116 
seizures                  0.108     0.101  0.108  0.101  0.104 
vomiting                  0.091     0.101  0.101  0.091  0.096


## Page 42


montelukast               0.083     0.104  0.104  0.083  0.093 
infections                0.183     0.078  0.183  0.078  0.131 
itching                   0.109     0.077  0.109  0.077  0.093 
irritability              0.112     0.076  0.112  0.076  0.094 
constipation              0.145     0.074  0.145  0.074  0.110 
osteoporosis              0.102     0.074  0.102  0.074  0.088 
acetylsalicylic acid      0.073     0.095  0.095  0.073  0.084 
infertility               0.094     0.067  0.094  0.067  0.081 
nausea                    0.076     0.067  0.076  0.067  0.071 
irritation                0.105     0.064  0.105  0.064  0.084 
allergic                  0.088     0.062  0.088  0.062  0.075 
 
Transitive Closure (proximity) Networks Results 
              psoriasis  glaucoma  (max)  (min)  (avg) 
hypertension      0.159     0.157  0.159  0.157  0.158 
hepatitis         0.144     0.195  0.195  0.144  0.170 
glaucoma          0.135     1.000  1.000  0.135  0.567 
psoriasis         1.000     0.135  1.000  0.135  0.567 
diarrhea          0.160     0.120  0.160  0.120  0.140 
stroke            0.140     0.109  0.140  0.109  0.124 
dermatitis        0.125     0.106  0.125  0.106  0.116 
seizures          0.108     0.101  0.108  0.101  0.104 
vomiting          0.091     0.101  0.101  0.091  0.096 
irritability      0.112     0.091  0.112  0.091  0.101 
 
 
 
Query 1W:​
`glaucoma’,`psoriasis’, `hepatitis’ 
Ordering: ​
min 
 
Proximity Network Results 
                      psoriasis  glaucoma  hepatitis  (max)  (min)  (avg) 
hypertension              0.159     0.157      0.171  0.171  0.157  0.162 
hepatitis                 0.144     0.195      1.000  1.000  0.144  0.446 
glaucoma                  0.135     1.000      0.195  1.000  0.135  0.443 
psoriasis                 1.000     0.135      0.144  1.000  0.135  0.426 
diarrhea                  0.160     0.120      0.169  0.169  0.120  0.150 
stroke                    0.140     0.109      0.122  0.140  0.109  0.124 
dermatitis                0.125     0.106      0.155  0.155  0.106  0.129 
seizures                  0.108     0.101      0.163  0.163  0.101  0.124 
vomiting                  0.091     0.101      0.126  0.126  0.091  0.106 
montelukast               0.083     0.104      0.094  0.104  0.083  0.094 
infections                0.183     0.078      0.122  0.183  0.078  0.128 
itching                   0.109     0.077      0.105  0.109  0.077  0.097 
irritability              0.112     0.076      0.145  0.145  0.076  0.111 
constipation              0.145     0.074      0.124  0.145  0.074  0.115 
osteoporosis              0.102     0.074      0.114  0.114  0.074  0.097 
acetylsalicylic acid      0.073     0.095      0.113  0.113  0.073  0.094 
infertility               0.094     0.067      0.113  0.113  0.067  0.091 
nausea                    0.076     0.067      0.080  0.080  0.067  0.074


## Page 43


irritation                0.105     0.064      0.100  0.105  0.064  0.090 
allergic                  0.088     0.062      0.084  0.088  0.062  0.078 
 
Transitive Closure (proximity) Networks Results 
              psoriasis  glaucoma  hepatitis  (max)  (min)  (avg) 
hypertension      0.159     0.157      0.171  0.171  0.157  0.162 
hepatitis         0.144     0.195      1.000  1.000  0.144  0.446 
glaucoma          0.135     1.000      0.195  1.000  0.135  0.443 
psoriasis         1.000     0.135      0.144  1.000  0.135  0.426 
diarrhea          0.160     0.120      0.169  0.169  0.120  0.150 
stroke            0.140     0.109      0.122  0.140  0.109  0.124 
dermatitis        0.125     0.106      0.155  0.155  0.106  0.129 
seizures          0.108     0.101      0.163  0.163  0.101  0.124 
vomiting          0.091     0.101      0.126  0.126  0.091  0.106 
irritability      0.112     0.091      0.145  0.145  0.091  0.116


## Page 44


Instagram Post Examples 
 
 
date: Sun, May 25 2014 @ 09:05 
“#notmypic .. Say hello to my new friend! Fluoxetina! Side effects by now are a bit of nausea and 
inquietude.. Better than zoloft! Yesterday night i started to cry while i was with my 2 friends because my ex, 
bulimia's stress.. I'm sure they thought i'm crazy so i felt like i had to explain my reasons with one of those 
friends.. Now i'm terrified of his reaction, he is even a friend of my ex.. Don't know what to expect.. It's so 
hard telling someone about ED and bulimia   . I'm also thinking about a b/p session today after 2 days 
clean, maybe it's not the right solution. Idk. #bulimia #bulimic #mia #ed #edfamily #eatingdisorder 
#prorecovery #bingepurge #purge #binge #fat #prozac #fluoxetine #depression #meds” 
 
date: Wed, May 13 2015 @ 20:05 
“​
I start ​
fluoxetine (D)​
 tomorrow, the doctor switched me from citalopram to this so let's hope it goes better 
this time #anxietymeds #depressionmeds #citalopram​
#fluoxetine (D)​
 ​
#anxiety (AE)​
#depression” 
 
then, same user on the next day: 
 
“ok so I don't know if it's the tablets that are doing this but I feel the lowest I've ever felt and I'm hoping it's 
not the tablets. Hopefully it's just a bad day, not that there are many good days  I hope tomorrow is a better 
day for everyone, especially if you are feeling the same way I am. #fluoxetine (D) #depression (AE) #anxiety 
#depressionmeds #anxietymeds” 
 
date: Wed, Dec 24 2014 @ 10:12 
“I've gained a significant amount of weight since this summer... It's hard.. It's too much for someone to ask if 
I'm okay or not. Screw people.. #me #statistic #unhappy #depression (AE) #fluoxetine (D) #christmaseve 
#yule #hurt #toomanythoughts 
 
date: Wed, Feb 05 2014 @ 14:02 
“i survived another trip to the clinic, saw a specialist, did a test that explained i'm an INFJ (introvert) which is 
apperently only 1% of the population. Added risperidone and upped ritalin as well as prozac. considering this 
keeps me "sane" and able to assimilate into the chaos of everyday life i think this counts as my 
#100happydays today #findhappinessineachday #bipolar #borderlinepersonalitydisorder #INFJ 
#manicdepression #goinggovernment #prozac #lamotragine #ritalin #risperidone” 
 
date: Tue, Mar 31 2015 @ 18:03 
“Anyone has ever tried Prozac !? If so... please share ur feedback 
I'd be thankful xo #Depression #anxiety #Bipolar #Prozac #mood_swings

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.05195v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.05195v1_retina-VAE__Variationally_Decoding_the_Spectrum_of_Macular_Disease

> Source: 1907.05195v1_retina-VAE__Variationally_Decoding_the_Spectrum_of_Macular_Disease.pdf

> Pages: 11

---


## Page 1


retina-VAE: Variationally Decoding the Spectrum of
Macular Disease
Stephen G. Odaibo∗
(1) Department of Machine Learning Research
RETINA-AI Health, Inc.
(2) Department of Head & Neck Surgery
Ophthalmology Section
MD Anderson Cancer Center
stephen.odaibo@retina-ai.com
Abstract
In this paper, we seek a clinically-relevant latent code for representing the spec-
trum of macular disease. Towards this end, we construct retina-VAE, a variational
autoencoder-based model that accepts a patient proﬁle vector (pVec) as input. The
pVec components include clinical exam ﬁndings and demographic information.
We evaluate the model on a subspectrum of the retinal maculopathies, in particular,
exudative age-related macular degeneration, central serous chorioretinopathy, and
polypoidal choroidal vasculopathy. For these three maculopathies, a database of
3000 6-dimensional pVecs (1000 each) was synthetically generated based on known
disease statistics in the literature. The database was then used to train the VAE and
generate latent vector representations. We found training performance to be best for
a 3-dimensional latent vector architecture compared to 2 or 4 dimensional latents.
Additionally, for the 3D latent architecture, we discovered that the resulting latent
vectors were strongly clustered spontaneously into one of 14 clusters. Kmeans was
then used only to identify members of each cluster and to inspect cluster properties.
These clusters suggest underlying disease subtypes which may potentially respond
better or worse to particular pharmaceutical treatments such as anti-vascular en-
dothelial growth factor variants. The retina-VAE framework will potentially yield
new fundamental insights into the mechanisms and manifestations of disease. And
will potentially facilitate the development of personalized pharmaceuticals and
gene therapies.
1
Introduction
In current clinical practice, physicians see patients and based on a combination of objective and
subjective information gathered, make a diagnoses of the condition. The diagnosis is however
typically based on a rigid and mutually exclusive classiﬁcation of the disease. This system is brittle as
it does not take into account that most diseases manifest between and outside of these rigid classes, and
it does not provide opportunity for personalized diagnosis and treatment. Increasingly as clinicians
become more aware of the inadequacies of the current system, there is a concept of “Spectrum of
disease.” It recognizes that the genetic, metabolic, environmental, and demographic proﬁle of a
patient points to predilection for speciﬁc manifestations which may be better or less responsive to
any particular treatment. In the case of the retinal maculopathies for instance, a prototypical one is
age-related macular degeneration (ARMD), which in a certain subtype progresses into an exudative
state which requires intravireal injections with anti vascular endothelial growth factor (anti-VEGF)
∗Correspondence: RETINA-AI Health, Inc. P.O.Box 20169, Houston TX
Preprint. Under review.
arXiv:1907.05195v1  [eess.IV]  11 Jul 2019


## Page 2


(a)
(b)
Figure 1: (a) Normal retina (b) Retina with age-related macular degeneration showing large diffuse
soft conﬂuent drusen (yellow dots)
injections. In the absence of this treatment, patients will often go blind. It is known to practicing
retina specialists that there are multiple manifestations of this condition, simply based on the broad
range of presentations and responses to treatment. However, this notion is yet to be rigorously
quantiﬁed and described. For instance, certain patients with what would appear to be central serous
chorioretinopathy, do progress to develop choroidal neovascular membranes and respond positively to
intravitreal injections of anti-VEGF. Similarly, polypoidal choroidal vasculopathy is another related
disease with clear distinctions from ARMD, that also requires intravitreal injections for treatment. In
this paper, we sought out to develop a framework for the study and characteization of this notion of a
“spectrum of macular disease,” a notion that if properly described, can potentially yield signiﬁcant
advances in the development of personalized pharmaceuticals and gene therapies.
From a methodological standpoint, the notion of seeking latent codes that represent a data distribution
is certainly not new. Various techniques and efforts such as principal component analysisJolliffe
(2011) and kmeans clusteringMacQueen et al. (1967); Wagstaff et al. (2001); Coates et al. (2011);
Coates and Ng (2012) have been ongoing for a while in the statistics community. Within machine
learning, there has been some early work in adversarial generative modelingSchmidhuber (1992), and
more recently, a great surge of interest since the entry of generative adversarial networks Goodfellow
et al. (2014); Radford et al. (2015); Mirza and Osindero (2014). Another class, autoencoding
algorithms generate a latent representation and then reconstruct the input data from the latent using
the data itself as the labelLe et al. (2011); Hinton and Salakhutdinov (2006); Lee et al. (2009);
Vincent et al. (2010); Ngiam et al. (2011). These did not yield a continuous latent space, and as such
were not truly generative in the sense of having capacity to generate meaningful (or interpretable)
data for any point in the latent space. This was addressed by Kingma and Welling via variational
autoencodersKingma et al. (2013), which is what we have adopted in retina-VAE. We see variational
inference as particularly suitable for the problem of discovering latent features which hold diagnostic
and therapeautic relevance.
There has been some related work using VAEs to determine relevant latent representations for
disease stratiﬁcation. For instance, Way et al used VAEs to extract a latent space from cancer
transcriptomesWay et al. (2017). Rampasek et al used VAEs to deduce latent space of drug response
in cancer cell lines. And Cohen et al used an autoencoder to obtain a representation of in situ
hybridization images.Cohen et al. (2017). No studies to date have yet been done on utilizing
variational autoencoders to determine clinically relevant latent spaces for retinal disease diagnosis.
2
Background
The retina is the sensory tissue in the back of the eye. It contains the photoreceptors which absorb
light and transmit a signal onwards to the primary visual cortex (area V1) via the optic nerve. Figure 1
(a) shows a normal retina. Various diseases can affect the retina resulting in vision loss and blindness.
One such disease is age-related macular degeneration (ARMD)Vinding et al. (1989) which is the
leading cause of blindness in people over the age of 50 in the United States. Figure 1 (b) shows
the retina of a patient with ARMD. The condition often starts out in a “non-exudative” state and
progresses with age into an “exudative” state, because of renegade blood vessels called choroidal
neovascular membranes which pathologically arise from the choroid, the vascular layer underneath
2


## Page 3


the retina, and break through bruch’s membrane and into the subretinal space where they leak and
cause vision loss. When such an exudative transformation occurs, to decrease vision loss and prevent
blindness intravitreal injections of anti-VEGF are required typically anywhere from monthly to once
every 3 months.
Central serous chorioretinopathy (CSCR)Liew et al. (2013); Castro-Correia et al. (1992) is another
disease of the macular and associated central choroid. It typically occurs in men in their 30s to
40sCastro-Correia et al. (1992); Tsai et al. (2013) and has been associated with stress or steroid
usage. Typically, this condition resolves on its own within a few weeks and does not require particular
intervention, other than a caution to abstain from any steroid use such as in nasal sprays. In its more
common form, CSCR is not thought of as being related to ARMD. However, in some instances,
CSCR can become chronic and can develop choroidal neovascular membranes requiring treatment
with anti-VEGFs. This is typically termed “atypical CSCR” and is understood to be somewhere in the
spectrum of ARMD. It is not currently understood why some patients with CSCR follow a different
prognostic course and end up requiring intravitreal injections potentially indeﬁnitely, while most
others have complete resolution of symptoms within weeks without ever having a recurrence, and yet
others have complete resolution within weeks, but then have recurrences periodically. Variational
substratiﬁcation of the disease and discovery of relevant latent represenattion codes will likely help
answer these open questions.
Polypoidal choroidal vasculopathy (PCV) is another related condition, one in which polyps patholog-
ically arise in the choroid. The polyps leak and can progressively disrupt bruch’s membrane, causing
choroidal neovascular membranes, subretinal hemorrhages (bleeds), and vision loss. The condition
is often confused with exudative ARMD. Similarly to exudative ARMD, it responds positively to
intravireal injections of anti-VEGF. This condition is most common in persons of Asian or African
ancestry, but is increasingly being recognized in perons of European ancestry as well. PCV was not
historically associated with drusen, however it is increasingly recognized that drusen-like deposits
do occur in PCV patients. Such pattern is a recurrent theme undermining the traditional notion of
singular ‘hallmark feature switches’ which can absolutely discriminate between diseases. As these
once presumed ‘absolute discriminants’ are increasingly found with some, albeit lower, probability
in the alternative diagnoses. This further underscores the need for probabilistic models which can
distill clinically-relevant latent representation codes, and variationally infer classes of disease for
personalized treatment.
In variational inference, the goal often is to determine a posterior distribution p(z|x) of a latent
variable z given some data evidence x. However, determining this posterior distribution is typically
computationally intractible, because according to Bayes,
p(z|x) =
Z
z
p(x|z)p(z)
p(x)
dz,
(1)
which is intractible because it involves computing the integral over the entire latent space z, and
also typically because it requires knowledge or computation of the entire evidence distribution p(x).
To circumvent this intractibility problem one instead approximates the posterior with some other
distribution q(z|x) in a manner that minimizes some similarity measure between the true posterior
and the approximation, q. Here we use the Kullback-Leibler, DKL:
DKL(q(z|xi)||p(z|xi)) =
Z
q(z|xi) log q(z|xi)
p(z|xi)dz,
(2)
which when manipulated in the above yields the below
log p(xi) = DKL(q(z|xi)||p(z|xi)) + Eq(z|xi) [log p(z, xi) −log q(z|xi)] .
(3)
Since DKL ≥0, it follows that
log p(xi) ≥Eq(z|xi) [log p(z, xi) −log q(z|xi)] .
(4)
3


## Page 4


(a)
(b)
(c)
(d)
(e)
Figure 2: (a) Racial Distribution of Exudative Age-Related Macular Degeneration (ARMD) (b)
Racial Distribution of Central Serous Chorioretinopathy (CSCR) (c) Racial Distribution of Polypoidal
Choroidal Vasculopathy (PCV) (d) Distribution of polyps, drusen, and subretinal hemorrhage in
ARMD, CSR, and PCV (e) Age Distributions of exudative ARMD, of CSCR, and of PCV.
Therefore maximizing the log likelihood of the data is synonymous with maximizing the term on the
right, the variational lower bound L. In the manner of Kingma et al Kingma et al. (2013), we utilize
the variational lower bound as the loss function of our VAE. It can be reexpressed as:
L = Eq(z|xi) [log p(z, xi) −log q(z|xi)] =
Z
z
q(z|xi) [log p(z, xi) −log q(z|xi)] dz
(5)
L =
Z
z
q(z|xi) log p(z, xi)
q(z|xi) dz =
Z
z
q(z|xi) log p(xi|z)p(z)
q(z|xi)
dz
(6)
L =
Z
z
q(z|xi) log
p(z)
q(z|xi)dz +
Z
z
q(z|xi) log p(xi|z)dz
(7)
L = −DKL(q(z|xi)||p(z)) + Eq(z|xi) [log p(xi|z)]
(8)
Choosing a gaussian latent prior and a gaussian approximate posterior yields a closed form for the
DKL term. The resulting loss function is then:
L = −1
2
J
X
j=1
 1 + log(σ2
j ) −µ2
j −σ2
j

+ 1
L
L
X
l=1
Eq(z|xi)
h
log p(xi|z(i,l))
i
(9)
where J is the dimension of the latent, σj and µj are parameters of the approximate posterior, q, and
L is the number of samples stochastically drawn utilizing the reparametrization trickKingma et al.
(2013).
3
Methods
Three thousand patient proﬁle vectors (pVec) were generated based on literature on the epidemiology
of the three maculopathies under study. Mean values and distribution information was obtained,
distribution models built, and then sampling carried out on the distributions. The pVec consisted of
the following 6 components: race, age, presence or absence of polyps, presence or absence of drusen
or drusen-like deposits, presence or absence of subretinal hemorrhage (SRH), and sex. The random
variables polyps, drusen, SRH, and sex had values of either 0 or 1. The race categories were asian,
black, caucasian, hispanic, and other. The age random variable was continuous, assuming values in
the positive reals.
4


## Page 5


Figure 3: Training Spectral-VAE with 2, 3, and 4 dimensional latent
Figure 4: Composite Latent Vector Map
Data Model
For the data model, it was noted that CSCR has a median age of about 36 to 39 yearsCastro-Correia
et al. (1992); Tsai et al. (2013). Hence for the CSCR age distribution model, we used a mean age of
39 years and a variance of 60. The mean age of patients affected with PCV varied by study between
55 and 68 years Sho et al. (2003); Yannuzzi et al. (2012). Hence for the PCV age distribution model
we used a mean age of 60 years and a variance of 40. The average age of patients with exudative
(a)
(b)
(c)
(d)
Figure 5: (a) 3D latent vector space of exudative ARMD (b) 3D latent vector space of CSCR (c) 3D
latent vector space of PCV (d) 3D latent vector space composite of exudative ARMD, CSCR, and
PCV
5


## Page 6


(a)
(b)
(c)
(d)
(e)
(f)
(g)
(h)
(i)
(j)
(k)
(l)
(m)
(n)
Figure 6: (a) Cluster 1 (b) Cluster 2 (c) Cluster 3 (d) Cluster 4 (e) Cluster 5 (f) Cluster 6 (g) Cluster 7
(h) Cluster 8 (i) Cluster 9 (j) Cluster 10 (k) Cluster 11 (l) Cluster 12 (m) Cluster 13 (n) Cluster 14
ARMD is about 80 years Jonas et al. (2003). Hence for exudative ARMD we used a mean age of
80 years and a variance of 80 in the data model. Figure 2 (e) shows age distribution of exudative
ARMD, of CSCR, and of PCV used in our data model. Notably, exudative ARMD is most common
amongst asians and caucasians and least common amongst blacks and hispanics Friedman et al.
(1999); Kawasaki et al. (2010); Vanderbeek et al (2011); Klein et al. (2006). Figure 2 (a) shows the
racial distribution of exudative ARMD used in our data model. PCV is notably more common in
people of Asian and African descent than in other racial groups Ciardella et al. (2004); Imamura et al.
(2010), while CSCR is most common in asians, caucasians, and hispanics, and is relatively rare in
blacks Liew et al. (2013); Desai et al. (2003); Ahlers et al. (2009); Lin et al. (2016). Figures 2 (b)
and (c) respectively show the racial distribution of CSCR and of PCV used in our data model. In
exudative ARMD, CSCR, and PCV, we respectively used [0.39, 0.01, 0.5, 0.05,0.05], [0.33, 0.05,
0.32, 0.25, 0.05], and [0.4, 0.3, 0.10, 0.18, 0.02] as the categorical distributions amongst asians,
blacks, caucasians, hispanics, and other races respectively. Drusen and drusen-like deposits have
been observed in up to one third of patients with PCV Lafaut et al. (2000); Iwama et al. (2008). In
our model we use 28% coincidence of drusen and PCV. Drusen or drusen-like deposits are known
to occur in CSCR Schatz et al. (1992); Chumbley et al. (1974) even though this is not a common
occurence. We model with 10% drusen or drusen-like occurence conincident with CSCR. About one
third of patients with PCV were found to have large subretinal hemorrhage in one study Byeon et al.
(2008). No deﬁnite sex predilection has been established for PCV Yannuzzi et al. (1999). Neither has
there been any deﬁnite sex predilection established for exudative ARMD Vinding et al. (1989). Of
note, for exudative ARMD a few studies have noted some potentially race-speciﬁc sex predilection in
either directionMaruko et al. (2007); Rudnicka et al. (2012), but nothing deﬁnite across the board. In
our data model we used a uniform bernouli distribution for sex of PCV and exudative ARMD patients.
6


## Page 7


Table 1: Cluster characteristics
ID
Size
Race
Age
Polyps
Drusen
SRH
Sex
1
249
[249,0,0,0,0]
[26,56,86]
[249,0]
[189,60]
[68,181]
[249,0]
2
198
[0,35,163,0,0]
[23,39,70]
[0,198]
[0,198]
[8,190]
[198,0]
3
298
[0,8,229,35,0]
[23,79,104]
[0,298]
[298,0]
[57,241]
[0,298]
4
220
[220,0,0,0,0]
[24,79,105]
[0,220]
[220,0]
[41,179]
[220,0]
5
339
[0,141,78,104,16]
[21,60,104]
[339,0]
[112,227]
[101,238]
[0,339]
6
225
[225,0,0,0,0]
[30,61,92]
[225,0]
[71,154]
[66,159]
[0,225]
7
203
[0,129,74,0,0]
[20,57,78]
[203,0]
[37,166]
[55,148]
[203,0]
8
186
[186,0,0,0,0]
[30,78,107]
[0,186]
[186,0]
[32,154]
[0,186]
9
348
[0,11,268,43,26]
[22,79,106]
[0,348]
[348,0]
[54,294]
[348,0]
10
154
[0,17,60,61,16]
[14,40,75]
[0,154]
[0,154]
[8,146]
[0,154]
11
165
[165,0,0,0,0]
[22,40,75]
[0,165]
[0,165]
[7,158]
[165,0]
12
69
[69,0,0,0,0]
[22,39,59]
[0,69]
[0,69]
[4,65]
[0,69]
13
195
[0,0,36,141,18]
[25,60,91]
[195,0]
[77,118]
[61,134]
[195,0]
14
151
[0,0,0,134,17]
[18,39,63]
[0,151]
[0,151]
[11,140]
[151,0]
Table 2: The ‘Size’ col is number of patients in cluster. ‘Race’ col shows race distribution with
notation: [Asian, Black, Caucasian, Hispanic, Other]. ‘Age’ column shows the age distribution as
[min age, median age, max age]. ‘Polyps,’ ‘Drusen,’ and ‘SRH’ cols show respective distributions
as [number with, number without]. And ‘Sex’ col shows sex distribution as [number male, number
female].
In CSCR, there is a signiﬁcant male preponderence ranging anywhere from 1:3 to 1:7 Roberts
et al. (2016); Kitzmann et al. (2008). Our dataset has been made publicly available for download at
https://github.com/VeryVeryGoodNews/retina-VAE.
Model Architecture
The VAE was implemented in Keras using the loss function described in Equation 9 above. The
model architecture’s encoder part consisted on 6-dimensional input vector, one hidden layer of size
512, and latent vectors of varying dimensions (2, 3, and 4) were set in experiment runs. For the
encoder network, a reLu was used as the activation function of the hidden layer, and a linear activation
function was used in the output. For the decoder network, a reLu was used for the activation function
of the hidden layer, while a sigmoid was used in the output layer. The decoder part of the model
also consisted of a single hidden layer of size 512 and a 6 dimensional output. Training was done
on an NVIDIA Tesla V100 GPU with 16 GB RAM. And the number of iterations on the VAE was
set to 1000 epochs. The reparametrization trickKingma et al. (2013) was utilized for the stochastic
sampling of the latent vector during training. The loss function was plotted to monitor training. The
code is available for download at https://github.com/VeryVeryGoodNews/retina-VAE.
4
Experiments & Results
After training the VAE, the encoder network was detached such that the latent vector, z was encoder
output. Inference was then run on this trained encoder to determine the latent vectors that corresponded
to each pVec vector in the training set. The latent vectors were plotted in the 3D latent case and
14 spontaneously formed clusters were visually observed as shown in Figure 5. Upon observation
of these 14 clusters, kmeans was run with a cluster size set to 14, so as to identify the members of
the individual clusters. The overlay of latent vectors of all 3 maculopathies under study is shown
in Figure 5 (d). Notably, 8 of the 14 clusters were found to contain representatives from all 3
maculopathies under study. Those 8 are clusters 4, 5, 6, 8, 9, 10, 12, and 14. On the other hand, 6 of
the 14 clusters were found to contain representatives from only CSCR and PCV. Those 6 clusters are
clusters 1, 2, 3, 7, 11, and 13. The sizes of the clusters varied as shown in Table 1. The ‘ID’ column
shows the cluster ID, i.e cluster 1 has ID of 1. The ‘Size’ column shows number of patients in the
cluster. The ‘Race’ column shows the race distribution in the cluster, and we have used notation
[Asian, Black, Caucasian, Hispanic, Other]. The ‘Age’ column shows the age distribution of the
7


## Page 8


cluster, shown as [min age, median age, max age]. The ‘Polyps’ column shows the polyps distribution
of patients in the cluster, shown as [number with, number without]. The ‘Drusen’ column shows
the ‘drusen’ distribution of patients in the cluster, shown as [number with, number without]. The
‘SRH’ column shows the subretinal hemorrhage distribution in the cluster, shown as [number with,
number without]. And the ‘Sex’ column shows the sex distribution in the cluster, shown as [number
male, number female]. Interestingly, the polyps and sex attributes were not mixed between clusters in
the sense that for any given cluster, the patients in the cluster either all had polyps or none of them
had polyps; also, they were either all male or all female. Also interesting was the number of clusters
which had all Asians and no other races. Those clusters are 1, 4, 6, 8, 11, and 12. No other races were
the sole occupants of any cluster. Clusters 2, 12, and 14 had the lowest median ages of 39. Clusters
10 and 11 also had young median ages of 40. Clusters 3, 4, and 9 had the oldest median ages of 79,
and cluster 8 was close with a median age of 78. Subretinal hemorrhage was the only categorical
random variable that was completely mixed amongst the clusters, i.e. all clusters had some but not all
patients with SRH.
5
Discussion
The determination of clinically-relevant latent codes holds the key to personalized medicine, and
represents a critical step in that direction. It is interesting to ask how retina-VAE mechanistically
went about grouping the pVecs into these 14 classes. In statistical machine learning, dimensionality
reduction is often presented as a process in which irrelevant information is discarded. However, our
result here makes it apparent that dimensionality reduction can be an intelligent and more efﬁcient
rearrangement of information to ﬁt into smaller dimensions. In this sense, one can think of the 14
clusters as representing an additional coordinate in the address space of the disease representation.
For instance, such that when the decoder network “reads” a latent vector as arising from cluster 4
and knows to reconstruct that pVec as being of the Asian race and male sex. However, there are 14
spontaneous clusters yet only 4 or less of any given attribute in the pVec. Therefore, clearly as shown
in Table 1, most clusters have a mixture of multiple different categories of any given random variable.
And these clusters are likely to have biological relevance and hold insights into the mechanisms of
macular disease.
The concept of dimensionality reduction such as going from a 6 dimensional pVec to a 3D latent
space is clinically appealing as it agrees with our intuition and clinical practice. It agrees with the
notion that common pathophysiology and therefore common pharmacology connects and determines
diseases in a spectrum. This concept of a spectrum of diseases is what we have set out here to
decode for the maculopathies. Notably, all three of the maculopathies under study have forms
or states that require treatment with anti-VEGF drugs. Exudative ARMD and exudative PCV are
treated with anti-VEGF in common and standard clinical practice, while atypical CSCR is a less
common state often considered (or confused with) a variant of exudative ARMD. All three conditions
pathophysiologically involve or can progress towards a disruption of Bruch’s membrane and the
subsequent formation of a choroidal neovascular membrane. Once in this state, all three of these
maculopathies respond positively to intravitreal injection of anti-VEGF. This all suggests common
physiological pathways which converge under certain circumstances.
As shown in Figure 6, within each of the 14 clusters, the individual maculopathies are visually and
computationally separable. Thus suggesting a multidimensional spectrum that could yield fundamen-
tal insights about which patients will respond better or worse to what drugs. And consequently, about
how to develop the best drugs.
6
Conclusion
We have introduced, retina-VAE, a novel application of variational autoencoders towards determining
a clinically relevant latent space for exudative macular degeneration and related conditions which
require treatment with anti-VEGF agents. The latent vectors spontaneously formed into 14 clinically-
relevant clusters which are candidates for further disease characterization, personalized intervention,
and optimal pharmaceutical development.
8


## Page 9


7
Future Work
The authors plan to further characterize and study the 14 clusters which formed spontaneously
in retina-VAE. A clinical study will be conducted in which patients at our health center will be
prospectively classiﬁed into one of the 14 clusters by running inference using the trained retina-VAE
model. These patients will then be followed to assess their phenotypic characteristics such as disease
course, response to anti-VEGF treatment, injection interval, genetic proﬁle, co-morbidities, family
history, and environmental exposures. This information could then potentially be used to provide
treatment recommendations to optimize patient outcomes and to facilitate new drug development.
Acknowledgments
The author thanks Google Cloud for providing the compute resources used in the experiments.
References
Castro-Correia J, Coutinho MF, Rosas V, Maia J. Long-term follow-up of central serous retinopathy in 150
patients. Documenta Ophthalmologica. 1992 Dec 1;81(4):379-86.
Tsai DC, Chen SJ, Huang CC, Chou P, Chung CM, Huang PH, Lin SJ, Chen JW, Chen TJ, Leu HB, Chan WL.
Epidemiology of idiopathic central serous chorioretinopathy in Taiwan, 2001–2006: a population-based study.
PLoS One. 2013 Jun 24;8(6):e66858.
Sho K, Takahashi K, Yamada H, Wada M, Nagai Y, Otsuji T, Nishikawa M, Mitsuma Y, Yamazaki Y, Mat-
sumura M, Uyama M. Polypoidal choroidal vasculopathy: incidence, demographic features, and clinical
characteristics. Archives of Ophthalmology. 2003 Oct 1;121(10):1392-6.
Yannuzzi LA, Sorenson J, Spaide RF, Lipson B. Idiopathic polypoidal choroidal vasculopathy (IPCV). Retina.
2012 Feb 1;32:1-8.
Jonas JB, Kreissig I, Hugger P, Sauder G, Panda-Jonas S, Degenring R. Intravitreal triamcinolone acetonide for
exudative age related macular degeneration. British Journal of Ophthalmology. 2003 Apr 1;87(4):462-8.
Friedman DS, Katz J, Bressler NM, Rahmani B, Tielsch JM. Racial differences in the prevalence of age-related
macular degeneration: the Baltimore Eye Survey. Ophthalmology. 1999 Jun 1;106(6):1049-55.
Kawasaki R, Yasuda M, Song SJ, Chen SJ, Jonas JB, Wang JJ, Mitchell P, Wong TY. The prevalence of age-
related macular degeneration in Asians: a systematic review and meta-analysis. Ophthalmology. 2010 May
1;117(5):921-7.
Vanderbeek BL, Zacks DN, Talwar N, Nan B, Musch DC, Stein JD. Racial differences in age-related macular
degeneration rates in the United States: a longitudinal analysis of a managed care network. American journal
of ophthalmology. 2011 Aug 1;152(2):273-82.
Ciardella AP, Donsoff IM, Huang SJ, Costa DL, Yannuzzi LA. Polypoidal choroidal vasculopathy. Survey of
ophthalmology. 2004 Jan 1;49(1):25-37.
Imamura Y, Engelbert M, Iida T, Freund KB, Yannuzzi LA. Polypoidal choroidal vasculopathy: a review. Survey
of ophthalmology. 2010 Nov 1;55(6):501-15.
Liew G, Quin G, Gillies M, Fraser-Bell S. Central serous chorioretinopathy: a review of epidemiology and
pathophysiology. Clinical & experimental ophthalmology. 2013 Mar;41(2):201-14.
Desai UR, Alhalel AA, Campen TJ, Schiffman RM, Edwards PA, Jacobsen GR. Central serous chorioretinopathy
in African Americans. Journal of the National Medical Association. 2003 Jul;95(7):596.
Ahlers C, Geitzenauer W, Stock G, Golbaz I, Schmidt-Erfurth U, Prünte C. Alterations of intraretinal layers in
acute central serous chorioretinopathy. Acta ophthalmologica. 2009 Aug;87(5):511-6.
Lin J, Chen RW. Central serous chorioretinopathy. InManual of Retinal Diseases 2016 (pp. 421-426). Springer,
Cham.
Lafaut BA, Leys AM, Snyers B, Rasquin F, De Laey JJ. Polypoidal choroidal vasculopathy in Caucasians.
Graefe’s archive for clinical and experimental ophthalmology. 2000 Sep 1;238(9):752-9.
Iwama D, Tsujikawa A, Sasahara M, Hirami Y, Tamura H, Yoshimura N. Polypoidal choroidal vasculopathy
with drusen. Japanese journal of ophthalmology. 2008 Apr 1;52(2):116-21.
9


## Page 10


Schatz H, Madeira D, Johnson RN, McDonald HR. Central Serous Chonoretinopathy Occurring in Patients 60
Years of Age and Older. Ophthalmology. 1992 Jan 1;99(1):63-7.
Chumbley LC, Frank RN. Central serous retinopathy and pregnancy. American journal of ophthalmology. 1974
Feb 1;77(2):158-60.
Maruko I, Iida T, Saito M, Nagayama D, Saito K. Clinical characteristics of exudative age-related macular
degeneration in Japanese patients. American journal of ophthalmology. 2007 Jul 1;144(1):15-22.
Vinding T. Age-related macular degeneration. Macular changes, prevalence and sex ratio: An epidemiological
study of 1000 aged individuals. Acta ophthalmologica. 1989 Dec;67(6):609-16.
Varma R, Fraser-Bell S, Tan S, Klein R, Azen SP, Los Angeles Latino Eye Study Group. Prevalence of
age-related macular degeneration in Latinos: the Los Angeles Latino eye study. Ophthalmology. 2004 Jul
1;111(7):1288-97.
Rudnicka AR, Jarrar Z, Wormald R, Cook DG, Fletcher A, Owen CG. Age and gender variations in age-related
macular degeneration prevalence in populations of European ancestry: a meta-analysis. Ophthalmology. 2012
Mar 1;119(3):571-80.
Klein R, Klein BE, Knudtson MD, Wong TY, Cotch MF, Liu K, Burke G, Saad MF, Jacobs Jr DR. Prevalence
of age-related macular degeneration in 4 racial/ethnic groups in the multi-ethnic study of atherosclerosis.
Ophthalmology. 2006 Mar 1;113(3):373-80.
Byeon SH, Lee SC, Oh HS, Kim SS, Koh HJ, Kwon OW. Incidence and clinical patterns of polypoidal choroidal
vasculopathy in Korean patients. Japanese journal of ophthalmology. 2008 Feb 1;52(1):57-62.
Yannuzzi LA, Wong DW, Sforzolini BS, Goldbaum M, Tang KC, Spaide RF, Freund KB, Slakter JS, Guyer
DR, Sorenson JA, Fisher Y. Polypoidal choroidal vasculopathy and neovascularized age-related macular
degeneration. Archives of Ophthalmology. 1999 Nov 1;117(11):1503-10.
Roberts P, Baumann B, Lammer J, Gerendas B, Kroisamer J, Bühl W, Pircher M, Hitzenberger CK, Schmidt-
Erfurth U, Sacu S. Retinal pigment epithelial features in central serous chorioretinopathy identiﬁed by
polarization-sensitive optical coherence tomography. Investigative ophthalmology & visual science. 2016 Apr
1;57(4):1595-603.
Kitzmann AS, Pulido JS, Diehl NN, Hodge DO, Burke JP. The incidence of central serous chorioretinopathy in
Olmsted County, Minnesota, 1980–2002. Ophthalmology. 2008 Jan 1;115(1):169-73.
Kingma DP, Welling M. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114. 2013 Dec 20.
Coates, A., Ng, A., and Lee, H. (2011). An analysis of single-layer networks in unsupervised feature learning. In
Proceedings of the fourteenth international conference on artiﬁcial intelligence and statistics, pages 215–223.
Coates, A. and Ng, A. Y. (2012). Learning feature representations with k-means. In Neural networks: Tricks of
the trade, pages 561–580. Springer.
Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., and Bengio, Y.
(2014). Generative adversarial nets. In Advances in neural information processing systems, pages 2672–2680.
Hinton, G. E., Osindero, S., and Teh, Y.-W. (2006). A fast learning algorithm for deep belief nets. Neural
computation, 18(7):1527–1554.
Hinton, G. E. and Salakhutdinov, R. R. (2006). Reducing the dimensionality of data with neural networks.
science, 313(5786):504–507.
Jolliffe, I. (2011). Principal component analysis. Springer.
Le, Q. V., Ranzato, M., Monga, R., Devin, M., Chen, K., Corrado, G. S., Dean, J., and Ng, A. Y. (2011). Building
high-level features using large scale unsupervised learning. arXiv preprint arXiv:1112.6209.
Lee, H., Grosse, R., Ranganath, R., and Ng, A. Y. (2009). Convolutional deep belief networks for scalable
unsupervised learning of hierarchical representations. In Proceedings of the 26th annual international
conference on machine learning, pages 609–616. ACM.
MacQueen, J. et al. (1967). Some methods for classiﬁcation and analysis of multivariate observations. In
Proceedings of the ﬁfth Berkeley symposium on mathematical statistics and probability, volume 1, pages
281–297. Oakland, CA, USA.
10


## Page 11


Mirza, M. and Osindero, S. (2014). Conditional generative adversarial nets. arXiv preprint arXiv:1411.1784.
Ngiam, J., Khosla, A., Kim, M., Nam, J., Lee, H., and Ng, A. Y. (2011). Multimodal deep learning. In
Proceedings of the 28th international conference on machine learning (ICML-11), pages 689–696.
Radford, A., Metz, L., and Chintala, S. (2015). Unsupervised representation learning with deep convolutional
generative adversarial networks. arXiv preprint arXiv:1511.06434.
Schmidhuber, J. (1992). Learning factorial codes by predictability minimization. Neural Computation, 4(6):863–
879.
Vincent, P., Larochelle, H., Lajoie, I., Bengio, Y., and Manzagol, P.-A. (2010). Stacked denoising autoencoders:
Learning useful representations in a deep network with a local denoising criterion. Journal of machine
learning research, 11(Dec):3371–3408.
Wagstaff, K., Cardie, C., Rogers, S., Schrödl, S., et al. (2001). Constrained k-means clustering with background
knowledge. In Icml, volume 1, pages 577–584.
Way GP, Greene CS. Extracting a biologically relevant latent space from cancer transcriptomes with variational
autoencoders. BioRxiv. 2017 Jan 1:174474.
Rampasek L, Hidru D, Smirnov P, Haibe-Kains B, Goldenberg A. Dr. VAE: Drug response variational autoen-
coder. arXiv preprint arXiv:1706.08203. 2017 Jun 26.
Cohen I, David EO, Netanyahu NS, Liscovitch N, Chechik G. Deepbrain: Functional representation of neu-
ral in-situ hybridization images for gene ontology classiﬁcation using deep convolutional autoencoders.
InInternational Conference on Artiﬁcial Neural Networks 2017 Sep 11 (pp. 287-296). Springer, Cham.
11

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1907_05195v1_retina_vae_variationally_decoding_the_spectrum_of_macular_disease
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1907_05195V1_RETINA_VAE_VARIATIONALLY_DECODING_THE_SPECTRUM_OF_MACULAR_DISEASE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

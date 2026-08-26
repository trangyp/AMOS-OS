---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1702.07422v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1702.07422v1_sourceR__Classification_and_Source_Attribution_of_Infectious_Agents_among_Hetero

> Source: 1702.07422v1_sourceR__Classification_and_Source_Attribution_of_Infectious_Agents_among_Hetero.pdf

> Pages: 25

---


## Page 1


sourceR: Classiﬁcation and Source Attribution of Infectious Agents
among Heterogeneous Populations
Poppy Miller1, Jonathan Marshall2,3, Nigel French3,4,5, and Chris Jewell4
1CHICAS, Faculty of Health and Medicine, Lancaster University, Lancaster, UK
2Institute of Fundamental Sciences, Massey University, Palmerston North, New Zealand
3mEpiLab, Massey University, Palmerston North, New Zealand
4New Zealand Food Safety Science and Research Centre
5New Zealand Institute for Advanced Studies
March 8, 2022
Abstract
Zoonotic diseases are a major cause of morbidity, and productivity losses in both humans and animal
populations. Identifying the source of food-borne zoonoses (e.g. an animal reservoir or food product) is
crucial for the identiﬁcation and prioritisation of food safety interventions. For many zoonotic diseases
it is diﬃcult to attribute human cases to sources of infection because there is little epidemiological
information on the cases. However, microbial strain typing allows zoonotic pathogens to be categorised,
and the relative frequencies of the strain types among the sources and in human cases allows inference
on the likely source of each infection.
We introduce sourceR, an R package for quantitative source
attribution, aimed at food-borne diseases. It implements a fully joint Bayesian model using strain-typed
surveillance data from both human cases and source samples, capable of identifying important sources of
infection. The model measures the force of infection from each source, allowing for varying survivability,
pathogenicity and virulence of pathogen strains, and varying abilities of the sources to act as vehicles
of infection. A Bayesian non-parametric (Dirichlet process) approach is used to cluster pathogen strain
types by epidemiological behaviour, avoiding model overﬁtting and allowing detection of strain types
associated with potentially high ’virulence’.
sourceR is demonstrated using Campylobacter jejuni isolate data collected in New Zealand between
2005 and 2008. Chicken from a particular poultry supplier was identiﬁed as the major source of campy-
lobacteriosis which is qualitatively similar to results of previous studies using the same dataset. Addi-
tionally, the software identiﬁes a cluster of 9 MLSTs with abnormally high ’virulence’ in humans.
sourceR enables straightforward attribution of cases of zoonotic infection to putative sources of infec-
tion by epidemiologists and public health decision makers. As sourceR develops, we intend it to become
an important and ﬂexible resource for food-borne disease attribution studies.
1
Introduction
1.1
Background
Zoonotic diseases are a major source of human morbidity world wide. In 2010, there were an estimated 600
million cases globally [1], of which 96 million were Campylobacter spp. (resulting in 21 thousand deaths [2]).
Attributing cases of food-borne disease to putative sources of infection is crucial to identify and prioritise
food safety interventions. Traditional approaches to source attribution include full risk assessments, analysis
and extrapolation of surveillance or outbreak data, and analytical epidemiological studies [3]. However, their
1
arXiv:1702.07422v1  [stat.AP]  23 Feb 2017


## Page 2


results can be highly uncertain due to long and variable disease incubation times, and many and various
exposures of an individual to potential sources of infection.
Given this diﬃculty, quantitative methods
using pathogen strain type frequency have shown promise for statistically identifying important sources of
food-borne illness [4].
For a given disease, quantitative source attribution uses typing of pathogen isolates from human cases and
suspected sources of infection (food and environmental).
Samples are screened for the presence of the
pathogen, with isolates then categorised using a typing methodology. Multilocus Sequence Typing (MLST)
is a commonly used genotyping method providing a relatively coarse characterisation of isolates of bacterial
species [5]. An MLST sequence type is deﬁned as a unique combination of alleles at several gene loci, typically
located in conserved regions of the genome [6].
Routine surveillance for food-borne pathogens is now commonplace in many countries and is performed by
national authorities, for example FoodNet in the US [7], the Danish Zoonosis Centre (food.dtu.dk), and
the Ministry for Primary Industries in New Zealand (foodsafety.govt.nz). Despite this availability of
data we are unaware of any previous implementations in standard statistical software for source attribution
modelling, with past analyses being performed using a variety of ad hoc methodologies. Moreover, current
statistical source attribution models have strong assumptions, computational approximations or inherent
identiﬁability problems (discussed further in the ‘Review of models and notation’ section).
This paper presents an R package sourceR, which implements a ﬂexible Bayesian non-parametric model,
designed for use by epidemiologists and public health decision makers to attribute cases of zoonotic infection
to putative sources of infection. We ﬁrst describe a motivating example and review previous source attribu-
tion models before describing our model innovations, demonstrating the software, and discussing results and
future directions.
1.2
Motivating example
In 2006, New Zealand had one of the highest incidences of campylobacteriosis in the developed world, with
an annual incidence in excess of 400 cases per 100,000 people [8]. The data set was ﬁrst published in [9],
with a detailed description of the data (and data collection methods) available in [10] and [11]. A campaign
to change poultry processing procedures, supported in part by results from previous quantitative source
attribution approaches, was successful in leading to a sharp decline in campylobacteriosis incidence after
2007 [4].
The data consists of MLST-genotyped Campylobacter isolates (from both human cases of campylobacteriosis
and potential food and environmental sources) collected between 2005 and 2008 in the Manawatu region of
New Zealand. These data are included in our sourceR package (named campy). We use this data set as a
case study, and compare our results with previously published statistical approaches.
1.3
Review of models and notation
In this section we deﬁne our notation, and brieﬂy review the approaches that have been used previously to
analyse campy. For a given time period, we denote by yi the number of human cases of a disease caused by
pathogen type i = 1, . . . , n. For the same time period, we let sj denote the total number of source samples
collected from source j = 1, . . . , m, for which xij are positive for pathogen type i.
1.3.1
Hald model
The approach of Hald et al. [12] was to compare the number of human cases caused by diﬀerent pathogen
types with their prevalence in diﬀerent food sources (whilst accounting for type and source speciﬁc eﬀects).
2


## Page 3


This requires a heterogenous distribution of pathogen types among the food sources. The number of human
cases for each type yi is modelled as a Poisson random variable with mean given by a linear combination of
source speciﬁc eﬀects, type speciﬁc eﬀects and source sample Campylobacter contamination prevalences.
yi
∼
Poisson(λi)
(1)
λi
=
qi
m
X
j=1
αjcjpij
(2)
where for source j cj is the annual exposure, pij = rij × kj is the absolute prevalence of each pathogen type
with kj = Pn
i=1 xij/sj the prevalence of positive samples and rij =
xij
Pn
i=1 xij the relative prevalence of each
pathogen type.
The unknown parameters in the model are the vectors q and α. Here, q represents the characteristics that
determine a type’s capacity to cause an infection (such as survivability during food processing, pathogenicity
and virulence), and α accounts for the ability of a particular source to act as a vehicle of infection. These
parameters are interpreted further in S4 Appendix. Inference is performed in a Bayesian framework allowing
the model to explicitly include and quantify the uncertainty surrounding each of the parameters.
Equation 2 over-speciﬁes the model, with m + n parameters (the source and type eﬀects) but only n inde-
pendent observations (the observed human case totals yi). In the original approach [12], identiﬁability was
obtained by a priori clustering of the elements of α and q. In constrast, the Modiﬁed Hald model [4] prefers
to reduce the eﬀective number of parameters by treating q as a log Normal(0, τ) distributed random eﬀect.
However, a strong prior is needed on τ to shrink q towards 0 suﬃciently to avoid overﬁtting the model, the
choice of which is arbitrary.
The Modiﬁed Hald model introduces uncertainty into the relative prevalence matrix by modelling the source
sampling process. This model was ﬁtted in WinBUGS using an approximate two stage process [4]. First, a
posterior distribution was estimated for the absolute prevalence of source types p, using the model speciﬁed
in Eqs 3 and 4 :
r·j ∼Dirichlet(1) ∀j
(3)
kj ∼Beta(1, 1) ∀j
(4)
The marginal posterior for each element of p was then approximated by a Beta distribution
pij ∼Beta(wij, vij)
using the method of moments to calculate wij and vij. These were used as independent priors for each pij
which removes the constraint that they sum to kj over each type i. Thus, the absolute prevalence for source
j (PI
i=1 pij) is no longer constrained to be a probability (as it may be larger than 1).
1.3.2
Asymmetric Island model
The Asymmetric Island Model [13, 14] takes a diﬀerent approach to the models described above.
Here,
the evolutionary processes (mutation, migration and recombination) of the sequence types are modelled to
infer probabilistically the source of each human infection using genetic data from each subtype. The extra
information in the genetic typing allows the model to attribute human cases from a type not observed in any
sources to a likely source of infection by comparing the genetic similarity to other types that are observed
in the sources. This is not possible with the Hald or Modiﬁed Hald models, however, they are much simpler
with fewer assumptions and a wider range of suitable data (for example, phenotypic typing can be used).
We include results from this model as a comparison in the ‘Results’ section.
3


## Page 4


2
Design and Implementation
Our approach addresses the problems inherent in both the Hald and Modiﬁed Hald models. We introduce a
fully joint model for both source and human case sampling allowing us to integrate over uncertainty in the
source sampling process, estimating both the prevalence of contaminated source samples and the relative
prevalence of each identiﬁed type (without resorting to an approximate marginal probability distribution on
p). Furthermore, we introduce non-parametric clustering of pathogen types using a Dirichlet Process (DP)
model on the type eﬀect vector q, providing an automatic data-driven way of reducing the eﬀective number
of parameters to aid model identiﬁability. We are able, therefore, to circumvent the Hald model requirement
for heuristically grouping pathogen types, as well as avoiding an arbitrary prior distribution speciﬁcation for
the random eﬀect precision parameter (τ) required by the Modiﬁed Hald model.
Often, human case data is associated with location such as urban/rural, or even GPS coordinates. On the
other hand, food samples are likely to be less spatially constrained due to distances between production and
sale locations. Also, both human and source data may exist for multiple time-periods. We therefore denote
the number of human cases of time i occurring in time-period t at location l by yitl, the number of samples
of source j in time-period t by sjt, with the type counts xijt. We allow for diﬀerent exposures of humans to
sources in diﬀerent locations, by allowing the source eﬀects to vary between times and locations, αjtl.
2.1
Model
As with the Hald model, we assume the number of human cases yitl identiﬁed by isolation of subtype i in
time-period t at location l is Poisson distributed
yitl ∼Poisson(λitl = qi
m
X
j=1
αjtlpijt)
(5)
For each source j, we model the number of positive source samples
xjt ∼Multinomial(s+
jt, rjt)
(6)
where xjt = (xijt, i = 1, ..., n)T denotes the vector of type-counts in source j in time-period t, s+
jt =
Pn
i=1 xijt denotes the number of positive samples obtained, and rjt denotes a vector of relative preva-
lences Pr (typei|sourcej, timet). The advantage of this model is that it automatically places the constraint
Pn
i=1 rijt = 1, avoiding the approximation made in [4] where independent Beta-distributed priors were as-
signed marginally to components of rjt. The source case model is then coupled to the human case model
through the simple relationship
pijt = rijtkjt
(7)
where kjt is the prevalence of any isolate in source j in time-period t.
In principle, a Beta distribution could be used to model kjt, arising as the conjugate posterior distribution
of a Binomial sampling model for s+
jt positive samples from sjt tested, and a Beta prior on kjt. We instead
choose to ﬁx the source prevalences at their empirical estimates (kjt = s+
jt/sjt) because the number of source
samples is typically high.
The type eﬀects q, which are assumed invariant across time or location, are drawn from a DP with base
distribution Q0 and a concentration parameter aq
qi ∼DP (aq, Q0) .
(8)
The DP groups the elements of q into a ﬁnite set of clusters 1 : κ (unknown a priori) with values θ1, ..., θκ
meaning bacterial types are clustered into groups with similar epidemiological behaviour.
Heterogeneity in the source matrix x is absolutely required to identify clusters from sources, which may not
be guaranteed a priori due to the observational nature of the data collection.
4


## Page 5


2.2
Inference
This section describes how the model is ﬁtted in a Bayesian context by ﬁrst describing the McMC algorithm
used to ﬁt this model, then developing the prior model.
2.2.1
McMC algorithm
The joint model over all unobserved and observed quantities is ﬁtted using Markov chain Monte Carlo
(McMC, full details in S6 Appendix). The source eﬀects and relative prevalence parameters are updated
using independent adaptive Metropolis-Hastings updates [15]. The type eﬀects q are modelled using a DP
(Eq 8) with a Gamma base distribution Q0 ∼Gamma(aθ, bθ). As the Gamma distribution is conjugate with
respect to the Poisson likelihood (Eq 5), it is possible to use a marginal Gibbs sampler within a Polya Urn,
or “Chinese restaurant process” construction [16] (see S6 Appendix). This was chosen over the more general
“Stick breaking process” because it allows sampling from the conditional posterior of θ. This is particularly
important when the elements of θ values are highly dispersed: a base distribution with little mass near the
locations of some of the true values for the groups results in poor mixing for the group allocations using the
stick breaking algorithm (as it is diﬃcult for a type to change group when no other groups have a suitable
θ value). In contrast, the marginal scheme allows an element of q to move into a new cluster, then samples
a θ value directly from the conditional posterior for that group, improving group mixing dramatically.
2.2.2
Priors
The source and type parameters (αtl for all t and l, and q respectively) account for a multitude of source
and type speciﬁc factors which are diﬃcult to quantify a priori. Therefore, with no single real-world inter-
pretation, the distributional form of the priors were chosen for their ﬂexibility. A Dirichlet prior is placed
on each rjt which suitably constrains its L1 norm, i.e.
Pn
i=1 rijt = 1.
A Dirichlet prior is also placed
on each αtl, with the constrained L1 norm aiding identiﬁability between the mean of the source and type
eﬀect parameters. For more detail on specifying parameters for the Dirichlet Process and priors see the S2
Appendix.
2.3
Code implementation
Standard McMC packages (e.g. WinBUGS, Stan, PyMC3) all lack the capability to implement marginal
Gibbs sampling for Dirichlet processes, necessitating a custom McMC framework (see section ‘Extensibility’).
We chose R as a platform because of its ubiquity in epidemiology, and advanced support for post-processing
of McMC samples. Minimal dependencies on other R packages are required, and are installed automatically.
sourceR uses an object-oriented design, which allows separation of the model from the McMC algorithm.
Internally, the model is represented as a directed acyclic graph (DAG, see S3 Appendix) in which nodes are
represented by an R6 class hierarchy. Generic adaptive Metropolis Hastings algorithms are attached to each
parameter node, with the conditional independence properties of the DAG allowing automatic computation
of the required (log) conditional posterior densities.
A diﬃculty with the DAG setup is the representation of the Dirichlet process model on the type eﬀects q,
since each update of the marginal Gibbs sampler requires structural alterations. Therefore, we subsume the
entire Dirichlet process into a single node, with a bespoke marginal Gibbs sampling algorithm written for
our Gamma base-distribution and Poisson likelihood model.
5


## Page 6


3
Results
The case study below (using the campy (campylobacteriosis) data set described in the ‘Motivation’ section)
illustrates how the sourceR package is used in practice to identify important sources of infection. We compare
the results of our Bayesian non-parametric approach with results from the Modiﬁed Hald and Asymmetric
Island models, and additionally the historical ‘Dutch’ model (see S1 Appendix and [17]). The priors for our
model were selected to be non-informative.
The prevalence kj is calculated by dividing the number of positive samples by the total number of samples
for each source. In the data below, we note that for several samples the MLST typing failed, with the number
of positive samples exceeding the apparent total number of MLST-typed isolates. However, assuming MLST
typing fails independently of pathogen type, this does not bias our results.
The work ﬂow for ﬁtting the model begins with removing types with no source cases and calculating the
prevalences k.
data(campy)
zero_rows
<- which(apply(campy[, c(2 : 7)], 1, sum) == 0)
campy
<- campy[-zero_rows ,]
total_samples = c(239 , 196, 127, 595, 552, 524)
positive_samples = c(181 , 113, 109, 97, 165, 86)
k <- data.frame(Value = positive_samples / total_samples ,
Source = colnames(campy[, 2:7]) ,
Time = rep("1", 6),
Location = rep("A", 6))
The data and model parameters are set using the HaldDP$new() constructor. Starting values are selected
automatically unless provided via a list named init to the constructor.
priors
<- list(a_theta = 0.01 , b_theta = 0.00001 ,
a_alpha = 1, a_r = 0.1)
my_model
<- HaldDP$new(data = campy , k = k, priors = priors , a_q = 0.1)
McMC control parameters are be passed via fit params
my_model$fit_params(n_iter = 1000 , burn_in = 10000 ,
thin = 500)
The model is run using the update function. Additional iterations may be appended using append = TRUE.
set.seed (59623)
my_model$update ()
# my_model$update (n_iter = 10000 ,
append = T)
We provide the extract method for ease of access to the complex posterior.
## returns
the
posterior
for
the r, alpha , q, c,
## lambda_i, lambda_j and
lambda_j_prop
parameters
my_model$extract ()
The extract function returns the posterior for the selected parameters as a list with a multidimensional
array for each of alpha, r, q, s, lambda j and lambda i.
Trace and autocorrelation plots for the parameters indicate that the Markov chain is mixing well and has
converged, and that thinning by 500 is adequate (Figure 1). The residual plots for the λis (Figure 2) show
that the model ﬁts well.
## Plot
the
marginal
posteriors
for
the
following
parameters
## source
effect
for
Chicken
supplier C
plot(my_model$extract(params="alpha", sources="ChickenC")$alpha , type="l")
6


## Page 7


0
400
800
0.00
0.10
0.20
iteration / 1
value
source eﬀect
(Chicken C)
0
400
800
0
10000
iteration / 1
value
type eﬀect
(type 25)
0
400
800
0.00
0.10
iteration / 1
value
r
(Ovine, type 354)
0
400
800
0
100
300
iteration / 1
value
λ
(Chicken B)
0
400
800
0
40
80
120
iteration / 1
value
λ
(type 42)
0
40
80
0.0
0.4
0.8
Lag
0
40
80
0.0
0.4
0.8
Lag
0
40
80
0.0
0.4
0.8
Lag
0
40
80
0.0
0.4
0.8
Lag
0
40
80
0.0
0.4
0.8
Lag
Figure 1: Trace and acf plots for a sample of the model parameters (Manawatu Campylobacter data).
## type
effect
25
plot(my_model$extract(params="q", types="25")$q, type="l")
## relative
prevalence
for
source
effect
Ovine , type
354
plot(my_model$extract(params="r", sources="Ovine", types="354")$r,
type="l")
## number
of
cases
attributed
to
Chicken
supplier B
plot(my_model$extract(params="lambda_j", sources="ChickenB")$lambda_j,
type="l")
## number
of
cases
attributed
to sub
type
42
plot(my_model$extract(params="lambda_i", types="42")$lambda_i, type="l")
The summary() function calculates medians and credible intervals calculated with three possible methods
(percentile, SPIn [18], or Chen-Shao [19]).
my_model$summary(alpha = 0.05 , CI_type = " percentiles ")
These can be used to plot an observation versus ﬁtted plot as follows
## The
summary
for
lambda i is a 4D array
with
## [type , time , location , ( median/ CI_lower/ CI_upper )]
med_li_vals
<- my_model$summary(alpha = 0.05 ,
params = "lambda_i",
time = "1", location = "A")$lambda_i[, , , "median"]
human_cases
<- my_model$print_data ()$y
plot(med_li_vals , human_cases)
See S5 Appendix and S8 Appendix for more details on using the package.
3.1
Type eﬀect marginal distributions and clustering
To visualise how the DP has clustered the type eﬀects, we use Gower’s distance [20] to compute a dissimilarity
matrix between all possible pairs of types.
To aid interpretation of the posterior clustering of the type
eﬀects under the DP, we provide a method plot heatmap() that plots the clustering as a heatmap with a
dendrogram. Figure 4 shows that the DP identiﬁed four main pathogen type clusters.
my_model$plot_heatmap ()
7


## Page 8


0
100
200
21
25
38
42
45
48
50
52
53
61
137 177 190 227 257 354 393 422 436 451 474 520 526
Type
λi value
0
25
50
75
583 618 677 694 1030111511911223122512431517158118181911202623452347235023542381239123922397
Type
λi value
0
20
40
60
25352584261930723230323233013538360936103640365536563657365836593660366136623663366436723673
Type
λi value
0
20
40
60
80
3674 3675 3676 3711 3714 3716 3717 3719 3721 3722 3723 3724 3725 3726 3793 3794 3795 3797 3798 3799 3800 3802
Type
λi value
Figure 2: Violin plots showing the marginal posteriors for each λi (number of cases attributed to each type).
Observed number of cases for each type are shown as horizontal red lines. (Manawatu Campylobacter data).
8


## Page 9


0.00
0.25
0.50
0.75
1.00
λj value
M1
M2
M3
M4
ChickenA
M1
M2
M3
M4
ChickenB
M1
M2
M3
M4
ChickenC
M1
M2
M3
M4
Bovine
M1
M2
M3
M4
Ovine
M1
M2
M3
M4
Environment
Figure 3: Comparison of the proportion of human campylobacteriosis cases attributable to each source for
the models: M1 (Dutch model), M2 (Modiﬁed Hald model), M3 (Island model) and M4 (HaldDP model).
Error bars represent 95% conﬁdence or credible intervals. Violin plots show the marginal posteriors of the
λj parameters for the HaldDP model.
The violin plots of the marginal posterior distributions for each type eﬀect (Figure 5) show the largest group
of types has very small type eﬀects. These correspond to types observed in few source samples and no human
cases. Consequently, there is very little information for their type eﬀects which results in very wide credible
intervals. The other three groups have much larger type eﬀects. The clustering results identify clusters of
strains having particular traits that could be explored using further genotyping or phenotyping assays.
3.2
Comparison of the proportion of cases attributed to each source
Figure 3 shows the proportion of cases attributed to each source for the HaldDP model and three commonly
used source attribution models. The median values are similar between all models except the Dutch method
[17]. The Dutch model conﬁdence intervals are very narrow because there are far fewer parameters in the
model; however, the lack of source and type eﬀects in the model biases the results. The credible intervals
produced by the Island model may be narrow due to more accuracy (as additional genetic information
is used).
The wide credible intervals for the the HaldDP and modiﬁed Hald models may be due to C.
jejuni’s complex epidemiology resulting in relatively large uncertainty for the disease origin [4], and posterior
correlations between some parameters. In particular, the new model shows that the proportion of cases
attributed to poultry supplier A is negatively correlated with the proportion of cases attributed to both
ovine and poultry supplier B sources (Pearson correlation coeﬃcients of -0.60 and -0.65 respectively, see Fig
7 in S7 Appendix). The HaldDP model gives a more accurate representation of the uncertainty inherent
in source attribution. Some of this non-identiﬁability is not fully explored in the Modiﬁed Hald model [4]
as ﬁtting the model in two stages does not allow full propagation of the uncertainty. In particular, when
calculating the hyper-parameters for the Beta priors for each pij from the ﬁrst stage model, the authors
imposed a minimum αij of 1. This prevents ’bath tub’ shaped beta priors for any pijs which makes the
model easier to ﬁt at the expense of discouraging full exploration of the marginal posteriors for pijs that
truly have a bath-tub shape.
9


## Page 10


2026
436
3676
3711
3538
3717
3072
137
2350
21
354
474
38
451
52
61
48
677
2354
1243
1191
1911
227
3232
2397
3610
3721
3609
3726
3664
3674
3655
3673
3659
1818
2392
3663
1115
2347
3661
3301
3656
1225
2619
3657
526
618
694
3725
393
3795
3797
3793
3794
3799
3800
3658
3716
3640
3724
3719
3722
2584
3714
3798
1030
3662
3675
1223
3660
2381
3802
3230
3672
177
2535
3723
53
50
520
190
42
1517
1581
422
45
583
2345
2391
25
257
2026
436
3676
3711
3538
3717
3072
137
2350
21
354
474
38
451
52
61
48
677
2354
1243
1191
1911
227
3232
2397
3610
3721
3609
3726
3664
3674
3655
3673
3659
1818
2392
3663
1115
2347
3661
3301
3656
1225
2619
3657
526
618
694
3725
393
3795
3797
3793
3794
3799
3800
3658
3716
3640
3724
3719
3722
2584
3714
3798
1030
3662
3675
1223
3660
2381
3802
3230
3672
177
2535
3723
53
50
520
190
42
1517
1581
422
45
583
2345
2391
25
257
Figure 4: Heatmap showing the grouping of the type eﬀects (q) using the Manawatu Campylobacter data.
A white pixel represents a dissimilarity value of 1 between a pair of sub types, whilst dark blue (see pixels
on the diagonal) gives a value of zero.
10


## Page 11


10-250
10-200
10-150
10-100
10-50
100
2354
1243
1191
1911
227
3232
2397
3610
3721
3609
3726
3664
3674
3655
3673
3659
1818
2392
3663
1115
2347
3661
3301
3656
1225
2619
3657
526
618
694
3725
393
3795
3797
3793
3794
3799
3800
3658
3716
3640
3724
3719
3722
2584
3714
3798
1030
3662
3675
1223
3660
2381
3802
3230
3672
177
2535
3723
Type ID (group 3)
Type eﬀect value
101
103
105
2026
436
3676
3711
3538
3717
3072
137
2350
21
354
474
38
451
52
61
48
677
53
50
520
190
42
1517
1581
422
45
583
2345
2391
25
257
Type ID (groups 1, 2 and 4)
Type eﬀect value
Figure 5: Violin plots of the marginal distributions of the type eﬀects (q) using the Manawatu Campylobacter
data (using a log scale axis).
11


## Page 12


4
Availability and Future Directions
The stable release version of sourceR is available from the Comprehensive R Archive Network, released
under a GPL-3 licence. The development version is available at http://fhm-chicas-code.lancs.ac.uk/
millerp/sourceR.
As this package develops, we intend sourceR to become a platform for new source
attribution model development, providing a central analytic resource for public health professionals. The
establishment of a standard package with a familiar interface will therefore lead to improved repeatability
and reusability of source attribution analyses, supporting national public health and hygiene policy decisions.
4.1
Package extensibility
With increased interest in source attribution models for both food-borne pathogens, and sourceR has been
written with extensibility in mind, with the DAG representation allowing for rapid construction of modiﬁed
or new models. The package routines are written in R (as opposed to C or C++) to aid readability, with
the node class hierarchy and three stage workﬂow designed to aid the addition of new model classes. All
internal classes and methods are documented to enable prospective developers to familiarise themselves with
the source code quickly. We note that the DAG framework is not limited solely to source attribution models
and may used for other Bayesian applications, particularly those for which a Dirichlet process is required.
4.2
Model extensions
The main focus of extending sourceR will be on modelling spatiotemporal correlation in the time- and
location- dependent parameters. With the trend in collecting precise geolocation data with human cases,
and improved traceability of food, a spatiotemporal correlation model on αtl could be used to identify
particular foci of source contamination, therefore enabling targeted investigation of particular food supply
regions. Implementation of time varying type eﬀects may be appropriate, particularly in the face of evidence
that Campylobacter can evolve quickly, with genetic variation conferring virulence not apparent from course-
scale MLST typing [22]. Interaction terms between some sources and types would allow for the biologically
plausible possibility that certain types are more or less likely to survive and cause disease, dependent on the
food source they appear in. This would occur if a speciﬁc type was particularly well adapted to a certain
food source. However, including interaction terms would signiﬁcantly increase the number of parameters
and reduce identiﬁability of the model.
4.3
Increasing McMC eﬃciency
Testing has revealed that the current Metropolis-Hastings based ﬁtting algorithm suﬀers a loss of eﬃciency if
the source matrix is sparse or highly unbalanced, imbuing negative correlations between certain type/source
eﬀect combinations. Gradient-based ﬁtting algorithms such as Hamiltonian Monte Carlo (HMC) [23] are
designed to converge to high-dimensional, non-orthogonal target distributions much more quickly, and are a
target of future development. In particular, the No U-Turn Sample (NUTS) presents an attractive method for
tuning HMC adaptively, a quality which we consider necessary to minimise user intervention and maximise
research productivity [24].
5
Conclusions
We have presented a novel source attribution model which builds upon, and unites, the Hald and Modiﬁed
Hald approaches. It is widely applicable, fully joint, and does not require approximations or a large number of
assumptions. Mixing and a posteriori correlations are signiﬁcantly decreased in comparison to the Modiﬁed
12


## Page 13


Hald model. Furthermore, it allows the data to inform type eﬀect clustering using a Bayesian non-parametric
model which identiﬁes groups of bacterial sub types with similar putative virulence, pathogenicity and
survivability. This is a signiﬁcant improvement over the previous attempts to improve model identiﬁability
(ﬁxing some source and type eﬀects, or modelling the type eﬀects as random using a 2 stage model). Like
the Modiﬁed Hald model, the new model incorporates uncertainty in the prevalence matrix into the model,
however, it does this by ﬁtting a fully joint model rather than a 2 step model. This has the advantage
of allowing the human cases to inﬂuence the uncertainty in the source cases and preserves the restriction
on the sum of the prevalences for each source.
The sourceR package implements this model to enable
straightforward attribution of cases of zoonotic infection to putative sources of infection by epidemiologists
and public health decision makers.
6
Supporting Information
S1 Appendix.
Dutch model overview
The Dutch method [17] is one of the simplest models for source attribution. It compares the number of
reported human cases caused by a particular bacterial subtype with the relative occurrence of that subtype
in each source. The number of reported cases per subtype and reservoir is estimated by:
λij =
rij
P
j rij
yi
(9)
where rij is the relative occurrence of bacterial subtype i in source j, yi is the estimated number of human
cases of type i per year, λij is the expected number of cases per year of type i from source j. A summation
across types gives the total number of cases attributed to source j, denoted by λj:
λj =
X
i
λij
(10)
As the Dutch model has no inherent statistical noise model, conﬁdence intervals for the estimated total
attributed cases ˆλj by bootstrap sampling over the data set.
This model implicitly assumes that there
are no source or type speciﬁc eﬀects (such as diﬀering virulence of types, or diﬀering consumption of food
sources) which is not plausible for most zoonoses.
S1 Table.
Summary of model parameters.
The following table gives a list of the model parameters for easy reference.
13


## Page 14


Table 1: Description and deﬁnition of the model parameters.
Parameter Description
Estimation
λijtl
Number of human cases from type i, source j
λijtl = αjtl · qi · rijt · kjt
time t and location l
λitl
Number of human cases from type i
λitl = Pm
j=1 λijtl
time t and location l
λjtl
Number of human cases from source j
λjtl = Pn
i=1 λijtl
time t and location l
yitl
Number of human cases from type i
yi ∼Poisson(λitl)
time t and location l
xijt
Number of positive samples (that were
Data
successfully MLST typed) from source j, type i
time t
hijt
Number of positive samples (PCR) that
Data
could not be MLST typed.
s+
jt
Total number of samples from source j time t
Data
kjt
Prevalence of contamination for each source
PI
i=1(xijt + hijt)/s+
jt
rijt
Relative occurrence of type i on source j
rjt ∼Dirichlet(ar)
time t
or xijt/ Pn
i=1 xijt
pijt
Absolute prevalence of type i in source j
rijt · kjt
time t
αjtl
Unknown source eﬀect for source j
αtl ∼Dirichlet(aα)
time t and location l
qi
Unknown type eﬀect for type i in group k,
q ∼DP(Gamma(aθ, bθ), aq)
where group k has an unknown value θk
S2 Appendix.
Dirichlet Priors and Process details
The Dirichlet Process is a random probability measure deﬁned by a base distribution Q0 and a concentration
parameter aq [25]. The base distribution constitutes a prior distribution in the values of each element of the
type eﬀects q whilst the concentration parameter encodes prior information on the number of groups K to
which the pathogen types are assigned. For small values of aq, samples from the DP are likely to have a small
number of atomic measures with large weights. For large values, most samples are likely to be distinct, and
hence, concentrated on Q0. A value of 1 implies that, a priori, two randomly selected types have probability
0.5 of belonging to the same cluster [16].
Specifying the Dirichlet Process base distribution and concentration parameters:
The concen-
tration parameter of the DP is speciﬁed by the analyst as a modelling decision. The concentration parameter
speciﬁes how strong the prior grouping is. In the limit a →0, all types will be assigned to one group, increas-
ing a makes a larger number of groups increasingly likely. The Gamma base distribution Q0 induces a prior
for the cluster locations. This prior should not be too diﬀuse because if these locations are too spread out,
the penalty in the marginal likelihood for allocating individuals to diﬀerent clusters will be large, hence the
tendency will be to overly favour allocation to a single cluster. However, the prior parameters may have a
stronger eﬀect than anticipated due to the small size of the relative prevalence and source eﬀect parameters.
This can been seen by considering the marginal posterior for θk
θk ∼Gamma

aθ +
X
i:Si=k
yi, bθ +
X
i:Si=k
m
X
j=1
αj · pij


14


## Page 15


The term P
i:Si=k
Pm
j=1 αj · pij is very small (due to the Dirichlet priors on α and rj), which can result in
even a fairly small rate parameter (bθ) dominating.
Specifying Dirichlet priors:
The simplest Dirichlet priors for the source eﬀects and relative prevalences
are symmetric (meaning all of the elements making up the parameter vector a have the same value a,
called the concentration parameter). Symmetric Dirichlet distributions are used as priors when there is no
prior knowledge favouring one component over another. When a is equal to one, the symmetric Dirichlet
distribution is uniform over all points in its support. Values of the concentration parameter above one prefer
variates that are dense, evenly distributed distributions, whilst values of the concentration parameter below
1 prefer sparse distributions. Note, a prior of 1 for the relative prevalences is too strong (if a relatively non-
informative prior is preferred) when there are many observed zero’s in the source data; a prior value of 0.1
is more suitable. A more informative prior can be speciﬁed by using a non-symmetric Dirichlet distribution.
The magnitude of the vector of a parameters corresponds to the strength of the prior. The relative values
of the a vector corresponds to prior information on the comparative sizes of the parameters.
S3 Appendix.
Directed acyclic graph of the model
aθ
bθ
aq
ci
θi
aαjtl
xijt
hijt
arijt
pijt
qi
αjtl
λijtl
yitl
Figure 6: Directed acyclic graph of the source attribution model. See Table 1 for a concise description of
the parameters.
S4 Appendix.
Further details about the interpretation of the source and type eﬀects.
The interpretation of source and type eﬀects depends on the quality and type of data collected, the model
speciﬁcation, and the characteristics of the organism of interest. Source eﬀects account for factors such as
the amount of the food source consumed, the physical properties of the source and the environment provided
for the bacteria through storage and preparation. Including an environmental source in the model can be
thought of as grouping the (individually) unmeasured wildlife sources into one. It may also be a transmission
15


## Page 16


pathway for pathogens present in livestock sources (for example, through the contamination of waterways)
which complicates the interpretation meaning the source eﬀects no longer directly summarise the ability of
the source to act as a vehicle for food-borne infections [12]. Future work could involve attributing the water/
environmental samples to the other sources of infection (such as contamination from bovine, ovine, poultry,
or other animal sources). Therefore, it would be possible to estimate the proportion of cases attributed to a
sample directly, and via the environement.
S5 Appendix.
Helpful details regarding use of sourceR
The sourceR package currently allows the relative prevalence matrix to be ﬁxed at the maximum likelihood
estimates, which includes zero values where a particular type was not detected in any samples from a source.
Fixing the relative prevalence matrix increases the posterior precision (and signiﬁcantly reduces run time),
but the results may be biased if the source data is not of high quality. Reducing the number of elements
in the relative prevalence matrix r that get updated at each iteration can signiﬁcantly reduce computation
time, however, the chains will converge more slowly.
Care must be taken in performing marginal interpretations of the number of type parameters. It is much
easier to split a group into two (with similar group means) than it is to merge two groups with clearly
diﬀerent means. Hence, a histogram of the number of groups per iteration is positively skewed compared to
the true number of groups. When ﬁtting the model with simulated data, visually assessing the dendrogram
and heatmap to determine the number of groups usually provides a closer value to the true number of groups
than looking at a histogram, particularly when the group means are well separated.
S6 Appendix.
Full McMC Algorithm. This section gives the full details of the algorithm used to ﬁt
our fully joint non-parametric source attribution model. The outline McMC is shown in Algorithm 1. The
Dirichlet distributed source eﬀects αtl across times t and locations l (Step 1), and the relative prevalences
rjt across sources j and times t (Step 2) are updated using a constrained adaptive multisite logarithmic
Metropolis-Hastings update step for 95% of proposals, and a constrained adaptive multisite Metropolis-
Hastings update step for the remainder to prevent the chain getting stuck at very low values [15]. The
adaptive algorithm updates the tuning value every 50 updates of the parameter. This is further explained
in Algorithm 2.
Data: Human cases y, source isolates X, source prevalence s
Initialize all parameters ;
for z times do
foreach t, l do
1
Update αtl ;
end
foreach j,t do
2
Update rjt ;
end
3
Update q ;
Save chain state ;
end
Algorithm 1: Outline McMC algorithm for the HaldDP model.
For the Dirichlet process prior on q, a marginal Gibbs sampler is constructed, as described in Algorithm
3. Let H denote a set of cluster identiﬁers, with the n-dimensional group assignment vector c associating
elements of q with clusters, such that ci = h assigns qi to cluster h. Furthermore, each cluster h assumes a
value θh such that qi = θci.
In Step 1 of Algorithm 3, conjugacy between the Gamma-distributed base distribution P0 and the Poisson
16


## Page 17


Input: d-dimensional Dirichlet(a) distributed random variable W , tuning variance vector σ, online
acceptance rate vector ρ, z the current McMC iteration number.
Output: Updated W and σ.
Let W ′ = W ;
for h times do
1
Let j ∼UniformInteger[1, d] ;
2
Let g ∼Uniform[0, 1];
if g > 0.05 then
Simulate W ′
j = Wj ∗exp [N(0, σj)]
δ = W ′
W
end
else
Simulate W ′
j = N(Wj, 0.1)
δ = 1
end
3
Let W ′ = W ′/|W ′| ;
4
Accept W = W ′ with probability 1 ∧f(W ′|a)
f(W |a) · δ and update ρj ;
5
if h mod 50 = 0 then
if ρj > 0.44 then
σj = exp

log(σj) +

0.05 ∧
1
√
(z)

end
else
σj = exp

log(σj) −

0.05 ∧
1
√
(z)

end
end
end
Algorithm 2: Constrained adaptive multisite logarithmic random walk used for Dirichlet-distributed ran-
dom variables.
17


## Page 18


data likelihood permits the calculation of Multinomial conditional posteriors for elements of c arising from
the Chinese Restaurant Process construction. Here, the conditional posterior probability of type i being
assigned to group h is as shown in Algorithm 3, with conjugacy permitting marginalisation with respect to
the base distribution in order to calculate the probability of being assigned to a new group h⋆
ph⋆= aq
Z
Θ
L(yi|θ, λ⋆
i )dP0(θ) =
baθ
θ (aθ + yi)
Γ(aθ)(bθ + λ⋆
i )aθ+yi
with y⋆
i = P
t,l yitl and λ⋆
i = P
t,l αT
tl(rit ⊙kt)
If a type is assigned to a new group, the set H is augmented and a corresponding cluster value is drawn from
the posterior of θh⋆. Conversely, H is shrunk if a particular group becomes empty.
In Step 2, the group values are drawn from the posterior, conditional on c. The algorithm therefore alternates
between updating group assignments c and group values θ. Hence, it explores the number of groups present,
the type eﬀects assigned to each group, and the values of each group.
Data: Human case counts y⋆= P
t,l{y1tl, . . . , yntl}, source intensities λ⋆: λ⋆
i = P
t,l αT
tl(rit ⊙kt)
Input: H the set of cluster identiﬁers, c an n-dimensional vector of group allocators, ci ∈H, θ a
|H|-dimensional vector of cluster values
// Update group allocation c
for i in 1 : n do
1
Sample ci from k(ci|·) ∼Multinomial(⟨ph : h ∈H, ph⋆⟩) where
ph = |H(−i)
h
|L(y⋆
i |θh, λ⋆
i ),
h ∈H
(11)
ph⋆= aq
Z
Θ
L(y⋆
i |θ, λ⋆
i )dP0(θ),
h ̸∈H
(12)
;
if ci = h⋆then
Set H = {H, h⋆} ;
Sample θh⋆∼Gamma(y⋆
i + aθ, 1 + bθ) ;
end
else if |Hh| = 0 then
Set H = H(−h) ;
end
end
// Update cluster values θ
for h in H do
2
Update θh ∼Gamma(P
i:ci=h y⋆
i + aθ, nh + bθ)
end
Algorithm 3: Marginal Gibbs sampling algorithm using the Chinese Restaurant Process construction of a
Dirichlet process
S7 Appendix.
Posterior correlations and non-identiﬁability of source attribution.
18


## Page 19


100
200
300
400
500
0
100
200
300
400
ChickenA vs Chicken B:
Pearson correlation = -0.65
λj: ChickenA
ChickenB
100
200
300
400
500
0
100
200
300
ChickenA vs Ovine:
Pearson correlation = -0.6
λj: ChickenA
Ovine
Figure 7: Scatter plots showing the correlation between the λj marginal posteriors for Chicken supplier A
versus Chicken supplier B and Ovine.
S8 Appendix.
Worked example showing features of package using simulated data.
In this section, we provide a worked example using simulated data with multiple times and locations for
source attribution data generated from the model in Section 2.1 (available in the sourceR data sets). There
are two times (1, 2) and two locations (A, B) over which the human cases vary. The data must be in long
format, with columns giving the number of human cases for each type, a column for each of the sources
giving the number of positive samples for each type, and columns giving the time, location and type id’s for
each observation. Note, the source data is the same for all locations within a time.
The algorithm is run for a total of 500,000 iterations (with a burn in of 10000 iterations and thinning 500).
The acceptance rates for all parameters (except those updated using a Gibbs sampler) can be accessed using
the my model$acceptance().
## source
and
human
case
data
data(sim_SA_data)
## prevalences
for
each
source/ time
data(sim_SA_prev)
## true
values
for
the
model
parameters
data(sim_SA_true)
priors
<- list(a_theta = 0.01 , b_theta = 0.00001 ,
a_alpha = 1, a_r = 0.1)
my_model
<- HaldDP$new(data = sim_SA_data , k = sim_SA_prev ,
priors = priors , a_q = 0.1)
Fitting parameters for the McMC are be passed using
my_model$fit_params(n_iter = 1000 , burn_in = 2000 , thin = 500)
The model is then run using
set.seed (59623)
my_model$update ()
Trace and autocorrelation plots for the parameters (Figure 8) indicate that the Markov chain is mixing well
and has converged, and that thinning by 500 is adequate. The following R code demonstrates how to access
and plot the marginal posteriors for some parameters.
19


## Page 20


## Plot
the
marginal
posterior
for
source
effect 2, time 1, location A
plot(my_model$extract(params = "alpha", times = "1", locations = "B",
sources = "Source4")$alpha , type="l")
## Plot
the
marginal
posterior
for
the
type
effect
21
plot(my_model$extract(params = "q", types = "21")$q, type="l")
## Plot
the
marginal
posterior
for
the
relative
prevalence
of
## source
effect 5, type 17, at
time 2
plot(my_model$extract(params = "r", times = "2", sources = "Source5",
types = "17")$r, type="l")
## Plot
the
marginal
posterior
for
lambda _j source 1, time 1, location A
plot(my_model$extract(params = "lambda_j", times = "1", locations = "A",
sources = "Source1")$lambda_j, type = "l")
## Plot
the
marginal
posterior
for
lambda _i 10, time 2, location B
plot(my_model$extract(params = "lambda_i", times = "2", locations = "B",
types = "10")$lambda_i, type="l")
Medians and credible intervals can be obtained for each parameter using res$summary(). The marginal
density plots of the number of cases attributed to each source at each time and location (λjtl) show that the
true values (shown by a red horizontal line on the graph) are being estimated well (Figure 9). The violin
plots of the number of cases attributed to each type (residual plot) for λi (Figure 10) shows that the model is
ﬁtting well. The heatmap shows the grouping of the type eﬀects (Figure 11) computed using a dissimilarity
matrix from the clustering output of the McMC. The coloured bar under the dendrogram gives the correct
grouping from the simulated data. This shows that the majority of types have been classiﬁed correctly.
0
200
600
1000
0.20
0.30
0.40
0.50
iteration / 500
value
source effect
(source 3, time 1,
location A)
0
200
600
1000
2000
6000
iteration / 500
value
type effect
type 21
0
200
600
1000
0.000
0.010
0.020
iteration / 500
value
r
(source 5, type 17,
time 1, location A)
0
200
600
1000
200
600
1000
iteration / 500
value
λ
(source 1, time 1
location A)
0
200
600
1000
20
40
60
80
100
iteration / 500
value
λ
(type 10, time 2
location B)
0
20
40
60
80
0.0
0.4
0.8
Lag
0
20
40
60
80
0.0
0.4
0.8
Lag
0
20
40
60
80
0.0
0.4
0.8
Lag
0
20
40
60
80
0.0
0.4
0.8
Lag
0
20
40
60
80
0.0
0.4
0.8
Lag
Figure 8: Trace and acf plots for a sample of the model parameters. True values of the parameters are shown
in red.
20


## Page 21


Source5
Source6
Source3
Source4
Source1
Source2
1A
1B
2A
2B
1A
1B
2A
2B
0
1000
2000
3000
0
1000
2000
3000
0
1000
2000
3000
Group
Value
Figure 9: Violin plots showing marginal posteriors for each λj (number of cases attributable to each source)
for each time (1, 2) and location (A, B). True λj values are shown as horizontal red lines.
21


## Page 22


2B
2A
1B
1A
1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728293031323334353637383940414243444546
10-3
10-1
101
103
10-3
10-1
101
103
10-3
10-1
101
103
10-3
10-1
101
103
Type
Value
2B
2A
1B
1A
47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91
10-5
10-3
10-1
101
103
10-5
10-3
10-1
101
103
10-5
10-3
10-1
101
103
10-5
10-3
10-1
101
103
Type
Value
Figure 10: Violin plots showing the marginal posteriors for each λi (number of cases attributed to each type)
for each time (1, 2) and location(A, B). True λi values are shown as horizontal red lines.
22


## Page 23


7
Acknowledgments
The research for this paper was ﬁnancially supported by the Ministry for Primary Industries, the Institute
of Fundamental Sciences (Massey University), the mEpiLab (Massey University), and CHICAS (Lancaster
University). We acknowledge the following individuals and groups: mEpiLab (Massey University), MidCen-
tral Public Health Services and Petra Mullner (for the Manawatu data set) and GeoﬀJones (for his helpful
input on automatic clustering methods).
References
[1] Havelaar AH, Kirk MD, Torgerson PR, Gibb HJ, Hald T, Lake RJ, et al. World Health Organization
Global Estimates and Regional Comparisons of the Burden of Foodborne Disease in 2010. PLoS Med.
2015;12(12):1–23. doi:10.1371/journal.pmed.1001923.
[2] World Health Organization. WHO estimates of the global burden of foodborne diseases: foodborne
disease burden epidemiology reference group 2007-2015; 2015.
available on the WHO web site
(www.who.int) or can be purchased from WHO Press, World Health Organization, 20 Avenue Ap-
pia, 1211 Geneva 27, Switzerland. Available from: http://apps.who.int/iris/bitstream/10665/
199350/1/9789241565165_eng.pdf?ua=1.
[3] Crump JA, Griﬃn PM, Angulo FJ. Bacterial Contamination of Animal Feed and Its Relationship to
Human Foodborne Illness. Clinical Infectious Diseases. 2002;35(7):859–865. doi:10.1086/342885.
[4] Mullner P, Jones G, Noble A, Spencer S, Hathaway S, French N. Source Attribution of Food Borne
Zoonoses in New Zealand: A Modiﬁed Hald Model. Risk Analysis. 2009;29(7).
[5] Urwin R, Maiden M. Multi-locus Sequence Typing: A Tool for Global Epidemiology. Trends in Micro-
biology. 2003;.
[6] Dingle K, Colles F, Wareing D, Ure R, Fox A, Bolton F, et al. Multilocus sequence typing system for
Campylobacter jejuni. Journal of Clinical Microbiology. 2001;.
[7] Allos BM, Moore MR, Griﬃn PM, Tauxe RV. Surveillance for Sporadic Foodborne Disease in the 21st
Century: The FoodNet Perspective. Clinical Infectious Diseases. 2004;38(Supplement 3):S115–S120.
doi:10.1086/381577.
[8] Baker M, Wilson R, Ikram R, Chambers S, Shoemack S, Cook G. Regulation of Chicken Contamination
Urgently Needed to Control New Zealand’s Serious Campylobacteriosis Epidemic. The New Zealand
Medical Journal. 2006;.
[9] Mullner P, Collins-Emerson J, Midwinter A, Carter P, Spencer S, van der Logt P, et al. Molecular
Epidemiology of Campylobacter jejuni in a Geographically Isolated Country with a Uniquely Structured
Poultry Industry. Applied and Environmental Microbiology. 2010;76(7):2145–2154.
[10] French N, Marshall J.
Dynamic Modelling of Campylobacter Sources in the Manawatu.
Hopkirk
Institute, Massey University; 2009.
[11] French N, Marshall J.
Completion of Sequence Typing of Human and Poultry Isolates and Source
Attribution Modelling. Hopkirk Institute, Massey University; 2013.
[12] Hald T, Vose D, Wegener H, Koupeev T. A Bayesian Approach to Quantify the Contribution of Animal-
Food Sources to Human Salmonellosis. Risk Analysis. 2004;24(1):255–269.
[13] Wilson D, Gabriel E, Leatherbarrow A, Cheesebrough J, Hart C, Diggle P.
Tracing the Source of
Campylobacteriosis. PLoS Genetics. 2008;.
[14] Wilson D. iSource; 2016. Available from: http://www.danielwilson.me.uk/iSource.html.
23


## Page 24


[15] Roberts G, Rosenthall J. Examples of Adaptive MCMC. University of Toronto Department of Statistics;
2006.
[16] Gelman A, Carlin J, Stern H, Dunson D, Vehtari A, Rubin D. Bayesian Data Analysis. Chapman &
Hall/CRC Texts in Statistical Science; 2013.
[17] van Pelt W, van de Giessen A, van Leeuwen W, Wannet W, Henken A, Evers E. Oorsprong, Omvang
en Kosten van Humane Salmonellose. Deel1. Oorsprong van Humane Salmonellose met Betrekking tot
Varken, Rund, Kip, ei en Overige Bronnen. Infectieziekten Bull. 1999;.
[18] Liu Y, Gelman A, Zheng T. Simulation-eﬃcient Shortest Probability Intervals. Statistics and Comput-
ing. 2015;.
[19] Chen M, Shao Q. Monte Carlo Estimation of Bayesian Credible and HPD Intervals. Journal of Com-
putational and Graphical Statistics. 1991;.
[20] Gower JC. A general coeﬃcient of similarity and some of its properties. Biometrics. 1971;.
[21] pubmlst. Campylobacter MLST; 2016. Available from: http://pubmlst.org/campylobacter/.
[22] Wilson DJ, Gabriel E, Leatherbarrow AJH, Cheesbrough J, Gee S, Bolton E, et al. Rapid Evolution
and the Importance of Recombination to the Gastroenteric Pathogen Campylobacter jejuni. Molecular
Biology and Evolution. 2009;26(2):385–397.
[23] Duane S, Kennedy AD, Pendleton BJ, Roweth D.
Hybrid Monte Carlo.
Physics Letters B.
1987;195(2):216 – 222. doi:http://dx.doi.org/10.1016/0370-2693(87)91197-X.
[24] Homan MD, Gelman A. The No-U-turn Sampler: Adaptively Setting Path Lengths in Hamiltonian
Monte Carlo. J Mach Learn Res. 2014;.
[25] Ferguson T. Bayesian Analysis of some Nonparametric Problems. Ann Stat. 1973;1:209–230.
24


## Page 25


29
27
6
15
1
2
11
16
17
30
5
14
24
22
23
9
13
21
19
12
28
4
25
18
26
7
10
56
53
3
8
91
55
79
61
86
82
90
89
87
70
64
81
80
85
65
68
67
71
78
66
69
75
72
83
62
63
74
84
88
76
77
43
73
44
46
38
45
34
50
42
54
49
35
31
36
20
57
51
52
32
39
48
40
41
33
37
58
59
47
60
29
27
6
15
1
2
11
16
17
30
5
14
24
22
23
9
13
21
19
12
28
4
25
18
26
7
10
56
53
3
8
91
55
79
61
86
82
90
89
87
70
64
81
80
85
65
68
67
71
78
66
69
75
72
83
62
63
74
84
88
76
77
43
73
44
46
38
45
34
50
42
54
49
35
31
36
20
57
51
52
32
39
48
40
41
33
37
58
59
47
60
Figure 11: Heatmap showing the grouping of the type eﬀects (q) using simulated data (true groupings given
by the 3 colours in the bar under the dendrogram).
25

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
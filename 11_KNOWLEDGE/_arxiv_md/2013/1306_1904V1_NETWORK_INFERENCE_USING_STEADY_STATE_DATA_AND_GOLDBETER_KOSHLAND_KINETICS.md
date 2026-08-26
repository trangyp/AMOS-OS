---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1306.1904v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1306.1904v1_Network_Inference_Using_Steady_State_Data_and_Goldbeter-Koshland_Kinetics

> Source: 1306.1904v1_Network_Inference_Using_Steady_State_Data_and_Goldbeter-Koshland_Kinetics.pdf

> Pages: 7

---


## Page 1


Doc-StartBIOINFORMATICS
Vol. 00 no. 00 2005
Pages 1–7
Network Inference Using Steady-State Data and
Goldbeter-Koshland Kinetics
Chris J Oates 1,2,3, Bryan T Hennessy4, Yiling Lu5, Gordon B Mills5 and Sach
Mukherjee 3
1Centre for Complexity Science, University of Warwick, CV4 7AL, UK.
2Department of Statistics, University of Warwick, CV4 7AL, UK.
3Department of Biochemistry, Netherlands Cancer Institute, 1066CX Amsterdam, The Netherlands.
4Department of Medical Oncology, Beaumont Hospital, Dublin, Ireland.
5Department of Systems Biology, The University of Texas M. D. Anderson Cancer Center, Houston,
TX 77030, USA.
Received on XXXXX; revised on XXXXX; accepted on XXXXX
Associate Editor: XXXXXXX
ABSTRACT
Motivation: Network inference approaches are widely used to shed
light on regulatory interplay between molecular players such as genes
and proteins. Biochemical processes underlying networks of interest
(e.g. gene regulatory or protein signalling networks) are generally
nonlinear.
In many settings,
knowledge is available concerning
relevant chemical kinetics.
However,
existing network inference
methods for continuous data are typically rooted in convenient
statistical formulations which do not exploit chemical kinetics to guide
inference.
Results:
Here we present an approach to network inference
for steady-state data that is rooted in nonlinear descriptions of
biochemical mechanism. We use equilibrium analysis of chemical
kinetics to obtain functional forms that are in turn used to infer
networks using steady-state data. The approach we propose is
directly applicable to conventional steady-state gene expression or
proteomic data and does not require knowledge of either network
topology or any kinetic parameters; both are simultaneously learned
from data. We illustrate the approach in the context of protein
phosphorylation networks,
using data simulated from a recent
mechanistic model and proteomic data from cancer cell lines. In the
former, the true network is known and used for assessment, whilst
in the latter results are compared against known biochemistry. We
ﬁnd that the proposed methodology is more effective at estimating
network topology than methods based on linear models.
Availability: MATLAB R2009b code used to produce these results is
provided in the Supplemental Information.
Contact: c.j.oates@warwick.ac.uk, s.mukherjee@nki.nl
1
INTRODUCTION
Networks of molecular components play a prominent role in
molecular and systems biology. A graph G = (V, E) can be used
to describe a biological network, with vertex set V (G) identiﬁed
with molecular components (e.g. genes or proteins) and edge set
E(G) with regulatory interplay between the components. Edges
in a biological network are often associated with the causal notion
that intervention on a parent node inﬂuences its child node(s). Data-
driven characterisation of the graph structure E(G) (often referred
to as the topology) is known as network inference and has emerged
as an important problem class in bioinformatics and systems biology
(Chou and Voit, 2009). Network inference can aid in efﬁcient
generation of biological hypotheses from high-throughput data.
Further, network inference can aid in exploring molecular interplay
that is associated with speciﬁc phenotypes, such as disease states.
From a statistical perspective, network inference entails reverse-
engineering a graph G using biochemical data D and, where
available, prior knowledge regarding aspects of the topology. Over
the last decade many methods for network inference have been
proposed, with popular approaches are reviewed in Bansal et al.
(2007); Hecker et al. (2009); Lee and Tzou (2009); Markovetz
and Spang (2007). To date, most methods for network inference
have been rooted in discrete or linear formulations (Bender et al.,
2010; Sachs et al., 2005; Morrissey et al., 2010; Opgen-Rhein and
Strimmer, 2007; Hill, 2012; Kim et al., 2003). As discussed in Oates
and Mukherjee (2012a), a wide range of existing approaches can
be viewed as variants of the linear regression model in statistics.
(In this paper “linear” refers to linearity in parameters, so that
nonlinear basis functions may be used within a “linear” framework.)
Moreover, a number of approaches based on ordinary differential
equations (ODEs; Bansal et al. (2007); Li and Chen (2010); Nam
et al. (2007)) are ultimately reducible to linear statistical models, as
described in Oates and Mukherjee (2012c).
However,
the biochemical processes underlying biological
networks are often highly nonlinear. When the data-generating
process is nonlinear, use of linear models may produce inefﬁcient or
inconsistent estimation, attributing causal status to artifacts resulting
from model misspeciﬁcation (Heagerty and Kurland, 2001; Lv
and Liu, 2010). Indeed, such bias can prevent recovery of the
correct network even in favourable asymptotic limits of large
sample size and low noise (Oates and Mukherjee, 2012a). On
the other hand, in many settings nonlinear dynamical models of
relevant biochemical processes are available. For example gene
regulation may be modelled using Michaelis-Menten functionals
(Cantone et al., 2009), and metabolism may be modelled using
c
⃝Oxford University Press 2005.
1
arXiv:1306.1904v1  [stat.AP]  8 Jun 2013


## Page 2


Oates and Mukherjee
mass action chemical kinetics (Min Lee et al., 2008). Here, we
describe an approach by which kinetic models can be used to
inform network inference from steady-state data. As we show below,
such information can be valuable in guiding exploration of network
topologies.
Kinetic formulations have been widely studied in the systems
biology literature (Bintu et al., 2005) and recently there has
been much interest in statistical inference for such systems, with
examples including Chen et al. (2009); Xu et al. (2010). Our
work is in a similar vein, but focuses on network inference
per se and on the steady-state rather than time-course setting.
While biochemical assays have become cheaper, it remains the
case that experimental designs must often negotiate a trade off
between more conditions (e.g. perturbations, biological samples,
technical replicates) and temporal resolution (e.g. number of time
points). Methodologies which can exploit knowledge concerning
relevant dynamical systems in the steady-state setting are therefore
potentially valuable.
In brief,
we proceed as follows.
We consider a class of
nonlinear biochemical dynamical systems that are relevant to the
biological process of interest (we focus on protein signalling,
discussed in detail below). Steady-state analysis leads to a class of
functional relationships between parent and child. These functional
relationships are used to formulate a statistical model for network
inference from steady-state data. In this way, network inference is
rooted in functional relationships derived from nonlinear kinetics.
Importantly, we do not assume detailed knowledge of the dynamical
system, but only the broad class to which dynamics and associated
equilibria may belong. Indeed, the approach we describe does not
require any kinetic parameters to be known a priori, nor knowledge
of the network topology, and is in that sense directly comparable
to conventional network inference methods. Its potential advantage
stems from then rich yet constrained nature of the class of functional
relationships that are considered. As recently discussed in Peters et
al. (2011), nonlinear functional forms can aid in identiﬁcation of
underlying causal relationships.
We develop these ideas in the context of protein signalling
mediated
by
phosphorylation.
Enzyme
kinetics
have
been
extensively studied,
and dynamical formulations are widely
available in the literature (see e.g. Leskovac, 2003). For some
proteins and pathways, regulation has been studied in considerable
causal and mechanistic detail.
Indeed,
there exist detailed
computational models for canonical protein signalling pathways,
which have been validated against experimental data (e.g. Schoeberl
et al., 2002; Xu et al., 2010). Further, proteomic technologies now
allow multivariate, data-driven study of phosphorylation, facilitating
biological validation of proposed methodology. We take advantage
of these factors to examine the performance of our methodology
using both simulated and real data.
In the phosphorylation setting,
Goldbeter-Koshland kinetics
(Goldbeter and Koshland, 1981) form the functional class that
underlies our network inference approach. Goldbeter-Koshland
kinetics are well known to be capable of highly nonlinear
behaviour including exquisite sensitivity. It has been experimentally
demonstrated that this so-called ultrasensitivity is biologically
relevant to signalling network dynamics, facilitating abrupt and
precise decision making (e.g. Kim and Ferrell (2007)). We carry
out statistical inference in a Bayesian framework, using reversible-
jump Markov chain Monte Carlo (RJMCMC) to explore the joint
model and parameter space. This yields posterior probability scores
for edges in the network that are analogous to scores obtained in
existing statistical network inference approaches for steady-state
data Hill (2012).
The remainder of this paper is organised as follows. In Section
2 our approach is laid out, followed by a detailed exposition of the
associated computational statistics. In Section 3 we present results
on data simulated from a recently developed dynamical model of
the mitogen-activated protein kinase (MAPK) signalling, that has
been validated against experimental data (Xu et al., 2010). We then
show results on real proteomic data from breast cancer cell lines.
Finally, Section 4 closes with a discussion of practical implications
and opportunities for network inference based on functional models,
along with associated technical challenges.
2
METHODS
We begin in Section 2.1 by describing our approach in general terms. Section
2.2 then introduces relevant concepts in the application area of protein
phosphorylation. In particular we describe a class of nonlinear equations
derived from Goldbeter-Koshland kinetics. Next, in Section 2.3 this model
class is embedded into a Bayesian statistical framework for observations
obtained at equilibrium. Inference over model space is facilitated by
RJMCMC, with Section 2.4 dedicated to a presentation of our sampling
scheme and a discussion of key implementational details.
2.1
General Formulation
We consider a state vector X = (X1, . . . , Xp) containing concentrations of
p proteins. Equilibrium analysis of phosphorylation dynamics, as described
below, leads to a system of p equations Xi = fi(X, Ui; θi) where i indexes
proteins, Ui are external input variables and θi unknown parameters. The
component function fi depends on a subset πi of the state variables, such
that we may write Xi = fi(Xπi, Ui; θi), where Xπi indicates selection
of components of the vector X whose indices are members of the set πi.
Variables j ∈πi are the parents of node i in graph G; the parent sets πi
specify the (unknown) topology of interest since (j, i) ∈E(G)
⇐⇒
j ∈πi. Our inference scheme seeks to infer the πi’s from steady-state
data. Since the dynamical system is not usually known in detail a priori,
we consider the practically applicable case in which the fi’s are known only
to belong to a certain class F (derived from Goldbeter-Koshland kinetics,
as described below) with parent sets πi and all parameters θi remaining
unknown.
2.2
Protein Phosphorylation
We consider proteins i
∈
V
=
{1, . . . , p}, each of which has
an unphosphorylated form X0
i
and a phosphorylated form Xi (i
∈
V ). Phosphorylated proteins are referred to as phosphoproteins. The
chemical reaction that gives product Xi from substrate X0
i is known
as phosphorylation and is catalysed by kinases XE (E
∈
Ei). We
consider the case in which the kinases themselves are phosphoproteins (if
phosphorylation is not driven by a kinase in V , we set Ei = ∅). The ability
of a kinase E ∈Ei to catalyse phosphorylation of Xi may be tempered
by inhibitors XI (I ∈Ii,E ⊂V ; the double subscript indicates that
inhibition is speciﬁc to both substrate and kinase). Thus the parents πi of
Xi comprise both the kinases and their inhibitors: πi = Ei ∪{Ii,E}E∈Ei.
Due to speciﬁcity of phosphorylation reactions, the underlying network G is
typically sparse, such that the number of parents πi for variate Xi is usually
low. An example is shown, using a standard graphical representation, in Fig.
1a. In what follows we use X0
i , Xi to denote the concentrations of proteins
X0
i , Xi respectively; Ui = X0
i + Xi is then the total concentration of
protein i, which is taken to be approximately invariant over the timescale of
phosphorylation dynamics.
2


## Page 3


Network Inference Using Goldbeter-Koshland Kinetics
X0
1
X1
X0
2
X2
X3
X0
3
X0
4
X4
(a)
X1
X2
X3
X4
. . .
Xp
Xi
X0
i
inhibitor
kinase
kinase
fi(Xπi, Ui; θi) =
V2X2X0
i
X0
i +K2(1+X4/K4)
+ VpXpX0
i
X0
i +Kp −V0Xi
(Ui = X0
i + Xi)
(b)
E ∈Ei
XE
I ∈Ii,E
XI
X0
i
Xi
σ
V0
VE
KE
VI
KI
(c)
Fig. 1: Overview of approach. (a) An example of a phosphorylation network. (b) Our approach couples automatic generation of chemical
models with Bayesian model selection to infer regulators πi of species i. (c) A statistical formulation (graphical model) for equilibrium
phosphorylation of species i is characterised by specifying kinases (E ∈Ei) and inhibitors (I ∈Ii,E) of kinases. [Bounding boxes in this
case are used to indicate multiplicity of variables, shaded nodes are observed with noise.]
For network inference, model selection will take place over parent sets
πi. Accordingly, we require functional equations for any such subset (Fig.
1b). Following the biochemical literature (Kholodenko, 2006; Steijaert et
al., 2010), we use ODEs of the Michaelis-Menten type to provide a suitable
class of analytic approximations for phosphorylation dynamics. The rate of
phosphorylation X0
i →Xi due to kinase Xj is given by V XjX0
i /(X0
i +
K), which explicitly acknowledges variation of kinase concentration Xj
and permits kinase-speciﬁc response proﬁles (parameterised by K) with
maximum reaction rate V .
Equilibrium analysis of the foregoing kinetic model yields functional
relationships between nodes that we use to inform analysis of steady-state
data. The famous example of Goldbeter and Koshland (1981) considered
phosphorylation by a single enzyme (XE) and dephosphorylation by a
single phosphatase (XP ), which at equilibrium satisfy the balance equation
VEXEX0
i
X0
i + KE
= VP XP Xi
Xi + KP
(1)
whose solution Xi = fi((XE, XP ), X0
i ; θi) is capable of expressing
a range of biologically relevant nonlinearities. In this work we extend
the class of molecular regulatory mechanisms by entertaining multiple
(independent) kinases along with competitive inhibition, where substrate
(X0
i ) and inhibitor (XI) compete for the same binding site on the enzyme
(XE):
XEXI ⇌XE ⇌XEX0
i →XE + Xi
(2)
When multiple inhibitors (I, I′) are present, they are assumed to act
exclusively, competing for the same binding site on the enzyme:
XEXI′ ⇌XE ⇌XEXI′
(3)
Mathematically, competitive inhibition by exclusive inhibitors corresponds
to rescaling of the Michaelis-Menten parameter
KE 7→KE
 
1 +
X
I∈Ii,E
XI
KI
!
.
(4)
where the sum ranges over inhibitors I of the kinase E. Phosphatase
speciﬁcity is currently poorly characterised compared with kinase speciﬁcity,
so our analysis does not attempt to cover this level of regulation. In particular
dephosphorylation is assumed to occur at a rate V0Xi proportional to the
amount of phosphoprotein. Collecting together our modelling assumptions
and solving the resulting balance equation produces a functional model class
F, with member functions fi ∈F given by
fi(Xπi, Ui; θi) =
X
E∈Ei
VE/V0XEX0
i
X0
i + KE
 1 + P
I∈Ii,E
XI
KI
 .
(5)
Here the parameter vector θi contains the maximum rates (V ) and
Michaelis-Menten constants (K) speciﬁc to phosphorylation of species i
(dependence of V , K on i is notationally suppressed for clarity). When
Ei = ∅we instead deﬁne fi = µi, equal to the average phosphoprotein
concentration.
2.3
Statistical Formulation
The Goldbeter-Koshland model (5) gives a general form for the functional
relationship between nodes at steady-state. Inference proceeds based on
a Bayesian formulation of this model (Fig. 1c). Consider independent
observations of protein expression obtained at equilibrium with respect
to phosphorylation dynamics. To ﬁx a characteristic scale, all data are
scale-normalised prior to inference such that each species has unit mean.
For a given protein i, a model Mi for phosphorylation describes putative
kinases Ei and associated inhibitors Ii,E (E ∈Ei) for protein i (note
that Mi contains more information than the subset πi, namely the speciﬁc
mechanistic roles played by each variable in πi). Then, conditional on Mi
and parameters θi we have the following statistical model
log(Xi) = log(fi(Xπi, Ui; θi)) + ϵi
(6)
where ϵi ∼N(0, σ2
i ). The logarithm of both predictor and response is taken
in order to improve the normality assumption on the error ϵi.
In the Bayesian setting, prior probability distributions are required for
parameters θi and models Mi. For the parameters θi
= (V , K, σ),
which we have augmented with σ (as with the other parameters, we
drop the subscript i on σ for clarity), physical considerations require that
Vj, Kj, σ > 0. Following Xu et al. (2010) we postulate that all biological
processes must occur on an observable timescale, motivating, in the shape,
scale parametrisation, the gamma priors V ∼Γ(2, 1/2), K ∼Γ(2, 1/2),
each of unit mean and variance 1/2. The noise parameter σ is inverse-
gamma distributed a priori as σ ∼Γ−1(6, 1), with prior mean 1/5 and
variance 1/100 chosen to correspond to the magnitude of measurement
noise in current proteomic technologies (Hennessey et al., 2010).
When expert opinion is available, rich subjective model priors may be
elicited (see e.g., for graphical models, Mukherjee and Speed, 2008), but for
this work we employed an objective prior, depending on a (possibly empty)
prior model M0
i . Prior speciﬁcation should account for the distinct roles of
kinases and inhibitors; a mathematical formulation for the objective model
prior is described in the Supplemental Information.
2.4
Reversible Jump Markov Chain Monte Carlo
The dimensionality of the parameter vector θM depends on the model M;
dim(θM) = dim(V M)+dim(KM)+1 where the former quantities are
3


## Page 4


Oates and Mukherjee
functions of the numbers of kinases and inhibitors according to M. Since we
seek models with high posterior probability, and noting that most models will
provide insufﬁcient explanatory power, we implement RJMCMC (Green,
1995) to reduce the effective size of model space. Following Green and
Hastie (2009) we enumerate all possible models as {M(k)}k∈K and deﬁne
the across-model state space
S =
[
k∈K
({k} × Θk),
k =
O
E∈EM(k)
({E} × IM(k)
E
)
(7)
where parameters θM(k) for model M(k) belong to Θk and ⊗denotes
the Cartesian product. The reversible jump sampler constructs an ergodic
Markov chain on S which has, as its stationary distribution, the posterior
probability distribution p(s|D), s
∈
S.
In particular the marginal
p(k|D) over the model index k
∈
K corresponds exactly to the
posterior model probabilities p(M(k)|D). Construction of an efﬁcient
RJMCMC sampler requires an intuition for the across model state space.
We adopt a deliberately transparent Metropolis-within-Gibbs approach
(Roberts and Rosenthal, 2006),
updating one coordinate of S at a
time using a Metropolis-Hastings accept/reject probability of the form
α(s, s′)
=
min(1, A(s, s′)p(D|s′)/p(D|s)). A number of distinct
proposal mechanisms were employed in order to ensure ergodicity and
provide rapid mixing. Precise details of the proposals used, along with their
associated ratios A(s, s′) may be found in the Supplemental Information.
For applications, 30,000 iterations of the Gibbs sampler were performed,
with 5,000 discarded as burn-in. Convergence was assessed using repeated
runs from dispersed initial conditions.
3
RESULTS
In this Section we empirically assess our methodology and compare
its performance against network inference based on the linear
model. In Section 3.1 we show results using a recently published
dynamical model of the MAPK signalling pathway due to Xu et
al. (2010), where the underlying network is known exactly. In
Section 3.2 we apply our approach to a real proteomic dataset, which
has an unknown and presumably more complex noise structure.
In both cases, for fair comparison between different methods, no
informative model priors were used (i.e. we set ∀i, M 0
i = ∅).
3.1
Simulation Study
Data were generated from a computational model of the MAPK
signaling pathway due to Xu et al. (2010), speciﬁed by a system
of 25 nonlinear ODEs (Fig. 2a). The simulation gives covariates
that are highly correlated at equilibrium, as would be expected
in practice, whilst providing a known network G for evaluation
purposes.
Further details regarding the computational model
are described in the Supplemental Information. We introduced
independent Gaussian measurement noise, additive on the log scale,
of magnitude σ = 0.2, similar to technical error incurred by current
proteomic technologies (Hennessey et al., 2010).
We benchmarked our approach against the linear-additive-
Gaussian formulation log(Xi) ∼N(1β0 + DMβM, σ2I) with
design matrix DM
=
[. . . log(Xj) . . . ]j∈πM
and intercept
β0; the logarithm of a vector is taken component-wise. All
variables were mean-variance standardised prior to inference. We
consider two standard approaches to inference for the linear model,
namely (1) the LASSO with penalty parameter set according to
cross validation (“Lin. Lasso”), and (2) a conjugate Bayesian
formulation (“Lin. Bayes”; Hill (2012)), based on the g-prior
βM ∼N(0, nσ2(D′
MDM)−1), with a ﬂat prior over the intercept
p(β0) ∝1 and reference prior over the noise p(σ) ∝1/σ. For
the Bayesian approach we took a model prior p(M) to be uniform
over in-degree d = dim(βM) with the restriction d ≤3. Model
averaging was then used to obtain posterior inclusion probabilities.
For each of the linear approaches (1) and (2) we also considered
adjusted variants (“Lin. Lasso Adj.” and “Lin. Bayes Adj.”) where
log-phospho-ratios log(Xi/Ui) constitute the response; this can be
motivated as a simple ﬁrst order correction for variation in total
protein levels.
For each phosphorylated or active species i in the computational
model, we sought to infer the parents πi. For a fair comparison
with the linear approaches, which do not ascribe functional roles
to variables, we did not distinguish between kinases and inhibitors
during assessment. The resulting receiver operating characteristic
(ROC) curves are shown in Fig. 2b. Overall performance was
quantiﬁed using area under the ROC curve (AUR), aggregated over
all i ∈V . Results are shown over 10 datasets D for each of various
combinations of sample size n and noise level σ (Fig. 2c). In all
regimes our approach outperformed linear approaches; the latter did
not perform well even in this low dimensional example. We note
also that even in the least challenging regime (n = 24, σ = 0), none
of the approaches were able to perfectly recover the entire network
G. The adjusted regressions, which model the log-phospho-ratio as
the response, did not outperform the standard linear regressions.
3.2
Cancer Proteomic Data
Data were obtained using reverse-phase protein arrays (RPPA;
Hennessey et al. (2010)) applied to a panel of breast cancer
cell lines (Neve et al., 2006). Data D comprised equilibrium
observations for p = 38 phosphorylated proteins, in addition to their
unphosphoryated counterparts (Fig. 3a). Cell lines belong to two
biologically distinct subtypes known as basal (n = 22) and luminal
(n = 21), with each member cell line comprising one sample. The
true data-generating network is not known for biological samples,
but for certain nodes the relevant kinase-substrate relationships have
been described in considerable mechanistic detail in the literature.
To minimize the risk of comparing results of inference against an
incorrect literature model, we focused attention on selected nodes
in the data for each of whom the key kinase is well established.
For example, the protein S6 is known to be phosphorylated via
the kinase activity of p70 S6 Kinase (p70S6K); both proteins are
included in our assay. Treating S6 as the target (i.e. the network
child), we scored each of the remaining 37 proteins as a candidate
regulator (i.e. for inclusion in the parent set πS6) using each method.
Fig. 3b displays the result of inference for the parents of S6 (S6
is phosphorylated on amino acid residues Serine 235,236; results
for basal subtype shown; measurements of S6 phosphorylation on
residues Serine 240,244 were excluded since this correlates closely
with phosphorylation on Serine 235,236). Despite the known well
established regulatory role for p70S6K, it is striking that only our
approach ranks p70S6K highly. The LASSO approaches ascribe
no weight to the correct kinase in this case. To gain more insight
into the assignment of weights by the competing methodologies we
constructed scatter plots comparing weight distributions (Fig. 3c).
It is immediately clear that the weight assignments vary markedly
between basal and luminal subtypes. In addition, it is noticeable
that there is little agreement between the apparently similar linear
formulations. We extended this investigation to several other key
signalling players whose regulation is well understood (Table 1).
4


## Page 5


Network Inference Using Goldbeter-Koshland Kinetics
EGFR
EGFR
SOS
SOS
SOS
C3G
C3G
EPAC
EPAC
RAS
RAS
RAP1
RAP1
RAF
RAF
RAF
BRAF
BRAF
PKA
PKA
MEK
MEK
ERK
ERK
GAP
PKAA
EPACA
Cilostamide
(a)
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
False Positive Rate
True Positive Rate
Averaged Receiver Operating Characteristic Curves
 
 
G.K. Kinetics
Lin.Bayes
Adj.Lin.Bayes
Lin.LASSO
Adj.Lin.LASSO
n=8,σ = 0.2
(b)
0.4
0.5
0.6
0.7
0.8
0.9
1
               
               
Lin. Lasso Adj.
               
               
               
     Lin. Lasso
               
               
               
Lin. Bayes Adj.
               
               
               
     Lin. Bayes
               
               
               
  G.K. Kinetics
               
n = 8, σ = 0.2   
n = 16, σ = 0.2   
n = 24, σ = 0.2   
n = 24, σ = 0   
Area Under ROC Curve
(c)
Fig. 2: Simulation study. (a) Computational model of the MAPK signalling pathway (due to Xu et al., 2010). Circles represent proteins,
rectangles represent interventions (drug treatments) used to perturb the system. For proteins, one strike-through represents inactivity, two
strikes represent degradation. (b) Average receiver operating characteristic (ROC) curves (sample size n = 24, noise σ = 0.2, see text
for details) using data generated from model (a). (c) Area under ROC curve (AUR) for each of the sample size (n) and noise (σ) regimes
shown (boxplots over 10 datasets for each n, σ regime). [Legend: “G.K. Kinetics”: network inference using Goldbeter-Koshland kinetics as
described in text; “Lin. Bayes”: Bayesian variable selection using linear model; “Lin. Lasso”: variable selection using LASSO and linear
model; “Lin. Bayes Adj.” and “Lin. Lasso Adj.”: as previous but corrected for total protein levels as described in text.]
Overall, we ﬁnd that the proposed approach outperforms the linear
methods.
4
DISCUSSION AND CONCLUSIONS
In this work we investigated integration of biochemical mechanisms
into network inference for steady-state data. We focused on protein
phosphorylation, a key biochemical process where the availability
of relatively sophisticated simulation models, extent of existing
mechanistic insight and availability of relevant proteomic data
combine to facilitate assessment of network inference approaches.
Our results,
on simulated and real data,
demonstrated that
protein signalling network topology may be estimated much
more successfully under our approach than by conventional linear
formulations. The linear approaches we used were outperformed
on simulated data and failed to identify known regulation in real
data. Further, we saw that apparently similar linear formulations can
return very different recommendations for which variables ought
to be included in the model; one possible explanation for such
disagreement may be model misspeciﬁcation. In addition to superior
performance,
a chemical formulation beneﬁts from increased
interpretability, ascribing mechanistic roles to variables and relating
parameters to scientiﬁcally interpretable rates.
Although we
focussed on network inference, the methodology presented here
simultaneously learns values for these rate parameters, providing
a ﬁtted predictive model of signalling dynamics.
Up to this point we have not discussed identiﬁability of either
parameters or structure. Parameter identiﬁability does not present
challenges within our Bayesian formulation when the objective is
structural inference. (The interested reader is referred to Craciun and
Pantea (2008); Calderhead and Girolami (2011) for discussions of
parameter identiﬁability in chemical systems.) It terms of structural
identiﬁability, Peters et al. (2011) recently discussed the limitations
that arise from symmetry inherent in the the linear-additive-
Gaussian model and showed that within an identiﬁable functional
model class (IFMOC) it is possible to estimate causal relationships
with statistical consistency. However, in order to formally show
that a given functional class constitutes an IFMOC, the theory at
present requires strong assumptions, including acyclicity of the
causal graph, that do not hold in many real systems, including
protein signalling networks. When faced with such challenging
circumstances, empirical investigations naturally have a key role to
play. In this sense, our contribution demonstrates that the theoretical
results of Peters et al. (2011) have substantive implications for
biological network inference in practice. Further work will be
required to better understand these implications and to extend
the ideas presented here to further application domains, including
gene regulation. In complementary work, (Oates and Mukherjee,
2012b) considered the use of nonlinear chemical kinetics for
network inference using time-course data, reporting that a chemical
formulaion outperformed a number of mechanism-free approaches,
including nonparametric models.
Network inference is naturally facilitated by interventional
experiments (Lu et al., 2011), however adequate modelling of
the effects of intervention is important to ameliorate statistical
confounding (Pearl, 2009). Within a chemical kinetic framework
such factors may be easily accounted for;
for instance a
perfect intervention simply corresponds to removal of the targeted
species from the chemical model. In testing, not presented here,
we extended our methodology to incorporate imperfect certain
intervention, where the interventional targets are assumed known,
but the interventions may not completely block catalytic activity of
their targets (see Eaton and Murphy, 2007, for a general discussion
of interventions in graphical models). In the context of protein
5


## Page 6


Oates and Mukherjee
Protein Species 
Log(expression) 
Basal 
Luminal 
(a) Phosphoproteomic data obtained from breast cancer cell lines
0
5
10
15
20
25
30
35
40
0
0.5
1
G.K. Kinetics
 
 
0
5
10
15
20
25
30
35
40
0
0.5
Lin. Bayes
0
5
10
15
20
25
30
35
40
0
0.1
0.2
Lin. Bayes Adj.
0
5
10
15
20
25
30
35
40
0
0.2
0.4
Lin. Lasso
0
5
10
15
20
25
30
35
40
0
0.5
1
Lin. Lasso Adj.
Phosphorylated Proteins (ranked by scores)
incorrect proteins
p70S6K
(b) Inferred parents (ranked) for S6, based on basal cell line
data
p70S6K 
Inference for regulators of p-S6 
G.K. Kinetics 
(c) Comparison of competing methodologies
Fig. 3: Cancer protein data. (a) Heatmap of reverse-phase protein
array data from a panel of breast cancer cell lines. (b) Proteins
were ranked as potential regulators of the node S6 under each
methodology. The protein p70 S6 Kinase (p70S6K) is known to be
a key kinase for the node S6; this known regulator is shown in red
in the bar plots. (c) Comparison of methodologies: Each point in the
scatter plots represents one phosphoprotein, with the known kinase
p70S6K highlighted in bold. [(b) and (c) display weights (posterior
probabilities or absolute regression coefﬁcients) assigned to each
protein by each method.
phosphorylation, kinases and their inhibitors can be intervened upon
using agents (such as monoclonal antibodies or small molecule
inhibitors). We modelled these effects by rescaling the effective
concentration of interventional targets, in the presence of the
treatment, as Xj 7→αjXj where 0 ≤αj ≤1 is an unknown
parameter capturing interventional efﬁcacy of the agent. Using this
extended methodology we observed that interventional experiments
were more informative than the global perturbation experiments
considered here, leading to improved AUR scores.
Network inference based on nonlinear models is computationally
challenging. We considered low-to-moderate dimensional settings
(p = 12, 38), for which the RJMCMC proved to be effective. The
computations in this paper are parallelisable by population Monte
Carlo techniques (Laskey and Myers, 2003), and it may therefore
be possible to also extend this work to the high-dimensional setting
(Lee et al., 2010). In general, nonlinear approaches are clearly
more burdensome than their linear counterparts, where highly
efﬁcient approaches, including those based on LASSO and related
penalised likelihood schemes, allow rapid estimation even in high
dimensions (Meinshausen and B¨uhlmann, 2006). We therefore view
the methods presented here as complementary to variable selection
based on linear models, allowing more reﬁned exploration in
settings where some insight into underlying dynamics is available.
Target:
Akt
p70S6K
S6
p53
G.K. Kinetics
4
3
1
8
Lin. Bayes
10
9
15
32
Lin. Bayes Adj.
14
8
8
14
Lin. Lasso
NA
8
NA
NA
Lin. Lasso Adj.
NA
12
NA
NA
Total # Candidates:
36
37
36
37
Table 1. Cancer protein data, comparison of methods. The proposed method
was compared with linear approaches using reverse-phase protein array data
for nodes whose regulation has been extensively studied in the literature.
Each method ranked potential regulators among candidate proteins; here we
display the rank assigned to the known kinase, using each of the 5 methods.
For example, Fig 3b shows such an analysis for the target node (i.e. network
child) S6, where G.K. Kinetics ranked the known kinase p70S6K 1st out of a
total of 36 candidates. High rank indicates that the known kinase is correctly
highlighted in the analysis; the highest-ranked result is highlighted in bold
for each target node. Here we show the rank assigned to the known kinase for
each of the target nodes Akt, p70S6k, S6 and p53. [“NA” indicates that the
known kinase received zero weight. Alternative phospho-forms of the target
were excluded as candidates for Akt and S6, so that there were 36 candidates
rather than 37. Here we present results obtained using data from cell lines of
basal subtype; luminal results are shown in Supplementary Information.]
On real proteomic data we observed that network inference was
challenging. In particular, inference based on data obtained from
luminal cell lines encouraged poor performance from all approaches
(see Supplemental Information). Whilst the genomic background
(in our example breast cancer) may be a factor - illustrated by the
luminal failure case - we suspect that the real difﬁculties result from
a complex noise process. At present, network inference can aid in
hypothesis generation, but care must be taken in interpreting results.
Further experimental and methodological advances will be required
6


## Page 7


Network Inference Using Goldbeter-Koshland Kinetics
before network inference methods can be regarded as truly robust
tools for biological discovery.
In
this
work
we
investigated
integration
of
biochemical
mechanisms into network inference.
Whilst the Goldbeter-
Koshland formulae are invalid at the single-cell level, which
is intrinsically stochastic, the evidence presented here suggests
that these deterministic nonlinear equations represent a better
approximation than the corresponding linear equations. In particular
a chemical kinetic formulation is able to account, in a principled
way,
for variation in total protein levels between samples.
Consequently, inferred edges cannot be interpreted as indicators of
direct biochemical interaction; rather an edge corresponds to the
prediction that intervention on the parent will result in a change in
expression of the child, possibly indirectly via unobserved variables.
In our real data example we therefore allowed for candidate species
which are not themselves kinases, such as S6 and p53.
For simplicity,
in specifying the class F
of functional
forms, we did not consider post-translational modiﬁcations such
as ubiquitinylation,
nor spatial effects such as translocation,
nor did we explicitly distinguish between phosphorylation on
different residues. The methodology which we presented may be
generalised to other molecular mechanisms. In particular alternative
mechanisms of enzyme interaction such as noncompetitive,
uncompetitive, hyperbolic and parabolic inhibition could be readily
integrated into our framework.
ACKNOWLEDGEMENT
Funding: Financial support was provided by NCI CCSG support
grant CA016672, NIH U54 CA112970, UK EPSRC EP/E501311/1
and the Cancer Systems Biology Center grant from the Netherlands
Organisation for Scientiﬁc Research.
REFERENCES
Bansal, M. et al. (2007) How to infer gene networks from expression proﬁles, Mol. Sys.
Bio., 3, 78.
Bender, C. et al (2010) Dynamic deterministic effects propagation networks: learning
signalling pathways from longitudinal protein array data, Bioinformatics, 26(ECCB
2010), i596-i602.
Bintu, L. et al. (2005) Transcriptional regulation by the numbers: models, Curr. Opin.
Genet. Dev., 15(2), 116-124.
Calderhead, B., Girolami, M. (2011) Statistical analysis of nonlinear dynamical systems
using differential geometric sampling methods, J. Roy. Soc. Interface Focus, 1(6),
821-835.
Cantone, I. et al. (2009) A yeast synthetic network for in vivo assessment of reverse-
engineering and modeling approaches, Cell, 137(1), 172-81.
Chen, W. et al. (2009) Input-output behavior of ErbB signaling pathways as revealed
by a mass action model trained against dynamic data, Mol. Sys. Bio., 5, 239
Chou, I.C., Voit, E.O. (2009) Recent Developments in Parameter Estimation and
Structure Identiﬁcation of Biochemical and Genomic Systems, Math. Biosci.,
219(2), 5783.
Craciun, G., Pantea, C. (2008) Identiﬁability of chemical reaction networks, J. Math.
Chem., 44, 244-59.
Eaton D, Murphy K (2007) Exact Bayesian structure learning from uncertain
interventions, Proc. 11th Conf. Artiﬁcial Intelligence and Statistics (AISTATS-07).
Goldbeter, A., Koshland, D.E. (1981) An ampliﬁed sensitivity arising from covalent
modiﬁcation in biological systems, Proc. Nati Acad. Sci., 78(11), 6840-6844.
Green, P.J. (1995) Reversible jump Markov chain Monte Carlo computation and
Bayesian model determination, Biometrika, 82(4), 711-732.
Green,
P.,
Hastie,
D.
(2009)
Reversible
jump
MCMC,
technical
report
(http://www.maths.bris.ac.uk/mapjg/Papers.html).
Heagerty, P.J., Kurland, B.F. (2001) Misspeciﬁed Maximum Likelihood Estimates and
Generalised Linear Mixed Models, Biometrika, 88(4), 973-985.
Hecker, M. et al. (2009) Gene regulatory network inference: Data integration in
dynamic models - A review, Biosystems, 96(1), 86-103.
Hennessey, B.T. et al. (2010) A Technical Assessment of the Utility of Reverse Phase
Protein Arrays for the Study of the Functional Proteome in Nonmicrodissected
Human Breast Cancer, Clin. Proteom., 6, 129-151.
Hill, S. (2012) Sparse Graphical Models for Cancer Signalling, PhD Thesis, University
of Warwick, U.K.
Kholodenko, B.N. (2006) Cell-signalling dynamics in time and space, Nat. Rev. Mol.
Cell Bio., 7(3), 165-176.
Kim, S.Y., Imoto, S., Miyano, S. (2003) Inferring gene networks from time series
microarray data using dynamic Bayesian networks, Brieﬁngs in Bioinformatics,
4(3), 228-35.
Kim, S.Y., Ferrell, J.E. (2007) Substrate Competition as a Source of Ultrasensitivity in
the Inactivation of Wee1, Cell, 128, 11331145.
Laskey, K.B., Myers, J. (2003) Population Markov Chain Monte Carlo, Mach. Learn.,
50(12), 175196.
Lee, A. et al. (2010) On the Utility of Graphics Cards to Perform Massively Parallel
Simulation of Advanced Monte Carlo Methods, J. Comp. and Graph. Stat., 19(4),
769-789.
Lee, W.P., Tzou, W.S. (2009) Computational methods for discovering gene networks
from expression data, Brief. Bioinform., 10(4), 408-423.
Leskovac, V. (2003) Comprehensive enzyme kinetics, Springer.
Li, C-W., Chen, B-S. (2010) Identifying Functional Mechanisms of Gene and Protein
Regulatory Networks in Response to a Broader Range of Environmental Stresses,
Comp. and Func. Genomics, 408705.
Lu, Y. et al. (2011) Kinome siRNA-phosphoproteomic screen identiﬁes networks
regulating Akt signaling, Oncogene, 30, 4567-77.
Lv, J., Liu, J.S. (2010) Model Selection Principles in Misspeciﬁed Models, Technical
Report, arXiv:1005.5483v1.
Markowetz, F., Spang, R. (2007) Inferring cellular networks - A review, BMC
Bioinformatics, 8(Suppl. 6), S5.
Meinshausen, N., B¨uhlmann, P. (2006) High-dimensional graphs and variable selection
with the lasso, The Annals of Statistics, 34(3), 1436-62.
Min Lee, J. et al. (2008) Dynamic Analysis of Integrated Signaling, Metabolic, and
Regulatory Networks, PLoS Comput. Biol., 4(5), e1000086.
Morrissey, E.R. et al. (2010) On reverse engineering of gene interaction networks using
time course data with repeated measurements, Bioinformatics, 26(18), 2305-2312.
Mukherjee, S., Speed, T.P. (2008) Network inference using informative priors, Proc.
Nat. Acad. Sci., 105(38), 14313-14318.
Nam, D., Yoon, S.H., Kim, J.F. (2007) Ensemble learning of genetic networks from
time-series expression data, Bioinformatics, 23(23), 3225-3231.
Neve, R. et al. (2006) A collection of breast cancer cell lines for the study of
functionally distinct cancer subtypes, Cancer Cell, 10(6), 515-527.
Oates, C., Mukherjee, S. (2012a) Network Inference and Biological Dynamics, To
Appear in the Annals of Applied Statistics.
Oates, C., Mukherjee, S. (2012b) Structural inference using nonlinear dynamics,
CRiSM Working Paper Series, No. 12-07.
Oates, C., Mukherjee, S. (2012c) On the relationship between ODEs and DBNs,
Technical Report, arXiv:1201.3380v2.
Opgen-Rhein, R., Strimmer, K. (2007) Learning causal networks from systems
biology time course data: an effective model selection procedure for the vector
autoregressive process, BMC Bioinformatics, 8, (Suppl. 2), S3.
Pearl, J. (2009) Causal inference in statistics: An overview, Stat. Surveys, 3, 96-146.
Peters, J. et al. (2011) Identiﬁability of Causal Graphs using Functional Models, Proc.
27th Ann. Conf. Uncertainty in Artiﬁcial Intelligence (UAI-11), 589-598.
Roberts, G.O., Rosenthal, J.S. (2006) Harris Recurrence of Metropolis-within-Gibbs
and Trans-Dimensional Markov Chains, Ann. App. Prob., 16(4), 2123-2139.
Sachs, K. et al (2005) Causal protein-signaling networks derived from multiparameter
single-cell data, Science, 308, 5239.
Schoeberl, B. et al. (2002) Computational modeling of the dynamics of the MAP kinase
cascade activated by surface and internalized EGF receptors, Nat. Biotech., 20(4),
370-375.
Steijaert, M.N. et al. (2010) Computing the Stochastic Dynamics of Phosphorylation
Networks, J. Comp. Bio., 17(2), 189-199.
Xu, T. et al. (2010) Inferring signaling pathway topologies from multiple perturbation
measurements of speciﬁc biochemical species, Sci. Sig., 3(113), ra20.
7

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1306_1904v1_network_inference_using_steady_state_data_and_goldbeter_koshland_kinetics
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1306_1904V1_NETWORK_INFERENCE_USING_STEADY_STATE_DATA_AND_GOLDBETER_KOSHLAND_KINETICS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

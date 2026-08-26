---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1808.00301v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1808.00301v1_Advances_in_computational_modeling_approaches_in_pituitary_gonadotropin_signalin

> Source: 1808.00301v1_Advances_in_computational_modeling_approaches_in_pituitary_gonadotropin_signalin.pdf

> Pages: 35

---


## Page 1


Advances in computational modeling approaches in pituitary gonadotropin signaling
Romain Yvinec1, Pascale Crépieux1, Eric Reiter1,  Anne Poupon 1 and Frédérique Clément2,3
1 PRC, INRA, CNRS, IFCE, Université de Tours, 37380 Nouzilly, France.
2Inria, Université Paris-Saclay, 91120 Palaiseau, France.
3LMS, Ecole Polytechnique, CNRS, Université Paris-Saclay 91128  Palaiseau, France,
Corresponding author : 
Romain Yvinec 
romain.yvinec@inra.fr
    
Abstract 
Introduction
Pituitary gonadotropins play an essential and pivotal role in the control of 
human and animal reproduction within the hypothalamic-pituitary-gonadal ( H P G )  axis. 
The computational modeling of pituitary gonadotropin signaling encompasses phenomena of 
different  natures  such  as  the dynamic  encoding o f  gonadotropin  secretion, and  the 
intracellular cascades triggered by gonadotropin binding to their cognate receptors, resulting in 
a variety of biological outcomes. 
Areas covered  We overview historical and ongoing issues in modeling and data analysis 
related to gonadotropin secretion in the field of both physiology and neuro-endocrinology. We 
mention the different mathematical formalisms involved, their interest and limits. We discuss 
open  statistical questions in signal analysis associated with  key  endocrine  issues. We also 
review recent advances  in the modeling of the intracellular pathways  activated by 
gonadotropins, which  yields promising development for innovative  approaches  in drug 
discovery.
Expert opinion The greatest challenge to be tackled in computational modeling of pituitary 
gonadotropin signaling is the embedding of gonadotropin signaling within its natural multi-
scale environment, from the single  cell  level, to the organic and whole HPG level. The 
development of modeling approaches of G protein-coupled receptor signaling, together with 
1


## Page 2


multicellular systems biology may lead to unexampled mechanistic understanding with critical 
expected fallouts in the therapeutic management of reproduction.
Keywords: FSH, GnRH, GPCR signaling, hormone rhythms, LH, mathematical models, multi-
scale modeling, systems biology.
Article highlights box: 

Modeling of pituitary gonadotropin blood levels involves underlying endocrine feedback 
loops to shed light on the complex dynamical patterns of hormonal rhythms.

Sophisticated statistical tools are needed to decipher the encoding of hormonal signals 
within the HPG axis.

Dynamical modeling of the intracellular gonadotropin signaling networks leads to a 
mechanistic understanding of the gonadotropin action in a short time scale.

Multi-scale modeling is needed to renew our understanding of the molecular, cellular, and 
physiological processes underlying the control of the reproductive function.

Innovative approaches in drug discovery may arise from integrating the cellular and 
intracellular scales in a multi-scale modeling framework of the reproduction axis.
1) Introduction: 
Systems Biology, which heavily relies on mathematical modeling, has long been recognized as an 
opportunity  to  discover  new, more  efficient  and  safer, drugs  [1-3].  Systems  Biology  driven 
mathematical models allow one to understand the consequences of a local perturbation on the whole 
network behavior. For example, these models help understanding the effect of a drug, whose target 
is located in a precise cell type, on the physiological function this cell type participates in. These 
2


## Page 3


models are also very useful for determining the best targets within a physiological net [4]. As stated 
by the statistician George Box, “all models are wrong, but some are useful” [5]. Indeed, models 
have been proven to be useful in many different situations, from the network-based classification of 
metastatic cancers [6], or the susceptibility to metabolic disorders  [7], to the study of anti-
angiogenic therapies in cancer [8] and the mechanisms underlying neurodegeneneration [9], just to 
name a few. However, modeling is not a straightforward task, and requires both the detailed 
knowledge of the studied system, and the selection of the most adapted mathematical formalism. In 
view of the complexity of the reproductive system, arising in particular from the multiple entangled 
levels of controls and its highly dynamic characteristics, it is understandable that the in-silico 
modeling approaches to drug discovery for reproductive biology are still in its infancy. Yet, a 
variety of mathematical tools have been used to help understanding the dynamics of the pituitary 
gonadotropin signaling and its perturbation, within the HPG axis. Here we present the state of the 
art  in  mathematical  modeling  applied  to  pituitary  gonadotropin  signaling,  which  could  help 
designing better therapeutic solutions for reproductive disorders. 
Pituitary gonadotropins are high molecular weight glycoproteins secreted by a specific type of 
pituitary cells, the gonadotrophs. In vertebrates, the pituitary gland is a pivotal organ within the 
neuroendocrine axes, linking the hypothalamus (and afferent connections) belonging to the central 
nervous system, to the peripheral target organs. In the hypothalamic-pituitary-gonadal (HPG) axis, a 
unique hypothalamic neuro-hormone, GnRH (gonadotropin-releasing hormone), exerts a direct and 
differential control onto the production and secretion of two pituitary hormones, FSH (follicle-
stimulating hormone) and LH (luteinizing hormone) released by the same cell type. 
FSH and LH control the double gonadal function of gametogenesis and steroidogenesis, through G 
protein-coupled receptors (GPCR) expressed specifically on somatic cells. In the testes, Leydig 
cells are endowed with LH receptors (LHCGR), while Sertoli cells express FSH receptors (FSHR) 
3


## Page 4


[10]. In the ovaries, granulosa cells of growing follicles bear FSHR, theca and granulosa cells from 
preovulatory  follicles  express  LHCGR [11].  Gonadal  steroid  hormones  like  estradiol  (E2), 
progesterone (P), and testosterone (Te)  modulate in turn the secretion of pituitary LH and FSH,  as 
well as hypothalamic GnRH, within entangled endocrine feedback loops. FSH secretion is further 
tuned by inhibin (a peptide hormone of gonadal origin) and, in addition, inhibin action is enhanced 
or toned down by local paracrine secretion of activin and follistatin, respectively [12]. In female, 
each reproductive cycle is characterized by a drop in FSH level, which is first suppressed by 
gonadal inhibin emanating  from the  whole cohort  of terminally  growing  follicles, while  the 
contribution of the dominant follicle(s) to E2 production further impact FSH secretion at the end of 
the follicular phase [11,13]. Note that there exist other gonadotropins that are not secreted from the 
pituitary. For instance,  the human chorionic gonadotropin (hCG) has  a placental  origin,  and 
interacts with the LHCGR of the ovary and promotes the maintenance of the corpus luteum during 
the beginning of pregnancy. We will deal almost exclusively with pituitary gonadotropins in this 
article.
The secretion patterns of GnRH, FSH and LH have remarkable dynamic features. GnRH is secreted 
in pulses, and its encoding as a pulsatile signal is a prerequisite to sustain gonadotropin secretion. 
As a result of the excitation-secretion coupling in gonadotroph cells, involving calcium-mediated 
exocytosis of secretion granules, LH is also secreted in a pulsatile manner. In contrast, FSH appears 
to be mainly secreted in a calcium-independent basal manner (Note that basal secretion does not 
imply time-constant FSH level nor constant secretion rate). In addition, in each species investigated 
so far, including non human primates [14,15], FSH and LH are secreted massively at the time of 
ovulation, under the control of the GnRH surge, occurring each ovarian cycle [16]. 
4


## Page 5


In the gonads, at the cellular scale, FSH and LH trigger, through their cognate GPCRs, multiple 
connected signaling pathways conveying hormonal signals. Multiple  feedbacks and cross-talks 
contribute to a complex signaling network, which results in various cellular responses, spanning 
distinct spatial and time scales, from short-range membrane protein activation to sustained signaling 
and cell-cell communications [17].
Understanding the pituitary gonadotropin signaling is thus a challenging and multi-faceted issue, 
which does not only encompass the outcomes of ligand binding to the receptor, but also the 
dynamic encoding of the gonadotropin signal, subject to multiple feedback controls. In agreement 
to their role as pivotal endocrine players within the HPG axis, LH and FSH signaling networks are 
embedded in a multi-scale framework.
In the following, we will illustrate, with the help of selected instances, different approaches of 
modeling covering some of these facets and calling to various modeling formalisms.
2) Encoding the pituitary gonadotropin signal 
We will first give an overview on different computational approaches aiming to reproduce and 
analyze the changes in the secretion rates of gonadotropins and the resulting, finely tuned, time-
varying blood levels of pituitary gonadotropins in a physiological context. 
These approaches deal with the encoding of gonadotropin levels as dynamic endocrine signals. 
These signals follow various dynamic regimes, mainly (quasi-)steady states or oscillatory regimes, 
and  are  characterized  by a  combination  of properties  (amplitude,  frequency, duration)  either 
considered on a rather long term (typically on the several-week term of an ovarian cycle, on a day-
to-day basis), or on a shorter term (the several-hour term of secretion events considered as such). 
In  the  former  case,  the  main  motivation  is  to  be  able  to  reproduce  both  qualitatively  and 
quantitatively the patterns of FSH and LH levels, together with the levels of gonadal hormones. It 
amounts to setting in a proper mathematical music the multiple and entangled feedback loops at 
5


## Page 6


play within the HPG axis. In the latter case, the main motivation is to dissect the different steps (i.e. 
production, release, clearance) of the secretion events in order to get access to hidden endocrine 
information (typically the secretion rate in the cavernous sinus [18]), and to analyze possible 
differences in the secretion patterns specific to physiological conditions (i.e. age, gender, puberty) 
or pathological situations.
2.1) Modeling the fluctuations in hormonal levels as the result of endocrine feedback loops 
within the HPG
The observation of the periodic and coordinated fluctuations in hormone levels along the ovarian 
cycle, especially along the menstrual cycle in the human species, has been the initial driving force 
for the development of dynamic models of the interactions between the ovaries and pituitary gland. 
A long modeling history, continuing up to now [19], started from the core “push-and pull” concept 
associated with the FSH/estradiol feedback loop (FSH-stimulated estradiol secretion as opposed to 
estradiol-inhibited FSH secretion) studied as soon as in the early 1940s. The pioneering work of 
Lamport [20] was the first to investigate this question from a mathematical perspective and to 
introduce the natural mathematical formalism of ordinary differential equations (ODE) (Brief 
definitions and explanations of all technical mathematical terms are provided in a glossary in 
annex.)  to tackle endocrine issues.
The two-dimensional linear ODE model analyzed by Lamport in 1940, modeling the estradiol level 
as a damped harmonic oscillator, failed to reproduce properly the pattern of estradiol oscillations. It 
was only twenty years later that this drawback was circumvented by Thompson [21], who separated 
the contribution of the growing dominant follicle (the future ovulatory follicle) to estradiol secretion 
in a three dimensional extension of the initial model. The model studied by Thompson is piecewise 
linear with reset “decision” functions (the size of the dominant follicle is reset to 0 after reaching a 
6


## Page 7


given  threshold,  representing  the  occurrence of  ovulation),  and  its  solution  is  an  undamped 
oscillator.
Later developments, with a gold age in the early 1970s, have progressively complexified the model 
core structure, by adding nonlinearities in hormonal interactions, and other endocrine players, 
mainly progesterone and LH. Among others, a seminal instance is provided by the work of Bogumil 
et al. [22]. They considered a rudimentary pulsatile-like mode of LH secretion and distinguished the 
episodic secretion regime during the ovulatory surge from the constitutive FSH secretion or 
pulsatile LH secretion in the remaining of the ovarian cycle (the authors qualify as “tonic” and 
“phasic” the general versus surge secretion regime). The key ingredients of the gonadotropin 
dynamics mostly rely on three mechanisms: (1) FSH and LH secretions are controlled by nonlinear 
feedback terms mediating the effects of gonadal, and possibly adrenal, steroids; (2) FSH and LH 
removal rates in the plasma  are linearly proportional to their plasma levels (first order process, or 
single exponential decay); (3) the LH surge occurs as a result of LH accumulation in the pituitary 
gland, controlled by stepwise functions that integrate through time the positive stimulus of steroids. 
Bogumil et al also introduced a more elaborate description of ovarian follicle dynamics, again with 
threshold-mediated transitions, including the FSH-induced recruitment of a cohort of growing 
follicles, as well as different development stages for the dominant follicle and corpus luteum. 
Altogether, combining the endocrine variables with the physiological ones, the model consists in 34 
equations, involving a system of algebraic-integro-differential equations.
An alternative way to generate proper hormonal patterns while keeping a relatively tractable 
mathematical  formalism  is  the  use  of  delay  differential  equations  (DDE).  In  the  context  of 
gonadotropin dynamic models, explicit constant time delays are often used in feedback terms 
entering the FSH and LH secretion rates. This is consistent with the effective latency in the 
7


## Page 8


feedback of gonadal hormones, upon pituitary gonadotropin hormone synthesis. For instance Clark 
et al. have designed in [23] an autonomous DDE system reproducing the average levels of FSH and 
LH, subject to the control exerted by estradiol, inhibin and progesterone, without introducing 
stepwise decision functions nor convolution integrals. Applying tools from Hopf bifurcation theory 
and performing numerical simulations, they have shown the existence of two distinct, locally 
asymptotically stable, periodic solutions. The first one is consistent with the hormonal patterns in 
normal menstrual cycles, and the other one to an abnormal cycle,  that can correspond to a 
pathological endocrine status such as the Polycystic Ovarian Syndrome. Further developments and 
variants of this model have been proposed and are reviewed in [24]. The model can be refined by 
embedding additional variables to include more detailed biological knowledge. In particular, the 
distinction between two types of inhibin (inhibin A and  inhibin B), which affect differentially the 
synthesis of FSH, and the role of Anti-Müllerian Hormone (AMH) on the developing follicles was 
included in [25]. These refinements allowed the authors to broaden the timescale of the model up to 
a lifelong model, and to investigate the impact of a putative AMH treatment on the onset of 
menopause.
The efforts in developing models of hormone interactions mainly regard the hypothalamic-pituitary-
ovarian axis in women. Nevertheless, several approaches have tackled similar issues in different 
breeding [26] or laboratory species [27]. For instance, in line with the approach followed in [23], a 
model based on DDE has been designed in [26] for the bovine species, whose ovarian physiology is 
rather close to human ovarian physiology (roughly comparable duration of the ovarian cycle, 
existence of follicular waves and similar size of the ovarian follicles). Interesting approaches in fish 
species  [28,29] have  also  been  developed  with  an  underlying  motivation  of  comprehensive 
ecotoxicology. 
8


## Page 9


The models discussed so far are physiologically-based pharmacokinetic (PBPK) models, where 
secretion/clearance mechanisms are included as building blocks, and hormone circulating levels are 
related to one another by means of linear or nonlinear functions. Such equations intend to describe 
in a simple (or even simplistic) way the recurrent growth and decline of the steroidogenic ovarian 
tissues, ovarian follicles and corpus luteum. This is possible with the help of logic, rather than 
dynamic smooth, functions to compensate for the inaccurate understanding of some processes 
and/or to skip too complex phenomena. The rationale behind the construction of such models is thus 
to embed the endocrine and physiological knowledge available at the time of the model design in a 
single mathematical framework. Beyond the question of gonadotropin dynamics, the concomitant 
study  of  such  models  has  motivated  important  advances  in  the  theoretical  understanding  of 
dynamical systems [30,31] in the mathematical physiology and mathematical biology communities.
As far as the hypothalamic-pituitary-testicular axis in men or males, a similar core structure as the 
E2-FSH push-and-pull concept arises from the GnRH-LH-testosterone feedback loop: GnRH-
stimulated LH secretion, LH-stimulated testosterone secretion, and testosterone-inhibited GnRH 
secretion. This concept was first illustrated by Smith [32] who used the ODE formalism to derive a 
three-dimensional model analogous to the widespread feedback repression or Goodwin model (see 
[31]), and obtained an oscillatory solution that could describe periodic hormone patterns. We refer 
to  [33]  for  recent  developments  based  on  a  DDE  formalism,  and  model  outputs  matching 
experimental  observation  under  normal  and  perturbed  conditions  (such  as  castration  and 
testosterone replacement). 
2.2) Computational approaches of the GnRH and LH pulse generator
The endocrine system in male, as compared to females, has relatively simpler key features: a main 
gonadal player, testosterone, a static  pool of steroidogenic cells  in  the gonad, no surge nor 
9


## Page 10


qualitative change in the secretion regime on the central side. Inhibin also affects FSH secretion in 
males [10], and oestradiol seems to contribute significantly to the steroid feedback exerted by testes 
onto the hypothamo-piuitary axis. However, the role of testosterone is prominent in the control of 
the GnRH-LH system, and has been the main focus of modeling approaches designed on the whole 
HPG scale. This has encouraged the design of more comprehensive modeling approaches facing 
explicitly the issue of GnRH and LH pulse modeling and its embedding within the whole HPG axis. 
The difficulty arises from the almost discontinuous character of pulses (with GnRH signal being 
encoded as a square wave) and the discrete nature of the times of pulse release events. To represent 
point events, one has to call to other mathematical formalisms than autonomous ODE or DDE 
systems: stochastic point processes [34], stochastic differential equations (SDE) [35], excitable 
dynamics in the framework of impulse ordinary differential equations [36], or stiff nonlinear ODE 
with several timescales [37].
Even  if  the  variety  of  the  involved  formalisms  hamper  direct  comparisons  between  these 
approaches, they all share the ability to generate time series of GnRH and/or LH inter-peak intervals 
(IPI) to follow on a short term basis (generally on the order of several hours) the pulse frequency 
and the frequency modulations related to physiological (e.g. circadian rhythmicity at puberty) or 
pathological (e.g. exposure to endocrine disruptors) conditions. In contrast, notwithstanding the 
specific mathematical formalism, they may differ according to the access to endocrine data. 
Clinically-oriented studies can only make use of LH time series.  Information on GnRH activity is 
not available, so that GnRH pulse times must be inferred from LH pulse times. In this framework, 
even if elaborate theoretical and computational works, mostly based on deconvolution methods, 
manage to reconstruct the most plausible (in a statistical sense) GnRH signal, no direct validation is 
possible. When such approaches are deployed with an objective of signal analysis such as pulse 
10


## Page 11


detection  [38,39],  it  becomes  very  difficult  to  assess  the  validity  of  the  detection  results. 
Nevertheless  such  studies  have  a  clear  methodological  interest  since  they  have  led  to  the 
development of useful statistical tools dedicated to challenging problems in data analysis. Also, the 
use of simulated secretion data, as performed in [40] and [41], can be of great help to assess the 
sensitivity to noisy and subsampled data, and the positive and negative predictive values of the 
detection method.
In contrast, in experimentally-oriented studies, one can take advantage of other sources of data 
retrieved in non-human primates, rodent or ruminant species. These are mainly multi-unit activity 
recordings (MUA, volleys of electrical activity recorded from the median eminence [42]), providing 
an electrophysiological correlate of the GnRH-induced LH pulses, and GnRH levels measured 
directly from the pituitary portal blood with a high time resolution. 
MUA data have motivated the design of stochastic point process models to investigate the temporal 
structure of the HPG activity, which were used for instance in [34] to detect possible memory 
mechanisms in successive LH pulses, as well as a circadian rhythm. 
The seminal work of Keenan et al. [35] has provided a SDE-based description of the male HPG 
incorporating a sophisticated point process for GnRH and LH pulses. 
A Weibull renewal process, with an intensity depending on both GnRH and testosterone, represents 
the GnRH release times, and drives subsequent LH release times, subject to a deterministic 
refractory period and fixed time delay. The pulse shape follows a generalized gamma density. The 
pulse amplitude is derived from the detailed dynamics of the content of exocytosis secretion 
vesicles. These dynamics combine previous accumulation and new synthesis of LH or GnRH, ruled 
by stochastic rates (logistic functions integrating over time the testosterone and/or GnRH regulating 
11


## Page 12


activities, perturbed by an Ornstein-Uhlenbeck process). A continuous mode of synthesis for LH as 
well as for testosterone is also included, which eventually filters the upstream pulsatile signals. The 
comparison of the model outputs with data was later performed in [43] to investigate possible 
systematic changes affecting the dynamics of the GnRH-LH-Te axis in aging men. This SDE-based 
pulse generator has also been taken-up in [44] to represent pulse events in a female HPG model.
In the framework of pulse modulated systems, Churilov et al. have also incorporated the pulsatile 
secretion of GnRH into the ODE model initially proposed in [32], by introducing deterministic 
jump discontinuities as Dirac delta functions for the pulses in [45]. Both the firing times and 
amplitudes of the jumps are modulated by the testosterone level. The detailed mathematical analysis 
of the stability of periodic solutions is challenging; it is based on the design of an equivalent 
discrete time map (between any two GnRH pulses) and the study of its fixed points. 
In the framework of excitable systems, Brown et al. have designed a mathematical neuroscience 
approach to represent in a compact and averaged way the dynamic neuron network underlying the 
GnRH/LH pulse generator [36]. They used the excitation property of a well-known model in 
electrophysiology, the  FitzHugh-Nagumo  (FHN)  model.  In  this  model,  the  input  is  a  point 
stochastic process with varying amplitude and intensity, which generates the GnRH and LH pulses. 
The slow-fast structure of the FHN model was not fully exploited here. In contrast, timescale 
separation was at the source of the design and analysis of a multiple timescale model involving 
coupled  FHN  systems  and  coping  not  only  with  GnRH  pulses,  but  also  with  the  recurrent 
alternation between the pulse and surge regimes [37].  This GnRH pulse and surge generator is also 
able to capture the modulation of pulse frequency along an ovarian cycle and the effects of estradiol 
or progesterone bolus [46], in agreement with the whole corpus of biological knowledge drawn 
from GnRH portal blood data.
12


## Page 13


The objective of the deconvolution analysis is to recover the full secretion signal. Deconvolution-
based methods are somehow close to the former PBPK-like models mentioned in the first part of 
this  section,  in  the  sense that  they  aim to explain  the  encoding of dynamic signals  by the 
combination of a secretion mechanism with a clearance mechanism. The convolution ensues from 
the fact that, at a given time t, hormone molecules secreted at any time s less than t, and still not 
cleared-off by time t, can contribute to the current hormone level. We refer to [40] for an instance of 
non-parametric reconstruction of LH and FSH secretory rates, upon exogenous GnRH stimulation. 
In general, the results of the deconvolution procedure are dependent on the specific hypotheses 
underlying the secretory burst shape and clearance mechanisms, as well as on the statistical method 
and regularization scheme (see [47] for a review and comparison of different deconvolution-based 
methods).
Empirical detection methods have been provided outside the deconvolution framework, with the 
objective to provide one with a reliable sequence of IPIs, hence to detect the pulse peak times only, 
rather than to reconstruct the whole signal. By necessity, they often rely on ad-hoc threshold 
parameters and may generate false-positive and false-negative errors, mainly due to the fact that the 
effective, almost instantaneous, pulse times are almost never observed experimentally, so that the 
selection of the locally highest values as time peaks may be misleading. To circumscribe this pitfall, 
the algorithm proposed in [41] involves a mixture of local, semi-local and global criteria combined 
with basic PBPK notions (LH half-life). Its reliability has been deeply investigated on simulated 
and reference data, and it has been applied in different experimental contexts (see e.g. [48]). The 
field of pulse/peak detection is still very active from the methodological ground (see for instance 
the use of nonlinear diffusion equations reviewed in [49]).
13


## Page 14


The issue of the statistical estimation of signal features becomes even harder when one considers 
several linked data series, such as joint measurement of LH and FSH levels [50]. To decipher the 
inherent multi-hormone interactions gonadotropins are part of, Veldhuis et al. have combined peak 
detection algorithms, deconvolution-based methods and biomathematical modeling to reconstruct 
unobserved signals in a framework called ensemble models [51]. However, methods are still in 
active development, and no gold standard has been achieved yet. For instance, network inference 
and model-free approaches may also be used to unravel hormonal regulations [51,52].
3) Decoding the pituitary gonadotropin signal at the cellular level
Pituitary gonadotropins transmit their signal through GPCR receptors (FSHR and LHCGR [53]) in 
the gonadal cells, to control gametogenesis and steroidogenesis. The binding of gonadotropins to 
their cognate receptors triggers the activation of several intracellular signaling pathways and leads 
to global changes in gene transcription [54-56] and protein translation [57,58]. 
3.1) Interaction network
Signaling cascades activated by the gonadotropins mainly originate from the interaction of their 
receptors with Gαs and β-arrestin proteins. However, the large number of molecules participating in 
these reaction cascades, the numerous interconnections (with feedback) existing between these 
molecules, and the cross-talks between pathways, partly underlie the complexity of signaling 
networks [59].
A first step toward the understanding of the signaling dynamics is based on the notion of interaction 
network (see Figure 2), i.e. a graph summarizing the links (direct or indirect activation, inhibition, 
modulation, complexation, etc) between the molecules involved in the various signaling cascades. 
This graph may be derived from a careful analysis of biological experiments in various cell models. 
14


## Page 15


Several attempts to characterize FSH-induced signaling networks have been made recently, in 
particular in Sertoli cells [17,60,61], in granulosa cells [17] or in cumulus cells [62]. See also [63] 
for a recent curation of the literature on FSH signaling. We are not aware of analogous results for 
LH-induced signaling networks, yet recent experimental works shed light on the different LH-
dependent pathways in granulosa cells [64].
To face  the  complexity  of  interaction  networks,  and  the  always  increasing  volume  of  data, 
especially –omics data, computational tools are needed to gather and integrate information. For 
example, enrichment of -omics data following specific hormone stimulation is possible through the 
confrontation with large pathway databases, such as Ingenuity®  Pathway Analysis or Cytoscape 
[65]. Such an approach has been used in [62] to identify key functions and pathways associated 
with a list of differentially expressed genes after FSH stimulation in bovine cultured cumulus cells. 
Logic-based inference may also complete possible reaction networks by abductive reasoning with 
perturbation experiments (knock-in, knock-out, siRNA etc) and has been applied to the FSH-
induced signaling network in [66].
3.2) Receptors Structures, trafficking and signaling bias
Studies on the gonadotropin receptors biology may also inform on receptor trafficking, cross-talks 
between pathways, or identification of scaffolding or hub molecules [67]. Structural modeling helps 
to gain insights on specific mechanisms such as the activation of the receptor upon ligand binding, 
although the structures of the full-length gonadotropin receptors are currently not available. One 
instance of such an approach is provided by [68], where structure modeling helps to understand the 
different actions of the human luteinizing hormone (hLH) and the human chorionic gonadotropin
(hCG) at their common receptor. Although hLH and hCG occupy the same binding site on the 
extracellular part of the receptor, 3D homology models, based on the known FSH/FSHR structure 
[69], predict that the subsequent interaction with the hinge region of the LHCGR receptor varies 
15


## Page 16


between the two hormones. See also [70] for a review on  LHCGR and its structure-function 
relationships, [67] for a review on FSHR and [71] for recent advances in GnRH receptor structure. 
Structural modeling approaches may also reveal the architecture of molecular complexes involving 
the receptor [72], and predict direct interactions having important consequences within a signaling 
pathway.
Receptor oligomerization (formation of a protein complex that consists of a small number of 
receptors)  also  play  an  important  role  in  the  signaling  networks.  In  particular, homodimers 
(complex made of two receptors of the same type) and heterodimers (complex made of two 
different receptors) have been shown for FSHR and LHCGR [73,74], which adds a new layer of 
complexity. Indeed,  these  different  oligomers  might  induce  different  signaling,  and  may  be 
selectively favored by a given ligand (natural or synthetic hormones, small molecules, etc).  In 
particular, the signaling of these oligomers might be biased relative to each other, that is, the same 
set of signaling pathways is triggered, but with different relative efficacy. Signaling bias is now 
considered as a common feature to many GPCRs, and has profound therapeutic implications 
[75,76]. Recent evidence show that gonadotropin receptor signaling pathways can be biased by 
allosteric modulators or differentially activated in a context-dependent manner, leading to different 
cellular outcomes [77-80] like steroid productions. Functional selectivity also probably occurs at the 
GnRH receptor, which opens the way to interesting pharmacological opportunities [81].
From  the  modeling  viewpoint,  signaling  bias  has  been  revealed  using  classical  equilibrium 
pharmacology models [82]. The so-called operational model is widely used to infer bias from dose-
response data [83]. However, the current availability of  fluorescence (or Förster ) resonance energy 
transfer (FRET, mechanism describing energy transfer between two light-sensitive molecules, a 
donor  and  an  acceptor)  and  bioluminescence  resonance  energy  transfer  (BRET,  using 
bioluminescent luciferase as donor molecules instead of a light-sensitive molecule which has to be 
16


## Page 17


initially  excited  by illumination)  techniques  [84,85], as  well  as  recent  evidence  of  temporal 
signatures of bias signaling [86,87], motivate the use of dynamic modeling techniques to decipher 
the mechanisms underlying functional selectivity.
3.3) Intracellular dynamic modeling
Beyond the large size of the GPCR interaction networks and the numerous possibilities of cross-
talks between signaling pathways, an additional and key layer of complexity comes from the 
dynamic  properties  of  intracellular GPCR  signaling.  In  fact,  different  types  of  stimulations 
(biochemical nature of the ligand, temporal pattern, dose etc) may activate the same molecules but 
at different subcellular locations or with distinct temporal signatures, leading to very different 
cellular responses [88,89]. 
Various modeling approaches have been used to represent GPCR signaling dynamics [90-93]. Once 
an interaction network has been built, a common framework based on ODE is used to dynamically 
represent the activation of signaling pathways. The interaction network is appropriately interpreted 
as  a  biochemical  reaction  network,  and  each  reaction  is  translated  into  infinitesimal 
elimination/production rates for the concentration of its reactant/product, using the law of mass 
action. 
A standard iterative workflow between model construction and experimental data is applied to 
address specific biological questions [94]. Once the dynamic model has been built, extensive 
optimization  algorithms  are  used  to  estimate  unknown  parameters  (kinetic  rates,  initial 
concentration, etc) [95], and dedicated statistical frameworks can be used for model selection [96].
To our  knowledge,  there  are  few  detailed  works  on  the  intracellular modeling  of  pituitary 
gonadotropin intracellular signaling. Clément et al. [97] proposed a model of the dramatic increase 
17


## Page 18


in the efficiency of cAMP response along follicular development. A steady state analysis and 
parameter sensibility have been performed in the case of constant input, and numerical simulations 
were done for time-varying inputs. The dynamic regulation of p70S6 kinase, through both the 
cAMP and mTOR pathways, after either FSH or insulin stimulation, has been compared at two 
different  developmental  stages  in  primary  rat  Sertoli  cells  [98].  This  model  gave  access  to 
experimentally  unavailable  detailed  quantitative  description  on  p70S6  kinase  complex 
phosphorylation mechanisms. At a coarser scale, Quignot and Bois [99] have used a dynamic model 
to simulate steroid synthesis under FSH stimulation and investigated the effects of endocrine 
disruptors on steroidogeneis, using both  in-vitro and  in-vivo experimental data on rat granulosa 
cells. Their model includes the CYP19 aromatase and Hsd17b1 enzyme, whose syntheses are 
known to be regulated by FSH through the cAMP signaling pathway. These enzymes control in turn 
the production of gonadal steroids.
One can expect that this research field will be rapidly growing, as much biological knowledge has 
been gathered recently (see sections above 2.1, and 2.2), and important and challenging open 
questions remain to be tackled from the modeling viewpoint. The temporal encoding of hormonal 
signals,  as  discussed  in  the  first  section  of  this  review, is  a  powerful  information-carrying 
mechanism, since cells may be able to behave as sophisticated decoding sensors [100]. 
Deciphering the impact of the pulsatile nature of the signal, and possible differential effects of the 
pulse frequency (as it is naturally the case for LH), on the downstream intracellular targets [101] is 
a  particularly  relevant issue in this  context.  The study of the  respective contribution  of the 
amplitude, duration and frequency of the signaling events will require the design of specific 
experimental setups, such as microfluidic devices for instance, allowing one to control accurately 
the encoding of the input signal, combined with the development of mathematical methods suited to 
the analysis of non-autonomous dynamical systems [102]. Up to now, the decoding of GnRH pulses 
18


## Page 19


by gonadotrophs has retained much more attention than that of LH pulses by gonadal cells. This is 
probably due to the fact that the pulsatility of GnRH is an absolute prerequisite for its biological 
action. Moreover, the frequency of GnRH pulses differentially controls the expression of the FSH 
and LH beta subunits and the release rates of FSH and LH (see review [103]). An additional interest 
in the framework of this review is that the decoding of GnRH pulses results in the encoding of 
gonadotropin signals. Hence the insight gained from models dedicated to GnRH pulse decoding will 
certainly be beneficial to the understanding of pituitary gonadotropin signaling as a whole. An 
impressive amount of modeling work has been dedicated to GnRH signaling (which falls out of the 
scope of this article, see a comprehensive review in [104]). These approaches raise a generic 
theoretical question: which network motifs are able to decode and discriminate different pulse 
frequency-coded signals and/or to preserve the frequency information downstream in the signaling 
cascades? Some steps forward have been made to answer this question through the careful analysis 
of low-dimensional ODE models corresponding to small network motifs [105,106]. Information 
theory and stochastic modeling have also been used to assess how reliable a signaling pathway can 
be in transmitting information from a given input into a given output [107]. Yet, much work is still 
needed to correctly embed these theoretical results in a realistic signaling network.
4) Conclusion
Many efforts in the study of gonadotropin signals have been put on modeling the fluctuations in 
circulating hormone levels on a day-to-day basis and on the statistical and mathematical analysis of 
the GnRH-driven LH pulse generator. This is mostly due to the wide availability of endocrine time 
series and their interest for clinical investigations. Mathematical modeling has proven to be useful 
and successful in bringing qualitative and quantitative information on hormonal rhythms. These 
approaches are still under active development, and models are being challenged to generate a 
variety of behaviors including relevant pathological situations. Current challenges in this direction 
19


## Page 20


include data fitting and statistical analysis of the measured signals (times series analysis), to supply 
information  as  accurate  as  possible  on  unobservable  variables  in  natural  and  pathological 
conditions. Although the mathematical modeling approaches in reproductive pharmacology is still 
to be much more developed, we believe that these models will be particularly important for 
evaluating the consequences of treatments, either in pathological situations or for medically assisted 
procreation. 
Yet, there will remain limitations in terms of mechanistic interpretation as long as the cellular and 
intracellular scales are not embedded in larger scale approaches. The GPCR community is very 
active currently, and has for instance developed new experimental tools that shed light on key 
mechanisms of GPCR trafficking. It is to be expected that the modeling of pituitary gonadotropin 
signals will benefit from a larger effort of the GPCR modeling community [108]. In turn, this will 
bring decisive tools for drug screening and development of innovative approaches in drug discovery 
for reproductive biology.
5) Expert opinion
In this review, we have illustrated some computational modeling approaches dealing with the 
proper assessment of FSH and LH release from rather  blurred  experimental data,  the 
phenomenological “push-and-pull” like hormone dynamics ensuing from the endocrine dialogs 
between the gonads and pituitary, the detailed description of the molecular pathways triggered 
by FSHR and LHCGR, and some associated structural biology issues. Even if these issues 
have been dealt  partially  from the modeling viewpoint,  there  still remain many open 
questions.
To our opinion, the greatest challenge to be tackled is embedding gonadotropin signaling within 
its natural multi-scale environment, which encompasses the following different scales: the 
cellular level, the cell-to-cell level, and the cell population level.
20


## Page 21


At the cell level, there remain many challenges regarding the intracellular networks downstream 
the gonadotropin receptors. To date, most attention has been put on canonic second messenger 
pathway (such as cAMP), while it is now clearly established that  there  are  several 
distinct  signaling  modules, such as  β-arrestin-induced ones [76].  T h e  s y s t e m a t i c 
a c c o u n t  o f  cross-talks between gonadotropin receptors, with growth-factor and/or steroid 
induced pathways, or even direct conformational effect of steroids, will also be decisive to yield 
more predictive computational models in drug discovery.  An instance of functional interaction of 
great physiological impact is provided by the granulosa cells of terminally developing ovarian 
follicles in which FSHR and LHCGR coexist. FSHR and LHCGR signaling interact in different 
ways in granulosa cells. First the expression of LHCGR in granulosa cells is induced by FSHR 
signaling. Second, once granulosa cells are endowed with both FSHR and LHCGR, FSH and LH 
act in synergy on cAMP and steroid synthesis (see l o w e r  panel of Figure 3). Finally, in those 
cells there might be physical interactions between FSHR and LHCGR, yet such interactions remain 
to be assessed in vivo (there are evidence in in vitro devices [73,74]).
Systems biology approaches, able to aggregate biological knowledge in a single 
framework and predict effect of (physiological or pharmaceutical) alterations of 
these networks,  are going to be key tools in drug discovery in reproduction. 
Concomitantly, methodological improvements will be needed as more involved 
formalisms are required. The spatialization of the signaling modules and actors (nucleus, 
cytoplasmic, scaffolding, endocytosis) has to be taken into account, as  it  can be associated with 
clearly different kinetics, hence different final biological  outcomes [109].  For  instance,  a 
general mechanism yielding persistent cAMP signals triggered by internalized GPCR 
has  been proposed and supported by a reaction-diffusion model [110] . Recently, this 
mechanism has been revealed for the LHCGR in mural granulosa cells by [111], and the authors 
have suggested that it could contribute to transmit signals up to the oocyte and be physiologically 
21


## Page 22


relevant for oocyte meiosis resumption. Spatial modeling approaches will then rapidly develop in 
the need of refined description of the signaling networks.
In addition, stochastic modeling approaches also becomes important. The recent 
study on the GnRH receptor at the single cell level [107] has allowed one to 
understand how negative feedback in the ERK signaling pathway provides an 
optimal information transfer at intermediate feedback levels. It is thus to be 
expected that advances in experimental tools will allow a more general study of 
signaling pathways at the single cell level, and that stochastic modeling will be 
helpful to decipher inherent biological variability and the intrinsic role of cell-
cell response variations.
At the cell-to-cell level, the intercellular communication between cells expressing either LHCGR 
or FSHR is a key mechanism within the HPG axis. 
A typical instance  of coordination  between FSH and LH signaling is the control of 
steroidogenesis in the somatic cells of ovarian follicles. LH-induced signaling in theca cells 
results in the production of androgens that are transferred to granulosa cells. In these latter cells, 
the androgens are converted into estrogens thanks to FSH-induced expression of the aromatase 
enzyme. This process is known as the two-cell two-gonadotropin model [112] (see upper panel 
of Figure 3 ). It has been considered in a phenomenological, coarse-grain manner in [44] [113], 
yet would deserve more dedicated studies, all the more since it can give rise to imbalanced 
steroidogenesis  as encountered  in pathological  situations such as  the Polycystic  Ovarian 
Syndrome  [114]. Again,  spatial  modeling may  also help  here to understand  how  the spatial 
distribution of FSHR and LHCGR within a follicle can affect the signaling processes [115].
22


## Page 23


A  comparable  coordination  between 
FSH and 
LH signaling  exists  in  the 
spermatogenesis process. When stimulated by LH, Leydig cells secrete testosterone, 
which together with FSH stimulate Sertoli cell activity and spermatogenesis [116] . 
However, up to our knowledge, there is no precise mathematical modeling to decipher this 
cell-cell  communication.  Undoubtedly,  theoretical  approaches  will  reveal  nontrivial 
behaviors of this system, and  will permit to shed light on possible alterations of its 
dynamics.
Finally, the ultimate challenge will be to embed gonadotropin-induced decision-making of 
individual  cells into the mechanistic modeling of tissular or organic functions subject to 
systemic whole- body controls (cell population and tissue level). This means connecting fine-grain 
models designed at each level of the HPG. Some steps forward have already been made through 
the design and study of spatio-temporal  multi-scale models for structured cell populations 
[117,118] in the context of ovarian follicle development. The gonadotropin-induced signaling is 
explicitly accounted for by control terms driving both the cell fates locally (proliferation, terminal 
differentiation, cell death)  and the whole cell dynamics  globally. The simulation  and 
mathematical analysis of such models are really tricky and necessitate dedicated mathematical 
and computational developments. Even if the formulations of the control terms a r e  b a s e d 
o n  biochemistry, they remain  very compact. An even more challenging science front,  both 
from the  experimental and  mathematical/computational grounds, consists in coupling the 
detailed dynamics of intracellular signaling networks induced by gonadotropins ,  with the 
dynamics of cell populations underlying physiological functions, which would open the way to 
unheard-of fallouts in systems biology and systems pharmacology.
Acknowledgments. 
23


## Page 24


We are grateful to the anonymous reviewers for their helpful comments. We thank Danielle 
Monniaux for her careful reading of our manuscript and her invaluable inputs.
References
[1]
Butcher EC, Berg EL, Kunkel EJ. Systems biology in drug discovery. Nat. Biotechnol. 2004;22:1253–1259.
[2]
Hood L, Perlmutter RM. The impact of systems approaches on biological problems in drug discovery. Nat. 
Biotechnol. 2004 ;22:1215–1217.
[3]
Materi W, Wishart DS. Computational systems biology in drug discovery and development: methods and 
applications. Drug Discov. Today 2007 ;12: 295–303. 
[4]
Wang Z, Deisboeck TS. Mathematical modeling in cancer drug discovery. Drug Discov. Today 2014 ;19: 145–
150.
[5]
Box GEP. Robustness in the Strategy of Scientific Model Building. In Robustness in Statistics, Launer RL, and 
Wilkinson GN, eds. (Academic Press), pp. 201–236, 1979. 
[6]
Chuang H-Y, Lee E, Liu Y-T, et al. Network‐based classification of breast cancer metastasis. Mol. Syst. Biol. 
2007;3: 140. 
[7]
Chen Y, Zhu J, Lum PY, et al. Variations in DNA elucidate molecular networks that cause disease. Nature 
2008;452: 429–435. 
[8]
Finley SD, Chu L-H, Popel AS. Computational systems biology approaches to anti-angiogenic cancer 
therapeutics. Drug Discov. Today 2015; 20: 187–197. 
[9]
Lloret‐Villas A, Varusai TM, Juty N, et al. The Impact of Mathematical Modeling in Understanding the 
Mechanisms Underlying Neurodegeneration: Evolving Dimensions and Future Directions. CPT Pharmacomet. 
Syst. Pharmacol. 2017 ; 6: 73–86. 
[10]
Kaprara A, Huhtaniemi IT. The hypothalamus-pituitary-gonad axis: Tales of mice and men. Metabolism - Clinical 
and Experimental 2017; In press, doi: 10.1016/j.metabol.2017.11.018.
[11]
Baerwald AR, Adams GP, Pierson RA. Ovarian antral folliculogenesis during the human menstrual cycle: a 
review. Hum. Reprod. Update. 2012; 18:73-91.
[12]
Evans JJ. Modulation of Gonadotropin Levels by Peptides Acting at the Anterior Pituitary Gland. Endocr. Rev 
1999;20:46–67.
[13]
Barbieri RL. The Endocrinology of the Menstrual Cycle. In Human Fertility: Methods and Protocols, Rosenwaks 
Z, Wassarman PM, eds. (Springer New York), pp.145–169, 2014.
[14]
Xia L, Van Vugt D,  Alston EJ, et al. A surge of gonadotropin-releasing hormone accompanies the estradiol-
induced gonadotropin surge in the rhesus monkey. Endocrinology 1992; 131:2812–2820.
[15]
Levine JE, Norman RL, Gliessman PM, et al. In vivo gonadotropin-releasing hormone release and serum 
luteinizing hormone measurements in ovariectomized, estrogen-treated rhesus macaques. Endocrinology 1985; 
177:711-721.
[16]
Christian AC, Moenter SM. The neurobiology of preovulatory and estradiol-induced gonadotropin-releasing 
hormone surges. Endocr Rev. 2010;11:544–577.
[17] Gloaguen P, Crépieux P, Heitzler D, et al. Mapping the Follicle-Stimulating Hormone-Induced Signaling 
Networks. Front. Endocrinol. 2011;2:45.
24


## Page 25


[18] Clarke I, Moore L, Veldhuis J. Intensive direct cavernous sinus sampling identifies high-frequency, nearly 
random patterns of FSH secretion in ovariectomized ewes: combined appraisal by RIA and bioassay. 
Endocrinology. 2002;143:117–129.
** Outstanding experimental study combined with statistical analysis of LH and FSH pulsatility
[19] Clark AR, Kruger JA. Mathematical modeling of the female reproductive system: from oocyte to delivery. Wiley 
Interdiscip. Rev. Syst. Biol. Med. 2017;9:n/a, e1353.
[20] Lamport H. Periodic changes in blood estrogen. Endocrinology. 1940;27:673–680.
[21] Thompson HE, Horgan JD, Delfs E. A simplified mathematical model and simulations of the hypophysis-ovarian 
endocrine control system. Biophys. J. 1969;9:278–291.
[22] Bogumil RJ, Ferin M, Rootenberg J, et al. Mathematical Studies of the Human Menstrual Cycle. I. Formulation 
of a Mathematical Model. J. Clin. Endocrinol. Metab. 1972;35:126–143.
* Detailed description with physiological motivation of a mathematical model of human menstrual cycle,  involving a 
system of thirty-four algebraic-integro-differential equations
[23] Clark LH, Schlosser PM, Selgrade JF. Multiple stable periodic solutions in a model for hormonal control of the 
menstrual cycle. Bull. Math. Biol. 2003;65:157–173.
* Numerical evidence of limit cycles in a compact delay differential equation model of the menstrual cycle. 
[24] Harris LA, Selgrade JF. Modeling endocrine regulation of the menstrual cycle using delay differential equations. 
Math. Biosci. 2014;257:11–22.
[25]
Margolskee A, Selgrade JF. A lifelong model for the female reproductive cycle with an antimüllerian hormone 
treatment to delay menopause. J. Theor. Biol. 2013; 326:21–35.
[26] Boer HMT, Stötzel C, Röblitz S, et al. A simple mathematical model of the bovine estrous cycle: Follicle 
development and endocrine interactions. J. Theor. Biol. 2011;278:20–31.
[27] Schank JC, McClintock MK. A coupled-oscillator model of ovarian-cycle synchrony among female rats. J. Theor. 
Biol. 1992;157:317–362.
[28] Kim J, Hayton WL, Schultz IR. Modeling the brain–pituitary–gonad axis in salmon. Mar. Environ. Res. 
2006;62:S426–S432.
[29] Li Z, Kroll KJ, Jensen KM, et al. A computational model of the hypothalamic - pituitary - gonadal axis in female 
fathead minnows (Pimephales promelas) exposed to 17α-ethynylestradiol and 17β-trenbolone. BMC Syst. Biol. 
2011;5:63.
[30] Goldbeter A. Computational approaches to cellular rhythms. Nature. 2002;420:238–245.
[31] Keener JP, Sneyd J. Mathematical Physiology. Springer-Verlag New York. 1998.
[32] Smith WR. Hypothalamic regulation of pituitary secretion of luteinizing hormone—II feedback control of 
gonadotropin secretion. Bull. Math. Biol. 1980;42:57–78.
[33] Ferasyi TR, Barrett PHR, Blache D et al. Modeling the Male Reproductive Endocrine Axis: Potential Role for a 
Delay Mechanism in the Inhibitory Action of Gonadal Steroids on GnRH Pulse Frequency. Endocrinology. 
2016;157:2080–2092.
[34] Camproux AC, Thalabard JC, Thomas G. Stochastic modeling of the hypothalamic pulse generator activity. Am. 
J. Physiol. 1994;267:E795-800.
25


## Page 26


[35] Keenan D, Veldhuis J, Sun W. A Stochastic Biomathematical Model of the Male Reproductive Hormone System. 
SIAM J. Appl. Math. 2000;61:934–965.
** Detailed description with physiological motivation of a mathematical model of the male reproductive hormone 
system, with rigorous construction of appropriate stochastic point processes to represent pulsatile secretions.
[36] Brown D, Herbison AE, Robinson JE, et al. Modelling the luteinizing hormone-releasing hormone pulse 
generator. Neuroscience. 1994;63:869–879.
[37] Clément F, Françoise J. Mathematical Modeling of the GnRH Pulse and Surge Generator. SIAM J. Appl. Dyn. 
Syst. 2007;6:441–456.
[38] Urban RJ, Johnson ML, Veldhuis JD. In Vivo Biological Validation and Biophysical Modeling of the Sensitivity 
and Positive Accuracy of Endocrine Peak Detection. I. The LH Pulse Signal. Endocrinology. 1989;124:2541–
2547.
[39] Urban RJ, Johnson ML, Veldhuis JD. In Vivo Biological Validation and Biophysical Modeling of the Sensitivity 
and Positive Accuracy of Endocrine Peak Detection. II. The Follicle-Stimulating Hormone Pulse Signal. 
Endocrinology. 1991;128:2008–2014.
[40] De Nicolao G, Liberati D, Veldhuis JD, et al. LH and FSH secretory responses to GnRH in normal individuals: a 
non-parametric deconvolution approach. Eur. J. Endocrinol. 1999;141:246–256.
[41] Vidal A, Zhang Q, Médigue C, et al. DynPeak: An Algorithm for Pulse Detection and Frequency Analysis in 
Hormonal Time Series. PLOS ONE. 2012;7:e39001.
* Efficient pulse detection algorithm (mainly for LH) motivated by biological knowledge and synthetic data.
[42]
Nishihara M, Takeuchi Y, Tanaka T, et al. Electrophysiological correlates of pulsatile and surge gonadotrophin 
secretion. Rev. Reprod. 1999;4:110-116.
[43] Veldhuis JD, Keenan DM, Liu PY, et al. The aging male hypothalamic–pituitary–gonadal axis: Pulsatility and 
feedback. Mol. Cell. Endocrinol. 2009;299:14–22.
[44] Reinecke I, Deuflhard P. A complex mathematical model of the human menstrual cycle. J. Theor. Biol. 
2007;247:303–330.
[45] Churilov A, Medvedev A, Shepeljavyi A. Mathematical model of non-basal testosterone regulation in the male by 
pulse modulated feedback. Automatica. 2009;45:78–85.
[46] Vidal A, Clément F. A Dynamical Model for the Control of the Gonadotrophin-Releasing Hormone 
Neurosecretory System. J. Neuroendocrinol. 2010;22:1251–1266.
[47] Carlson NE, Horton KW, Grunwald GK. A comparison of methods for analyzing time series of pulsatile hormone 
data. Stat. Med. 2013;32:4624–4638.
[48] Czieselsky K, Prescott M, Porteous R, et al. Pulse and Surge Profiles of Luteinizing Hormone Secretion in the 
Mouse. Endocrinology. 2016;157:4794–4802.
[49] Keenan DM, Veldhuis JD. Pulsatility of Hypothalamo-Pituitary Hormones: A Challenge in Quantification. 
Physiology. 2016;31:34–50.
[50] Liu H, Carlson NE, Grunwald GK, et al. Modeling associations between latent event processes governing time 
series of pulsing hormones. Biometrics. 2017; in press, doi: 10.1111/biom.12790.
[51] Veldhuis JD, Keenan DM, Pincus SM. Motivations and Methods for Analyzing Pulsatile Hormone Secretion. 
Endocr. Rev. 2008;29:823–864.
* Nice review on statistical analysis and modelisation of hormone secretion.
26


## Page 27


[52] Vis DJ, Westerhuis JA, Hoefsloot HCJ, et al. Network Identification of Hormonal Regulation. PLOS ONE. 
2014;9:e96284.
[53] Casarini L, Huhtaniemi I, Simoni M, et al. Gonadotrophin Receptors. In: Endocrinology of the Testis and Male 
Reproduction, Simoni M, Huhtaniemi I, eds. (Springer International Publishing) 2016. p. 1–46.
[54] Griffin DK, Ellis PJ, Dunmore B, et al. Transcriptional Profiling of Luteinizing Hormone Receptor-Deficient 
Mice Before and after Testosterone Treatment Provides Insight into the Hormonal Control of Postnatal Testicular 
Development and Leydig Cell Differentiation. Biol. Reprod. 2010;82:1139–1150.
[55] Bonnet A, Lê Cao KA, Sancristobal M, et al. In vivo gene expression in granulosa cells during pig terminal 
follicular development. Reproduction. 2008;136:211–224.
[56] Friedmann S, Dantes A, Amsterdam A. Ovarian transcriptomes as a tool for a global approach of genes modulated 
by gonadotropic hormones in human ovarian granulosa cells. Endocrine. 2005;26:259–265.
[57] Sanz E, Evanoff R, Quintana A, et al. RiboTag Analysis of Actively Translated mRNAs in Sertoli and Leydig 
Cells In Vivo. PLoS ONE. 2013;8:e66179.
[58] Musnier A, Leon K, Morales J, et al. mRNA-Selective Translation Induced by FSH in Primary Sertoli Cells. Mol. 
Endocrinol. 2012;26:669–680.
[59] Roth S, Kholodenko BN, Smit MJ, et al. G Protein-Coupled Receptor Signalling Networks from a Systems 
Perspective. Mol. Pharmacol. 2015;88:604–616.
[60] Lucas TF, Nascimento AR, Pisolato R, et al. Receptors and signaling pathways involved in proliferation and 
differentiation of Sertoli cells. Spermatogenesis. 2014;4:e28138.
[61] Gallay N, Gagniac L, Guillou F, et al. The follicle-stimulating hormone signaling network in Sertoli cells. In: 
Cellular endocrinology in health and disease, Ulloa-Aguirre A, Michael Conn P, eds. (Elsevier). 2014. p. 85–100.
[62] Khan DR, Guillemette C, Sirard MA, et al. Characterization of FSH signalling networks in bovine cumulus cells: 
a perspective on oocyte competence acquisition. MHR Basic Sci. Reprod. Med. 2015;21:688–701.
[63] Telikicherla D, Ambekar A, Palapetta SM, et al. A comprehensive curated resource for follicle stimulating 
hormone signaling. BMC Res. Notes. 2011;4:408.
* Great effort to gather information and knowledge on FSH signaling pathways in a single open-source resource.
[64] Casarini L, Lispi M, Longobardi S, et al. LH and hCG Action on the Same Receptor Results in Quantitatively and 
Qualitatively Different Intracellular Signalling. PLOS ONE. 2012;7:e46682.
[65] Shannon P, Markiel A, Ozier O, et al. Cytoscape: a software environment for integrated models of biomolecular 
interaction networks. Genome Res. 2003;13:2498–2504.
[66] Rougny A, Yamamoto Y, Nabeshima H, et al. Completing signaling networks by abductive reasoning with 
perturbation experiments. In: 25th International Conference on Inductive Logic Programming. 2015. Available 
from: https://hal.archives-ouvertes.fr/hal-01259205.
[67] Ulloa-Aguirre A, Zariñán T, Gutiérrez-Sagal R, et al. Intracellular Trafficking of Gonadotropin Receptors in 
Health and Disease. In: Handbook of Experimental Pharmacology. Springer, Berlin, Heidelberg. 2017. p. 1–39.
[68] Grzesik P, Kreuchwig A, Rutz C, et al. Differences in Signal Activation by LH and hCG are Mediated by the 
LH/CG Receptor’s Extracellular Hinge Region. Front. Endocrinol. 2015;6:140.
[69]
Jiang X, Liu H, Chen X, et al. Structure of follicle-stimulating hormone in complex with the entire ectodomain of 
its receptor. Proc Natl Acad Sci U S A. 2012;109:12491-6.
27


## Page 28


[70] Puett D, Angelova K, da Costa MR, et al. The luteinizing hormone receptor: Insights into structure-function 
relationships and hormone-receptor-mediated changes in gene expression in ovarian cancer cells. Mol. Cell. 
Endocrinol. 2010;329:47–55.
[71] Flanagan CA, Manilall A. Gonadotropin-Releasing Hormone (GnRH) Receptor Structure and GnRH Binding. 
Front. Endocrinol. 2017;8:274.
[72] Bourquard T, Landomiel F, Reiter E, et al. Unraveling the molecular architecture of a G protein-coupled 
receptor/β-arrestin/Erk module complex. Sci. Rep. 2015;5:10760.
[73] Mazurkiewicz J, Barroso M, Herrick-Davis K, et al. Single Molecule Analyses of Fluorescent Protein Tagged 
FSHR Reveals Homodimerization and Specific Heterodimerization with LHCGR. FASEB J. 2015;29:685.14.
[74] Hanyaloglu AC, Fanelli F, Jonas KC. Class A GPCR: Di/Oligomerization of Glycoprotein Hormone Receptors. 
In: G-Protein-Coupled Receptor Dimers, Herrick-Davis K, Milligan G, Di Giovanni G, eds. (Humana Press) 
2017. pp. 207–231.
* Comprehensive review on the role of GPCR oligomerization on cellular signaling.
[75] Behar M, Barken D, Werner SL, et al. The Dynamics of Signaling as a Pharmacological Target. Cell. 
2013;155:448–461.
[76] Reiter E, Ayoub MA, Pellissier LP, et al. β-arrestin signalling and bias in hormone-responsive GPCRs. Mol. Cell. 
Endocrinol. 2017;449:28–41.
[77] Ulloa-Aguirre A, Crépieux P, Poupon A, et al. Novel pathways in gonadotropin receptor signaling and biased 
agonism. Rev. Endocr. Metab. Disord. 2011;12:259–274.
[78] Riccetti L, Yvinec R, Klett D, et al. Human Luteinizing Hormone and Chorionic Gonadotropin Display Biased 
Agonism at the LH and LH/CG Receptors. Sci. Rep. 2017;7:940.
[79] Ayoub MA, Yvinec R, Jégot G, et al. Profiling of FSHR negative allosteric modulators on LH/CGR reveals 
biased antagonism with implications in steroidogenesis. Mol. Cell. Endocrinol. 2016;436:10–22.
[80] Landomiel F, Gallay N, Jégot G, et al. Biased signalling in follicle stimulating hormone action. Mol. Cell. 
Endocrinol. 2013;382:452–459.
[81] A. McArdle C. Gonadotropin-Releasing Hormone Receptor Signaling: Biased and Unbiased. Mini Rev. Med. 
Chem. 2012;12:841–850.
[82] Kenakin T. Theoretical Aspects of GPCR–Ligand Complex Pharmacology. Chem. Rev. 2017;117:4–20.
[83] Rajagopal S, Ahn S, Rominger DH, et al. Quantifying Ligand Bias at Seven-Transmembrane Receptors. Mol. 
Pharmacol. 2011;80:367–377.
[84] Ayoub MA, Landomiel F, Gallay N, et al. Assessing Gonadotropin Receptor Function by Resonance Energy 
Transfer-Based Assays. Front. Endocrinol. 2015;6:130.
[85] Namkung Y, Radresa O, Armando S, et al. Quantifying biased signaling in GPCRs using BRET-based biosensors. 
Methods. 2016;92:5–10.
[86] Lane JR, May LT, Parton RG, et al. A kinetic view of GPCR allostery and biased agonism. Nat. Chem. Biol. 
2017;13:929–937.
* Short review on recent results on kinetic aspect of signaling bias, and discussion on its impact on the observation and 
quantification of bias.
[87] Grundmann M, Kostenis E. Temporal Bias: Time-Encoded Dynamic GPCR Signaling. Trends Pharmacol. Sci. 
2017;38:1110–1124.
28


## Page 29


[88] Lohse MJ, Hofmann KP. Spatial and Temporal Aspects of Signaling by G-Protein-Coupled Receptors. Mol. 
Pharmacol. 2015;88:572–578.
[89] Kholodenko BN, Hancock JF, Kolch W. Signalling ballet in space and time. Nat. Rev. Mol. Cell Biol. 
2010;11:414–426.
[90] Heitzler D, Crépieux P, Poupon A, et al. Towards a systems biology approach of G protein-coupled receptor 
signalling: Challenges and expectations. C. R. Biol. 2009;332:947–957.
[91] Linderman JJ. Modeling of G-protein-coupled Receptor Signaling Pathways. J. Biol. Chem. 2009;284:5427–
5431.
[92] Kholodenko B, Yaffe MB, Kolch W. Computational approaches for analyzing information flow in biological 
networks. Sci. Signal. 2012;5:re1.
[93] Ayoub MA, Yvinec R, Crépieux P, et al. Computational modeling approaches in gonadotropin signaling. 
Theriogenology. 2016;86:22–31.
[94] Yvinec R, Ayoub MA, De Pascali F, et al. Workflow description to dynamically model β-arrestin signaling 
networks. In Press.
[95] Heinemann T, Raue A. Model calibration and uncertainty analysis in signaling networks. Curr. Opin. Biotechnol. 
2016;39:143–149.
[96] Kirk P, Thorne T, Stumpf MP. Model selection in systems and synthetic biology. Curr. Opin. Biotechnol. 
2013;24:767–774.
[97] Clément F, Monniaux D, Stark J, et al. Mathematical model of FSH-induced cAMP production in ovarian 
follicles. Am. J. Physiol. Endocrinol. Metab. 2001;281:E35–E53.
[98] Musnier A, Heitzler D, Boulo T, et al. Developmental regulation of p70 S6 kinase by a G protein-coupled 
receptor dynamically modelized in primary cells. Cell. Mol. Life Sci. 2009;66:3487–3503.
[99] Quignot N, Bois FY. A Computational Model to Predict Rat Ovarian Steroid Secretion from In Vitro Experiments 
with Endocrine Disruptors. PLOS ONE. 2013;8:e53891.
[100] Mandoki JJ, Mendoza-Patiño N, Molina-Guarneros JA, et al. Hormone multifunctionalities: a theory of endocrine 
signaling, command and control. Prog. Biophys. Mol. Biol. 2004;86:353–377.
[101] Bhattacharya I, Gautam M, Sarkar H, et al. Advantages of pulsatile hormone treatment for assessing hormone-
induced gene expression by cultured rat Sertoli cells. Cell Tissue Res. 2017;368:389–396.
* Experimental evidence on the impact of pulsatile input signals in downstream intracellular signaling, in cell culture 
experiments.
[102] Sumit M, Takayama S, Linderman JJ. New insights into mammalian signaling pathways using microfluidic 
pulsatile inputs and mathematical modeling. Integr. Biol. 2017;9:6–21.
[103] Stamatiades GA, Kaiser UB. Gonadotropin regulation by pulsatile GnRH: Signaling and gene expression. Mol. 
Cell. Endocrinol. 2017; In Press. Doi: 10.1016/j.mce.2017.10.015 .
[104] Pratap A, Garner KL, Voliotis M, et al. Mathematical modeling of gonadotropin-releasing hormone signaling. 
Mol. Cell. Endocrinol. 2017;449:42–55.
** Concise review of the important aspect of GnRH pulsatility and of the use of mathematical model to help 
understanding it, with in particular innovative approaches using stochastic modeling and information transfer 
theory.
29


## Page 30


[105] Stern E, Ruf-Zamojski F, Zalepa-King L, et al. Modeling and high-throughput experimental data uncover the 
mechanisms underlying Fshb gene sensitivity to gonadotropin-releasing hormone pulse frequency. J. Biol. Chem. 
2017;292:9815–9829.
[106] Fletcher PA, Clément F, Vidal A, et al. Interpreting Frequency Responses to Dose-Conserved Pulsatile Input 
Signals in Simple Cell Signaling Motifs. PLoS ONE. 2014;9:e95613.
[107] Garner KL, Perrett RM, Voliotis M, et al. Information Transfer in Gonadotropin-releasing Hormone (GnRH) 
Signaling. J. Biol. Chem. 2016;291:2246–2259.
[108] Sokolina K, Kittanakom S, Snider J, et al. Systematic protein–protein interaction mapping for clinically relevant 
human GPCRs. Mol. Syst. Biol. 2017;13:918.
[109] West C, Hanyaloglu AC. Minireview: Spatial Programming of G Protein-Coupled Receptor Activity: Decoding 
Signaling in Health and Disease. Mol. Endocrinol. 2015;29:1095–1106.
[110] Calebiro D, Nikolaev VO, Gagliani MC, et al. Persistent cAMP-Signals Triggered by Internalized G-Protein–
Coupled Receptors. PLoS Biol. 2009;7:e1000172.
** Experimental evidence of the cAMP signaling induced by internalized receptors, and reaction-diffusion model to 
illustrate the consequences of this mechanism in downstream spatio-temporal dynamics.
[111] Lyga S, Volpe S, Werthmann RC, et al. Persistent cAMP Signaling by Internalized LH Receptors in Ovarian 
Follicles. Endocrinology. 2016;157:1613–1621.
[112] Hillier SG, Whitelaw PF, Smyth CD. Follicular oestrogen synthesis: the ‘two-cell, two-gonadotrophin’ model 
revisited. Mol. Cell. Endocrinol. 1994;100:51–54.
[113] Graham EJ, Selgrade JF. A model of ovulatory regulation examining the effects of insulin-mediated testosterone 
production on ovulatory function. J. Theor. Biol. 2017;416:149–160.
[114] Dumesic D, Abbott D. Implications of Polycystic Ovary Syndrome on Oocyte Development. Semin. Reprod. 
Med. 2008;26:53–61.
[115] Iber D, Geyter CD. Computational modelling of bovine ovarian follicle development. BMC Syst. Biol. 
2013;7:60.
[116] O’Shaughnessy PJ, Morris ID, Huhtaniemi I, et al. Role of androgen and gonadotrophins in the development and 
function of the Sertoli cells and Leydig cells: Data from mutant and genetically modified mice. Mol. Cell. 
Endocrinol. 2009;306:2–8.
[117] Clément F, Monniaux D. Multiscale modelling of ovarian follicular selection. Prog. Biophys. Mol. Biol. 
2013;113:398–408.
* Review of innovative approaches based on nonlinear cell population dynamics to decipher the multiscale nature of 
ovarian follicular selection.
[118] Aymard B, Clément F, Monniaux D, Postel M. Cell-Kinetics Based Calibration of a Multiscale Model of 
Structured Cell Populations in Ovarian Follicles. SIAM J. Appl. Math. 2016;76:1471–1491.
30


## Page 31


Figure 1: the hypothalamic-pituitary gonadal (HPG) axis
As  any  neuroendocrine  axis,  the  reproductive  (hypothalamic-pituitary  gonadal)  axis 
involves three anatomic levels : the hypothalamus and pituitary gland on the central side, 
the gonads (ovaries in females, testes in males) on the peripheral side. The gonadotropin-
releasing hormone (GnRH) is secreted by endocrine neurons of the hypothalamus into a 
dedicated portal system, which preserves its encoding as a pulsatile signal up to its target 
cells within the pituitary gland, the gonadotrophs. In response to GnRH pulses, these cells 
are able to release both gonadotropins, the follicle-stimulating hormone (FSH) and the 
luteinizing hormone (LH). FSH and LH are released into the general blood flow and act 
upon the somatic cells of the gonads to sustain both gametogenesis (oocyte and sperm 
maturation) and steroidogenesis (production of steroid hormones such as progesterone, 
testosterone and estradiol). The main source of steroid hormones are Leydig cells in the 
testes, granulosa and theca cells in the ovarian follicles and luteal cells of the corpus 
luteum (the histological remnant of follicles after ovulation) in the ovaries. In turn, 
gonadal steroids affect the production and secretion of both the hypothalamic GnRH and 
gonadotropins, while FSH secretion is further modulated by gonadal inhibin. In addition, 
in females, at each ovarian cycle, the GnRH pattern switches from a pulsatile secretion 
regime to a surge regime resulting in a massive and prolonged increase in GnRH level, 
which triggers the LH ovulatory surge. The inserts represent the change in the estradiol 
and progesterone levels over a whole ovarian cycle, on a day-to-day basis (left side) and 
the changes in testosterone levels on an hour-to-hour basis (right side).
31


## Page 32


Figure 2: Schematic view of the FSHR signaling network
Representation of a model of the FSHR signaling network, gathering various signaling 
levels:  trans-membrane  receptors,  transducer  molecules,  second  messengers,  effector 
molecules and kinases, transcription factors and translation modulators, mRNA and genes. 
Note that only a small subset of FSHR signaling network is shown.  Roughly, four 
(linked) signaling pathways are represented: (i) Activation of calcium channels, mediated 
by either Gq or the adaptor protein, phosphotyrosine interacting with PH domain and 
leucine zipper 1 (APPL1); (ii) p38/ERK/PKA cAMP-dependent pathway; (iii) PI3K/AKT 
Gs-dependent pathway; (iv) mTOR/rpS6 , both Gs and β-arrestin dependent pathways. 
Note that these pathways are neither linear chain nor independent of each other, as 
multiple cross-talks and retroaction loops exist. LHCGR and EGFR are also represented 
at  the  cell  membrane,  to  highlight  possible  cross-talks  and  receptor  trans-activation 
(LHCGR is known to activate Gq, Gi, Gs, β-arrestin and Src pathways; EGFR activates 
PI3K and ERK). Finally, while some information on FSH-dependent gene transcription 
and  protein translation is  available  in the literature,  a  current  open  question  is  the 
understanding of the comprehensive mechanistic link between the signaling pathways and 
gene expression level (thus, we have not represented any arrow here). Note also that the 
protein encoded by the gene AREG interacts with EGFR (thus adding another level of 
complexity in the cross-talks).
32


## Page 33


Figure 3: coordination between FSH and LH signaling
Upper panel : the two-cell two-gonadotropin model
In the ovaries, granulosa cells from ovarian follicles express FSH receptors while theca cells 
express LH receptors. The two cell types function in a coordinated manner, especially as far as 
the synthesis of steroid hormones is concerned. LH-induced signaling in theca cells results in 
the synthesis of testosterone from  progesterone, catalyzed  by the CYP17A1 enzyme. The 
aromatization of testosterone into estradiol by the CYP19A1 enzyme is in turn induced by 
FSH signaling in granulosa cells.
Lower panel : FSH and LH synergic signaling in granulosa cells
Although most of the time granulosa cells are deprived of LH receptors, they can become 
endowed  with both gonadotropin receptors in specific physiological conditions, namely in 
follicles which have been selected for ovulation. In these follicles, LH receptor expression is 
induced  by FSH signaling,  which results in an enhanced cAMP output as well as a more 
efficient production of estradiol. Hence, compared to the other growing follicles, the dominant 
follicle gets the double advantage of becoming less dependent to FSH supply and contributing 
the most to the drop in FSH levels at the end of the follicular phase.
33


## Page 34


List of abbreviations
DDE:  delay differential equations
E2: estradiol
FHN:  FitzHugh-Nagumo
FSH: follicle-stimulating hormone
FSHR: FSH receptors
GnRH: gonadotropin-releasing hormone
GPCR: G protein-coupled receptor
hCG: human chorionic gonadotropin
hLH: human luteinizing hormone
HPG : hypothalamic-pituitary-gonadal
IPI: inter-peak intervals
LH: luteinizing hormone
LHCGR: LH receptors
MUA:  multi-unit activity
ODE: ordinary differential equations
P: progesterone 
PBPK: physiologically-based pharmacokinetic
SDE :stochastic differential equations
Te: testosterone
 
34


## Page 35


The figures are available at http://yvinec.perso.math.cnrs.fr/Publi/RYPCERAPFC_18_advances_gonado_figures.pdf
The supplemental mathematical notes are available at 
http://yvinec.perso.math.cnrs.fr/Publi/RYPCERAPFC_18_advances_gonado_supp.pdf
35

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
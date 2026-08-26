---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.02979v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1904.02979v2_A_stochastic_individual-based_model_to_explore_the_role_of_spatial_interactions_

> Source: 1904.02979v2_A_stochastic_individual-based_model_to_explore_the_role_of_spatial_interactions_.pdf

> Pages: 36

---


## Page 1


A stochastic individual-based model to explore the role
of spatial interactions and antigen recognition in the
immune response against solid tumours
FR Macfarlane∗, MAJ Chaplain, T Lorenzi
School of Mathematics and Statistics, University of St Andrews, St Andrews KY16 9SS,
United Kingdom
Abstract
Spatial interactions between cancer and immune cells, as well as the recog-
nition of tumour antigens by cells of the immune system, play a key role
in the immune response against solid tumours. The existing mathematical
models generally focus only on one of these key aspects. We present here
a spatial stochastic individual-based model that explicitly captures antigen
expression and recognition. In our model, each cancer cell is characterised
by an antigen proﬁle which can change over time due to either epimutations
or mutations. The immune response against the cancer cells is initiated by
the dendritic cells that recognise the tumour antigens and present them to
the cytotoxic T cells. Consequently, T cells become activated against the tu-
mour cells expressing such antigens. Moreover, the diﬀerences in movement
between inactive and active immune cells are explicitly taken into account
by the model. Computational simulations of our model clarify the conditions
for the emergence of tumour clearance, dormancy or escape, and allow us to
assess the impact of antigenic heterogeneity of cancer cells on the eﬃcacy
of immune action. Ultimately, our results highlight the complex interplay
between spatial interactions and adaptive mechanisms that underpins the
immune response against solid tumours, and suggest how this may be ex-
ploited to further develop cancer immunotherapies.
Keywords:
Tumour-Immune Competition, Individual-Based Models,
Spatial Interactions, Antigen Recognition, Antigenic Variations
∗Corresponding author: Email address: frm3@st-andrews.ac.uk
Preprint submitted to Journal of Theoretical Biology
15th July 2019
arXiv:1904.02979v2  [q-bio.CB]  12 Jul 2019


## Page 2


1. Introduction
The immune system is a collection of cells, structures and processes that
work together to remove harmful foreign material from the body. Under-
standing the mechanisms which underpin the cellular immune response to
solid tumours is crucial for the development of new immunotherapy tech-
niques, which can strengthen the natural human immune response to support
the successful treatment of cancer (Couzin-Frankel, 2013; June et al., 2018;
Mellman et al., 2011; Ribas and Wolchok, 2018).
Immune cells, speciﬁcally dendritic cells (DCs) and cytotoxic T lympho-
cytes (CTLs), detect and target solid tumours through recognising and pro-
cessing the small peptides (i.e. the antigens) that are expressed by tumour
cells (Messerschmidt et al., 2016). The antigenic composition of solid tu-
mours can be heterogeneous, whereby each cell within the tumour mass may
have an antigen proﬁle characterised by diﬀerent expression levels of tumour
antigens. On the surface of a tumour cell, antigens are integrated with major
histocompatibility complex (MHC) molecules allowing the DCs to recognise
the antigens and present them to the CTLs. The CTLs then become ac-
tivated and subsequently express the corresponding antigen receptor, which
enables them to interact with the tumour cells expressing that particular
antigen at a suﬃciently high level (Coulie et al., 2014). Further interactions
between CTLs and tumour cells can then trigger tumour cell death.
There are three distinct classes of tumour antigens: tumour associated
antigens (TAAs), tumour speciﬁc antigens (TSAs) and cancer testis antigens
(CTAs). These antigens are expressed, respectively, by: both normal and
cancer cells, cancer cells only, and both cancer cells and human germ-line
cells. Germ-line cells do not contain MHC molecules and, therefore, these
cells cannot present antigens that can be recognised by T cells. This makes
CTAs a viable target for immunotherapy as targeting these antigens implies
a lower risk of autoimmune reactions (Coulie et al., 2014).
One speciﬁc
group of CTAs is represented by the melanoma associated antigen (MAGE)
genes (Boon et al., 2006; Connerotte et al., 2008; M¨uller-Richter et al., 2009;
Urosevic et al., 2005). Within this group, the MAGE-A family consists of el-
even genes that are linked to poor prognosis in various types of cancer (Coulie
et al., 2014; Hartmann et al., 2016; Zajac et al., 2017). In general, the expres-
sion of MAGE-A genes promotes tumour progression by enhancing tumour
2


## Page 3


cell division and reducing apoptosis (Van Tongelen et al., 2017). Some of the
speciﬁc functions of MAGE-A genes have been discovered and include: indu-
cing chemoresistance through a decrease in p53 (Marcar et al., 2010; Monte
et al., 2006; Yang et al., 2007), enhancing tumour proliferation (Costa et al.,
2007) and decreasing the eﬃcacy of anti-tumour drugs (Hartmann et al.,
2013, 2014). The MAGE-A antigens are commonly expressed in melanomas
(Boon et al., 2006; Connerotte et al., 2008; Coulie et al., 2014; Urosevic et al.,
2005), oesophageal cancers (Zajac et al., 2017), lung, breast, prostate and
colorectal carcinomas (Coulie et al., 2014), and head and neck cancers (Hart-
mann et al., 2016; M¨uller-Richter et al., 2009). Therefore, ﬁnding an eﬀective
way of targeting these antigens via immunotherapy may be beneﬁcial to the
treatment of multiple types of cancer (Zajac et al., 2017). For instance, clin-
ical trials have shown that targeting MAGE-A3 can be a successful treatment
option (Chinnasamy et al., 2011; Connerotte et al., 2008).
The antigen expression proﬁles of tumour cells can evolve over time due to
epigenetic and genetic mechanisms. Amongst epigenetic mechanisms, spon-
taneous epimutations are ‘stochastic and heritable changes in gene expression
that leave the sequence of bases in the DNA unaltered’ (Oey and Whitelaw,
2014). Through spontaneous epimutations, the MAGE-A antigen expression
levels of tumour cells can change over time, which may result in variability
between the antigen proﬁles of histological samples from the same patient or
between patients (Urosevic et al., 2005).
One potential cause of spontaneous epimutations is DNA methylation,
whereby methylation of speciﬁc promoter regions of the gene represses tran-
scription. Consequently, if the gene is methylated the corresponding protein
will not be expressed. MAGE genes are methylated in normal cells, but they
can be de-methylated, and thus expressed, in cancer cells (Boon et al., 2006;
Chalitchagorn et al., 2004; Chinnasamy et al., 2011; M¨uller-Richter et al.,
2009; Zajac et al., 2017). Demethylation of these genes can become more
prominent during cancer progression, which suggests that demethylation of
the MAGE genes may support tumour development (Coulie et al., 2014).
Cell-cell interactions involved in the immune response to cancer depend
upon the spatial position of both immune cells and tumour cells within the
tumour micro-environment (Chaplin, 2010; Messerschmidt et al., 2016). In
particular, as a result of tumour growth, cells within the tumour can be-
come more exposed to immune action depending on their location in relation
to other cells of the tumour micro-environment (Hanahan and Weinberg,
2011). Moreover, stochastic antigenic variations can induce further spatial
3


## Page 4


heterogeneity within the tumour (Boon et al., 2006; Yarchoan et al., 2017).
Additionally, the movement of immune cells is dictated by the spatial distri-
bution of tumour antigens within the tumour micro-environment (Boissonnas
et al., 2007).
Mathematical models are a useful tool for simulating and investigating
biological systems, and have been increasingly used to describe tumour an-
tigen expression and tumour-immune interactions. Tumour antigen expres-
sion and the eﬀects of epigenetic and genetic events have been modelled
through diﬀerential equation models (Asatryan and Komarova, 2016; Lorenzi
et al., 2016; Johnston et al., 2007; Tomasetti and Levy, 2010) and cellular-
automaton (CA) models (Bouchnita et al., 2017; Manem et al., 2014). Tra-
ditionally, tumour antigen expression and recognition by the immune system
have been implicitly modelled by tuning the rates of T cell recruitment, T cell
proliferation or tumour cell removal (Arciero et al., 2004; Balea et al., 2014;
Besse et al., 2018; De Boer et al., 1985; de Pillis et al., 2009; K¨ose et al., 2017;
Mallet and de Pillis, 2006). More recently, these processes have been expli-
citly captured by mathematical models formulated in terms of either ordin-
ary diﬀerential equations (Balachandran et al., 2017; d’Onofrio and Ciancio,
2011;  Luksza et al., 2017) or integro-diﬀerential equations (Delitala et al.,
2013; Delitala and Lorenzi, 2013; Kolev et al., 2013; Lorenzi et al., 2015).
However, these models rely on the assumption that cells are well-mixed and,
as such, they do not reﬂect spatial aspects of tumour-immune competition.
On the contrary, the spatial and temporal dynamics of tumour-immune in-
teractions have been described through partial diﬀerential equation (PDE)
models (Al-Tameemi et al., 2012; Matzavinos et al., 2004; Matzavinos and
Chaplain, 2004) and hybrid PDE-CA models (de Pillis et al., 2006; Mallet
and de Pillis, 2006), but these do not take into account the antigen expression
and recognition processes.
In light of these considerations, we present here a spatial individual-based
model of tumour-immune competition that explicitly captures antigen ex-
pression and recognition. In our model, each cancer cell is characterised by
an antigen proﬁle which can change over time due to either epimutations or
mutations. The immune response against the cancer cells is initiated by the
DCs that recognise the tumour antigens and present them to the CTLs. Con-
sequently, T cells become activated against the tumour cells which express
such antigens. Moreover, exploiting the modelling strategies that we have
previously developed (Macfarlane et al., 2018), the diﬀerences in movement
between inactive and active immune cells are explicitly taken into account.
4


## Page 5


Computational simulations of this model clarify the conditions for the emer-
gence of tumour clearance, dormancy or escape, and allow us to assess the
impact of antigenic heterogeneity of cancer cells on the eﬃcacy of immune ac-
tion. Ultimately, our results highlight the complex interplay between spatial
interactions and adaptive mechanisms that underpins the immune response
against solid tumours, and suggest how this may be exploited to further
develop cancer immunotherapies.
The remainder of this work is organised as follows.
In Section 2, we
present the individual-based model and detail how each biological mechanism
is mathematically described. In Section 3, we parametrise the model and
present the results of computational simulations. In Section 4, we discuss
the results obtained and highlight their biological implications along with
potential further applications of this work.
2. The mathematical model
Building upon our previous work (Macfarlane et al., 2018), we consider
three cell types: tumour cells, dendritic cells and cytotoxic T lymphocytes.
We use an on-lattice individual-based approach to describe the interactions
between these three cell types. Our model is posed on a 2D spatial grid of
spacing ∆x in the x direction and ∆y in the y direction, with the constraint
that only one cell of any type is allowed at each grid-site, at any time-step
of duration ∆t.
The system is initially composed of cancer cells and inactive immune cells
only. The immune cells are randomly distributed on the spatial grid, while
the cancer cells are tightly packed in a circular conﬁguration positioned at
the centre of the grid, to reproduce the geometry of a solid tumour. We
let the tumour grow through cell division. A cancer cell divides at rate λ
into two progeny cells of which one occupies the position of the parent cell
while the other is positioned at an unoccupied neighbouring grid-site. This
ensures that only cancer cells with free grid-sites in their neighbourhood can
divide. Inactive immune cells update their position according to a L´evy-like
walk (Harris et al., 2012). This process allows them to move in a randomly
chosen direction for a number of time-steps s sampled from a L´evy distribu-
tion L(s) with exponent 0 ≤α < 2, i.e. L(s) ∼s−(α+1). DCs are activated
at rate DAct upon contact with tumour cells, and CTLs become activated at
rate CAct upon contact with active DCs. Upon activation, DCs and CTLs
switch to Brownian motion, i.e. at each time-step they can move to any
5


## Page 6


of the neighbouring grid sites with the same probability. Moreover, we let
active CTLs remove tumour cells, upon contact, at rate µ. Once activated,
both DCs and CTLs remain active throughout the simulations. For simpli-
city, we omit natural death of tumour cells and proliferation of both DCs and
CTLs (i.e. the total numbers of DCs and CTLs are constant over time). We
refer the reader to our previous paper (Macfarlane et al., 2018) for a detailed
description of these modelling strategies.
In this work, we develop each of these modelling strategies further to
include the antigen proﬁles of cancer cells and their possible variation, the
immune recognition of tumour antigens by DCs, and the targeted activation
of CTLs against speciﬁc tumour antigens. The modelling strategies used to
take into account such additional layers of biological complexity are described
in detail in the following subsections, and are also schematically illustrated
in Figure 1 and Figure 2.
2.1. Mathematical modelling of antigen expression
We denote by NT(t) the number of tumour cells in the system at time
t = h ∆t, with h ∈N0, and we label each cell by an index n = 1, . . . , NT(t).
We incorporate antigen expression into our model by letting each tumour
cell express eleven diﬀerent antigens, to represent the eleven MAGE-A anti-
gens that, as mentioned in Section 1, have a key role in tumour development
(Coulie et al., 2014). These antigens are reported in Table 2 and we label
them by an index i = 1, . . . , 11. There can be high variability in each anti-
gen’s expression between patients with the same type of cancer (Hartmann
et al., 2016; M¨uller-Richter et al., 2009; Urosevic et al., 2005) and even within
cancer cell samples from the same patient (Hartmann et al., 2016; M¨uller-
Richter et al., 2009; Urosevic et al., 2005). Therefore, at each time instant
t, we characterise the antigen proﬁle of the nth tumour cell by means of a
vector
ATn(t) = (A(1)
Tn(t), . . . , A(11)
Tn (t)),
with A(i)
Tn(t) representing the expression level of antigen i. Biologically, there
is evidence that there can be correlation between antigen expression in some
cancers, e.g. epithelial ovarian cancer (Daudi et al., 2014), but not all can-
cers, e.g. hepatocelllular carcinoma (Roch et al., 2010). To consider a more
generalised situation, we assume that the expression levels of each antigen
i can evolve independently from the others. As schematically illustrated in
Figure 1, for each tumour cell n we deﬁne the initial expression of the ith
6


## Page 7


Figure 1: Schematic representation of the mechanisms and processes included
in the individual-based model. We consider three cell types in the model: tumour
cells, DCs and CTLs, along with their corresponding antigen and receptor proﬁles (Key).
a Initially the tumour is composed of tumour cells characterised by diﬀerent antigenic
proﬁles. The standard deviation of the initial tumour antigen proﬁles from the reference
experimental proﬁle is given by the parameter VT . b Tumour cells divide at rate λ. c
Tumour cells may undergo epimutations with probability θE. The standard deviation of
the epimutation altered tumour antigen proﬁles from the previous proﬁles is given by the
parameter VE.
d DCs become activated upon contact with tumour cells at rate DAct.
The standard deviation of the antigen proﬁles recognised by DCs from the tumour antigen
proﬁles is given by the parameter VD. e Upon contact, active DCs present the antigen
proﬁle they have recognised to inactive CTLs.
This leads to the targeted activation of
CTLs against speciﬁc tumour antigens at rate CAct. f Activated CTLs remove tumour
cells, upon contact, at rate µ, on the condition that the tumour cells express a suﬃcient
amount of the antigens corresponding to the CTL receptors. The binding aﬃnity of the
CTLs is measured by the parameter β.
antigen as
A(i)
Tn(0) = (Mi + VT Ri)+,
i = 1, . . . , 11.
(2.1)
In equation (2.1), the parameter Mi denotes a mean expression level of an-
tigen i taken from published experimental data, the values of which are
reported in Table 2. The value of Ri is sampled from a standard normal
7


## Page 8


distribution centred at zero. In equation (2.1) we take the positive part of
the right-hand side to ensure non-negativity of the antigen expression level.
As Ri is taken from a standard normal distribution, the parameter VT rep-
resents the standard deviation of the initial antigen proﬁle from the experi-
mental value Mi (Kenney and Keeping, 1962). Therefore, the parameter VT
determines how close the value of A(i)
Tn(0) will be to the value of Mi.
2.2. Modelling variations in antigen expression
At each time-step, we let the tumour cells divide at rate λ [refer to the
schemes in Figure 1b] and change their antigen proﬁle either through epi-
mutations or through mutations. We assume that epimutations can occur
at any time during the life of a cell [refer to the schemes in Figure 1c and
Figure 2a], whereas mutations take place during cell division and may cause
the antigen proﬁle of one progeny cell to be diﬀerent from that of the parent
cell [refer to the scheme in Figure 2b]. We allow epimutations and mutations
to occur with probabilities θE and θM, respectively. In the absence of changes
in antigen expression (i.e. if θE = 0 and θM = 0), the antigen proﬁles of the
tumour cells will remain constant over time, that is, ATn(t) = ATn(0) for all
t > 0. If antigenic changes do occur through epimutations or mutations, the
antigen proﬁles of tumour cells are updated using the methods described in
the following paragraphs.
Epimutations. A variation in the level of expression of the ith antigen of
the nth tumour cell at the time instant t due to an epimutation is modelled
according to the following equation
A(i)
Tn(t + ∆t) = (A(i)
Tn(t) + VE Ri)+,
i = 1, . . . , 11.
(2.2)
In equation (2.2), the value of Ri is sampled from a normal distribution
centred at zero and we take the positive part of the right-hand side to en-
sure non-negativity of the antigen expression level. Following on from the
deﬁnition of the parameter VT, since Ri is taken from a standard normal
distribution the parameter VE is the standard deviation of the updated anti-
gen proﬁle from the previous expression proﬁle (Kenney and Keeping, 1962).
Therefore, VE determines how close the value of A(i)
Tn(t + ∆t) will be to the
value of A(i)
Tn(t).
8


## Page 9


Figure 2: Schematic comparison of the modelling strategies used to describe
changes in antigen expression induced by epimutations and mutations within
tumour cells. a Antigenic variations due to epimutations can occur, with probability θE,
at any time during the life of a tumour cell. The standard deviation of the new antigen
proﬁle from the previous proﬁle is given by the parameter VE. b Mutations can take place,
with probability θM, only during cell division, which occurs at rate λ. Due to mutations,
one progeny cell may exhibit an antigen proﬁle diﬀerent from that of the parent cell. The
standard deviation between the parent and progeny cell antigen proﬁles is given by the
parameter VM.
Mutations. Upon division at the time instant t, the nth tumour cell is re-
placed by two cells, one labelled by the index n and the other one labelled
by the index NT(t) + 1. If mutations do not occur, the progeny cells in-
herit the antigen proﬁle of the parent cell, i.e. A(i)
Tn(t + ∆t) = A(i)
Tn(t) and
A(i)
T NT (t)+1(t + ∆t) = A(i)
Tn(t). Conversely, if a mutation occurs, the antigen
proﬁle of the progeny cells will be given by the following equations
A(i)
Tn(t + ∆t) = A(i)
Tn(t),
i = 1, . . . , 11
(2.3)
and
A(i)
T NT (t)+1(t + ∆t) = (A(i)
Tn(t) + VM Ri)+,
i = 1, . . . , 11.
(2.4)
Equations (2.3) and (2.4) rely on notation analogous to that of equation (2.2)
and, therefore, VM is the standard deviation of the progeny antigen proﬁles
from the parent antigen proﬁles (Kenney and Keeping, 1962). The value of
VM determines how close the value of A(i)
T NT (t)+1(t + ∆t) will be to the value
of A(i)
Tn(t).
9


## Page 10


2.3. Activation of immune cells
Activation of DCs. We denote by ND the number of DCs, which we assume
to be constant, and we label each DC by an index k = 1, . . . , ND. Activation
of DCs occurs, at rate DAct, through contact with tumour cells. At any time
instant t, the kth DC is characterised by a recognised antigen proﬁle
ADk(t) = (A(1)
Dk(t), . . . , A(11)
Dk (t)).
We let all DCs be initially inactive and thus assume
A(i)
Dk(0) = 0,
i = 1, . . . , 11
for all k = 1, . . . , ND. There is biological evidence supporting heterogeneity
within the antigen presentation process where a less prevalent antigen may
be recognised and presented by the DCs (Boes et al., 2002; Fehres et al.,
2014; Ljunggren et al., 1990). Additionally, it is known that the MAGE-
A genes have similar homology (Roch et al., 2010; Zajac et al., 2017) and,
therefore, there is a potential that they could be mis-recognised as each
other (Graﬀ-Dubois et al., 2002; Linette et al., 2013; Raman et al., 2016;
Schueler-Furman et al., 1998; Tong et al., 2004). As schematically described
by Figure 1d, we consider the case where there may be potential variation
in the antigen recognition process. To capture this idea, upon activation
through contact with the nth tumour cell at the time instant t, we assign the
recognised antigen proﬁle of the kth DC using the following equation
A(i)
Dk(t + ∆t) = (A(i)
Tn(t) + VD Ri)+,
i = 1, . . . , 11.
(2.5)
In equation (2.5), the value of Ri is sampled from a normal distribution
centred at zero and we take the positive part of the right-hand side to ensure
non-negativity of the antigen expression level. We can describe VD as the
standard deviation of the antigen proﬁle recognised by each DC from the
actual tumour antigen proﬁle (Kenney and Keeping, 1962). Therefore, VD
determines how close the value of A(i)
Dk(t + ∆t) will be to the value of A(i)
Tn(t).
Following the method of our previous work (Macfarlane et al., 2018), once
activated, we let the DCs remain activated against their recognised tumour
antigen proﬁle.
Activation of CTLs. We denote by NC the number of CTLs, which we assume
to be constant, and we label each CTL by an index m = 1, . . . , NC. As
10


## Page 11


schematically described by Figure 1e, activation of CTLs occurs, at rate
CAct, through contact with activated DCs. At any time instant t, each CTL
m has a receptor proﬁle
ACm(t) = (A(1)
Cm(t), . . . , A(11)
Cm(t)).
We let all CTLs be initially inactive and thus assume
A(i)
Cm(0) = 0,
i = 1, . . . , 11
for all m = 1, . . . , NC. While DCs can recognise multiple types of antigens,
CTLs can produce copies of one antigen receptor only (Brenner et al., 2008;
Coico and Sunshine, 2015). This means that each CTL can only be activated
against one of the eleven MAGE-A antigens.
To capture this fact, upon
activation through contact with the kth DC at the time instant t, we let the
mth CTL become activated against the highest expressed antigen within the
tumour antigen proﬁle recognised by the kth DC, i.e. we assign the receptor
proﬁle of the mth CTL using the following equation
A(i)
Cm(t) =
(
1 for i = ˆi,
0 for i ̸= ˆi,
with ˆi = arg max
j
A(j)
Dk(t),
(2.6)
where the index ˆi speciﬁes the target antigen of the activated CTL. Note that,
if | arg maxj A(j)
Dk(t)| > 1, then we arbitrarily choose ˆi = min arg maxj A(j)
Dk(t).
Using the same assumptions as in our previous work, once activated, a CTL
remains activated against the same tumour antigen.
2.4. Removal of tumour cells by activated CTLs
Upon contact, each activated CTL can induce death of the tumour cells
which express a suﬃciently high level of the CTL’s target antigen (Coulie
et al., 2014; Stone et al., 2009), which we assume to be given by the mean
antigen expression levels reported in Table 2. In particular, as schematically
described by Figure 1f, when the mth CTL interacts with the nth tumour cell
at time t, we compare the receptor proﬁle ACm(t) with the antigen proﬁle
ATn(t) and let the tumour cell be removed from the system at rate µ provided
that
A(i)
Tn(t) ≥(Mi −β) for i such that A(i)
Cm(t) = 1.
(2.7)
In equation (2.7), the parameter β describes the binding aﬃnity of the CTLs,
which determines the range of tumour cells that each CTL can interact with.
11


## Page 12


Table 1: Model parameters and related values used in computational simulations. Note,
standard deviation has been abbreviated to StD.
Symbol
Description
Value(s)
Reference
∆t
time-step
1 min
(Boissonnas et al., 2007)
∆x,y
grid spacing in the x or y direction
10 µm
(Macfarlane et al., 2018)
NT(0)
initial number of tumour cells
400 cells
(Christophe et al., 2015)
NC
total number of CTLs
400 cells
(Christophe et al., 2015)
ND
total number of DCs
400 cells
(Macfarlane et al., 2018)
n
Index identiﬁer of each tumour cell
n = 1, . . . , NT
-
k
Index identiﬁer of each DC
k = 1, . . . , ND
-
m
Index identiﬁer of each CTL
m = 1, . . . , NC
-
ATn(t)
Antigen proﬁle of tumour cell n at time t
values ≥0
-
ADk(t)
Recognised antigen proﬁle of DC k at time t
values ≥0
-
ACm(t)
Antigen receptor proﬁle of CTL m at time t
values of 0 or 1
-
λ
tumour cell division rate
0.001 min−1
(Christophe et al., 2015)
θ∗
E
Average probability of epimutations
0.23
(De Smet et al., 1996)
µ
removal rate of tumour cells by CTLs
0.03 cells min−1
(Christophe et al., 2015)
DAct
DC activation rate
0.07 cells min−1
(Bianca et al., 2012)
CAct
CTL activation rate
≈0.12 cells min−1
(Engelhardt et al., 2012)
α
L´evy walk exponent
1.15
(Harris et al., 2012)
β
T cell binding aﬃnity
[0, 0.2]
(Schmid et al., 2010)
VT
StD of the initial tumour antigen proﬁles from the reference experimental proﬁle M
[0, 1]
-
VD
StD of the antigen proﬁles recognised by DCs from the tumour antigen proﬁles
[0, 1]
-
VE/M
StD of the tumour antigen proﬁles from the previous proﬁles after epimutations/mutations
same as VT
-
If β is larger, then the CTL can recognise tumour cells with a lower level of
expression of the antigen that they target. Independently of the outcome of
the interaction, the CTL can subsequently interact with further tumour cells
following the same process.
3. Computational simulations
3.1. Model parametrisation and simulation set up
We use a 2D spatial domain with 100 grid sites, of length ∆x = ∆y =
10 µm, both in the x and in the y direction, which correspond to a domain
of size 1 mm2.
Simulations were developed and run in Matlab, for an
appropriate number of time-steps, with one time-step chosen to be ∆t = 1
min, to allow for the resulting dynamics of the system to be investigated. All
quantities in the results we report on in this section were obtained through
averaging the results of 5 simulations.
We refer the interested reader to
Macfarlane et al. (2018) for a detailed description of the parameterisation
of the original model, and we describe here the way in which the additional
components of the model were calibrated using the parameter values reported
in Table 1.
Initial tumour antigen expression levels. Hartmann et al. (2016) investigated
the levels of expression of the eleven MAGE-A antigens in oral squamous cell
cancers of 38 patients. The mean antigen expression levels were taken to
12


## Page 13


Table 2: Average levels of expression of the MAGE-A antigens in oral squamous cell
cancer cell lines. The experimental data were taken from (Hartmann et al., 2016) and
then normalised.
Antigen (i)
Mean Expression, Mi
MAGE-A1 (1)
0.10
MAGE-A2 (2)
0.25
MAGE-A3 (3)
0.41
MAGE-A4 (4)
0.24
MAGE-A5 (5)
0.36
MAGE-A6 (6)
0.35
MAGE-A8 (7)
0.17
MAGE-A9 (8)
0.16
MAGE-A10 (9)
0.38
MAGE-A11 (10)
0.06
MAGE-A12 (11)
0.32
be values between 0-12 arbitrary units as an immune-reactivity score, which
are normalised and reported in Table 2. In our model, the initial expression
level of each antigen for each tumour cell is deﬁned by using equation (2.1)
along with the values of Mi from Table 2. To determine the value of the
product VT Ri in equation (2.1) we consider the properties of Ri, which
is a random value taken from a standard normal distribution. A standard
normal distribution N(0, 1), with mean 0 and standard deviation 1, has a
95% conﬁdence interval of ±1.96 (Kenney and Keeping, 1962). Therefore,
for 95% of values we expect -1.96 ≤Ri ≤1.96 with the majority of the
values being close to the mean value.
We then use the parameter VT to
control the minimum and maximum value of the product VT Ri, i.e. when
VT=1 then VT Ri ∈[−1.96, 1.96], for most values. However, if VT is lower,
e.g. VT=0.1, then the values of the product VT Ri will also be lower, e.g.
VT Ri ∈[−0.196, 0.196]. To consider a wide range of biological situations
corresponding to diﬀerent initial levels of heterogeneity in tumour antigen
proﬁles, we use a range of values, between 0 and 1, for the parameter VT. As
the experimental data in Table 2 are dimensionless, we consider also VT to
be dimensionless.
Probabilities of epimutations and mutations. De Smet et al. (1996) found
that cancer cell lines expressing the MAGE-A1 antigen were 23% more likely
13


## Page 14


to undergo demethylation events than tumour cell lines that did not express
this antigen. Such a value is supported by other studies that consider the
likelihood of DNA demethylation in various cancers (Chalitchagorn et al.,
2004; Ehrlich, 2002). We make the assumption that this holds true for the
other ten MAGE-A antigens, and let the average probability of epimutations
in our model be
θ∗
E = 0.23.
In the model we consider the eﬀect of increase or decreasing the probability
of epimutations or mutations by setting θE and θM, respectively, as multiples
of θ∗
E. The parameters VE and VM control how much the antigen expression
of a tumour cell can change through epimutations or how much the antigen
expression of a progeny tumour cell can change through mutations [refer to
equations (2.2) and (2.3)]. The values of VM and VE are chosen to match the
values of VT. Since the experimental data in Table 2 are dimensionless, we
also consider VE and VM to be dimensionless..
Antigen recognition process:. To consider a wide range of biological situations
corresponding to diﬀerent scenarios in terms of the number of CTLs activated
against each antigen, we use a range of values, between 0 and 1, for the
parameter VD [refer to equation (2.5)]. As the experimental data in Table 2
are dimensionless, we also consider VD to be dimensionless.
T cell binding aﬃnity:. The binding aﬃnity of a T cell is related to the
association rate, that is the inverse of the dissociation rate KD. In general
this value is between 0.005 µM −1 and 1 µM −1 for all natural T cells (Davis
et al., 1998; Slansky and Jordan, 2010). Furthermore, the MAGE-A T cell
receptors association rates have been found to be even larger than this range,
e.g. for MAGE-A3 the values are between 0.018 µM −1 and 5.917 µM −1 (Tan
et al., 2015). However, Schmid et al. (2010) have shown that an association
rate of 0.2 µM −1 or higher did not improve the binding aﬃnity and, therefore,
higher binding aﬃnities may have a limited eﬀect. We take Mi to be the
minimal binding and allow the likelihood of binding to increase depending on
β. In line with experimental evidence, we investigate a range of dimensionless
values between 0 and 0.2 for the parameter β that models the T cell receptor
binding aﬃnity [refer to equation (2.7)].
3.2. Main Results
14


## Page 15


Figure 3:
Variability in the initial tumour antigen proﬁles determines the
eﬀectiveness of the immune response. Plots displaying the number of tumour cells
remaining after 1000 time-steps for increasing values of the parameter VT : a VT = 0.001,
b VT = 0.01 and c VT = 0.1. For each value of VT a range of values of the parameter
VD are tested. The tumour cell numbers presented have been obtained as the average over
5 simulations and the error bars display the related standard deviation. Here, β = 0.01,
θE = θM = 0, and all the other parameter values are reported in Table 1.
15


## Page 16


Variability in the initial tumour antigen proﬁles determines the eﬀectiveness
of the immune response. To investigate how the immune response is aﬀected
by variability in the initial tumour antigen proﬁles, we test for three increas-
ing values of the parameter VT (i.e. VT = 0.001, VT = 0.01 and VT = 0.1).
We choose β = 0.01 and we let the antigen proﬁles of the tumour cells re-
main constant over time (i.e. we choose θE = θM = 0). For each value of VT
considered, we also explore the eﬀect of increasing the value of the parameter
VD. In all cases, we carry out numerical simulations for 1000 time-steps. As
shown by Figure 3a, for a low value of VT, very few tumour cells remain in
the system after 1000 time-steps for all considered values of VD. Conversely,
the results presented in Figure 3c show that if we set a relatively large value
for VT, there is a signiﬁcant number of remaining tumour cells after 1000
time-steps for all values of VD. Moreover, as shown by Figure 3b, for an in-
termediate value of VT, there appears to be a correlation between the number
of tumour cells remaining after 1000 time-steps and the parameter VD. In
particular, larger values of the parameter VD correspond to smaller numbers
of the remaining tumour cells after 1000 time-steps. These results suggest
that for tumours characterised by intermediate levels of initial antigenic het-
erogeneity between tumour cells, higher deviation between the antigen proﬁle
recognised by DCs and the actual antigen proﬁle of tumour cells may res-
ult in a more eﬀective immune response. This is further illustrated by the
computational results presented in the next paragraph.
Increasing variations between the antigen proﬁle recognised by DCs and the
actual antigen proﬁle of tumour cells can result in immune escape, chronic
dormancy or immune clearance of the tumour. The results discussed in the
previous paragraph illustrate how diﬀerent cell dynamics can be observed
for increasing values of the parameter VD.
We test this further by using
the parameter setting of Figure 3b (i.e. VT = 0.01, θE = 0 and β = 0.01)
and comparing the dynamics obtained for three diﬀerent values of VD (i.e.
VD = 0.001, VD = 0.05 and VD = 0.1). In Figure 4, we compare the average
antigen proﬁle of the tumour cells at the end of simulations with the average
antigen proﬁle recognised by the DCs, and we show the corresponding time
evolution of the number of tumour cells. The insets also display the spatial
cell distributions observed at the end of simulations to allow for a clearer un-
derstanding of the resulting dynamics. We observe that VD is a bifurcation
parameter whereby three distinct situations result from choosing increasing
values of VD. In particular, Figures 4a,d refer to the case where the value of
16


## Page 17


Figure 4: Increasing VD can result in immune escape or chronic dormancy or
immune clearance of the tumour. Plots in panels
a-c display the average antigen
proﬁle of tumour cells and the average antigen proﬁle recognised by the DCs at the end
of simulations. The error lines represent the standard deviation between 5 runs of the
simulations. Plots in panels d-f display the time evolution of the tumour cell number with
an example of the observed cell spatial distributions at the ﬁnal time-step shown in the
insets. Three values for the parameter VD are tested: a,d VD = 0.001, b,e VD = 0.05 and
c,f VD = 0.1. Here, VT = 0.01, β = 0.01, θE = θM = 0, and all the other parameter
values are reported in Table 1.
17


## Page 18


VD is relatively low (i.e. VD = 0.001), and show that there is very little diﬀer-
ence between the average antigen proﬁle of the tumour cells and the average
recognised antigen proﬁle at the end of simulations. Moreover, after an initial
decrease, the tumour cell number increases steadily over time resulting in a
relatively large ﬁnal number of tumour cells. Furthermore, Figures 4b,e refer
to the case where an intermediate value of VD is considered (i.e. VD = 0.05),
and show that there a is larger variation between the average antigen proﬁle
of the tumour cells and the average recognised antigen proﬁle at the end of
simulations. Additionally, after a steep decrease, the tumour cell number
remains at a low, almost constant, level for the remainder of the simulation
time interval. Finally, Figures 4c,f refer to the case where the value of VD
is relatively large (i.e. VD = 0.1), and show that the diﬀerence between the
average antigen proﬁle of the tumour cells. Moreover, the average recognised
antigen proﬁle at the end of simulations is even more varied than in the pre-
vious cases and the number of tumour cells decreases steadily over time until
eventually the tumour is completely removed.
Increasing the T cell receptor binding aﬃnity can beneﬁt the immune system
response to cancer. To explore the eﬀect of altering the T cell receptor bind-
ing aﬃnity, we test for three increasing values of the parameter β (i.e. β = 0,
β = 0.0001 and β = 0.001). We choose VT = 0.0001 and we let the tumour
cell antigen proﬁles remain constant over time (i.e. we choose θE = θM = 0).
For each value of β considered, we also explore the eﬀect of increasing the
value of the parameter VD. In all cases, we carry out numerical simulations
for 1000 time-steps. As shown by Figure 5a, for β = 0, a considerable num-
ber of tumour cells remain inside the system at the end of simulations for all
values of VD. Conversely, the results presented in Figure 5c show that when
β is suﬃciently high, very few tumour cells remain in the system after 1000
time-steps for all values of VD. Moreover, as shown by Figure 5b, for inter-
mediate values of β, there appears to be a correlation between the number of
tumour cells remaining after 1000 time-steps and the parameter VD. In par-
ticular, larger values of the parameter VD correspond to smaller numbers of
the remaining tumour cells after 1000 time-steps. These results suggest that
the T cell receptor binding aﬃnity plays a key role in the immune response
to tumour cells. In the same way as Figure 4, Figure 6 shows that, under
the parameter choice of the computational simulations related to Figure 5b,
increasing the value of the parameter VD leads to immune escape or chronic
dormancy or immune clearance of the tumour.
18


## Page 19


Figure 5: Increasing the T cell receptor binding aﬃnity can beneﬁt the immune
system response to cancer. Plots displaying the number of tumour cells remaining after
1000 time-steps for increasing values of the parameter β: a β = 0, b β = 0.0001 and c
β = 0.001. For each value of β a range of values of the parameter VD are tested. The
tumour cell numbers presented have been obtained as the average over 5 simulations and
the error bars display the related standard deviation. Here, VT = 0.0001, θE = θM = 0,
and all the other parameter values are reported in Table 1.
19


## Page 20


Figure 6: For multiple parameter settings, increasing VD can result in immune
escape or chronic dormancy or immune clearance of the tumour. Plots in panels
a-c display the average antigen proﬁle of tumour cells and the average antigen proﬁle
recognised by the DCs at the end of simulations. The error lines represent the standard
deviation between 5 runs of the simulations. Plots in panels d-f display the time evolution
of the tumour cell number with an example of the observed cell spatial distributions at
the ﬁnal time-step shown in the insets. Three values for the parameter VD are tested:
a,d VD = 0.001, b,e VD = 0.05 and c,f VD = 0.1. Here, VT = 0.0001, β = 0.0001,
θE = θM = 0, and all the other parameter values are reported in Table 1.
20


## Page 21


Figure 7: Increasing the probability of epimutations can lead to variations in
the immune response to tumour cells. Panels a and b display the time evolution
of the tumour cell number for increasing values of θE (cf. the legend below the panels).
For the numerical results reported in Panel a all the other parameter values are as for
Figures 4a,d and VE = 0.01, while for the numerical results reported in Panel b all the
other parameter values are as for Figures 6c,f and VE = 0.0001.
Increasing the probability of epimutations can lead to variations in the im-
mune response to tumour cells. So far, we have considered only the situation
where the antigen proﬁle of each tumour cell remains constant over time
(i.e. the probability with which epimutations and mutations leading to an-
tigenic variations occur are θE = 0 and θM = 0). To investigate the eﬀect
of epimutations on the success of the immune response against tumour cells,
we consider the parameter setting that we have used in the computational
simulations shown either in Figures 4a,d or in Figures 6c,f but now we allow
the antigen proﬁles of tumour cells to change through epimutations (i.e. we
choose θE > 0). We consider eight distinct values of θE deﬁned as fractions
or multiples of the average probability of epimutations θ∗
E, given in Table 1.
The range we consider, 0 ≤θE ≤0.92, is chosen to include the range of
De Smet et al. (1996), 012 ≤θE ≤0.45. In all cases, we carry out numer-
ical simulations for 8640 time-steps and we report on tumour cell numbers
obtained as the average over 5 simulations. Figure 7a displays the time evol-
ution of the tumour cell number for the parameter setting of Figures 4a,d.
These results show that increasing values of θE correspond to decreasing
numbers of tumour cells inside the system at the end of simulations. In sum-
mary, by increasing the probability of epimutations the dynamics of tumour
21


## Page 22


cells change from immune escape, through to chronic dormancy to immune
clearance. On the other hand, Figure 7b displays the time evolution of the
tumour cell number for the parameter setting of Figures 6c,f. These results
show that for suﬃciently small values of θE there are no tumour cells left
inside the system at the end of simulations, whereas for larger values of θE a
small number of tumour cells persist at the ﬁnal time-step. Generally, by in-
creasing the probability of epimutations the dynamics of tumour cells change
from immune clearance to chronic dormancy.
Mutations have a weaker impact on the immune response to tumour cells
compared to epimutations. We now compare the impact of mutations and
epimutations on the immune response to tumour cells. Following what we
have done in the previous paragraph, we consider the parameter setting used
in the computational simulations shown either in Figures 4a,d or in Fig-
ures 6c,f but now we allow the antigen proﬁles of tumour cells to change
through mutations (i.e.
we choose θM > 0).
We consider eight distinct
values of θM deﬁned as fractions or multiples of the average probability of
epimutations θ∗
E, given in Table 1. In all cases, we carry out numerical sim-
ulations for 8640 time-steps and we report on tumour cell numbers obtained
as the average over 5 simulations. Figure 8a displays the time evolution of
the tumour cell number for the parameter setting of Figures 4a,d and shows
that immune escape occurs for all values of θM considered. On the other
hand, Figure 8b displays the time evolution of the tumour cell number for
the parameter setting of Figures 6c,f and shows that immune clearance oc-
curs for all values of θM considered.
Comparing these results with those
displayed in Figure 7a and Figure 7b, respectively, we reach the conclusion
that mutations have a weaker impact on the immune response to tumour
cells compared to epimutations.
4. Discussion and conclusions
Spatial interactions between cancer and immune cells, as well as the re-
cognition of tumour antigens by cells of the immune system, play a key role
in the immune response against solid tumours. The existing mathematical
models generally focus only on one of these key aspects. We have presented
here a spatially explicit stochastic individual-based model that incorporates
the adaptive processes driving tumour antigen recognition. Our model takes
22


## Page 23


Figure 8: Mutations have a weaker impact on the immune response to tumour
cells compared to epimutations. Panels a and b display the time evolution of the
tumour cell number for increasing values of θM (cf. the legend below the panels). Here
θ∗
M = θ∗
E. For the numerical results reported in Panel a all the other parameter values are
as for Figures 4a,d and VM = 0.01, while for the numerical results reported in Panel b all
the other parameter values are as for Figures 6c,f and VM = 0.0001.
explicitly into account the dynamical heterogeneity of tumour antigen ex-
pression, and eﬀectively captures the way in which this aﬀects the immune
response against the tumour.
Our computational simulation results show that the initial antigen expres-
sion proﬁles of cancer cells within the tumour have a crucial impact upon
the outcome of the immune response [refer to Figure 3]. In the situation of
an almost homogeneous tumour (i.e. where all tumour cells have a similar
antigen proﬁle), immune clearance occurs. Conversely, when the antigenic
composition between cancer cells is highly heterogeneous the tumour may
be able to escape the immune system response and continue growing. In-
terestingly, for moderate levels of initial antigenic heterogeneity our results
demonstrate that the fate of the tumour is determined by the speciﬁcity of
the cellular immune response.
The computational outcomes of our model indicate that the parameter
controlling the speciﬁcity of the antigen recognition process of the dendritic
cells (i.e. the parameter VD) ultimately dictates which receptors are produced
by the cytotoxic T lymphocytes [refer to Figures 3 and 4]. A larger value
of this parameter brings about a more diverse receptor repertoire of the
CTLs, and in turn results in a better immune response. This suggests that
23


## Page 24


it is advantageous for the T cell pool to be multi-speciﬁc, whereby several
diﬀerent antigen receptors are simultaneously expressed by the CTL pool.
In this respect, the outcomes of our model recapitulate the conclusions of
experimental papers showing the success of a more diverse T cell repertoire
in response to cancer (Carreno et al., 2015; Gerdemann et al., 2011; Ott
et al., 2017; Sahin et al., 2017; Schumacher and Hacohen, 2016; Sharma and
Allison, 2015). We remark that new experimental techniques have recently
been developed to alter the speciﬁcity of T cell receptors (Smith et al., 2014).
One particular approach is to use gene editing, in vitro, to modify which
antigen the T cell receptors will respond to (Albers et al., 2019).
Moreover, our numerical results support the idea that varying the spe-
ciﬁcity of the immune response can result in three distinct scenarios, from
immune escape, through to chronic dormancy to immune clearance of the
tumour [refer to Figures 4 and 6].
The importance of tumour dormancy
controlled by the immune system (i.e. immunological dormancy) has been
highlighted by previous experimental and theoretical work (Kuznetsov et al.,
1994; Lorenzi et al., 2015; Matzavinos et al., 2004; Wu et al., 2018). In par-
ticular, immunological dormancy can explain situations where there is an
extended period of time before the occurrence of tumour relapse (Aguirre-
Ghiso, 2007; Gomis and Gawrzak, 2017; Manjili, 2018; Teng et al., 2008;
Wang and Lin, 2013; Yeh and Ramaswamy, 2015). In this regard, our model
suggests the existence of a possible relationship between the speciﬁcity of the
immune response and the emergence of prolonged immunological dormancy.
We have also explored the way in which altering the binding aﬃnity of
the CTLs to their corresponding tumour antigen may change the immune
response to the tumour. Our results indicate that a stronger binding aﬃnity
leads to a more eﬀective immune response, as the CTLs have a wider range
of tumour cells that they can interact with [refer to Figure 5]. Previously,
Gerdemann et al. (2011) found experimentally that a strong T cell binding
aﬃnity to tumour antigens played a key role in the overall immune response
to the disease. Integrating the outcomes of our model and such experimental
ﬁndings suggests that enhancing the binding aﬃnity of T cells – e.g. through
the modiﬁcation of the receptors that the T cells of a patient can produce –
could be a potential target of adoptive T cell therapy.
The results from our computational simulations suggest that changes in
the antigenic expression of tumour cells due to epimutations can be either
beneﬁcial or detrimental to the immune response to a solid tumour [refer
to Figure 7]. In more detail, we have found that in some cases increasing
24


## Page 25


the probability of epimutations could transform situations of immune escape
into tumour dormancy and eventually tumour removal. These ﬁndings are
interesting in light of cancer therapy as they suggest that the eﬃcacy of
the immune response against solid tumours could be enhanced by increasing
the probability of epimutations. In this respect, the loss of DNA methylation
was the ﬁrst epimutation to be identiﬁed in cancer cells (Feinberg and Tycko,
2004) and several experimental and clinical works found that the expression
of MAGE antigens could be increased through demethylation (Chinnasamy
et al., 2011; Gerdemann et al., 2011; Graﬀ-Dubois et al., 2002; Wischnewski
et al., 2006). Taken together, the outcomes of our model suggest that by
combining a T cell therapy targeting multiple MAGE genes – e.g.
using
approaches similar to those of Gerdemann et al. (2011) – and increasing
the probability of epimutations through demethylating agents – e.g. using
methods similar to those of Chinnasamy et al. (2011) and Wischnewski et al.
(2006) – a stronger immune response could be induced. However, in other
cases, we have observed that increasing the probability of epimutations can
turn instances of tumour removal into scenarios whereby a small number of
tumour cells persisted over time. These contrasting results were also sugges-
ted previously through experimental research, where epimutations could be
either beneﬁcial or detrimental to tumour development (Chen and Mellman,
2017; Yarchoan et al., 2017).
We have additionally studied the eﬀect of variations in the antigenic ex-
pression of tumour cells caused by mutations. In all parameter settings we
have considered, increasing the probability of mutations did not change the
resulting dynamics of the tumour-immune response [refer to Figure 8]. This
suggests that mutations have a weaker eﬀect on tumour-immune competition
than antigenic variations caused by epimutations. This ﬁnding is coherent
with experimental observations indicating that epimutations generally oc-
cur more frequently than mutations in tumour development (Feinberg, 2004;
Peltom¨aki, 2012). Hence, our results demonstrate the importance of under-
standing the underlying causes of antigenic variations in tumour cells when
considering tumour-immune competition.
Looking to the future, our individual-based model could be developed
further in several ways. We could incorporate extended aspects of the tu-
mour micro-environment, such as, proliferation of the immune cells and the
interaction of tumour cells with abiotic factors (e.g. oxygen and glucose) that
can aﬀect the phenotypic composition of the tumour. Moreover, by posing
the model on a 3D domain, further understanding could be obtained regard-
25


## Page 26


ing the spatial dynamics of the tumour-immune response. The ﬂexibility of
our model would also allow for the inclusion of a wider range of antigens.
Finally, although useful for investigating the qualitative and quantitative
dynamics of a biological system, individual-based models like ours are not
amenable to mathematical analysis. In a variety of contexts the beneﬁt of
relating stochastic individual-based models to deterministic continuum mod-
els has been highlighted (Champagnat et al., 2006; Chisholm et al., 2016,
2015; Deroulers et al., 2009; Painter and Hillen, 2015; Penington et al., 2011;
Stevens, 2000). Combining such modelling approaches makes it possible to
integrate computational simulations with analytical results, thus enabling a
more extensive exploration of the model parameter space. This is a line of
research that we will be pursuing in the near future by exploiting the formal
methods that we have recently presented (Chaplain et al., 2018; Stace et al.,
2019).
Acknowledgments
FRM is funded by the Engineering and Physical Sciences Research Coun-
cil (EPSRC).
Bibliography
References
Aguirre-Ghiso, J.A., 2007.
Models, mechanisms and clinical evidence for
cancer dormancy. Nat Rev Cancer 7, 834–846.
Al-Tameemi, M., Chaplain, M.A.J., d’Onofrio, A., 2012. Evasion of tumours
from the control of the immune system: Consequences of brief encounters.
Biol Direct 7, 31.
Albers, J.J., Ammon, T., Gosmann, D., Audehm, S., Thoene, S., Winter,
C., Secci, R., Wolf, A., Stelzl, A., Steiger, K., et al., 2019. Gene editing
enables T-cell engineering to redirect antigen speciﬁcity for potent tumor
rejection. Life Sci Alliance 2, e201900367.
Arciero, J.C., Jackson, T.L., Kirschner, D.E., 2004. A mathematical model
of tumor-immune evasion and siRNA treatment. Discrete Contin Dyn Syst
Ser B 4, 39–58.
26


## Page 27


Asatryan, A.D., Komarova, N.L., 2016. Evolution of genetic instability in
heterogeneous tumors. J Theor Biol 396, 1–12.
Balachandran, V.P.,  Luksza, M., Zhao, J.N., Makarov, V., Moral, J.A., Re-
mark, R., et al., 2017.
Identiﬁcation of unique neoantigen qualities in
long-term survivors of pancreatic cancer. Nature 551, 512–516.
Balea, S., Halanay, A., Jardan, D., Neamt¸u, M., Safta, C., 2014. Stabil-
ity analysis of a feedback model for the action of the immune system in
leukemia. Math Model Nat Phenom 9, 108–132.
Besse, A., Clapp, G.D., Bernard, S., Nicolini, F.E., Levy, D., Lepoutre, T.,
2018. Stability analysis of a model of interaction between the immune
system and cancer cells in chronic myelogenous leukemia. Bull Math Biol
80, 1084–1110.
Bianca, C., Chiacchio, F., Pappalardo, F., Pennisi, M., 2012. Mathemat-
ical modeling of the immune system recognition to mammary carcinoma
antigen. BMC Bioinformatics 13, S21.
Boes, M., Cerny, J., Massol, R., den Brouw, M.O.P., Kirchhausen, T., Chen,
J., Ploegh, H.L., 2002. T-cell engagement of dendritic cells rapidly re-
arranges MHC class II transport. Nature 418, 983.
Boissonnas, A., Fetler, L., Zeelenberg, I.S., Hugues, S., Amigorena, S., 2007.
In vivo imaging of cytotoxic T cell inﬁltration and elimination of a solid
tumor. J Exp Med 204, 345–356.
Boon, T., Coulie, P.G., Van den Eynde, B.J., van der Bruggen, P., 2006.
Human T cell responses against melanoma. Annu Rev Immunol 24, 175–
208.
Bouchnita, A., Belmaati, F.E., Aboulaich, R., Koury, M.J., Volpert, V.,
2017. A hybrid computation model to describe the progression of multiple
myeloma and its intra-clonal heterogeneity. Computation 5, 16.
Brenner, D., Krammer, P.H., Arnold, R., 2008. Concepts of activated T cell
death. Crit Rev Oncol Hematol 66, 52–64.
Carreno, B.M., Magrini, V., Becker-Hapak, M., Kaabinejadian, S., Hundal,
J., Petti, A.A., Ly, A., Lie, W.R., Hildebrand, W.H., Mardis, E.R., et al.,
27


## Page 28


2015. A dendritic cell vaccine increases the breadth and diversity of melan-
oma neoantigen-speciﬁc T cells. Science 348, 803–808.
Chalitchagorn, K., Shuangshoti, S., Hourpai, N., Kongruttanachok, N.,
Tangkijvanich, P., Thong-ngam, D., Voravud, N., Sriuranpong, V., Mutir-
angura, A., 2004. Distinctive pattern of LINE-1 methylation level in nor-
mal tissues and the association with carcinogenesis. Oncogene 23, 8841.
Champagnat, N., Ferri`ere, R., M´el´eard, S., 2006. Unifying evolutionary dy-
namics: from individual stochastic processes to macroscopic models. Theor
Pop Biol 69, 297–321.
Chaplain, M.A., Lorenzi, T., Macfarlane, F.R., 2018.
Bridging the gap
between individual-based and continuum models of growing cell popula-
tions. arXiv preprint arXiv:1812.05872 .
Chaplin, D.D., 2010.
Overview of the immune response.
J Allergy Clin
Immunol 2, S3–S23.
Chen, D.S., Mellman, I., 2017. Elements of cancer immunity and the cancer-
immune set point. Nature 541, 321–330.
Chinnasamy, N., Wargo, J.A., Yu, Z., Rao, M., Frankel, T.L., Riley, J.P.,
Hong, J.J., Parkhurst, M.R., Feldman, S.A., Schrump, D.S., et al., 2011.
A TCR targeting the HLA-A∗0201–restricted epitope of MAGE-A3 re-
cognizes multiple epitopes of the MAGE-A antigen superfamily in several
types of cancer. J Immunol 186, 685–696.
Chisholm, R.H., Lorenzi, T., Desvillettes, L., Hughes, B.D., 2016. Evolution-
ary dynamics of phenotype-structured populations: From individual-level
mechanisms to population-level consequences. Z Angew Math Phys 67,
100.
Chisholm, R.H., Lorenzi, T., Lorz, A., Larsen, A.K., Almeida, L., Escargueil,
A., Clairambault, J., 2015. Emergence of drug tolerance in cancer cell
populations: An evolutionary outcome of selection, non-genetic instability
and stress-induced adaptation. Cancer Res 75, 930–939.
Christophe, C., M¨uller, S., Rodrigues, M., Petit, A.E., Cattiaux, P., Dupr´e,
L., Gadat, S., Valitutti, S., 2015. A biased competition theory of cytotoxic
T lymphocyte interaction with tumor nodules. PloS One 10, e0120053.
28


## Page 29


Coico, R., Sunshine, G., 2015. Overview of the immune system, in: Im-
munology: A short course 7th Edition. John Wiley & Sons. chapter 1, pp.
1–11.
Connerotte, T., Van Pel, A., Godelaine, D., Tartour, E., Schuler-Thurner,
B., Lucas, S., Thielemans, K., Schuler, G., Coulie, P.G., 2008. Functions
of anti-MAGE T-cells induced in melanoma patients under diﬀerent vac-
cination modalities. Cancer Res 68, 3931–3940.
Costa, F.F., Le Blanc, K., Brodin, B., 2007. Concise review: Cancer/testis
antigens, stem cells, and cancer. Stem Cells 25, 707–711.
Coulie, P.G., Van den Eynde, B.J., Van Der Bruggen, P., Boon, T., 2014.
Tumour antigens recognized by T lymphocytes: At the core of cancer
immunotherapy. Nat Rev Cancer 14, 135.
Couzin-Frankel, J., 2013. Cancer immunotherapy. Science 342, 1432–1433.
Daudi, S., Eng, K.H., Mhawech-Fauceglia, P., Morrison, C., Miliotto, A.,
Beck, A., Matsuzaki, J., Tsuji, T., Groman, A., Gnjatic, S., et al., 2014.
Expression and immune responses to MAGE antigens predict survival in
epithelial ovarian cancer. PloS One 9, e104099.
Davis, M.M., Boniface, J.J., Reich, Z., Lyons, D., Hampl, J., Arden, B.,
Chien, Y., 1998. Ligand recognition by αβ T cell receptors. Annu Rev
Immunol 16, 523–544.
De Boer, R.J., Hogeweg, P., Dullens, H.F., De Weger, R.A., Den Otter, W.,
1985. Macrophage T lymphocyte interactions in the anti-tumor immune
response: A mathematical model. J Immunol 134, 2748–2758.
De Smet, C., De Backer, O., Faraoni, I., Lurquin, C., Brasseur, F., Boon, T.,
1996. The activation of human gene MAGE-1 in tumor cells is correlated
with genome-wide demethylation. Proc Nat Acad Sci 93, 7149–7153.
Delitala, M., Dianzani, U., Lorenzi, T., Melensi, M., 2013. A mathematical
model for immune and autoimmune response mediated by T-cells. Comput
Math Appl 66, 1010–1023.
Delitala, M., Lorenzi, T., 2013. Recognition and learning in a mathematical
model for immune response against cancer. Discrete Contin Dyn Syst Ser
B 18, 891–914.
29


## Page 30


Deroulers, C., Aubert, M., Badoual, M., Grammaticos, B., 2009. Modeling
tumor cell migration: From microscopic to macroscopic models. Phys Rev
E 79, 031917.
d’Onofrio, A., Ciancio, A., 2011. Simple biophysical model of tumor evasion
from immune system control. Phys Rev E 84, 031910.
Ehrlich, M., 2002. DNA methylation in cancer: Too much, but also too little.
Oncogene 21, 5400.
Engelhardt, J.J., Boldajipour, B., Beemiller, P., Pandurangi, P., Sorensen,
C., Werb, Z., Egeblad, M., Krummel, M.F., 2012.
Marginating dend-
ritic cells of the tumor microenvironment cross-present tumor antigens
and stably engage tumor-speciﬁc T cells. Cancer Cell 21, 402–417.
Fehres, C.M., Unger, W.W.J., Garcia-Vallejo, J.J., van Kooyk, Y., 2014.
Understanding the biology of antigen cross-presentation for the design of
vaccines against cancer. Front Immunol 5, 149.
Feinberg, A.P., 2004. The epigenetics of cancer etiology, in: Seminars in
Cancer Biology, Elsevier. pp. 427–432.
Feinberg, A.P., Tycko, B., 2004. The history of cancer epigenetics. Nat Rev
Cancer 4, 143.
Gerdemann, U., Katari, U., Christin, A.S., Cruz, C.R., Tripic, T., Rousseau,
A., Gottschalk, S.M., Savoldo, B., Vera, J.F., Heslop, H.E., et al.,
2011. Cytotoxic T lymphocytes simultaneously targeting multiple tumor-
associated antigens to treat EBV negative lymphoma. Mol Theory 19,
2258–2268.
Gomis, R.R., Gawrzak, S., 2017. Tumor cell dormancy. Mol Oncol 11, 62–78.
Graﬀ-Dubois, S., Faure, O., Gross, D.A., Alves, P., Scardino, A., Chouaib,
S., Lemonnier, F.A., Kosmatopoulos, K., 2002. Generation of CTL recog-
nizing an HLA-A* 0201-restricted epitope shared by MAGE-A1,-A2,-A3,-
A4,-A6,-A10, and-A12 tumor antigens: Implication in a broad-spectrum
tumor immunotherapy. J Immunol 169, 575–580.
Hanahan, D., Weinberg, R.A., 2011. Hallmarks of cancer: The next genera-
tion. Cell 144, 646–674.
30


## Page 31


Harris, T.H., Banigan, E.J., Christian, D.A., Konradt, C., Wojno, E.D.T.,
Norose, K., Wilson, E.H., John, B., Weninger, W., Luster, A.D., et al.,
2012. Generalized L´evy walks and the role of chemokines in migration of
eﬀector CD8+ T cells. Nature 486, 545–548.
Hartmann, S., Brisam, M., Rauthe, S., Driemel, O., Brands, R.C., Rosen-
wald, A., K¨ubler, A.C., M¨uller-Richter, U.D., 2016. Contrary melanoma-
associated antigen-A expression at the tumor front and center: A compar-
ative analysis of stage I and IV head and neck squamous cell carcinoma.
Oncol Lett 12, 2942–2947.
Hartmann, S., Kriegebaum, U., K¨uchler, N., Brands, R.C., Linz, C., K¨ubler,
A.C., M¨uller-Richter, U.D.A., 2014. Correlation of MAGE-A tumor anti-
gens and the eﬃcacy of various chemotherapeutic agents in head and neck
carcinoma cells. Clin Oral Investig 18, 189–197.
Hartmann, S., Kriegebaum, U., K¨uchler, N., Lessner, G., Brands, R.C., Linz,
C., Schneider, T., K¨ubler, A.C., M¨uller-Richter, U.D.A., 2013. Eﬃcacy of
cetuximab and panitumumab in oral squamous cell carcinoma cell lines:
Prognostic value of MAGE-A subgroups for treatment success. J Cranio
Maxill Surg 41, 623–629.
Johnston, M.D., Edwards, C.M., Bodmer, W.F., Maini, P.K., Chapman, S.J.,
2007. Mathematical modeling of cell population dynamics in the colonic
crypt and in colorectal cancer. Proc Nat Acad Sci 104, 4008–4013.
June, C.H., O’Connor, R.S., Kawalekar, O.U., Ghassemi, S., Milone, M.C.,
2018. CAR T cell immunotherapy for human cancer. Science 359, 1361–
1365.
Kenney, J.F., Keeping, E.S., 1962. Mathematics of Statistics Pt. 1. Princeton,
NJ: Van Nostrand.
Kolev, M., Nawrocki, S., Zubik-Kowal, B., 2013. Numerical simulations for
tumor and cellular immune system interactions in lung cancer treatment.
Commun Nonlinear Sci Numer Simul 18, 1473–1480.
K¨ose, E., Moore, S., Ofodile, C., Radunskaya, A., Swanson, E.R., Zollinger,
E., 2017. Immuno-kinetics of immunotherapy: Dosing with DCs. Lett
Biomath 4, 39–58.
31


## Page 32


Kuznetsov, V.A., Makalkin, I.A., Taylor, M.A., Perelson, A.S., 1994. Non-
linear dynamics of immunogenic tumors: Parameter estimation and global
bifurcation analysis. Bull Math Biol 56, 295–321.
Linette, G.P., Stadtmauer, E.A., Maus, M.V., Rapoport, A.P., Levine, B.L.,
Emery, L., Litzky, L., Bagg, A., Carreno, B.M., Cimino, P.J., et al., 2013.
Cardiovascular toxicity and titin cross-reactivity of aﬃnity-enhanced T
cells in myeloma and melanoma. Blood 122, 863–871.
Ljunggren, H., Stam, N.J., ¨Ohl´en, C., Neefjes, J.J., H¨oglund, P., Heemels,
M., Bastin, J., Schumacher, T.N.M., Townsend, A., K¨arre, K., et al., 1990.
Empty MHC class I molecules come out in the cold. Nature 346, 476.
Lorenzi, T., Chisholm, R.H., Clairambault, J., 2016. Tracking the evolution
of cancer cell populations through the mathematical lens of phenotype-
structured equations. Biol Direct 11, 43.
Lorenzi, T., Chisholm, R.H., Melensi, M., Lorz, A., Delitala, M., 2015. Math-
ematical model reveals how regulating the three phases of T-cell response
could counteract immune evasion. Immunology 146, 271–280.
 Luksza, M., Riaz, N., Makarov, V., Balachandran, V.P., Hellmann, M.D.,
Solovyov, A., Rizvi, N.A., Merghoub, T., Levine, A.J., Chan, T.A., et al.,
2017. A neoantigen ﬁtness model predicts tumour response to checkpoint
blockade immunotherapy. Nature 551, 517–520.
Macfarlane, F.R., Lorenzi, T., Chaplain, M.A.J., 2018. Modelling the im-
mune response to cancer: An individual-based approach accounting for the
diﬀerence in movement between inactive and activated T cells. Bull Math
Biol 80, 1539–1564.
Mallet, D.G., de Pillis, L.G., 2006. A cellular automata model of tumor-
immune system interactions. J Theor Biol 239, 334–350.
Manem, V.S., Kohandel, M., Komarova, N., Sivaloganathan, S., 2014. Spatial
invasion dynamics on random and unstructured meshes: Implications for
heterogeneous tumor populations. J Theor Biol 349, 66–73.
Manjili, M.H., 2018. A theoretical basis for the eﬃcacy of cancer immun-
otherapy and immunogenic tumor dormancy: The adaptation model of
immunity. Adv Cancer Res 137, 17–36.
32


## Page 33


Marcar, L., MacLaine, N.J., Hupp, T.R., Meek, D.W., 2010.
MAGE-A
cancer/testis antigens inhibit p53 function by blocking its interaction with
chromatin. Cancer Res 70, 10362–10370.
Matzavinos, A., Chaplain, M.A.J., 2004. Travelling-wave analysis of a model
of the immune response to cancer. C R Biol 327, 995–1008.
Matzavinos, A., Chaplain, M.A.J., Kuznetsov, V.A., 2004. Mathematical
modelling of the spatio-temporal response of cytotoxic T-lymphocytes to
a solid tumour. Math Med Biol 21, 1–34.
Mellman, I., Coukos, G., Dranoﬀ, G., 2011. Cancer immunotherapy comes
of age. Nature 480, 480.
Messerschmidt, J.L., Prendergast, G.C., Messerschmidt, G.L., 2016. How
cancers escape immune destruction and mechanisms of action for the
new signiﬁcantly active immune therapies: Helping non-immunologists de-
cipher recent advances. Oncologist 21, 233–243.
Monte, M., Simonatto, M., Peche, L.Y., Bublik, D.R., Gobessi, S., Pierotti,
M.A., Rodolfo, M., Schneider, C., 2006. MAGE-A tumor antigens target
p53 transactivation function through histone deacetylase recruitment and
confer resistance to chemotherapeutic agents.
Proc Nat Acad Sci 103,
11160–11165.
M¨uller-Richter, U.D.A., Dowejko, A., Reuther, T., Kleinheinz, J., Reichert,
T.E., Driemel, O., 2009. Analysis of expression proﬁles of MAGE-A anti-
gens in oral squamous cell carcinoma cell lines. Head Face Med 5, 10.
Oey, H., Whitelaw, E., 2014. On the meaning of the word “epimutation”.
Trends Genet 30, 519–520.
Ott, P.A., Hu, Z., Keskin, D.B., Shuklka, S.A., Sun, J., et al., 2017. An
immunogenic personal neoantigen vaccine for patients with melanoma.
Nature 547, 217–221.
Painter, K.J., Hillen, T., 2015. Navigating the ﬂow: Individual and con-
tinuum models for homing in ﬂowing environments. J R Soc Interface 12,
20150647.
33


## Page 34


Peltom¨aki, P., 2012. Mutations and epimutations in the origin of cancer.
Exp Cell Res 318, 299–310.
Penington, C.J., Hughes, B.D., Landman, K.A., 2011. Building macroscale
models from microscale probabilistic models: a general probabilistic ap-
proach for nonlinear diﬀusion and multispecies phenomena. Phys Rev E
84, 041120.
de Pillis, L., Renee Fister, K., Gu, W., Collins, C., Daub, M., Gross, D.,
Moore, J., Preskill, B., 2009.
Mathematical model creation for cancer
chemo-immunotherapy. Comput Math Meth Med 10, 165–184.
de Pillis, L.G., Mallet, D.G., Radunskaya, A.E., 2006. Spatial tumor-immune
modeling. Comput Math Meth Med 7, 159–176.
Raman, M.C.C., Rizkallah, P.J., Simmons, R., Donnellan, Z., Dukes, J.,
Bossi, G., Le Provost, G.S., Todorov, P., Baston, E., Hickman, E., et al.,
2016. Direct molecular mimicry enables oﬀ-target cardiovascular toxicity
by an enhanced aﬃnity TCR designed for cancer immunotherapy. Sci Rep
6, 18851.
Ribas, A., Wolchok, J.D., 2018. Cancer immunotherapy using checkpoint
blockade. Science 349, 1350–1355.
Roch, N., Kutup, A., Vashist, Y., Yekebas, E., Kalinin, V., Izbicki, J.R.,
2010. Coexpression of MAGE-A peptides and HLA class I molecules in
hepatocellular carcinoma. Anticancer Res 30, 1617–1623.
Sahin, U., Derhovanessian, E., Miller, M., Kloke, B., Simon, P., et al., 2017.
Personalized RNA mutanome vaccines mobilize poly-speciﬁc therapeutic
immunity against cancer. Nature 547, 222–226.
Schmid, D.A., Irving, M.B., Posevitz, V., Hebeisen, M., Posevitz-Fejfar,
A., Sarria, J.C.F., Gomez-Eerland, R., Thome, M., Schumacher, T.N.M.,
Romero, P., et al., 2010. Evidence for a TCR aﬃnity threshold delimiting
maximal CD8 T cell function. J Immunol 184, 4936–4946.
Schueler-Furman, O., Elber, R., Margalit, H., 1998. Knowledge-based struc-
ture prediction of MHC class I bound peptides: A study of 23 complexes.
Fold Des 3, 549–564.
34


## Page 35


Schumacher, T.N., Hacohen, N., 2016. Neoantigens encoded in the cancer
genome. Curr Opinion Immunol 41, 98–103.
Sharma, P., Allison, J.P., 2015. The future of immune checkpoint therapy.
Science 348, 56–61.
Slansky, J.E., Jordan, K.R., 2010. The Goldilocks model for TCR: Too much
attraction might not be best for vaccine design. PLoS Biol 8, e1000482.
Smith, S.N., Wang, Y., Baylon, J.L., Singh, N.K., Baker, B.M., Tajkhorshid,
E., Kranz, D.M., 2014. Changing the peptide speciﬁcity of a human T cell
receptor by directed evolution. Nature Comm 5, 5223.
Stace, R.E., Stiehl, T., Marciniak-Czochra, A., Lorenzi, T., 2019.
A
phenotype-structured individual-based model for the evolution of cancer
cell populations under chemotherapy. Preprint .
Stevens, A., 2000. The derivation of chemotaxis equations as limit dynamics
of moderately interacting stochastic many-particle systems. SIAM J Appl
Math 61, 183–212.
Stone, J.D., Chervin, A.S., Kranz, D.M., 2009. T-cell receptor binding aﬃn-
ities and kinetics: Impact on T-cell activity and speciﬁcity. Immunology
126, 165–176.
Tan, M.P., Gerry, A.B., Brewer, J.E., Melchiori, L., Bridgeman, J.S., Ben-
nett, A.D., Pumphrey, N.J., Jakobsen, B.K., Price, D.A., Ladell, K., et al.,
2015.
T cell receptor binding aﬃnity governs the functional proﬁle of
cancer-speciﬁc CD8+ T cells. Clin Exp Immunol 180, 255–270.
Teng, M.W.L., Swann, J.B., Koebel, C.M., Schreiber, R.D., Smyth, M.J.,
2008. Immune-mediated dormancy: An equilibrium with cancer. J Leuk-
ocyte Biol 84, 988–993.
Tomasetti, C., Levy, D., 2010. An elementary approach to modeling drug
resistance in cancer. Math Biosci Eng: MBE 7, 905.
Tong, J.C., Tan, T.W., Ranganathan, S., 2004. Modeling the structure of
bound peptide ligands to major histocompatibility complex. Protein Sci
13, 2523–2532.
35


## Page 36


Urosevic, M., Braun, B., Willers, J., Burg, G., Dummer, R., 2005. Expression
of melanoma-associated antigens in melanoma cell cultures. Exp Dermatol
14, 491–497.
Van Tongelen, A., Loriot, A., De Smet, C., 2017. Oncogenic roles of DNA
hypomethylation through the activation of cancer-germline genes. Cancer
Lett 396, 130–137.
Wang, S., Lin, S., 2013. Tumor dormancy: Potential therapeutic target in
tumor recurrence and metastasis prevention. Exp Hematol Oncol 2, 29.
Wischnewski, F., Pantel, K., Schwarzenbach, H., 2006. Promoter demethyl-
ation and histone acetylation mediate gene expression of MAGE-A1,-A2,-
A3, and-A12 in human cancer cells. Mol Cancer Res 4, 339–349.
Wu, A., Liao, D., Kirilin, V., Lin, K., Torga, G., Qu, J., Liu, L., Sturm,
J.C., Pienta, K., Austin, R., 2018. Cancer dormancy and criticality from
a game theory perspective. Cancer Convergence 2, 1.
Yang, B., O’Herrin, S.M., Wu, J., Reagan-Shaw, S., Ma, Y., Bhat, K.M.R.,
Gravekamp, C., Setaluri, V., Peters, N., Hoﬀmann, F.M., et al., 2007.
MAGE-A, MAGE-B and MAGE-C proteins form complexes with KAP1
and suppress p53-dependent apoptosis in MAGE-positive cell lines. Cancer
Res 67, 9954–9962.
Yarchoan, M., Johnson, B.A., Lutz, E.R., Laheru, D.A., Jaﬀee, E.M., 2017.
Targeting neoantigens to augment antitumour immunity. Nat Rev Cancer
17, 209–222.
Yeh, A.C., Ramaswamy, S., 2015.
Mechanisms of cancer cell dormancy:
Another hallmark of cancer? Cancer Res 75, 5014–5022.
Zajac, P., Schultz-Thater, E., Tornillo, L., Sadowski, C., Trella, E., Men-
gus, C., Iezzi, G., Spagnoli, G.C., 2017. MAGE-A antigens and cancer
immunotherapy. Front Med 4, 18.
36

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1904_02979v2_a_stochastic_individual_based_model_to_explore_the_role_of_spatial_interactions
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1904_02979V2_A_STOCHASTIC_INDIVIDUAL_BASED_MODEL_TO_EXPLORE_THE_ROLE_OF_SPATIAL_INTERACTIONS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

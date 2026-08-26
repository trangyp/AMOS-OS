---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1404.2900v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1404.2900v1_Lower_glycolysis_carries_a_higher_flux_than_any_biochemically_possible_alternati

> Source: 1404.2900v1_Lower_glycolysis_carries_a_higher_flux_than_any_biochemically_possible_alternati.pdf

> Pages: 9

---


## Page 1


arXiv:1404.2900v1  [q-bio.MN]  10 Apr 2014
Lower glycolysis carries a higher ﬂux than any biochemically possible alternative
Steven J. Court, Bart lomiej Waclaw, Rosalind J. Allen
SUPA, School of Physics and Astronomy, University of Edinburgh,
Mayﬁeld Road, Edinburgh EH9 3JZ, United Kingdom
The universality of many pathways of core metabolism suggests a strong role for evolutionary
selection, but it remains unclear whether existing pathways have been selected from a large or
small set of biochemical possibilities. To address this question, we construct in silico all possible
biochemically feasible alternatives to the trunk pathway of glycolysis and gluconeogenesis, one of
the most highly conserved pathways in metabolism. We show that, even though a large number
of alternative pathways exist, the alternatives carry lower ﬂux than the real pathway under typical
physiological conditions. Alternative pathways that could potentially carry higher ﬂux often lead
to infeasible intermediate metabolite concentrations. We also ﬁnd that if physiological conditions
were diﬀerent, diﬀerent pathways could outperform those found in nature. Our results demonstrate
how the rules of biochemistry restrict the alternatives that are open to evolution, and suggest that
the existing trunk pathway of glycolysis and gluconeogenesis represents a maximal ﬂux solution.
I.
INTRODUCTION
The
biochemical
pathways
of
central
carbon
metabolism are highly conserved across all domains
of life, and largely control the productivity of life on
Earth [1, 2].
Yet it remains unknown whether these
pathways are the result of historical contingency during
early evolution [3], or are instead optimal solutions to
the problem of energy and biomass production [4–9].
Put simply, are there alternative biochemically feasible
pathways that could perform the same function, and if
so, how do they perform compared to those found in
nature?
Previous studies have mainly addressed this question
either by constructing simpliﬁed artiﬁcial metabolic net-
works [4–6], or by mining databases of biochemical com-
pounds and reactions for known organisms [7, 8, 10–12].
Both of these approaches have drawbacks: the former
does not capture real biochemistry, while the latter is
limited to metabolites and reactions found in well-studied
organisms. Nevertheless this work has led to suggested
optimality principles including maximizing biochemical
ﬂux or yield [5, 6], minimizing biochemical steps or pro-
tein costs [4, 7], and ensuring that function is main-
tained in a changing environment [10]. Only a few stud-
ies have attempted to explore the full universe of possible
metabolic pathways, using realistic rules of biochemistry
[9, 13–16]. In particular, using this approach Noor et al.
[9] recently suggested that central carbon metabolism,
taken as a whole, uses the minimal number of enzymatic
steps needed to generate a predeﬁned set of biochemical
precursors.
Here, we perform an exhaustive computational search
for all possible biochemically feasible alternatives to one
of the most ancient and most highly conserved sections of
central carbon metabolism, the trunk pathway of glycoly-
sis and gluconeogenesis. Glycolysis breaks down glucose
to pyruvate, generating ATP, NADH and biosynthetic
precursors, while gluconeogenesis uses ATP and NADH
to generate glucose from pyruvate.
The glycolytic-
gluconeogenic pathway (Fig. S1) is almost linear and can
be divided into two parts: an “upper” chain of reactions
involving 6-carbon molecules, which connects glucose to
glyceraldehyde-3-phosphate (G3P), and a “lower” chain
of reactions involving 3-carbon molecules, which connects
G3P to pyruvate (Fig. 1). This lower reaction chain is
known as the trunk pathway. In prokaryotes, the gly-
colytic and gluconeogenic trunk pathways consist of al-
most the same set of 5 reactions, diﬀering only in one
step.
In glycolysis, the exergonic conversion of phos-
phoenolpyruvate (PEP) to pyruvate is coupled to the
phosphorylation of ADP to ATP, while in gluconeoge-
nesis the reverse reaction is driven by the hydrolysis of
ATP to AMP, either with release of inorganic phosphate
G3P
Figure 1:
The trunk pathway of glycolysis and gluconeo-
genesis.
The end points are glyceraldehyde 3-phosphate
(G3P) and pyruvate (PYR); intermediate metabolites are 1,3-
bisphosphoglycerate (1,3-BPG); 3-phosphoglycerate (3PG);
2-phosphoglycerate (2PG); and phosphoenolpyruvate (PEP).
For each reaction the external metabolites involved and the
ﬁrst 3 numbers from the EC number classiﬁcation are indi-
cated. The inset shows thermodynamic proﬁles for the trunk
pathway in the glycolytic and gluconeogenenic (pps) direc-
tions (see Methods).


## Page 2


2
(the phosphoenolpyruvate synthase (pps) route), or via
consumption of inorganic phosphate and release of py-
rophosphate (the phosphate dikinase (ppdk) route).
While the upper part of the glycolytic/gluconeogenic
pathway exists in several very distinct variants, most
notably
the
Embden-Meyerhof-Parnas
and
Entner-
Doudoroﬀpathways (Fig. S1) [7, 17], the trunk path-
way is ubiquitous, and contains enzymes which are highly
conserved and universally distributed across the three do-
mains of life [18, 19]. The existence of such an ancient and
universal pathway suggests three possible scenarios: (i)
the trunk pathway is the only biochemical possibility, (ii)
alternatives exist but the extant pathway is evolutionar-
ily optimal and (iii) alternatives are possible but have not
been found by evolution. Distinguishing these scenarios
lies at the heart of much of evolutionary biology. Here,
we address this question directly using a computational
approach. By systematically constructing and exploring
the full space of biochemically feasible metabolites and
reactions, many of which are not currently exploited by
any known organism, we ﬁnd that hundreds of alternative
trunk pathways are possible. The one observed in na-
ture, however, carries the maximal biochemical ﬂux, un-
der reasonable constraints on the intermediate metabo-
lite and enzyme concentrations. Our results suggest that
the trunk pathway represents an optimal solution among
many possible alternatives.
II.
RESULTS
A.
A network of all possible biochemical reactions
We used a computer program to generate the network
of all possible biochemically feasible pathways between
G3P and pyruvate.
Metabolites.
Our program ﬁrst systematically gen-
erates all possible relevant internal metabolites,
i.e.
molecules intermediate between G3P and pyruvate, in-
cluding those that are not found in nature. Central car-
bon metabolism consists exclusively of reactions between
“CHOP” molecules: those composed of carbon, hydro-
gen, oxygen and phosphorus atoms, with the latter being
present only in phosphate groups. Nitrogen and sulfur
are present only in cofactors such as ATP, NAD and CoA
[20, 21]. Moreover, the trunk pathway contains only un-
branched aliphatic 3-carbon CHOP molecules, with the
exception of the 4-carbon oxaloacetate, used in gluconeo-
genesis in liver and kidney cells [22]. We therefore include
in our analysis all possible unbranched aliphatic CHOP
molecules containing up to 4 carbon atoms. We consider
only molecules which are electrostatically charged (i.e.
include carboxyl or phosphate groups). This condition
is motivated by the need to avoid leakage through the
lipid membrane, and is satisﬁed by almost all molecules
in core metabolism [23]. Applying these criteria results in
over 1000 diﬀerent molecules, including all the internal
metabolites in the real trunk pathway.
We computed
the free energy of formation ∆fG for all our internal
metabolites, using existing experimental data where pos-
sible [24] or, in the absence of such data, using a variant
of the group contribution method [25–27] (see Methods
and Supporting Information [28]).
Reactions.
Our program generates all possible reac-
tions among our set of internal metabolites, based on 12
EC reaction classes [29], which encompass all the reac-
tions between CHOP molecules of length 2-4 carbons in
core metabolism (Table I) [22]. Many of these reactions
involve cofactors such as ATP and NAD; we refer to these
as external metabolites and we assume that they have
ﬁxed concentrations, which deﬁne the cellular (physio-
logical) conditions. The external metabolites in our re-
action network are ATP, ADP, AMP, NAD, NADH, inor-
ganic phosphate Pi, pyrophosphate PPi, CO2 and H2O.
For each of our reaction classes, we include all known
couplings with the external metabolites (see Supporting
Information [28]).
B.
Our network generates many alternative trunk
pathways
Our network reveals a huge number of alternative path-
ways connecting G3P and pyruvate, which are consis-
tent with the rules of biochemistry.
For example, in
the glycolytic direction, we ﬁnd 13 pathways of length 4,
532 pathways of length 5, and the number of pathways
increases exponentially with the path length (Fig. S2).
Some of these alternative pathways use the same set of
reaction types as the real trunk pathway, but execute
them in a diﬀerent order (e.g.
Fig.2 E, left).
Others
make use of a diﬀerent set of reaction types (Fig 2E,
right). A similar picture holds in the gluconeogenic di-
rection (Fig. S2).
How many of these alternative trunk pathways are fea-
sible under typical physiological conditions? We ﬁrst de-
mand that candidate pathways in the glycolytic direc-
tion should produce at least 2 ATP molecules. This is
required to make the whole glycolytic pathway produce
a net ATP yield, since the two dominant forms of gly-
colysis, the EMP and ED pathways, consume 1 ATP
molecule per G3P in their upper halves. In the gluco-
neogenic direction, the real trunk pathway consumes 2
ATPs, one of which is converted to ADP and the other
to AMP (Fig. 1); the AMP being eventually recycled to
ADP via the consumption of a third ATP in the adeny-
late kinase reaction. In this direction, we exclude any
candidate paths that have a poorer yield of G3P per ATP
than the real path. Motivated by considerations of sim-
plicity [4, 9] and cost of enzyme production [7], we then
further restrict our analysis to those pathways with the
minimum number of steps. In both the glycolytic and
gluconeogenic directions, the minimum pathway length
consistent with the above requirements is 5 steps; our


## Page 3


3
EC class
Example reaction
1.1.1
oxidation
CH3-CH2(OH) + NAD+ ⇋CH3-CHO + NADH
1.2.1
CH3-CHO + NAD+ + Pi ⇋CH3-COp + NADH + H+
2.7.1
CHO-CH2(OH) + ATP ⇋CHO-CH2p + ADP
2.7.2
phosphate transfer
CH3-COOH + ATP ⇋CH3-COp + ADP
2.7.9
CH3-CO-COOH + ATP + H2O/Pi ⇋CH2=Cp-COOH + AMP + Pi/PPi
3.1.3
hydrolysis
CH3-CH2p + H2O ⇋CH3-CH2(OH) + Pi
4.1.1
decarboxylation
CH3-CH(OH)-COOH + H2O ⇋CH3-CH2(OH) + CO2(aq)
4.2.1
dehydration
CH3-CH(OH)-COOH ⇋CH2=CH-COOH + H2O
5.3.1
isomerisation
CH3-CO-CH2(OH) ⇋CH3-CH(OH)-CHO
5.3.2
tautomerism
CH3-C(OH)=C(OH)-CH2p ⇋CH3-CO-CH(OH)-CH2p
5.4.2
isomerisation
CH3-CH(OH)-CH2p ⇋CH3-CHp-CH2(OH)
6.4.1
ATP-driven carboxylation CH3-CH2(OH) + CO2(aq) + ATP ⇋CH3-CH(OH)-COOH + ADP + Pi
Table I: The set of reaction types included in our analysis, deﬁned by the ﬁrst 3 numbers of the EC classiﬁcation. Phosphate
groups are denoted by a “p”. Not all variants of each reaction type are listed here; for a full list see Table SIII.
network generates 202 candidate 5-step glycolytic paths,
and 300 candidate 5-step gluconeogenic paths.
C.
Real glycolysis and gluconeogenesis carry
maximal ﬂux under physiological conditions
We next evaluated the performance of the alternative
trunk pathways generated by our network, by comparing
their steady-state metabolic ﬂux.
For glycolytic path-
ways, the metabolic ﬂux corresponds to the rate of ATP
production, while for gluconeogenic pathways, it corre-
sponds to the rate of production of G3P (and ultimately
of glucose). This ﬂux depends not only on the total free
energy change across a given pathway, but also on the
distribution of the individual reaction free energies (see
e.g. Fig. 1), which in turn depends on the intracellular en-
vironment via the concentrations of the external metabo-
lites. For linear pathways, the ﬂux can be calculated an-
alytically, assuming linear kinetics with diﬀusion-limited
enzymes [6, 30, 31] (see Methods). We also assume that,
for each pathway, the individual enzyme concentrations
are optimised to maximise pathway ﬂux, for a ﬁxed total
amount of enzyme (although similar results are obtained
when we relax this assumption; Fig. S3).
Importantly, when calculating the metabolic ﬂux, we
impose constraints on the intermediate internal metabo-
lite concentrations. For the bacterium E.coli, metabolite
concentrations range from 0.1µM to 100mM, with the
total intracellular metabolite pool being around 300mM
[33]. We expect that very low metabolite concentrations
are undesirable due to molecular noise, while very high
concentrations are precluded by osmotic considerations.
We therefore set the ﬂux to zero for a given pathway
if any of its intermediate metabolite concentrations falls
outside the range 1nM to 0.5M.
Imposing this constraint, we calculated the metabolic
ﬂux of all our 202 glycolytic, and 300 gluconeogenic can-
didate paths, across a wide range of intracellular con-
ditions, as deﬁned by the external metabolite concen-
trations. We randomly selected 10,000 points from the
10-dimensional parameter space consisting of the concen-
trations of the 8 external metabolites, G3P and pyruvate,
sampling each parameter logarithmically over several or-
ders of magnitude above and below its typical physiolog-
ical concentration (see Supporting Information [28]). For
each point in parameter space we evaluated the ﬂux of
each candidate pathway.
As a simple metric, we ﬁrst compare the performance
of our candidate pathways, averaged over the entire pa-
rameter space. To this end, we compute the comparative
ﬂux (CF), which is the ﬂux of a given pathway, divided
by the maximum ﬂux obtained amongst all pathways, at
a given point in parameter space. Averaging this quan-
tity across the whole parameter space gives a measure of
relative performance, for each candidate path. We ﬁnd
that the real glycolytic and gluconeogenic pathways per-
form remarkably well, compared to the many alternatives
(Fig. 2, left panels). For glycolysis (Fig. 2A), the natural
trunk pathway (in green, indicated by the arrow) outper-
forms all the alternative pathways except one. For glu-
coneogenesis, the two natural variants, with diﬀerent co-
factor coupling for the pyruvate to PEP step, are ranked
ﬁrst (the pps route, shown in red in Fig. 2C) and 8th
(the ppdk route, shown in black in Fig. 2C). These re-
sults strongly suggest that the natural trunk pathways
carry a high ﬂux compared to alternatives; however this
metric is dependent on the range of parameter space that
is sampled.
To investigate in more detail, we analyzed which of our
candidate pathways achieved the highest ﬂux at diﬀerent
points in the parameter space. This allows us to under-
stand how the performance of a given pathway depends
on the intracellular environment. Our results show that
diﬀerent candidate pathways perform best in diﬀerent
regions of the parameter space. In particular, pathway
performance is very sensitive to the cellular energy state,
as measured by the ratio of the ATP and ADP concen-


## Page 4


4
A
C
E
B
D
Glycolysis
Gluconeogenesis
      Glycolytic path:
 6                                  1
Figure 2: The real glycolytic and gluconeogenic trunk pathways represent maximal ﬂux solutions. A, C: Alternative pathways
generated in our analysis ordered by their comparative ﬂux (see text), averaged across the whole 10-dimensional parameter
space. The top 25 paths are shown. Panel A shows glycolytic pathways; the green bar (indicated by the arrow) is the real
pathway. Panel C shows gluconeogenic paths; the black and red bars (indicated by arrows) are the real pps and ppdk routes. B,
D: Relative pathway performance as a function of the intracellular environment. Each dot represents a randomly sampled point
in parameter space; the colour of the dot indicates the candidate pathway which had the highest ﬂux at that point in parameter
space (colours as in panels A,C). For parameter sampling procedure, see Methods. The axes represent the redox state and
energy state of the cell: [NAD][Pi]/[NADH] and [ATP]/[ADP]. The red boxes indicate the typical physiological state of the
cell [32, 33]: [ATP]/[ADP] = 3-20, [NAD][Pi]/[NADH] = 0.01-10M [based on [NAD]/[NADH] =10-100 and [Pi] = 1-100mM].
Panel B shows glycolytic pathways; real glycolysis (green) does best under typical physiological conditions. Panel D shows
gluconeogenic pathways; the two real routes (red and black) perform best under typical cellular conditions. E: two alternative
glycolytic pathways, numbers 6 and 1. In the molecular representations, grey, white, red and orange spheres represent carbon,
hydrogen, oxygen and phosphorus atoms respectively.
trations ([ATP]/[ADP]), and redox state, as measured
by the ratio [NAD][Pi]/[NADH] (Fig. 2 (middle panels)).
Focusing on the glycolytic pathways (Fig.
2B) we see
that, remarkably, the natural trunk pathway (green dots)
outperforms all the alternatives in the region of parame-
ter space close to that found in living cells (red box). This
suggests that the glycolytic trunk pathway represents a
maximal ﬂux solution for the conversion of G3P to pyru-
vate, under typical intracellular conditions. For the glu-
coneogenic pathways (Fig. 2D), a similar picture holds.
Here, the two pathways found in nature, the pps-route
(red) and the ppdk-route (black), both outperform the
alternatives under typical physiological conditions (red
box). The relative performance of these two pathways de-
pends sensitively on the concentration of pyrophosphate
(see Fig. S4).
D.
Alternative trunk pathways
Our analysis reveals several alternative pathways that
can, under diﬀerent intracellular conditions, outperform
the true glycolytic and gluconeogenic pathways (Fig. 2,
middle panels and Fig. 3, Fig. S5-S8).
In the glycolytic direction, path 1 (black) outper-
forms the real trunk pathway for low [ATP]/[ADP] ratios
(Fig. 2B), resulting in its apparently better performance
than the real pathway when averaged over the whole pa-
rameter space (Fig. 2A). This pathway, shown on the
right of Fig. 2E, diﬀers from the real pathway in that
it converts G3P directly to 3-phosphoglycerate (3-PG)
without the production of ATP (Fig. 3, compare black
and green). This means that it has a highly exergonic
oxidation reaction as its ﬁrst step. In a linear pathway,
the initial reactions tend to exert the greatest control
over the ﬂux [6], so an exergonic ﬁrst reaction can result
in a large ﬂux. However, pathway 1 is highly sensitive to
the constraints on the intermediate metabolite concentra-
tions. Because of its exergonic ﬁrst reaction, it tends to


## Page 5


5
G3P
CHO-CH(OH)-CH2p
CHO-CHp-CH2(OH)
1,3-BPG
CH2p-CH(OH)-COp
3-PG
COOH-CH(OH)-CH2p
 
CH2=Cp-CHO
2-PG
CH2(OH)-CHp-COOH
PEP
  CH2=Cp-COOH
PYR 
 CH3-CO-COOH
CH3-CO-COp
oxaloacetate 
COOH-CH2-CO-COOH
CH2=Cp-COp
2,3-BPG
COOH-CHp-CH2p
CHO-CO-CH2-COOH
Path  1  
Path  5 
Path  2  (real)
Path  3 
Path  4
Figure 3: Alternative pathways which perform well in the
glycolytic direction.
Reactions are indicated by lines; the
colour denotes the pathway as in Fig. 2A and B; stars indicate
ATP-producing steps. Intermediate metabolites are shown by
symbols; black squares indicate metabolites in the real trunk
pathway, black and grey circles indicate metabolites present
and not present in the KEGG database [34], respectively.
accumulate high concentrations of downstream metabo-
lites, causing it to be deemed infeasible in our analysis
over a large part of the parameter space.
Pathway 3 (red), is similar to the real glycolytic trunk
path, except that 1,3 bisphosphoglycerate (1,3-BPG) is
ﬁrst isomerized (to 2,3-BPG) and then dephosphory-
lated (to 2-phosphoglycerate 2PG, with ATP genera-
tion), rather than being ﬁrst dephosphorylated and then
isomerized as in the real pathway (Fig. 3 and Fig. S5).
The large free energy change for the isomerization (∆G =
−28kJmol−1) means that pathway 3 can in principle
carry a higher ﬂux than the real pathway, but because
of this large drop in free energy it tends to accumu-
late high concentrations of 2,3-BPG and is therefore only
favourable for low concentrations of the starting metabo-
lite G3P. Interestingly, a similar pathway exists in red
blood cells, where 2,3-BPG is produced from 1,3-BPG
via the Rapoport-Leubering shunt [35].
In red blood
cells, however, the 2,3-BPG is hydrolysed to either 3-PG
or 2-PG without ATP generation [35], thus sacriﬁcing
one ATP compared to the usual glycolytic pathway. It is
tempting to hypothesize that nature is forced to sacriﬁce
an ATP molecule when using this shunt, to prevent the
buildup of 2,3-BPG, which is already the most concen-
trated organophosphate in erythrocytes.
Pathway 4 (violet) outperforms the real pathway at
high ATP concentrations (Fig. 2B); this is because its
ATP producing steps are at the end (4th and 5th steps),
in contrast to the real pathway where ATP is produced
in the 2nd and 5th steps (Fig. 3, Fig. S5). Because later
steps in a linear pathway tend to have less impact on the
ﬂux [6], this makes pathway 4 more tolerant of high ATP
concentrations than the real pathway. Similarly, path-
way 5 (orange) diﬀers from the real pathway in that its
oxidation step is moved to the end (the 4th step rather
than the ﬁrst as in the real pathway); this makes path-
way 5 more tolerant of reducing conditions than the real
pathway (Fig. 2B, Fig. S5). Several other interesting al-
ternative glycolytic trunk pathways are discussed in the
Supporting Information [28], section XI.
In the gluconeogenic direction (Fig. 2, C and D; Fig. S7
and S8), pathways 1 (red) and 8 (black) correspond to the
two prokaryotic trunk pathway variants found in nature,
the pps and ppdk routes. Interestingly, alternative path-
ways 2-7 all contain the same set of reaction types as the
real pps pathway, but carry out these reactions in varying
order, thus making use of diﬀerent intermediate internal
metabolites.
This aﬀects their relative performance in
diﬀerent regions of the parameter space. For example,
pathway 2 (orange) and pathway 4 (green) both diﬀer
from the real pps pathway in that ATP is consumed in
the ﬁrst two reactions (rather than in the 1st and 4th
reactions as in the real pps pathway, Fig. S8).
This
makes their ﬂux more sensitive to the ATP concentra-
tion, explaining why they dominate at high ATP/ADP
ratio (Fig. 2D).
Interestingly, eukaryotes use a slightly diﬀerent gluco-
neogenic trunk pathway, in which the conversion of pyru-
vate to PEP is a two-step process (via 4-carbon oxaloac-
etate) in which ATP is converted to ADP twice, rather
than a 1-step process, converting ATP to AMP as in the
prokaryotic pps and ppdk routes. Because the eukaryotic
gluconeogenic trunk pathway is of length 6 steps, it was
not considered in our analysis. However, when we repeat
our analysis in the absence of dikinase reactions (i.e. not
allowing the conversion of ATP to AMP), we ﬁnd that
the shortest feasible gluconeogenic pathways are 6 steps,
and that the real eukaryotic pathway outperforms all al-
ternatives under physiological conditions (Fig. S9).
E.
Constraints on metabolite concentrations are
important
Imposing constraints on the intermediate internal
metabolite concentrations is crucial to our analysis. Re-
peating our analysis without these constraints produces
a very diﬀerent outcome (Fig. 4). In the glycolytic direc-
tion, if the metabolite concentrations are unconstrained,
glycolytic path 1 (Fig. 2E, right; black in Fig. 2A and B),
which has a highly exergonic ﬁrst reaction, produces the
highest ﬂux across the entirety of the parameter space.
A similar picture emerges in the gluconeogenic direction
(Fig. S10). The fact that our results are strongly aﬀected
by constraining the metabolite concentrations highlights


## Page 6


6
Figure 4: Constraints on metabolite concentrations are cru-
cial. Repeating our analysis without these constraints, in the
glycolytic direction, pathway 1 (black in Fig. 2A and B and
shown on the right of Fig. 2E) dominates over the whole pa-
rameter space. The inset to the left panel shows the thermo-
dynamic proﬁle for pathway 1 (black) alongside that of the
real path 2 (green).
the importance of considering metabolite concentrations
when using methods such as ﬂux balance analysis [36] to
study metabolic networks.
Interestingly, all the enzymes required for glycolytic
pathway 1 exist in nature, in various organisms (Fig. S6),
although this route is not known to be used in nature
as a glycolytic pathway.
Our analysis hints that con-
structing this pathway could provide an interesting target
for synthetic biology, since it could, in principle, provide
a new way to accelerate growth of organisms useful for
biotechnological applications, if suitable branching path-
ways were provided to prevent the buildup of downstream
metabolites.
We also repeated our analysis, imposing a narrower
concentration range for the intermediate metabolite con-
centrations (10−7 to 10−2M rather than 10−9 to 5 ×
10−1M). Under these constraints, we ﬁnd that the real
glycolytic pathway outperforms the alternatives over a
wider range of parameter space, while the restricted con-
centration range has little eﬀect on our results for the
gluconeogenic paths (Fig. S11).
This further supports
the picture emerging from our analysis, that in the pres-
ence of reasonable limits on intermediate metabolite con-
centrations, the real glycolytic and gluconeogenic paths
outperform the alternatives.
III.
DISCUSSION
Despite the huge variety and complexity of life on
Earth, the biochemistry of core metabolism is remark-
ably universal. Our analysis shows that this universal-
ity does not arise from an absence of other possibilities.
Using a systematic approach, we have identiﬁed many
alternatives to perhaps the most highly conserved set
of metabolic reactions, the glycolytic and gluconeogenic
trunk pathways. Our alternative pathways obey the rules
of biochemistry, carry positive ﬂux under reasonable in-
tracellular conditions, and satisfy reasonable constraints
on metabolite concentrations. Remarkably, of all these
alternatives, we ﬁnd that the trunk pathway observed
in nature carries the highest biochemical ﬂux in both
the glycolytic and gluconeogenic directions, for parame-
ters that represent typical intracellular physiological con-
ditions.
Of the two variants of the prokaryotic gluco-
neogenic pathway that are found in nature, the pps route
is the best performer across a wide parameter range,
while the ppdk route also carries a high ﬂux, but is
more sensitive to environmental conditions, requiring a
low concentration of pyrophosphate (Fig. S4). The fact
that our analysis identiﬁes the real pathways using only
ﬂux maximization combined with constraints on inter-
mediate metabolite concentrations and a requirement for
minimal pathway length suggests that these three factors
are all likely to have been important driving forces in the
evolution of metabolism.
Flux maximization is widely recognized as an impor-
tant concept in the study of metabolism; both from the
perspective of glycolysis [5, 6] and more broadly [36].
Our results support this picture, but suggest that evo-
lutionary pressures on metabolic ﬂuxes have to operate
within the context of reasonable constraints on metabo-
lite concentrations, and that neglecting these constraints
can produce dramatically diﬀerent outcomes.
Our re-
sults expand on the recent suggestion of Noor et al. [9]
that central carbon metabolism can be understood as a
minimal walk between the set of metabolites essential
for growth.
In our analysis, the real pathways do in-
deed minimize the total number of reaction steps; this
imposes a strong constraint on the number of alternative
paths. However we ﬁnd that the requirement to produce
a set of essential biochemical precursors is not suﬃcient
to explain the biochemical structure of the natural trunk
pathway. Firstly, alternative pathways are possible which
produce the essential precursors with the same number
of steps (e.g. glycolytic path 1). Secondly, many of our
alternative pathways produce very similar, but not iden-
tical, intermediates to those of the real trunk pathway
and it is conceivable that these could be used as alterna-
tive precursors. Our results show that ﬂux maximization
provides a criterion by which these alternative minimal-
length pathways may be distinguished.
Our analysis also reveals alternative trunk pathways
which can perform better than the real one under dif-
ferent concentrations of reactant, product and external
metabolites.
While some of these alternatives involve
compounds and reactions which are not found in bio-
chemical databases, others use enzymes which are known
to exist in nature. The latter pathways are clearly plausi-
ble biochemically but are apparently not used in nature.
In some cases (e.g. our alternative glycolytic paths 1 and
3) this is probably because they tend to generate large in-
termediate concentrations. In other cases (e.g. glycolytic
pathways 4 and 5), the alternatives are not optimal under
typical physiological conditions, but would be optimal if
conditions were diﬀerent.
In this study, we have limited our analysis to path-
ways which start and end at G3P and pyruvate. Relax-
ing this requirement would certainly lead to many more


## Page 7


7
alternative pathways for the generation of energy, and
for biosynthesis. While it is also important to consider
other factors, including the need for integration within a
wider metabolic network, our analysis suggests that key
principles underlying the structure of core metabolism
may emerge from simple biochemical, thermodynamic
and biophysical considerations.
IV.
METHODS
A.
Chemical compounds and reactions
We created a list of chemical compounds with 2, 3 or 4
carbon atoms by generating all possible linear combina-
tions of the 17 “building blocks” shown in Table SI. Each
of the building blocks was composed of a single carbon
atom with associated oxygen, hydroxyl, hydrogen and/or
phosphate groups. Building blocks were connected to-
gether in linear chains by single or double bonds. This
procedure created 1008 linear molecules, 828 of which
are electrostatically charged in solution, i.e. containing
at least one carboxyl or phosphate group.
These 828
molecules are our internal metabolites.
Next, for ev-
ery possible pair of molecules from this list we checked
systematically whether the reactions from Table I could
transform one molecule into another, allowing for all pos-
sible couplings with the external metabolites. In this way,
a network of 7145 reactions was generated (see Support-
ing Information [28] section VII).
B.
Free energies of compounds and reactions
For those internal metabolites which are known bio-
chemical species, standard free energies of formation
∆fG were taken from the literature [24]. For other in-
ternal metabolites, for which such data does not exist,
we employed a variant of the group contribution method
[25–27].
For each such molecule g1g2 . . . gn, composed
from building blocks {gi}, we calculated ∆fG using
∆fG = E0 +
X
j
E1(gj) +
X
<j,k>
E2(gj, gk),
(1)
where E0 is a constant, E1(gj) is the contribution of
group gj and E2(gj, gk) is a small correction due to neigh-
bouring group-group interactions. The values of E0, the
vector E1 and matrix E2 are determined by performing a
least-squares ﬁt to a training set of molecules with known
∆fGs that correspond most closely to the linear CHOP
molecules of our network (see Supporting Information
[28] section III). Thermodynamic proﬁles in Figs 1 and 4
are plotted for 1M concentrations of all metabolites.
C.
Flux calculation
We used the method of Ref. [6] to calculate the ﬂux
carried by a linear pathway. This method assumes that
the ﬂux through reaction i is given by [6, 30]:
vi = kd[Ei]([Si−1]qi −[Si])
1 + qi
,
(2)
where kd is the diﬀusion-controlled rate constant, [Ei]
is the enzyme concentration, [Si−1] and [Si] represent
substrate and product concentrations and qi is the ther-
modynamic constant. This expression assumes that the
enzyme acts as a perfect catalyst, and is used to derive
an expression for pathway ﬂux and metabolite concentra-
tions (a complete explanation can be found in the Sup-
porting Information [28] section IV and V). We then use
Powell’s method [37] to ﬁnd the set of enzyme concentra-
tions which maximize the ﬂux subject to the constraints
that (1) all steady-state intermediate concentrations are
within the prescribed range and (2) the total enzyme
concentration is ﬁxed.
D.
Sampling the parameter space
We randomly selected 10000 points from the parameter
space corresponding to the concentrations of 8 external
metabolites and the G3P and pyruvate concentrations.
Each parameter was sampled logarithmically over a range
covering several orders of magnitude above and below
its typical physiological concentrations (see Table SIV).
For each of these parameter points, we calculated the
optimized ﬂux Ji of each candidate pathway as detailed
above, and computed the comparative ﬂux of path i as
CFi = Ji/ max{Ji}, by dividing its ﬂux by the highest
ﬂux obtained across all pathways at the given point in
parameter space.
E.
Robustness of our results to small free energy
changes
Using the group contribution method, the typical error
in our calculation of the free energy of formation ∆fG for
a given molecule is a few kJ/mol (see Supporting Infor-
mation [28] section III). To check the robustness of our
results to such errors, our entire analysis was repeated
using ∆fG values computed using diﬀerent sets of train-
ing molecules, consisting of 80% of the molecules from
the original training set, chosen at random. The qual-
itative results using such networks were identical from
those obtained from the full set of training compounds.
For example, the top 25 glycolytic pathways obtained
from the reduced set contained 23 out of the 25 path-
ways from the original analysis. Although the rank order
of the pathways in terms of comparative ﬂux across the
whole parameter space did diﬀer, the top 3 performing
pathways were the same in both cases.


## Page 8


8
Acknowledgments
BW and RJA contributed equally to this work.
We thank Patrick Warren and Vincent Danos for
many helpful discussions.
SJC was supported by
a Carnegie/Caledonian Scholarship from the Carnegie
Trust for Scotland, BW was supported by a Leverhulme
Trust Early Career Fellowship and by a Royal Society of
Edinburgh Personal Research Fellowship, and RJA was
supported by a Royal Society University Research Fel-
lowship.
Conﬂict of interest
The authors declare no competing ﬁnancial interests.
[1] Romano, A. & Conway, T. Evolution of carbohydrate
metabolic pathways.
Res. Microbiol. 147, 448 – 455
(1996).
[2] Smith, E. & Morowitz, H. J. Universality in intermedi-
ary metabolism. Proc. Natl Acad. Sci. USA 101, 13168–
13173 (2004).
[3] Pal, C. et al.
Chance and necessity in the evolution
of minimal metabolic networks.
Nature 440, 667–670
(2006).
[4] Mel´endez-Hevia, E. & Isidoro, A. The game of the pen-
tose phosphate cycle.
J. Theor. Biol. 117, 251 – 263
(1985).
[5] Ebenh¨oh, O. & Heinrich, R. Evolutionary optimization
of metabolic pathways. theoretical reconstruction of the
stoichiometry of ATP and NADH producing systems. B.
Math. Biol. 63, 21–55 (2001).
[6] Heinrich, R., Montero, F., Klipp, E., Waddell, T. G.
& Mel´endez-Hevia, E.
Theoretical approaches to the
evolutionary optimization of glycolysis: Thermodynamic
and kinetic constraints. Eur. J. Biochem. 243, 191–201
(1997).
[7] Flamholz, A., Noor, E., Bar-Even, A., Liebermeister, W.
& Milo, R.
Glycolytic strategy as a tradeoﬀbetween
energy yield and protein cost. Proc. Natl Acad. Sci. USA
(2013).
[8] Barve, A. & Wagner, A. A latent capacity for evolution-
ary innovation through exaptation in metabolic system.
Nature 500, 203–206 (2013).
[9] Noor, E., Eden, E., Milo, R. & Alon, U. Central carbon
metabolism as a minimal biochemical walk between pre-
cursors for biomass and energy. Mol. Cell 39, 809 – 820
(2010).
[10] Samal, A., Wagner, A. & Martin, O. C.
Environ-
mental versatility promotes modularity in genome-scale
metabolic networks. BMC. Syst. Biol. 5 (2011).
[11] Bar-Even, A., Noor, E., Lewis, N. E. & Milo, R. Design
and analysis of synthetic carbon ﬁxation pathways. Proc.
Natl Acad. Sci. USA 107, 8889–8894 (2010).
[12] Handorf, T., Ebenh¨oh, O. & Heinrich, R.
Expanding
metabolic networks: Scopes of compounds, robustness,
and evolution. J. Mol. Evol. 61, 498–512 (2005).
[13] Mel´endez-Hevia, E., Waddell, T. G., Heinrich, R. &
Montero, F.
Theoretical approaches to the evolution-
ary optimization of glycolysis: Chemical analysis. Eur.
J. Biochem. 244, 527–543 (1997).
[14] Mittenthal, J. E., Yuan, A., Clarke, B. & Scheeline, A.
Designing metabolism: Alternative connectivities for the
pentose phosphate pathway. B. Math. Biol. 60, 815–856
(1998).
[15] Hatzimanikatis, V. et al. Exploring the diversity of com-
plex metabolic networks. Bioinformatics 21, 1603–1609
(2005).
[16] Henry,
C. S.,
Broadbelt,
L. J. & Hatzimanikatis,
V.
Discovery and analysis of novel metabolic path-
ways for the biosynthesis of industrial chemicals:
3-
hydroxypropanoate.
Biotechnol. Bioeng. 106, 462–473
(2010).
[17] Bar-Even, A., Flamholz, A., Noor, E. & Milo, R. Re-
thinking glycolysis: on the biochemical logic of metabolic
pathways. Nat. Chem. Biol. 8, 509–517 (2012).
[18] Ronimus, R. S. & Morgan, H. W. Distribution and phylo-
genies of enzymes of the embden-meyerhof-parnas path-
way from archaea and hyperthermophilic bacteria sup-
port a gluconeogenic origin of metabolism. Archaea 1,
199–221 (2002).
[19] Verhees, C. H. et al. The unique features of glycolytic
pathways in archaea. Biochem. J. 375, 231–246 (2003).
[20] Morowitz, H. J., Kostelnik, J. D., Yang, J. & Cody, G. D.
The origin of intermediary metabolism. Proc. Natl Acad.
Sci. USA 97, 7704–7708 (2000).
[21] Morowitz, H. J. A theory of biochemical organization,
metabolic pathways, and evolution. Complexity 4, 39–53
(1999).
[22] Berg, J., Tymoczko, J. & Stryer, L. Biochemistry (W H
Freeman and Company, 2002), 5th edn.
[23] Srinivasan, V. & Morowitz, H. J. Analysis of the interme-
diary metabolism of a reductive chemoautotroph. Biol.
Bull. 217, 222–232 (2009).
[24] Alberty, R. A. Biochemical Thermodynamics: Applica-
tions of Mathematica. Methods of Biochemical Analysis
(2006).
[25] Mavrovouniotis, M. L. Estimation of standard gibbs en-
ergy changes of biotransformations. Journal of Biological
Chemistry 266, 14440–14445 (1991).
[26] Mavrovouniotis, M. L. Group contributions for estimat-
ing standard gibbs energies of formation of biochemical
compounds in aqueous solution. Biotechnology and Bio-
engineering 36, 1070–1082 (1990).
[27] Jankowski, M. D., Henry, C. S., Broadbelt, L. J. & Hatz-
imanikatis, V. Group contribution method for thermody-
namic analysis of complex metabolic networks. Biophys.
J. 95, 1487 – 1499 (2008).
[28] S. J. Court, B. W. & Allen, R. J. Supporting information.
http://www2.ph.ed.ac.uk/~bwaclaw/suppmatt/Court_et_al_SupIn
(2014).
[29] Webb, E.
Enzyme nomenclature 1992:
recommenda-
tions of the Nomenclature Committee of the International
Union of Biochemistry and Molecular Biology on the
nomenclature and classiﬁcation of enzymes (Academic
Press, San Diego, 1992), 6 edn.
[30] Albery, J. W. & Knowles, J. R.
Evolution of enzyme
function and the development of catalytic eﬃciency. Bio-


## Page 9


9
chemistry 15, 5631–5640 (1976).
[31] Heinrich, R. & Hoﬀmann, E. Kinetic parameters of en-
zymatic reactions in states of maximal activity; an evo-
lutionary approach. J. theor. Biol 151, 249–283 (1991).
[32] Berg, J., Hung, Y. P. & Yellen, G. A genetically encoded
ﬂuorescent reporter of ATP:ADP ratio. Nat. Methods 6,
161–166 (2009).
[33] Bennett, B. D. et al. Absolute metabolite concentrations
and implied enzyme active site occupancy in escherichia
coli. Nat. Chem. Biol. 5, 593–599 (2009).
[34] http://www.genome.jp/kegg/.
[35] Cho, J., King, J. S., Qian, X., Harwood, A. J. & Shears,
S. B. Dephosphorylation of 2,3-bisphosphoglycerate by
MIPP expands the regulatory capacity of the Rapoport-
Luebering glycolytic shunt. Proc. Natl Acad. Sci. USA
105, 5998–6003 (2008).
[36] Varma, A. & Palsson, B. O. Metabolic ﬂux balancing -
basic concepts, scientiﬁc and practical use. Nat. Biotech.
12, 994–998 (1994).
[37] Press, W. H., Teukolsky, S. A., Vetterling, W. T. & Flan-
nery, B. P.
Numerical Recipes: The Art of Scientiﬁc
Computing (Cambridge University Press, New York, NY,
USA, 2007), 3rd edn.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1404_2900v1_lower_glycolysis_carries_a_higher_flux_than_any_biochemically_possible_alternati
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1404_2900V1_LOWER_GLYCOLYSIS_CARRIES_A_HIGHER_FLUX_THAN_ANY_BIOCHEMICALLY_POSSIBLE_ALTERNATI.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

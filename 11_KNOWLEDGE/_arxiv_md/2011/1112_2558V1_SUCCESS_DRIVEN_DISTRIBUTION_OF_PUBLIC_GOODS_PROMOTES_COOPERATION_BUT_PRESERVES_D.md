---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1112.2558v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1112.2558v1_Success-driven_distribution_of_public_goods_promotes_cooperation_but_preserves_d

> Source: 1112.2558v1_Success-driven_distribution_of_public_goods_promotes_cooperation_but_preserves_d.pdf

> Pages: 4

---


## Page 1


arXiv:1112.2558v1  [physics.soc-ph]  12 Dec 2011
Success-driven distribution of public goods promotes cooperation but preserves defection
Matjaˇz Perc
Faculty of Natural Sciences and Mathematics, University of Maribor, Koroˇska cesta 160, SI-2000 Maribor, Slovenia
Established already in the Biblical times, the Matthew effect stands for the fact that in societies rich tend to get
richer and the potent even more powerful. Here we investigate a game theoretical model describing the evolution
of cooperation on structured populations where the distribution of public goods is driven by the reproductive
success of individuals. Phase diagrams reveal that cooperation is promoted irrespective of the uncertainty by
strategy adoptions and the type of interaction graph, yet the complete dominance of cooperators is elusive due to
the spontaneous emergence of super-persistent defectors that owe their survival to extremely rare microscopic
patterns. This indicates that success-driven mechanisms are crucial for effectively harvesting beneﬁts from
collective actions, but that they may also account for the observed persistence of maladaptive behavior.
PACS numbers: 89.75.Fb, 87.23.Ge, 89.75.Hc
The Gospel of St. Matthew states: “For to all those who
have, more will be given.”
Roughly two millennia latter
sociologist Robert K. Merton [1] was inspired by this writ-
ing and coined the term “Matthew effect” for explaining dis-
crepancies in recognition received by eminent scientists and
unknown researchers for similar work. A few years earlier
physicist and information scientist Derek J. de Solla Price [2]
actually observed the same phenomenon when studying the
network of citations between scientiﬁc papers, only that he
used the phrase cumulative advantage for the description. To
most physicists, however, preferential attachment will be best
known due to the seminal paper by Barab´asi and Albert [3],
who used the concept ingeniously to explain the emergence of
scaling in growing random networks. Other common varia-
tions of the phrase include rich-get-richer and success-breeds-
success [4], all implying that initial advantages are often self-
amplifying and tend to snowball over time. No matter the
wording, be it the accumulation of wealth [5] or citations [6],
the making of new friends [7], or the longevity of one’s ca-
reer [8], this simple yet fascinatingly powerful phenomenon
arguably inﬂuences many facets of our existence.
In this paper we investigate how the Matthew effect affects
the evolution of cooperation in the public goods game. The
public goods game [9, 10] is played in groups and captures the
essential social dilemma in that collective and individual in-
terests are in dissonance. Players must decide simultaneously
whether they wish to contribute to the common pool or not.
All the contributions are then multiplied to take into account
synergetic effects of cooperation, and the resulting amount is
divided equally among all group members irrespective of their
initial decision. From the perspective of each individual, de-
fection is clearly the rational decision to make as it yields the
highest personal income if compared to other members of the
group. However, if nobody decides to invest the group fails
to harvest the beneﬁts of a collective investment and the soci-
ety evolves towards the “tragedy of the commons” [11]. The
sustenance of cooperation in sizable groups of unrelated indi-
viduals, as is the case by the public goods game, is particularly
challenging since group interactions tend to blur the trails of
those who defect. Unlike by pairwise interactions, reciprocity
[12, 13] often fails as it is not straightforward to determine
whom to reciprocate with. Social enforcement, on the other
hand, may work well, although it is challenged by the fact
that it is costly (see [14] for a review). Other prominent ways
of promoting cooperation in public goods games include the
introduction of volunteering [15], social diversity by means
of complex interaction networks [16], heterogeneous wealth
distributions [17], and institutionalized punishment [18].
Inspired by the seminal works on games on coevolution-
ary and social networks [19–23], the most recent advances on
this topic [24–28] (see [29] for a review), as well as the seem-
ing omnipresence of the Matthew effect in social interactions,
we consider the public goods game where the distribution of
multiplied contributions is not equally shared amongst all the
group members, but rather it depends on the evolutionary suc-
cess of each individual. Naturally, the more successful an in-
dividual is the higher its share of the public good.
Assuming structured interactions, L2 players are arranged
into overlapping groups of size G such that every player is
surrounded by its G −1 nearest neighbors. Accordingly, each
individual belongs to g = G different groups. Initially each
player on site x is designated either as a cooperator (sx = C)
or defector (sx = D) with equal probability. Cooperators
contribute a ﬁxed amount (here considered being equal to 1
without loss of generality) to the public good while defectors
contribute nothing. The sum of all contributions in each group
is multiplied by the factor r > 1 and the resulting public goods
are distributed amongst all the group members. If sx = C the
payoff of player x from every group g is P g
C = MxrN g
C/G−1
and if sx = D the payoff is P g
D = MxrN g
C/G, where N g
C is
the number of cooperators in group g while Mx is the fac-
tor by means of which the Matthew effect is introduced. Ini-
tially all players have Mx = 1, and so without further mod-
iﬁcations the setup returns the classical spatial public goods
game [30]. Here, however, each time player x successfully
enforces its strategy on another player y, Mx = Mx + ∆and
My = My −∆, where ∆> 0 is a free parameter. Thus, in the
next round player x will receive a higher share of the public
goods while player y will receive, to the same extent, a smaller
one. Note that since the fact that player x was able to enforce
its strategy on player y already implies that the former is more
successful, this simple coevolutionary rule will strengthen this


## Page 2


2
10
-3
10
-2
10
-1
10
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
1.0
  K=0.1
  K=0.3
  K=0.8
 
R
-5
0
5
0.0
0.2
0.4
0.6
0.8
1.0
payoff difference
0
G/2
G
-G/2
-G
 
 
w
FIG. 1: (Color online) Critical R at the D →C +D phase transition
in dependence on ∆for three different values of K. Success-driven
distribution of public goods strongly decreases the multiplication fac-
tor needed for cooperation to survive, irrespective of K. Inset depicts
the probability of strategy adoption w in dependence on the payoff
difference for the three K [same color (gray scale) as in the main
panel]. Square lattice with G = 5 was used as the interaction graph.
further whilst at the same time additionally degrading player
y, thus concisely introducing the Matthew effect into the pub-
lic goods game. Importantly, the coevolutionary rule is strat-
egy independent and at no point in time assumes any public
goods being lent or not spent, i.e., L−2 P
x Mx = 1 at all
times.
Monte Carlo simulations are carried out comprising the
following elementary steps. A randomly selected player x
plays the public goods game with its G partners as a mem-
ber of all the g = 1, . . . , G groups, whereby its overall pay-
off is thus Psx = P
g P g
sx. Next, player x chooses one of
its nearest neighbors at random, and the chosen co-player y
also acquires its payoff Psy in the same way. Finally, player
x enforces its strategy sx onto player y with a probability
w(sx →sy) = 1/{1 + exp[(Psy −Psx)/GK]}, where K
quantiﬁes the uncertainty by strategy adoptions due to errors
in decision making or incomplete information (see inset of
Fig. 1), and G normalizes the effect for different interaction
graphs [30]. Each Monte Carlo step (MCS) gives a chance for
every player to enforce its strategy onto one of the neighbors
once on average. The average frequencies of cooperators (ρC)
and defectors (ρD) were determined in the stationary state af-
ter sufﬁciently long relaxation times. Depending on the actual
conditions (proximity to phase transition points and the typ-
ical size of emerging spatial patterns) the linear system size
was varied from L = 200 to 1600 and the relaxation time was
varied from 104 to 107 MCS to ensure proper accuracy.
In Fig. 1 we plot the critical value of r, deﬁned as the min-
imally required R = r/G (note that the normalization with
G enables comparisons with results on graphs other than the
square lattice [30]) where ρC ﬁrst becomes > 0, in depen-
dence on ∆. It can be observed that the stronger the Matthew
effect, the lower the multiplication factor needed for the sus-
tenance of cooperation. This holds irrespective of K. While
10
-3
10
-2
10
-1
10
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
RRG
G=5
sqaure lattice
G=5
triangular lattice
G=7
 
R
FIG. 2: (Color online) Critical R at the D →C + D phase transi-
tion in dependence on ∆for three different interaction graphs. In-
sets show the graphs schematically in the color (symbol type) cor-
responding to the results in the main panel, with the group size G
indicated for vertices encircled red (gray). As in Fig. 1 the promo-
tion of cooperation is clearly inferable, irrespective of the properties
of the interaction graph. Here K = 0.1 was used in all three cases.
The dashed orange line shows the result as predicted by the mean-
ﬁeld approximation (see main text for details).
∆= 0.001 essentially returns the classical version of the
game, with the same R as reported in [30], a sharp descent
towards as low as R = 0.17 follows for larger ∆. The ef-
fect saturates and may even revert slightly when ∆becomes
comparable to G, which is due to the fact that Mx must not ex-
ceed G since all the accumulated public goods within a group
are then already assigned to player x. To test the generality
of the observed promotion of cooperation further, we plot in
Fig. 2 the critical R for three different interaction graphs (see
insets) with very distinct properties that are know to vitally
affect the evolution of cooperation [31]. Namely, a regular
graph with zero clustering coefﬁcient (square lattice), a regu-
lar graph with a high clustering coefﬁcient (triangular lattice),
and a random regular graph having no local structure. Irre-
spective of these details the Matthew effect promotes cooper-
ation equally well, as can be concluded from the descending
R(∆) phase transition lines.
An inspection of the stationary distribution of Mx values
for intermediate ∆reveals a double peaked Gaussian with
maxima approximately at −G/2 and G/2 respectively. This
is easily traced back to the nature of the Matthew effect
in that it segregates the population into successful (peaked
around G/2) and unsuccessful (peaked around −G/2) play-
ers. What is more intriguing is the observed promotion of
cooperation, which was in the past typically associated with
strongly heterogeneous (e.g. power law or exponential) dis-
tributions, whereby it was argued that the high-impact (in
our case equivalent to high Mx) players stabilize cooperation
while defectors are doomed by means of a negative feedback
effect [31]. This well-known explanation applies only par-
tially in our case. In fact, here cooperators beneﬁt also from
the dynamical reshaping of the evolutionary landscape (de-


## Page 3


3
10
-3
10
-2
10
-1
10
0
0.125
0.25
0.5
1
2
4
8
16
64
256
1024
4096
10
-6
10
-5
10
-4
10
-3
10
-2
10
-1
C
+D
C
C+D
D
 
R
 
 
D
MCS
FIG. 3: (Color online) Strategy regions in the ∆−R parameter space
for the square lattice at K = 0.1. While R needed for cooperation
to survive decreases steadily with increasing ∆(solid red line), the
opposite holds for the extinction of defectors. The transition to the
pure C region (dotted green line) is preceded by the emergence of a
peculiar C+D region (dashed blue line), where a minute fraction of
defectors is able to survive in the presence of dominating coopera-
tors. The inset shows two characteristic time courses for just above
[dashed green line (top arrow at R = 1.5)] and below [solid blue
line (bottom arrow at R = 1.47)] the C+D →C transition line
for ∆= 0.001. Within the C+D region defectors utilize their one-
in-a-million survival chance to evade extinction. Although in the
inset only the ﬁrst 4096 MCS are depicted, we have veriﬁed that at
R = 1.47 ρD > 0 for up to 107 MCS at L = 1600 system size. The
dashed black line in the inset is proportional to MCS−1.
ﬁned by Mx), which renders the defective strategy maladap-
tive and thus gives way to a mixed C + D phase. This can
be conﬁrmed analytically by means of a simple well-mixed
approximation of our model. Namely, by plugging into the
well-mixed ansatz [32] ˙ρC = ρC(1 −ρC)(PC −PD) the pay-
offs as deﬁned above, treating NC/G as ρC and introducing
Gaussian distributed values ξ with standard deviation σ for
the difference in M (as motivated by the observed distribu-
tion of Mx values), we obtain ˙ρC = ρC(1 −ρC)(rρCξ −1).
Following a ﬁrst-order small-noise expansion [33] we ﬁnally
have ˙ρC = ρC(1 −ρC)(σ2rρC(ρC −3ρ2
C/2) −1). From
˙ρC = 0 and the sign of the second derivative we ﬁnd ρC = 0
and ρC = 1 as unstable steady states. The new stable steady
state of ρC comes from σ2rρC(ρC −3ρ2
C/2) = 1 (the poly-
nomial has three roots, two of which complex conjugates),
which however is to cumbersome to be expressed here explic-
itly. What is relevant is that one obtains r ∝σ−0.5 for the
D →C + D phase transition, which can be veriﬁed easily by
straightforward numerical integration of ˙ρC. Since we lost G
in the well-mixed approximation r may be rescaled to account
for R as obtained from Monte Carlo simulations and σ takes
on the role of ∆. Preserving the slope of the dependence this
yields the dashed orange line depicted in Fig. 2. While it is
by no means implied that this approximation gives a good ﬁt
to the Monte Carlo simulations, it nevertheless conﬁrms the
effect by means of a simple analytically treatable model.
The promotion of cooperation, however, is only one ob-
10
2
10
3
10
4
10
5
10
6
10
7
-4
-2
0
2
4
-G
* 
* 
* 
* 
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
G
 
 
M
x
MCS
*
*
*
*
 
 
 
 
*
*
*
*
*
*
*
*
 
 
 
 
*
*
*
*
*
*
*
*
 
 
 
FIG. 4: (Color online) Uppermost panel shows time courses of
Mx for the “super-persistent” defector (solid black), its four near-
est neighbors (dashed red), its four next-nearest neighbors (dash-
dotted green) and the four next-next-nearest neighbors (dotted blue).
The three middle panels depict gray-scale coded (white maximal,
black minimal) values of Mx around the “super-persistent” defec-
tor at times corresponding to the vertical dashed lines in the upper-
most panel. Colored stars serve the identiﬁcation of the neighbors
corresponding to the colors (shades of gray) used in the uppermost
panel. The bottommost row depicts possible conﬁgurations of de-
fectors (gray) around the “super-persistent” defector (black). Re-
sults were obtained on a square lattice of linear size L = 1600 at
K = 0.1, R = 1.47 and ∆= 0.001.
servation following from the introduction of the Matthew ef-
fect. There is another, namely the preservation of defectors
to be demonstrated below, which is rooted in extremely rare
small-region effects originating from the spatiality of the con-
sidered model. Figure 3 depicts the strategy regions in the
∆−R parameter space for the square lattice, from where the
peculiar behavior can be inferred. In particular, as the crit-
ical R inducing D →C + D falls, the critical R required
for C + D →C raises sharply with increasing ∆. Extensive
Monte Carlo simulations using L = 1600 reveal a narrow in-
termediate region denoted as C+D, where the most minute
fraction of defectors can prevail indeﬁnitely in the sea of co-
operators. The inset features two time courses just above and
below the C+D →C transition line (see arrows in the main
panel). What at ﬁrst appears to be algebraically slow relax-
ation (marked by the dashed line in the inset) is facilitated by
the coevolutionary impact of the Matthew effect to become ei-
ther an absorbing C region (green) or the C+D region (blue),
where approximately one defector is able to survive amongst
106 cooperators (note that the temporal courses are averages
over 10 independent realizations). We also note that we use


## Page 4


4
region rather than phase for the C + D →C+D →C tran-
sitions since we were unable to completely resolve the large
system size limit.
Zooming in on the neighborhoods around these “super-
persistent” defectors gives vital clues with regards to their sur-
vival. Figure 4 shows the time evolution of Mx for one such
defector and its neighbors. Evidently, it is possible, although
highly unlikely, that isolated defectors become fully protected
by their neighbors by means of the spontaneous emergence
of successive microscopic hierarchies (expressed in terms of
Mx) in space. The three middle panels show that while the
central player (defector) enjoys the beneﬁts of the highest pos-
sible Mx, its four nearest neighbors have the lowest possible
Mx associated to them. Further crucial is then the fact that
all the neighbors of the four nearest neighbors, like the central
defector, also all eventually acquire the highest possible Mx.
This makes it impossible for the four potential donors of the
new strategy to the central defector to overtake it. Even though
they may occasionally succeed in adopting the cooperative
strategy, it is impossible to enforce the latter onto the central
defector because they are at an inherent disadvantage due to
the unfavorable outcome of the Matthew effect in their imme-
diate neighborhood. Consequently, the only possible conﬁgu-
rations (showing defectors only) around the “super-persistent”
defector are those depicted in the bottom row of Fig. 4, with
zero chances of full cooperator dominance. It is to be em-
phasized that although one defector amongst a million co-
operators seems negligible, from the evolutionary viewpoint
it nevertheless preserves the seed for defection to take on a
more dominant role should the conditions ever become more
favorable. From the view point of statistical mechanics, it is
fascinating to learn that coevolutionary rules may, due to the
interplay of spatial structure and the dynamics of the coevolv-
ing quantity, induce spatially extremely localized microscopic
patterns that prevent phase transitions into absorbing states
despite the fact that the strategy destined to die out is com-
pletely maladaptive (note that in the absence of the Matthew
effect cooperators reach full dominance on the square lattice
at R ≈1.1 [30]).
In sum, we have demonstrated that a simple strategy-
independent coevolutionary rule mimicking the Matthew ef-
fect promotes cooperation in group interactions amongst unre-
lated individuals. This can be partially attributed to the emer-
gent Gaussian distribution of factors determining the distri-
bution of public goods, but also to the inability of defectors
(or their lesser ability if compared to cooperators) to adapt
to continuously changing evolutionary landscapes, as demon-
strated by an analytically treatable well-mixed approximation.
However, the Matthew effect may also give rise to spatially
highly localized microscopic patterns that protect maladaptive
strategies despite of their obvious evolutionary disadvantage,
thus preventing absorbing phases and preserving an option of
a comeback of seemingly exterminated traits. We hope that
this work will inspire further research in the yet unexplored
directions concerning the impact of coevolutionary rules on
the outcome of games governed by group interactions.
This research was supported by the Slovenian Research
Agency (grants Z1-2032 and J1-4055).
[1] R. K. Merton, Science 159, 53 (1968).
[2] D. J. de Solla Price, Science 149, 510 (1965).
[3] A.-L. Barab´asi and R. Albert, Science 286, 509 (1999).
[4] L. Egghe and R. Rousseau, J. Am. Soc. Inf. Sci. 46, 426 (1995).
[5] A. Smith, The Wealth of Nations (Methuen and Co., London,
1904).
[6] S. Redner, Phys. Today 58, 49 (2005).
[7] A. Tomkins, J. Novak, and R. Kumar, KDD’06, 611 (2006).
[8] A. M. Petersen, W.-S. Jung, J.-S. Yang, and H. E. Stanley, Proc.
Natl. Acad. Sci. USA 108, 18 (2011).
[9] K. Sigmund, The Calculus of Selﬁshness (Princeton University
Press, 2010).
[10] M. A. Nowak, Evolutionary Dynamics (Harvard University
Press, 2006).
[11] G. Hardin, Science 162, 1243 (1968).
[12] R. Axelrod, The Evolution of Cooperation (Basic Books, New
York, 1984).
[13] M. A. Nowak and K. Sigmund, Nature 393, 573 (1998).
[14] K. Sigmund, Trends Ecol. Evol. 22, 593 (2007).
[15] C. Hauert, S. De Monte, J. Hofbauer, and K. Sigmund, Science
296, 1129 (2002).
[16] F. C. Santos, M. D. Santos, and J. M. Pacheco, Nature 454, 213
(2008).
[17] J. Wang, F. Fu, and L. Wang, Phys. Rev. E 82, 016102 (2010).
[18] K. Sigmund, H. D. Silva, A. Traulsen, and C. Hauert, Nature
466, 861 (2010).
[19] G. Abramson and M. Kuperman, Phys. Rev. E 63, 030901(R)
(2001).
[20] H. Ebel and S. Bornholdt, Phys. Rev. E 66, 056118 (2002).
[21] M. G. Zimmermann, V. Egu´ıluz, and M. S. Miguel, Phys. Rev.
E 69, 065102(R) (2004).
[22] V. M. Equ´ıluz, M. G. Zimmermann, C. J. Cela-Conde, and
M. S. Miguel, Am. J. Sociology 110, 977 (2005).
[23] J. M. Pacheco, A. Traulsen, and M. A. Nowak, Phys. Rev. Lett.
97, 258103 (2006).
[24] T. Wu, F. Fu, and L. Wang, Phys. Rev. E 80, 026121 (2009).
[25] A. Cardillo, J. G´omez-Garde˜nes, D. Vilone, and A. S´anchez,
New J. Phys. 12, 103034 (2010).
[26] G. Zschaler, A. Traulsen, and T. Gross, New J. Phys. 12, 093015
(2010).
[27] S. Lee, P. Holme, and Z.-X. Wu, Phys. Rev. Lett. 106, 028702
(2011).
[28] J. G´omez-Garde˜nes, M. Romance, R. Criado, D. Vilone, and A.
S´anchez, Chaos 21, 016113 (2011).
[29] M. Perc and A. Szolnoki, BioSystems 99, 109 (2010).
[30] A. Szolnoki, M. Perc, and G. Szab´o, Phys. Rev. E 80, 056109
(2009).
[31] G. Szab´o and G. F´ath, Phys. Rep. 446, 97 (2007).
[32] J. Hofbauer and K. Sigmund, Evolutionary Games and Popula-
tion Dynamics (Cambridge University Press, 1998).
[33] W. Horsthemke and R. Lefever, Noise-Induced Transitions
(Springer Verlag, Berlin, 1984).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1112_2558v1_success_driven_distribution_of_public_goods_promotes_cooperation_but_preserves_d
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2011/1112_2558V1_SUCCESS_DRIVEN_DISTRIBUTION_OF_PUBLIC_GOODS_PROMOTES_COOPERATION_BUT_PRESERVES_D.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

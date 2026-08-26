---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1502.00726v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1502.00726v2_The_context-dependence_of_mutations__a_linkage_of_formalisms

> Source: 1502.00726v2_The_context-dependence_of_mutations__a_linkage_of_formalisms.pdf

> Pages: 9

---


## Page 1


arXiv:1502.00726v2  [q-bio.QM]  22 Apr 2015
The context-dependence of mutations: a linkage
of formalisms
Frank J. Poelwijk ∗1, Vinod Krishna ∗2, and Rama Ranganathan†1
∗Green Center for Systems Biology, UT Southwestern Medical Center, 6001 Forest Park Road, Dallas, TX 75235, USA, and †Departments of Biophysics and Pharmacology
and Green Center for Systems Biology, UT Southwestern Medical Center, 6001 Forest Park Road, Dallas, TX 75235, USA
1To whom correspondence should be addressed. E-mail: poelwijk@gmail.com or rama.ranganathan@utsouthwestern.edu
2 Present address: Janssen Pharmaceuticals Research & Development, 1400 McKean Road, Spring House, PA 19454
Deﬁning the extent of epistasis – the non-independence of the ef-
fects of mutations – is essential for understanding the relationship of
genotype, phenotype, and ﬁtness in biological systems. The applica-
tions cover many areas of biological research, including biochemistry,
genomics, protein and systems engineering, medicine, and evolution-
ary biology. However, the quantitative deﬁnitions of epistasis vary
among ﬁelds, and its analysis beyond just pairwise eﬀects remains
obscure in general. Here, we show that diﬀerent deﬁnitions of epis-
tasis are versions of a single mathematical formalism - the weighted
Walsh-Hadamard transform. We discuss that one of the deﬁnitions,
the backgound-averaged epistasis, is the most informative when the
goal is to uncover the general epistatic structure of a biological sys-
tem, a description that can be rather diﬀerent from the local epistatic
structure of speciﬁc model systems. Key issues are the choice of ef-
fective ensembles for averaging and to practically contend with the
vast combinatorial complexity of mutations. In this regard, we dis-
cuss possible approaches for optimally learning the epistatic structure
of biological systems.
There has been much recent interest in the prevalence of
epistasis in the relationships between genotype, phenotype,
and ﬁtness in biological systems [1–7]. Epistasis here is deﬁned
as the non-independence (or context-dependence) of the eﬀect
of a mutation, which is a generalization of Bateson’s original
deﬁnition of epistasis as a genetic interaction in which a mu-
tation ’masks’ the eﬀect of variation at another locus [8]. It
is also in line with Fisher’s broader deﬁnition of ’epistacy’ [9].
Epistasis limits our ability to predict the function of a system
that harbors several mutations given knowledge of the eﬀects
of those mutations taken independently [10–13], and makes
these relationships increasingly more complex [14–19]. From
an evolutionary perspective, the presence of epistatic inter-
actions may limit or entirely preclude trajectories of single-
mutation steps towards peaks in the ﬁtness landscape [20–29].
With regard to human health, epistasis complicates our un-
derstanding of the origin and progression of disease [30–37].
Thus, interest in the extent of epistatic interactions in bio-
logical systems has originated from the ﬁelds of protein bio-
chemistry, protein engineering, medicine, systems biology, and
evolutionary biology alike.
Originally epistasis was considered in the context of two
genes,
but we can deﬁne it more broadly as the non-
independence of mutational eﬀects in the genome, whether
the eﬀects are within, between, or even outside protein coding
regions (e.g. in regulatory regions). The perturbations may
go beyond point mutagenesis, but we limit the discussion here
for clarity of presentation. Importantly, the deﬁnition of epis-
tasis can be extended beyond pairwise eﬀects to comprise a
hierarchy of 3-way, 4-way, and higher-order terms that repre-
sent the complete theoretical description of epistasis between
the parts that make up a biological system.
How can we quantitatively assign an epistatic interaction
given experimentally determined eﬀects of mutations? Since
epistasis is deviation from independence, it is crucial to ﬁrst
explicitly state the null hypothesis: asserting what exactly it
means to have independent contributions of mutations. This
by itself can be non-trivial. In some cases the phenotype is
directly related to a thermodynamic state variable, and the
issue is then straightforward: independence implies additivity
in the state variable. For example, for equilibrium binding re-
actions between two proteins, independence means additivity
in the free energy of binding ∆Gbind, such that the energetic
eﬀect of a double mutation is the sum of the energetic ef-
C
y100
y100
A
B
y10
y11
y 1
0
y00
y0
y1
y000
0
y 1
0
y111
y101
y110
y 11
0
y 1
00
Fig. 1.
Representation of (A) single mutant, (B) double mutant, and (C) triple
mutant experiments. Phenotypes are denoted by yg, where g is the underlying geno-
type. g = {gN, ..., g1} with gi ∈{0, 1}; ’0’ or ’1’ indicates the state of the
mutable site (e.g., amino acid position). The eﬀect of a single, double, triple muta-
tion is given by the red arrows. Pairwise (or second-order) epistasis is deﬁned as the
diﬀerential eﬀect of a mutation depending on the background in which it occurs, for
example in (B) it is the degree to which the eﬀect of one mutation (e.g. y10 −y00)
deviates in the background of the second mutation (y11−y01). Thus, the expression
for second order epistasis is (y11 −y10)−(y01 −y00). The third order and higher
cases are considered in the main text,
fects of each single mutation taken independently. However,
in general, many phenotypes cannot be so directly linked to a
thermodynamic state variable, and quantiﬁcation of epistasis
needs to be accompanied by a proper rationale for the choice
of null hypothesis. In what follows we will assume this step
has already been carried out and we will equate independence
with additivity of mutational eﬀects. Epistasis between two
mutations is then deﬁned as the degree to which the eﬀect of
both mutations together diﬀers from the sum of the eﬀects of
the single mutations.
In this paper, we describe three theoretical frameworks that
have been proposed for characterizing the epistasis between
components of biological systems; these frameworks originate
in diﬀerent ﬁelds and use seemingly diﬀerent calculations to
describe the non-independence of mutations [14,24,33,38–46].
We show that these formalisms are diﬀerent manifestations
of a common mathematical principle, a ﬁnding that explains
their conceptual similarities and distinctions. Each of these
formalisms has its value depending on depth of coverage and
nature of sampling in the experimental data, and the purpose
of the analysis. In the end, the fundamental issue is to de-
velop practical approaches for optimally learning the epistatic
structure of biological systems in the face of explosive combi-
natorial complexity of possible epistatic interactions between
mutations. Demonstrating the mathematical relationships be-
tween the diﬀerent frameworks for analyzing epistasis is a ﬁrst
key step in this process.
Results
Basic deﬁnitions We begin with a formal deﬁnition of geno-
type, phenotype, and the representation of mutational eﬀects.
Consider a speciﬁc sequence comprised of N positions as a bi-
nary string g = {gN, ..., g1} with gi ∈{0, 1}, where ’0’ and ’1’
represent the ”wild-type” and mutant state of each position,
respectively. This deﬁnes a total space of 2N genotypes. The
analysis could be expanded to the case of multiple substitu-
tions per position, but we consider just the binary case for
clarity here. Each genotype g has an associated phenotype
yg, which is of the form that the independent action of two
1


## Page 2


mutations means additivity in y. For notational simplicity, we
will simply write the genotype in a k-bit binary form, where
k is the order of the mutations that are considered. For ex-
ample, the eﬀect of a single mutation is simply y1 −y0, the
diﬀerence in the phenotype between the mutant and wild-type
states (Fig. 1A). The eﬀect of a double mutant is given by
y11 −y00 (red arrow, Fig. 1B), and its linkage through paths
of single mutations is deﬁned by a two-dimensional graph (a
square network) with four total genotypes. Similarly, a triple
mutant eﬀect is y111 −y000 (red arrow, Fig. 1C), and its link-
age through paths of single mutations are enumerated on a
three-dimensional graph (a cube) with eight total genotypes.
More generally, and as described by Horowitz and Fersht [47],
the phenotypic eﬀect of any arbitrary n-dimensional mutation
can be represented by an n-dimensional graph, with 2n total
genotypes. Understanding the relationship of the phenotypes
of multiple mutants to that of the underlying lower-order mu-
tant states is the essence of epistasis, and is described below.
The biochemical view of epistasis A well-known approach in
biochemistry for analyzing the cooperativity of amino acids in
specifying protein structure and function is to use the formal-
ism of thermodynamic mutant-cycles [10,47–49], one manifes-
tation of the general principle of epistasis. In this approach,
the ”phenotype” is typically an equilibrium free energy ∆G
(e.g. of thermodynamic stability or biochemical activity), and
the goal is to obtain information about the structural ba-
sis of this phenotype through mutations that represent sub-
tle perturbations of the wild-type state.
For pairs of mu-
tations, the analysis involves measurements of four variants:
wild-type (y00 = ∆G
o
0 ), each single mutant (y01 = ∆G
o
1 and
y10 = ∆G
o
2 ), and the double mutant (y11 = ∆G
o
1,2), where
the subscripts designate the mutated positions, and the su-
perscript ’o’ indicates free energy relative to a standard state
(Fig. 1B).
From this, we can compute a coupling free energy between
the two mutations (∆2G1,2) as the degree to which the eﬀect of
one mutation (∆
1G1) is diﬀerent when tried in the background
of the other mutation (∆
1G1|2):
∆
2
G1,2 = ∆
1
G1|2 −∆
1
G1
= (∆G
o
1,2 −∆G
o
2 ) −(∆G
o
1 −∆G
o
0 )
[1]
Whereas the ∆G
o terms are individual measurements and ∆
1G
terms are the eﬀects of single mutations relative to wild-type,
∆
2G is a second order epistatic term describing the coopera-
tivity (or non-independence) of two mutations with respect to
the wild-type state. This analysis can be expanded to higher
order. For example, the third order epistatic term describing
the cooperative action of three mutations 1, 2, and 3 (∆
3G1,2,3)
is deﬁned as the degree to which the second order epistasis of
any two mutations is diﬀerent in the background of the third
mutation:
∆
3
G1,2,3 = ∆
2
G1,2|3 −∆
2
G1,2
= ∆G
o
1,2,3 −
3
X
i<j
∆G
o
i,j +
3
X
i
∆G
o
i −∆G
o
0
[2]
Note that ∆
3G requires measurement of eight individual geno-
types (Fig. 1C). More generally, we can deﬁne an n-th order
epistatic term (∆
nG), describing the cooperativity of n muta-
tions,
∆
n
G1,...,n = ∆G
o
1,...,n + (−1)1
n
X
i1<i2<...<in−1
∆G
o
i1,i2,...,in−1
+ (−1)2
n
X
i1<i2<...<in−2
∆G
o
i1,i2,...,in−2 + . . . + (−1)n∆G
o
0
[3]
It is possible to write this expansion in a compact matrix form:
¯γ = G¯y
[4]
where ¯γ is the vector of 2n epistasis terms of all orders, and ¯y
is the vector of 2n free energies corresponding to phenotypes of
all the individual variants listed in binary order. To illustrate,
for three mutations n = 3, and we obtain










γ000
γ001
γ010
γ011
γ100
γ101
γ110
γ111










=










1
0
0
0
0
0
0
0
−1
1
0
0
0
0
0
0
−1
0
1
0
0
0
0
0
1 −1 −1
1
0
0
0
0
−1
0
0
0
1
0
0
0
1 −1
0
0 −1
1
0
0
1
0 −1
0 −1
0
1
0
−1
1
1 −1
1 −1 −1
1










∗










y000
y001
y010
y011
y100
y101
y110
y111










In this representation, subscripts in ¯y represent combinations
of mutations (e.g. y011 = ∆G
o
1,2, a double mutant) and sub-
scripts in ¯γ represent epistatic order (e.g. γ011 = ∆
2G1,2, pair-
wise epistasis between mutations 1 and 2). Thus, equations 1
and 2 correspond to multiplying ¯y by the fourth or eighth row
of G, respectively, to specify γ011 and γ111. Note that ¯y and ¯γ
contain precisely the same information, re-written in a diﬀer-
ent form. The matrix G represents an operator linking these
two representations of the mutation data and we will return
to the nature of the operation in a later section. We can write
a recursive deﬁnition for G that deﬁnes the mapping between
¯y and ¯γ for all epistatic orders n:
Gn+1 =
 Gn
0
−Gn
Gn

with
G0 = 1
[5]
The inverse mapping is deﬁned by ¯y = G−1¯γ. This relation-
ship gives the eﬀect of any combination of mutants (in ¯y) as
a sum over epistatic terms (in ¯γ). For example, the energetic
eﬀect of three mutations 1,2, and 3 (∆G o
1,2,3 = y111) is:
∆G
o
1,2,3 = ∆
3
G1,2,3 +
3
X
i<j
∆
2
Gi,j +
3
X
i
∆
1
Gi + ∆G
o
0
[6]
Thus, in the most general case, the free energy value of a mul-
tiple mutation requires knowledge of the eﬀect of the single
mutations and all associated epistatic terms. For the triple
mutant, this means the wild-type phenotype, the three sin-
gle mutant eﬀects, the three two-way epistatic interactions,
and the single three-way epistatic term. This analysis high-
lights two important properties of epistasis: (1) the lack of any
epistatic interactions between mutations dramatically simpli-
ﬁes the description of multiple mutations to just the sum over
the underlying single mutation eﬀects, and (2) the absence of
lower-order epistatic interactions (e.g. ∆
2Gi,j = 0) does not
imply absence of higher order epistatic terms.
The ensemble view of epistasis In contrast to the biochemi-
cal deﬁnition, the signiﬁcance of a mutation (and its epistatic
interactions) may also be deﬁned not solely with regard to a
single reference state as the ”wild-type”, but as an average
over many possible genotypes. As we show below, such aver-
aging better represents the epistatic level at which mutations
operate, and in principle, can separate mutant eﬀects that are
idiosyncratic to particular genotypes from those that are fun-
damentally important. The concept of averaging epistasis over
genotypic backgrounds is analogous to the idea of the ’schema
average ﬁtness’ in the ﬁeld of genetic algorithms (GA) [50,51],
which was recently introduced in biology [45].
In its complete form, background-averaged epistasis con-
siders averages over all possible genotypes for the remaining
positions in the ensemble. For example, if n = 3, the epista-
sis between two positions 1 and 2 is computed as an average
over both states of the third position (ε∗11, with the averaging
denoted by ’∗’) (see. Fig. 1C):
ε∗11 = 1
2

[(y111 −y110) −(y101 −y100)]
+ [(y011 −y010) −(y001 −y000)]

[7]
2


## Page 3


Thus for n = 3, we can write all epistatic terms:










ε∗∗∗
ε∗∗1
ε∗1∗
ε∗11
ε1∗∗
ε1∗1
ε11∗
ε111










= V ∗










1
1
1
1
1
1
1
1
1 −1
1 −1
1 −1
1 −1
1
1 −1 −1
1
1 −1 −1
1 −1 −1
1
1 −1 −1
1
1
1
1
1 −1 −1 −1 −1
1 −1
1 −1 −1
1 −1
1
1
1 −1 −1 −1 −1
1
1
1 −1 −1
1 −1
1
1 −1










∗










y000
y001
y010
y011
y100
y101
y110
y111










where V is a diagonal weighting matrix to account for averag-
ing over diﬀerent number of terms as a function of the order
of epistasis; vii = (−1)qi/2n−qi, where qi is the order of the
epistatic contribution in row i. More generally, for any number
of mutations n:
¯ε = V H ¯y.
[8]
where ¯y is the same vector of phenotypes of variants as deﬁned
above, ¯ε is the vector of background averaged epistatic terms,
and H is the operator for background-averaged epistasis, de-
ﬁned recursively as
Hn+1 =
 Hn
Hn
Hn −Hn

with
H0 = 1
[9]
The recursive deﬁnition for the weighting matrix V is
V n+1 =
 1
2V n
0
0
−V n

with
V 0 = 1
[10]
The matrix H has special signiﬁcance; its action mathemat-
ically corresponds to a generalized Fourier analysis [52] known
as the Walsh-Hadamard transform. This converts the pheno-
types of individual variants (in ¯y) into a vector of averaged
epistasis (in ¯ε), an operation that can also be seen as a spectral
analysis of the high-dimensional phenotypic landscape deﬁned
by the genotypes studied. In this transform, the phenotypic
eﬀects of combinations of mutations are represented as sums
over averaged epistatic terms.
In summary, the deﬁnition of epistasis proposed in evolu-
tionary genetics is a global deﬁnition over sequence space, av-
eraging the epistatic eﬀects of mutations over the ensemble of
all possible variants. In contrast, the biochemical deﬁnition
given in the previous section is a local one, treating a partic-
ular variant as a reference for determining the epistatic eﬀect
of mutations.
Estimating epistasis with linear regression A third approach
for analyzing epistasis is linear regression. For example, when
we have a complete dataset of phenotypes of all 2n genotypes,
we can use regression to deﬁne the extent to which epistasis
is captured by only considering terms to some order r < n.
That is, whether terms up to the rth order are suﬃcient for
eﬀectively capturing the full complexity of a biological system.
The standard form for a linear regression is a set of equations:
yg = β0+
n
X
i=1
βigi+
n
X
i<j
βijgigj+
n
X
i<j<k
βijkgigjgk+...+ǫg [11]
for each genotype g. The β terms denote the regression co-
eﬃcients corresponding to the (epistatic) eﬀects between sub-
scripted positions, and ǫg is the residual noise term. In matrix
form this can be written as
¯y = X ¯β + ¯ǫ.
[12]
where X tabulates which regression coeﬃcients are summed
over for genotypes g. For n = 3, regressing to full order, we
can write










y000
y001
y010
y011
y100
y101
y110
y111










=










1
0
0
0
0
0
0
0
1
1
0
0
0
0
0
0
1
0
1
0
0
0
0
0
1
1
1
1
0
0
0
0
1
0
0
0
1
0
0
0
1
1
0
0
1
1
0
0
1
0
1
0
1
0
1
0
1
1
1
1
1
1
1
1










∗










β000
β001
β010
β011
β100
β101
β110
β111










+ ¯ǫ
following the same rule for subscripts as before. X has the
recursive deﬁnition:
Xn+1 =
 Xn
0
Xn Xn

with
X0 = 1
[13]
It is worth noting that the inverse of X is X−1 = G, the
operator for biochemical epistasis (Eq. 5; see Supplementary
Information). Thus, the multi-dimensional mutant-cycle anal-
ysis is indistinguishable from regression to full order – the case
in which r = n and ¯ǫ = 0.
However, the usual aim of regression is to approximate the
data with fewer coeﬃcients than there are data points, i.e.,
r < n. To express this, we simply remove the columns from
X that refer to the epistatic orders excluded from the regres-
sion (i.e., > r): X is multiplied by an 2n-by-m matrix Q, the
identity matrix with columns corresponding to epistatic orders
higher than r removed. m is the number of epistatic terms up
to r and is given by m = Pr
i=0
 n
i

. Thus for regression to
order r, we can deﬁne ˆ
X = XQ, and write
¯y = ˆ
X ˆβ + ˆǫ.
[14]
The linear regression is performed by solving the so-called nor-
mal equations
ˆβ = ( ˆ
X
T ˆ
X)−1 ˆ
X
T ¯y
[15]
where ˆ
X
T ˆ
X is necessarily square and invertible as long as ˆ
X
is full column rank and hence ˆ
X
T ˆ
X is full rank. Note that
in this analysis we compute epistatic terms only up to the
rth order, but use phenotype/ﬁtness data of all 2n combina-
tions of mutants. The more general case in which we estimate
epistatic terms with less than 2n data points is distinct and is
discussed below.
If the biochemical deﬁnition of epistasis is a local one, ex-
ploring the coupling of mutations of all order with regard to
one ”wild-type” reference, and the ensemble view of epistasis
is a global one, assessing the coupling of mutations of all order
averaged over all possible genotypes, then the regression view
of epistasis is an attempt to project to a lower dimension -
capturing epistasis as much as possible with low-order terms.
Link between the formalisms The analysis presented above
leads to a simple unifying concept underlying the calculations
of epistasis.
In general, all the calculations are a mapping
from the space of phenotypic measurements of genotypes ¯y to
epistatic coeﬃcients ¯ω, in a general form ¯ω = Ωepi ¯y, where
Ωepi is the epistasis operator. We give the bottom line of the
diﬀerent operators below; their formal mathematical deriva-
tions can be found in the Supplementary Information.
The most general situation is that of the background-
averaged epistasis with averaging over the complete space of
possible genotypes. In this case
Ωepi = V H,
[16]
where H is a 2n × 2n matrix corresponding to the Walsh-
Hadamard transform (n is the number of mutated sites) and
V is a matrix of weights to normalize for the diﬀerent num-
bers of terms for epistasis of diﬀerent orders. The biochemical
deﬁnition of epistasis using one ”wild-type” sequence as a ref-
erence is a sub-sampling of terms in the Hadamard transform.
In this case
Ωepi = V XT H,
[17]
where X is, as deﬁned in Eq. 13. In essence, XT picks out
the terms in H that concern the wild-type background. Note
that both these mapping are one-to-one, such that the number
of epistatic terms (in ¯ω) is equal to the number of phenotypic
measurements (in ¯y) and no information is lost. In contrast,
regression to lower orders necessarily implies fewer epistatic
3


## Page 4


T-2
H372
G330
B
A
T-2 F
G330T
H372A
0.8 ± 0.09 
22.1 ± 2.6 
36 ± 2.1 
0.5 ± 0.05 
1.8 ± 0.33 
2.2 ± 0.33 
1.9 ± 0.3 
26.9 ± 6.3 
Fig. 2.
Example of three-way epistasis in the aﬃnity of a PDZ binding domain
for its ligand. A) In blue the PSD95-PDZ3 domain, and in orange its ligand peptide
positioned in the binding pocket. The positions under consideration are shown as
space-ﬁlling spheres. B) Measured Kd values in µM for all eight combinations of two
amino acids at the three mutable positions.
terms than data points, which means the mapping is com-
pressive and information is lost. In this case
Ωepi = V XT SH,
[18]
where S (≡QQT ) is the identity matrix but with zeros on the
diagonal at the orders that are higher than which we regress
over.
The fundamental point is that all three formalisms for
computing epistasis are just versions of the Walsh-Hadamard
transform, with terms selected as appropriate for the choice
of a single reference sequence or limitations on the order
of epistatic terms considered.
From a computational point
of view, it is interesting to note that regression using the
Hadamard transform makes matrix inversion unnecessary
(compare with Eq. 15).
An empirical example: a cooperative mechanism in a PDZ
domain To illustrate the diﬀerent analyses of epistasis, we
consider a small case study of three spatially proximal muta-
tions that deﬁne a switch in ligand speciﬁcity in PSD95-PDZ3,
a member of the PDZ family of protein interaction modules
(Fig. 2A). Two mutations are in PSD95-PDZ3 (G330T and
H372A), and one mutation in its cognate ligand peptide (T-
2F). The phenotype is the binding aﬃnity, Kd, and the ab-
sence of epistasis implies additivity in the corresponding free
energy, expressed as ∆G
o = RT lnKd in kcal mol−1. Binding
aﬃnities for this system are from ref. [53], and given in Figure
2B. These quantitative phenotypes are then transformed to
epistatic terms using Eq. 16-18 (Table 1).
A number of simple mathematical relationships are evident
in the data. First, regression is carried out only to the second-
order and therefore the third-order epistatic term for this
Table 1.
Interaction terms after applying the three diﬀerent transforms to
the PDZ-ligand dataset with three mutable positions:
three-way mutant-cycle,
background-averaged epistasis, and regression (to second order).
genotype∗
free
interaction
mutant
bg. ave.
regression
THG
energy†
term‡
cycle
epistasis
terms
¯
y
¯γ
¯ε
ˆ
β
000
−8.17
***
−8.17
−7.24
−7.96
001
−7.58
**1
0.59
−0.51
0.17
010
−6.13
*1*
2.05
0.23
1.63
011
−6.24
*11
−0.70
0.13
0.13
100
−5.96
1**
2.22
−0.41
1.80
101
−7.70
1*1
−2.33
−1.50
−1.50
110
−7.67
11*
−3.76
−2.92
−2.92
111
−8.45
111
1.67
1.67
0
∗The three mutable positions in genotypes are T-2F in the ligand, and H372A and
G330T in the protein, respectively. They are designated in this column as ’THG’.
†Measured free energies in kcal/mol, expressed as RTlnKd, at T = 293K
‡Interacting positions are in the same order as genotypes, for example ’*11’ indicates
the epistasis between amino acid positions 372 and 330 in PSD95-PDZ3.
analysis does not exist (or, equivalently, is set to zero if the
epistatic vector ˆβ is deﬁned to be of full length 2n). Second,
there are some equalities. The regression terms at the high-
est order (second, in this case) are equal to the correspond-
ing terms for the averaged epistasis.
This is because XT S
sets columns corresponding to orders higher than the regres-
sion order to zero, leaving rows corresponding to the highest
regression order with only one non-zero element, on the di-
agonal. For these rows the entries in the epistasis operators
V XT SH and V H are equal. Another more trivial equality is
the highest-order term for the mutant-cycle and averaged epis-
tasis formalisms; there is only one contribution for the highest
order, and therefore no backgrounds to average over.
The data also illustrate the key properties of the diﬀerent
formalisms. The G330T, H372A, and T-2F mutations repre-
sent a collectively cooperative set of perturbations, as indi-
cated by a signiﬁcant third-order epistatic term by both mu-
tant cycle and background averaged deﬁnitions (γ111 = ε111 =
1.67 kcal mol−1). But the three formalisms diﬀer in the en-
ergetic value of the lower order epistatic terms. For example,
G330T is essentially neutral for wild-type ligand binding but
shows a dramatic gain in aﬃnity in the context of the T-2F
ligand; thus, a large second-order epistatic term by the bio-
chemical deﬁnition (γ101 = −2.33 kcal mol−1). However, the
coupling between G330T and T-2F is nearly negligible in the
background of H372A; as a consequence, the background av-
eraged second-order epistasis term ε1∗1 is smaller (−1.5 kcal
mol−1). Similarly, both biochemical and regression formalisms
assign a large ﬁrst-order eﬀect to the T-2F (1**) and H372A
(*1*) single mutations, while the corresponding background-
averaged terms are nearly insigniﬁcant. For example, the free
energy eﬀect of mutating H372A (γ010) is 2.05 kcal mol−1 in
the wild-type background, but is −1.71 kcal mol−1 in the back-
ground of the T-2F ligand mutation - a nearly complete rever-
sal of the eﬀect of this mutation depending on context. Thus
with background averaging, the ﬁrst order term for H372A
(ε∗1∗) is close to zero.
This makes sense; given the experi-
ment described in Figure 2, the H372A mutation should not
be thought of as a general determinant of ligand aﬃnity. In-
stead it is a conditional determinant, with an eﬀect that de-
pends on the identity of the amino acid at the −2 position of
the ligand. Note that the degree of averaging depends on the
number of mutated sites, and thus the interpretation of mu-
tational eﬀects will depend on the scale of the experimental
study.
These examples show that background averaging has the
eﬀect of ”correcting” mutational eﬀects for the existence of
higher-order epistatic interactions. Without background aver-
aging, the eﬀect of a mutation (at any order) idiosyncratically
depends on a particular reference genotype and will fail to
account for higher order epistasis which modulates the ob-
served mutational eﬀect.
Thus, background averaging pro-
vides a measure of the eﬀects of mutation that represents its
general value over many related systems, and more appropri-
ately represents the cooperative unit within which the muta-
tion operates.
The epistatic structure of real systems The analytical expres-
sions in Eq. 16-18 involves the measurement of phenotypes (¯y)
for all 2n combinatorial mutants, a fact that exposes two fun-
damental problems. First, it is only practical when n is small.
In such cases (e.g Figure 2, n = 3), the data can be combi-
natorially complete permitting a full analysis - the local and
global structure of epistasis, possible evolutionary trajecto-
ries, and adaptive trade-oﬀs [54]. But for the typical size of
protein domains (n ∼150), the combinatorial complexity of
mutations precludes the collection of complete datasets. Sec-
ond, even if it were possible, the sampling of all genotypes is
not desired; indeed, the majority of systems in such an ensem-
ble are unlikely to be functional and and averages over them
are not meaningful with regard to learning the epistatic struc-
ture of native systems. How then can we apply these epistasis
formalisms in practice, especially with regard to background
averaging?
4


## Page 5


1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
A
B
Fig. 3.
Examples of matrices Zp introduced to calculate the partial background-
averaged epistasis, for n = 3. (A) Z2 for when data for mutants up to second-order
is available and (B) Z1 for when only ﬁrst-order mutants are available. Both matrices
are self-similar, which allows their generation for arbitrary order, and are related to
the so-called logical Sierpiski triangle. For example Z2 = 1−AΣ, where A is the
anti-diagonal identity matrix and Σ is the Sierpinski matrix (i.e. multigrade AND in
Boolean logic) for three inputs.
To develop general principles, we begin with two obvious ap-
proaches that lead to well-deﬁned alternative expressions for
averaged epistasis. First, consider the case in which the data
are only ”locally complete”; that is, we have all possible mu-
tants up to a certain order p ≤n. We can then deﬁne a mea-
sure that is intermediate between epistasis with a single ref-
erence genotype and epistasis with full background-averaging,
which we will refer to as the partial background-averaged epis-
tasis.
For example, for three positions (n = 3) with data
complete only up to order (p = 2), the partial background-
averaged eﬀect of the ﬁrst position (rightmost subscript), is
calculated as ε∗∗1,p = (y001 −y000 +y011−y010+y101−y100)/3.
Compared to the full background-averaged epistasis, the par-
tial averages just leaves out the last term, y111 −y110, which
represents the unavailable phenotype of the triple mutant y111.
More generally, we can deﬁne this measure of epistasis as an-
other special case of the Hadamard transform:
¯εp = Wp
 Zp ◦H

¯y,
[19]
where ◦designates the element-wise product. Wp is again a
diagonal weighting vector, now given by vii = (−1)qi/Tp,qi
where qi is the epistatic order associated with row i as deﬁned
earlier, and Tp,qi = Pp−qi
j=0
 n−qi
j

. Note that p ≥qi because
mutants of order higher than p are considered absent in the
dataset.
The matrix Zp simply serves to multiply by zero the terms
in the Hadamard matrix that include orders higher than p. In-
terestingly, the Zp matrices display a self-similar hierarchical
pattern (Fig. 3) and are related to so-called Sierpinski trian-
gles (see ref [55]). This permits a recursive deﬁnition in both
n and p for the product Zp ◦H, which we will designate as
Fn,p:
Fn,p =
 Fn−1,p
Fn−1,p−1
Fn−1,p−1
−Fn−1,p−1

[20]
with Fn,p = Hn for n ≤p, and Fn,0 is a 2n × 2n matrix of
zeros, except for a 1 in the upper left corner. This analysis
assumes that data are complete up to the order p.
If not,
analytical schemes for background-averaged epistasis such as
Eqs 19-20 are not obvious.
A second analytically tractable case for incomplete data
arises in regression, where the idea is to estimate epistatic
terms up to a speciﬁed order from available data. This involves
solving a set of equations similar to the normal equations:
˜β = Q

˜
X
T ˜
X
−1 ˜
X
T M ¯y
[21]
where M is an s × 2n matrix constructed from the 2n by 2n
identity matrix by deleting the 2n −s rows corresponding to
the unavailable phenotypic data, and ˜
X = MXQ, with Q
deﬁned as above.
In order for this system of equations to
be solvable, a necessary constraint is that s ≥m; that is,
the number of data points available should be larger than or
equal to the number of regression parameters. In addition, the
data must be such that it is possible to uniquely solve for all
epistatic terms in the regression. For example, if two muta-
tions always co-occur in the data, it is obviously impossible to
calculate their independent eﬀects. In such cases, the number
of solutions to Eq. 21 is inﬁnite ( ˜
X
T ˜
X is not invertible).
In practice, even with ”high-throughput” assays, we can
only hope to measure a tiny fraction of all combinatorial mu-
tants due to the vast number of possibilities. In this situation,
the problem of inferring epistasis by regression may be fur-
ther constrained by imposing additional conditions, termed
regularization. For example, kernel ridge regression [56] and
LASSO [57] include a weighted norm of the regression coef-
ﬁcients in the minimization procedure. Regularization comes
with its own set of caveats [58], but its application is, unlike
the approaches in Eq. 19 and 21, not conditional on speciﬁc
structure of the data or depth of coverage.
However, none of these approaches directly addresses the
problem of optimally deﬁning appropriate ensembles of geno-
types over which averages should be taken. In principle, the
idea should be to perform background averaging over a rep-
resentative ensemble of systems that show invariance of func-
tional properties of interest. How can we generally ﬁnd such
ensembles without the impractical notion of exhaustive func-
tional analysis of the space of possible genotypes? One idea
is motivated by the empirical ﬁnding of sparsity in the pat-
tern of key epistatic interactions within biological systems.
Indeed, evidence suggests that in proteins, the architecture is
to have a small subset of amino acids that shows strong and
distributed epistatic couplings surrounded by a majority of
amino acids that are more weakly and locally coupled [59–63].
More generally, the notion of a sparse core of strong couplings
surrounded by a milieu of weak couplings has been argued to
be a signature of evolvable systems [64].
If it can be more
generally veriﬁed, the notion of sparsity might be exploited to
deﬁne relevant strategies for optimally learning the epistatic
structure of natural systems. One approach is to minimize the
so-called ℓ1-norm (the sum of absolute values of the epistatic
coeﬃcients) in a constrained optimization, which has the ef-
fect of producing many epistatic coeﬃcients with zero or very
small values [57], while projecting onto background-averaged
epistatic terms:
min
¯ε
||¯ε||1 subject to ¯y = H−1V −1¯ε
[22]
This procedure is akin to the technique of compressed sens-
ing [65], a powerful approach used in signal processing to rec-
ognize the low-dimensional space in which the relevant features
of a high-dimensional dataset occur given the assumption of
sparsity of these features. The application of this theory for
mapping biological epistasis has to our knowledge not been
reported before, but might be explored with focused high-
order mutational analyses in speciﬁc well-chosen model sys-
tems.
The necessary technologies for such experiments are
now becoming available, and should help deﬁne practical data
collection strategies for studying epistasis more generally.
It is worth pointing out that other approaches that use
ensemble-averaged information to understand biological sys-
tems have been developed and experimentally tested. For ex-
ample, statistical methods that operate on multiple sequence
alignments of proteins [63, 73] calculate quantities related to
epistasis that are averaged over the space of homologous se-
quences.
Importantly, these approaches have been success-
ful at revealing a hierarchy of cooperative interactions be-
tween amino acids that range from local structural contacts
in protein tertiary structures [74,75] to more global functional
modes [63].
For deﬁning good experimental approaches to
epistasis, a conceptual advance may come from an attempt to
formally map the constrained optimization problem described
in Eq. 22 to the kind of ensemble averaging that underlies the
statistical coevolution approaches.
Discussion
A fundamental problem is to deﬁne the epistatic structure
of biological systems, which holds the key to understanding
5


## Page 6


how phenotype arises from genotype. Here we provide a uni-
ﬁed mathematical foundation for epistasis in which diﬀerent
approaches are found to be versions of a single mathemati-
cal formalism - the weighted Walsh-Hadamard transform. In
the most general case, this transform corresponds to an aver-
aging of mutant eﬀects over all possible genetic backgrounds
at every order order of epistasis. This approach corrects the
eﬀect of mutations at every level of epistasis for higher or-
der terms. Importantly, it represents the degree to which the
eﬀects of mutations are transferable from one model system
to another, the usual purpose of most mutagenesis studies.
In contrast, the thermodynamic mutant cycle [47] (commonly
used in biochemistry) constitutes a special case of taking a sin-
gle reference genotype and thus no averaging [59,66–71]. This
analysis represents the eﬀects of mutations that are speciﬁc
to a particular model system. Regression (commonly used in
evolutionary biology) is an attempt to capture features of a
system with epistatic terms up to a deﬁned lower order, often
to bound the extent of epistasis or to predict the eﬀects of
higher-order combinations of mutations [72]. The similarity
of the regression operator to that of the mutant cycle (see Eq.
13) indicates that this approach is also focused around the
local mutational environment of a chosen reference sequence.
In general, background averaging would seem to provide the
most informative representation of the eﬀect of a mutation.
However, with the exception of very small-scale studies fo-
cused in the local mutational environment of extant systems,
it is both impractical and logically ﬂawed to collect combi-
natorially complete mutation datasets for any system. Thus,
the essence of the problem is to deﬁne optimal strategies for
collecting data on ensembles of genotypes that is suﬃcient for
discovering the biologically relevant epistatic structure of sys-
tems.
The notion of sparsity in epistasis provides a general ba-
sis for developing such a strategy, and it will be interesting
to test practical applications of this concept (e.g. Eq. 22) in
future work. Deﬁning optimal data collection strategies will
not only provide practical tools to probe speciﬁc systems, but
might guide us to principles underlying the ”design” of these
systems through the process of evolution, and help the rational
design of new systems. The mathematical relations discussed
here provide a necessary foundation to advance such under-
standing.
ACKNOWLEDGMENTS. We thank E. Toprak, K. Reynolds, and members of the
Ranganathan laboratory for critically reading the manuscript. FJP gratefully acknowl-
edges funding by the Helen Hay Whitney Foundation sponsored by the Howard Hughes
Medical Institute. RR acknowledges support from the Robert A. Welch Foundation
(I-1366, R.R.) and the Green Center for Systems Biology.
1. Wells JA (1990) Additivity of mutational eﬀects in proteins. Biochemistry 29:8509.
2. Phillips PC (2008) Epistasis–the essential role of gene interactions in the structure and
evolution of genetic systems. Nat Rev Genet 9:855.
3. Costanzo M, Baryshnikova A, Myers CL, Andrews B, Boone C (2011) Charting the
genetic interaction map of a cell. Curr Opin Biotechnol 22:66.
4. Lehner B (2011) Molecular mechanisms of epistasis within and between genes. Trends
Genet 27:323.
5. Dowell RD, Ryan O, Jansen A, Cheung D, Agarwala S, et al. (2010) Genotype to
phenotype: a complex problem. Science 328:469.
6. Lunzer M, Golding GB, Dean AM (2010) Pervasive cryptic epistasis in molecular evo-
lution. PLoS Genet 6:e1001162.
7. Kryazhimskiy S, DushoﬀJ, Bazykin GA, Plotkin JB (2011) Prevalence of epistasis in
the evolution of inﬂuenza A surface proteins. PLoS Genet 7:e1001301.
8. Bateson W (1908) Facts limiting the theory of heredity. Science 26:647.
9. Fisher RA (1918) The correlation between relatives on the supposition of Mendelian
inheritance. Trans R Soc Edinb 52:399.
10. Horovitz A (1987) Non-additivity in protein-protein interactions. J Mol Biol 196:733.
11. Cordes MH, Davidson AR, Sauer RT (1996) Sequence space, folding and protein de-
sign. Curr Opin Struct Biol 6:3.
12. Horovitz A, Bochkareva ES, Yifrach O, Girshovich AS (1994) Prediction of an inter-
residue interaction in the chaperonin GroEL from multiple sequence alignment is con-
ﬁrmed by double-mutant-cycle analysis. J Mol Biol 238:133.
13. Dill KA (1997) Additivity principles in biochemistry. J Biol Chem 272:701.
14. Jain RK, Ranganathan R (2004) Local complexity of amino acid interactions in a
protein core. Proc Natl Acad Sci USA 101:111.
15. Lander ES, Schork NJ (1994) Genetic dissection of complex traits. Science 265:2037.
16. Pettersson M, Besnier F, Siegel PB, Carlborg O (2011) Replication and explorations
of high-order epistasis using a large advanced intercross line pedigree. PLoS Genet
7:e1002180.
17. Kouyos RD, Leventhal GE, Hinkley T, Haddad M, Whitcomb JM, et al. (2012) Ex-
ploring the complexity of the HIV-1 ﬁtness landscape. PLoS Genet 8:e1002551.
18. Brem RB, Kruglyak L (2005) The landscape of genetic complexity across 5,700 gene
expression traits in yeast. Proc Natl Acad Sci USA 102:1572.
19. Ehrenreich IM, Torabi N, Jia Y, Kent J, Martis S, et al. (2010) Dissection of genetically
complex traits with extremely large pools of yeast segregants. Nature 464:1039.
20. Burch CL, Chao L (2004) Epistasis and its relationship to canalization in the RNA
virus phi 6. Genetics 167:559.
21. Weinreich DM, Watson RA, Chao L (2005) Perspective: Sign epistasis and genetic
constraint on evolutionary trajectories. Evolution 59:1165.
22. Poelwijk FJ, Kiviet DJ, Weinreich DM, Tans SJ (2007) Empirical ﬁtness landscapes
reveal accessible evolutionary paths. Nature 445:383.
23. Poelwijk FJ, Tˇanase-Nicola S, Kiviet DJ, Tans SJ (2011) Reciprocal sign epistasis is a
necessary condition for multi-peaked ﬁtness landscapes. J Theor Biol 272:141.
24. Lozovsky ER, Chookajorn T, Brown KM, Imwong M, Shaw PJ, et al. (2009) Stepwise
acquisition of pyrimethamine resistance in the malaria parasite. Proc Natl Acad Sci
USA 106:12025.
25. Maharjan RP, Ferenci T (2013) Epistatic interactions determine the mutational path-
ways and coexistence of lineages in clonal Escherichia coli populations.
Evolution
67:2762.
26. Draghi JA, Plotkin JB (2013) Selection biases the prevalence and type of epistasis
along adaptive trajectories. Evolution 67:3120.
27. VanderSluis B, Bellay J, Musso G, Costanzo M, Papp B, et al. (2010) Genetic inter-
actions reveal the evolutionary trajectories of duplicate genes. Mol Syst Biol 6:429.
28. Natarajan C, Inoguchi N, Weber RE, Fago A, Moriyama H, et al. (2013) Epistasis
among adaptive mutations in deer mouse hemoglobin. Science 340:1324.
29. Gong LI, Suchard MA, Bloom JD (2013) Stability-mediated epistasis constrains the
evolution of an inﬂuenza protein. eLife 2:e00631.
30. Ashworth A, Lord C, Reis-Filho J (2011) Genetic interactions in cancer progression
and treatment. Cell 145:30.
31. Chakravarti A, Clark AG, Mootha VK (2013) Distilling pathophysiology from complex
disease genetics. Cell 155:21.
32. Leiserson MDM, Eldridge JV, Ramachandran S, Raphael BJ (2013) Network analysis
of GWAS data. Curr Opin Genet Dev 23:602.
33. Hinkley T, Martins J, Chappey C, Haddad M, Stawiski E, et al. (2011) A systems
analysis of mutational eﬀects in HIV-1 protease and reverse transcriptase. Nat Genet
43:487.
34. Combarros O, Cortina-Borja M, Smith AD, Lehmann DJ (2009) Epistasis in sporadic
Alzheimer’s disease. Neurobiol Aging 30:1333.
35. Fitzgerald JB, Schoeberl B, Nielsen UB, Sorger PK (2006) Systems biology and com-
bination therapy in the quest for clinical eﬃcacy. Nat Chem Biol 2:458.
36. Fu W, O’Connor TD, Akey JM (2013) Genetic architecture of quantitative traits and
complex diseases. Curr Opin Genet Dev 23:678.
37. Wang X, Fu AQ, McNerney ME, White KP (2014) Widespread genetic epistasis among
cancer genes. Nature Comm 5:4828
38. Chen J, Stites WE (2001) Higher-order packing interactions in triple and quadruple
mutants of staphylococcal nuclease. Biochemistry 40:14012.
39. Frisch C, Schreiber G, Johnson CM, Fersht AR (1997) Thermodynamics of the inter-
action of barnase and barstar: changes in free energy versus changes in enthalpy on
mutation. J Mol Biol 267:696.
40. Jiang C, Hwang YT, Wang G, Randell JCW, Coen DM, et al. (2007) Herpes simplex
virus mutants with multiple substitutions aﬀecting DNA binding of UL42 are impaired
for viral replication and DNA synthesis. J Virol 81:12077.
41. Natarajan M, Lin KM, Hsueh RC, Sternweis PC, Ranganathan R (2006) A global
analysis of cross-talk in a mammalian cellular signalling network. Nat Cell Biol 8:571.
42. Weinreich DM, Delaney NF, Depristo MA, Hartl DL (2006) Darwinian evolution can
follow only very few mutational paths to ﬁtter proteins. Science 312:111.
43. Aita T, Iwakura M, Husimi Y (2001) A cross-section of the ﬁtness landscape of dihy-
drofolate reductase. Protein Eng 14:633.
44. Kinney JB, Murugan A, Callan CG, Cox EC (2010) Using deep sequencing to charac-
terize the biophysical mechanism of a transcriptional regulatory sequence. Proc Natl
Acad Sci USA 107:9158.
45. Weinreich DM, Lan Y, Wylie CS, Heckendorn RB (2013) Should evolutionary geneti-
cists worry about higher-order epistasis? Curr Opin Genet Dev 23:700.
46. Szendro IG, Schenk MF, Franke J, Krug J, de Visser JAGM (2013) Quantitative anal-
yses of empirical ﬁtness landscapes. J Stat Mech 2013:P01005.
47. Horovitz A, Fersht AR (1990) Strategy for analysing the co-operativity of intramolec-
ular interactions in peptides and proteins. J Mol Biol 214:613.
48. Horovitz A (1996) Double-mutant cycles: a powerful tool for analyzing protein struc-
ture and function. Fold Des 1:R121.
49. Horovitz A, Fersht AR (1990) Co-operative interactions during protein folding. J Mol
Biol 224:733.
50. Goldberg D (1989) Genetic Algorithms and Walsh Functions: Part I, A Gentle Intro-
duction. Complex Systems 3:129.
51. Beer T (1981) Walsh transforms. American Journal of Physics 49:466.
52. Stoﬀer DS (1991-06-01) Walsh-Fourier analysis and its statistical applications. Journal
of the American Statistical Association 86:461.
53. McLaughlin RN, Poelwijk FJ, Raman A, Gosal WS, Ranganathan R (2012) The spatial
architecture of protein function and adaptation. Nature 491:138.
54. Hartl DL (2014) What can we learn from ﬁtness landscapes?
Curr Opin Microbiol
21:51.
55. Sierpinski W (1915) Sur une courbe dont tout point est un point de ramiﬁcation. CR
hebd Acad Science Paris 160:302.
56. Hastie T, Tibshirani R, Friendman J (2009) The Elements of Statistical Learning, 2nd
ed. New York: Springer Publishing. Springer Series in Statistics.
6


## Page 7


57. Tibshirani R (2011) Regression shrinkage and selection via the lasso: a retrospective.
J Roy Stat Soc: Ser B 73:273.
58. Otwinowski J, Plotkin JB (2014) Inferring ﬁtness landscapes by regression produces
biased estimates of epistasis. Proc Natl Acad Sci USA 111:E2301.
59. Sadovsky Y, Yifrach O (2007) Principles underlying energetic coupling along an al-
losteric communication trajectory of a voltage-activated K+ channel. Proc Natl Acad
Sci USA 104:19813.
60. Shi L, Kay LE (2014) Tracing an allosteric pathway regulating the activity of the HslV
protease. Proc Natl Acad Sci USA 111:2140.
61. Ruschak AM, Kay LE (2012) Proteasome allostery as a population shift between in-
terchanging conformers. Proc Natl Acad Sci USA 109:E3454.
62. Luque I, Leavitt SA, Freire E (2002) The linkage between protein folding and func-
tional cooperativity: two sides of the same coin?. Ann Rev Biophys Biomol Struct
31:235.
63. Halabi N, Rivoire O, Leibler S, Ranganathan R (2009) Protein sectors: evolutionary
units of three-dimensional structure. Cell 138: 774.
64. Kirschner M, Gerhart J (1998) Evolvability. Proc Natl Acad Sci USA 95:8420.
65. Cand`es EJ, Wakin MB (2008) An introduction to compressive sampling. IEEE Signal
Proc Mag 25:21.
66. Zaremba SM, Gregoret LM (1999) Context-dependence of amino acid residue pairing
in antiparallel -sheets. J Mol Biol 291:463.
67. Shepherd TR, Hard RL, Murray AM, Pei D, Fuentes EJ (2011) Distinct ligand speci-
ﬁcity of the Tiam1 and Tiam2 PDZ domains. Biochemistry 50:1296.
68. Yifrach O, MacKinnon R (2002) Energetics of pore opening in a voltage-gated K+
channel. Cell 111:231.
69. Hidalgo P, MacKinnon R (1995) Revealing the architecture of a K + channel pore
through mutant cycles with a peptide inhibitor. Science 268:307.
70. Carter PJ, Winter G, Wilkinson AJ, Fersht AR (1984) The use of double mutants to
detect structural changes in the active site of the tyrosyl-tRNA synthetase (Bacillus
stearothermophilus). Cell 38:835.
71. Ranganathan R, Lewis JH, MacKinnon R (1996) Spatial localization of the K+ channel
selectivity ﬁlter by mutant cycle-based structure analysis. Neuron 16:131.
72. Hinkley T, Martins J, Chappey C, Haddad M, Stawiski E, Whitcomb JM, Petropoulos
CJ, Bonhoeﬀer S (2011) A systems analysis of mutational eﬀects in HIV-1 protease
and reverse transcriptase. Nat Genetics 43:487.
73. Marks DS, Hopf T, Sander C (2012) Protein structure prediction from sequence vari-
ation. Nat. Biotechnol 11:1072.
74. Morcos F, Pagnani A, Lunt B, Bertolino A, Marks DS, Sander C, Zecchina R, Onuchic
JN, Hwa T, Weigt M (2011) Direct-coupling analysis of residue coevolution captures
native contacts across many protein families. Proc Natl Acad Sci 108:E1293.
75. Skerker JM, Perchuk BS, Siryaporn A, Lubin EA, Ashenberg O, Goulian M, Laub MT
(2008) Rewiring the speciﬁcity of two-component signal transduction systems. Cell
133:1043.
7


## Page 8


Supplementary Information: Proofs and extended methods
A. Expressing the biochemical epistasis operator G as a Hadamard transform:
G = X
−1 = V XTH
(Eq. 17)
First we write the diﬀerent matrix operators in their recursive form, and then proceed by induction. We have for the re-
cursive form of X:
Xn+1 =
 Xn
0
Xn
Xn

with
X0 = 1
In order to ﬁnd the generative function for the inverse X
−1 we can write Xn+1X
−1
n+1 = I:
 Xn
0
Xn
Xn

X
−1
n+1 =
 I
0
0
I

,
which we can solve by Gauss-Jordan elimination:
 Xn
0
I
0
Xn
Xn
0
I

⇒
 
I
0
X
−1
n
0
I
I
0
X
−1
n
!
⇒
 
I
0
X
−1
n
0
0
I
−X
−1
n
X
−1
n
!
hence we have for the inverse of X:
X
−1
n+1 =
 
X
−1
n
0
−X
−1
n
X
−1
n
!
with
X
−1
0
= 1
Which is identical to the recursive form for G:
Gn+1 =

Gn
0
−Gn
Gn

We further have:
Hn+1 =
 Hn
Hn
Hn
−Hn

with
H0 = 1
and V n+1 =
 1
2V n
0
0
−V n

with
V 0 = 1
With the above relations we can derive the equality in the main text expressing G as a Hadamard transform:
Gn = X
−1
n
= V nXT
n Hn
For n = 0 the statement is trivial. We now show by induction that this relation holds for all n.
Gn+1 =

Gn
0
−Gn
Gn

=

V nXT
n Hn
0
−V nXT
n Hn
V nXT
n Hn

=
 1
2V n
0
0
−V n
  2XT
n Hn
0
XT
n Hn
−XT
n Hn

=
 1
2V n
0
0
−V n
  XT
n
XT
n
0
XT
n
  Hn
Hn
Hn
−Hn

= V n+1XT
n+1Hn+1
QED
B. Expressing the regression operator as a Hadamard transform:
Q

ˆ
X
T ˆ
X
−1 ˆ
X
T = V XT SH
(Eq. 18)
We will use ˆ
X = XQ and S = QQT as deﬁned in the main text.
8


## Page 9


For the right-hand side we can write
V XT SH =
1
2n V XT (HH) SH
where we used H2
n = 2nIn, which can be proven straightforwardly by induction using the generative function for H.
Rearranging and using X
−1 = V XT H, we obtain
V XT SH =
1
2n X
−1 (HSH)
We thus have to prove
Q

ˆ
X
T ˆ
X
−1 ˆ
X
T =
1
2n X−1 (HSH)
Left-multiplying both sides by ˆ
X
T X (mind the hat is only on the ﬁrst operator) and right-multiplying by H we are left
to prove
ˆ
X
T H = ˆ
X
T HS
Left-multiplication by Q yields
SXT H = SXT HS
which, again using the relation we proved in section A above, can be rewritten as
SV −1X−1 = SV −1X−1S
or
SX−1 = SX−1S
given the commutative properties of diagonal matrices S and V −1.
This equality indicates that setting certain rows of X−1 to zero (left-hand side) is the same as setting both those rows
and corresponding columns of X−1 to zero (right-hand side). This is obviously not true for every set of rows and columns, and
needs more discussion.
We can prove this iteratively starting at regression to order n −1 and going down to lower order. If regression is done to
order n −1, this means that only the last row of X−1 is set to zero, and by construction of X−1 (see above) the last column
only has a non-zero element in this row. This means that in this case the equality is correct. Another way to see this is
looking at matrix G for n = 3 in its explicit representation in the main text (here G being identiﬁed with X−1) and noting
that the highest order epistatic term γ111 is the only one that receives a contribution from the highest order (n) mutant term y111.
Next, if regression is performed instead to order n −2, not only the last row of X−1 is set to zero, but also the rows
corresponding to n −1 order mutants. Analogously to above, the only terms in the vector ¯γ that receive contributions from
the n −1 order mutants are the ones in the rows corresponding to n −1 order of epistasis (since the row corresponding to nth
order is already set to zero), meaning that their corresponding column again has only one non-zero element. Hence setting
these rows to zero will directly set their corresponding column to zero, and the equality holds.
And so forth for regression to order n −3, etc., etc.
QED
9

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
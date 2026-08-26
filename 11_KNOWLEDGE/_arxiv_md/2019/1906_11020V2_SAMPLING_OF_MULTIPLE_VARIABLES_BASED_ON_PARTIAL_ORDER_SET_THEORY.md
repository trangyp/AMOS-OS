---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.11020v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1906.11020v2_Sampling_of_multiple_variables_based_on_partial_order_set_theory

> Source: 1906.11020v2_Sampling_of_multiple_variables_based_on_partial_order_set_theory.pdf

> Pages: 21

---


## Page 1


arXiv:1906.11020v2  [stat.ME]  21 Jul 2020
Sampling of multiple variables based on partial order set theory
Bardia Panahbehagh
Department of Mathematics and computer science, Kharazmi University,
Tehran, Iran, panahbehagh@khu.ac.ir; bardia.panah@gmail.com
Rainer Bruggemann
Leibniz-Institute of Freshwater Ecology and Inland Fisheries,
Berlin, Germany, brg home@web.de
Mohammad M. Salehi
Department of Mathematics, Statistics and Physics, Qatar University,
P.O. Box 2713, Doha, Qatar, salehi@qu.edu.qa
July 22, 2020
Abstract
This paper is going to introduce a new method for ranked set sampling with multiple
criteria. The method is based on a version of ranked set sampling, introduced by Panah-
behagh et al. (2017), which relaxes the restriction of selecting just one individual variable
from each ranked set. Under the new method for ranking, elements are ranked in sets based
on linear extensions in partial order sets theory, where based on all the variables simultane-
ously. Results will be evaluated by some simulations and two real case study on economical,
medicinal use of ﬂowers and the pollution of herb-layer by Lead, Cadmium, Zinc and Sulfur
in regions in the southwest of Germany.
Keywords: Multiple variables ranked set sampling; Linear extension; Partial order sets
theory; Medicinal use of ﬂowers; Environmental pollution.
1
Introduction
Ranked set sampling (RSS) was ﬁrst introduced by McIntyre (1952) and has been widely used
as a design in many applications. The idea behind RSS is appealing particularly to agricultural
and environmental scientists where identifying sampling units in the ﬁeld is straightforward but
the exact exploration measurement of the units by measurements is time consuming. Many
sampling units can be identiﬁed and within them subsets are actually measured. In RSS the
identiﬁcation of these subsets is based on ranking the units and a selection according to their
relative ranks.
The RSS technique brieﬂy involves taking random samples of size m from the population. The
sample units are ranked by some quick and easy measure. Then, one unit from each sample is
chosen and precisely measured for the character of interest. To take a sample of size m, the unit
that has the lowest rank in the ﬁrst sample (with size m) is chosen, the unit with the second
lowest rank is chosen from the second sample, and so on. This process is repeated n times,
giving a ﬁnal sample size, n. = nm. Sampling can be balanced or unbalanced where the number
of sample units selected in the ranks are not constant. With highly skewed population distri-
1


## Page 2


butions more units from low (or high) ranks can be selected. Unbalanced designs are similar in
concept to the optimal allocation in stratiﬁed sampling where strata with bigger variances, take
bigger sample fractions. RSS is reported as being more eﬃcient than simple random sampling
(Ridout, 2003; Samawi, 1996). See full reviews of RSS by Patil et al. (1999) and the related
book of Chen et al. (2004).
In this paper, based on method of Panahbehagh et al.
(2017) multivariate RSS based on
partial order sets will be introduced. In some populations there are more than one character of
interest, Patil et al. (1994) have discussed RSS for multiple variables when one of the variable
can be deﬁned as a primary variable. Ranking is based on this main primary variable only,
and if the other variables are correlated with the main one, the method will perform reasonably
well. Norris et al. (1995) have developed two approaches, one using an unbalanced allocation
process based on the Neyman allocation for the variable of primary interest, treating this as a
concomitant for the other variables of interest and the other using a design based on randomly
choosing sample units from the rank list derived from an individual variable. Al-Saleh and
Zheng (2002) as well as Chen and Shen (2003) have proposed a two-layer ranked set sampling
for the situation in which we have two main variables or two concomitant variables to rank the
data. In their methods at the ﬁrst layer, the data is ranked based on the ﬁrst variable and a
RSS sample is selected. At the second round, the ﬁrst layer RSS data will be ranked based on
the second variable and the RSS data in the second layer will be present as the ﬁnal sample.
One disadvantage of their methods is that they consider the two variables separately, and not
simultaneously. Another disadvantage is that they are requiring many initial samples to achieve
the needed sample size and also with increasing dimension of the space of variables, the size of
the needed sample will increase severely.
In this paper, applying the framework developed by Panahbehagh et al.
(2017) multivari-
ate RSS based on partial order sets will be introduced.
We demonstrate our suggested sampling technique with two environmental examples:
• The ﬁrst example deals with the estimation of mean values of ﬂower dry weight and
essence of Matricaria chamonilla, which is considered as a very important commercial
and medicinal plant in Iran and many other countries. The main part of chamomile for
medicinal purposes is the ﬂower essence and it is economically important to maximize the
oil yield. It is hardly possible to measure the eﬃciency of oil yield under all scenarios and
all suitable geographical units within Iran. Therefore sampling technique is necessary and
is performed.
• Chemical pollution in the environment is a problem which came into the focus of admin-
istration since the early eighties. Chemicals pose a hazard to humans, animals, plants,
etc. due to their toxicity. The quantiﬁcation of the hazard is however extremely diﬃcult
as uptake mechanisms, mode of toxic action, the role of chemical speciation and the state
of the environmental geographical unit are important. Therefore in almost all nations
monitoring programs were installed to observe the chemical pollution spatially and tem-
porarily. The data have mostly the unit mass of chemicals (as total concentration) mass
of the target, for example soil.
These data are thought of as surrogates expressing the hazard potential due to the consid-
ered chemicals. It is diﬃcult to obtain for example mean values of concentrations taking
2


## Page 3


into account all geographical units, especially when a temporal trend is to be monitored.
Here 59 geographical units are selected by the environmental protection agency taking
care for deﬁning the regions as homogeneous as possible with respect to the chemical
pollution processes. The sampling technique can be validated, because in that speciﬁc
case the mean values can also directly obtained from all 59 units for a speciﬁed year of
observation. When the proposed method is successful then the monitoring process can
be simpliﬁed, namely to relax the precondition of almost homogeneous geographical units
and a more elaborated locally speciﬁc monitoring can be applied.
To develop the new method, in section 2 we extend the method of Panahbehagh et al. (2017)
for multiple variables. In section 3 we introduce stratiﬁed sampling using RSS derived from
linear extensions (LE) in partial order sets (Posets). Section 4 contains examples, simulations
and two real case study to compare the methods and evaluate the results and the paper will be
ﬁnished in section 5 with a conclusion.
2
Multivariate Virtual Stratiﬁed Ranked Set Sampling (MVSR)
In multivariate RSS, we have an R dimensional random variable. We start with the basic idea
of multivariate RSS (Patil et al., 1994), ranking according to just one of the variables. Then we
adapt the design with the design of Panahbehagh et al. (2017).
Suppose that X ∼fµ with E(X) = µ, where X = (X1, X2, ..., XR) and µ = (µ1, µ2, ..., µR)
also V ar(Xj) = σ2
j , Cov(Xj, Xj′) = ρjj′σjσj′ and E(|Xj|2) < ∞for all j. Main aim is to
estimate µ. Our strategy to get a sample of size n. = nm from the population is to generate
an iid sample of Xis of size m from f and sort them according to X1 (using itself or based
on an auxiliary variable) in m columns and repeat this method K times. Then we will have a
stratiﬁed population, formed in m strata, each of size K (see table 1), just assume we have a
vector of X(h)i instead of a X(h)i, where X(h)i = (X1
(h)i, X2
[h]i, ..., XR
[h]i), and X1
(h)i is the hth order
statistics in the ith set with µ1
(h)and σ2
(h)1 as the mean and variance respectively, and Xj
[h]i for
j = 2, 3, .., R are concomitant variables with respect to X1
(h)i in ith set with µj
[h]and σ2
[h]j. Now
we get a Simple Random Sampling Without Replacement (SRSWOR) from the hth stratum of
size n (an integer smaller than K), say sh, and we can estimate µj by
bµ1
V
=
1
m
m
X
h=1
¯X1
(h),
bµj
V
=
1
m
m
X
h=1
¯Xj
[h]
where
¯X1
(h)
=
1
n
X
iǫsh
X1
(h)i,
¯Xj
[h]
=
1
n
X
iǫsh
Xj
[h]i
3


## Page 4


Theorem 1 In MVSR, bµj
V is an unbiased estimator for µj and
V (bµ1
V )
=
1
nm(σ2
1 −(1 −n
K )
m
m
X
h=1
(µ1
(h) −µ1)2),
V (bµj
V )
=
1
nm(σ2
j −(1 −n
K )
m
m
X
h=1
(µj
[h] −µj)2)
and if we assume that X1 and Xj are linked with below linear regression model
Xj
i = µj + ρ1j
σj
σ1
(X1
i −µ1) + εi
(1)
where ε is a random variable independent from X1, then
V (bµj
V ) =
1
nm(σ2
j −(1 −n
K )
m
ρ2
1j
m
X
h=1
(µj
(h) −µj)2)
and
bV (bµ1
V) =
K −1
m(mK −1)
m
X
h=1
1
n(n −1)
X
iǫsh
(X1
(h)i −¯X1
(h))2 +
1
m(mK −1)
m
X
h=1
( ¯X1
(h) −bµ1
V)2
bV (bµj
V) =
K −1
m(mK −1)
m
X
h=1
1
n(n −1)
X
iǫsh
(Xj
[h]i −¯Xj
[h])2 +
1
m(mK −1)
m
X
h=1
( ¯Xj
[h] −bµj
V)2
are unbiased estimators for the variance of variables.
For the proof of Theorem 1 see Appendix A.
As we saw, in MVSR one is selected as a leading one to perform a ranking, the others are just
adjusted which implies some errors. Therefore we introduce a method of ranking that ranks all
variables simultaneously.
3
Ranking based on Posets
In this section, we ﬁrst describe Posets theory and then introduce two new versions of multi-
variate RSS, based on them.
3.1
Posets and Linear Extensions
The application of theory of partial orders for ranking has been described by Bruggemann and
Patil (2011). In this theory, we have a set containing m elements each of them with R variables,
with a binary relation between the elements. To compare two elements of the set, if all variables
of the ﬁrst element are equal or bigger (smaller) than the second one, then the ﬁrst element is
better (≥) (worse (<)) than second one, otherwise the two elements are not comparable. Linear
extensions (LEs) are diﬀerent projections of the partial order into a complete order that respect
all the relations in the partial order set. I.e. Linear extensions are the result of order preserving
mappings. Therefore a relation x < y in a poset is preserved in all linear extensions.
We use this theory to introduce two designs; Ranking based on Posets using complete form
(or at least a random sample) of LEs (CPOR) and Ranking based on Posets using just one
random selection of LEs (RPOR):
4


## Page 5


CPOR: First rank the elements according to the mean height of the elements due to all the
possible LEs where height is deﬁned as the rank of the element in the respective LE and
then construct an unequal size population using these mean heights based on complete
LEs.
RPOR: Select one of the LEs to construct an equal size population.
We illustrate the topic with an example where we assume a set with m = 5 and R = 2 (see
table 2). The set of all LEs obtained from the data in table 2 is shown in table 3. Here, due to
the low number of linear extensions, the average height of each element can be easily directly
determined from table 3.
Generally, the determination of all linear extensions is computationally a hard problem. There-
fore the determination of average heights needs themselves sampling techniques as shown by
Bubley and Dyer (1999). However, it is not necessary to determine the set of LEs explicitly,
because only the average height is of interest. In this case, there are also pretty good approxi-
mations available, see for instance Bruggemann et al. (2004), (2013) or De Loof et al. (2013).
According to the heights of each element in LEs form, we have table 4.
We will use above theory to stratify each set in the next subsection.
3.2
CPOR
We are going to put each element of a set into a stratum equal to the nearest integer of the
mean of its height (MH). Following the previous example according to table 3, we will put the
elements of the set into 5 virtual strata (see table 5).
Then, the design proceeds as follow: an iid sample of size m (a set) from f will be generated, and
according to their variables (Xjs) all possible linear extensions will be constructed. We then
calculate the mean height (either explicitly by determination of the set of all LEs or directly
by applying approximations). Finally, using these heights, put the elements of the set into the
strata and repeat this approach K times. It is obvious that this method leads to an unequal
size stratiﬁed population.
Then instead of a R dimensional variable X{h}i = (X1
{h}i, X2
{h}i, ..., XR
{h}i) we have a R+1
dimensional variable X{h}i = (X1
{h}i, X2
{h}i, ..., XR
{h}i, MH{h}i) where MH stands for the mean
heights of the objects.
We now have a stratiﬁed population with unequal size. For the hth stratum we will take a
SRSWOR, sh, with size nh, proportional to the stratum size, Kh, where
m
P
h=1
Kh = Km such
that
m
P
h=1
nh = n. = nm. The stratiﬁed population is presented in table 6.
In table 6, X{h}i = (X1
{h}i, X2
{h}i, ..., XR
{h}i) where Xj
{h}i is the jth character of an element that
has been fallen into the hth stratum after i −1 elements, according to its mean height MH in
respective LEs. Now we propose an estimator for µj (the expectation of the jth character in f)
as
bµj
P =
m
X
h=1
Wh ¯Xj
{h}
where
Wh = Kh
Km
(2)
5


## Page 6


and
¯Xj
{h} = 1
nh
X
iǫsh
Xj
{h}i
Theorem 2 In CPOR, bµj
P is an unbiased estimator for µj.
For the proof of Theorem 2 see Appendix B.
Here instead of Neyman allocation, proportional to size is used that is easy to implement and
does not need extra information (Sarndal et al. 1992).
3.3
RPOR
RPOR is easier than CPOR to perform. Here it is just enough to select (or construct) on of the
LEs in table 3 randomly and put them in 5 strata and then we will have a stratiﬁed population,
formed in m strata, each of size K like MVSR (see table 1). Here we show the vector of ith
variable in hth stratum with X[h}i = (X1
[h}i, X2
[h}i, ..., XR
[h}i). Now we get a SRSWOR from the
hth stratum of size n (an integer smaller than K), say sh. Now we propose an estimator for µj
as
bµj
R = 1
m
m
X
h=1
¯Xj
[h}
where
¯Xj
[h} = 1
n
X
i∈sh
Xj
[h}i
Theorem 3 In RPOR, bµj
R is an unbiased estimator for µj with variance
V (bµj
R) =
σ2
j
Km + 1
m2
m
X
h=1
1 −n
K
n
EM( 1
Q
Q
X
q=1
S2
[h}qjK).
(3)
where q = 1, 2, ..., Q are all the possible combinations of LEs, with the below unbiased estimator
of variance
bV (bµj
R) =
1
nm(Km −1)[
m
X
h=1
X
iǫs[h}
(Xj
[h}i −bµj
R)2 + (K −n)
m
X
h=1
s2
[h}j].
where S2
[h}qjK and s2
[h}j are variance of hth stratum under qth combination of LEs and sample
variance of hth stratum for jth variable respectively.
For the proof of Theorem 3 see Appendix C.
3.4
Negative Correlation
When correlation between variables are strongly negative, according to Posets theory, it is
probable that most of the elements in a set are incomparable. This can make it meaningless to
stratify the sets (note that in this case most of the elements will fall in the middle stratum).
6


## Page 7


An extreme case is when the correlation between two variables is ”-1”. All the generated ele-
ments will be incomparable and in the LEs the mean height of all of them will be the same and
all will fall in the same stratum. The weight of the stratum (equation (2)) will be 1 (and the
other strata zero). Finally we will take a simple random sampling without replacement of size
n. = mn from the stratum and the design will essentially become simple random sampling with
replacement.
To overcome this problem, we suggest that if the bivariate correlations between some variables
are negative, multiple a ”-1” to some of them to change the correlations to positive. But if
we have more than two variables, sometimes it would not possible to make all the correlations
positive. In such cases, it is better to select some more important variables that we are able to
make their correlations positive. We then rank the elements using Posets theory with this new
correlations.
In Bruggemann and Patil (2011) a procedure is explained, how subsets of variables can be sys-
tematically found. The crucial concept is the number of incomparabilities of a poset. First a
sensitivity measure for each variable is to be deﬁned. The sensitivity measures the impact of
each variable on the structure of the poset (roughly: the system of comparabilities within a
poset). Secondly the variables are ordered due to their impact on a poset. Thirdly considering
ﬁrst the poset, due to the most sensitive variable, then the poset, due to the ﬁrst two most
important variables, etc the number of incomparabilities is calculated as function of the merged
variables. The resulting curve motivates to ﬁnd subsets of variables, which constitute mainly
the poset. The remaining variables are considered as ﬁne tuning, and will be ignored.
4
Simulation Study
To evaluate and compare the eﬃciency of the designs, we calculate
Eﬃciency(bµ.) =
V (¯y)
MSE(bµ.)
where ¯y is the sample mean of a simple random sample, and bµ. stands for bµV (MVSR design),
bµP (CPOR design) or bµR (RPOR design) and MSE indicate mean square error.
This section contains 3 parts:
• Comparing CPOR and RPOR with MVSR using some simulations
• Comparing CPOR and RPOR with MVSR using a real case study on medical ﬂowers
• Comparing CPOR and RPOR with MVSR using a real case study on environmental
pollution.
Also in the simulations, no matter how small was size or variance of a particular stratum, at
least one sample is dedicated to the stratum. All the simulations are done by ”R 3.1.2” software.
For the Monte Carlo simulation we have used 20000 iterations. Expectations, variances and
MSEs of the estimators are computed using Mote Carlo method.
4.1
Comparing CPOR and RPOR with MVSR using some simulations
In this part we will investigate eﬃciency of the designs that are introduced in section 2 and 3,
using bivariate normal distribution (with solving negative correlation problem).
7


## Page 8


4.1.1
Bivariate Normal distribution with negative correlation
Here we performed the simulation assuming normal distribution with negative correlation, with
n = 4, K = 8 and m = 3. As we can see in table 7, and as we asserted in Section 3.4, when
the correlation is strongly negative, CPOR and RPOR decline to simple random sampling
(eﬃciency≃1). When we convert the correlation to a positive value by changing the sign of
one variable, the eﬃciency problem will be solved (compare the results in the last two columns
with the results in the ﬁrst two columns).
4.1.2
Bivariate Normal
More complete simulations for bivariate Normal distribution are shown in table 8. For all the
cases we simulated bivariate normal with µ1 = 0, µ2 = 0, σ1 = 1, σ2 = 1 and ρ = 0.3, 0.5, 0.7, 0.9.
First note that changing ρ, does not aﬀect the eﬃciency of the ﬁrst variable which is conﬁrmed
by simulations with less than 0.02 error. As a general point, CPOR and RPOR designs increase
the eﬃciency of the estimator for both variables, simultaneously, whereas the traditional multi-
variate ranked set sampling just enhances estimation of one of the variables. As the correlations
increase, eﬃciency increase. Unlike MVSR, CPOR and RPOR had good and reasonable eﬃ-
ciency with all the correlations. Also CPOR that uses all information of LEs was more eﬃcient
than RPOR.
4.2
Comparing CPOR and RPOR with MVSR using a real case study on
medical ﬂowers
To evaluate the designs in this section we used a real case study data on chamomile ﬂower
(Panahbehagh et al. 2017) as an medicinal use of ﬂowers. We consider the population mean
of the ”Flower dry weight” (Fdw) and ”Essence” (Esn) as the two main parameters. Because
we have no information about them before sampling, and it is expensive to measure them, we
used two auxiliary variables, easy to measure with reasonable correlation with the two main
variables. For sorting Fdw, we used ”Flower height” (Fht) with correlation of 0.78 and for
Esn we used ”Number of petals” (Npt) with correlation of 0.71. Also the correlation between
Fht and Npt was 0.77. Simulation results are in table 9. As we can see in table 9, CPOR
and RPOR enhance eﬃciency of both of the estimators simultaneously. The most important
factor in eﬃciency is the portion of K/n and eﬃciency increased with increasing this factor. For
example compare two cases: one m = 5, K = 7, n = 3 and two m = 5, K = 7, n = 5, although
n is larger in the second case, because the portion of K/n is larger for ﬁrst one, the eﬃciency
of the ﬁrst case is larger than the second case. Also if the other parameters are equal, m is
the other important parameter that aﬀect eﬃciency and eﬃciency increased with increasing m.
Again CPOR was more eﬃcient than RPOR in almost all the cases.
4.3
Chemical Pollution
The Environmental Protection Agency (EPA) of the German state Baden-Wuerttemberg per-
formed a series of measurements in diﬀerent targets, for example in the herb layer, in the
epiphytic mosses of trees, in ﬁsh etc.. For this purpose the state Baden Wuerttemberg was
divided in 60 more or less homogenous regions with respect to their natural environment. The
8


## Page 9


regions are not selected according to administrative classiﬁcation but to get regions as homo-
geneous as possible with respect to environmental pollution processes.
The task was and is, to protocol the pollution due to industry, traﬃc, agrarian management
with respect to the total concentrations of Lead, Cadmium, Zinc and Sulfur (measured in mg/kg
dry mass).
According to the diﬀerent emission types there are diﬀerent chemical species, for example SO2
or solved in atmospheric droplets H2SO3, similarly the other metals as for example Pb, which
can be bounded in organic chemicals or as oxids.
The diﬀerent targets, selected by the EPA should help to diﬀerentiate among the diﬀerent trans-
port processes and to be able to trace back the emission source. So, the herb layer is mainly a
short range transport indicator, whereas the epiphytic mosses (simply: moss layer) is considered
as indicating middle range transports. The herb layer should especially indicate the loading
due to the public traﬃc whereas the moss layer may mainly indicate industrial sources.
An interesting point of geochemical research is as to how far the presence of e.g. Pb implies the
presence of Cadmium. A ﬁrst attempt in this direction can be found in a paper by Bruggemann,
Kerber, 2018 (submitted to a special issue of Comm.in Math. and in Comp. Chemistry). A
classiﬁcation approach concerning the pollution of Baden - Wuerttemberg was published by
Bruggemann et al. (2013).
4.3.1
Comparing CPOR and RPOR with MVSR using a real case study on en-
vironmental pollution
In this study, regions in Baden-Wuerttemberg, South-West of Germany were selected and mon-
itored with respect to total concentrations of the chemical elements Pb, Cd, Zn and S in the
herb layer (Environmental Protection Agency Baden-Wurttemberg (Germany) 1994, Signale
aus der Natur). The herb layer is one of the targets, selected by the Environmental Protection
Agency of Baden-Wuerttemberg. This multi-indicator system with regions as objects and con-
centrations of the four chemical elements as indicators (Bruggemann and Patil 2011) raises the
questions:
• How can we get information about the pollution status?
• What can be said about geochemical relations?
For example does an increase in pollution with respect to one pollutant,for example Pb, always
imply the increase of another pollutant, for instance Cd? For an answer from the point of
view of applied partial order theory, see Bruggemann and Voigt (2012) (For more details see
Bruggemann et al., 1996; Bruggemann et al., 1998; Bruggemann et al., 1999; Bruggemann et
al., 2003 and Bruggemann et al., 2013).
Here to give all the correlations a positive value, we multiple a ”-1”to Cd and Zn. In this
part we run two diﬀerent scenarios:
Scenario I. Selecting Pb and Zn as the two main variables with high correlation (0.60) and Cd and
S as the two main variables with low correlation (0.06). In this scenario we used perfect
ranking, and we didn’t use auxiliary variables.
Scenario II. From a chemical point of view we, selecting Cd and Pb as the two main variables and
for sorting them using two auxiliary variables; Zn with 0.48 correlation with Cd and S
with 0.27 with Pb. This is a heuristic approach.
Basically economical or sociological
information or the density of highways could also serve as auxiliary variables.
9


## Page 10


Results are shown in table 10 (Scenario I) and table 11 (Scenario II). In table 10, eﬃciency of
estimators for estimating the means of Pb and Zn with 0.6 correlation, and the means of Cd
and S with 0.06 correlation are presented. For two variables with reasonable correlation (Zn
and Pb) MVSR is not bad, because ranking just based on the ﬁrst variable, supports the second
variable.
For Cd and S, the situation is worse for MVSR, because of weak correlation around 0.06 between
them. The ﬁrst variable is not able to support the second one. Eﬃciency for S in MVSR is
around 1. But for CPOR and RPOR results for the second variable are better. With decreas-
ing eﬃciency of the ﬁrst variable (Cd) from MVRS to CPOR and RPOR, the eﬃciency of the
second variable (S) raise reasonably. Average of eﬃciency for S in MVSR is around 1.01 but in
CPOR and RPOR are around 1.09. Again, K/n is the most important parameter in eﬃciency
and after that m.
In table 11, we have used two auxiliary variables to rank the main variables. For Zn we have
used Cd with 0.48 and for Pb we have used S with 0.27 correlations. As we can see, MVRS
just improves eﬃciency of the ﬁrst variable (Cd) and CPOR and RPOR improve the both vari-
ables estimations however the improvement is not so large because of almost week correlations
between auxiliary variables and the main variables (0.48 and 0.27).
Also table 12 presents Monte Carlo expectation of the estimators that shows unbiasness of
the estimators.
By our sampling technique mean values referring to a complete set of 59 geographical units
are obtained. Clearly the regional relation is not taken into regard (which is already done by
papers mentioned above) but there is now a number available which can characterize the status
of Baden-Wrttemberg overall, and for example a time series could be done to see the general
changes with respect to the pollution.
5
Conclusion
CPOR and RPOR can be used for implement RSS in population surveys where there are multi-
ple variables of interest. CPOR and RPOR enhance the parameters estimation simultaneously
with a reasonable sample size, that most of the RSS methods can not do in multiple variables
cases. As we see in the real case studies, for CPOR and ROPR there are no need to use perfect
ranking using the main variables and it can be done using some variables, easy to measure,
with reasonable correlation with the main variables. The simulation section and real case study
conﬁrmed the assertions in the paper.
For further works, it would be beneﬁcial to ﬁnd some unbiased estimators for variance of CPOR.
Because of randomness of Kh it is not easy to calculate variance and an unbiased estimator of
variance for CPOR but as CPOR uses information of all LEs and in simulations we saw that
CPOR was more eﬃcient than RPOR in almost all the cases and maybe it is reasonable to use
variance estimator of RPOR as a conservative estimate for variance of CPOR.
Appendix A. Proving Theorem 1
10


## Page 11


Proof of the theorem is the same as Panahbehagh et al. (2017) and just please note that
here E(I[h]i) = E(I(h)i).
Appendix B. Proving Theorem 2
Here according to the sampling strategy, (i) taking an iid sample from f (a model) and
(ii) taking an stratiﬁed ﬁnite population sampling from the selected sample (a design),
we have a Model-Design based sampling, let indexes of ”M” and ”D”, mean ”according
to the Model and the Design” respectively. Then with
bµj
P =
m
X
h=1
Wh ¯Xj
{h}
where
I{h}i =



1
if Xj
{h}i is in the s{h}
0
otherwise
we have
E(bµj
P)
=
EM[ED(bµj
P|XKm)] = EM[
m
X
h=1
Kh
Km
1
nh
Kh
X
i=1
Xj
{h}iED(I{h}i|XKm)]
=
EM(
m
X
h=1
Kh
Km
1
nh
Kh
X
i=1
Xj
{h}i
nh
Kh
) =
1
KmEM(
m
X
h=1
K
X
i=1
Xj
hi) = µj
where XKm indicates whole sample of size Km.
Appendix C. Proving Theorem 3
Here the design aﬀected by two sources of variations; variation from selecting one of
the LEs and variation from selection the sample from the ﬁxed form of the stratiﬁed
population conditional on the result of the LEs which we indicate them with ”D1” and
”D2” respectively. Therefore here based on LEs assume we have XKm.q; q = 1, 2, ..., Q
and XKm.q may happen with probability Lq. Please note that Lq = 1
Q because all com-
binations of LEs happen with equal probability. Then we have
E(bµj
R) = EMED1ED2(bµj
R)
11


## Page 12


now as
ED2(I[h}i) = n
K
and
ED1ED2(bµj
R) = ED1( ¯XKm) = ¯XKm
we have
E(bµj
R) = EM[ 1
mK
m
X
h=1
K
X
i=1
Xj
hi] = µj
then E(bµj
R) = µj
R.
For variance we have
V (bµj
R) = VMED1ED2(bµj
R) + EMVD1ED2(bµj
R) + EMED1VD2(bµj
R).
It is easy to see that
VMED1ED2(bµj
V ) = σ2
j
Km
and then as VD1ED2(bµj
R) = 0 (because ED2(bµj
R) = ¯XKm is not variable respect to D1) we
have
ED1VD2(bµj
R) = 1
m2
m
X
h=1
1 −n
K
n
1
Q
Q
X
q=1
S2
[h}qjK
and therefore
V (bµj
R) = σ2
j
Km + 1
m2
m
X
h=1
1 −n
K
n
EM( 1
Q
Q
X
q=1
S2
[h}qjK).
For the unbiased estimator of the variance ﬁrst note that as we take an iid sample for
each set and rank them in m ranks then rank for each unit is distributed uniformly in
vector (1, 2, ..., m) and therefore we have
µj = E(Xj
1) = EE(Xj
1|rank(Xj
1)) = 1
m
m
X
h=1
E(Xj
1|rank(Xj
1) = h) = 1
m
m
X
h=1
µj
[h},
σ2
j
=
V E(Xj|rank(Xj)) + EV (Xj|rank(Xj))
(4)
=
V [
m
X
h=1
µj
[h}I(rank(Xj) = h)] + E[
m
X
h=1
σ2
[h}jI(rank(Xj) = h)]
=
1
m
m
X
h=1
(µj
[h} −µ)2 + 1
m
m
X
h=1
σ2
[h}j
where rank(X1) indicates rank of X1 in its selected set and I(rank(Xj
1) = h) is an
indicator function which takes 1, if rank(Xj
1) = h.
12


## Page 13


Then
E(bV (bµj
R)) =
1
nm(Km −1)[E(
m
X
h=1
X
iǫs[h}
(Xj
[h}i −bµj
R)2) + (K −n)E(
m
X
h=1
s2
[h}j)].
Now as
E(
m
X
h=1
s2
[h}j) =
m
X
h=1
EM( 1
Q
Q
X
q=1
S2
[h}qjK),
and
E(
m
X
h=1
X
iǫs[h}
(Xj
[h}i −bµj
R)2)
=
E(
m
X
h=1
X
iǫs[h}
(Xj
[h}i)2) −nmE(bµj
R)2
=
E(
m
X
h=1
K
X
i=1
(Xj
[h}i)2I[h}i) −nmV (bµj
R) −nmE2(bµj
R)
=
m
X
h=1
n
K K(σ2
[h}j + (µj
[h})2) −n
K σ2
j −1
m
m
X
h=1
(1 −n
K )EM( 1
Q
Q
X
q=1
S2
[h}qjK) −nmµ2
=
nm( 1
m(
m
X
h=1
σ2
[h}j +
m
X
h=1
(µj
[h} −µ)2)) −n
K σ2
j −1
m
m
X
h=1
(1 −n
K )EM( 1
Q
Q
X
q=1
S2
[h}qjK)
=
(nm −n
K )σ2
j −1
m
m
X
h=1
(1 −n
K )EM( 1
Q
Q
X
q=1
S2
[h}qjK)
where the last equation is based on 4, we have
E(bV (bµj
R)) = V (bµj
R)
13


## Page 14


References
Al-Saleh, M. and Zheng, G. (2002) Estimation of bivariate characterstics using ranked set sampling.
Australian & New Zealand Jurnal of Statistics, 44, 221–232.
Bruggemann, R. and Carlsen, L. (2011) An Improved Estimation of Averaged Ranks of Par-
tial Orders. MATCH Comm.Math.Comput.Chem. 65, 383–414.
Brggemann, R., Kaune, A. and Voigt. K. (1996) Vergleichende kologische Bewertung von Re-
gionen in Baden- Wrttemberg. Pages 455-467 in Landesanstalt fr Umweltschutz Baden-Wrttemberg,
ed. 4.Statuskolloquium, Projekt ”Angewandte kologie” Nr. 16. Przis-Druck Karlsruhe, Karlsruhe.
Bruggemann, R., Mucha, H.-J. and Bartel, H.-G. (2013) Ranking of Polluted Regions in South West
Germany Based on a Multi-indicator System. MATCH Commun. Math. Comput. Chem., 69,433–462.
Bruggemann, R. and Patil, G. P. (2011) Ranking and Prioritization with Multi- Indicator Sys-
tems, Introduction to Partial Order and Its Applications, Springer, New York.
Bruggemann, R., Pudenz S., Voigt K., Kaune A., and Kreimes K. (1999) An algebraic/graphical tool
to compare ecosystems with respect to their pollution. IV: Comparative regional analysis by Boolean
arithmetics. Chemosphere, 38, 2263–2279.
Bruggemann, R., Sorensen, P. B., Lerche, D. and Carlsen, L. (2004) Estimation of Averaged
Ranks by a Local Partial Order Model. J. Chem. Inf. Comp. Sc. 44, 618–625.
Bruggemann, R., Voigt, K., Kaune, A., Pudenz, S., Komossa, D., and Friedrich, J. (1998)
Vergleichende kologische Bewertung von Regionen in Baden- Wrttemberg GSF-Bericht 20/98. GSF,
Neuherberg.
Bruggemann, R., Welzl, G., and Voigt, K. (2003) Order Theoretical Tools for the Evaluation
of Complex Regional Pollution Patterns. J. Chem. Inf. Comp. Sc., 43, 1771–1779.
Bubley, R. and Dyer, M. (1999) Faster random generation of linear extensions. Discr. Math.,
201, 81–88.
Chen, Z., Bai, Z. and Sinha, B. (2004) Ranked set sampling:
theory and applications. Lecture
Notes in Statistics, Springer, New York.
Chen, Z. and Shen, L. (2003) Two-layer ranked set sampling with concomitant variables. Journal of
Statistical Planning and Inference, 115, 45–57.
David, H. A. and Nagaraja, H. N. (2003) Order Statistic, third ed. Wiley, New York.
De Loof, K., De Baets, B. and De Meyer, H. (2011) Approximation of Average Ranks in
Posets. MATCH Commun. Math. Comput. Chem., 66, 219–229.
Environmental Protection Agency Baden-Wurttemberg, (1994) Signale aus der Natur 10 Jahre
Okologisches Wirkungskataster Baden-Wurttemberg. Kraft Druck GmbH, Ettlingen
McIntyre, G. A. (1952) A method of unbiased selective sampling. using ranked sets. Australian
Journal of Agricultural Research, 3, 385–390.
Norris, R. C., Patil, G. P. and Sinha, A. K. (1995) Estimation of multiple characteristics by
ranked set sampling methods. Coenoses, 10, 95–111.
Panahbehagh, B., Bruggemann R., Parvardeh, A., Salehi, M. and Sabzalian, M. R. (2017) An
14


## Page 15


unbalanced ranked set sampling to get more than one sample from each set. Journal of Survey
Statistics and Methodology, smx026, https://doi.org/10.1093/jssam/smx026
Patil, G. P., Sinha, A. K. and Taillie, C. (1994) Ranked set sampling for multiple characteris-
tics. International Journal of Ecology and Environmental Sciences, 20, 94–109.
Patil, G. P., Sinha, A. K. and Taillie, C. (1999) Ranked set sampling:
A bibliography. Envi-
ronmental and Ecological Statistics, 6, 91–98.
Patil, G. P., Sinha, A. K. and Taillie, C. (1994) Ranked set sampling, in Handbook of Statis-
tics, Environmental Statistics, Vol. 12, G.P. Patil and C.R. Rao, eds, NorthHolland, Amsterdam.
Ridout, M. S. (2003) On ranked set sampling for multiple characterestics. Environmental and
Ecological Statistics, 10, 225–262.
Samawi, H. M. (1996) Stratiﬁed ranked set sample. Pakistan Journal of Statistics, 12, 9–16.
Sarndal, C. E., Swensson, B. and Wretman, J. (1992), Model Assisted Survey Sampling, New
York, Springer.’
Yang, S. S. (1977) General distribution theory of the concomitants of order statistics. The
Annals of Statistics, 5, 996–1002.
15


## Page 16


Table 1:
Virtual strata, using conventional RSS.
1st stratum
2nd stratum
· · ·
mth stratum
X(1)1
X(2)1
· · ·
X(m)1
X(1)2
X(2)2
· · ·
X(m)2
...
...
...
...
X(1)K
X(2)K
· · ·
X(m)K
Table 2:
Elements of a set with their variables.
X1
X2
a
0
1
b
2
1
c
1
2
d
3
3
e
0
4
Table 3: All possible LEs with respect to Posets.
LE1
LE2
LE3
LE4
LE5
LE6
LE7
LE8
d
d
d
e
d
d
d
e
c
c
e
d
b
b
e
d
b
e
c
c
c
e
b
b
e
b
b
b
e
c
c
c
a
a
a
a
a
a
a
a
16


## Page 17


Table 4:
Mean height of each element in all possible LEs.
mean height
rounded height
a
1
1
b
2.875
3
c
2.875
3
d
4.75
5
e
3.5
4
Table 5:
Putting the elements of a set in strata.
strata
1
2
3
4
5
a
b
e
d
c
Table 6:
Virtual strata, using Posets ranking.
1st stratum
2nd stratum
· · ·
mth stratum
X{1}1
X{2}1
· · ·
X{m}1
X{1}2
X{2}2
· · ·
X{m}2
...
...
...
...
...
...
· · ·
X{m}Km
X{1}K1
...
X{2}K2
Table 7: Eﬃciency of the estimators in bivariate normal case (X1, X2) ∼B.N(0, 0, 1, 1, ρ) with
solving problem of negative correlation.
ρ=-0.9
ρ=-0.5
ρ=0
ρ=-0.5→0.5
ρ=-0.9→0.9
bµ1
V
1.32
1.32
1.33
1.30
1.31
bµ1
P
1.02
1.02
1.07
1.21
1.31
bµ1
R
0.99
1.02
1.04
1.16
1.28
bµ2
V
1.26
1.08
1.01
1.10
1.25
bµ2
P
1.02
1.00
1.06
1.22
1.31
bµ2
R
0.99
1.02
1.04
1.16
1.28
17


## Page 18


Table 8: Eﬃciency of the estimators for diﬀerent cases for bivariate normal distribution.
m
K
n
ρ
variable
bµV
bµP
bµR
3
12
4
0.3
X1
1.49
1.16
1.12
X2
1.00
1.12
1.11
0.5
X1
1.45
1.20
1.17
X2
1.05
1.21
1.18
0.7
X1
1.47
1.27
1.26
X2
1.17
1.30
1.26
0.9
X1
1.49
1.41
1.39
X2
1.35
1.42
1.41
6
0.3
X1
1.31
1.13
1.10
X2
1.01
1.10
1.07
0.5
X1
1.30
1.16
1.13
X2
1.05
1.14
1.11
0.7
X1
1.33
1.23
1.19
X2
1.13
1.23
1.20
0.9
X1
1.32
1.31
1.29
X2
1.23
1.31
1.27
Table 9: Eﬃciency of the estimators for estimating the means of Fdw and Esn as the main
variables and Fht and Npl as the auxiliary variables with 0.78 and 0.71 correlations.
bµ1
V
bµ2
V
bµ1
P
bµ2
P
bµ1
R
bµ2
R
K
m
n
Fdw
Esn
Fdw
Esn
Fdw
Esn
5
3
2
1.40
1.11
1.32
1.17
1.28
1.14
3
1.23
1.07
1.18
1.06
1.18
1.07
4
1.10
1.04
1.09
1.04
1.09
1.05
5
2
1.63
1.18
1.45
1.24
1.45
1.23
3
1.35
1.10
1.26
1.11
1.24
1.13
4
1.14
1.05
1.11
1.06
1.11
1.06
7
2
1.77
1.19
1.55
1.27
1.53
1.27
3
1.40
1.10
1.29
1.12
1.30
1.14
4
1.17
1.06
1.13
1.07
1.13
1.07
7
3
3
1.36
1.09
1.26
1.15
1.25
1.13
5
1.15
1.06
1.13
1.07
1.12
1.08
6
1.09
1.03
1.07
1.03
1.06
1.03
5
3
1.58
1.16
1.43
1.22
1.40
1.20
5
1.23
1.07
1.18
1.08
1.17
1.09
6
1.10
1.03
1.08
1.04
1.08
1.04
7
3
1.71
1.19
1.53
1.25
1.51
1.24
5
1.26
1.08
1.22
1.09
1.20
1.11
6
1.12
1.04
1.09
1.05
1.09
1.05
Average
1.32
1.09
1.24
1.12
1.23
1.12
18


## Page 19


Table 10: Eﬃciency of the estimators for estimating the means of Pb and Zn with 0.6 correlation
and the means of Cd and S with 0.06 correlation. Here we used complete ranking.
bµ1
V
bµ2
V
bµ1
P
bµ2
P
bµ1
R
bµ2
R
bµ1
V
bµ2
V
bµ1
P
bµ2
P
bµ1
R
bµ2
R
m
K
n
Pb
Zn
Pb
Zn
Pb
Zn
Cd
S
Cd
S
Cd
S
3
5
2
1.32
1.11
1.13
1.21
1.12
1.15
1.36
1.01
1.13
1.09
1.12
1.09
4
1.11
1.02
1.06
1.03
1.05
1.03
1.11
1.01
1.05
1.00
1.05
1.03
7
2
1.41
1.11
1.15
1.16
1.10
1.12
1.41
0.99
1.16
1.08
1.11
1.07
4
1.25
1.08
1.11
1.10
1.09
1.10
1.16
1.01
1.00
1.01
1.03
1.06
10
2
1.59
1.16
1.24
1.25
1.16
1.17
1.53
1.04
1.22
1.12
1.19
1.11
4
1.38
1.11
1.15
1.17
1.12
1.14
1.29
1.02
1.16
1.09
1.07
1.07
5
5
2
1.61
1.21
1.23
1.27
1.18
1.23
1.53
1.02
1.19
1.12
1.15
1.10
4
1.15
1.04
1.05
1.05
1.04
1.06
1.13
1.01
1.05
1.02
1.04
1.02
7
2
1.69
1.21
1.23
1.30
1.21
1.26
1.62
1.00
1.23
1.11
1.18
1.08
4
1.35
1.14
1.14
1.15
1.13
1.16
1.33
1.00
1.12
1.04
1.09
1.04
10
2
1.93
1.28
1.31
1.37
1.24
1.34
1.78
0.99
1.28
1.13
1.21
1.12
4
1.56
1.21
1.20
1.28
1.17
1.26
1.47
1.03
1.15
1.12
1.13
1.11
7
5
2
1.69
1.21
1.26
1.31
1.21
1.28
1.63
1.04
1.26
1.18
1.21
1.19
4
1.16
1.10
1.09
1.10
1.07
1.12
1.15
0.99
1.06
1.04
1.06
1.01
7
2
1.90
1.28
1.27
1.35
1.29
1.32
1.85
1.03
1.30
1.12
1.28
1.09
4
1.45
1.19
1.19
1.19
1.17
1.20
1.37
1.02
1.17
1.07
1.17
1.07
10
2
2.20
1.36
1.40
1.49
1.39
1.49
1.99
1.02
1.40
1.19
1.31
1.15
4
1.66
1.30
1.27
1.36
1.25
1.34
1.62
1.02
1.25
1.13
1.24
1.12
Average
1.52
1.17
1.19
1.23
1.17
1.21
1.46
1.01
1.18
1.09
1.15
1.09
19


## Page 20


Table 11: Eﬃciency of the estimators for estimating the means of Cd and Pb as the main
variables and Zn and S as the auxiliary variables with 0.48 and 0.27 correlations.
bµ1
V
bµ2
V
bµ1
P
bµ2
P
bµ1
R
bµ2
R
m
K
n
Cd
Pb
Cd
Pb
Cd
Pb
3
5
2
1.31
1.01
1.07
1.03
1.02
1.02
4
1.08
1.01
0.99
0.98
1.00
1.01
7
2
1.40
0.99
1.02
1.01
1.04
1.03
4
1.20
1.00
1.00
1.00
1.02
1.01
10
2
1.46
0.99
1.04
1.02
1.03
1.03
4
1.31
0.99
1.02
1.03
1.01
1.01
5
5
2
1.48
1.00
1.07
1.05
1.04
1.05
4
1.13
1.00
1.00
1.00
1.01
1.01
7
2
1.63
1.00
1.03
1.05
1.05
1.04
4
1.31
1.00
1.01
1.04
1.03
1.04
10
2
1.82
1.01
1.06
1.09
1.07
1.07
4
1.49
1.00
1.07
1.06
1.04
1.04
7
5
2
1.62
1.02
1.07
1.10
1.06
1.08
4
1.14
1.00
1.01
1.02
1.02
1.02
7
2
1.85
1.01
1.07
1.07
1.08
1.09
4
1.37
1.01
1.03
1.04
1.05
1.05
10
2
2.05
1.01
1.09
1.08
1.08
1.07
4
1.61
1.02
1.07
1.10
1.06
1.07
Average
1.46
1.00
1.04
1.04
1.04
1.04
20


## Page 21


Table 12: Expectation of the estimators based on Scenario I.
bµ1
V
bµ2
V
bµ1
P
bµ2
P
bµ1
R
bµ2
R
bµ1
V
bµ2
V
bµ1
P
bµ2
P
bµ1
R
bµ2
R
m
K
n
Pb
Zn
Pb
Zn
Pb
Zn
Cd
S
Cd
S
Cd
S
3
5
2
0.9
132.9
0.9
132.3
0.9
132.3
0.1
1787.9
0.1
1786.0
0.1
1789.7
4
0.9
133.7
0.9
133.4
0.9
131.5
0.1
1789.7
0.1
1789.5
0.1
1788.3
7
2
0.9
134.1
0.9
132.2
0.9
134.1
0.1
1787.7
0.1
1788.4
0.1
1787.0
4
0.9
132.2
0.9
132.3
0.9
132.7
0.1
1787.9
0.1
1787.3
0.1
1788.8
10
2
0.9
132.0
0.9
132.8
0.9
133.7
0.1
1783.6
0.1
1789.3
0.1
1786.2
4
0.9
132.4
0.9
132.8
0.9
132.4
0.1
1788.4
0.1
1786.3
0.1
1785.3
5
5
2
0.9
133.3
0.9
133.3
0.9
133.8
0.1
1788.2
0.1
1788.7
0.1
1787.2
4
0.9
132.7
0.9
133.0
0.9
133.1
0.1
1787.7
0.1
1787.7
0.1
1787.1
7
2
0.9
133.3
0.9
132.8
0.9
133.1
0.1
1788.8
0.1
1787.4
0.1
1786.1
4
0.9
133.5
0.9
133.5
0.9
132.5
0.1
1788.7
0.1
1788.5
0.1
1788.1
10
2
0.9
133.8
0.9
132.9
0.9
131.9
0.1
1790.0
0.1
1787.9
0.1
1782.9
4
0.9
132.7
0.9
132.8
0.9
132.8
0.1
1789.0
0.1
1787.8
0.1
1787.8
7
5
2
0.9
133.0
0.9
133.1
0.9
133.4
0.1
1788.4
0.1
1789.7
0.1
1787.7
4
0.9
132.6
0.9
132.7
0.9
132.4
0.1
1788.9
0.1
1789.2
0.1
1787.2
7
2
0.9
132.9
0.9
133.3
0.9
132.8
0.1
1787.2
0.1
1786.6
0.1
1785.7
4
0.9
133.2
0.9
133.0
0.9
133.1
0.1
1786.0
0.1
1787.4
0.1
1787.0
10
2
0.9
132.5
0.9
132.9
0.9
132.9
0.1
1787.1
0.1
1787.3
0.1
1786.7
4
0.9
132.9
0.9
132.8
0.9
133.2
0.1
1787.2
0.1
1786.5
0.1
1787.8
Average
0.9
133.0
0.9
132.9
0.9
132.9
0.1
1787.9
0.1
1787.9
0.1
1787.0
Real
0.9
132.9
0.9
132.9
0.9
132.9
0.1
1787.8
0.1
1787.8
0.1
1787.8
21

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1906_11020v2_sampling_of_multiple_variables_based_on_partial_order_set_theory
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1906_11020V2_SAMPLING_OF_MULTIPLE_VARIABLES_BASED_ON_PARTIAL_ORDER_SET_THEORY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

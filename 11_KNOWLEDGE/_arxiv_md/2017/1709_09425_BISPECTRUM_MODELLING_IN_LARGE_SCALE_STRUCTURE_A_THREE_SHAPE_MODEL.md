---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1709.09425
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1709.09425_Bispectrum_Modelling_in_Large_Scale_Structure_-_A_Three_Shape_Model

> Source: 1709.09425_Bispectrum_Modelling_in_Large_Scale_Structure_-_A_Three_Shape_Model.pdf

> Pages: 8

---


## Page 1


BISPECTRUM MODELLING IN LARGE SCALE STRUCTURE - A THREE
SHAPE MODEL
A. LAZANU
INFN, Sezione di Padova, Via Marzolo 8,
I-35131 Padova, Italy
We study the matter bispectrum of large structure by comparing theoretical models (perturba-
tion theories and halo models) to numerical simulations using shape and amplitude correlators.
We show that among the perturbation theories at one loop the eﬀective ﬁeld theory of large
scale structure extends the furthest into the non-linear regime. We analyse the one and two-
loop bispectra in the renormalised perturbation theory and we show that there is a signiﬁcant
extension in the range where results are accurate when going to two loops. In the case of
the halo model, we show that there are deﬁciencies in the modelling of the two-halo term at
redshifts z > 0 that worsen in the past. Based on this observation and on the shapes identiﬁed
in the halo model, we build a simple ‘three-shape model’ that provides a good ﬁt to N-body
simulations on all scales, at both low and high redshifts. We show that this model can be
easily extended to local and equilateral primordial non-Gaussianity using the same shapes.
1
Introduction
Cosmic Microwave Background (CMB) probes, and in particular Planck, have provided a wealth
of information in recent years, conﬁrming that the six-parameter ΛCDM model and the inﬂa-
tionary paradigm provide an adequate description of the observed Universe 1. Many theories
have been developed to explain the mechanism of inﬂation. Most of them predict the same two-
point correlation function (power spectrum) of the temperature anisotropy, but higher-order
correlations may be diﬀerent. Therefore, in order to distinguish between diﬀerent models, one
must look at these correlators, starting with the three-point function (bispectrum). Complemen-
tary information to the CMB can be obtained from the late-time distribution of galaxies (large
scale structure – LSS). This contains signiﬁcantly more information than the CMB, due to its
three-dimensional nature, but it is much more diﬃcult to extract, because of the non-linearities,
redshift space eﬀects and the relationship between the observed galaxies and the underlying dark
matter distribution (bias).
In this paper, we study the modelling of the matter bispectrum of LSS by analysing predic-
tions of theoretical models. We compare numerical bispectra arising from perturbation theories
and halo models with N-body simulations, in the absence 2 and in the presence of primordial
arXiv:1709.09425v2  [astro-ph.CO]  18 Oct 2017


## Page 2


non-Gaussianity (PNG) 3 using an innovative three-dimensional approach based on shapes, and
we build a new ‘three-shape’ model that provides a very good ﬁt to the simulations.
2
Matter Bispectrum and Correlators
By denoting the matter overdensity δ we deﬁne its power spectrum and bispectrum in Fourier
space as
⟨δ(k1)δ(k2)⟩= (2π)3δD(k1 + k2)P(k) ,
(1)
⟨δ(k1)δ(k2)δ(k3)⟩= (2π)3δD(k1 + k2 + k3)B(k1, k2, k3) ,
(2)
where δD is the Dirac delta function and ki = |ki|. We deﬁne the scalar product between two
bispectra Bi and Bj as
⟨Bi, Bj⟩≡V
π
Z
VB
dVk
k1k2k3 Bi(k1, k2, k3) Bj(k1, k2, k3)
P(k1)P(k2)P(k3)
,
(3)
where V is the volume of integration and VB represents the region deﬁned by the triangle
condition on wavevectors k1, k2, k3. We consider two regions for VB: (i) k1, k2, k3 ≤kmax – the
cumulative scalar product; (ii) K −∆K ≤k1 + k2 + k3 ≤K + ∆K – the sliced scalar product.
Using Eq. 3, we deﬁne shape (S) and amplitude (A) correlators between two bispectra
S (Bi, Bj) ≡⟨Bi, Bj⟩/
q
⟨Bi, Bi⟩⟨Bj, Bj⟩,
(4)
A (Bi, Bj) ≡
q
⟨Bi, Bi⟩/⟨Bj, Bj⟩.
(5)
These two correlators can be used to compare how much two bispectra resemble, and in particular
they can be employed to compare theoretical models with simulations, to ﬁnd up to which scale
one can expect a theoretical model to be accurate (cumulative scalar products), or to check
resemblances on scale-invariant slices (sliced scalar products). For a model to be an accurate
description of data, both shape and amplitude correlators must be as close as possible to unity.
3
Simulations
For analysing the performance of the theoretical models, we have used N-body simulations 4
based on modal estimators5,6 with both Gaussian and non-Gaussian initial conditions (floc
NL = 10
and fequilat
NL
= 100), each of them having three realisations. Around 100 coeﬃcients have been
required to accurately reconstruct the matter bispectrum from the modal expansion. In the
case of Gaussian initial conditions, we have smoothly combined three simulations 2, covering
scales up to k ∼7.8h/Mpc and for the non-Gaussian scenarios we have employed two sets of
simulations up to k ∼2.0h/Mpc. Each of the simulations considered contains 5123 particles,
the initial redshift is 49 and the box sizes are 1600(h/Mpc)3, 400(h/Mpc)3 and 100(h/Mpc)3
respectively.
4
Theoretical Models
4.1
Perturbation Theories
Perturbation theories are describing matter clustering on mildly non-linear scales and represent
corrections to linear theory. In this work we focus mostly on one-loop results, and we also show
an extension to two-loops. We have analysed the following models in perturbation theory:
• The Eulerian Standard Perturbation Theory (SPT) is based on a linearised expansion of the
evolution equations for the overdensity and velocity ﬁelds 7,8, when these are much smaller


## Page 3


than unity. In the case of the bispectrum, the lowest order non-zero term is called the ‘tree-
level’ bispectrum. At the next order (one loop), there are four non-zero terms. This theory
is however inaccurate, because the loop integrals involve integration over inﬁnite domains,
where the assumption |δ| ≪1 is no longer valid. Moreover, there are cancellations between
terms which does not guarantee a more accurate result at a larger number of loops. The
bispectrum predicted is too high compared to numerical simulations. Various approaches
to resolve this issue have been proposed, some of which are summarised in the next few
paragraphs.
• The Eﬀective Field Theory (EFT) of LSS 9,10 modiﬁes the evolution equations used in
SPT, by considering terms that account for the eﬀect of short wavelength modes on the
long wavelength ones. These induce corrections to the linearised ﬂuid equations, and in the
case of the bispectrum, all the of SPT terms are recovered, but also additional correction
terms that must be added. The counterterms subtract the excessive SPT contribution,
increasing the accuracy of the modelling 11,12. This theory requires ﬁtting parameters to
numerical simulations for the power spectrum, and the same parameters can be used for
the bispectrum.
• The Renormalised Perturbation Theory 13,14 recasts the evolution equations used in SPT
in matrix form and solves them using a ‘non-linear propagator’.
In this work we use
its simpliﬁed form MPTbreeze 15. This yields a resummed, convergent expansion that
becomes more accurate at a higher number of loops. Technically, only some of the terms
of SPT are required. We have computed numerically the bispectrum of this theory at both
one and two loops.
• Resummed Lagrangian Perturbation Theory. One can derive the equations of motion of
the ﬂuid displacements in Lagrangian coordinates, and a resummed expression for the
bispectrum can be obtained 16,17.
4.2
Halo Models
The halo model is a phenomenological model, based on the spherical collapse model, that can be
used to extend clustering to non-linear scales. The main assumption is that all the matter present
in the Universe is contained within virialised haloes. The model has three main ingredients: the
halo proﬁle, the halo mass function and the bias functions 18,19. In this model, the bispectrum is
expressed as a sum of three terms – the one-, two- and three-halo terms, describing contributions
of three particles in the same halo, two in one halo and another in a diﬀerent halo, or all three
in diﬀerent haloes. Although the halo model provides a useful description of matter clustering
on all scales, it has two deﬁciencies: (a) on large scales, at late times, there is an excess of
power because the one and two-halo terms do no decay fast enough; (b) on intermediate scales,
there is a deﬁcit of power at early times, because the assumption that all matter is contained
within virialised haloes is increasingly inaccurate at higher redshifts. One solution to resolve
the problems on large scales has been proposed in Refs. 20,21, where a perturbative method is
combined with the halo model, eﬀectively replacing the three-halo term. In our implementation,
we have used EFT as the perturbation theory.
5
Primordial non-Gaussianity
When initial conditions are non-Gaussian, the matter bispectrum gets modiﬁed according to the
shape of the primordial bispectrum, which is based on the inﬂationary model considered. Its
amplitude is quantiﬁed through the parameter fNL. In this work, we will only focus on the local
and equilateral shapes. For perturbation theories, there are additional terms that must be added
to the Gaussian expansion 22; in particular, there is an additional tree-level contribution. In the


## Page 4


0.1
0.5
1
5
0.6
0.7
0.8
0.9
1
Shape correlators
Gaussian
 
 
Constant
Squeezed
Tree level
Figure 1 – Shapes of the Gaussian N-body simulations. The thick dashed lines represent z = 0 and the narrow
continuous line – z = 0. The shapes at z = 1 follow a similar pattern, but are omitted for simplicity.
case of EFT, counterterms must be added to account for the eﬀect of the short wavelength
modes, as for the Gaussian scenario 23.
For the halo model there are modiﬁcations to the
proﬁle, mass function and bias 24.
The eﬀect of PNG is expected to be small compared to
the Gaussian component. Therefore, in order to make quantitative statements about the non-
Gaussian contribution, we have subtracted the Gaussian component of the bispectrum and we
analysed only the non-Gaussian remainder [∆BNG ≡B(fNL) −B(fNL = 0)].
6
Bispectrum Shapes
We consider the following shape functions:
Stree(k1, k2, k3) = 2
h
F (s)
2 (k1, k2)Plin(k1)Plin(k2) + 2 perms
i
,
(6)
Ssqueezed(k1, k2, k3) = 1
3 [Plin(k1)Plin(k2) + 2 perms] ,
(7)
Sconstant(k1, k2, k3) = 1 (Mpc/h)6 ,
(8)
where Eq. 6 is the gravitational tree-level bispectrum. By computing the sliced shape correlators
between the perturbation theories at one loop perturbation and the three shapes described
above (Fig. 6 of Ref.
2), we show that the perturbative theories have a ﬂattened shape, as
the gravitational tree-level bispectrum. In a similar manner, the three terms of the halo model
each have diﬀerent shapes – the one-halo term has a constant shape, the two-halo term has a
squeezed shape, while the three-halo term has a ﬂat shape (Fig. 7 of Ref. 2). The three shapes
can also be observed in the simulations (Fig. 1): on large scales, in the perturbative regime, the
bispectrum has a ﬂattened shape, corresponding to the three-halo term; on intermediate scales,
where the two-halo term is dominating, there is a squeezed shape; on small scales, in the deeply
non-linear regime, the bispectrum has a constant shape corresponding to the one-halo term.
Moreover, in Fig. 1 the evolution of the shapes with redshift is evidenced: the ﬂattened shape
becomes more extended as the redshift is increased (as structures become more linear at earlier
times and linear theory is becoming an increasingly good approximation), while the squeezed
and constant shapes shift towards non-linear scales.
7
The Three Shape Model
Based on the observations from the halo model, we propose the following decomposition for the
matter bispectrum:
B(k1, k2, k3) =
3
X
i=1
fi(K)Si(k1, k2, k3)
(9)


## Page 5


kmax [h/Mpc]
Amplitude correlators
z = 0
10
−1
10
0
0
0.2
0.4
0.6
0.8
1
1.2
kmax [h/Mpc]
z = 2
 
 
10
−1
10
0
Tree
Tree NL
SPT
EFT
MPTbreeze
RLPT
Halo model
Halo−PT
Figure 2 – Amplitude correlators between theoretical models and the three-shape model (for the Gaussian case)
at z = 0 (left) and z = 2 (right). The legend is common to both plots.
where K = k1 + k2 + k3, the shape functions Si are given by Eqs. 6-8, and functions fi are
unknown amplitude functions. We show that this ansatz can yield an improved ﬁtting to the
data with respect to the halo model on all scales.
On small scales, the bispectrum has a constant shape. We have seen that this model ac-
curately describes matter clustering. Therefore, we choose to ﬁt the amplitude function to the
one-halo term and use it directly in our three-shape model. Due to the particular form of the
ansatz, we can use the equilateral component of the model to ﬁnd a ﬁtting function of the form,
fconstant(K) =
A
(1 + bK2)2 ,
(10)
where the two coeﬃcients are then easily obtained for each redshift.
On intermediate scales, the halo model is no longer accurate at redshifts z > 0 and moreover
the two-halo term does not decay fast enough at low k; hence, we choose to use a function
inspired by the two-halo term, but we ﬁt the coeﬃcients to the simulations:
fsqueezed(K) =
C
(1 + DK−1)3 .
(11)
On large scales, perturbation theories are providing accurate descriptions of the matter
bispectrum. However, all one-loop perturbation theories are ﬂattened 2; hence the tree-level
bispectrum is not suﬃcient because it quickly decays. In order to keep the model simple, we
choose to use the gravitational tree-level bispectrum, but replace the linear power spectrum in
Eq. 6 with the HALOFIT power spectrum 25,26, thus creating a ‘non-linear tree-level’ bispec-
trum. This provides excessive signal on small scales (Fig. 2) and hence we cut it oﬀwith an
exponential of the form ftree(K) = exp(−K/E). Coeﬃcients C, D and E are then ﬁtted to the
simulations, thus determining the three-shape model.
In the case of the non-Gaussian bispectrum, the ansatz from Eq. 9 remains largely un-
changed, with the exception that the tree-level shape (Eq. 6) is replaced with its non-Gaussian
counterpart 3 (which depends on the shape of PNG),
∆B3−shape
NG
(k1, k2, k3) = Stree
NG,NL + c1fsqueezed(K)Ssqueezed(k1, k2, k3)
+c2fconstant(K)Sconstant(k1, k2, k3) .
(12)
The amplitude functions also remain the same, but they are multiplied by diﬀerent numerical
coeﬃcients (c1, c2), which are ﬁtted to simulations.


## Page 6


kmax [h/Mpc]
Amplitude correlators
MPTbreeze, z = 0
 
 
10
−1
10
0
0
0.2
0.4
0.6
0.8
1
1.2
MPTbreeze 1 loop
MPTbreeze 2 loops
kmax [h/Mpc]
MPTbreeze, z = 2
 
 
10
−1
10
0
MPTbreeze 1 loop
MPTbreeze 2 loops
Figure 3 – Amplitude correlators between the MPTbreeze model at one and two loops and the three-shape
model, at z = 0 (left) and z = 2 (right).
Both the three-shape model (Eq. 9) and its non-Gaussian correction (Eq. 12) provide a
good ﬁts to the N-body simulations, as the shape and amplitude correlators between the three
shape model and the simulations are close to unity 2,3.
8
Results
We have compared the predictions of theoretical models – perturbation theories and halo models
with the three-shape model and numerical simulations using the cumulative shape and amplitude
correlators. We have represented ﬁtting errors of the three shape model in dark grey, while the
light grey areas represent uncertainties between realisations of the simulations.
8.1
Perturbation theories (one loop) and halo models
We have investigated the predictions of perturbation theories at one loop by looking at the
shape and amplitude correlators. The shape correlators do no represent an accurate method of
testing the predictions because they are always smaller or equal to unity and hence one cannot
distinguish between the situations when the model is underestimating or overestimating the
actual bispectrum. Amplitude correlators are however more promising. In Fig. 2 (left) we have
plotted the amplitude correlator between the various theoretical models and the three shape
model at redshift zero for the Gaussian scenario. The plot shows that SPT is overestimating
the signal on mildly non-linear scales and that the EFT counterterm subtracts the eﬀective
contribution.
The MPTbreeze and RLPT (both one loop) predict a similar signal that is
exponentially suppressed. The ‘non-linear’ tree-level bispectrum, built using the HALOFIT
power spectrum has a signiﬁcant leftover signal on small scales, and in order to avoid any
excessive ﬂat signal we have cut it oﬀwith the exponential function in the three-shape model.
The plot shows that the EFT extends the furthest into the nonlinear regime and this trend is
also valid at earlier times (Fig. 2 - right).
In the case of the halo model, the features and deﬁciencies of it can be clearly seen in the
same plots. At redshift zero (red line) there is an excess of power on large scales, while this excess
is drastically reduced at z = 2. At this redshift one can see the inaccuracies in the modelling of
the two-halo term, which is signiﬁcantly underestimated, with the halo model giving only around
50% of the signal in the simulations. The dashed purple line, representing the halo-PT model
(combined with EFT) solves the large-scale issue by using EFT on large scales and cutting oﬀ
the large-scale part of the two-halo term 2.


## Page 7


kmax [h/Mpc]
Amplitude correlators
Local PNG, z = 2
 
 
10
−1
10
0
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Tree(NG)
SPT
Halo model
EFT
kmax [h/Mpc]
Amplitude correlators
Equilateral PNG, z = 2
 
 
10
−1
10
0
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Tree(NG)
SPT
Halo model
EFT
Figure 4 – Amplitude correlators between the non-Gaussian corrections to the tree-level bispectrum, one-loop
bispectrum, EFT the halo model, and ∆B3−shape
NG
at z = 2 for local (left) and equilateral (right) types of non-
Gaussianity.
8.2
Two-loop results
We have analysed the two-loop bispectrum in MPTbreeze.
Details of the terms that are
present in this case and how to take care of divergences are given in the Appendix of Ref. 2. In
Fig. 3 we have plotted the amplitude correlators between this model at one and two loops and
the three shape model. There is signiﬁcant gain in going to two loops in this model, as the scale
where the theory is decaying is shifting towards nonlinear scales with around 0.1 h/Mpc. This
model could be used in the future for an enhanced three-shape model.
8.3
Primordial non-Gaussianity
We have investigated the non-Gaussian corrections to the matter bispectrum for the case of
local and equilateral types of PNG, by analysing the predictions of the tree-level, one loop SPT,
EFT and halo model (Fig. 4). The predictions are very similar to those found in the Gaussian
scenario 3 – the one-loop SPT provides an excessive signal on mildly non-linear scales for both
local and equilateral shapes, that can be subtracted using counterterms in EFT. In the case of
the halo model the deﬁcit of power is appearing on similar scales to the Gaussian scenario.
9
Conclusions
In this paper we have performed a detailed investigation of the matter bispectrum of large scale
structure. We have analysed the predictions of perturbation theories and halo models for both
Gaussian and non-Gaussian initial conditions. In the Gaussian scenario, we have shown that
in the case of perturbation theories the eﬀective ﬁeld theory of large scale structure (at one
loop) extends the furthest into the non-linear regime. This requires nevertheless ﬁtting free
parameters to the power spectrum of simulations. The two-loop bispectrum of MPTbreeze
provides a competitive option to EFT, being parameter-free.
We have investigated the bispectrum of the halo model and we have shown that each of
its three terms has a diﬀerent shape – a constant shape, squeezed shape and ﬂattened shape
– and we have used this observation to build a new phenomenological, three-shape model that
provides an accurate description to the matter bispectrum of LSS by ﬁtting a few parameters.
In the process we have identiﬁed inaccuracies in the modelling of the two-halo term of the halo
model, that account for an overall underestimation of the bispectrum on intermediate scales.
We have also shown that this model can be extended to PNG and that the three shapes are
preserved even in that situation.


## Page 8


Acknowledgements
First of all I would like to express my gratitude to the organisers of the Rencontres du Vietnam
Cosmology 2017 Conference, and especially to Professors Jacques Dumarchez and Jean Trˆan
Thanh Vˆan, for inviting me to attend the conference, for their hospitality in Quy Nhon and for
creating such a stimulating environment for cosmology. I would also like to thank Paul Shellard,
Tommaso Giannantonio and Marcel Schmittfull for the fruitful collaboration which leaded to
Refs. 2,3.
References
1. R. Adam et al. (Planck Collaboration), Astron. Astrophys. 594, A1 (2016).
2. A. Lazanu, T. Giannantonio, M. Schmittfull and E.P.S. Shellard, Phys. Rev. D 93, 083517
(2016).
3. A. Lazanu, T. Giannantonio, M. Schmittfull and E.P.S. Shellard, Phys. Rev. D 95, 083511
(2017).
4. M.M. Schmittfull, D.M. Regan and E.P.S. Shellard, Phys. Rev. D 88, 063512 (2013).
5. J.R. Fergusson, D.M. Regan and E.P.S. Shellard, Phys. Rev. D 86, 063511 (2012).
6. D.M. Regan, M.M. Schmittfull, E.P.S. Shellard and J.R. Fergusson, Phys. Rev. D 86,
123524 (2012).
7. J.N. Fry, Astrophys. J. 279, 499 (1984).
8. F. Bernardeau, S. Colombi, E. Gazta˜naga and R. Scoccimarro, Phys. Rep. 367, 1 (2002).
9. D. Baumann, A. Nicolis, L. Senatore and M. Zaldarriaga, J. Cosmol. Astropart. Phys. 7,
051 (2012).
10. J.J.M. Carrasco, M.P. Hertzberg and L. Senatore, J. High Energy Phys. 9, 82 (2012).
11. R.E. Angulo, S. Foreman, M. Schmittfull and L. Senatore, J. Cosmol. Astropart. Phys.
10, 039 (2015).
12. T. Baldauf, L. Mercolli, M. Mirbabayi and E. Pajer, J. Cosmol. Astropart. Phys. 5, 007
(2015).
13. M. Crocce and R. Scoccimarro, Phys. Rev. D 73, 063519 (2006).
14. F. Bernardeau, M. Crocce and R. Scoccimarro Phys. Rev. D 78, 103821 (2008).
15. M. Crocce, R. Scoccimarro and F. Bernardeau, Mon. Not. R. Astron. Soc. 427, 2537
(2012).
16. T. Matsubara, Phys. Rev. D 77, 063530 (2008).
17. C. Rampf and Y.Y.Y. Wong, J. Cosmol. Astropart. Phys. 6, 018 (2012).
18. U. Seljak, Mon. Not. R. Astron. Soc. 318, 203 (2000).
19. A. Cooray and R. Sheth, Phys. Rep. 372, 1 (2002).
20. P. Valageas and T. Nishimichi, Astron. Astrophys. 527, A87 (2011).
21. P. Valageas and T. Nishimichi, Astron. Astrophys. 532, A4 (2011).
22. E. Sefusatti, M. Crocce and V. Desjacques, Mon. Not. R. Astron. Soc. 406, 1014 (2010).
23. V. Assassi et al., J. Cosmol. Astropart. Phys. 11, 024 (2015).
24. D.G. Figueroa, E. Sefusatti, A. Riotto and F. Vernizzi, J. Cosmol. Astropart. Phys. 8, 36
(2012).
25. R.E. Smith et al., Mon. Not. R. Astron. Soc. 341, 1311 (2003).
26. R. Takahashi et al., Astrophys. J. 761, 152 (2012).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1709_09425_bispectrum_modelling_in_large_scale_structure_a_three_shape_model
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1709_09425_BISPECTRUM_MODELLING_IN_LARGE_SCALE_STRUCTURE_A_THREE_SHAPE_MODEL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

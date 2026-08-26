---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.08805v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1707.08805v1_Automatic_differential_analysis_of_NMR_experiments_in_complex_samples

> Source: 1707.08805v1_Automatic_differential_analysis_of_NMR_experiments_in_complex_samples.pdf

> Pages: 35

---


## Page 1


Automatic diﬀerential analysis of NMR
experiments in complex samples
Laure Margueritte1
Petar Markov2
Lionel Chiron3
Jean-Philippe Starck3
Catherine Vonthron-Sénécheau1
Mélanie Bourjot1
Marc-André Delsuc4*
1. Université de Strasbourg, CNRS, Laboratoire d’Innovation Thérapeutique
(LIT), UMR7200, Labex MEDALIS, 67000, Strasbourg, France
2. Structural Biophysics Group, School of Optometry and Vision Sciences,
CardiﬀUniversity, United Kingdom
3. CASC4DE Le Lodge, 20, Avenue du Neuhof, 67100 Strasbourg, France
4. Institut de Génétique et de Biologie Moléculaire et Cellulaire (IGBMC),
INSERM U596, CNRS UMR 7104, Université de Strasbourg, Illkirch-
Graﬀenstaden, France
Abstract
Liquid state NMR is a powerful tool for the analysis of complex mixtures of
unknown molecules. This capacity has been used in many analytical approaches:
metabolomics, identiﬁcation of active compounds in natural extracts, characteri-
zation of species, and such studies require the acquisition of many diverse NMR
measurements on series of samples.
While acquisition can easily be performed automatically, the number of NMR ex-
periments involved in these studies increases very rapidly and this data avalanche
requires to resort to automatic processing and analysis.
We present here a program that allows the autonomous, unsupervised processing
of a large corpus of 1D, 2D and DOSY experiments from a series of samples
acquired in diﬀerent conditions. The program provides all the signal processing
steps, as well as peak-picking and bucketing of 1D and 2D spectra, the program
and its components are fully available. In an experiment mimicking the search
of an active species in natural extract, we use it for the automatic detection
of small amounts of artemisin added to a series of plant extracts, and for the
generation of the spectral ﬁngerprint of this molecules.
This program called Plasmodesma is a novel tool which should be useful to deci-
1
arXiv:1707.08805v1  [physics.chem-ph]  27 Jul 2017


## Page 2


pher complex mixtures, particularly in the discovery of biologically active natural
products from plants extracts, but can also in drug discovery or metabolomics
studies.
Introduction
Liquid state NMR is a powerful tool for the analysis of mixtures containing
unknown molecules. All species in the solution display their NMR spectra, with
a signal intensity proportional to their relative concentrations, provided that
slow tumbling rates or relaxation agents do not hide the lines by fast relax-
ation processes. This capacity has been used in many analytical approaches:
metabolomics, identiﬁcation of active compounds in natural extracts, characteri-
zation of species1–5. See references (6), (7), and (8) for recent reviews.
Such studies require the acquisition of many diverse NMR measurements on series
of samples. Modern NMR spectrometers allow sequential actions (introduction
of the sample, probe tuning, acquisition) in order to produce automatically the
corresponding 1D and 2D data sets.
Unfortunately, if the acquisition is quite easily performed, the access to the
ﬁnal informations is less straightforward: signal processing (Fourier transform,
phasing, baseline correction, peak detection) and ﬁnally spectrum interpretation
are not trivial tasks. Moreover, the use of 2D spectra implies more complex
steps and additional tasks such as reduction of t1-noise and t1-ridges, or the
determination of contour levels for display.
In the case of metabolomics studies, or natural extracts screening, the number
of NMR experiments increases very rapidly and this data avalanche requires to
resort to automatic processing. While metabolomics are aimed at measuring
precisely the amount of well-known compounds, and to quantify precisely their
variations from sample to sample, the identiﬁcation of an active molecule in a
natural extracts starts with its detection and then its characterization of an
unknown compond or eventually a family of related species.
In this article, we present the speciﬁc development of a computer program
allowing the autonomous, unsupervised processing of a large corpus of 1D and
2D experiments from a series of samples acquired in diﬀerent conditions.
Results obtained using this program on series of complex natural extracts
highlight the time saving and the eﬃciency increase regarding classical “hand-
made” processing of raw data.
2


## Page 3


Software developments
Plasmodesma
The program Plasmodesma9 developped for this project relies on the SPIKE
library for most of its operation10. It is intended to process autonomously a large
series of diﬀerent spectra originated from diﬀerent samples, obtained in varying
conditions. This analytical process involves the handling of a complex set of
NMR experiments (1D and 2D homo- or hetero-nuclear spectra), at the end, a
spectral report summarizing the analysis is expected, containing all ﬁgures, peak
and bucket lists for each sample.
The current work is based on SPIKE (Spectrometry Processing Innovative
KErnel)a comprehensive software on which the current work is based, is a
comprehensive software library aimed at the processing and analysis of Fourier
transform spectroscopies. It provides basic functionalities such as apodization,
Fourier transforms, phasing, peak-picking, line-ﬁtting, baseline correction as well
as more advanced tools. It is easily extensible through a plug-in mechanism.
SPIKE combines the use of a parallel multi processor approach to a low memory
footprint, thus insuring rapid processing with an optimal use of the computer
hardware. Moreover, SPIKE allows the eﬃcient handling and visualization of very
large data-sets limited only by disk space. SPIKE is a continuation of the previous
Gifa and NPK11,12 NMR processing softwares, and was developed to include
other Fourier transform spectroscopies, in particular FT Mass spectrometry
(Orbitrap and FT-ICR) and 2D-FT-ICR13–15. For portability reasons and ease
of development, the program is written in Python, and relies on external libraries
such as numpy, scipy, pandas, and hdf5.16–20
Principle of operations
The program Plasmodesma operates without any human interaction. When
applied to a folder, all NMR ﬁles are imported, processed, and a global report is
generated for the totality of the analysis. All the processing and analysis steps
are optimized depending on the acquisition parameters found in the data-sets,
either 1D or 2D data. No other input is required. The 1D and 2D experiments
are processed sequentially, The data are apodized, Fourier transformed, and the
baseline corrected, 1D spectra are also automatically phased. Additionally, an
eﬃcient denoising step21 is performed on the 2D experiments, in order to reduce
the t1-noise. The F1 Fourier transform step of the 2D data-sets is performed
depending on the spectral type and on the acquisition protocol. The calibration
is then determined precisely from the reference signal (in this case, 0 ppm for
the TMS). A peak-picking and bucket analysis are then performed (see below).
Peak lists and bucket lists are generated as csv ﬁles for each experiment. Finally,
ﬁgures of each spectrum is created, with and without peaks displayed. A ﬁnal
3


## Page 4


report that contains all acquisition and processing parameters is generated (see
S.I. S1).
Speciﬁc developments
Some functions used by Plasmodesma have been developed speciﬁcally for this
analysis, and were implemented as SPIKE plug-ins.
Autophasing
In the context of metabonomics and screening studies, the possibility to detect
and quantify precisely the intensity of vanishing small peaks is paramount. The
phase of a 1D spectrum, if set slightly oﬀ, may have a strong impact on the
possibility to detect small signals, in particular if they are close to a large one.
Errors of only a few degrees introduce bias resulting to too low or too high
quantization, as well as shifts of the maximum. Automatically acquired natural
extract spectra are usually diﬃcult to phase because of strong solvent lines
and other artifacts present in the spectra. The improvement of the simple but
robust automatic phasing procedure developed in NPK12 contributes eﬃciently
to resolve this problem. The principle is to minimize the negative wing of the 1D
spectrum, by performing a grid search ﬁrst on 0th order (frequency independent)
alone, then on both 0th and 1st order (frequency dependent) corrections, the
larger peak being used as the 1st order pivot. An automatic baseline correction
(see below) is performed at each correction step, and an optional inwater mode
allows to ignore the central spectral zone.
Autobaseline
A ﬂat baseline is also a requisite for correct analysis, and a speciﬁc plugin as
been developed in this respect. We developed a new approach, which relies on an
iterative statistical treatment on the signal split into pieces of constant length,
and ﬁtting the baseline by piecewise linear segments. The ﬁt is based on the use
of a linear regression minimizing the ℓp(x) = (P(|x|p))1/p norm of the diﬀerence.
A rough estimate of the spectral baseline is ﬁrst generated using p = 1 on each
pieces. Then, the estimate is iteratively improved by removing that part of the
signal above the current baseline approximation, and using p = 3 for ﬁtting.
This method guarantees baselines that stick well to the signal avoiding spurious
oscillations that higher-order polynomials or splines may produce.
Bucketing
Bucketing is an important operation in the processing pipeline. It consists in
computing the area under the spectrum over small spectral segments which cover
4


## Page 5


the whole spectral width. The segments should be large enough to blur the
small discrepancies that appear from one sample to another, while preserving
the resolutive power of the spectra. A bucket size of 0.01 ppm was used for 1D
1H spectra.
Bucketing also reduces the size of the data that will be submitted to statistical
analysis. This is of foremost importance in the analysis of 2D spectra, which
routinely contains millions of points. The reduction of 2D datasets to tractable
sizes in statistical tools requires nevertheless bucket sizes on the order of 0.03
to 0.05 ppm in 1H spectroscopy and to 1.0 ppm in 13C. Such sizes are certainly
too large to capture all the details contained in the 2D spectra. One solution
to this diﬃculty could be to use segments of varying size, however we rather
chose to enrich the information by adding to the area of each bucket, additional
information. For each bucket, computed over 1D or 2D spectra, the coordinates
of the bucket center and its size in pixel were stored, along with the area
information computed as the mean over the bucket, and enriched with the values
of the min and max points, and the standard deviation of data over the bucket.
Processing of DOSY experiment
DOSY spectra are extremely eﬃcient in deciphering complex mixtures, and have
been used in many diﬀerent work (see Mahrous et al7 and reference therein).
They require a speciﬁc processing for the analysis of the exponential decays
observed along the indirect dimension of the 2D spectrum. In this work this
speciﬁc processing was performed by using the recently introduced PALMA
algorithm22 that implements a rapid Inverse Laplace Transform analysis, using
a hybrid constraint, maximizing the entropy while minimizing the ℓ1 norm of
the reconstructed spectrum. This algorithm was developed using the SPIKE
library, so it was particularly easy to insert it into the processing pipe-line. As a
consequence, they are systematically processed and a peak list and an adapted
bucket list is also generated.
Report
Finally, a concise report is produced as a csv ﬁle (see S.I. S2). The report contain
all the important parameters related to data acquisition and processing. They
are ﬁnally displayed, as rendered using the pandas python library18.
Analysis
Given a set of 1D and 2D NMR raw experiments, the approach described above
is able to produce, in full automation and without any human interaction, a
set of correctly processed spectra, along with complete peak lists and enriched
bucket lists.
5


## Page 6


The artifacts observed in the spectra, such as antidiagonals, t1 noise and ridges,
etc. were corrected on the bucket list. On modern spectrometers these artifacts
are usually at a low intensity, however as the purpose here is to detect species at
low concentration, and their presence is detrimental.
The 2D bucket list is corrected for remaining t1 noise and t1 ridges for each
column in the matrix, by setting to null all buckets below twice the median value
of the considered column. The bucket list originated from symmetric spectra,
such COSY and TOCSY, were further corrected for departure of this symmetry
by setting symmetrical buckets to the minimum value of the pair. These two
operations have the eﬀect of preserving the most signiﬁcant buckets, without
loosing the weak spectral areas.
M&M
Chemicals. Artemisinin 98% was purchased in Sigma-Aldrich and deuterated
methanol (10 x 0.75mL) in Eurisotop (Saint Aubin, France).
Algae collection and identiﬁcation. The algae Sargassum muticum was
collected in June 2006 in Cap Lévy (Manche), France. Taxonomic determination
was performed by Dr A-M. Rusig and a voucher specimen was deposited in the
Herbarium of the University of Caen. Extraction was realized as in Vonthron-
Sénécheau et al.23.
Samples preparation. Five samples containing 10 mg of S. muticum hydroal-
coholic extract were prepared. An artemisinin DMSO solution at 3 mg/mL was
added to the samples to obtain a ﬁnal concentration of artemisinin of 0.2, 0.3,
0.4 and 2.7 mg/ml in NMR tubes, as summarized in Table 1. All samples were
lyophilized and dissolved in 750 µL of methanol d4, and put in 5 mm NMR tubes.
The NMR tubes were spun with a small bench centrifuge to help sedimentation
of insoluble parts, and placed in the NMR sample changer.
Table 1: Samples preparation
Sample n°
1
2
3
4
5
S. muticum extract
10 mg
10 mg
10 mg
10 mg
10 mg
added artemisinin
0 mg
0.15 mg
0.24 mg
0.32 mg
2 mg
A sample of pure artemisinin was prepared in methanol d4 and studied by NMR.
NMR spectroscopy
Acquisitions were performed on a Bruker Avance-III spectrometer operating
at 700 MHz, and equipped with a TCI cryo probe and a standard Bac60 sample
6


## Page 7


changer. Each sample was automatically inserted into the spectrometer, tuned
and shimmed after a stabilization delay of 120 seconds. All experiments were
automatically run on each sample, the whole sequence being programmed using a
TopSpin macro (see E.S.I S2). Spectral parameters (π/2 pulses, receiver gain. . . )
were optimized on one sample and used for the whole series without further
check.
Spectral widthes were set to 12 ppm in 1H and to 150 ppm in 13C. 1D spectra
were acquired on 64 scans, 16384 points, and a relaxation delay of 1.5 sec, for
a total time of 3 minutes. COSY experiments were performed with 8 scans,
with 512 increments of 4096 points each, for a total acquisition time of 2 hours.
TOCSY experiments were performed with 8 scans, with 400 increments of 4096
points each, and using a DISPSI-2 mixing sequence of 80 msec duration. TOCSY
acquisition time was 1 hour 40 minutes. DOSY experiments were performed
with 32 scans, with 50 increments of 4096 points each, for a total acquisition
time of 50 minutes. HSQC experiments were performed with 4 scans, with 512
increments of 2048 points each, for a total acquisition time of 1 hour. HMBC
experiments were performed with 48 scans, with 400 increments of 4096 points
each, for a total acquisition time of 10 hours.
The complete acquisition time for one sample, including sample injection and
tuning, took about 16 hours. The ﬁve samples were acquired in one continuous
run.
The artemisinin sample was studied by NMR: Artemisinin: 1H NMR (CD3OD,
700 MHz) δ 0.99 (3H, d, J = 6.2 Hz, 6-CH3), 1.16 (3H, d, J = 7.2 Hz, 9-CH3),
1.38 (3H, s, 3-CH3), 2.08 (1H, ddd, H4), 2.40 (1H, ddd, H4), 2.01 (1H, m, H5),
1.47 (1H, m, H5), 1.38 (1H, m, H5a), 1.52 (1H, m, H6), 1.09 (1H, m, H7), 1.77
(1H, m, H7), 1.17 (1H, m, H8), 1.86 (1H, m, H8), 1.82 (1H, m, H8a), 3.31 (1H,
dq, H9), 6.03 (1H, dq, H12), 13C NMR (CD3OD, 700 MHz) δ 106.7 (C, C3),
25.2 (CH3, C3), 36.6 (CH2, C4), 25.7 (CH2, C5), 51.2 (CH, C5a), 38.1 (CH,
C6), 19.9 (CH3, C6), 34.6 (CH2, C7), 24.0 (CH2, C8), 45.6 (CH, C8a), 34.0
(CH, C9), 12.7 (CH3, C9), 81.0 (CH, C12a), 95.5 (CH, C12).
Data Processing
Spectral Processing was integrally performed using the Plasmodesma program
presented here. The program is written in python, and is compatible both with
python 2 and python 3. It is based on the SPIKE library10 and the DOSY
processing were performed using the PALMA approach22 embedded in SPIKE
as a plugin.
Complete processing took 96 minutes on a MacOs machine, running the python
anaconda distribution 4.2 from Continuum Analytics (Austin, TX).
Statistical Analysis. The bucket lists and peak lists produced by the Plas-
modesma run were analyzed with a python script based on the pandas library,
7


## Page 8


using the Jupyter notebook environment.
The Plasmodesma program, along with examples, experimental data related to
the artemisin series, Jupyter notebooks presenting the data analysis, and the spe-
ciﬁc SPIKE plugins are freely available at https://github.com/delsuc/plasmodesma
repository.
Results
To mimic the presence of a bioactive molecule at diﬀerent concentrations in com-
plex mixtures, crude plant extracts were supplemented at diﬀerent concentrations
with artemisinin, a naturally occurring and structurally known sesquiterpene
lactone, and ﬁve diﬀerent samples were prepared. All ﬁve samples were placed
in the sample changer and NMR data were acquired in an automatic manner,
after an initial tuning of the ﬁrst sample.
Data Processing
The raw data-sets were processed as described above, and the peak lists and
bucket lists generated. Figures 1 and 2 show an example of the result of such a
processing.
~
~
~
~
Figure 1: 1D 1H spectrum of sample n°5.
The bucketing procedure is used to summarize the spectral content, and by
reducing the size of the data to handle, to ease further statistical analysis.
However, it can be seen in Figure 2 that t1-noise and other spectral artifacts are
present in particular in the standard deviation analysis, which enhances the local
signal variations. It appears that corruption of buckets from spectral artifacts
appear more deleterious in 2D spectroscopy than in classical 1D. For this reason,
the areas and standard deviation values of the bucket list were subjected to the
simple procedures described above. The ﬁrst step consists in setting to a null
value all values below a certain threshold computed from the median over the
vertical column of the considered bucket. This procedure allows to remove a large
part of the noise, and to only retain the peaks separated above the threshold.
8


## Page 9


a)
c)
b)
Figure 2: COSY spectrum of sample n°5. a) automatically generated contour
plot, b) graphic representation of the raw bucket list, c) same as b, but showing
the standard deviation of each bucket.
The threshold level adapted for each column permit to eﬃciently clean the strong
t1-noise stripes, while preserving weak peaks located in less crowded regions.
In a second step, homonuclear experiments a symmetrization procedure can be
applied, it was done here by simply taking the smaller of the two values related
by symmetry. This procedure is much simpler and more robust on bucket lists
than on real spectra, as the bucketing has already homogenized the spectral axes
and produced squared buckets. This procedure was applied on the area and the
standard deviation values of the bucket list.
b)
a)
Figure 3: a) Standard deviation the bucket list from Figure 2 after t1-noise
removal, b) same data as in a after symmetrization.
Figure 3 shows the result of each cleaning steps. It can clearly be seen that
this procedure, allows an improvement of the quality of data and a better
compatibility with automatic analysis.
9


## Page 10


Data Analysis
The cleaned bucket lists can be eﬃciently used for detection of the spectral
features varying from spectrum to another. This can be done on any 1D or 2D
spectra: Figure 4 shows the result on the analysis of the COSY spectrum.
b)
c)
a)
Figure 4: Automatic extraction of spectral ﬁngerprint from the automatic spectral
analysis a) standard COSY spectrum of artemisinin, b) result of the subtraction
of the std channel of the bucket lists of sample 5 and sample 1, c) same as b for
sample 4 and sample 1.
Obviously, the positions of the signals of the artemisinin spectrum is detected
and separated from the constant background, even though the background is
of much larger intensity. Here the original spectrum is not genuinely recovered,
not only because some signals are missing, but principally because of the loss of
the intensities. However, the generated spectral pattern can be used to extract
chemical shifts and topologies, and recognize a molecular pattern, which can
be used as a ﬁngerprint. The same result cannot be obtained directly from the
spectrum, and is eﬃcient because the bucketing standardizes the spectra, the
standard deviation measures the ﬂuctuation rather the intensity. Finally the
cleaning operation smooth out the random ﬂuctuations which otherwise would
hamper the direct comparison to operate.
The procedure above is not very sensitive, and the samples with lower level of
added artemisin could not be processed eﬃciently. A second procedure was tested
by taking the ratio of the bucket standard deviation values. The results are
shown in Figure 5: despite a low level of concentration (few hundred micrograms
of artemisin in 10 mg of crude material), the spectral ﬁngerprint is recovered.
In this case the diagonal of the homonuclear spectrum is not recovered, this
does not have a strong imapct, as it can be fully infered from the oﬀ-diagonal
ﬁngerprint dots.
Linear regression
This ﬁrst approach take spectra two by two, and can be used on homonuclear
spectra, as shown here, and also on heteronuclear ones. Using the whole set of
10


## Page 11


b)
a)
d)
c)
Figure 5: Spectral ﬁngerprint obtained by the ratio of bucket standard deviation,
a) comparison of sample 5 and sample 1, b-c-d) same as a for sample 4, 3 and 2
respectively.
11


## Page 12


spectra at once requires to have an additional information, eventually imprecise,
on the amount of active material in each sample. In this case, signals coming
from the studied molecule are expected to be proportional to its concentration,
and this property can be exploited to separate those signals, varying along
with the concentration value, to the other signal, uncorrelated with it. This
was performed by using the scikit-learn library24, a generic tool for machine
learning, written in python with full interoperability with python, Jupyter and
SPIKE. The linear_model.LinearRegression() function and the Recursive
Feature Elimination tool were used, and applied on the the bucket lists area
values (see S.I. for detailed operation).
These tools allow to select a small subset of parameters which best correlate
with the estimated concentration. The selected features are then supposed to
deﬁne a spectral ﬁngerprint in a manner equivalent with the previous approach,
but with a quantitative aspect this time. As the whole spectrum series is used,
it is expected to produce better results. Results are shown in Figure 6 for the
HSQC spectra obtained on the 4 samples presenting the lowest concentration.
It can be seen that the HSQC spectrum of artemisinin is extracted from the
complex spectrum of the mixture. The main artifacts observed in the ﬁnger
print are associated with the solvent lines (here water, methanol and DMSO)
sample 4
Artemisinin
linear regression
RFE
Figure 6: HSQC Spectral ﬁngerprint determined from the linear regression
analysis over the 4 samples with lowest concentration.
12


## Page 13


Discussion
The measurement of NMR spectra over series of complex samples, and their
analysis, is a common procedure in screening or activity studies. The acquisition
part is usually well covered through the use of sample changers and associated
softwares, with the eventual help of companion programs, allowing an optimized
set-up25. Here, we extend the set of tools for these studies to the possibility of
automatic processing and statistical analysis of the set of 1D and 2D spectra.
There are already basic tools which allow to perform the ﬁrst processing steps of
the data, however, they usually rely either on preset parameters values (phase
corrections, window function) or crude estimate of the optimum parameters
(baseline correction). In contrast, the program Plasmodesma presented here,
works in an autonomous manner, without any user interaction, relying on a
small set of preset global parameters. It is able to autonomously process 1D,
2D, and DOSY experiments, processing parameters are optimized either from
the experiment types (window function) or optimized automatically on the data
(phase correction, baseline). In addition, advanced methods are used for the
denoising of 2D spectra or the analysis of DOSY experiments. Finally, the
program generates spectra and peak lists and bucket lists for all spectra, as well
as reports on the data and the analysis.
The use of the SPIKE library10, a generalist processing library for NMR and
other Fourier spectroscopies, allowed a rapid development of the program, as well
as the use of advance tools. Not relying on parameters previously by an operator
allow to process directly after the measure, and use the result of the processing
as a token for the quality of the acquisition. The processing step being more
rapid than the acquisition, it is perfectly possible to repeat the processing along
the series of measurements, to monitor the advance and quality of the current
experiment.
The series of spectra are further algorithmically analyzed using machine-learning
inspired approaches. However, each 2D spectrum is typically composed of several
million of data points, and this size hampers the possibility to algorithmically
compare eﬃciently several spectra For instance the series of spectra generated
in this study represents more than 20 million points overall, and some pre-
conditioning of the data is required. For this reason, the automatic analysis of the
spectra is here principally performed on the bucket lists, which provided a reduced
but faithful representation of the spectrum. Many artifacts such as antidiagonals,
t1 noise and ridges, are also present. These artifacts are of rather low intensity,
however as the purpose here is the detection of compounds at low concentration,
their presence is detrimental, and we chose to correct them on the bucket list
rather than on the original spectra. This smoothing and spectral normalization
aﬀorded by the bucketing operation allows optimal spectral corrections and makes
comparison between spectra obtained from diﬀerent samples easier. Finally,
access to quantities such as standard deviation of the signal, min and max values,
allows a ﬁner description of the spectra.
13


## Page 14


From this material, a spectral ﬁngerprint of the searched molecule could be ﬁrst
determined from a two-by-two comparison of spectra with a presence/absence of
the searched compound, In this case the approach consisting in comparing by
ratio the standard deviation of buckets from spectra of COSY type showed to
be able to detect and extract the spectral features of the compound even at low
concentrations. Linear regression over the whole series of spectra was also used
to generate a faithful ﬁngerprint. One step regression as well as recursive feature
selection were used, and both proved to be eﬃcient in extracting a spectral
ﬁngerprint for both homonuclear and heteronuclear experiments (see ﬁgure 6
and S.I. S2).
Each experiment types can be used for the determination of the ﬁngerprint,
and COSY type and HSQC type experiments were explored. It is possible to
perform the same analysis on a concatenation of all experiments, however such an
approach did not provide a correct result, probably because of the heterogeneity
of the diﬀerent spectra types.
Conclusion
The program developed in this work represents an eﬃcient alternative for the
autonomous processing of a series of NMR data (1D and 2D) and contributes
eﬃciently to the discovery of structurally unknown molecules present in natural
extracts, without any chromatographic separation. It fully exploits the NMR
technique as a ﬁngerprinting technique: complete 2D NMR ﬁngerprint of the
compound is recovered through diﬀerential analysis performed both by com-
parison of local variation in the spectra or by linear regression between signal
intensity and the concentrations of the natural product in the sample.
The extended bucketing procedure allows a strong reduction of the size of the
data, while preserving a large part of the molecular information present in the
original spectra. Basic machine learning approaches were used to analyze this
compressed but rich information, and proved suﬃcient to readily extract the
spectral ﬁngerprint of the unknown molecule, either from spectral comparison,
or by handling of the whole spectral series at once.
Plasmodesma is a novel tool which should be useful to decipher complex mixtures,
particularly in the discovery of biologically active natural products from plants
extracts, but can also in drug discovery or metabolomics studies.
Acknowledgments
The authors are very grateful to Labex Medalis and Région Alsace for a fellowship
(LM), and Europe for an Erasmus fellowship (PM). We are also grateful to A-
M.Rusig for the collect and the identiﬁcation of the algal material, J.Viéville
14


## Page 15


for help in the NMR set-up, and G.Bret for help in the statistical analysis.
We acknowledge Wikimedia26 for the S.muticum picture used in the Graphical
Abstract.
E.S.I.
• S1 Processing of the artemisinin series
• S2 Analysis of the artemisinin series
References
[1] Bakiri, A.; Hubert, J.; Reynaud, R.; Lanthony, S.; Harakat, D.; Renault,
J.-H.; Nuzillard, J.-M. J Nat Prod. 2017, 80 (5), 1387–1396.
[2] D’Abrosca, B.; Lavorgna, M.; Scognamiglio, M.; Russo, C.; Graziani, V.;
Piscitelli, C.; Fiorentino, A.; Isidori, M. Food Chem Toxicol. 2017.
[3] Abdelsalam, A.; Mahran, E.; Chowdhury, K.; Boroujerdi, A.; El-Bakry, A.
Physiol Mol Biol Plants. 2017, 23 (2), 369–383.
[4] Hubert, J.; Nuzillard, J.-M.; Purson, S.; Hamzaoui, M.; Borie, N.; Reynaud,
R.; Renault, J.-H. Anal Chem. 2014, 86 (6), 2955–2962.
[5] Oettl, S.-K.; Hubert, J.; Nuzillard, J.-M.; Stuppner, H.; Renault, J.-H.;
Rollinger, J.-M. Anal Chim Acta. 2014, 846, 60–67.
[6] Larive, C. K.; Barding Jr, G. A.; Dinges, M. M. Anal Chem 2015, 87 (1),
133–146.
[7] Mahrous, E.; Farag, M. J Adv Research 2015, 6 (315).
[8] Wolfender, J.-L.; Marti, G.; Thomas, A.; Bertrand, S. J Chromatogr A. 2015,
1382, 136–164.
[9] Wikipedia. “Plasmodesma are microscopic channels which traverse the cell
walls of plant cells and some algal cells, enabling transport and communication
between them”. https://en.wikipedia.org/wiki/Plasmodesma, [Online; accessed
16-May-2017].
[10] Chiron, L.; Coutouly, M.-A.; Starck, J.-P.; Rolando, C.; Delsuc, M.-A. arXiv
2016.
[11] Pons, J. L.; Malliavin, T. E.; Delsuc, M.-A. J Biomol NMR 1996, 8, 445–452.
[12] Tramesel, D.; Catherinot, V.; Delsuc, M.-A. J Magn Reson 2007, 188 (1),
56–67.
[13] Pfändler, P.; Bodenhausen, G.; Rapin, J.; Houriet, R.; Gäumann, T. Chem
15


## Page 16


Phys Let 1987, 138 (2), 195–200.
[14] Pfändler, P.; Bodenhausen, G.; Rapin, J.; Walser, M.; Gäumann, T. J Am
Chem Soc 1988, 110 (17), 5625–5628.
[15] van Agthoven, M. A.; Delsuc, M.-A.; Bodenhausen, G.; Rolando, C. Anal
Bioanal Chem 2013, 405, 51–61.
[16] van der Walt, S.; Colbert, S.; Varoquaux, G. Comput Sci Eng 2011, 13,
22–30.
[17] Jones, E.; Oliphant, T.; Peterson, P.; Others. SciPy: Open source scientiﬁc
tools for Python, 2001.
[18] McKinney, W. Pandas, Python Data Analysis Library. 2015; Reference
Source, 2014.
[19] The HDF Group. Hierarchical Data Format, version 5.
[20] Alted, F.; Vilata, I.; others. PyTables: Hierarchical datasets in Python,
2002.
[21] Chiron, L.; van Agthoven, M. A.; Kieﬀer, B.; Rolando, C.; Delsuc, M.-A.
Proc Natl Acad Sci USA 2014, 111 (4), 1385–1390.
[22] Cherni, A.; Chouzenoux, E.; Delsuc, M.-A. Analyst 2017, 142 (5), 772–779.
[23] Vonthron-Sénécheau, C.; Kaiser, M.; Devambez, I.; Vastel, A.; Mussio, I.;
Rusig, A.-M. Mar. Drugs 2011, 9, 922–933.
[24] Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel,
O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; Vanderplas, J.; Passos,
A.; Cournapeau, D.; Brucher, M.; Perrot, M.; Duchesnay, E. Journal of Machine
Learning Research 2011, 12, 2825–2830.
[25] Clos, L. J.; Jofre, M. F.; Ellinger, J. J.; Westler, W. M.; Markley, J. L.
Metabolomics 2013, 9 (3), 558–563.
[26] Commons, W. File:Sargassum muticum yendo fensholt 1955 lamiot wim-
mereuxhautsdefrance estran juillet 2016a9.jpg — wikimedia commons, the free
media repository, 2016.
16


## Page 17


Supp.Info 1
17


## Page 18


Supporting	
  Information	
  
Automatic	
  differential	
  analysis	
  of	
  NMR	
  experiments	
  in	
  complex	
  samples	
  
Laure	
  Margueritte,	
  Petar	
  Markov,	
  Lionel	
  Chiron,	
  Jean-­‐Philippe	
  Starck,	
  Catherine	
  Vonthron-­‐
Sénécheau,	
  Mélanie	
  Bourjot,	
  Marc-­‐André	
  Delsuc*	
  
	
  
Spectra	
  of	
  sample	
  1	
  :	
  
S1	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S2	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S3	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S4	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S5	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S6	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
Spectra	
  of	
  sample	
  2	
  :	
  
S7	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S8	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S9	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S10	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S11	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S12	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
Spectra	
  of	
  sample	
  3	
  :	
  
S13	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S14	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S15	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S16	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S17	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S18	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
Spectra	
  of	
  sample	
  4	
  :	
  
S19	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 19


S20	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S21	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S22	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S23	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S24	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
Spectra	
  of	
  sample	
  5	
  :	
  
S25	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S26	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S27	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S28	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S29	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
S30	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 20


S1	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S2	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 21


S3	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S4	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 22


S5	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S6	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 23


S7	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S8	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 24


S9	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S10	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 25


S11	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S12	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 26


S13	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S14	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 27


S15	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S16	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 28


S17	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S18	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 29


S19	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S20	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 30


S21	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S22	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 31


S23	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S24	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 32


S25	
  -­‐	
  1H	
  NMR	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S26	
  -­‐	
  COSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 33


S27	
  -­‐	
  TOCSY	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S28	
  -­‐	
  HSQC	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 34


S29	
  -­‐	
  HMBC	
  spectrum	
  (MeOD,	
  700	
  MHz)	
  
	
  
S30	
  -­‐	
  DOSY	
  spectrum	
  (MeOD,	
  700	
  MHz)


## Page 35


Supp.Info 2
Supp Info 2 can be found at https://github.com/delsuc/plasmodesma/blob/master/Analysis.ipynb
35

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
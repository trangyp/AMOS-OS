---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.00770v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1902.00770v1_The_reliability_of_an_environmental_epidemiology_meta-analysis__a_case_study

> Source: 1902.00770v1_The_reliability_of_an_environmental_epidemiology_meta-analysis__a_case_study.pdf

> Pages: 19

---


## Page 1


The reliability of an environmental epidemiology meta-analysis, a case study 
S. Stanley Young, Mithun Kumar Acharjee, Kumer Das 
 
https://doi.org/10.1016/j.yrtph.2018.12.013 
Summary 
Background Claims made in science papers are coming under increased scrutiny with many 
claims failing to replicate. Meta-analysis studies that use unreliable observational studies should 
be in question. We examine the reliability of the base studies used in an air quality/heart attack 
meta-analysis and the resulting meta-analysis. 
Methods A meta-analysis study that includes 14 observational air quality/heart attack studies is 
examined for its statistical reliability. We use simple counting to evaluate the reliability of the 
base papers and a p-value plot of the p-values from the base studies to examine study 
heterogeneity. 
Findings We find that the based papers have massive multiple testing and multiple modeling 
with no statistical adjustments. Statistics coming from the base papers are not guaranteed to be 
unbiased, a requirement for a valid meta-analysis. There is study heterogeneity for the base 
papers with strong evidence for so called p-hacking. 
Interpretation We make two observations: there are many claims at issue in each of the 14 base 
studies so uncorrected multiple testing is a serious issue. We find the base papers and the 
resulting meta-analysis are unreliable. 
Funding The work of Young was partially funded by the American Petroleum Institute. The 
other researchers are unfunded.


## Page 2


Introduction 
A positive result for a single, sharp question that is examined in a randomized experiment is 
usually taken as evidence for causality. Replication increases confidence. Randomized studies 
are either not feasible or have not been done for many important questions, medical and 
environmental. Where randomized studies are not feasible, researchers often combine results 
from observational studies into a meta-analysis. It is thought that a meta-analysis will have 
improve reliability over and above what is available in any of the individual studies. In practice, 
is that true? Advice on how to conduct and report on a meta-analysis of observational studies is 
given by Stroup et al. (2000). These authors are largely silent assessing the reliability of the 
individual observational studies. 
  
Claims coming from many science disciplines fail to replicate, Horton (2015) among many 
others. The failure of observational studies to replicate is a well-known, old problem, Mayes et 
al. (1988). They looked at 56 questions that were examined by the case-control method and the 
papers divided roughly equally on each question. Clearly, half of the studies were wrong. 
Unlimited slicing and dicing of a data set as a problem has been long recognized, Cournot 
(1843). Feinstein (1988) restated the question and noted that not defining and not limiting the 
questions in a study was likely part of the problem. Rothman (1990) quickly asserted that 
multiple testing was not an issue, and many continue to subscribe to his position. More recently 
Perneger (1998) asserted “the view, widely held by epidemiologists, that Bonferroni adjustments 
are, at best, unnecessary and, at worst, deleterious to sound statistical inference.” Both Rothman 
and Perneger are highly cited by authors that want to leave no stone unturned and, to that end,


## Page 3


are happy to have any number of false positives, a position that is extremely self-serving for the 
producer and a disaster for the consumer. For a criticism of Rothman/Perneger, see Frane (in 
press). 
  
Using a statistical argument, Ioannidis (2005) asserted that 90% of sciences claims were 
expected not to replicate. Young and Karr (2011) found 12 randomized clinical studies where 52 
claims coming from observational studies were tested. None of the 52 claims were statistically 
significant in the claimed direction while five were significant, but in the opposite direction. 
Begeley and Ellis (2012) noted that 47 of 53 claims coming from experimental biology failed to 
usefully replicate. A Nature survey of ~1,500 scientists reported that 90% thought there was a 
crisis, 52% serious, 38% minor, Baker (2016). 
  
Three recent books, Hubbard (2015), Harris (2017) and Chambers (2017), henceforth referred to 
as HHC, discuss statistical, experimental and logical problems with current science. Multiple 
testing is one of the problems. If you ask a lot of questions and base your decisions on a 
statistically test at the 5% level, false positives are expected. Pejoratively, asking a lot of 
questions is called p-hacking. Head et al. (2015): “We used text-mining to search for p-values in 
all Open Access papers available in the PubMed.” and concluded that p-hacking is rife. Naming 
your hypothesis after the fact, letting the data suggest a hypothesis for any found result, is called, 
HARKing, Hypothesis After the Results are Known. The problems p-hacking and HARKing 
were noted, but not so named by Feinstein (1988). 
  
Standard science is to propose a single, sharp hypothesis before the fact and then collect data, 
either experimental or observational, to test the sharp hypothesis. Randomized clinical trials, as


## Page 4


supervised by the Food and Drug Administration, are a good example. Karl Popper is one of the 
great philosophers of science. His position was that a theory could not be proven correct, but 
could be tested by sharp, decisive experiments and proven wrong. HARKing is a total corruption 
of the (Popper) science process. 
  
Some assert that the p-value itself is the problem and that hypothesis testing needs to be 
abandoned, Wasserstein RL, Lazar NA. (2016) or that the significance level used needs to be 
dramatically reduced, Boos and Stefanski (2011) Johnson (2013),  0.001 and 0.005 respectively. 
These authors assume one, pre-planned question with careful attention to study design and study 
execution. Hubbard 2015 would move away from or abandon hypothesis testing altogether and 
concentrate on replication of findings as the path to reliable results. Any sharp decision rule 
should take multiple testing into account. We assert that a major problem is multiple testing. 
  
In this paper, we examine a meta-analysis study, Nawrot et al. (2011), hereafter Nawrot, where 
their focus is on the question: can Particulate Matter, PM, induce a heart attack? PM is 
ubiquitous and is an air component regulated by the US Environmental Protection Agency. PM 
is not chemically defined; physically, it consists of particles small enough to pass through a 10 
micron grid. Note that Nawrot assumes that PM10 is 70% PM2.5 (See their Table 3.), so their 
analysis applies to both.  Many observational studies show an association between PM and heart 
attacks (myocardial infarcts, Mis); 14 of these papers were collected by Nawrot. 
  
First, we examine the reliability of the 14 observational studies that deal with PM and that are 
used in the Nawrot meta-analysis study. We use simple counting to establish the size of the 
analysis search space available to the researchers. We look at the distribution of the results from


## Page 5


these papers, p-values, to evaluate the possibility of p-hacking/p-HACKing, building on ideas of 
Simonsohn et al. 2014. 
  
Methods 
Our methods involve simple counting for each base study to examine the analysis search space 
and the examination of the distribution of p-values across the studies using a p-value plot. We 
count the numbers of outcomes, predictors, covariates and lags and use those counts to 
approximate the analysis search space available to a researcher, the number of possible statistical 
tests. Many researchers think that air quality some days before the day at issue might give rise to 
a heart attack, hence the interest in lags. Mostly, this counting is easy, but it can take some time 
to count these features as the authors might mention some of the variables anywhere in the paper. 
Covariates are often given in different places and some available covariates might not be 
mentioned at all in the paper. 
  
The product of Outcomes, Predictors and Lags gives the number of questions at issue, Space_1. 
A covariate can be in the model or not so one way to approximate the modeling options is to 
raise 2 to the power of the number of covariates, Space_2. The product of Space_1 and Space_2 
gives an approximation to analysis total search space, Space_3. 
  
The meta-analysis researcher takes a summary statistic from each paper to combine in the meta-
analysis estimation of the effect in question. In this instance, the summary statistic is a risk ratio 
with confidence limits. For 12/14 studies, unadjusted p-values are reported; two studies note 
their results were not significant. Each base paper tested at the 0.05 level, ignoring multiple 
testing. The authors of Nawrot take the summary statistics and their p-values at face value. The 
14 risk ratios are taken from Nawrot, their Table 3 and their p-values are computed using their


## Page 6


95% confidence intervals. If there is no effect of PM10 on heart attacks, these p-values should 
follow a uniform distribution. The distribution of the p-values can be examined using a p-value 
plot, Schweder and Spjøtvoll (1982). In a p-value plot, the p-values are rank ordered from 
smallest to largest and plotted against the integers, 1, 2, 3, …, 14. If the p-values form a 45-
degree line, then that is evidence for randomness, no effect. The positioning of p-values in the 
distribution can be used to evaluate potential manipulation of the analysis process, Simonsohn et 
al. (2014); they worked with a limited the range of p-values, those less than or equal to 0.05 as 
those were the only ones reported in their literature. We have p-values across the whole interval, 
so we use them all in a p-value plot. 
  
Results 
Table 1 gives the counts of the outcomes, predictors, lags and covariates for the 14 papers. Table 
2 gives summary statistics for Space_1, Space_2 and Space_3. The median of Space_3, the 
number of possible analyses, is 6,784 with an interquartile range of 2,600 to 94,208. The 
modeling search space can be large. The authors of the 14 papers screened statistically using a p-
value of 0.05; the authors provide only very weak evidence to support their claims. Note that a 
small p-value due to chance will have an associated biased statistic. 
  
Table 3 gives the named covariates in the papers used by Nawrot. Some covariates are used a lot, 
e.g. age and sex, and some version of temperature/relative humidity, while others are particular 
to a paper. There is considerable variation in how weather variables are used. 
  
A p-value plot of the 14 p-values is given in Figure 1. We see many small p-values, but we also 
see p-values that roughly form a 45-degree line that are consistent with no effect. A test for a 
quadratic dose response gave a p-value of 0.00015, which supports a bi-linear response. The p-


## Page 7


values are heterogeneous; some are nominally statistically significant, while others appear to be 
random. 
  
Discussion 
  
A basic requirement of a meta-analysis that a statistic, mean value, risk ratio, etc., taken from a 
base paper and use in a meta-analysis be an unbiased estimate of the statistic of interest, Boos 
and Stefanski (2013). In the Nawrot meta-analysis, the authors took the estimates from the base 
papers at face value, which assumes that they are unbiased, and which we think is unsupported 
given the size of the search spaces in the base papers. The authors of the base papers have the 
responsibility to provide solid statistical evidence to support their statistically based claims. In all 
the base papers, statistical testing was at the 0.05 level while large numbers of claims were at 
issue. If the small p-value reported in the base paper is due to multiple testing/multiple modeling, 
then the associated statistic biased. The authors of the base papers provide no evidence that the 
small effects they report are anything but chance. In the 14 papers used by Nawrot to examine 
the relationship of PM10 to heart attacks, there was no adjustment for multiple testing. 
The distribution of the p-values from the base studies was evaluated using a p-value plot. If you 
take the p-values from each of the base questions and look at the distribution of them, you can 
evaluate the possibility of analysis manipulation. These observational studies are large and 
complex and the researcher can try alternative ways to do the analysis; some of these analysis 
might give a p-value less than 0.05, opening the door to publication.   
  
If when looking at multiple p-values, one from each analysis, you find many below the 
publishable 0.05, but the remaining p-values appear uniformly distributed between 0.05 and 
1.00, then you have a problem. Do you believe the small p-values or the not significant p-values?


## Page 8


IF there is a real effect, the non-significant ones should still be relatively small and still fall on a 
line with a slope less than 45 degrees. If p-values are bi-linear and the analysis search space is 
large, then there is evidence for analysis manipulation in the base papers. 
  
Editors and referees generally require a statistically significant result to support publication, 
HHC. Simonsohn et al. 2014 support this statement but go on to say that authors might search 
through many results until they find a significant p-value, p-HACKing. Also, authors might 
simply not submit a negative study, the file drawer problem, leading to publication bias. 
Is there additional support for a negative finding? Milojevic et al. (2014) looked at 
cardiovascular disease, CVD, events in all of England and Wales. “…over 2 million CVD 
emergency hospital admissions and over 600 000 CVD deaths” were linked to six air quality 
variables including PM2.5 and PM10 and tested for 11 cardiac diagnoses. Hospital admissions 
and mortality were analyzed. There were 6x11x2=132 questions at issue. Their Figures 1&2 are 
given here as our Figures 2&3. Percent change in hospital admissions and mortality are the y-
axes in the glyphs. Along the x-axis are given the standard air components, carbon monoxide 
(CO), nitrogen dioxide (NO2), particulate matter less than 10 μm in aerodynamic diameter 
(PM10), particulate matter less than 2.5 μm in aerodynamic diameter (PM10) and sulfur dioxide 
(SO2 ), and daily maximum of 8-hourly running mean of O3 measured at the nearest air 
pollution monitoring site to the place of residence. The results given for PM10 are consistent 
with randomness. Milojevic points to no effect of PM2.5 on heart attacks, RR= 1.003 with a p-
value of 0.36. 
  
Young et al. (2017) conducted a time series analysis of daily deaths for the eight most populated 
air basins in California. There is a total of over 37,000 exposure days. Three death classifications


## Page 9


were analyzed, AllCause, Cardiovascular, and Respiratory. They found no effect of PM2.5 on 
acute deaths. Our p-value plot analysis supports the no effect claims of Milojevic and Young and 
call into question association or causation of PM with heart attacks. 
  
In summary, the claims coming from the base papers used in the Nawrot meta-analysis are 
consistent with random results, those on the 45-degree line, and manipulated results, those on the 
blade of the hockey stick, while recent, large studies are consistent with no effect of PM2.5 on 
heart attacks. At this point, causality of PM10/PM2.5 on heart attacks is not supported. 
Contributors 
SSY designed the study. SSY, MKA and KD acquired, analysed, and interpreted data. SSY 
drafted the initial manuscript. SSY, MKA and KD edited the manuscript. 
 
Declaration of interests 
We declare no competing interests


## Page 10


References, Lancet, Air quality and health effects, references numbers from Nawrot. 
12 Barnett AG, Williams GM, Schwartz J, et al. The eﬀects of air pollution on hospitalizations 
for cardiovascular disease in elderly people in Australian and New Zealand cities. Environ 
Health Perspect 2006; 114: 1018–23. 
 
13 Zanobetti A, Schwartz J. Air pollution and emergency admissions in Boston, MA. J 
Epidemiol Community Health 2006; 60: 890–95. 
 
14 Zanobetti A, Franklin M, Koutrakis P, Schwartz J. Fine particulate air pollution and its 
components in association with cause-speciﬁc emergency admissions. Environ Health 2009;8:58. 
 
15 Peters A, von Klot S, Heier M, et al. Particulate air pollution and nonfatal cardiac events. Part 
I. Air pollution, personal activities, and onset of myocardial infarction in a case-crossover study. 
Res Rep Health Eﬀ Inst 2005; 124: 1–66. 
 
20 Lanki T, Pekkanen J, Aalto P, et al. Associations of traﬃc related air pollutants with 
hospitalisation for ﬁrst acute myocardial infarction: the HEAPSS study. Occup Environ Med 
2006;63:844–851. 
 
21 Cendon S, Pereira LA, Braga AL, et al. Air pollution eﬀects on myocardial infarction. Rev 
Saude Publica 2006;40:414–419. 
 
22 Peters A, von Klot S, Heier M, et al. Exposure to traﬃc and the onset of myocardial 
infarction. N Engl J Med 2004;351:1721–1730. 
 
40 Koken PJ, Piver WT, Ye F, Elixhauser A, Olsen LM, Portier CJ. Temperature, air pollution, 
and hospitalization for cardiovascular diseases among elderly people in Denver. Environ Health 
Perspect 2003; 111: 1312–17. 
 
41 Linn WS, Szlachcic Y, Gong H Jr, Kinney PL, Berhane KT. Air pollution and daily hospital 
admissions in metropolitan Los Angeles. Environ Health Perspect 2000;108:427–34. 
 
42 Mann JK, Tager IB, Lurmann F, et al. Air pollution and hospital admissions for ischemic 
heart disease in persons with congestive heart failure or arrhythmia. Environ Health 
Perspect2002; 110: 1247–52. 
 
43 Peters A, Dockery DW, Muller JE, Mittleman MA. Increased particulate air pollution and the 
triggering of myocardial infarction. Circulation2001;103:2810–15. 
 
44 Pope CA, Muhlestein J, May H, Renlund D, Anderson J, Horne B. Ischemic heart disease 
events triggered by short-term exposure to fine particulate air pollution. Circulation 
2006;114:2443–2448.


## Page 11


45 Sullivan J, Sheppard L, Schreuder A, Ishikawa N, Siscovick D, Kaufman J. Relation between 
short-term fine-particulate matter exposure and onset of myocardial infarction. 
Epidemiology2005;16:41–48. 
 
46 Ye F, Piver WT, Ando M, Portier CJ. Effects of temperature and air pollutants on 
cardiovascular and respiratory diseases for males and females older than 65 years of age in 
Tokyo, July and August 1980–1995. Environ Health Perspect 2001;109:355–359. 
 
47 Zanobetti A, Schwartz J. The eff ect of particulate air pollution on emergency admissions for 
myocardial infarction: a multicity case-crossover analysis. Environ Health Perspect 2005; 
113: 978–82. 
 
 
References, General 
References 
1       Baker M. Is there a reproducibility crisis? Nature 2016; 533: 452-454. 
  
2       Begley CG, Ellis LM. Drug development: raise standards for preclinical cancer research. 
Nature 2012; 483: 531–533. 
3       Boos DD, Stefanski LA. P-value precision and reproducibility. The American Statistician 
2011: 65: 213-221. 
4       Boos DD, Stefanski LA. Essential Statistical Inference: Theory and Methods. New 
Yourk: Springer, 2013. 
  
5       Cournot AA. Exposition de la theorie des chance des probability. Paris, France: Librairie 
de L’Hachette,1843. 
  
6       Chambers C. The Seven Deadly Sins of Psychology. New Jersey: Princeton University 
Press, 2017. 
7       Ehm W. Reproducibility: Principles, Problems, Practices, and Prospects. New York: 
Wiley, 2016. 
8       Feinstein AR. Scientiﬁc standards in epidemiologic studies of the menace of daily life. 
Science 1988; 242: 1257-1263.


## Page 12


9       Greven S, Dominici F, Zeger S. An approach to the estimation of chronic air pollution 
effects using spatio-temporal information. Journal of the American Statistical Association, 2011; 
106: 396-406. 
  
10     Frane, A. V. Misguided opposition to multiplicity adjustment remains a problem. Journal 
of Modern Applied Statistical Methods, in press. 
11     Harris R. Rigor mortis: how sloppy science creates worthless cures, crushes hope, and 
wastes billions. New York: Basic books, 2017. 
12     Head ML, Holman L, Lanfear R, Kahn AT, Jennions, MD. The extent and consequences 
of p-hacking in science. PLoS Biol 2015; 13(3): e1002106. 
  
13     Hubbard R. Corrupt Research. London: Sage Publications, 2015. 
  
14     Ioannidis JPA. Contradicted and initially stronger effects in highly cited clinical research. 
JAMA 2005; 294: 218–228. 
  
15     Johnson V. Revised Standards for Statistical Evidence. Proceedings of the National 
Academy of Sciences of the United States of America 2013; 110: 19313-19317. 
16     Mayes LC, Horwitz RI, Feinstein, AR. A collection of 56 topics with contradictory 
results in case-control research.  International Journal of Epidemiology 1988; 17: 680-685. 
  
17     Milojevic A, Wilkinson P, Armstrong B, Bhaskaran K, Smeeth L, Hajat S. Short-term 
effects of air pollution on a range of cardiovascular events in England and Wales: case-crossover 
analysis of the MINAP database, hospital admissions and mortality. Heart 2014; 100: 1093-
1098. 
  
19     Perneger TV. What's wrong with Bonferroni adjustments. The BMJ 1998; 316(7139): 
1236–1238. 
  
20     Rothman KJ. No adjustments are needed for multiple comparisons. Epidemiology 1990; 
1(1): 43–46. 
  
21     Schweder T, Spjøtvoll E. Plots of p-values to evaluate many tests simultaneously. 
Biometrika 1982; 69: 493–502.


## Page 13


22     Simonsohn U, Nelson LD, Simmons JP. P-Curve: A Key to the File-Drawer. Journal of 
Experimental Psychology: General 2014; 143: 534–547. 
  
23     Stroup DF, Berlin JA, Morton SC, Olkin I, Williamson GD, Rennie D, Moher D, Becker  
BJ, Sipe TA, Thacker SB. Meta-analysis of observational studies in epidemiology: a proposal for 
reporting Meta-analysis of Observational Studies in Epidemiology (MOOSE) group. Journal of 
the American Medical Association, 2000; 283: 2008-2012. 
24     Wasserstein RL, Lazar NA. The ASA's Statement on p-Values: Context, Process, and 
Purpose. The American Statistician 2016; 70: 215-220. 
24     Young SS, Karr A. Deming, data and observational studies: a process out of control and 
needing ﬁxing. Signiﬁcance 2011; 8: 122-126. 
  
25     Young SS, Smith RL, Lopiano KK. Air quality and acute deaths in California, 2000-
2012. Regulatory Toxicology and Pharmacology 2017; 88: 173-184.


## Page 14


Table 1. Authors, variable counts, and analysis search spaces for the 14 Nawrot base papers. The 
number before the author name is the Nawrot reference number. 
Author 
Outcomes Predictors Lags Covars Space_1 
 
Space_2  
 
Space_3  
12 Barnett 
7 
4 
1 
13 
28 
   
8,192  
   
229,376  
13 Zanobetti 
2 
6 
2 
7 
24 
   
128  
   
3,072  
14 Zanobetti 
5 
19 
1 
5 
95 
   
32  
   
3,040  
15 Peters 
2 
6 
13 
12 
156 
   
4,096  
   
638,976  
20 Lanki 
2 
5 
4 
5 
40 
   
32  
   
1,280  
21 Cendon 
2 
5 
1 
6 
10 
   
64  
   
640  
40 Koken 
5 
6 
10 
5 
300 
   
32  
   
9,600  
41 Linn 
10 
4 
2 
8 
80 
   
256  
   
20,480  
42 Mann 
21 
4 
7 
9 
588 
   
512  
   
301,056  
43 Peters 
1 
7 
2 
5 
14 
   
32  
   
448  
44 Pope 
1 
2 
7 
9 
14 
   
512  
   
7,168  
45 Sullivan 
4 
4 
3 
10 
48 
   
1,024  
   
49,152  
46 Ye 
8 
5 
5 
5 
200 
   
32  
   
6,400  
47 Zanobetti 
5 
2 
4 
7 
40 
   
128  
   
5,120


## Page 15


Table 2 Summary statistics for the number of possible analyses using the three search spaces. 
 
Statistics 
Space_1 
Space_2 
Space_3 
maximum 
588.0 
8,192 
638,976 
quartile 
167.0 
640 
94,208 
median 
44.0 
128 
6,784 
quartile 
21.5 
32 
2,600 
minimum 
10.0 
32 
448


## Page 16


Table 3. Named covariates used in studies. 
Paper 
Covariates 
12 Barnett 
Age, Sex, Region, T, T-1, RH, AP, DOW, HotDays, ColdDays, HD, HD-1, Rain 
13 Zanobetti 
Age, Sex, T, AT, RH, DOW, season 
14 Zanobetti 
T, DPT, Trend, Season, Year 
15 Peters 
Age, Sex, T, Occupational status, Educational status, Smoking status, Hospital 
location, DOW, HOD, Season, Location, Symptoms of MI  
20 Lanki 
Age, Sex, T, Season, Case fatality 
21 Cendon 
mT, mT-1, RH, RH-1, DOW, Trend 
40 Koken 
Age, Sex, T, DPT, DOW 
41 Linn 
Age, Sex, T, RH, AP, Race, Region, Season 
42 Mann 
Age, Sex, mT, RH, DOW, Year, Trend, Region, Day of Study 
43 Peters 
Age, Sex, mT, RH, MH 
44 Pope 
Age, Sex, T, DPT, Smoking status, BMI, Region, MH, Clearing index 
45 Sullivan 
Age, Sex, T, RH, DOW, Race, BMI, Smoking status, MH, Season 
46 Ye 
Age, Sex, MT, mT, Trend  
47 Zanobetti 
Age, Sex, AT, AT-1, DOW, Season, Region


## Page 17


03 Figures 
Figure 1. P-value plot, ranked p-values plotted against the integers. 
 
Note that two p-values were declared not significant in Nawrot, but p-values were not given so 
two not significant p-values are not plotted.


## Page 18


Figure 2.


## Page 19


Figure 3.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
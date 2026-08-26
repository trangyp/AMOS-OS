---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1704.06112v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1704.06112v3_Exploratory_and_Confirmatory_Factor_Analyses_of_Religiosity__A_Four-Factor_Conce

> Source: 1704.06112v3_Exploratory_and_Confirmatory_Factor_Analyses_of_Religiosity__A_Four-Factor_Conce.pdf

> Pages: 16

---


## Page 1


Exploratory and Confirmatory Factor Analyses of Religiosity:
A Four-Factor Conceptual Model
Carlos Miguel Lemos1*, Ross Joseph Gore2, F. LeRon Shults3,4
1 Institute for Religion, Philosophy and History, University of Agder, Kristiansand,
Norway
2 Virginia Modeling, Analysis and Simulation Center, Old Dominion University,
Norfolk, VA, United States of America
3 Institute for Global Development and Planning, University of Agder, Kristiansand,
Norway
4 Center for Modeling Social Systems at NORCE, Kristiansand, Norway
* carlos.lemos@uia.no
Abstract
We describe an exploratory and confirmatory factor analysis of the International Social
Survey Programme Religion Cumulation (1991-1998-2008) data set. The exploratory
factor analysis was performed using data from the first two waves (1991 and 1998), and
led to the identification of four factors which we labeled “Religious formation,”
“Supernatural beliefs,” “Belief in God,” and “Religious practice.” The confirmatory
factor analysis was run using data from 2008, and led to results consistent with the
four-factor structure obtained in the previous step. We also run a set of structural
equation models in an attempt to find whether this procedure could suggest causality
links among the three factors related to the respondents’ current religiosity, given the
known causal precedence of “Religious formation.” The two SEMs with best fit suggest
that religious practice influences beliefs more than the latter influence practice, but no
causal precedences can be inferred from this result.
1
Introduction
Religion has traditionally played a central role in human societies, shaping both
personal development and cultural change. The complexity and diversity of religious
phenomena have led to long-standing debates among scholars about how to
conceptualize and measure “religiosity.” The scientific study of these highly contested
and extremely complicated phenomena calls for a multidisciplinary approach
encompassing fields as diverse as cognitive science, evolutionary biology, moral
psychology, anthropology, sociology, and political science [1].
Several researchers have utilized statistical analyses of large data sets based on large
scale surveys such as the World Values Survey (WVS), the European Values Survey
(EVS) or the International Social Survey Programme (ISSP). For example, Gervais and
Najle [2] used three variables in the WVS related to belief in God, religious upbringing
and attendance to services to show, via a signal detection approach, that religious
upbringing has a strong influence on later belief in God. Norris and Inglehart [3]
presented a conceptual scheme connecting a number of hypotheses for explaining
secularization ( [3], Fig. 1.1, page 15), which they define as the erosion of religious
1
arXiv:1704.06112v3  [stat.AP]  11 Jun 2019


## Page 2


participation, values and beliefs. They classify the latter as “indicators of religiosity”
( [3], Table 2.1, page 41). Their factor analysis in Table 7.1 of [3] describes three factors
of “Work Ethic,” but no attempt was made to carry out a corresponding analysis on the
religiosity “indicators.” Inglehart and Welzel [4,5] used sets of selected variables in the
WVS, EVS and ISSP to provide supporting evidence for their theories on secularization
and the human development path (both of which are related to religion). More recently,
Doebler has identified three “dimensions” of religion (believing, belonging, and
attendance) based on a multilevel analysis of the EVS [6].
However, none of the previous works was specifically directed towards the
quantitative description of the core factors of individual religiosity, using a sufficiently
representative set of variables related to attitudes and opinions about religion.
Moreover, none of these studies applied the methods of factor analysis and structural
equation modeling (SEM) in a systematic way. For example, the three indicators of
religiosity considered by Norris and Inglehart [3] were not proven to be factors of
religiosity derived from statistical methods. Another problem is that even when factor
analyses are used in the scientific study of religion, scholars rarely present detailed
descriptions of the criteria used for acceptance or rejection of items and factors, the
sequence of the elimination process, or estimates of reliability and goodness of fit for the
solutions obtained.
In this article, we describe exploratory and confirmatory factor analyses of 34
selected variables in the ISSP Religion Cumulation data set [7], which combines the
results from three waves of questionnaires on religion for years 1991, 1998 and 2008.
The work was performed in three stages. First, we ran an exploratory factor analysis
(EFA) using the first two waves (1991 and 1998). In this way we identified four factor
that we labeled “Supernatural beliefs,” “Religious formation,” “Belief in God,”
“Religious practice” and “Religious formation,” the first three related to the respondent’s
current religiosity. Then, we used the last wave (2008) to run a confirmatory factor
analysis (CFA), as EFA and CFA should be based on different data [8]. This led to
results consistent with those obtained in the first stage. Finally, we ran different
structural equation models (SEMs) in an attempt to determine the causal relationships
between the factors related to the current religiosity, taking into account the causal
precedence of “Religious formation.”
2
Methods
2.1
Description of the ISSP Religion Cumulation Data Set.
Selected Variables
The ISSP Religion Cumulation data set [7] contains the cumulated variables of the ISSP
“Religion” surveys of 1991, 1998 and 2008 and comes in two separate files: a main file
(ZA5070) with topic-related and background variables that appear in at least two
surveys, and an add-on file (ZA5071) with variables that could not be cumulated for
various reasons. The analysis in this article is based on the information in main file,
which includes 122 variables (fields) for 102454 respondents from 28 countries. Only the
countries that participated in at least two surveys (1998 and 2008) were included in the
cumulation data file. For Germany and the United Kingdom two subsamples were
included (East and West German, and Great Britain and Northern Ireland,
respectively). Details on the contents, structure and coding of the ZA5070 cumulation
file can be found in [9].
Because of its size, the variables included and the proportion of valid respondents’
answers, the ISSP Religion Cumulation data set is very valuable for extracting
information about religious beliefs, practices and values. However, the ISSP “Religion”
2


## Page 3


surveys have the important limitation that they mostly cover Christian Catholic,
Protestant and Orthodox countries. Although Israel and Japan also contributed, there
is no information from Muslim countries, India or China.
Table 1 shows the initial set of questions selected for the exploratory factor analysis
as well as the variables’ labels, number of valid levels and indication of score reversal.
First, we identified the questions about religious beliefs, practices, and values that were
most clearly related to the scientific study of religion, as well as others related to
attitudes and values influenced by religiosity and confidence in churches and secular
institutions. Finally, we also selected demographic variables that could help exploring
other aspects often considered in the scientific study of religion such as age, gender and
educational level.
2.2
Software Tools
The data processing was done using R [10]. Functions were written to import the
ZA5070 v1-0-0.dta Stata file and generate a R data frame, and to perform frequent
queries and operations (retrieving a set of fields corresponding to selected questions, the
records for a particular year and country or set of countries, etc.).
Exploratory factor analysis was done using the psych package [11]. Confirmatory
factor analysis of the four reliable and strongly correlated factors of religiosity found in
the exploratory factor analysis was done using lavaan [12]. The structural equation
modeling (SEM) analysis was done using lavaan as well.
2.3
Data Preparation
The R data frame generated from the ZA5070 v1-0-0.dta Stata file was split in two
data frames, one including the data from years 1991 and 1998 with 61928 records and
another the data from year 2008 with 40526 records, so as to run EFA and CFA with
distinct data.
The data preparation was done in the following steps (identical for EFA, CFA and
SEMs).
First the selected variables were converted to ordered factors except AGE and SEX
which were converted to numeric and unordered factor (categorical, nominal)
respectively. Then, all ordinal variables were inspected to mark invalid/inconclusive
answers as NA and remove spurious factor levels (e.g. levels for which no answer was
recorded. After that, the ordinal variables were further inspected for score reversal.
Table 1 shows the questions for which the scores were reversed.
In the EFA stage we computed the correlation matrices using three different
methods via the psych::mixed.cor function: Pearson (simplest), Spearman, and
mixed Spearman/polychoric with polychoric correlations being used for variables with
up to six levels (inclusive). It was found that the differences between the correlation
matrices computed using the three methods were negligible and Pearson correlation
produced marginally better factor solutions.Therefore, all variables were converted to
numeric in a final stage, which allowed faster and more efficient computation of EFA,
CFA and SEMs.
2.4
Exploratory Factor Analysis Method
The EFA was done in two stages. In the first stage we computed factor solutions and
eliminated variables (items) with low communality and low or cross-loadings [8], until
all variables met the acceptance criteria described below, and a statistically significant
and theoretically meaningful solution was found. This process was iterative, for
removing variables also led to changes in the optimal number of factors to be extracted
3


## Page 4


Table 1. Initial set of selected variables in the ISSP Religion Cumulation data set: variables’ names, labels,
number of valid levels and indication of polarity inversion.
Variable
Question label
Number of
valid levels
Score
reversed
V11
Sexual.relations.before.marriage
4
Yes
V12
Sexual.relations.with.someone.other.than.spouse
4
Yes
V13
Sexual.relations.between.two.adults.of.the.same.sex
4
Yes
V14
Opinion..Abortion.if.defect.in.the.baby
4
Yes
V15
Opinion..Abortion.if.family.has.very.low.income
4
Yes
V16
Husband.earn.money..wife.s.job.is.family
5
Yes
V20
Confidence.in.parliament
5
Yes
V21
Confidence.in.business.and.industry
5
Yes
V22
Confidence.in.churches.and.religious.organizations
5
Yes
V23
Confidence.in.courts.and.legal.system
5
Yes
V24
Confidence.in.schools.and.educational.system
5
Yes
V25
Religious.leaders.should.not.influence.vote
5
No
V26
Religious.leaders.should.not.influence.government
5
No
V27
Power.of.churches.and.religious.organizations
5
No
V28
Closest.to.Rs.belief.about.God
6
No
V29
Best.describes.beliefs.about.God
4
No
V30
Belief.in.life.after.death
4
Yes
V31
Belief.in.heaven
4
Yes
V32
Belief.in.hell
4
Yes
V33
Belief.in.religious.miracles
4
Yes
V35
God.concerns.Himself.with.human.beings
5
Yes
V37
Life.meaningful.because.God.exists
5
Yes
V46
R.child..mother.attend.church
9*
No
V47
R.child..father.attend.church
9**
No
V48
R.age.11.12..R.attend.church
9
No
V49
How.often.R.pray
11
No
V50
Take.part.in.church.activities
11
No
V51
R.describes.self.as.religious
7
Yes
V64
Modern.science.does.more.harm.than.good
5
Yes
V65
Too.much.trust.in.science
5
Yes
ATTEND
Attendance.of.religious.services
6
Yes
AGE
Age.of.respondent
-
-
SEX
Sex.of.respondent
2
-
DEGREE
Highest.education.level.degree
6
No
* The uppermost level “No mother/mother not present” was merged with the lowest level “Never.”
** The uppermost level “No father/father not present” was merged with the lowest level “Never.”
and consequently the variables’ communality and loadings. In the second stage, the
factors’ reliability was assessed using the criteria described below, and a factor solution
was computed using only the variables loading on the factors deemed reliable. This final
factor solution was found to meet all acceptance criteria and to be theoretically
meaningful, and the ensuing factor structure was then considered in the CFA and SEM
analyses.
The first stage consisted of the following steps:
1. Inspection of the correlation structure and estimation of the optimal number of
factors to be extracted;
4


## Page 5


2. Computation of the factor analysis solution for the recommended number of
factors as well as for one more and one less factor than recommended (i.e.
“bracketing” on the number of factors) [8];
3. Inspection of the factor solution for variables with low communality and weak or
cross loadings [13], [8];
4. Elimination of variables that did not meet the acceptance criteria, if any, and
re-doing the previous steps; otherwise, proceed to the second stage (inspection of
factors’ reliability).
To determine the recommended number of factors, we used the scree test, the Very
Simple Structure (VSS) and Velicer’s Minimum Average Partial (MAP) criteria, as well
as parallel analysis using psych::fa.paralell [11]. Parallel analysis consistently led to
better estimates for the number of factors than the other methods, and was therefore
the method of choice in the present work (bracketing on the number of factors as
described in the second step above also confirmed this finding).
The acceptance criteria for the variables were: i) communality > 0.40 [13]
(reference [8] recommends > 0.50); ii) loadings with absolute value > 0.32 (accounts for
at least 10% variance); and iii) no cross loadings (variables with loadings with absolute
value at 0.32 or higher on two or more factors [13]).
In the second stage, the factors obtained at the end of the first stage were inspected
for reliability, using Cronbach’s α [14] computed via the psych::alpha function. The
acceptance criteria for factors were α > 0.70 and at least three variables (items) loading
on them [8]. This last restriction is important for the subsequent CFA. Factors that
failed to meet these criteria were removed from the analysis by eliminating the variables
loading on them, and a final factor solution was computed and checked against all
acceptance criteria (for variables and factors).
We now describe further details necessary for the replication of the EFA reported
herein. The factor solutions were computed using psych::fa using data frames as
inputs (instead of correlation matrices). Correlations were estimated using the Pearson
coefficient (cor = ‘‘cor’’), as noted in the comment above on data preparation, with
pairwise complete observations and no imputation of missing values. Oblique rotations
(using the oblimin method, default in psych::fa) were used, since strong correlations
between factors were to be expected. The factor extraction was done using the
minimum residual method [15,16](default in psych::fa). We used one hundred
bootstrap iterations and specified a maximum of 2000 iterations for convergence. The α
level for confidence intervals of loadings and factor correlations was set to 0.01. The
remaining input parameters required by psych::fa were set to default values.
2.5
Confirmatory Factor Analysis Method
We used CFA to test the measurement and model of the four factors suggested in EFA,
i.e. to determine how well the measured variables represent the factors, and also to
inspect the correlation structure among the factors. We used the 2008 data to run the
CFA, since EFA and CFA should be done using independent data sets [8].
The CFA was done by first preparing the data as done for EFA. Then, the
measurement and structural models of the final four-factor solution obtained in EFA
were set up in and run in “lavaan” using lavaan::cfa. Following the standard
procedures in CFA, no cross loadings were permitted (measured variables were forced to
load on a single factor), and non null correlations between factors were allowed. The
GOF of the confirmatory model was assessed using several different estimators (as
described below) and the acceptance criteria were [8]: i) standardized loadings with
5


## Page 6


(absolute) value > 0.50; ii) average variance extracted (AVE) > 0.50; iii) reliability of
constructs (factors) > 0.70; and iv) standardized residuals of measured variables < 2.50.
The details necessary for the replication of our CFA are as follows. The
lavaan::cfa function was ran using a data frame of the variables loading on the four
factors obtained in EFA with the records for ISSP Religion 2008. The model was
specified so that each variable (item) loaded on a single factor. The scale of the latent
variables was set by fixing the factor loading of the first indicator to one (default in
lavaan::cfa). The estimator used was diagonally weighted least squares (DWLS) [17].
One hundred bootstrap iterations were used, as was done in EFA. The remaining
parameters required to run lavaan::cfa were set to their default values.
2.6
Structural Equation Modeling
Next, we used structural equation modeling (SEM) to organize the relationships among
the four factors obtained in EFA, taking into account that “Religious formation” has
causal precedence over the other three factors. SEM enables us to specify path diagrams
that hypothesize relationships among the four factors. Each diagram can be converted
into a model with two components [12]:
1. a measurement model that describes the relationship of factors and their
indicators (survey questions);
2. structural equations that depict regressions among factors as causal paths from
one factor to another.
Given a model, the structural equation modeling algorithm (lavaan::sem)
computes the values for parameters within the measurement model and structural
equation model that best match the observed data. The best parameters were estimated
using Full Maximum Likelihood Estimation (FML).
The χ2 is the statistical fit index used for assessing the GOF between the observed
and model-implied covariance structures for the best solution for the model parameters.
A χ2 that is not significant implies a model with good fit. However, achieving a χ2 that
is not significant for any model, regardless of fit quality, becomes increasingly difficult
as the size of the sample increases. Most SEMs are based on samples of size ˜200.
However, the sample size in our data set is measured in tens of thousands. Given the
size of our data set, identifying a χ2 that is not significant is exceptionally unlikely.
This is not uncommon. In situations where the sample size is large and the χ2 tests lead
to over-rejection, it is usual to evaluate the models’ fit using alternative fit indices
(AFIs), which belong to two categories: (1) absolute fit indices and (2) incremental fit
indices [18–21].
Absolute AFIs are based on the discrepancy between the observed and
model-implied covariance structure, and thus should be sufficiently small for a model to
have good fit. We used two absolute fit indices, namely the Root Mean Squared Error of
Approximation (RMSEA) and the Standardized Root Mean Square Residual (SRMR).
RMSEA is the standardized difference between the observed data and the SEM
predicted data, while SRMR is defined as the standardized difference between the
correlation of the observed data and the predictions of the SEM. Values of SRMR and
RMSEA < 0.08 reflect models with acceptable fit [18]. Incremental AFIs compare the
fit of a given SEM with that of a null (or independence) model that only estimates the
means and variances of the indicators (observed variables). The values of incremental
AFIs of a SEM range from 0 (no better than the null model) to 1 (corresponding to a
saturated model that predicts the observed variance-covariance matrix exactly). The
two incremental fit measures employed in the evaluation of SEMs are the Comparative
Fit Index (CFI) and Tucker-Lewis Index (TLI). Both apply penalties for including
6


## Page 7


additional parameters in the model, but the TLI applies a more severe penalty than the
CFI. Values of CFI and TLI > 0.95 reflect models with acceptable fit [18]. The TLI is
also referred to as Non-Normed Fit Index or (NNFI).
The details necessary for the replication of our SEM are as follows. The SEM was
done by first preparing the data as done for EFA and CFA. Then 588 different
candidate models were generated. Each model was fit using a data frame of the
variables, loading on the four factors obtained in EFA, with the records for ISSP
Religion 2008. The lavaan::sem function was run on the data with all function
parameters set to their default values. The quality of fit was assessed using the four fit
indices previously mentioned: CFI, TLI, RMSEA and SRMR.
3
Results
3.1
Exploratory Factor Analysis
As outlined above, EFA was done in two stages. The first stage started by computing
factor solutions using all variables in table 1 for a recommended (and best) twelve
factors. Examination of this solution according to the criteria outlined above led to the
exclusion of variables “V12,” “V16,” “V21,” “V24,” “AGE,” “SEX” and “DEGREE.” In a
second iteration, factor solutions were computed excluding these variables for a
recommended (and best) ten factors. This led to a third iteration in which variables
“V35,” “V37,” and “V64” were excluded and factor solutions were computed for a
recommended (and best) eight factors. Examination of the best eight-factor solution led
to further elimination of variables “V27” and “V65,” the first due to low communality
and the second because it did not load on any factor. The final iteration in stage one
consisted of computing factor solutions for a recommended eight factors, which led to
the best fit indexes.
Fig 1 shows the factor solution diagram for the eight-factor solution obtained at the
final iteration of the first stage of the EFA. Table 2 shows the reliability estimates for
the eight factors for several different estimators, computed using psych::alpha.
Table 2. Reliability estimates for the eight-factor solution obtained in the
first stage of EFA.
raw α
std. α
λ6
average r
S/N
ase
mean
sd
MR1
0.90
0.90
0.88
0.70
9.1
0.00065
2.5
1.0
MR2
0.87
0.87
0.82
0.69
6.5
0.00094
4.9
2.5
MR3
0.78
0.78
0.64
0.64
3.6
0.0017
2.1
1.1
MR4
0.73
0.74
0.58
0.58
2.8
0.0021
2.1
1.1
MR5
0.89
0.90
0.87
0.75
9.2
0.00075
3.8
1.4
MR6
0.56
0.57
0.48
0.31
1.3
0.0031
2.9
0.82
MR7
0.75
0.81
0.75
0.58
4.2
0.0015
3.5
2.3
MR8
0.62
0.63
0.46
0.46
1.7
0.003
2.3
1.1
Description: raw α is Cronbach’s estimate based on covariances; std. α is
Cronbach’s estimate based on correlations; λ6 is Guttman’s λ6 reliability coefficient;
average r is the average inter item correlation; S/N is the signal-to-noise ratio (or
ratio of reliable variance to unreliable variance); ase is α’s standard error; mean is the
mean of the summed scale constructed from the items; and sd is the standard deviation
of the total factor scores [11].
All factors in Fig. 1 are seen to have a clear meaning. MR1 can be labeled
“Supernatural beliefs;” MR2 “Religious formation;” MR3 “Religion and politics”
7


## Page 8


V32    − Belief.in.hell                                     
V31    − Belief.in.heaven                                   
V30    − Belief.in.life.after.death                         
V33    − Belief.in.religious.miracles                       
V46    − R.child..mother.attend.church                      
V47    − R.child..father.attend.church                      
V48    − R.age.11.12..R.attend.church                       
V29    − Best.describes.beliefs.about.God                   
V28    − Closest.to.Rs.belief.about.God                     
V51    − R.describes.self.as.religious                      
V26    − Religious.leaders.should.not.influence.government  
V25    − Religious.leaders.should.not.influence.vote        
ATTEND − Attendance.of.religious.services                   
V50    − Take.part.in.church.activities                     
V49    − How.often.R.pray                                   
V14    − Opinion..Abortion.if.defect.in.the.baby            
V15    − Opinion..Abortion.if.family.has.very.low.income    
V23    − Confidence.in.courts.and.legal.system              
V20    − Confidence.in.parliament                           
V22    − Confidence.in.churches.and.religious.organizations 
V13    − Sexual.relations.between.two.adults.of.the.same.sex
V11    − Sexual.relations.before.marriage                   
MR1
0.9
0.9
0.8
0.6
MR2
1
0.8
0.7
MR5
0.9
0.7
0.5
MR3
0.9
0.7
MR7
0.7
0.6
0.5
MR4
0.9
0.6
MR6
0.7
0.6
0.3
MR8
0.7
0.5
0.4
0.7
0.5
0.6
0.5
0.6
0.5
0.3
0.5
0.3
0.4
Fig 1. Factor solution diagram for the eight-factor solution. Factor solution diagram for the eight-factor solution
obtained in the EFA after the successive elimination of variables V12, V16, V21, V24, V27, V35, V37, V64, V65, AGE, SEX and
DEGREE, drawn using psych::fa.diagram. Standardized item loadings and correlation coefficients between factors lower than
0.32 (10% variance) are not represented.
(influence of religious leaders on vote and government); MR5 “Belief in God;” MR6
“Confidence in institutions;” MR7 “Religious practice;” and the two factors MR4 and
MR8 are related to “traditional values” (or “Conservatism”) with respect to opinions
about abortion and sex, respectively.
Inspection of table 2 shows that only factors MR1, MR2, MR5 and MR7 have
α > 0.7 and at least three variables loading on them, and therefore verify all acceptance
criteria stated above. Also, they are also the ones with top ratio of reliable to unreliable
variance (S/N). It should be noted that the factor MR2 (“Religious formation”) is
associated to Christian religion, in which attendance at regular church services involves
both men and women (contrary to the cas of Islam). also, the correlation between this
factor and MR1, MR5 and MR7 is due to causality. MR1, MR5 and MR7 can be
interpreted as “core” factors of the respondent’s current religiosity. Although the
diagram in Fig.1 is interesting for illustrating the correlation between religiosity and
attitudes and opinions about traditional values, confidence in institutions and the
relationship between religion and politics, we will not further address these aspects, and
from now on concentrate on the factors associated with current religiosity and early
religious socialization (MR”, “Religious formation”).
Fig. 2 shows the diagram for the four-factor model of religiosity. Table 3 shows the
8


## Page 9


V32 – Belief.in.hell
V32 – Belief.in.heaven
V30 – Belief.in.life.after.death
V33 – Belief.in.religious.miracles
V46 – R.child.mother.attend.church
V47 – R.child.father.attend.church
V48 – R.age.11.12..R.attend.church       
V29 – Best.describes.beliefs.about.God
V28 – Closest.to.Rs.belief.about.God
V51 – R.describes.self.as.religious
ATTEND – Attendance.of.religious.services
V50 -
Take.part.in.church.activities
V49 -
How.often.R.pray
MR1
MR2
MR3
MR4
0.41
0.52
0.62
0.69
0.63
0.56
0.91
0.90
0.74
0.64
0.96
0.77
0.67
0.94
0.70
0.54
0.76
0.70
0.50
Fig 2. Factor Diagram for the four factors of religiosity. Factor solution diagram for the four factors of religiosity
obtained at the final stage of EFA, using psych::fa.parallel. Standardized item loadings and correlation coefficients
between factors lower than 0.32 (10% variance) are not represented. All loadings and correlations are positive due to the
polarity inversions described in table 1. Factor labels: MR1 ⇐⇒“Supernatural beliefs;” MR2 ⇐⇒“Religious formation;”
MR3 ⇐⇒“Belief in God;” MR4 ⇐⇒“Religious practice.”
Additional information: Mean item complexity = 1.2; Tucker-Lewis Index (TLI) of factoring reliability = 0.99; Root
means square error of approximation (RMSEA) index = 0.034 with 90% confidence interval (0.033;0.035).
standardized factor loadings, communality, uniqueness and Hoffmann complexity
index [22,23] for all variables, and table 4 shows the corresponding estimates and 99%
confidence intervals for the factor correlations.
3.2
Confirmatory Factor Analysis
Fig. 3 shows the path diagram of the standardized parameter estimates obtained in
CFA of a model built upon the four factors of religiosity identified in EFA and the
variables (items) loading on them, using the procedure and settings described in the
“Methods” section above. The CFA was computed using lavaan:cfa, which converged
after 76 iterations, using 23636 out of 40526 observations.
9


## Page 10


Table 3. Standardized factor loadings (pattern matrix), communality (h2),
uniqueness (u2) and Hoffmann’s item complexity (com) (see e.g. [22,23])
for the four-factor model of individual religiosity.
MR1
MR2
MR3
MR4
h2
u2
com
V30
0.74
-0.03
0.07
0.01
0.61
0.39
1.0
V31
0.90
0.01
0.05
-0.01
0.88
0.12
1.0
V32
0.91
0.03
-0.09
0.00
0.74
0.26
1.0
V33
0.64
0.00
0.10
0.07
0.57
0.43
1.1
V46
0.02
0.96
-0.02
-0.05
0.87
0.13
1.0
V47
0.04
0.77
-0.04
0.07
0.65
0.35
1.2
V48
-0.08
0.67
0.18
0.10
0.64
0.36
1.2
V28
0.16
0.00
0.70
0.09
0.77
0.23
1.1
V29
0.01
0.05
0.94
-0.05
0.89
0.11
1.0
V51
0.05
0.01
0.54
0.30
0.65
0.35
1.6
V49
0.11
0.05
0.31
0.50
0.70
0.30
1.8
V50
0.05
-0.04
-0.09
0.70
0.44
0.56
1.0
ATTEND
0.02
0.12
0.04
0.76
0.75
0.25
1.1
Factor labels:
MR1 ⇐⇒“Supernatural beliefs;” MR2 ⇐⇒“Religious formation;”
MR3 ⇐⇒“Belief in God;” MR4 ⇐⇒“Religious practice.”
Table 4. Factor correlations and 99% confidence intervals estimated via
bootstrap iterations.
lower
estimate
upper
MR1-MR2
0.40
0.41
0.42
MR1-MR3
0.68
0.69
0.69
MR1-MR4
0.62
0.63
0.64
MR2-MR3
0.51
0.52
0.53
MR2-MR4
0.55
0.56
0.57
MR3-MR4
0.61
0.62
0.63
Factor labels:
MR1 ⇐⇒“Supernatural beliefs;” MR2 ⇐⇒“Religious formation;”
MR3 ⇐⇒“Belief in God;” MR4 ⇐⇒“Religious practice.”
Table 5. Reliability estimates for the CFA model computed using the
semTools::reliability function.
Supernatural
beliefs
Religious
formation
Belief
in God
Religious
practice
α
0.903
0.891
0.892
0.774
ω1
0.904
0.892
0.912
0.845
ω2
0.904
0.892
0.912
0.845
ω3
0.905
0.893
0.916
0.838
AVE
0.703
0.734
0.781
0.682
Additional information:
α is Cronbach’s reliability coefficient. The theoretical
description of the ω1, ω2 and ω3 coefficients can be found in [24], [25] and [26]
respectively.
Table 5 shows some reliability estimates for the CFA model. Combining the
information presented in Fig. 3 and table 5, it can be observed that the factors’
10


## Page 11


0.80
0.90
0.82
0.83
0.88
0.82
0.88
0.90
0.86
0.87
0.90
0.54
0.83
0.36
0.20
0.33
0.31
0.23
0.33
0.23
0.19
0.26
0.24
0.20
0.71
0.31
1.00
1.00
1.00
1.00
0.51
0.81
0.77
0.63
0.68
0.85
V30 − Belief.in.life.after.death         
V31 − Belief.in.heaven                   
V32 − Belief.in.hell                     
V33 − Belief.in.religious.miracles       
V46 − R.child..mother.attend.church      
V47 − R.child..father.attend.church      
V48 − R.age.11.12..R.attend.church       
V28 − Closest.to.Rs.belief.about.God     
V29 − Best.describes.beliefs.about.God   
V51 − R.describes.self.as.religious      
V49 − How.often.R.pray                   
V50 − Take.part.in.church.activities     
ATTEND − Attendance.of.religious.services
Supernatural
beliefs
Religious
formation
Belief
in God
Religious
practice
Fig 3. Path Diagram for CFA of the four factor model of religiosity. Path diagram standardized parameter
estimates for CFA of the four factor model of religiosity computed with lavaan::cfa, drawn using semPlot::semPaths.
Additional information: Test statistic chi2 = 1773.56 with df = 59, p-value 0; Comparative fit index (CFI) = 0.997; TLI
= 0.997; RMSEA = 0.035; Normed Fit Index (NFI) = 0.997; Bentler-Bonett Nonnormed Fit Index (NNFI) = 0.997.
reliability and AVE meet the criteria stated the the “Methods” section. Therefore, the
four-factor model was further studied using SEMs to investigate how the fit measures
depend on other types of links (e.g. regression) between factors, in an attempt to
determine whether the SEMs suggested any clue about eventual causal precedences
between the factors related to the current religiosity, or to differences between the
effects of practice on each of the beliefs factors.
3.3
Structural Equation Modeling
The four-factor model analysed in the previous sections shows that the four factors are
correlated, and which items measure each of the factors. However, at the structural
level, “Religious formation” is not related to the current religiosity and is a causal
antecedent of the other three factors. Thus, we wanted to study whether the
re-specification of the structural model, keeping the same measurement model, would
change the fit measures and possibly suggest causal relations among the three factors
11


## Page 12


related to the current religiosity.
Next, we applied structural equation modeling (SEM) to organize the relationships
among the four clear and strongly correlated latent variables (MR1 - “Supernatural
beliefs;” MR2 - “Religious formation;” MR3 - “Belief in God;” MR4 - “Religious
practice”). Given our four factors it is possible to construct 588 SEMs. As explained in
the Methods section, we used four AFIs to assess the models’ fit: CFI, TLI, SRMR and
RMSEA.
Of these 588 SEMs, the two models that are consistent with the causal precedence of
the “Religious formation” factor and have the best fit measures are shown in Fig. 4. In
addition, the models do not have invalid parameter values (negative residuals or
variances or correlations larger than 1.0). Furthermore, the regression coefficients, factor
loadings and covariances all have the expected sign (positive).
Fig 4. The two SEMs with the best measures for the four fit indices that are consistent with the causal
precedence of the “Religious formation” relative to the other three factors (related to beliefs and practice).
Table 6. Number of parameters, degrees of freedom, χ2 and fit indices for
the two best fitting SEMs that are consistent with the causal precedence of
the “Religious formation” relative to the other three factors (related to
beliefs and practice).
# Pars
df
χ2
CFI
TLI/NNFI
RMSEA
SRMR
Model 1
31
60
7729.068
0.968
0.958
0.074
0.034
Model 2
31
60
7729.068
0.968
0.958
0.074
0.034
The number of parameters (# Pars), degrees of freedom (DF) and four fit indices for
the two models are provided in Table 6. Table 7 provides several additional fit indices
for the models including the Bentler-Bonett Index or Normed Fit Index (NFI) and
upper and lower confidence intervals for the RMSEA. Based on the evaluation measures
shown in Table 6 and 7, none of the two models is statistically superior to the other.
12


## Page 13


Table 7. Additional fit indices for the two best fitting SEMs that are
consistent with the causal precedence of the “Religious formation” relative
to the other three factors (related to beliefs and practice). Upper and
Lower RMSEA are based on 90% confidence interval.
NFI
Lower RMSEA CI
Upper RMSEA CI
Model 1
0.967
0.072
0.075
Model 2
0.967
0.072
0.075
However, both models suggest that religious practice influences beliefs more than the
latter influence practice, but no causal precedences can be inferred from this result.
4
Discussion
The EFA and CFA analyses of the ISSP Religion Cumulation data described herein led
to the identification of four factors, one related to early religious socialization
(“Religious formation”) and three to the respondent’s current religiosity (“Supernatural
beliefs,” “Belief in God” and “Religious practice”).
The existence of two distinct factors of religious beliefs can be explained by the fact
that afterlife beliefs is related to death anxiety as postulated by thanatocentric
theories [27], whereas belief in God is culturally acquired and has different systemic and
psychological roots [28]. The strong correlation was found between factors such as belief
in the supernatural (and God) and attendance at religious services is not surprising.
The relationship between the tendency to believe in disembodied intentional forces and
the tendency to signal commitment to an in-group through ritual participation is
extremely well documented in fields such as the cognitive science of religion and cultural
anthropology [29–32].
The fit measures of the models shown in Fig. 4 are substantially worse that those of
the model shown in Fig. 3. Thus, while the four factors seem to be reliably measured by
the items suggested by the EFA, the levels of the three factors related to the current
religiosity are significantly affected by factors other than family attendance at regular
church services during the respondents’ formative years (“Religious formation”),
because the fit measures degraded when correlation paths were replaced by regression
paths from the latter factor to the other three.
4.1
Limitations
Factor analysis is very sensitive to a large number of aspects, such as the existence of
heterogeneous group structure(s) in the data (countries, religious groups, etc.), the way
the covariance structure is computed (Pearson, Spearman, Kendall-τ,
polychoric/tetrachoric/polyserial), the factor extraction methods in EFA, and the
estimation method used in CFA.
While methods similar to the ones described herein have been used in several works
that relate religiosity to indices that measure constructs such as existential security and
human development [3–5], researchers must be aware that these methods have
important limitations for cross-cultural analyses. In particular, they are not suitable for
performing more rigorous statistical comparisons between different groups (e.g.
nonreligious people and different Christian groups). This requires multi-group analysis
techniques that are substantially more complicated than the ones used in this work [33].
13


## Page 14


5
Conclusion
We performed exploratory and confirmatory factor analyses of religiosity based on ISSP
Religion Cumulation data set (1991-1998-2008). The EFA began with 34 selected
variables using the data for the 1991 and 1998 waves and led to the identification of four
factors, “Supernatural beliefs,” “Belief in God,” “Religious practice” and “Religious
formation,” the last of which is related to the frequency of family attendance at church
services during the respondents’ formative years and is causally precedent relative to the
other three factors. The latter represent different aspects of the respondents’ current
religiosity, whose meaning and inter-relation had already been documented in the
literature [27–32].
The measurement model of the four (or “1 + 3”) factors suggested was tested using
CFA based on the data for the 2008 wave. The resulting CFA model had good fit
measures, suggesting that the items loading on each factor provide reliable
measurements.
After the identification of the four factors using EFA and the confirmation of their
measurement indicators using CFA, we performed an exploration of the four-factor
model using SEMs, taking into account the causal precedence of the frequency of past
family attendance (“Religious formation”) relative to the other three factors related to
current religiosity, to investigate whether or not these would suggest any precedence
among the latter (although SEM do not prove causation). We found that when
correlation paths were replaced from regression paths from “Religious formation” the fit
measures degraded substantially. Thus, the levels of current religiosity seem to be
significantly affected by factors not considered in the SEMs. The two SEMs with best
fit suggest that religious practice influences beliefs more than the latter influence
practice, but no causal precedences can be inferred from this result.
Supporting Information
ISSP “Religion” cumulation of the years 1991, 1998 and 2008.
Available in
STATA (ZA5070 v1-0.0.dta) and SPSS (ZA5070 v1-0.0.sav) formats from:
https://dbk.gesis.org/dbksearch/sdesc2.asp?no=5070&db=e&doi=10.4232/1.10860.
Guide for the ISSP “Religion” Cumulation file (ZA5070 v1-0.0).
Guide for
the ISSP “Religion” cumulation of the years 1991, 1998 and 2008 with the variable
names and labels shown in table 1 is available from: http://zacat.gesis.org/
webview/index/en/ZACAT/ZACAT.c.ZACAT/ISSP.d.58/Cumulations.d.72/
International-Social-Survey-Programme-Religion-I-III-ISSP-1991-1998-2008-/
fStudy/ZA5070.
Acknowledgments
Funding for this research was provided by the Research Council of Norway (grant
#250449).
We would like to thank Saikou Diallo, Associate Research Professor at Old
Dominion University, for graciously offering us advice that helped hone our
methodology and analysis in this work.
14


## Page 15


References
1. Shults FL. Theology after the birth of God: atheist conceptions in cognition and
culture. Palgrave Macmillan; 2014.
2. Gervais WM, Najle MB. Learned faith: The influences of evolved cultural
learning mechanisms on belief in Gods. Psychology of Religion and Spirituality.
2015;7(4):327–335. doi:10.1037/rel0000044.
3. Norris P, Inglehart R. Sacred and Secular: Religion and Politics Worldwide.
Cambridge University Press; 2011.
4. Inglehart R, Welzel C. Modernization, Cultural Change, and Democracy: The
Human Development Sequence. Cambridge University Press; 2005.
5. Inglehart R, Foa R, Peterson C, Welzel C. Development, freedom, and rising
happiness: A global perspective (1981–2007). Perspectives on psychological
science. 2008;3(4):264–285.
6. Doebler S. Relationships between Religion and Intolerance towards Muslims and
Immigrants in Europe: A Multilevel Analysis. Review of Religious Research.
2014;56:61–68.
7. H¨ollinger F, Haller M, Bean C, Scholz K, Kelley J, Evans A, et al.. International
Social Survey Programme: Religion I-III - ISSP 1991-1998-2008; 2011. Available
from: https://doi.org/10.4232/1.10860.
8. Hair JF, Black WC, Babin BJ, Anderson RE. Multivariate Data Analysis. 7th ed.
Pearson; 2009.
9. GESIS - Data Archive for the Social Sciences. Guide for the ISSP “Religion”
cumulation of the years 1991, 1998 and 2008; 2011.
10. R Core Team. R: A Language and Environment for Statistical Computing; 2016.
Available from: https://www.R-project.org/.
11. Revelle W. psych: Procedures for Psychological, Psychometric, and Personality
Research; 2016. Available from: http://CRAN.R-project.org/package=psych.
12. Rosseel Y. lavaan: An R Package for Structural Equation Modeling. Journal of
Statistical Software. 2012;48(2):1–36.
13. Osborne JW, Costello AB. Best practices in exploratory factor analysis: Four
recommendations for getting the most from your analysis. Pan-Pacific
Management Review. 2009;12:131–146.
14. Cronbach LJ. Coefficient Alpha and the Internal Structure of Tests.
Psychometrika. 1951;16(3):297–334.
15. Comrey AL. The Minimum Residual Method of Factor Analysis. Psychological
Reports. 1962;11:15–18.
16. Zegers FE, ten Berge JMF. A Fast and Simple Computational Method of
Minimum Residual Factor Analysis. Multivariate Behavioral Research.
1983;18:331–340.
15


## Page 16


17. Baghdarnia M, Soreh RF, Gorji R. The Comparison of Two Methods of
Maximum Likelihood (ML) and Diagonally Weighted Least Squares (DWLS) in
Testing Construct Validity of Achievement Goals. Journal of Educational and
Management Studies. 2014;4:22–38.
18. Hu Lt, Bentler PM. Cutoff criteria for fit indexes in covariance structure analysis:
Conventional criteria versus new alternatives. Structural equation modeling: a
multidisciplinary journal. 1999;6(1):1–55.
19. Steiger JH. Understanding the limitations of global fit assessment in structural
equation modeling. Personality and Individual differences. 2007;42(5):893–898.
20. Bentler PM. On tests and indices for evaluating structural models. Personality
and Individual differences. 2007;42(5):825–829.
21. Iacobucci D. Structural equations modeling: Fit indices, sample size, and
advanced topics. Sample Size, and Advanced Topics. 2010;.
22. Hofmann RJ. Indices Descriptive of Factor Complexity. The Journal of General
Psychology. 1977;96:103–110.
23. Pettersson E, Turkheimer E. Item selection, evaluation, and simple structure in
personality data. Journal of Research in Personality. 2010;44:407–420.
24. Raykov T. Estimation of congeneric scale reliability using covariance structure
analysis with nonlinear constraints. British Journal of Mathematical and
Statistical Psychology. 2001;54:315–323.
25. Bentler PM. Alpha, dimension-free, and model-based internal consistency
reliability. Psychometrika. 2009;74:137–143.
26. McDonald RP. Test Theory: A Unified Approach. Lawrence Erlbaum Associates;
1999.
27. Jong J, Halberstadt J. Death Anxiety and Religious Belief: An Existential
Psychology of Religion. London: Bloomsbury Academic; 2016.
28. Norenzayan A. Big questions about Big Gods : response and discussion. Religion,
Brain & Behavior. 2015;5(4):327–342. doi:10.1080/2153599X.2014.928359.
29. Atran S. In Gods We Trust: The Evolutionary Landscape of Religion. Cambridge
University Press; 2002.
30. McCauley RN, Lawson ET. Bringing Ritual to Mind: Psychological foundations
of Cultural Forms. Cambridge University Press; 2002.
31. Whitehouse H. Modes of Religiosity: A Cognitive Theory of Religious
Transmission. Walnut Creek, CA: Altamira Press; 2004.
32. Martinez BC. Is Evil Good for Religion? The Link between Supernatural Evil
and Religious Commitment. Review of Religious Research. 2013;55(2):319–338.
doi:10.1007/s13644-012-0094-x.
33. Lemos CM, Gore RJ, Puga-Gonzalez I, Shults FL. Dimensionality and factorial
invariance of religiosity among Christians and the religiously unaffiliated: A
cross-cultural analysis based on the International Social Survey Programme.
PLoS ONE. 14(5): e0216352. doi:10.1371/journal.pone.0216352.
16

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1704_06112v3_exploratory_and_confirmatory_factor_analyses_of_religiosity_a_four_factor_conce
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1704_06112V3_EXPLORATORY_AND_CONFIRMATORY_FACTOR_ANALYSES_OF_RELIGIOSITY_A_FOUR_FACTOR_CONCE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

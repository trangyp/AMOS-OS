---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.09765v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.09765v1_Mixture_survival_models_methodology__an_application_to_cancer_immunotherapy_asse

> Source: 1911.09765v1_Mixture_survival_models_methodology__an_application_to_cancer_immunotherapy_asse.pdf

> Pages: 24

---


## Page 1


1 
 
 
 
 
MIXTURE SURVIVAL MODELS METHODOLOGY: AN APPLICATION TO 
CANCER IMMUNOTHERAPY ASSESSMENT IN CLINICAL TRIALS 
 
Lizet Sánchez1*, Patricia Lorenzo-Luaces1, Claudia Fonte2, Agustin Lage1 
 
 
1 Clinical Research Division, Center of Molecular Immunology, Calle 216 esq 15. 
Atabey, Havana 11600, Cuba 
2 Faculty of Mathematics and Computing. University of Havana, San Lazaro y L, 
Havana, Cuba 
 
*Corresponding author: 
email: lsanchez@cim.sld.cu


## Page 2


2 
 
Abstract 
Progress in immunotherapy revolutionized the treatment landscape for advanced 
lung cancer, raising survival expectations beyond those that were historically 
anticipated with this disease. In the present study, we describe the methods for 
the adjustment of mixture parametric models of two populations for survival 
analysis in the presence of long survivors. A methodology is proposed in several 
five steps: first, it is proposed to use the multimodality test to decide the number 
of subpopulations to be considered in the model, second to adjust simple 
parametric survival models and mixture distribution models, to estimate the 
parameters and to select the best model fitted the data, finally, to test the 
hypotheses to compare the effectiveness of immunotherapies in the context of 
randomized clinical trials. The methodology is illustrated with data from a clinical 
trial that evaluates the effectiveness of the therapeutic vaccine CIMAvaxEGF vs 
the best supportive care for the treatment of advanced lung cancer. The mixture 
survival model allows estimating the presence of a subpopulation of long 
survivors that is 44% for vaccinated patients. The differences between the treated 
and control group were significant in both subpopulations (population of short-
term survival: p = 0.001, the population of long-term survival: p = 0.0002). For 
cancer therapies, where a proportion of patients achieves long-term control of the 
disease, the heterogeneity of the population must be taken into account. Mixture 
parametric models may be more suitable to detect the effectiveness of 
immunotherapies compared to standard models. 
KEY WORDS: Survival mixture parametric models, long-term survival, lung 
cancer, immunotherapy.


## Page 3


3 
 
1. Introduction 
Advances in immunotherapy have revolutionized the treatment landscape for 
advanced lung cancer, raising survival expectations beyond those historically 
anticipated with this disease [1, 2]. More important than the improvements in the 
average survival time is the presence of a long and stable plateau with a heavy 
censoring at the tail of the curve [3]. This means that a proportion of patients are 
still alive even after long follow-up, it suggests the disease is controlled in a 
subgroup of long-term survivors. This new phenomenon is not currently captured 
by the most commonly used statistical procedures for the survival analysis, which 
generally assume that all patients are equally susceptible to the event of interest 
[3]. As an alternative, mixture parametric survival models have been proposed to 
take into account the heterogeneous structure in the data analysis [4,5]. 
The finite mixture models have stayed widely used in many disciplines. For 
example, Nemec & Nemec [6] apply the mixture models of astronomy 
distributions to study the number of distinct stellar populations in the Milky Way; 
Cameron and Heckman [7] use these types of models to assess the effect of 
family history on educational performance; Kollu [8] refers to several applications 
in engineering, Neale [9] in genetics and Land [10] in the social sciences. These 
models can be easily applied to the data set in which two or more subpopulations 
are mixed. Because of its flexibility, these models have been received intense 
attention in recent years, both from a practical and theoretical point of view. A 
complete description of the theory of mixture distributions and their applications 
can be found in McLachlan and Peel [11] or in Titterington et al. [12]. Finite 
mixture models have considered different distributions according to the data and 
problems that are modeled. For example, West [13] and Richardson and Green


## Page 4


4 
 
[14] studied the fit and applications of the mixture of normal distributions, 
McLachlan and Peel [11] the mixture of t- students, Wiper and Rugginieri Gamma 
distributions [15], and Tsionas Weibull [16]. However, in the analysis of data from 
clinical trials, specifically those that evaluate the effect on survival is rarely used 
[17,18]. 
The present study proposes a methodology for the evaluation of the effect of 
therapies in the presence of long-term survivors in the context of clinical trials. 
We have structured the methodology as follows: in session 2.1 we describe the 
multimodality test, a necessary condition for the application of the methods 
proposed below; Session 2 .2 describes the parametric models of simple survival 
and mixture distributions; in session 2 .3 the methods for estimating parameters 
of the proposed models are explained; session 2.4 explains how to make the 
selection of the best model and finally in session 2.5 the hypothesis tests for 
comparing the effectiveness of therapies in the context of randomized clinical 
trials are detailed . Additionally, the proposed methodology is illustrated for the 
analysis of data from a clinical trial that evaluates the effectiveness of the 
therapeutic vaccine CIMAvaxEGF for the treatment of advanced lung cancer. 
2. Methodology 
2.1 Multimodality test 
Before adjusting a mixture parametric model, we must prove the existence of 
multimodality in the data, which justifies the application of the model. In this work, 
we assume the approach proposed by Silverman [19] and adapted by Hall and 
York [20] for the case in which we want to test whether the true distribution of a 
variable in a population is unimodal or bi-modal. Formally, given a sample of a


## Page 5


5 
 
random variable with density function f (in our case the survival time), denoting 
by j the number of modes in f, the hypothesis to test will be considered: 
H0: j ≤ k, against H1: j > k, 
Where k ∈ Z + is the number of modes to contrast. 
The test proposed by Silverman is based on the concept of a critical width. The 
critical width will be the smallest width h for which it is verified that the estimate 
of the density function has at most k modes. From this critical width, denoted by 
hk, Silverman proposes to use this parameter as a contrast statistic. Therefore 
the null hypothesis will be rejected when hk is very “large”, since this would mean 
that it is necessary to overstate the core estimate for get a k – modal structure. 
The critical width, hk, would be the last value of h before one of the modes 
"separates" giving rise to an estimate with (k + 1) modes.  
The R silvermantest package (available at http://cran.r-project.org/) has 
implemented this method, which facilitates its implementation in practice. 
 
2.2 Survival parametric models  
Simple model 
Survival analysis is a branch of statistics for analyzing the expected duration of 
time until one or more events happen. For the subjects in which the event could 
not be observed at the end of the follow-up period, the final state of the patient is 
called “censored”, since the actual duration of survival time cannot be known [21]. 
We define the random variable T as the time that elapses since the patient is 
diagnosed with the disease until he dies. The survival function is defined as S (T) 
= P (T> t) where 0 <t <1, which can be obtained as:


## Page 6


6 
 



t
du
u
f
t
S
)
(
)
(
 
Where f (u) is the density function. Simple models assume a unimodal distribution 
of survival. The survival function, in this case, can be estimated from the data 
assuming a parametric model. The most used are Exponential, Weibull, Log-
logistic and Lognormal (Table 1). 
Table 1. Density and survival functions for continuous parametric distributions: 
Exponential, Weibull, Log-logistic and Lognormal. 
Model 
Density 
function 
)
(t
f
Survival 
function 
)
(t
S
 
Exponential 
t
e 


.
 
t
e 

 
 
Weibull 
kt
k e
t
k



1
 
kt
e 

 
 
Log-logistic 


2
1
1
k
k
t
kt




 
kt


1
1
 
 
Lognormal 


2
2
2
log
2
1






t
e
t
 
 











t
log
1
 
 
Mixture parametric survival model 
A model with a mixture of distributions assumes the existence of two or more 
populations within the sample, for each of which, the random variable T follows a 
different distribution. This means that there is heterogeneity in patient survival 
and that individuals in each subpopulation have different risks of dying. In this 
study, we will work with two-component mixture models [18].  
The density function for this model is given by: 
f(x; ψ) = π1 f1(x; θ1) + π2f2(x; θ2)


## Page 7


7 
 
Where f1 and f2 are the density functions of two of the distributions given in table 
1. The parameter π (population weight parameter) is such that 0 <π ≤ 1, π1 can 
be interpreted as the proportion of one component or population in the model, 
and π2 = 1 - π1 the proportion of the other. The vector ψ includes the vectors π; 
θ1 and θ2. 
 
2.3 Methods for parameter estimations 
To estimate the parameters of the distribution of a simple model, the maximum 
likelihood method implemented by the Optimum function of R was used. In the 
mixture models, the parameters were estimated by this same method, using the 
EM (Expectation-Maximization) algorithm, which was implemented in R and it will 
be described later. 
 
Likelihood function 
Let x1, x2, ..., xn be a countable set of values for the discrete random variable X 
and Pψ (x) = Pψ (X = x). For the correct values of the parameter vector ψ the 
function P allows us to find the probability that X takes each of the values x1, 
x2,…. Let's look at this same function from another point of view: let's say we 
know that the random variable X takes the given values and follows a distribution 
Pψ (x) for an unknown value of ψ, so let Φ be the space of the possible values 
of ψ, we can interpret Pψ (x) as a function of ψ given x. Seen in this way, the 
function Pψ (x) is known as the likelihood function and is denoted by Lx (ψ). 
In general, when you have a continuous random variable, for uncensored data, 
the likelihood function is given by Lx (ψ) = ∏
𝑓 (𝑥𝑖 ;  𝜓)
𝑛
𝑖=1
, it is assumed that the 
experiments in which the values of X were found were independent and f (xi; ψ)


## Page 8


8 
 
(the density function corresponding to the distribution with which the variable is 
assumed) replaces Pψ (x). Thus, if we considered the mixture distribution model 
defined in the previous section, we obtain: 
Lx (ψ) = ∏
(π1 f1 (xi;  θ1 ) +  π2 f2 (xi;  θ2 ))
𝑛
𝑖=1
 
A problem arises when considering censored data since the value of the variable 
for all the elements of the sample is not known exactly. However, taking into 
account the type of censorship existing in our data, this can be solved using the 
survival function instead of the density function (Since the information we have is 
that the individual survived at least a number of months, we take the probability 
of surviving y or more months instead of surviving exactly y months). Thus, the 
likelihood function is as follows: 
Lx(ψ) = ∏
(π1 f1(xi;θ1 ) + π2f2 (xi; θ2 )) ∏
(π1S1 (xj;  θ1 ) +  π2S2 (xj; θ2 ))
𝑛2
𝑗=1
𝑛1
𝑖=1
 
Where n1 and n2 are the number of not censored and censored individuals 
respectively. 
Given a space of possible values θ for the parameter ψ, the maximum likelihood 
method consists of finding the maximum likelihood estimate ψ̂ = arg maxψ∈Φ Lx 
(ψ). Taking into account the monotony of the logarithm function, it is sometimes 
convenient to use Lx (ψ) = ln Lx (ψ) (log-likelihood function) instead of the 
maximum likelihood function, to calculate the maximum likelihood estimate. 
 
EM algorithm 
We now have to answer the question: How to maximize the log-likelihood 
function? For this, there are several methods among which are the Moments 
Method, the EM Method, and the Fisher Information Method. More information


## Page 9


9 
 
on these can be found in [22]. In this study, we will use the EM algorithm, which 
is one of the most used in the literature.  
To make the notation less cumbersome while describing the algorithm, it is 
assumed that the data is not censored, otherwise they would have, x1, x2,. . . , 
xn1 uncensored data and y1, y2,. . . , and n2 censored data, and the density or 
survival function would be taken as appropriate, the rest being analogous. 
Let x1, x2,. . . , xn the values that the variable takes in a sample of individuals. 
The information can be considered incomplete since it is unknown to which of the 
two existing populations, in which the random variable distributes differently, 
within the sample each individual belongs. To complete the information, the 
indicator variable zi, i = 1, 2, . . , n is taken, where zi = 1 if x1 is given by f1 and 
zi = 0 otherwise. The system (zi, xi) will contain the complete information of the 
data. Initially, the zi values can be found as a random sample of Bernoulli 
distribution (α), where α is the weight parameter. 
The EM algorithm is divided into two stages, stage E and stage M. Each of these 
is described below in the k + 1-th iteration. In stage E, the value of zi is estimated 
from the conditional expectation E (zi | xi), which, using the Bayes total probability 
formula, can be found as: 
ẑi  = E(ẑi  | xi ) =
π1𝑓1(𝑥𝑖,𝜃1(𝑘))
π1𝑓1(𝑥𝑖,𝜃1(𝑘))+π2𝑓2(𝑥𝑖,𝜃2(𝑘)) 
Where θ1 (k) and θ2 (k) are the parametric vectors of the distributions of each 
component, estimated in the k-th iteration. 
In step M, the parameter values are maximized, completing the information with 
the ẑi found above. 
π(k+1) = 
1
𝑛∑
𝑧̂ 𝑖
𝑛
𝑖=1


## Page 10


10 
 
θ1(k+1)=arg maxθ1∈Φ∑
𝑧̂ 𝑖ln (𝑓1(𝑥𝑖, 𝜃1))
𝑛
𝑖=1
 
θ2(k+1)= arg maxθ2∈Φ∑
𝑧̂ 𝑖ln (𝑓1(𝑥𝑖, 𝜃2))
𝑛
𝑖=1
 
For a single component, knowing the individuals belonging to that component, 
the problem of finding the values of the parameters that maximize the likelihood 
function is no more difficult than estimating the parameters of a simple model. 
This was done, using the Optimum function of R. 
The iterations of stages E and M of the algorithm are repeated until | lx (ψ (k + 
1)) - lx (ψ (k)) | is less than a small value, specified previously. The EM algorithm 
satisfies that lx (ψ (k + 1)) ≥ lx (ψ (k)), this property is the fundamental reason for 
its convergence [21]. 
 
2.4 Method for selecting the best model 
If the actual distribution (G) of the variable with density function g is known, to 
measure how our model f (x | θˆ) approximates, the Kullback-Leibler Information 
(K-L) is used. K-L is given by: 
EG(X) [𝑙𝑛
g(X )
f (x,θ)] = EG(X) [ln g(X )] −EG(X) ln f (x, θˆ) 
Where the best model will be the one that differs to a lesser extent from the real 
one and, therefore, the value of the K-L Information is lower. Moreover, in most 
cases, as in ours, the actual distribution of the variable is unknown. However, 
note that the expression EG (X) [ln g (X)] is a common constant for all models, 
so that the best model will be that, such that the value of EG (X) ln f (x, θˆ) be 
higher. This value can be approximated by the log-likelihood function plus a bias 
b(θˆ). Depending on how this approach is taken, several Information Criteria are 
defined for the selection of the best model. This paper uses the Akaike 
Information Criterion (AIC), defined as −2ln (Lx (θˆ)) + 2k.


## Page 11


11 
 
 
2.5 Hypothesis testing to evaluate the effect of the treatment 
The Log-rank test is the most used method to compare the survival of groups. It 
has as a null hypothesis that there are no differences between the populations 
for the occurrence of an event at any time of the follow-up. The analysis is based 
on the time of the events (i.e. deaths) of each group, which is compared with the 
expected number of events if there were no differences between the groups. In 
this work, we have used this test for the direct comparison of the Treated and 
Control groups for the case in which the existence of a single homogeneous 
population is assumed, that is, when a simple survival model is assumed (model 
0). 
For the case in which we assume the existence of two subpopulations (model 1), 
we have taken, as a cut-off point, the intersection of the estimated density 
functions for each subpopulation. All patients with survival lower of this cut-off 
point have been classified in the short-term population and all patients above the 
cut-off are considered to belong to the long-term population. 
A new immunotherapy (IT) treatment being evaluated may not have an effect on 
the parameters for both populations, or it could modify the proportion of patients, 
or the median survival of some subpopulation, or simultaneously both effects [23]. 
To evaluate the effect of immunotherapy we allowed the model parameters to 
depend on the treatment. Table 2 summarizes the assumptions of the model and 
hypothesis tests considered on the parameters to assess the effect of IT.


## Page 12


12 
 
Table 2: Hypothesis tested to evaluate the effect of the treatment in the mixture 
parametric survival model 
VariantA Hypothesis  Explanation 
Mean structure 
Mixing 
proportions 
2 
H0: β1k=0, 
k=1,2 
There is an effect of the 
therapy on the parameters 
for median overall survival, 
but not on the mixing 
proportion parameters. 
λk= 
β0k 
+ 
β1k*IT1, 
k=1,2   
π1= logit(z0),  
π2=1- π1 
3 
H0: α=0    
H0:  z1=0 
There is an effect of the 
therapy on the mixing 
proportion parameters, but 
not on the parameters for 
median overall survival. 
λ2= λ1+ α             π1= 
logit(z0 
+ 
z1*IT) 
π2=1- π1 
4 
H0: β1k=0 
H0:  z1=0 
There is an effect of the 
therapy on the mixing 
proportion parameters and 
on the parameters for 
median overall survival. 
λ1k= 
β0k 
+ 
β1k*IT1   
k=1,2   
π1= 
logit(z0 
+ 
z1*IT) 
π2=1- π1 
A To incorporate the effect of treatment in this model, we considered three variants 
Definition of terms: 
H0, the null hypothesis 
IT is the variable for the treatment groups (Control: IT=0 and CIMAvaxEGF: IT1=1)  
k=1,2 represent the short- and long-term survival populations 
π1 and π2 = the proportion of short-term and long-term survivors, respectively; 
(where k=1 or 2), with the restriction that 0 < πk ≤1 and π1 + π2=1, are the mixing 
proportions for the kth population. 
λk is the scale parameters for the Weibull distribution 
* Note that if any of the β1k is not significant, the average overall survival for 
subpopulation k would not depend on the treatment and would be similar for 
treaties and controls.


## Page 13


13 
 
3. Application to the data 
3.1 Data description 
Data from a randomized, multicenter, controlled clinical trial in patients with 
advanced NSCLC was used. The phase III trial evaluated the efficacy of 
CIMAvaxEGF, an EGF-based cancer vaccine compared with best supportive 
care (Control). The recruitment period was between July 5, 2006, and January 3, 
2012. Patients in advanced stages (IIIb / IV) who received 4 to 6 cycles of 
platinum-based first-line chemotherapy and who had confirmation were included. 
of stable disease or an objective response at least 4 weeks before randomization. 
A total of 405 patients were randomized (2: 1) to vaccinated or control groups. 
The vaccination group (n = 270) received the CIMAvaxEGF vaccine plus the best 
supportive care while the control group (n = 135) only received the best 
supportive therapy. Both groups were balanced according to the prognostic 
factors of the disease. More details can be found in [24]. The main evaluation 
criterion of the trial was overall survival (OS).  
3.2 Existence of bimodality 
The p-values obtained for the different k considered in the Silverman test are 
shown in Fig 1. It can be seen that the unimodality hypothesis is rejected for both 
treaties (p = 0.01) and controls (p <0.001). The first value of the test that is not 
significant is k = 2 in both cases, which indicates that survival in the two groups 
has a bimodal distribution.


## Page 14


14 
 
 
Fig 1. P values according to the different k considered in the Silverman 
multimodality test for the survival distribution of the control groups and 
treated with CIMAvaxEGF. For k = 1 the values of p are less than 0.05, so 
the null hypothesis that the distribution is unimodal is rejected. The first 
non-significant value of p is obtained in both cases when k = 2 which is 
interpreted in this case as that the sample is bimodal. 
 
3.3 Models Fitting and best model selection 
For the illustration of the proposed methodology, we have considered a Weibull 
distribution or a mixture of Weibull distributions. Table 3 shows the results of the 
adjustment of the different models and the estimated values of the median 
survival time and the proportions for the subpopulations. The two-component 
model resulted in a much better fit than the model assuming a homogeneous 
population (AIC: 2452 vs. 2783). The best fit is achieved with model 4 (AIC = 
2448). This is the survival model that assumes the mixture of two distributions


## Page 15


15 
 
and that both parameters, median survival, and mixing proportion, depend on 
treatment. The components represent short-term and long-term survival 
subpopulations. A significant increase of 10% of patients with long-term survival 
is observed in the group treated with CIMAvaxEGF with respect to the control 
group (p = 0.005). 
Table 3: Adjustment and estimates of model parameters assuming different 
hypotheses. 
Model 
AIC 
groups 
Median1 
Median2 
π1 
π2 
0 (1 component) 
2783 
- 
9.21 
 
 
 
1 (2 components) 
 
2452 
- 
7.28 
27.29 
0.55 
0.45 
2 (m~Treatment) 
2449 
Control 
6.28 
26.24 
0.62 
0.37 
Treated 8.35 
34.95 
3 (π~ Treatment) 
2449 
Control 
7.27 
27.25 
0.68 
0.32 
Treated 
0.50 
0.50 
4 (m, π~ Treatment) 
2448 
Control 
6.69 
26.01 
0.66 
0.34 
Treated 7.91 
30.78 
0.56 
0.44 
 
3.4 Application to the evaluation of the effect of therapies 
Fig 2 shows the survival curves for the short and long survival populations for 
both groups considering the best fit model (Model 4). The differences between 
the treated and control groups were significant in both subpopulations (short-lived 
population: p = 0.028; long-lived population: p = 0.0001).


## Page 16


16 
 
 
Fig 2: Survival curves for short and long survival populations 
 
4. Discussion 
In this work, a useful methodology was proposed to take into account the 
heterogeneity in the survival data. The methodology was illustrated in the 
evaluation of the effect of a new immunotherapy. Specifically, for the study of the 
survival of lung cancer patients in advanced stages, it is shown that the use of 
mixture distribution models are more appropriate than the use of simple models. 
The results of the study can be interpreted from three points of view: the existence 
of subgroups with different risks of dying within the population of patients with 
advanced lung cancer regardless of the therapy used; the effects of the 
therapeutic vaccine CIMAvaxEGF in the subgroups of patients identified as short 
and long survival; and the adaptation of current statistical methods to face the 
transition from advanced cancer to a chronic disease. 
It has been shown that therapies for certain types of cancer induce a subset of 
long-term survivors, such as melanoma [25], breast cancer [26] and multiple 
myeloma [27]. Specifically for advanced lung cancer, evidence has been found 
of patients at different risk of death in both population studies [29-30] and in


## Page 17


17 
 
clinical trials [31-33]. The identification of this finding before modern therapies 
suggests that some patients experience prolonged survival regardless of 
treatment [29]. In this location, the fraction of long survival has been estimated in 
about half of the participants in the clinical trial, while in population studies it is 
estimated at around 10% [30]. This difference is attributed to the restrictive 
selection criteria in clinical trials, which means that there is an overrepresentation 
of patients more likely to be long-term survivors. 
It should be noted that in many of the studies that refer to the presence of long 
survivors, traditional survival methods that assume homogeneity in the sample 
are used, a stratified analysis is done according to groups defined by biomarkers 
or the group of patients is divided arbitrarily into of short and long survival. The 
biological characteristics that define the heterogeneity of the data or the patient 
populations that will evolve to a short or long survival are not always known in 
advance. Biomarkers are often not incorporated into the design of the clinical trial 
but arise in secondary analyzes that are performed afterward. The definition of 
long survivors varies widely for each cancer location and among studies reported 
in the literature. To more accurately measure the clinical benefits of therapies, 
the American Society of Clinical Oncology and the European Society of Medical 
Oncology have proposed the ASCO-VF and ESMO-MCBS scales respectively. 
Both proposals were recently amended to incorporate bonuses and adjustments 
that capture the tail of the survival curve [34,35]. However, a study that critically 
analyzes the application of these proposals in 107 clinical trials concludes that 
neither of the two proposals was consistent as a measure of the absolute survival 
benefit [36].


## Page 18


18 
 
The models of the mixture of distributions presented here are an alternative to 
consider and can be a useful tool for reinterpreting data from clinical trials already 
carried out based on taking into account heterogeneity. In our study, we do a 
retrospective re-analysis of the data from a clinical trial, and certainly, the 
percentage of long survivors may be overestimated. However, due to the 
randomization process, this must have occurred to the same extent in the treated 
and control groups. More important than the estimation itself of the fraction of 
long survivors, is the proposal to apply the mixture distribution model to test 
hypotheses about the effect of immunotherapies in clinical trials. This is in our 
opinion the greatest novelty of this work. 
The methodology proposed here has the advantage that heterogeneity assumes 
without requiring groups to be defined beforehand. This is illustrated for the case 
in which there are two populations, but can easily be extended to the case where 
there are multiple subpopulations. It is important to keep in mind that the 
estimation of the mixture fraction can be very sensitive to the parametric 
distribution chosen to work [28]. For this reason, the selection of the parametric 
distribution to model the observed data should be done carefully. McCullagh and 
Barry [37] proposed a model selection process algorithm and recommended 
adjusting different distributions to the data and selecting the best distribution 
using one of the available information criteria. 
Once the existence of heterogeneity in the main variable that is evaluated in 
retrospective exploratory studies has been detected, confirmation of this finding 
is imposed through the design of new clinical trials. This is one of the current 
challenges facing statisticians working in immuno-oncology. Even more so when 
the implementation of sequential Bayesian designs with intermediate analyzes


## Page 19


19 
 
has become a standard practice in phase III clinical trials to allow early 
termination of the studies. The software available for sample size calculation, 
such as PROC POWER in SAS, the survival analysis module in PASS, the 
powerSurvEpi package in R, is based on standard proportional hazard (PH) 
models that are not appropriate for the design in the presence of a fraction of 
patients with long survival. Cai [38] has proposed a methodology, which he has 
applied and implemented in the NPHMC R package. In his work, he establishes 
the calculation of sample size in the case in which a group of patients reaches a 
cure with the treatment. However, in the case of clinical trials in patients in 
advanced stages not operated, patients are not cured, but the new treatments 
are focused on achieving stabilization of the disease. New studies could address 
the proposal of clinical trial designs that take into account the mix of different 
distributions or risks in the subpopulations of the study. 
The implementation in the exposed case study confirmed that vaccination with 
CIMAvaxEGF prolongs the survival of patients with advanced lung cancer. 
Although in both populations, short and long survival, patients are benefited with 
immunotherapy, the benefit is markedly greater in the long-lived population. 
Subsequent studies could propose the characterization and identification of 
biomarkers predictive of successful treatment with CIMAvaxEGF of both 
subpopulations or the selection of patients with a high benefit with this 
immunotherapy. 
Future research could focus on the reproducibility of the findings of the effect of 
other treatments for lung cancer on the mixture fraction or on the survival of 
subpopulations. Alternatively, the prospective identification of patients with long-
term survival potential may allow the validation of biomarkers predictive of the


## Page 20


20 
 
effect of therapies and favor the use of more personalized therapeutic 
approaches. 
The 
phenomenon 
of 
multimodality 
and 
the 
effect 
of 
immunotherapies on other types of tumors could also be studied. Studies are 
needed to determine the host factors and molecular characteristics that influence 
the heterogeneity of the survival of cancer patients. 
 
Acknowledgement 
We thank all the patients and staff of all the institutions that were involved in the 
clinical trial. 
References 
1. Massarelli E, Papadimitrakopoulou V, Welsh J, Tang C, Tsao AS. 
Immunotherapy in lung cancer. Translational lung cancer research. 
2014;3(1):53-63.  
2. Carrizosa DR, Gold KA. New strategies in immunotherapy for non-small cell 
lung cancer. Translational lung cancer research. 2015;4(5):553- 9.  
3. Chen TT. Statistical issues and challenges in immunooncology. J Immuno 
Ther Cancer. 2013 ; 1:18. 
4. McLachlan GJ, Peel D. Finite Mixture Distributions. New York: Wiley; 2000. 
5. Titterington DM, Smith AFM, Makov UE. Statistical Analysis of Finite Mixture 
Distributions. New York: Wiley;1985. 
6. Nemec L, Nemec AFL. Mixture models for studying stellar populations. I. 
Univariate mixture models, parameter estimation, and the number of discrete 
population components. Publications of the Astronomical Society of the 
Pacific.1991; 103:95-121.


## Page 21


21 
 
7. Cameron SV, Heckman JJ. Life cycle schooling and dynamic selection bias: 
Models and evidence for five cohorts of American males. Journal of Political 
Economy. 1998;106,262– 333. 
8. Kollu R, Rayapudi SR, Narasimham SVL and Pakkurthi KM. Mixture probability 
distribution functions to model wind speed distributions. International Journal 
of Energy and Environmental Engineering. 2012 3:27. 
9. Neale MC. A Finite Mixture Distribution Model for Data Collected from Twins. 
Twin Research. 2003;6(3):235–239. 
10. Land KC. Introduction to the Special Issue on Finite Mixture Models. 
Sociological Methods & Research. 2001;29(3):275–281. 
11. McLachlan G, Peel D. Finite Mixture Models. Jonh Wiley & Sons, Inc. 2000 
12. Titterington, DM, Smith, AFM and Makov, UE. Statistical Analysis of Finite 
Mixture Distributions. London: Wiley. 1985 
13. West M. Approximating posterior distributions by mixtures. J. Roy. Statist. 
Soc. 1983;55:409–422. 
14. Richardson S, Green P. On Bayesian analysis of mixtures with an unknown 
number of components. J. Roy. Statist. Soc. Ser. 1997;B59:731–792. 
15. Wiper DR, Rugieri F. Mixture with gamma distribution with applications. 
Journal of computational and graphical statistics. 2001;10(3):440-454. 
16. Tsionas E. Bayesian analysis of finite mixtures of Weibull distributions. 
Communication in statistics. part A. 2002,31(1):37-48. 
17. Erişoğlu U, Erişoğlu M, Erol H. A Mixture Model of Two Different Distributions 
Approach to the Analysis of Heterogeneous Survival Data, International 
Journal of Computational and Mathematical Sciences. 2011; 5:2.


## Page 22


22 
 
18. Marin JM, Rodriguez-Bernal MT, Wiper MP: Using weibull mixture 
distributions to model heterogeneous survival data. Communicat Stat. 2005, 
34:673–684. 
19. Silverman BW. Using kernel estimates to investigate multimodality, J. Royal 
Statist. Sot. B 1981;43:97-99. 
20. Hall P, York M. On the calibration of Silverman’s test for multimodality, 
Statistica Sinica.2001;11:515–36 
21. Collet D. Modelling Survival Data in Medical Studies, 2nd edition, Chapman 
&Hall/CRC. 2003. 
22. Wu CFJ. On the convergence properties of the EM alorighm. The Annals of 
Statistics. 1983;11:95-103 
23. Sanchez L, Muchene L, Lorenzo-Luaces P, Viada C, Rodriguez PC, Alfonso 
S, et al. Differential Effects of Two Therapeutic Cancer Vaccines on Short- 
and Long-Term Survival Populations among Patients with Advanced Lung 
Cancer. Semin Oncol. 2018;45:52-57. 
24. Rodriguez PC, Popa X, Martínez O, Mendoza S, Santiesteban E, Crespo T, 
et al. A Phase III Clinical Trial of the Epidermal Growth Factor Vaccine 
CIMAvax-EGF as Switch Maintenance Therapy in Advanced Non-Small Cell 
Lung Cancer Patients. Clinical Cancer Research. 2016;22(15):3782-90. 
25. Eggermont AM, Suciu S, Testori A, Santinami M, Kruit WH, Marsden J, et al. 
Long-term results of the randomized phase III trial EORTC 18991 of adjuvant 
therapy with pegylated interferon alfa-2b versus observation in resected stage 
III melanoma. J Clin Oncol. 2012;30(31):3810–3818.


## Page 23


23 
 
26. Ambs S: Prognostic significance of subtype classification for short- and long-
term survival in breast cancer: survival time holds the key. PLoS Med 2010, 
7(5):e1000281. 
27. Othus M, Barlogie B, Leblanc ML, Crowley JJ: Cure models as a useful 
statistical tool for analyzing survival. Clin Cancer Res. 2012;18(14):3731–
3736. 
28. Sanchez L, Lorenzo-Luaces P, Viada C, Galan Y, Ballesteros J, Crombet T 
et al. Is there a subgroup of long-term evolution among patients with advanced 
lung cancer?: hints from the analysis of survival curves from cancer registry 
data. BMC cancer. 2014;14:933 - 9.  
29. Angelis R, Capocaccia R, Hakulinen T, Soderman B, Verdecchia A. Mixture 
models for cancer survical analysis: aplication to population-based data with 
covariates. Stat Med. 1999;18:144–454. 
30. Davis JS, Prophet E, Peng H-L, et al. Potential influence on clinical trials of 
long-term survivors of stage IV non-small-cell lung cancer. JNCI Cancer 
Spectr. 2019. 
31. Giroux Leprieur E, Lavole A, Ruppert AM, Gounant V, Wislez M, Cadranel J, 
et al. Factors associated with long-term survival of patients with advanced 
non-small cell lung cancer. Respirology. 2012;17(1):134-42. 32.  
32. Kaira K, Takahashi T, Murakami H, Tsuya A, Nakamura Y, Naito T et al. Long-
term survivors of more than 5 years in advanced non-small cell lung cancer. 
Lung cancer. 2010;67(1):120-3. doi:10.1016/j.lungcan.2009.03.014. 
33. Satoh H, Ishikawa H, Ohara G, Kagohashi K, Kurishima K, Ohtsuka M et al. 
Long-term survivors after chemotherapy in advanced non-small cell lung 
cancer. Anticancer research. 2007;27(6C):4457-60.


## Page 24


24 
 
34. Schnipper LE, Davidson NE,Wollins DS, et al. Updating the American Society 
of Clinical Oncology Value Framework: revisions and reflections in response 
to comments received. J Clin Oncol. 2016; 34(24):2925-2934.  
35. Cherny NI, Dafni U, Bogaerts J, et al. ESMO-Magnitude of Clinical Benefit 
Scale version 1.1. Ann Oncol. 2017;28 
36. Saluja R, Everest L, Cheng S, Cheung M, Chan KKW. Assessment of whether 
the American Society of Clinical Oncology’s value framework and the 
European Society for Medical Oncology’s magnitude of clinical benefit scale 
measure absolute or relative clinical survival benefit: a meta-analysis of 
randomized clinical trials.JAMA Oncol. 2019;5(8):1188-1194. 
37.  McCullagh L, Barry M: Survival analysis used in company submissions to the 
national centre for pharmacoeconomics. Ireland Value Health. 2013; 16:A398 
38. Cai C, Zou Y, Peng Y, Zhang J. smcure: an R-package for estimating 
semiparametric mixture cure models. Comput Methods Programs Biomed. 
2012;108(3):1255–60. 
 
Author Contributions 
Conceived and designed the study: LS and AL. Implemented the methodology 
and analyzed the data: LS, PL and CF. Wrote the paper: LS, CF and AL. All 
authors participate in the interpretation of the data, critically revised subsequent 
drafts of the manuscript, and approved the final version. 
 
Financial Disclosure Statement 
The authors received no specific funding for this work

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1911_09765v1_mixture_survival_models_methodology_an_application_to_cancer_immunotherapy_asse
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1911_09765V1_MIXTURE_SURVIVAL_MODELS_METHODOLOGY_AN_APPLICATION_TO_CANCER_IMMUNOTHERAPY_ASSE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

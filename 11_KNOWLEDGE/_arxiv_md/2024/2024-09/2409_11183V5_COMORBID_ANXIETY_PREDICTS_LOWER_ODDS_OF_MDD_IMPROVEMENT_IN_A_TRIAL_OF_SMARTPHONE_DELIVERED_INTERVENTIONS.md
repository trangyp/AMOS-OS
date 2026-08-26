---
canon-group: reference
rscf-state: source-claim
arxiv_id: 2409.11183v5
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 2409.11183v5_Comorbid anxiety predicts lower odds of MDD improvement in a trial of smartphone-delivered interventions

> Source: 2409.11183v5_Comorbid anxiety predicts lower odds of MDD improvement in a trial of smartphone-delivered interventions.pdf

> Pages: 17

---


## Page 1


Comorbid anxiety predicts lower odds of MDD improvement in a trial of
smartphone-delivered interventions
Morgan B. Talbota,b,c,∗, Jessica M. Lipschitz†b,d, Omar Costilla-Reyes†e
† Co-Senior Authors
aMassachusetts Institute of Technology, 77 Massachusetts Avenue, Cambridge, MA, 02139, USA
bHarvard Medical School, 25 Shattuck St, Boston, MA, 02115, USA
cBoston Children’s Hospital, 300 Longwood Avenue, Boston, MA, 02115, USA
dBrigham and Women’s Hospital, 75 Francis Street, Boston, MA, 02115, USA
eEqu Healthcare, Watertown, MA, 02472, USA. Work completed while at MIT.
Abstract
Comorbid anxiety disorders are common among patients with major depressive disorder (MDD), but their impact on
outcomes of digital and smartphone-delivered interventions is not well understood. This study is a secondary analysis
of a randomized controlled effectiveness trial (n=638) that assessed three smartphone-delivered interventions: Project
EVO (a cognitive training app), iPST (a problem-solving therapy app), and Health Tips (an active control). We applied
classical machine learning models (logistic regression, support vector machines, decision trees, random forests, and
k-nearest-neighbors) to identify baseline predictors of MDD improvement at 4 weeks after trial enrollment. Our
analysis produced a decision tree model indicating that a baseline GAD-7 questionnaire score of 11 or higher, a
threshold consistent with at least moderate anxiety, strongly predicts lower odds of MDD improvement in this trial.
Our exploratory findings suggest that depressed individuals with comorbid anxiety have reduced odds of substantial
improvement in the context of smartphone-delivered interventions, as the association was observed across all three
intervention groups. Our work highlights a methodology that can identify interpretable clinical thresholds, which, if
validated, could predict symptom trajectories and inform treatment selection and intensity.
Keywords: Mental health, machine learning, mood disorders, major depressive disorder, anxiety disorders,
comorbidity
1. Introduction
Major depressive disorder (MDD) affects roughly 322 million people, and is a leading cause of disability with
large impacts on quality of life (Moreno-Agostino et al., 2021). Less than 20% of people with MDD receive minimally
Full citation: Talbot, Morgan B., Jessica M. Lipschitz†, and Omar Costilla-Reyes†. “Comorbid anxiety predicts lower odds of MDD im-
provement in a trial of smartphone-delivered interventions.” Journal of Affective Disorders 394 (2026): 120416. † Co-Senior Authors. DOI:
10.1016/j.jad.2025.120416
Source code for data analysis: https://github.com/MorganBDT/brighten-mdd-outcome-predict
∗Corresponding author at: Department of Health Sciences and Technology, Massachusetts Institute of Technology, 77 Massachusetts Avenue
Building E25-518, Cambridge, MA 02139, USA.
Email address: mtalbot@mit.edu (Morgan B. Talbot)
Published in Journal of Affective Disorders (2026)
October 31, 2025
arXiv:2409.11183v5  [q-bio.QM]  30 Oct 2025


## Page 2


adequate treatment (Thornicroft et al., 2017). 50% of patients who receive MDD treatment experience minimal or
no improvement, with a subset of these not responding to multiple treatment attempts (Gaynes et al., 2020). Digital
and smartphone-delivered psychotherapy interventions are one promising avenue to increase access to evidence-based
MDD treatments (Linardon et al., 2024). Knowledge of the factors that predict which patients are likely to improve
could inform personalized care, such as identifying individuals who may require additional support. However, studies
attempting to identify these predictors have yielded inconsistent results (Sextl-Pl¨otz et al., 2024).
In this study, we investigated predictors of clinical MDD improvement by conducting a secondary analysis of
a large, publicly available clinical trial dataset (Arean et al., 2016). The Brighten MDD trial was an online, fully
remote effectiveness trial with a four-week primary intervention period, in which participants were randomized to
one of three conditions: Project EVO, a serious game designed to bolster cognitive skills related to MDD; iPST, an
app based on problem-solving therapy for MDD; and an information control app called Health Tips, which suggested
strategies to improve health and serves as an active control. Consistent with an effectiveness trial framework, some
participants endorsed simultaneously receiving other treatments (e.g., medication, seeing a therapist or psychiatrist)
while in the trial. The original clinical trial analysis found that for participants with moderate MDD, the active apps
resulted in higher remission rates compared to the control intervention at the 12-week follow up (Arean et al., 2016).
Although the original study compares effectiveness across the three groups, the participant-level factors related to
the likelihood of MDD improvement have not been explored to the best of our knowledge. We applied interpretable
machine learning techniques, coupled with a forward feature selection approach, to identify variables measured at
baseline that predict greater or lesser odds of clinical improvement during the treatment period.
2. Methods
2.1. Original clinical trial
This study is an independent secondary analysis of open-access data from the Brighten study, a randomized con-
trolled effectiveness trial. The original study evaluated the effectiveness of two smartphone-delivered interventions
for depression—Project EVO (a cognitive training app) and iPST (a problem-solving therapy app)—against an ac-
tive control intervention, Health Tips (Arean et al., 2016). Consolidated Standards of Reporting Trials (CONSORT)
diagrams detailing participant enrollment and flow are available in the original publications, which also provide com-
prehensive details about the interventions and trial design (Anguera et al., 2016; Arean et al., 2016). The primary
analysis of the original trial found that, among participants with moderate MDD at baseline, both the Project EVO
and iPST interventions resulted in higher remission rates at the 12-week follow-up compared to the Health Tips active
control (Arean et al., 2016).
2.2. Models and variables
Our study predicted a binary MDD improvement outcome, measured 4 weeks after trial enrollment in alignment
with the main intervention period of the original study Arean et al. (2016). This outcome was defined using estab-
lished criteria for MDD treatment response: a Patient Health Questionnaire-9 (PHQ-9) score of both < 10 and reduced
2


## Page 3


by ≥50% relative to baseline (Kroenke et al., 2001). We chose a machine learning framework for this analysis be-
cause of its ability to systematically identify predictive patterns using both linear and non-linear models, an approach
well-suited to contexts where prior evidence for predictors is inconsistent. Our methodology was designed to com-
pare multiple algorithm types, rigorously account for missing data and sampling variability, and select a parsimonious
set of predictors to generate robust and interpretable findings. We selected five commonly used algorithms to rep-
resent distinct modeling approaches: logistic regression and support vector machines as standard linear classifiers;
decision trees and random forests to capture non-linear relationships and interactions; and k-nearest-neighbors as a
non-parametric, instance-based method. We were specifically interested in decision trees for their ease of interpretabil-
ity in clinical settings (Banerjee et al., 2019). We considered the following variables in the dataset as “features” that
the models could use for prediction (> 0% percentages of missing data shown in brackets after each variable name):
• Demographics:
– Age
– Gender (collected as binary male/female)
– Race/ethnicity (categories “African-American/Black,” “Asian,” “Hispanic/Latino,” “Multiracial/other,” and
“Non-Hispanic White”)
– Working/employment (binary yes/no)
– Marital status (binarized to married/partnered or not)
– Education (binarized to education beyond high school or not)
– Satisfaction with level of income (binarized to responses of “can’t make ends meet” vs. responses indi-
cating higher satisfaction) [53% missing]
• Questionnaire scores:
– PHQ-9 at baseline (Kroenke et al., 2001) [0% missing]
– Generalized Anxiety Disorder-7 (GAD-7), used as a global measure of anxiety symptoms (Spitzer et al.,
2006; Kroenke et al., 2007; Beard and Bj¨orgvinsson, 2014) [47% missing]
– Sheehan Disability Scale (SDS) (Sheehan, 1983) [47% missing]
– AUDIT alcohol consumption questions (AUDIT-C) (Bush et al., 1998) [47% missing]
• Treatment group (binary feature for each)
– Project EVO
– iPST
– Health Tips (active control)
3


## Page 4


The set of predictor variables was chosen to include all available baseline demographic and clinical questionnaire
data for an exploratory analysis. Marital status, education, and satisfaction with level of income were binarized.
For race/ethnicity, response options “Native Hawaiian/other Pacific Islander,” “American Indian/Alaskan Native,” and
“More than one” were combined to form the category “Multiracial/other.” These modifications were designed to
prevent issues arising from categories with few participants. To maintain a parsimonious model and avoid multi-
collinearity from redundant predictors, we selected one of the two available income-related variables for inclusion.
We chose “satisfaction with level of income,” hypothesizing that this measure of subjective financial distress may
have a more direct relationship with mental health outcomes than absolute income brackets. We also considered using
responses from the IMPACT mania and psychosis screening questionnaire (Un¨utzer et al., 2002; Arean et al., 2016)
as predictors. We decided to exclude participants who endorsed a history consistent with bipolar disorder. Only 2 of
the remaining participants reported any history of psychosis, precluding a meaningful analysis of psychosis history as
a predictor of MDD outcomes. The most detailed source of information regarding the variables collected during the
original trial is the Brighten Study Public Researcher Portal (Sage Bionetworks, 2018).
2.3. Data preparation
Data from the Brighten Version 1 study (Anguera et al., 2016; Arean et al., 2016) were downloaded from the
Brighten Study Public Researcher Portal (Sage Bionetworks, 2018). We used all available records in the Brighten
Version 1 dataset (Anguera et al., 2016). While demographics and baseline PHQ-9 scores were collected upon en-
rollment, several other questionnaire scores were collected in the days following enrollment, notably GAD-7, SDS,
AUDIT-C, and mania and psychosis history. For these questionnaires, we used the earliest available response from
each participant as the “baseline” measurement. We did not consider any such responses that were made more than
5 days after enrollment. We excluded participants with a baseline PHQ-9 score below 10. To focus our analysis on
unipolar depression, we also excluded participants who endorsed a history of (i) lithium prescription, (ii) prescription
of medication for mania symptoms, or (iii) diagnosis of bipolar disorder on the IMPACT questionnaire. These criteria
left us with 638 participants.
The PHQ-9 outcome data required for our analysis had substantial missingness, with 52%, 58%, 59%, and 60%
missing at weeks 1-4 post-enrollment, respectively. Moreover, 41% of the included participants had only demo-
graphic data and baseline PHQ-9 (which were collected together), without any questionnaire scores for GAD-7, SDS,
IMPACT, AUDIT-C, and all post-baseline PHQ-9. We checked for differences in demographics and baseline PHQ-9
scores between this group and participants who had additional data, and did not find statistically significant evidence
supporting any differences (p > 0.05, t-tests for age and PHQ-9, χ2 tests for gender, race/ethnicity, employment, mari-
tal status, and education). We used a random forest-based multiple imputation strategy with predictive mean matching
to handle missing data (baseline variables and follow-up PHQ-9 at weeks 1-4), implemented with the miceRanger
package in R (Wilson, 2020). We produced 100 imputed versions of the dataset. On average across imputations,
41% of the participants met the definition for MDD improvement. Before training each machine learning model, all
4


## Page 5


non-categorical features in the dataset were rescaled to have a mean of 0 and a standard deviation of 1.
2.4. Feature selection and model fitting
To minimize overfitting due to the high number of features in the dataset, we used a forward selection procedure
to identify a minimal set of input features for each machine learning model. AUC estimates were first obtained for
univariate models on each feature, and the feature that resulted in the highest AUC was selected. Then, all possible
bivariate models including the first chosen feature were tested, and features were added one by one in this fashion
until adding another feature did not significantly increase AUC. Each AUC estimate was obtained using a Monte
Carlo cross-validation procedure with 10,000 iterations. For each iteration, we first randomly selected 1 of the 100
imputed versions of the dataset, and then randomly sampled 80% of the participants to form a training set, leaving the
remaining 20% as a validation set. We took the 10,000 difference values between estimates from the current candidate
model and those of the previous best model (or AUC = 0.5 for the first variable). We computed both the mean
∆AUC value and its 95% confidence interval from this empirical distribution, which accounts for uncertainty due to
both missingness and recruitment sampling. Statistical significance of the model’s improvement due to the added
variable was assessed by calculating the probability p = P(∆AUC ≤0) from the empirically sampled distribution.
The Benjamini-Hochberg procedure (Benjamini and Hochberg, 1995) was applied to control the false discovery rate
at 0.05 across all comparisons for a given model type. To balance the goals of maximizing prediction accuracy and
limiting model complexity, we also required an AUC improvement of ≥0.02 for each new variable (Greenberg et al.,
2024). For decision trees and random forests, we ran variable selection for different maximum tree depths (maximum
number of binary decisions allowed per tree, ranging here from 1 to 5 inclusive), keeping the tree depth that produced
the highest AUC estimate overall. While the forward selection process was guided exclusively by AUC, we also
calculated classification accuracy for the final models to aid in their interpretation and comparison. All models were
implemented using the scikit-learn Python library with default hyperparameters (Pedregosa et al., 2011).
2.5. Sensitivity Analyses
We conducted two alternate versions of our analysis to assess the sensitivity of our findings to certain method-
ological assumptions.
1. Instead of predicting MDD outcomes 4 weeks post-enrollment (corresponding to the main intervention period
in the original trial (Arean et al., 2016)), we predicted outcomes at 12 weeks.
2. Of the 638 participants who met our screening criteria (baseline PHQ-9 ≥10, no reported history of bipolar
disorder), 279 (41%) had only baseline PHQ-9 and demographic information recorded, with none of GAD-7,
SDS, AUDIT-C, mania/psychosis history, or any post-baseline PHQ-9. While our primary analysis includes
these participants and imputes their data in accordance with intention-to-treat principles, we exclude them in
an alternative version of the analysis (n = 359). Notably, missing data from these participants accounts for a
large proportion of the overall missingness in the dataset: more information can be found in the supplementary
material.
5


## Page 6


Model Type
Interp?
AUC
Accuracy
Depth
Pred.
Coefficient
Logistic Regression
Yes
0.74 (0.65, 0.82)
0.69 (0.61, 0.77)
-
GAD-7
-0.96 (-1.13, -0.80)
0.71 (0.62, 0.79)
0.66 (0.58, 0.74)
-
SDS
-0.75 (-0.93, -0.57)
Support Vector Machine
Yes
0.74 (0.65, 0.82)
0.70 (0.62, 0.78)
-
GAD-7
-1.01 (-1.15, -0.88)
0.70 (0.61, 0.79)
0.66 (0.57, 0.74)
-
SDS
-0.81 (-0.98, -0.58)
Random Forest
No
0.74 (0.65, 0.82)
0.70 (0.62, 0.78)
2
GAD-7
-
0.70 (0.61, 0.79)
0.66 (0.58, 0.74)
2
SDS
-
Decision Tree
Yes
0.73 (0.64, 0.81)
0.70 (0.61, 0.77)
3
GAD-7
-
0.70 (0.61, 0.77)
0.69 (0.61, 0.77)
1
GAD-7
-
0.69 (0.60, 0.77)
0.65 (0.57, 0.73)
3
SDS
-
K-Nearest-Neighbors
No
N.S.
N.S.
-
N.S.
-
Table 1: GAD-7 was the only predictor of MDD improvement across all selected models, and adding any second variable did not signif-
icantly increase AUC. K-nearest-neighbors failed to predict significantly above chance (N.S. = not significant). 95% confidence intervals are
included in parentheses. “Interp.” refers to whether or not each model type is considered interpretable. Logistic regression and support vector
machine coefficients are for standardized features (mean = 0, std = 1). “Depth” refers to maximum tree depth, and is only applicable for random
forests and decision trees. A selection of alternative models that predicted significantly above chance, but were not selected by the forward process,
are shown in gray: we provide results for (i) the best model with an alternative predictor (SDS) and (ii) a depth = 1 decision tree model using
GAD-7, which is of special interest for interpretability. A complete set of results for the main analysis and all sensitivity analyses can be found in
the supplementary material.
3. Results
Logistic regression, support vector machines, random forests, and decision trees demonstrated AUC values sig-
nificantly above the 0.5 chance level in predicting MDD improvement, while k-nearest-neighbors did not (Table 1).
All selected models used only one feature, baseline GAD-7: in no configuration did adding any additional variable
increase AUC with statistical significance. Notably, the predictive performance was highly similar across these top
4 model types, with AUC and accuracy point estimates falling within narrow ranges (0.728-0.739 and 0.694-0.702
respectively) with widely overlapping confidence intervals for both. All model types other than k-nearest-neighbors
also predicted significantly above the chance level using SDS as the sole predictor (indicating a negative relation-
ship between functional disability and depression improvement), but were not selected by the forward process due to
marginally lower AUC estimates.
While all model types had similar AUC values and near-identical accuracy, decision trees are arguably the most
straightforward to apply in clinical settings. The depth = 1 model provides a simple clinical heuristic, a binary
threshold on a single variable, that can be applied instantly without computation. Although the depth = 3 decision
tree yielded a marginally higher AUC value (0.728 vs. 0.696), the simpler and more interpretable depth = 1 tree
achieved nearly identical classification accuracy (0.697 vs. 0.692 respectively; see Table 1). We thus focus our
primary interpretation on the depth = 1 model, as it maximizes ease of interpretability with no meaningful loss in
6


## Page 7


GAD-7 ≥ 11?
No
Not improve
Improve
Yes
OR = 0.18, 95% CI [0.12, 0.28]  
Figure 1: A decision tree fitted to the multiply-imputed dataset predicts MDD improvement using baseline GAD-7 scores. Participants who
reported a GAD-7 score of 11 or higher were less than one-fifth as likely to experience significant MDD improvement as those with a score below
11.
Statistic
Pooled Value (%)
95% Confidence Interval (%)
Sensitivity
73
68 - 78
Specificity
67
59 - 73
Positive Predictive Value
76
70 - 81
Negative Predictive Value
63
56 - 70
Table 2: Prognostic performance of the GAD-7 ≥11 decision tree threshold for predicting MDD non-improvement. Sensitivity is the
probability that a participant who does not experience MDD improvement is correctly identified by the model (true positive rate). Specificity is the
probability that a participant who does experience MDD improvement is correctly identified by the model (true negative rate). Positive Predictive
Value is the probability that a participant with a GAD-7 score ≥11 truly does not experience MDD improvement. Negative Predictive Value is the
probability that a participant with a GAD-7 score < 11 truly does experience MDD improvement. Point estimates and confidence intervals for each
of these metrics are pooled from the multiply-imputed dataset using Rubin’s rules.
predictive performance.
Re-fitting a depth = 1 decision tree on the entire dataset (taking the median threshold across imputations) yields a
model that classifies participants with a baseline GAD-7 score ≥11 as unlikely to experience improvement, and those
with GAD-7 < 11 as likely to experience improvement (Fig. 1). Notably, this threshold is similar (but not identical)
to the Spitzer et al. (2006) threshold (GAD-7 ≥10) for “moderate” to “severe” generalized anxiety disorder.
To better quantify the association of GAD-7 being 11 or higher with MDD outcomes, we calculated an odds ratio
of 0.18 for improvement vs. non-improvement given GAD-7 ≥11, with a 95% confidence interval of [0.12, 0.28] (p <
0.0001). These findings indicate that a GAD-7 score of 11 or higher reduces the odds of clinical MDD improvement
by a factor of slightly less than one-fifth, with statistical significance. We used Rubin’s rules to combine the odds
ratio values from multiple imputations (Rubin, 1987). To explore the consistency of this finding across treatment
assignment groups, we calculated the odds ratio for a GAD-7 score ≥11 predicting improvement within each group
separately. The association was statistically significant in all three groups: Project EVO (0.14 [0.07, 0.28]), iPST
(0.12 [0.04, 0.39]), and the Health Tips active control (0.27 [0.14, 0.51]).
Viewed as a test that predicts MDD non-improvement, the proposed GAD-7 threshold has a positive predictive
value of 76% and a negative predictive value of 63% (Table 2). In other words, our results suggest that the probability
7


## Page 8


that a patient with GAD-7 < 11 will show clinically significant improvement in MDD is 0.63, but the probability that
a patient with GAD-7 ≥11 will improve is only 0.24.
The results of both sensitivity analyses are consistent overall with those of the main analysis in that (i) GAD-
7 is the single best predictor of MDD improvement, and (ii) GAD-7 ≥11 is the most informative threshold for a
depth = 1 decision tree, with statistically significant odds ratios. In the sensitivity analysis excluding participants with
substantial missing data, the reduced statistical power meant that only a random forest model identified GAD-7 as a
significant predictor during variable selection. However, an exploratory analysis of the depth = 1 decision tree in this
subgroup yielded the same GAD-7 ≥11 threshold with a statistically significant odds ratio. Detailed results for all
sensitivity analyses are available in the supplementary material.
While GAD-7 was the single most informative predictor of MDD improvement, SDS was also a statistically
significant predictor in alternative univariate models. Yet, bivariate models combining GAD-7 and SDS did not yield
significant improvements. In a post-hoc exploratory analysis, a Spearman’s rank-order correlation revealed a strong,
positive association between GAD-7 and SDS at baseline (ρ = 0.67, 95% CI [0.61, 0.71], p < 0.001).
4. Discussion
We predicted MDD improvement in a large cohort of participants receiving smartphone-delivered interventions.
Our decision tree analysis identified a clear and clinically meaningful relationship: depressed individuals with base-
line GAD-7 scores of 11 or higher were roughly one-fifth as likely to experience MDD improvement as those with
lower GAD-7 scores. In terms of predictive value, there is a large difference in the probability of MDD improvement
when GAD-7 ≥11 (24%) and when GAD-7 < 11 (63%). If replicated beyond the present study, this result suggests
that additional support or more intensive treatment is warranted for individuals with MDD and GAD-7 ≥11 compared
to people with GAD-7 < 11. This simple decision rule would be readily applicable in the clinic, as GAD-7 is widely
administered to assess a common set of MDD comorbidities. While originally developed to screen for generalized
anxiety disorder (Spitzer et al., 2006), the GAD-7 is now well-established as a screening tool for multiple anxiety dis-
orders (Kroenke et al., 2007) and as a transdiagnostic measure of global anxiety symptoms (Beard and Bj¨orgvinsson,
2014).
Our findings highlight the utility of decision trees as a readily interpretable non-linear modeling approach. While
decision trees demonstrated similar AUC scores and near-identical accuracy to logistic regression, support vector
machine, and random forest models, these four model types offer different levels of interpretability - the ability to
understand and explain the way the trained model makes predictions. While logistic regression and support vector
machines produce coefficients that can be interpreted as the importance of each predictor, the meanings of the actual
coefficient values are often unintuitive: logistic regression coefficients represent log-odds, while support vector ma-
chine coefficients define a class-separating hyperplane. Random forests are effectively uninterpretable “black-boxes”:
we cannot practicably explain how our random forests use GAD-7 to predict outcomes. In contrast, decision trees
provided a GAD-7 threshold (GAD-7 ≥11) above which MDD improvement is markedly less likely. While deci-
8


## Page 9


sion trees are commonly overlooked in both modern machine learning and traditional statistical analyses, they can
generate predictive rules that can be easily interpreted and applied by clinicians and thus directly inform clinical
decision-making (Banerjee et al., 2019).
In addition to the interpretability of decision trees, our machine learning-based pipeline, while computationally
intensive, offers distinct advantages over traditional statistical approaches. Our framework systematically evaluated
both linear models (such as logistic regression) and non-linear models (such as decision trees and random forests),
allowing for the discovery of complex relationships that a single, simpler model might miss. Our methodology is
also inherently robust: by combining random forest-based multiple imputation with Monte Carlo cross-validation,
we rigorously accounted for uncertainty arising from both missing data and participant sampling without making
strong distributional assumptions. Finally, our forward variable selection process, which included stringent criteria for
model improvement and correction for multiple comparisons, provided a defense against overfitting and identified a
parsimonious model while effectively handling co-linearity. While baseline GAD-7 and SDS scores were correlated,
the selection algorithm identified GAD-7 as the most powerful single predictor and determined that adding SDS
offered no significant improvement in predictive performance. This avoids the unstable coefficient estimates and
interpretation challenges that co-linearity creates in standard multivariate regression, resulting in a more parsimonious
and robust final model.
It is important to note two limitations of this study. As would be expected from a remotely-recruited national
sample for an effectiveness trial, there is a substantial proportion of missing data. We address this limitation by using
a rigorous multiple imputation approach, and with a sensitivity analysis that reduces the proportion of missing data
by excluding participants with only minimal baseline data. Furthermore, in a supplementary complete-case analysis,
we showed that GAD-7 predicts MDD improvement in a logistic regression model, confirming a statistically signif-
icant association in the raw, unimputed data (see Supplementary Section 3 for details). While this simpler analysis
corroborates our findings, our primary machine learning-based methodology offers several distinct advantages. First,
our analysis mitigates the risk of attrition bias, a significant concern given that the complete-case analysis excludes
the majority of study participants. Second, multiple imputation increases statistical power while accounting for un-
certainty introduced by missing data. Third, our approach is hypothesis-free, identifying GAD-7 as the best predictor
of MDD outcomes without a priori assumptions. Finally, our analysis yielded a clinically intuitive threshold (GAD-7
≥11) rather than a less interpretable odds ratio for an ordinal predictor.
A second limitation is that our analysis cannot establish causal associations. One possible explanation for the
association between baseline GAD-7 and MDD improvement is that anxiety hinders participants’ engagement with
smartphone-delivered interventions. Given findings from previous studies that comorbid anxiety reduces pharma-
cological treatment response in MDD (e.g., Fava et al. (2008); Saveanu et al. (2015); Dold et al. (2017)), it is also
conceivable that comorbid anxiety hinders treatment response through a mechanism that is independent of treatment
modality. A third possibility, which our results support most strongly, is that anxiety is a prognostic factor for poorer
short-term MDD outcomes, an effect that is independent of both treatment assignment and treatment adherence. The
9


## Page 10


original clinical trial analysis found higher MDD remission rates for moderately depressed participants in the Project
EVO and iPST groups compared to the Health Tips control group, despite also reporting that the majority of par-
ticipants in the active treatment groups did not download the assigned intervention app (Arean et al., 2016). Our
analysis, which used different inclusion criteria and was designed to identify outcome predictors with corrections for
multiple comparisons, not treatment effectiveness specifically, did not identify treatment assignment as a significant
predictor. This is consistent with our finding that GAD-7 ≥11 predicted lower odds of improvement within both
the active treatment groups and the Health Tips control group, supporting the interpretation that baseline anxiety is
a general prognostic factor for poorer short-term MDD outcomes in this context, rather than a predictor of response
to a specific treatment. While the point estimates for the odds ratios are consistent with a stronger association be-
tween baseline anxiety and MDD improvement in the active treatment groups than in the control group, their wide
and overlapping confidence intervals preclude a definitive conclusion about an interaction between baseline anxiety
and treatment assignment. Ultimately, our study cannot distinguish between treatment-related, treatment-unrelated,
or combined mechanisms for the observed association between baseline GAD-7 scores and PHQ-9 score reductions.
The link between higher baseline anxiety and lower odds of MDD improvement in this setting may have clinically
actionable implications. For example, if this association is partly due to patients with comorbid anxiety struggling to
engage with smartphone-delivered interventions, these patients might need additional support or different therapeutic
approaches. Regardless of the underlying mechanisms, one practical implication of our results is that future random-
ized controlled trials of smartphone-delivered interventions for MDD should consider stratifying by baseline anxiety
levels.
Acknowledgements
Morgan B. Talbot’s time was partially supported by the National Institute of General Medical Sciences under
Award T32GM144273, and partially supported by Massachusetts Institute of Technology through the David and
Beatrice Yamron Fellowship. Dr. Lipschitz’s time was partially supported by the National Institute of Mental Health
(NIMH) under Grant MH120324. Dr. Costilla-Reyes’ time was partially supported by the National Science Founda-
tion (NSF) under Award 1918839. The content of this paper is solely the responsibility of the authors and does not
necessarily represent the official views of any of the above organizations.
References
Anguera, J.A., Jordan, J.T., Castaneda, D., Gazzaley, A., Are´an, P.A., 2016. Conducting a fully mobile and randomised clinical trial for depression:
access, engagement and expense. BMJ Innovations 2.
Arean, P.A., Hallgren, K.A., Jordan, J.T., Gazzaley, A., Atkins, D.C., Heagerty, P.J., Anguera, J.A., 2016. The use and effectiveness of mobile apps
for depression: results from a fully remote clinical trial. Journal of Medical Internet Research 18, e330.
Banerjee, M., Reynolds, E., Andersson, H.B., Nallamothu, B.K., 2019. Tree-based analysis: a practical approach to create clinical decision-making
tools. Circulation: Cardiovascular Quality and Outcomes 12, e004879.
Beard, C., Bj¨orgvinsson, T., 2014. Beyond generalized anxiety disorder: psychometric properties of the GAD-7 in a heterogeneous psychiatric
sample. Journal of anxiety disorders 28, 547–552.
10


## Page 11


Benjamini, Y., Hochberg, Y., 1995. Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal
Statistical Society: Series B (Methodological) 57, 289–300.
Bush, K., Kivlahan, D.R., McDonell, M.B., Fihn, S.D., Bradley, K.A., Project, A.C.Q.I., 1998. The AUDIT alcohol consumption questions
(AUDIT-C): an effective brief screening test for problem drinking. Archives of Internal Medicine 158, 1789–1795.
Dold, M., Bartova, L., Souery, D., Mendlewicz, J., Serretti, A., Porcelli, S., Zohar, J., Montgomery, S., Kasper, S., 2017. Clinical characteristics
and treatment outcomes of patients with major depressive disorder and comorbid anxiety disorders-results from a European multicenter study.
Journal of Psychiatric Research 91, 1–13.
Fava, M., Rush, A.J., Alpert, J.E., Balasubramani, G., Wisniewski, S.R., Carmin, C.N., Biggs, M.M., Zisook, S., Leuchter, A., Howland, R., et al.,
2008. Difference in treatment outcome in outpatients with anxious versus nonanxious depression: a STAR*D report. American Journal of
Psychiatry 165, 342–351.
Gaynes, B.N., Lux, L., Gartlehner, G., Asher, G., Forman-Hoffman, V., Green, J., Boland, E., Weber, R.P., Randolph, C., Bann, C., et al., 2020.
Defining treatment-resistant depression. Depression and Anxiety 37, 134–145.
Greenberg, J.L., Weingarden, H., Hoeppner, S.S., Berger-Gutierrez, R.M., Klare, D., Snorrason, I., Costilla-Reyes, O., Talbot, M., Daniel, K.E.,
Vanderkruik, R.C., et al., 2024. Predicting response to a smartphone-based cognitive-behavioral therapy for body dysmorphic disorder. Journal
of Affective Disorders 355, 106–114.
Kroenke, K., Spitzer, R.L., Williams, J.B., 2001. The PHQ-9: validity of a brief depression severity measure. Journal of General Internal Medicine
16, 606–613.
Kroenke, K., Spitzer, R.L., Williams, J.B., Monahan, P.O., L¨owe, B., 2007. Anxiety disorders in primary care: prevalence, impairment, comorbidity,
and detection. Annals of internal medicine 146, 317–325.
Linardon, J., Torous, J., Firth, J., Cuijpers, P., Messer, M., Fuller-Tyszkiewicz, M., 2024. Current evidence on the efficacy of mental health
smartphone apps for symptoms of depression and anxiety. a meta-analysis of 176 randomized controlled trials. World Psychiatry 23, 139–149.
Moreno-Agostino, D., Wu, Y.T., Daskalopoulou, C., Hasan, M.T., Huisman, M., Prina, M., 2021. Global trends in the prevalence and incidence of
depression: a systematic review and meta-analysis. Journal of Affective Disorders 281, 235–243.
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., et al., 2011.
Scikit-learn: Machine learning in Python. Journal of Machine Learning Research 12, 2825–2830.
Rubin, D.B., 1987. Multiple imputation for nonresponse in surveys. John Wiley & Sons, New York.
Sage Bionetworks, 2018. Brighten study public researcher portal. https://www.synapse.org/Synapse:syn10848316. Accessed: 2025-07-
22, Synapse ID: syn10848316.
Saveanu, R., Etkin, A., Duchemin, A.M., Goldstein-Piekarski, A., Gyurak, A., Debattista, C., Schatzberg, A.F., Sood, S., Day, C.V., Palmer, D.M.,
et al., 2015. The international study to predict optimized treatment in depression (iSPOT-D): outcomes from the acute phase of antidepressant
treatment. Journal of Psychiatric Research 61, 1–12.
Sextl-Pl¨otz, T., Steinhoff, M., Baumeister, H., Cuijpers, P., Ebert, D.D., Zarski, A.C., 2024. A systematic review of predictors and moderators of
treatment outcomes in internet-and mobile-based interventions for depression. Internet Interventions , 100760.
Sheehan, D., 1983. The Anxiety Disease. Scribner, New York.
Spitzer, R.L., Kroenke, K., Williams, J.B., L¨owe, B., 2006. A brief measure for assessing generalized anxiety disorder: the GAD-7. Archives of
Internal Medicine 166, 1092–1097.
Thornicroft, G., Chatterji, S., Evans-Lacko, S., Gruber, M., Sampson, N., Aguilar-Gaxiola, S., Al-Hamzawi, A., Alonso, J., Andrade, L., Borges,
G., et al., 2017. Undertreatment of people with major depressive disorder in 21 countries. British Journal of Psychiatry 210, 119–124.
Un¨utzer, J., Katon, W., Callahan, C.M., Williams Jr, J.W., Hunkeler, E., Harpole, L., Hoffing, M., Della Penna, R.D., No¨el, P.H., Lin, E.H., et al.,
2002. Collaborative care management of late-life depression in the primary care setting: a randomized controlled trial. Journal of the American
Medical Association (JAMA) 288, 2836–2845.
Wilson, S., 2020.
miceRanger: Multiple imputation by chained equations with random forests.
https://cran.r-project.org/web/
packages/miceRanger/index.html. CRAN package (R).
11


## Page 12


Supplementary Material: Comorbid anxiety predicts lower odds of MDD
improvement in a trial of smartphone-delivered interventions
Morgan B. Talbota,b,c,∗, Jessica M. Lipschitz†b,d, Omar Costilla-Reyes†e
† Co-Senior Authors
aMassachusetts Institute of Technology, 77 Massachusetts Avenue, Cambridge, MA, 02139, USA
bHarvard Medical School, 25 Shattuck St, Boston, MA, 02115, USA
cBoston Children’s Hospital, 300 Longwood Avenue, Boston, MA, 02115, USA
dBrigham and Women’s Hospital, 75 Francis Street, Boston, MA, 02115, USA
eEqu Healthcare, Watertown, MA, 02472, USA. Work completed while at MIT.
1. Full table of selected and alternate models from main analysis
This section provides the complete results from our main analysis, supplementing the summary table in the main
manuscript (Main Text Table 1). We tested five categories of classical machine learning algorithms: logistic regres-
sion, support vector machines, decision trees, random forests, and k-nearest-neighbors. For the tree-based models, we
ran the analysis for maximum tree depths ranging from 1 to 5.
Supplementary Table 1 presents the performance metrics for all models that performed significantly above the
chance level. The additional results shown here are fully consistent with the conclusions in the main text. For
both decision trees and random forests, increasing the tree depth beyond 1 or 2 offered no substantive improvement
in performance. Although deeper trees yielded marginally increased AUC point estimates, accuracy remained nearly
identical across all depths. This occurs because AUC rewards models that assign more fine-grained probability scores,
which deeper trees can achieve by partitioning the data into more groups. However, the stability of the accuracy metric
suggests that a single decision threshold (as found in a depth = 1 tree) is sufficient to capture the main predictive
relationship in this dataset.
2. Sensitivity analyses
We conducted alternate versions of our main analysis to assess the sensitivity of our findings to certain assumptions
and data pre-processing decisions. Specifically, we tested sensitivity to the timing of the Patient Health Questionnaire-
9 (PHQ-9) used to measure outcomes, and to participant exclusion criteria based on data missingness.
This document contains supplementary material for the following published article:
Full citation: Talbot, Morgan B., Jessica M. Lipschitz†, and Omar Costilla-Reyes†. “Comorbid anxiety predicts lower odds of MDD im-
provement in a trial of smartphone-delivered interventions.” Journal of Affective Disorders 394 (2026): 120416. † Co-Senior Authors. DOI:
10.1016/j.jad.2025.120416
∗Corresponding author at: Department of Health Sciences and Technology, Massachusetts Institute of Technology, 77 Massachusetts Avenue
Building E25-518, Cambridge, MA 02139, USA.
Email address: mtalbot@mit.edu (Morgan B. Talbot)
Published in Journal of Affective Disorders (2026)
October 30, 2025


## Page 13


Model Type
Interp?
AUC
Accuracy
Depth
Pred.
Coefficient
Logistic Regression
Yes
0.74 (0.65, 0.82)
0.69 (0.61, 0.77)
-
GAD-7
-0.96 (-1.13, -0.80)
0.71 (0.62, 0.79)
0.66 (0.58, 0.74)
-
SDS
-0.75 (-0.93, -0.57)
Support Vector Machine
Yes
0.74 (0.65, 0.82)
0.70 (0.62, 0.78)
-
GAD-7
-1.01 (-1.15, -0.88)
0.70 (0.61, 0.79)
0.66 (0.57, 0.74)
-
SDS
-0.81 (-0.98, -0.58)
Random Forest
No
0.74 (0.65, 0.82)
0.70 (0.62, 0.78)
2
GAD-7
-
0.73 (0.64, 0.81)
0.70 (0.62, 0.78)
3
GAD-7
-
0.73 (0.65, 0.81)
0.70 (0.62, 0.78)
1
GAD-7
-
0.73 (0.64, 0.81)
0.70 (0.62, 0.77)
4
GAD-7
-
0.73 (0.64, 0.81)
0.69 (0.61, 0.77)
5
GAD-7
-
0.70 (0.61, 0.79)
0.66 (0.58, 0.74)
2
SDS
-
0.70 (0.61, 0.78)
0.66 (0.57, 0.74)
1
SDS
-
0.69 (0.60, 0.78)
0.66 (0.57, 0.73)
3
SDS
-
0.69 (0.60, 0.78)
0.65 (0.56, 0.73)
4
SDS
-
0.69 (0.59, 0.77)
0.65 (0.56, 0.73)
5
SDS
-
Decision Tree
Yes
0.73 (0.64, 0.81)
0.70 (0.61, 0.77)
3
GAD-7
-
0.73 (0.64, 0.81)
0.69 (0.61, 0.77)
4
GAD-7
-
0.72 (0.64, 0.80)
0.70 (0.62, 0.78)
2
GAD-7
-
0.72 (0.64, 0.81)
0.69 (0.61, 0.77)
5
GAD-7
-
0.70 (0.61, 0.77)
0.69 (0.61, 0.77)
1
GAD-7
-
0.69 (0.60, 0.77)
0.65 (0.57, 0.73)
3
SDS
-
0.68 (0.60, 0.77)
0.65 (0.57, 0.73)
2
SDS
-
0.68 (0.59, 0.77)
0.65 (0.56, 0.73)
4
SDS
-
0.68 (0.59, 0.77)
0.65 (0.56, 0.73)
5
SDS
-
0.65 (0.56, 0.73)
0.64 (0.55, 0.73)
1
SDS
-
K-Nearest-Neighbors
No
N.S.
N.S.
-
N.S.
-
Table 1: Performance results for all models predicting significantly above chance during forward variable selection in the main analysis.
The format of this table matches that of Main Text Table 1, which contains a subset of the results shown here. Values in parentheses are 95%
confidence intervals. “Interp.” indicates whether each model type is considered interpretable. Coefficients for logistic regression and support
vector machine models are for standardized features with mean = 0 and std = 1. “Depth” indicates the maximum tree depth for tree-based models.
Alternative models that predicted significantly above chance, but were not selected by the forward process, are shown in gray.
2


## Page 14


2.1. Sensitivity to timing of endpoint PHQ-9 measurement
In the main analysis for our study, we used a PHQ-9 measurement 4 weeks after trial enrollment to assess
MDD outcomes. Participants were considered to have experienced MDD improvement if their PHQ-9 score on
post-enrollment week 4 was both less than 10 and reduced by at least 50% relative to baseline. In this sensitivity anal-
ysis, we apply the same MDD improvement criterion to PHQ-9 measurements on post-enrollment week 12. In the
original Brighten trial, PHQ-9 scores were measured at baseline and on weeks 1, 2, 3, 4, 6, 8, 10, and 12 (Arean et al.,
2016). The missingness of PHQ-9 measurements on these weeks respectively is as follows: 52%, 58%, 59%, 60%,
67%, 72%, 75%, 77%. Like in our main analysis, we employ a random-forest based multiple imputation approach
to impute missing values. In this case, we include PHQ-9 values at all weeks (i.e., up to week 12) in the imputation
procedure.
Supplementary Table 2 shows the full results of this sensitivity analysis, which are highly similar to those of our
main analysis. Generalized Anxiety Disorder-7 (GAD-7) remains the most important predictor, with SDS yielding
alternative, statistically significant but less performant models of all types. Both AUC and accuracy for models using
GAD-7 fall within narrow ranges across all model types, with depth = 1 decision trees performing equivalently to trees
with higher maximum depth values. Like in the main analysis, we fitted depth = 1 decision trees on every imputed
version of the dataset and took the median GAD-7 threshold. This yielded the same prediction rule of GAD-7 ≥11
predicting lower odds of MDD improvement, with an odds ratio of 0.27 (95% CI [0.17, 0.43], p < 0.0001). The
results of this sensitivity analysis indicate that GAD-7 ≥11 predicts lower odds of MDD improvement in this trial on
a 12-week time scale in addition to a 4-week time scale.
2.2. Sensitivity to exclusion of participants with minimal data
Of the participants included in our main analysis, 41% were missing all baseline and post-baseline clinical ques-
tionnaire data aside from baseline PHQ-9. While these participants were assigned to receive one of three smartphone-
delivered interventions in the original Brighten study (Anguera et al., 2016; Arean et al., 2016), the only available data
from them are demographic variables and baseline PHQ-9. These participants are the primary source of missingness
in the overall dataset. To evaluate the effect of relatively extensive imputation of missing values, we conducted a
sensitivity analysis that excluded this subset of participants, with the caveat that this approach has the potential to
introduce selection biases. Participants were included in this analysis if they met the following criteria:
1. Baseline PHQ-9 of 10 or higher (same as main analysis)
2. No endorsed history consistent with bipolar disorder (same as main analysis)
3. At least one of the following measurements: AUDIT alcohol consumption questions (AUDIT-C, at baseline),
GAD-7 (at baseline), IMPACT Mania and Psychosis Screening (at baseline), Sheehan Disability Scale (SDS, at
baseline), or PHQ-9 at 1, 2, 3, or 4 weeks post-enrollment.
3


## Page 15


Model Type
Interp?
AUC
Accuracy
Depth
Pred.
Coefficient
Logistic Regression
Yes
0.68 (0.59, 0.77)
0.64 (0.55, 0.72)
-
GAD-7
-0.65 (-0.85, -0.50)
0.66 (0.56, 0.75)
0.61 (0.52, 0.70)
-
SDS
-0.58 (-0.76, -0.41)
Support Vector Machine
Yes
0.68 (0.59, 0.77)
0.63 (0.55, 0.71)
-
GAD-7
-0.84 (-1.00, -0.72)
0.66 (0.56, 0.75)
0.61 (0.52, 0.69)
-
SDS
-0.81 (-0.92, -0.70)
Random Forest
No
0.67 (0.58, 0.76)
0.65 (0.56, 0.73)
2
GAD-7
-
0.67 (0.58, 0.76)
0.65 (0.56, 0.73)
1
GAD-7
-
0.67 (0.57, 0.76)
0.64 (0.56, 0.73)
3
GAD-7
-
0.66 (0.57, 0.76)
0.64 (0.55, 0.72)
4
GAD-7
-
0.66 (0.57, 0.76)
0.63 (0.55, 0.72)
5
GAD-7
-
0.65 (0.56, 0.74)
0.60 (0.52, 0.69)
2
SDS
-
0.65 (0.56, 0.74)
0.60 (0.52, 0.69)
1
SDS
-
0.64 (0.54, 0.73)
0.60 (0.51, 0.68)
3
SDS
-
0.63 (0.54, 0.72)
0.59 (0.50, 0.68)
4
SDS
-
Decision Tree
Yes
0.66 (0.57, 0.75)
0.64 (0.55, 0.73)
3
GAD-7
-
0.66 (0.57, 0.75)
0.63 (0.55, 0.72)
5
GAD-7
-
0.66 (0.57, 0.74)
0.64 (0.56, 0.73)
2
GAD-7
-
0.66 (0.57, 0.75)
0.63 (0.55, 0.72)
4
GAD-7
-
0.65 (0.56, 0.73)
0.65 (0.56, 0.73)
1
GAD-7
-
0.63 (0.54, 0.72)
0.59 (0.51, 0.68)
3
SDS
-
0.63 (0.54, 0.72)
0.60 (0.51, 0.68)
2
SDS
-
K-Nearest-Neighbors
No
N.S.
N.S.
-
N.S.
-
Table 2: Performance results for all models predicting significantly above the chance level in a sensitivity analysis, in which MDD outcomes
were predicted at week 12 instead of week 4. The format of this table is identical to Main Text Table 1 and Supplementary Table 1.
4


## Page 16


The third criterion above excluded 279 (41%) of the 638 otherwise eligible participants who were included in our main
analysis, leaving a sample size of n = 359. This sensitivity analysis used the same set of variables as the main analysis
for imputation, variable selection, and outcome prediction. The missingness of the dataset used for this sensitivity
analysis is as follows: 54% missing satisfaction with level of income, 10% missing AUDIT-C, 11% missing GAD-7,
11% missing SDS, and 0%, 20%, 30%, 31%, and 33% missing PHQ-9 at baseline and weeks 1-4 respectively. All
other variables had 0% missingness.
The model performance results of this sensitivity analysis are shown in Supplementary Table 3. Only one model
predicted significantly above chance, a depth = 2 random forest using GAD-7 as the sole predictor. It is likely that
other models failed to cross the significance threshold because of the considerably reduced sample size relative to
the main analysis. Although it did not survive the correction for multiple comparisons with statistical significance,
we examine the depth = 1 decision tree using GAD-7 as a predictor due to its central role in our main findings.
This model had a mean cross-validated AUC of 0.63 (95% CI: [0.53, 0.74], p = 0.007, not significant), with mean
accuracy 0.63 (95% CI: [0.51, 0.74]). As in the main analysis, we fitted depth = 1 decision trees to each imputed
dataset version, finding the median GAD-7 threshold to yield the same GAD-7 ≥11 decision rule as our main results.
In this sensitivity analysis, GAD-7 ≥11 predicts lower odds of MDD improvement with odds ratio 0.30 (95% CI
[0.18, 0.49], p < 0.0001).
While the results of this sensitivity analysis did not find evidence for a depth = 1 decision tree at the level of
variable selection, a random forest model using GAD-7 predicted significantly above chance even under correction
for multiple comparisons. Furthermore, testing the GAD-7 hypothesis generated by forward selection in our main
analysis produced the same GAD-7 ≥11 threshold and yielded a highly significant odds ratio. While this should be
interpreted with caution as an exploratory finding, the overall results of this sensitivity analysis are consistent with
those of the main analysis.
Model Type
Interp?
AUC
Accuracy
Depth
Pred.
Coefficient
Logistic Regression
Yes
N.S.
N.S.
-
N.S.
N.S.
Support Vector Machine
Yes
N.S.
N.S.
-
N.S.
N.S.
Random Forest
No
0.67 (0.55, 0.78)
0.64 (0.54, 0.75)
2
GAD-7
-
Decision Tree*
Yes
0.63 (0.53, 0.74)*
0.63 (0.51, 0.74)
1
GAD-7
-
K-Nearest-Neighbors
No
N.S.
N.S.
-
N.S.
-
Table 3: Performance results for all models predicting significantly above chance in a sensitivity analysis, which excluded participants with
only baseline demographic data and no questionnaire data beyond baseline PHQ-9. The format of this table is identical to Main Text Table
1 and Supplementary Table 1. *The model marked with an asterisk did not meet the statistical significance threshold for forward selection in this
sensitivity analysis (under correction for multiple comparisons), but is shown for its relevance to the hypothesis generated in the main analysis.
5


## Page 17


3. Post-hoc complete-case analysis of GAD-7 and MDD improvement
To confirm that the association between baseline anxiety and MDD outcomes was present in the raw data prior to
imputation, we conducted a supplementary complete-case logistic regression analysis. This analysis was restricted to
participants with non-missing data for both the baseline GAD-7 questionnaire and the week 4 PHQ-9 score, which is
required to calculate the MDD improvement outcome. This exclusion criterion resulted in a sample of 228 partici-
pants, a reduction of 410 from the 638 participants included in the primary intention-to-treat analysis. The substantial
proportion of excluded participants highlights the primary limitations of a complete-case approach: a high risk of
selection bias and a reduction in statistical power.
Despite these limitations, the analysis confirmed a statistically significant negative association between baseline
GAD-7 scores and the odds of MDD improvement. Logistic regression showed an MDD-improvement odds ratio
of 0.93 (95% CI [0.89, 0.98], p = 0.006) for each one-point increase in GAD-7 score. This result, derived from
the unimputed data, corroborates our study’s primary finding that higher baseline anxiety is a significant predictor of
reduced odds of MDD improvement in this trial.
References
Anguera, J.A., Jordan, J.T., Castaneda, D., Gazzaley, A., Are´an, P.A., 2016. Conducting a fully mobile and randomised clinical trial for depression:
access, engagement and expense. BMJ Innovations 2.
Arean, P.A., Hallgren, K.A., Jordan, J.T., Gazzaley, A., Atkins, D.C., Heagerty, P.J., Anguera, J.A., 2016. The use and effectiveness of mobile apps
for depression: results from a fully remote clinical trial. Journal of Medical Internet Research 18, e330.
6
## Related

- [[11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409.12071v2_Quantifying_the_role_of_supernatural_entities_and_the_effect_of_missing_data_in_.md|2409.12071v2_Quantifying_the_role_of_supernatural_entities_and_the_effect_of_missing_data_in_]]
- [[11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409.10096v3_Robust_Reinforcement_Learning_with_Dynamic_Distortion_Risk_Measures.md|2409.10096v3_Robust_Reinforcement_Learning_with_Dynamic_Distortion_Risk_Measures]]
- [[11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409.10138v1_A_Method_for_Accurate_Spatial_Focusing_Simulation_via_Numerical_Integration_and_.md|2409.10138v1_A_Method_for_Accurate_Spatial_Focusing_Simulation_via_Numerical_Integration_and_]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 2409_11183v5_comorbid_anxiety_predicts_lower_odds_of_mdd_improvement_in_a_trial_of_smartphone_delive
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2024/2024-09/2409_11183V5_COMORBID_ANXIETY_PREDICTS_LOWER_ODDS_OF_MDD_IMPROVEMENT_IN_A_TRIAL_OF_SMARTPHONE_DELIVERED_INTERVENTIONS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

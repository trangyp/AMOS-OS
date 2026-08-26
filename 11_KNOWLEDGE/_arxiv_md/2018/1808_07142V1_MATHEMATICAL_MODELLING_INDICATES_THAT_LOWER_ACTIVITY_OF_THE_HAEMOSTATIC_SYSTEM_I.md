---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1808.07142v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1808.07142v1_Mathematical_modelling_indicates_that_lower_activity_of_the_haemostatic_system_i

> Source: 1808.07142v1_Mathematical_modelling_indicates_that_lower_activity_of_the_haemostatic_system_i.pdf

> Pages: 19

---


## Page 1


1 
 
Mathematical modelling indicates that lower activity of the haemostatic 
system in neonates is primarily due to lower prothrombin concentration 
 
Ivo Siekmann1,2,*, Stefan Bjelosevic3,4, Kerry Landman5, Paul 
Monagle3,6,7, Vera Ignjatovic3,7,† & Edmund J. Crampin1,2,5,8,† 
 
1Department of Applied Mathematics, Liverpool John Moores University, England 
2Systems Biology Laboratory, University of Melbourne, Australia 
3Haematology Research, Murdoch Children’s Research Institute, Melbourne, Australia 
4The Sir Peter MacCallum Department of Oncology, University of Melbourne, Australia 
5School of Mathematics and Statistics, University of Melbourne, Australia 
6Department of Clinical Haematology, Royal Children’s Hospital, Melbourne, Australia 
7Department of Paediatrics, University of Melbourne, Australia 
8School of Medicine, University of Melbourne, Australia 
 
†Vera Ignjatovic and Edmund J. Crampin contributed equally to this study. 
 
Corresponding Author: 
*Ivo Siekmann, Department of Applied Mathematics, Faculty of Engineering and 
Technology, Liverpool John Moores University, James Parson Building, 3 Byrom Street, 
Liverpool L3 3AF, England, phone: +44 151 231 2092, e-mail: i.siekmann@ljmu.ac.uk


## Page 2


2 
 
Haemostasis is governed by a highly complex system of interacting proteins. Due to the 
central role of thrombin, thrombin generation and specifically the thrombin generation 
curve (TGC) is commonly used as an indicator of haemostatic activity.  Functional 
characteristics of the haemostatic system in neonates and children are significantly 
different compared with adults; at the same time plasma levels of haemostatic proteins 
vary considerably with age. However, relating one to the other has been difficult, both due 
to significant inter-individual differences for individuals of similar age and the complexity 
of the biochemical reactions underlying haemostasis. Mathematical modelling has been 
very successful at representing the biochemistry of blood clotting. In this study we 
address the challenge of large inter-individual variability by parameterising the Hockin-
Mann model with data from individual patients, across different age groups from 
neonates to adults. Calculating TGCs for each patient of a specific age group provides us 
with insight into the variability of haemostatic activity across that age group. From our 
model we observe that two commonly used metrics for haemostatic activity are 
significantly lower in neonates than in older patients. Because both metrics are strongly 
determined by prothrombin and prothrombin levels are considerably lower in neonates 
we conclude that decreased haemostatic activity in neonates is due to lower prothrombin 
availability.  
 
INTRODUCTION 
Recent experimental studies have shown that the plasma levels of blood clotting 
proteins vary considerably, both with age, as well as between healthy individuals of the 
same age1. The haemostatic system in neonates and children also shows considerably 
different functional characteristics compared to adults2-4. Therefore, clinical studies of 
the adult haemostatic system may not be transferrable to the treatment of thrombotic 
and haemorrhagic disorders in young patients. 
 
The high variability of blood clotting protein abundances is an intrinsic property of the 
haemostatic system rather than being caused by flaws of the available experimental 
methods. The complexity of the haemostatic system in combination with the strong 
fluctuations of protein concentrations between individuals and with age makes 
determining the impact of experimentally measured differences in plasma levels of 
individual haemostatic proteins extremely challenging. Mathematical modelling is a 
useful tool for investigating the relative importance of a variety of complicated 
interdependencies in complex systems, and has also been successfully applied to the 
haemostatic system. Early qualitative models focused on investigating the mechanism 
of haemostatic response in rapidly forming a blood clot shortly following an 
injury5,6. More recently, this behaviour known as excitability was investigated in 
mathematical models by Jesty, et al. 7 and Beltrami and Jesty 8. 
 
The next generation of haemostasis models was based on more detailed representations 
of the biochemical reaction network of haemostatic proteins. Representing chemical 
reactions by mass-action kinetics allows for a more data-driven approach by 
measuring rate constants experimentally. Thus, given that sufficient experimental data 
is available, these models not only capture qualitative aspects such as excitability but


## Page 3


3 
 
may also be used to study haemostasis quantitatively. The model by Hockin, et al. 9, 
henceforth referred to as the Hockin-Mann model, consists of a system of 34 ordinary 
differential equations that represents the dynamics of 44 biochemical reactions of the 
haemostatic network by mass action kinetics. Each equation represents the time-
dependent dynamics of one of the haemostatic proteins, or a complex of proteins. For a 
given set of initial concentrations, the Hockin-Mann model enables us to calculate how 
these haemostatic factors change over time.  
 
The Hockin-Mann model continues to be used as the starting point or a building block 
in new models that are being developed. Wajima et al. extend a previous version of 
the Hockin-Mann model in order to study several experimental tests of the haemostatic 
system, its response to different treatments (warfarin, heparin, vitamin K) and to 
perturbations by Taipan snake venom10. Models based on the Hockin-Mann model have 
been developed for studying the effect of anti-coagulants such as e.g. the novel anti-
coagulant (NOAC) rivaroxaban11,12. Most recently Mitrophanov et al. used the Hockin-
Mann model for investigating the effects of acidosis on thrombin generation13.  
 
Gaining systematic insight into the behaviour of highly detailed models within the order 
of tens or even hundreds of equations is a difficult problem. Danforth et al. follow a 
computational approach for investigating the parameter sensitivity of the Hockin-Mann 
model14. In this study they examine the sensitivity of thrombin generation as well as the 
behaviour of the full model on variations of individual rate constants in a range from 10 
to 1000 % of the reference values given in the original publication9. In Danforth, et al. 
15 the statistical approach from14 is used to assess the sensitivity of thrombin generation 
to variations in blood haemostatic factors, both utilising synthetically generated 
combinations of concentrations, as well as data from healthy adults (patients with 
haemophilia A and a population receiving warfarin). The study presented here follows a 
similar approach as Danforth, et al. 15 but we investigate healthy individuals from 
different age groups rather than different adult populations. Most recently, Dunster and 
King 16 demonstrated, via a thorough mathematical analysis of one of the earlier models 
of haemostasis by Willems, et al. 17, how, taking advantage of distinct time scales, 
simplified models for different phases of thrombin generation can be derived. These 
phases can be related to the initiation, propagation and termination phase of thrombin 
generation. Because the simplified models are much easier to analyse than the full 
model, the dominant mechanisms in each of six different phases can be clearly 
identified.  
 
This study aims to investigate age-dependent changes of the blood clotting system. In 
the absence of knowledge regarding changes to the network of biochemical reactions 
itself, we use the Hockin-Mann model as a representation of the haemostatic system of 
all age classes. In order to test the hypothesis that age-dependent changes are due to 
differences in the plasma levels of blood clotting proteins we use age-stratified data by 
Attard, et al. 1. In contrast to previous studies we explicitly account for variability between 
individuals by parametrising the initial concentrations of haemostatic factors with data from


## Page 4


4 
 
individual patients – in fact, our results show that choosing the levels of haemostatic factors 
based on data aggregated for different age groups would be misleading. 
 
Different to earlier experimental studies of the age-dependent blood clotting system which were 
based on functional assays2,3, Attard et al. have presented the first comprehensive data set that 
provides quantitative age-stratified protein levels. Quantitative assays are clearly more suitable 
than functional data for obtaining blood clotting factor concentrations necessary for 
parametrising models of haemostasis because functional assays only provide a proxy for 
concentrations. For this reason, caution is required when comparing with older data sets based 
on functional assays. 
 
To the best of our knowledge, this is the first time that a model of the haemostatic system is 
parameterised with age-stratified haemostatic protein abundance data. This allows us to link 
observed age-dependent differences in the concentrations of individual haemostatic factors to 
functional implications for the activity of the haemostatic system. 
 
RESULTS 
In order to account for the strong inter-individual variability in different age groups we 
parametrised the initial protein concentrations in the Hockin-Mann model with levels of 
prothrombin, FV, FVII, FVIII, FIX and FX measured in individual patients1. For all age 
groups, we compared TGCs calculated from the mean levels of these haemostatic 
proteins, see Supplementary Material, Figure S1, with TGCs calculated for individual 
patients (Figure S2). In analogy to experimental studies, four indices were used for quantifying 
different aspects of a given thrombin curve (Figure 2): The lag time (LAG) – the time it takes 
until thrombin exceeds a certain fraction of its maximum - and the time it takes until 
thrombin reaches its maximum, the time to thrombin peak (TTP) indicate how 
quickly thrombin is generated in response to stimulation by TF. The other two 
indices, the maximum total thrombin generation (MAX) and the area under the 
thrombin curve (AUC), are measures for the strength of this response.  
 
The results show that a TGC calculated for the mean plasma levels of haemostatic 
proteins of a particular age class fails to accurately represent some of the properties of 
the TGCs calculated for individual patients. For example, whereas the TGCs calculated 
from mean plasma levels suggest that the TTP is approximately ݐ= 300ݏ, especially the 
results for teenagers and adults suggest that no such pattern exists because the TTP 
strongly varies within age groups. It was therefore considered essential to carry out further 
analysis based on TGCs calculated for individual patients. The results for individuals in each 
of the age groups for LAG, TTP, MAX and AUC are presented in Figure 3. The levels 
of LAG and TTP show no significant differences between different age groups. 
In contrast, both thrombin maximum (MAX) and area under thrombin curve (AUC) 
exhibit a significant increase from a low level observed for neonates at day 1 and day 3 
compared to other age groups. Also, the higher value of MAX and AUC for children 
less than one year old until adults is statistically similar (Figure 3).


## Page 5


5 
 
We then investigated the relationship between MAX and AUC and the initial 
concentrations of the blood clotting factors reported by Attard, et al. 1. Figure 4 shows 
that MAX appeared to increase linearly with prothrombin concentration. Figure 5 
suggests that AUC was solely determined by the concentration of prothrombin and 
was not dependent of the concentrations of all other haemostatic factors.  
 
Age-related differences in the concentrations of haemostatic factors, based on Attard, et 
al. 1 are shown in Figure 1. The concentrations of factor VII and factor IX clearly 
increased with age. The concentration of factor VIII did not change with age whereas 
for concentrations of factors V and X the dependence with age is less obvious. 
However, for the concentration of prothrombin we observed a clear jump from a low 
level of approximately 0.5 IU/mL to more than 1.0 IU/mL in the other age groups. 
Hence there were essentially two different levels of prothrombin concentrations for 
neonates compared with the other age groups, in contrast to factors VII and IX whose 
concentrations increased continuously with age. 
 
DISCUSSION 
Developmental haemostasis is a concept that describes multiple and complex age-
specific differences in the haemostatic system. The overall impact of these differences 
is believed to provide protection for the neonate and child in terms of response to 
bleeding and clotting stimuli. However, predicting the response to diseases that affect 
haemostasis, or to the multitude of new anticoagulant drugs that are becoming available 
for clinical care in children is challenging. Conducting large-scale trials of these drugs 
in children, such as those performed in adults, has proven to be very difficult. Thus, the 
development of a mathematical model that simulates the age appropriate haemostatic 
system would be very advantageous. 
 
We presented a novel mathematical modelling approach that enables us to link age-
related differences of haemostatic factors in neonates, children and adults to functional 
differences in their haemostatic system. The key contribution of this study is that data from 
individual patients has been used for parametrising the Hockin-Mann model. This enables us to 
appropriately account for the strong inter-individual variability present in different age groups, 
in contrast to the more common approach of obtaining aggregated parameters from population 
statistics – compare Figures S1 and S2 in the Supplementary Material. Because we calculate a 
thrombin curve for each individual patient, unlike previous studies, we are in a unique and novel 
position to draw conclusions regarding the variability of haemostatic activity based on realistic 
distributions of blood clotting factors from individual patients. We note that this is different to 
simply investigating the effect of upper and lower bounds of individual blood clotting factors 
because this ignores correlations between different factor levels – the strong variations of the 
correlation structure between various haemostatic factors is shown in Figure S3 of the 
Supplementary Material.  
 
Our approach is based on the hypothesis that the biochemical reactions of the haemostatic 
system are similar between different subjects and remain unchanged with age so that 
differences in haemostatic factor concentrations are the main source of observed age-related


## Page 6


6 
 
differences in haemostatic activity. Under these considerations, a model parameterised 
with age-stratified abundances of haemostatic factors (while leaving the reaction rate 
constants unchanged) fully accounts for age-related differences in the haemostatic 
system. The implications of these assumptions, in particular, the role of inhibitors, will 
be discussed in more detail below. Moreover, we will present a preliminary data set 
collected by two of the co-authors that confirms the qualitative differences between 
neonates and older age groups predicted by the model.  
 
Our main finding is that for neonates at day 1 and day 3 post-birth, MAX and AUC 
were significantly lower than in older age groups indicating a lower activity of the 
haemostatic system. Importantly, our model enables us to identify a significantly lower 
prothrombin level as the most likely cause for this observation. This simple relationship 
between prothrombin and indicators of blood clotting activity bypasses the complex 
correlation structure between haemostatic factors apparent in Figure S3 of the 
Supplementary Material. 
 
First, we found that whereas LAG and TTP are unchanged with age, MAX and AUC 
are significantly different between neonates and all other age groups. Both are elevated 
from a low level of approximately 200 nM or 500 nM·min, respectively, for neonates at 
day 1 and day 3 to significantly higher levels of 400 nM or 1000 nM·min for all other 
age groups. In Figure 6  we demonstrate that the increase of AUC for age groups older 
than day 3 predicted by the model is consistent with age-stratified measurements of 
AUC (Ignjatovic and Monagle, unpublished). This confirms that although some 
possible age-dependent changes in the haemostatic system are not accounted for, the 
model behaviour related to the indices considered in this study is nevertheless 
qualitatively correct. 
 
Second, we observed that prothrombin concentration is a strong predictor for MAX and 
AUC. This has been reported in both the modelling15 as well as in the experimental 
literature18 albeit in different settings as our study. Danforth, et al. 15 showed that both 
MAX and AUC depend most sensitively on prothrombin in their simulation study of the 
Hockin-Mann model. For the Willems, et al. 17 model, Dunster and King 16 demonstrate 
that both MAX as well as AUC increase linearly with prothrombin concentration and 
give Duchemin, et al. 18 as a reference which experimentally confirms this observation 
from the mathematical model. None of the above studies refers to different age groups.  
 
Third, by combining our observations, we identify the lower prothrombin concentration 
as the cause for the lower values of MAX and AUC in neonates. Whereas our model 
shows that MAX and AUC are lower in neonates at day 1 and day 3 post-birth than in 
the older age groups, we know from the Attard, et al. 1 data that neonates also have a 
decreased prothrombin concentration compared to adults. Taking into account that 
MAX and AUC are largely determined by prothrombin we conclude that the lower 
thrombin production in neonates is primarily due to lower prothrombin availability.  Although a 
strong influence of prothrombin and indices related to thrombin abundance is not unexpected it 
is interesting that the model suggests that other blood clotting factors hardly play any role in


## Page 7


7 
 
determining MAX and AUC. Given that the haemostatic network is in general characterised by a 
high level of complexity this observation is potentially very useful because it suggests that 
targeting prothrombin may to a great extent be sufficient for regulating the amount of thrombin 
generated.  
 
Because our study relies strongly both on data from individuals as well as quantitative rather 
than functional assays, the influence of several blood clotting proteins such as the inhibitors 
Tissue Factor Pathway Inhibitor (TFPI) and Antithrombin as well as Fibrinogen and 
thrombomodulin could not be accounted for because they were not measured by Attard, et al. 1. 
To the best of our knowledge, comparable age-stratified data sets for these blood clotting factors 
based on quantitative assays are currently not available. Moreover, although Attard et al. 
measured Factor XI (FXI), FXII as well as protein C and protein S, these blood clotting proteins 
could not be included because they are not accounted for by the Hockin, et al. 9 model. Before 
we discuss the possible roles of different inhibitors, we emphasise that our approach to age-
dependent modelling can be easily applied to an extended model as more comprehensive data 
becomes available. 
 
Andrew, et al. 19 observe that the inhibitor Antithrombin was decreased in neonates by 
60% and it has been suggested that this enabled normal haemostatic function. But the 
role of inhibitors in the neonate haemostatic system remains controversial because 
whereas Antithrombin is decreased, the inhibitor α2 Macroglobulin (α2M) is increased. 
In fact, our results are consistent with a recent article by Kremers, et al. 20 which 
attributed the decreased thrombin generation in young patients to decreased 
prothrombin conversion and to a lesser extent to elevated levels of α2M. Nevertheless, 
the issue of clarifying the relative importance of the different inhibitors in neonates 
clearly deserves further investigation. Because this requires extending the Hockin-Mann 
model by the inhibitor α2M we leave the study of this interesting question to future 
work. 
 
In this study, we aimed to represent the experimental assay for determining the activity 
of the haemostatic system via measurement of the thrombin generation curve. For 
representing the in vivo system more detailed models of haemostasis have been 
developed that account for the fluid dynamics of blood within the constraints of the 
blood geometry as well as the interaction with platelets, see, e.g. Cito, et al. 21 or the 
relevant chapters in Ambrosi, et al. 22. 
 
In summary, we have demonstrated that parametrising a mathematical model with data 
of individual patients from different age groups is a useful tool for investigating age-
dependent differences in the haemostatic system. As additional data become available, 
our approach can be easily transferred to more comprehensive models of the in vitro or 
in vivo haemostatic system which will enable us to explore the complex system 
underlying developmental haemostasis in more detail. Considering the considerable 
uncertainty regarding treatment of young patients with coagulation disorders, an 
extremely useful direction will be to incorporate the interactions with haemostatic drugs 
in the age-stratified model presented here.


## Page 8


8 
 
 
METHODS 
In order to account for the strong variability between individuals apparent in the data by Attard 
et al., we simulated the Hockin-Mann model with different parameters for each patient sample. 
This approach has been used earlier for investigating inter-individual variability in adults15. 
Based on these simulation results we then quantified the activity of the haemostatic system by 
four commonly used indices that are derived from the simulated thrombin concentration over 
time, the so-called thrombin generation curve (TGC): the lag time (LAG), the time to thrombin 
peak (TTP), the maximum thrombin concentration (MAX) and the area under the thrombin 
curve (AUC). Finally, we investigated which individual haemostatic factors had the strongest 
influence on each of the four metrics and related our results to differences in the availability of 
haemostatic factors between different age groups. 
 
Parameterisation:  
We parameterised the Hockin-Mann model using age-stratified data from the study by Attard, et 
al. 1, that consists of measurements for factors II and V given as international units (IU/mL) and 
factors VII, VIII, IX and X reported as percentages (%). Data for these six haemostatic factors 
were available for patients from seven age groups, 10 samples each for neonates at day 1 and 
day 3 of age and 20 samples each for the remaining age groups (younger than 1 year, 1-5 years, 
6-10 years, 11-16 years, adults). The distributions over the individual age groups are 
summarised in Figure  but note that in this study we used individual samples – i.e. the raw data. 
Measurements were converted from the original units to concentrations by choosing the average 
adult results measured by Attard et al. as a reference parameter set, see Table 1.  We required that 
these average adult results correspond to the initial concentrations of the Hockin-Mann model, 
see Table III in Hockin, et al. 9 or Table 1, which were chosen as average values in human 
plasma. Thus, measurements from an individual subject were converted to concentrations by 
scaling with respect to the average result for adults, as reported in Attard, et al. 1. 
 
Simulation:  
For each parameter set, our own implementation of the Hockin-Mann model was simulated 
using a numerical solver of the GNU Scientific Library (GSL)23.  For ݐ= 0 initial conditions for 
factors II, V, VII, VIII, IX and X were chosen according to a sample from the data by Attard, et 
al. 1 as described previously. Thrombin generation was initiated by initialising Tissue 
Factor (TF) at [TF]=5pM. The model was simulated until ݐ௘௡ௗ= 5000ݏ to ensure that 
thrombin generation proceeded through all phases from initiation via propagation to 
termination. Total thrombin is represented by two fractions in the Hockin-Mann model, 
meizothrombin (mIIa) and thrombin (IIa). Due to the higher activity of 
meizothrombin, the total amount of thrombin over time, the thrombin generation 
curve (TGC), is calculated by [IIa](t) + 1.2 [mIIa](t) – for details, see Hockin, et al. 
9. A representative example (where termination occurred approximately at   t = 1400 
s) is shown in Figure 2. 
 
Indices of thrombin generation:  
In analogy to experimental studies, thrombin generation was characterized quantitatively by four 
metrics: The lag time (LAG) and the time to thrombin peak (TTP) indicate how quickly


## Page 9


9 
 
thrombin is generated in response to stimulation by TF. In contrast, the remaining 
two indices, the maximum total thrombin generation (MAX) and the area under the 
thrombin curve (AUC), are measures for the strength of this response. The maximum 
total thrombin concentration is defined as 
MAX ≔݉ܽݔ௧∈ሾ଴,௧೐೙೏ሿ൫ሾIIaሿሺݐሻ+ 1.2ሾmIIaሿሺݐሻ൯ 
where [IIA](t) and [mIIa](t) are thrombin and meizothrombin concentration over time, 
respectively, and tend is the end time of the simulation. The time to thrombin peak 
(TTP) is then defined as the elapsed time after stimulating the system with tissue factor 
until the time the concentration MAX is attained. Similarly, the lag time LAG is 
defined as the time until 1/6 of the maximum thrombin concentration MAX is reached. 
The area under the thrombin curve AUC is given by the integral over the thrombin 
curve 
AUC ∶= න
ሾIIaሿሺݐሻ+ 1.2ሾmIIaሿሺݐሻ݀ݐ
௧೐೙೏
଴
 
All four indices are visualised in Figure 2. 
 
Analysis of age-stratified simulation results:  
All statistical analyses of the simulation results were performed in the R software24. 
From the simulations based on the age-stratified data from Attard et al. we obtained age-
stratified results for the four indices LAG, TTP, MAX and AUC. Differences between age 
groups were determined by comparing the distributions of each index. For indices that showed 
age-dependent differences we compared the dependency on measurements of the six haemostatic 
factors II, V, VII, VIII, IX, X by Attard, et al. 1. Finally, we inspected the data from Attard et al. 
for differences in the measurements of the six haemostatic factors II, V, VII, VIII, IX, X for 
different age groups. 
 
ACKNOWLEDGEMENTS 
This research was in part conducted and funded by the Australian Research Council Centre of 
Excellence in Convergent Bio-Nano Science and Technology (project number CE140100036). 
This study was supported by the Victorian Government's Operational Infrastructure Support 
Program.  
 
AUTHOR CONTRIBUTIONS 
All authors collaboratively conceived the study. IS developed and implemented the modelling 
approach with important contributions of KL and EC. VI and PM provided the raw experimental 
data (previously published in aggregated form), and guidance for the interpretation of these data 
and appropriate representation in the mathematical model. IS prepared all figures and together 
with SB, drafted the paper. All authors critically revised the manuscript for important intellectual 
content and approved the final version. VI and EC contributed equally to this study. 
 
COMPETING INTERESTS STATEMENT 
The authors declare that they have no conflicts of interest with the contents of this article.


## Page 10


10 
 
DATA AVAILABILITY STATEMENT 
The datasets analysed during this study are available from the corresponding author upon 
reasonable request. 
 
ETHICAL APPROVAL AND INFORMED CONSENT 
Ethical approval for the experiments carried out in Attard et al. which this work is based on 
was obtained as described there. Briefly, the collection of samples from children and adults 
was approved by the Royal Children’s Hospital Ethics in human Research Committee, 
reference number 2003. The collection of neonatal samples was approved by the Royal 
Women’s Hospital Research Ethics Committee, project 02/08. Informed consent was 
obtained from the parents of the neonates and children and from the adult participants 
themselves. All experiments were conducted according to the guidelines of the Declaration 
of Helsinki.


## Page 11


11 
 
Tables 
 
Table 1: Average, minimum and maximum levels of haemostatic factors for the data from 
Attard et al. (1). The average adult results are chosen as a standard which is assumed to 
correspond to the initial concentrations of the model by Hockin et al. (9). For example, the 
average level of prothrombin 1.33 IU/mL is assumed to equate 1,400 nM. As an example we 
calculate the mean prothrombin level for neonates: 0.562 / 1.33 ⋅ 1,400 nM ≈ 591 nM. For 
the individual age group we provide minimum, maximum and mean concentrations for 
factors II, V, VII, VIII, IX, X so that the range of these concentrations can be assessed.


## Page 12


12 
 
Figure Legends: 
Figure 1: Age-dependent variability of blood clotting factors (see Attard, et al. 1). 
Haemostatic factor abundances are both shown on the original scales in units of IU/mL or 
percentages % as well as in units of nM obtained by conversion according to Table 1. 
 
Figure 2: Thrombin generation curve simulated using the Hockin-Mann model with 
parameters corresponding to an individual adult subject. Four indices that were calculated for 
comparison of TGCs calculated for different subjects are shown; these are lag time (LAG), 
time to peak (TTP), maximum thrombin concentration (MAX) and area under thrombin 
curve (AUC). For the TGC plotted here we have LAG=554s, TTP=742s, MAX=570nM and 
AUC=2191 nM·min. 
 
Figure 3: Age-dependent changes of thrombin generation curve. Whereas lag time (LAG) and 
time to thrombin peak (TTP) seem not to vary with age, thrombin maximum (MAX) and the 
area under the thrombin curve (AUC) increase roughly two-fold with age. 
 
Figure 4: The thrombin maximum MAX increases approximately linearly with prothrombin. 
Similar relationships are seen for the other factors but the variation for the predicted 
thrombin maxima is much higher than the dependency on prothrombin shown here. The 
prothrombin level is both shown on the original scale in units of IU/mL from Attard, et al. 1 
as well as in units of nM obtained by conversion according to Table 1. 
 
Figure 5: The area under the thrombin curve (AUC) is solely determined by the concentration 
of prothrombin. The prothrombin level is both shown on the original scale in units of IU/mL 
from Attard, et al. 1 as well as in units of nM obtained by conversion according to Table 1. 
 
Figure 6: Age-stratified experimental data for the area under the thrombin curve (AUC) is 
compared with the model. Both data and model simulations are scaled by the mean adult 
level to demonstrate age-related differences. The data (white) confirms the approximate two-
fold relative increase of AUC to the adult level after day 3.


## Page 13


13 
 
Figures 
 
Figure 1


## Page 14


14 
 
 
Figure 2


## Page 15


15 
 
 
Figure 3


## Page 16


16 
 
 
Figure 4


## Page 17


17 
 
 
Figure 5


## Page 18


18 
 
 
Figure 6


## Page 19


19 
 
Bibliography 
1 
Attard, C., van der Straaten, T., Karlaftis, V., Monagle, P. & Ignjatovic, V. Developmental hemostasis: age-
specific differences in the levels of hemostatic proteins. J Thromb Haemost 11, 1850-1854, doi:Doi 
10.1111/Jth.12372 (2013). 
2 
Andrew, M., Paes, B. & Johnston, M. Development of the Hemostatic System in the Neonate and Young 
Infant. The American journal of pediatric hematology/oncology 12, 95-104 (1990). 
3 
Andrew, M. et al. Maturation of the hemostatic system during childhood. Blood 80, 1998-2005 (1992). 
4 
Monagle, P. et al. Developmental haemostasis - Impact for clinical haemostasis laboratories. Thromb 
Haemostasis 95, 362-372, doi:Doi 10.1160/Th05-01-0047 (2006). 
5 
Hearon, J. Z. The kinetics of blood coagulation. Bulletin of Mathematical Biophysics 10, 175-186, 
doi:10.1007/BF02477491 (1948). 
6 
Levine, S. N. Enzyme Amplifier Kinetics. Science 152, 651-&, doi:Doi 10.1126/Science.152.3722.651 (1966). 
7 
Jesty, J., Beltrami, E. & Willems, G. Mathematical-Analysis of a Proteolytic Positive-Feedback Loop - 
Dependence of Lag Time and Enzyme Yields on the Initial Conditions and Kinetic-Parameters. Biochemistry-
Us 32, 6266-6274, doi:Doi 10.1021/Bi00075a021 (1993). 
8 
Beltrami, E. & Jesty, J. Mathematical-Analysis of Activation Thresholds in Enzyme-Catalyzed Positive 
Feedbacks - Application to the Feedbacks of Blood-Coagulation. P Natl Acad Sci USA 92, 8744-8748, doi:Doi 
10.1073/Pnas.92.19.8744 (1995). 
9 
Hockin, M. F., Jones, K. C., Everse, S. J. & Mann, K. G. A model for the stoichiometric regulation of blood 
coagulation. J Biol Chem 277, 18322-18333, doi:Doi 10.1074/Jbc.M201173200 (2002). 
10 
Wajima, T., Isbister, G. K. & Duffull, S. B. A Comprehensive Model for the Humoral Coagulation Network in 
Humans. Clinical Pharmacology & Therapeutics 86, 290-298 (2009). 
11 
Burghaus, R. et al. Evaluation of the Efficacy and Safety of Rivaroxaban Using a Computer Model for Blood 
Coagulation. PLoS ONE 6, e17626, doi:10.1371/journal.pone.0017626 (2011). 
12 
Siegmund, H.-U., Burghaus, R., Kubitza, D. & Coboeken, K. Contribution of rivaroxaban to the international 
normalized ratio when switching to warfarin for anticoagulation as determined by simulation studies. 
British Journal of Clinical Pharmacology 79, 959-966, doi:10.1111/bcp.12571 (2015). 
13 
Mitrophanov, A. Y., Rosendaal, F. R. & Reifman, J. Mechanistic Modeling of the Effects of Acidosis on 
Thrombin Generation. Anesthesia & Analgesia 121, 278-288, doi:10.1213/ane.0000000000000733 (2015). 
14 
Danforth, C. M., Orfeo, T., Mann, K. G., Brummel-Ziedins, K. E. & Everse, S. J. The impact of uncertainty in a 
blood coagulation model. Mathematical medicine and biology : a journal of the IMA 26, 323-336, 
doi:10.1093/imammb/dqp011 (2009). 
15 
Danforth, C. M., Orfeo, T., Everse, S. J., Mann, K. G. & Brummel-Ziedins, K. E. Defining the boundaries of 
normal thrombin generation: investigations into hemostasis. PLoS One 7, e30385, 
doi:10.1371/journal.pone.0030385 (2012). 
16 
Dunster, J. L. & King, J. R. Mathematical modelling of thrombin generation: asymptotic analysis and 
pathway characterization. IMA Journal of Applied Mathematics 82, 60-96, doi:10.1093/imamat/hxw007 
(2017). 
17 
Willems, G. M., Lindhout, T., Hermens, W. T. & Hemker, H. C. Simulation model for thrombin generation in 
plasma. Haemostasis 21, 197-207 (1991). 
18 
Duchemin, J., Pan-Petesch, B., Arnaud, B., Blouch, M. T. & Abgrall, J. F. Influence of coagulation factors and 
tissue factor concentration on the thrombin generation test in plasma. Thromb Haemost 99, 767-773, 
doi:10.1160/th07-09-0581 (2008). 
19 
Andrew, M. et al. Development of the human coagulation system in the healthy premature infant. Blood 
72, 1651-1657 (1988). 
20 
Kremers, R. M. et al. Low paediatric thrombin generation is caused by an attenuation of prothrombin 
conversion. Thromb Haemost 115, 1090-1100, doi:10.1160/th15-09-0716 (2016). 
21 
Cito, S., Mazzeo, M. D. & Badimon, L. A review of macroscopic thrombus modeling methods. Thrombosis 
Research 131, 116-124 (2013). 
22 
Ambrosi, D., Quarteroni, A. & Rozza, G. Modelling of Physiological Flows. Vol. 5 (Springer, 2012). 
23 
Galassi, M. et al. GNU Scientific Library Reference Manual. 3 edn,  (Network Theory Limited, 2009). 
24 
Team, R. C. R: A language and environment for statistical computing. R Foundation for Statistical 
Computing (2016). <http://www.R-project.org/>.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
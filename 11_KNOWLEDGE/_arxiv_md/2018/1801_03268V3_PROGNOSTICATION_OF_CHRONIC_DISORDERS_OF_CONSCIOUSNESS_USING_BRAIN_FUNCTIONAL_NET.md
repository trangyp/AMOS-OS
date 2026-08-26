---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.03268v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1801.03268v3_Prognostication_of_chronic_disorders_of_consciousness_using_brain_functional_net

> Source: 1801.03268v3_Prognostication_of_chronic_disorders_of_consciousness_using_brain_functional_net.pdf

> Pages: 102

---


## Page 1


1 / 102 
 
Prognostication of chronic disorders of consciousness using brain 
functional networks and clinical characteristics 
Ming Song1,2*, Yi Yang3*, Jianghong He3, Zhengyi Yang1,2, Shan Yu1,2, Qiuyou Xie4, 
Xiaoyu Xia3, Yuanyuan Dang3, Qiang Zhang3, Xinhuai Wu5, Yue Cui1,2, Bing Hou1,2, 
Ronghao Yu4, Ruxiang Xu3, Tianzi Jiang1,2,6,7,8 
1National Laboratory of Pattern Recognition, Institute of Automation, The Chinese 
Academy of Sciences, Beijing 100190, China 
2Brainnetome Center, Institute of Automation, The Chinese Academy of Sciences, 
Beijing 100190, China 
3Department of Neurosurgery, PLA Army General Hospital, Beijing 100700, China 
4Centre for Hyperbaric Oxygen and Neurorehabilitation, Guangzhou General Hospital 
of Guangzhou Military Command, Guangzhou 510010, China 
5Department of Radiology, PLA Army General Hospital, Beijing 100700, China 
6CAS Center for Excellence in Brain Science and Intelligence Technology, Chinese 
Academy of Sciences, Beijing 100190, China 
7Key Laboratory for Neuroinformation of the Ministry of Education, School of Life 
Science and Technology, University of Electronic Science and Technology of China, 
Chengdu 625014, China 
8The Queensland Brain Institute, University of Queensland, Brisbane, QLD 4072, 
Australia 
 
*These authors contributed equally to this work.


## Page 2


2 / 102 
 
To whom correspondence should be addressed:  
Tianzi Jiang 
National Laboratory of Pattern Recognition 
Institute of Automation 
Chinese Academy of Sciences 
Beijing 100190, China  
Phone: +86 10 8254 4778 
Fax: +86 10 8254 4778 
Email: jiangtz@nlpr.ia.ac.cn 
 
And 
Ruxiang Xu 
Department of Neurosurgery 
PLA Army General Hospital 
Beijing 100700, China 
Phone: +86 10 6403 0762 
Fax: +86 10 6403 0762 
E-mail: zjxuruxiang@163.com 
 
Running title: 
Multidomain prognostic model for DOC


## Page 3


3 / 102 
 
Abstract 
Disorders of consciousness are a heterogeneous mixture of different diseases or 
injuries. Although some indicators and models have been proposed for 
prognostication, any single method when used alone carries a high risk of false 
prediction. This study aimed to develop a multidomain prognostic model that 
combines resting state functional MRI with three clinical characteristics to predict one 
year outcomes at the single-subject level. The model discriminated between patients 
who would later recover consciousness and those who would not with an accuracy of 
around 88% on three datasets from two medical centers. It was also able to identify 
the prognostic importance of different predictors, including brain functions and 
clinical characteristics. To our knowledge, this is the first reported implementation of 
a multidomain prognostic model based on resting state functional MRI and clinical 
characteristics in chronic disorders of consciousness, which we suggest is accurate, 
robust, and interpretable.


## Page 4


4 / 102 
 
Keywords: disorders of consciousness; prognosis; resting state fMRI; functional 
connectivity; brain network 
Abbreviations: CRS-R = Coma Recovery Scale-Revised; DOC = disorders of 
consciousness; GOS = Glasgow Outcome Scale; MCS = minimally conscious state; 
PLSR = partial least square regression; UWS = unresponsive wakefulness syndrome; 
VS = vegetative state


## Page 5


5 / 102 
 
Introduction 
Severe brain injury can lead to disorders of consciousness (DOC). Some patients 
recover consciousness from an acute brain insult, whereas others tragically fall into 
chronic DOC. The latter cannot communicate functionally or behave purposefully. 
Most patients remain bedridden, and require laborious care. The medical community is 
often confronted with expectations of the chronic DOC patients' families. The social, 
economic, and ethical consequences are also tremendous (Bernat, 2006). In parallel, 
although more validations are required, recent pilot studies have proposed new 
therapeutic interventions, which challenge the existing practice of early treatment 
discontinuation for a chronic DOC patient (Schiff et al., 2007; Corazzol et al., 2017; 
Yu et al., 2017). However, before using these novel therapeutic interventions, 
clinicians first need to determine if the patient is a suitable candidate. The availability 
of an accurate and robust prognostication is therefore a fundamental concern in the 
response to chronic DOC patients, as medical treatment, rehabilitation therapy and 
even ethical decisions depend on this information .  
To date, the prognostication for a DOC patient is based on physician observation of 
the patient's behavior over a sufficient period of time to discover whether there is any 
evidence of awareness. On the one hand, a patient's motor impairment, sensory deficit, 
cognitive damage, fluctuation of vigilance and medical complications could give rise 
to misjudgments; on the other hand, for the assessor, a lack of knowledge regarding 
DOC, poor training and non-use of adequate behavioral scales are additional elements 
that may contribute to a high possibility of mistakes. Consequently, careful and


## Page 6


6 / 102 
 
repeated behavioral assessments are considered to be particularly important for a 
precise diagnostic and prognostic judgment (Wannez et al., 2017). However, 
behavioral assessments are inevitably subjective and vulnerable to a variety of personal 
interferences (Giacino et al., 2009). Physicians and scientists have therefore been 
seeking accurate and objective markers for diagnosis and prognosis (Demertzi et al., 
2017; Noirhomme et al., 2017). 
Several pioneering studies suggested that the etiology, incidence age and duration 
of DOC were important indicators for prognosis (The Multi-Society Task Force on 
PVS, 1994). Specifically, patients with non-traumatic brain injury were expected to 
have a worse functional recovery than traumatic brain injury patients, and young 
patients were considered more likely to have a favorable outcome than older ones. 
During the past decades, some pilot prognostic models have also been explored based 
on features of neurological examination (Zandbergen et al., 1998; Booth et al., 2004; 
Dolce et al., 2008), abnormalities detected with EEG and evoked potentials 
(Steppacher et al., 2013; Kang et al., 2014; Hofmeijer and van Putten, 2016; Chennu et 
al., 2017), anatomical and functional changes identified with brain CT, PET and MRI 
(Maas et al., 2007; Sidaros et al., 2008; Galanaud et al., 2012; Luyt et al., 2012; 
Stender et al., 2014; Wu et al., 2015), and physiological and biochemical disturbances 
at both the brain and body levels (Kaneko et al., 2009; Rundgren et al., 2009). 
However, despite many efforts, identifying efficient biomarkers for the early 
prediction of outcome is still challenging and requires additional research. One of the 
reasons for this is that the DOC could have many different causes and be associated


## Page 7


7 / 102 
 
with several neuropathological processes and different severities, such that any method 
when used alone carries the risk of false prediction (Bernat, 2016; Rossetti et al., 
2016).  
Recently, resting state functional MRI (fMRI) has been widely used to investigate 
the brain functions of DOC patients. Research suggests that these patients demonstrate 
multiple changes in brain functional networks, including the default mode 
(Vanhaudenhuyse et al., 2010; Silva et al., 2015), executive control (Demertzi et al., 
2014b; Wu et al., 2015), salience (Qin et al., 2015; Fischer et al., 2016), sensorimotor 
(Yao et al., 2015), auditory (Demertzi et al., 2015), visual (Demertzi et al., 2014a) and 
subcortical networks (He et al., 2015). The within-network and between-network 
functional connectivity appeared to be useful indicators of functional brain damage and 
the likelihood of consciousness recovery (Silva et al., 2015; Di Perri et al., 2016). 
Taken together, these studies suggest that the brain networks and functional 
connectivity detected with resting state fMRI could be valuable biomarkers to trace the 
level of consciousness and predict the possibility of recovery. 
With advances in medicine, prognostication of a DOC patient has moved towards a 
multidomain paradigm that combines clinical examination with the application of 
novel technologies (Gosseries et al., 2014). Multidomain assessment has the potential 
to improve prediction accuracy. More importantly, it can provide reassurances about 
the importance of each predictor for prognostication by offering concordant evidence 
(Stevens and Sutter, 2013; Rossetti et al., 2016). More than twenty years ago, the 
Multi-Society Task Force on PVS suggested that the etiology, incidence age and


## Page 8


8 / 102 
 
duration of DOC could help to predict the outcome (The Multi-Society Task Force on 
PVS, 1994), and numerous studies have subsequently validated the clinical utility of 
these features (Jennett, 2005; Bruno et al., 2012; Estraneo et al., 2013; Celesia, 2016). 
Therefore, it is possible that a multidomain model that combines these clinical 
characteristics and resting state fMRI could improve prognostic predictions at an 
individual level and lead to the early identification of patients who could recover 
consciousness. 
The present work had two major objectives. The first aim was to develop an 
approach to predict the prognosis of an individual DOC patient using clinical 
characteristics and resting state fMRI. The second aim, building on the first, was to 
further explore different prognostic effects of these clinical and brain imaging features. 
Materials and methods 
The study paradigm is illustrated in Figure 1. Resting state fMRI and clinical data 
from DOC patients were collected at the so-called T0 time point when the patients' 
vital signs and conscious level had stabilized and a diagnosis had been made. 
Outcomes were assessed at least 12 months after this T0 time point; this is referred to 
as the T1 time point. The principal scales included the Coma Recovery Scale Revised 
(CRS-R) and the Glasgow Outcome Scale (GOS). Instead of predicting diagnosis, this 
study used the outcome as a target for regression and classification. Using the resting 
state fMRI and clinical data at the T0 time point in a training dataset, a regression 
model was first developed to fit each patient's CRS-R score at the T1 time point, after 
which the optimal cut-off value for classifying individual patients based on


## Page 9


9 / 102 
 
consciousness recovery was calculated. In this way, we set up the prognostic 
regression and classification model. Two independent testing datasets were then used 
to validate the model.  
Subjects 
This study involved three datasets. The datasets referred to as "Beijing 750" and 
"Beijing HDxt" were both collected in the PLA Army General Hospital in Beijing, 
and the same medical group diagnosed and managed the patients. However, the MRI 
scanners and imaging acquiring protocols were different; the "Beijing HDxt" cohort 
was scanned with a GE signa HDxt 3.0T scanner between May 2012 and December 
2013, whereas the "Beijing 750" cohort was scanned with a GE Discovery MR750 
3.0T scanner between January 2014 and May 2016. The dataset referred to as 
"Guangzhou HDxt" was collected from the Guangzhou General Hospital of 
Guangzhou Military Command in Guangzhou, and the MRI data were obtained with a 
GE signa HDxt 3.0T scanner between April 2011 and December 2014.  
The inclusion criterion was that the patients should be at least 1 month after the 
acute brain insult so that they met the DOC diagnosis. Patients were excluded when 
there was an unstable level of consciousness (continuous improvement or decline 
within the two weeks before the T0 time point), uncertain clinical diagnosis 
(ambiguity or disagreement between examiners), contraindication for MRI or large 
focal brain damage (>30% of total brain volume).  
One hundred and sixty DOC patients were initially enrolled in this study. Eleven 
patients were excluded due to large local brain lesions or movement artifacts during


## Page 10


10 / 102 
 
MRI scanning. Nine patients died during the period of the follow-up, 16 patients were 
lost to follow-up, and in 12 cases no definite outcome information was collected at the 
12-month endpoint of the follow-up. Thus, according to the inclusion and exclusion 
criteria and the follow-up results, the "Beijing 750" dataset included 46 vegetative 
state/ unresponsive wakefulness syndrome (VS/UWS) patients and 17 minimally 
conscious state (MCS) patients. The "Beijing HDxt" dataset contained 20 VS/UWS 
patients and 5 MCS patients, and the "Guangzhou HDxt" dataset contained 16 
VS/UWS patients and 8 MCS patients.  
The demographic and clinical characteristics of the patients are summarized in 
Table 1, with additional details provided in Appendix 1-table 1, 2, 3. The "Beijing 
750" dataset also included 30 healthy participants, and the "Beijing HDxt" dataset 
included 10 healthy participants. All of the healthy participants were free of 
psychiatric or neurological history. These healthy participants are referred to as 
"normal controls". See Appendix 1 -table 4, 5 for details. 
As the "Beijing 750" dataset involved more patients than the other two datasets, it 
was used as the training dataset for model development and internal validation, 
whereas the "Beijing HDxt" and "Guangzhou HDxt" datasets were only used for 
external validation. The study was approved by the Ethics Committee of the PLA 
Army General Hospital (protocol No: 2011-097) and the Ethics Committee of the 
Guangzhou General Hospital of Guangzhou Military Command (protocol No: 
jz20091287). Informed consent to participate in the study was obtained from the legal 
surrogates of the patients and from the normal controls.


## Page 11


11 / 102 
 
Clinical measurements 
Diagnosis and consciousness assessments 
The diagnosis of each patient in the three datasets was made by experienced 
physicians according to the CRS-R scale (The Multi-Society Task Force on PVS, 
1994; Bernat, 2006; Magrassi et al., 2016). In the "Beijing 750" and "Beijing HDxt" 
datasets, the patients underwent the evaluations at least twice weekly within the two 
weeks before the MRI scanning (i.e. the T0 time point). The highest CRS-R score was 
considered as the diagnosis. The CRS-R includes six subscales that address auditory, 
visual, motor, oromotor, communication, and arousal functions, which are summed to 
yield a total score ranging from 0 to 23.  
Outcome assessments 
All patients were followed up at least 12 months after MRI scanning, according to 
the protocols for DOC described in a number of previous studies (Galanaud et al., 
2012; Luyt et al., 2012; Stender et al., 2014; Pignat et al., 2016). Basically, follow-up 
interviews were performed in four ways, including outpatient visit, assessments by 
local physicians, home visit, and telephone/video review. Whenever possible signs of 
responsiveness were detected or reported, the patient was evaluated either at the unit 
or at home by the hospital staff. In cases where no change was signaled, patients were 
examined twice by one hospital physician via telephone/video reviews at the end of 
the follow-up process.  
For the training dataset "Beijing 750", two outcome scales were assessed: the 
GOS and CRS-R. The GOS is one of the most commonly reported global scales for


## Page 12


12 / 102 
 
functional outcome in neurology, and provides a measurement of outcome ranging 
from 1 to 5 (1, dead; 2, vegetative state/minimally conscious state; 3, able to follow 
commands/unable to live independently; 4, able to live independently/unable to return 
to work or school; 5, good recovery/able to return to work or school). Although 
simple to use and highly reliable, the GOS score cannot provide detailed information 
about individual differences in consciousness level for DOC patients. In contrast, the 
CRS-R score can assist with prognostic assessment in DOC patients (Giacino and 
Kalmar, 2006). The six subscales in the CRS-R comprise hierarchically-arranged 
items associated with brain stem, subcortical and cortical processes. The lowest item 
on each subscale represents reflexive activity, whereas the highest items represent 
cognitively-mediated behaviors. In order to simplify modeling, we hypothesized that 
the higher the total CRS-R score at the follow up, the better the outcome for the 
patient. We developed a regression model to fit each patient's CRS-R score at the T1 
time point based on their clinical characteristics and resting state fMRI data, and 
designed a classification model to predict consciousness recovery or not for each 
patient. The classification accuracy was assessed by comparing the predicted label 
and the actual GOS score, i.e. "consciousness recovery" (GOS≥3) versus 
"consciousness non-recovery" (GOS≤2). 
The testing dataset "Beijing HDxt" involved both the GOS scores and the CRS-R 
scores at the T1 time point for each patient. The testing dataset "Guangzhou HDxt" 
measured the GOS scores, but not the CRS-R scores at the T1 time point.


## Page 13


13 / 102 
 
MRI acquisition 
All of the participants in the three datasets were scanned with resting state fMRI 
and T1-weighted 3D high-resolution imaging. During the MRI scanning, the 
participants did not take any sedative or anesthetic drugs. The resting state fMRI scan 
was obtained using a T2*-weighted gradient echo sequence, and a high-resolution 
T1-weighted anatomical scan was obtained to check whether the patients had large 
brain distortion or focal brain damage. For the training dataset "Beijing 750", the 
resting state fMRI acquisition parameters included TR/TE=2000/30ms, flip angle=90°, 
axial 39 slices, thickness=4mm, no gap, FOV=240×240mm, matrix=64×64, and 210 
volumes (i.e., 7 minutes). For the testing dataset "Beijing HDxt", the resting state 
fMRI acquisition parameters were as follows: axial 33 slices, TR/TE=2000/30ms, flip 
angle=90°, thickness=4mm, no gap, FOV=220×220mm, matrix=64×64, and 240 
volumes (i.e., 8 minutes). For the testing dataset "Guangzhou HDxt", the resting state 
fMRI acquisition parameters included axial 35 slices, TR/TE=2000/30ms, flip 
angle=90°, thickness=4mm, no gap, FOV=240×240mm, matrix=64×64, and 240 
volumes (i.e., 8 minutes).  
Data analysis 
The data analysis pipeline is illustrated in Figure 2. 
Imaging preprocessing 
Preprocessing and connectivity calculation were performed in the same way for 
the training dataset and the two testing datasets. All resting state fMRI scans were 
preprocessed using SPM8 (SPM, RRID:SCR_007037) and in-house Matlab codes.


## Page 14


14 / 102 
 
Specifically, the first five volumes of each subject were discarded. The remaining 
resting state fMRI volumes were corrected for slice timing differences and realigned 
to the first volume to correct for inter-scan movements. The functional images were 
then spatially smoothed with a Gaussian kernel of 6×6×6 mm full-width at half 
maximum. Linear regression was used to remove the influence of head motion, whole 
brain signals and linear trends. The variables regressed out included 12 motion 
parameters (roll, pitch, yaw, translation in three dimensions and their first derivatives), 
the average series of the signals within the brain, and the regressors for linear trends. 
Motion artifact is increasingly recognized as an important potential confound in 
resting state fMRI studies. Any particular motion may produce a wide variety of 
signal changes in the fMRI data, and thus introduce complicated shifts in functional 
connectivity analysis. This problem was particularly serious for the DOC patients, as 
they were unlikely to follow the experimental instructions and control their head 
motion. To balance the demands of noise reduction and data preservation, we 
censored volumes that preceded or followed any movement (framewise displacement, 
FD) greater than 1.5 mm. The FD is a summarization of the absolute values of the 
derivatives of the translational and rotational realignment estimates (after converting 
the rotational estimates to displacement at 50 mm radius) (Power et al., 2015). The 
head motion measures were achieved in the preprocessing step of realignment using 
SPM. To obtain reliable Pearson's correlations for functional connectivity, the patients 
with less than 50 volumes worth of remaining data were excluded. More information 
about the analysis and validation of controls for motion-related artifacts are provided


## Page 15


15 / 102 
 
in Appendix 4. 
Finally, to reduce low-frequency drift and high-frequency noise, band-pass 
filtering (0.01-0.08 Hz) was only performed on volumes that survived motion 
censoring.  
Definition of networks and regions of interest  
As noted in the introduction, multiple functional brain networks are disrupted in 
DOC patients. Among these impaired networks, six (the default mode, executive 
control, salience, sensorimotor, auditory, and visual networks) show system-level 
damages and significant correlations with behavioral assessments (Demertzi et al., 
2014b; Demertzi et al., 2015). We therefore defined a total of 22 regions of interest 
(ROIs) to probe these six brain networks. The definitions of the 22 ROIs were based 
on the results of a series of previous brain functional studies (Seeley et al., 2007; 
Raichle, 2011; Demertzi et al., 2015), and their names and Montreal Neurological 
Institute (MNI) coordinates are listed in Appendix 2.  
The connection templates of the six brain networks were first investigated within 
the normal control group. In addition to the above-mentioned preprocessing stages, 
the resting state fMRI scans of the normal controls in the training dataset were 
transformed into MNI standard space. For each of the six networks, time series from 
the voxels contained in the various ROIs were extracted and averaged together. The 
averaged time series were then used to estimate whole-brain correlation r maps that 
were subsequently converted to normally distributed Fisher’s z-transformed 
correlation maps. Group functional connectivity maps for each of the six networks


## Page 16


16 / 102 
 
were then created with a one-sample t test (see Appendix 3 for details). Notably, the T 
map included both positive and negative values. We used the six T maps as the brain 
connection templates of the corresponding brain networks in the healthy population, 
which would assist to define one type of imaging features, i.e. the connection feature 
of the ROI. More information about the connection features of the ROIs are provided 
in the following section. 
The conventional fMRI preprocess normalizes individual fMRI images into a 
standard space defined by a specific template image. Our goal was to extend this 
conventional approach to generate a functional connectivity image for each patient in 
his/her own imaging space. During the preprocessing of each patient’s fMRI scans, 
the 22 ROIs and six brain connection templates were therefore spatially warped to 
individual fMRI space and resampled to the voxel size of the individual fMRI image. 
We also developed tools to visually check the registration for each subject, some 
examples of which are provided in Appendix 5 and Supplementary file 1. 
Calculation of imaging features 
We designed two types of imaging features from the resting state fMRI, one being 
the functional connectivity between each pair of 22 ROIs, and the other being the 
spatial resemblance between the functional connection patterns of each ROI and the 
brain connection templates across the whole brain. The functional connectivity was 
based on the Pearson’s correlation coefficients, while the spatial resemblance was 
conceptually similar to the template-matching procedure (Greicius et al., 2004; Seeley 
et al., 2007; Vanhaudenhuyse et al., 2010).The basis of template matching is that the


## Page 17


17 / 102 
 
more spatial consistency which exists between the template of a brain network and a 
specific connectivity map (for example, a component in an independent component 
analysis), the stronger the possibility that the connectivity map belongs to that brain 
network. Here, for each ROI of an individual DOC patient, we first computed the 
Pearson’s correlation coefficients between the time-course of the ROI and that of each 
voxel within the brain so as to obtain a functional connectivity map, and subsequently 
converted the functional connectivity map to a normally distributed Fisher’s z 
transformed correlation map. Next, we calculated the Pearson’s correlation 
coefficients between the Fisher’s z transformed correlation map and the 
corresponding brain connection template wrapped to individual fMRI space across 
each voxel within the brain. A greater correlation coefficient between the two maps 
suggests that there is more spatial resemblance between the functional connectivity 
map of the ROI and the normal brain connection template. Our assumption was that 
the more spatial consistency that existed between the connectivity map of the ROI in a 
DOC patient and the brain connection template, the more intact the corresponding 
brain function of the ROI in this individual. In this way, we defined the connection 
feature of the ROI with the spatial resemblance.  
Overall, for each participant in this study, there were 231 (22×21/2) functional 
connectivity features and 22 brain area connection features. 
Imaging feature selection 
Feature selection techniques have been widely adopted in brain analysis studies, in 
order to produce a small number of features for efficient classification or regression,


## Page 18


18 / 102 
 
and to reduce overfitting and increase the generalization performance of the model 
(Fan et al., 2007; Dosenbach et al., 2010; Drysdale et al., 2016). Feature ranking and 
feature subset selection are two typical feature selection methods (Guyon and 
Elisseeff, 2003). Feature subset selection methods are generally time consuming, and 
even inapplicable when the number of features is extremely large, whereas 
ranking-based feature selection methods are subject to local optima. Therefore, these 
two feature selection methods are usually used jointly. Here, we first used a 
correlation-based feature selection technique to select an initial set of features, and 
then adopted a feature subset selection method for further selection.  
As a univariate method, correlation-based feature selection is simple to run and 
understand, and measures the linear correlation between each feature and the response 
variable. Here, the image features (i.e., functional connectivity features and brain area 
connection features) which significantly correlated to the CRS-R scores at the T1 time 
point across the DOC patients in the training dataset were retained for further 
analysis.  
Competitive adaptive reweighted sampling coupled with partial least squares 
regression (CARS-PLSR, http://libpls.net/) was then used for further feature subset 
selection (Li et al., 2009; Li et al., 2014). Briefly, CARS-PLSR is a sampling-based 
feature selection method that selects the key informative variables by optimizing the 
model's performance. As it provides the influence of each variable without 
considering the influence of the remainder of the variables, CARS-PLSR is efficient 
and fast for feature selection (Mehmood et al., 2012), and has therefore been used to


## Page 19


19 / 102 
 
explore possible biomarkers in medicine (Tan et al., 2010) and for wavelength 
selection in chemistry (Fan et al., 2011). Using CARS-PLSR, we selected a subset of 
key informative imaging features. 
Notably, both the correlation-based and CARS-PLSR feature selection methods 
filtered the features from the original feature set without any transformations. This 
made the prognostic regression model easier to interpret, as the imaging predictors 
were associated with either brain regions or functional connectivity. 
Prognostic modeling and assessments of predictor importance 
PLSR is able to handle multicollinearity among the predictors well (Wold et al., 
2001; Krishnan et al., 2011). It was therefore used to generate the prognostic 
regression model in the training dataset "Beijing 750". Given that clinical 
characteristics, including the etiology, incidence age and duration of DOC, have been 
verified as useful prognostic indicators, we designated the selected imaging features 
and the three clinical characteristics at the T0 time point as independent co-variates 
and the CRS-R score at the T1 time point as the dependent variable. Among the three 
clinical characteristics, the incidence age and duration of DOC were quantitative 
variables, whereas the etiology was a qualitative variable. In accordance with a 
previous study (Estraneo et al., 2010), we categorized the etiology into three types, 
including traumatic brain injury, stroke and anoxic brain injury. Thus, two dummy 
variables for etiology were designed and included in the model. Prior to model 
training, all involved predictors were centered and normalized (i.e., transformed into 
Z-scores). The prognostic regression model therefore took the imaging and clinical


## Page 20


20 / 102 
 
features as input and returned a predicted score as output. In the training dataset 
"Beijing 750", we used cross-validation to decide that the number of latent variables 
for PLSR was three. To evaluate the regression model, the coefficient of 
determination R2 between the predicted scores and the CRS-R scores at the T1 time 
point was calculated, and the Bland-Altman plot was used to measure the agreement 
between them.  
Next, receiver operating characteristic (ROC) curves were plotted for the 
predicted scores. The optimal cut-off value for classifying an individual patient as 
having recovered consciousness or not was appointed to the point with the maximal 
sum of true positive and false negative rates on the ROC curve. Individual patients 
were classified as exhibiting recovery of consciousness if their predicted scores were 
higher than or equal to the cut-off value, otherwise as consciousness non-recovery .  
The classification accuracy was calculated by comparing the predicted label and the 
actual GOS score, i.e. "consciousness recovery" (GOS≥3) versus "consciousness 
non-recovery" (GOS≤2). 
As model interpretation is an important task in most applications of PLSR, there 
has been considerable progress in the search for optimal interpretation methods 
(Kvalheim and Karstang, 1989; Kvalheim et al., 2014). In this study, using the 
Significant Multivariate Correlation (sMC) method (Tran et al., 2014), we assessed 
predictor importance in the prognostic regression model. The key points in sMC are to 
estimate for each predictor the correct sources of variability resulting from PLSR (i.e. 
regression variance and residual variance), and use them to statistically determine a


## Page 21


21 / 102 
 
variable's importance with respect to the regression model. The F-test values (termed 
the sMC F-values) were used to evaluate the predictors' importance in the prognostic 
regression model. 
Internal validation of model 
The prognostic regression model was internally validated using bootstrap 
(Steyerberg, 2008). Specifically, bootstrap samples were drawn with replacement 
from the training dataset "Beijing 750" such that each bootstrap sampling set had a 
number of observations equal to that of the training dataset. Using a bootstrap 
sampling set, correlation-based feature selection and CARS-PLSR were first used to 
select the feature subset, after which the PLSR was used to generate a prognostic 
model. We then applied the model to the bootstrap sampling set and the original 
training dataset, and calculated the coefficient of determination R2 of each of the two 
datasets. The difference between the two coefficients of determination was defined as 
the optimism. This process was repeated 1000 times to obtain a stable estimate of the 
optimism. Finally, we subtracted the optimism estimate from the coefficient of 
determination R2 of the "Beijing 750" training dataset to obtain the 
optimism-corrected performance estimate. 
In addition, out-of-bag (OOB) estimation was used as an estimate of model 
classification performance in the training dataset (James et al., 2013). Specifically, for 
the original training dataset x, we left out one sample at a time and denoted the 
resulting sets by x(-1),..., x(-n). From each leave-one-out set x(-i), 1000 bootstrap learning 
sets of size n-1 were drawn. On every bootstrap learning set generated from x(-i), we


## Page 22


22 / 102 
 
carried out feature selection, built a PLSR regression and classification model, and 
applied the model to the test observation xi. A majority vote was then made to give a 
class prediction for observation xi. Finally, we calculated the accuracy for the whole 
training dataset x.  
External validation of model 
External validation is essential to support the general applicability of a prediction 
model. We ensured external validity by testing the model in two testing datasets, 
neither of which included samples that were considered during the development of the 
model. First, using the prognostic regression model, we calculated one predicted score 
for each patient in the two testing datasets. As the "Beijing HDxt" dataset assessed the 
patients' CRS-R scores at the T1 time point, we calculated the coefficient of 
determination R2 between the predicted scores and the patients' CRS-R scores at this 
time point. The Bland-Altman plot was also determined. Finally, the patients in the 
two testing datasets were assessed as achieving consciousness recovery or not based 
on the cut-off threshold obtained using the training dataset. The performance of the 
classification, including the accuracy, sensitivity and specificity, was determined.  
Comparison between single-domain model and combination model 
Using the same modeling and validation method as described above, we examined 
predictability and generalizability in the two testing datasets based on the clinical 
features alone or the imaging features alone.  
In addition, to compare the two types of single-domain models and the 
combination model, we used bootstrap resampling to obtain the distribution of the


## Page 23


23 / 102 
 
prediction accuracies in the two testing datasets based on each of the three types of 
models. We first resampled with replacement from the training dataset, and built a 
regression and classification model based on the clinical features alone, the 
neuroimaging features alone, or the combination of the two-domain features. We then 
tested the classification accuracy in the two testing datasets using the three types of 
models. In this way, we obtained the distribution of the prediction accuracies using 
each of the three types of models. Next, we used repeated measures ANOVA to 
determine whether or not the performances of the three types of models were the same, 
as well as Ψ, the root-mean-square standardized effect, to report the effect sizes of the 
mean differences between them. 
Comparison between the proposed modeling method and linear SVM 
We compared the prediction performances between the proposed modeling 
method and linear SVM. The code for SVM was downloaded from LIBSVM 
(LIBSVM, RRID:SCR_010243). The 253 imaging features and the four clinical 
features were integrated into one feature vector. No feature selection was adopted in 
the linear SVM-based classification. The patients with GOS≥3 were labeled as 1, with 
the others being designated as -1 (i.e., GOS ≤2).  
Similarly, the OOB estimation process was used to estimate the performance of 
linear SVM in the training dataset "Beijing 750". Next, using all the samples in the 
training dataset "Beijing 750", we trained a linear SVM-based classifier and then 
tested the predictive accuracy in the two testing datasets.


## Page 24


24 / 102 
 
RESULTS 
Imaging feature selection 
Correlation-based feature selection 
Using the training dataset, we found that some imaging features significantly 
correlated to the CRS-R scores at the T1 time point. For example, the connection 
features of some brain areas, including the anterior medial prefrontal cortex (aMPFC), 
posterior cingulate cortex/precuneus (PCC) and right lateral parietal cortex in the 
default mode network, and the dorsal medial prefrontal cortex (DMPFC) and left 
lateral superior parietal cortex in the executive control network, displayed significant 
correlations to the CRS-R T1 scores across the DOC patients. We also found 
numerous examples of significant correlation between functional connectivity and the 
CRS-R score at the T1 time point, with these functional connectivities being 
distributed both within and between brain networks. More information about the 
correlations between the imaging features and the CRS-R scores at the T1 time point 
are provided in Appendix 6.  
CARS-PLSR feature selection 
Figure 3 shows the final imaging features selected with CARS-PLSR. Specifically, 
the brain area connection features included the aMPFC and PCC in the default mode 
network, and the DMPFC in the executive control network. The functional 
connectivity features included the connectivity between the aMPFC in the default 
mode network and the DMPFC in the executive control network, as well as between 
the middle cingulate cortex in the auditory network and the right lateral primary


## Page 25


25 / 102 
 
visual cortex in the visual network. More information about the feature selection by 
bootstrap is provided in Appendix 7. 
Prognostic regression model and predictor importance 
The prognostic regression model is presented in Figure 4. Based on the regression 
formula, we noted some interesting findings. First, there were both positive and 
negative weights. In particular, the weights were all positive for the three brain area 
connection features, whereas the weight for the functional connectivity feature 
between the aMPFC in the default mode network and the DMPFC in the executive 
control network was negative. Interestingly, this connection had the maximum sMC 
F-value as shown in Figure 4B. In addition, the age and the anoxic etiology had 
negative weights, and the age predictor had the largest sMC F-value among the four 
clinical features. 
Prognostic classification model and internal validation 
Figure 5A presents the predicted score for each patient in the training dataset. As 
shown in Figure 5B, there was good agreement between the CRS-R scores at the T1 
time point and the predicted scores. The apparent coefficient of determination R2 was 
equal to 0.65 (permutation test, p=0.001), and the Bland-Altman plot verified the 
consistency between the predicted and achieved scores (one sample T test, p=1.0). 
The prognostic regression model was internally validated using bootstrap. The 
optimism-corrected coefficient of determination R2 was equal to 0.28.  
Figure 5C illustrates the number and proportion of DOC patients in different 
bands of predicted scores. We found that the proportion of the patients with a


## Page 26


26 / 102 
 
“consciousness recovery” outcome in the patient cohorts rose in conjunction with an 
increase in the predicted score. The higher the predicted score, the higher the 
proportion of patients who exhibited a favorable outcome. Figure 5D shows the area 
under the ROC curve (AUC=0.96, 95% CI=0.89-0.99). Based on the ROC curve for 
the training dataset, the threshold 13.9 was selected as the cut-off point to classify the 
recovery of individual patients. In other words, if the predicted score for a patient was 
equal to or larger than 13.9, the classification model designated the label 
"consciousness recovery" for this patient, otherwise "consciousness non-recovery". 
The classification accuracy was assessed by comparing the predicted and actual 
outcomes, i.e. "consciousness recovery" (GOS≥3) versus " consciousness 
non-recovery" (GOS≤2). Using this method, the classification accuracy in the training 
dataset was up to 92%. Specifically, the sensitivity was 85%, the specificity was 94%, 
the positive predictive value (PPV) was 79%, the negative predictive value (NPV) 
was 96%, and the F1 score was 0.81. 
The OOB was able to provide the mean prediction error on each training sample 
and estimate the generalizability of our method in the training dataset. Using the OOB 
estimation, we found that the prediction accuracy in the training dataset "Beijing 750" 
was 89%, and the sensitivity, specificity, PPV and NPV were 69%, 94%, 100%, and 
87%, respectively. 
Model external validation 
The performance of the prediction model on the two testing datasets is illustrated 
in Figure 6. As we assessed the CRS-R scores at the T1 time point for the patients in


## Page 27


27 / 102 
 
the "Beijing HDxt" dataset, we calculated the coefficient of determination R2 between 
these scores and the predicted scores. The R2 was equal to 0.35 (permutation test, 
p=0.005), with the Bland-Altman plot verifying the consistency between the predicted 
and actual scores (one sample T test, p=0.89). Using the predicted score 13.9 as the 
threshold, we then tested the classification accuracy on the two testing datasets. We 
found that, for the "Beijing HDxt" dataset, the prediction accuracy was up to 88% 
(sensitivity: 83%, specificity: 92%, PPV: 92%, NPV:86%, F1 score:0.87; permutation 
test, p<0.001), while for the "Guangzhou HDxt" dataset it was also up to 88% 
(sensitivity: 
100%, 
specificity:83%, 
PPV:67%, 
NPV:100%, 
F1 
score:0.80; 
permutation test, p<0.001). Notably, our model demonstrated good sensitivity and 
specificity for both the "subacute" patients (i.e. duration of unconsciousness ≤3 
months) and those in the chronic phase (i.e. duration of unconsciousness >3 months), 
as shown in Figure 7. More interestingly, for the testing dataset "Beijing HDxt", eight 
DOC patients who were initially diagnosed as VS/UWS subsequently recovered 
consciousness. Using the proposed model, we could successfully identify seven of 
these and there was only one false positive case. That is, for the VS/UWS patients, the 
model achieved 90.0% accuracy (sensitivity: 87.5%, specificity: 91.7%, PPV:87.5%, 
NPV:91.7%, F1 score:0.875).  
To test robustness, we evaluated whether the present prognostic regression model 
generalized to the healthy subjects scanned in the "Beijing 750" training dataset (n=30) 
and the "Beijing HDxt" testing dataset (n=10). We found that both the healthy subjects 
and the "consciousness recovery" patients had significantly higher predicted imaging


## Page 28


28 / 102 
 
subscores than the "consciousness non-recovery" patients (two sample T test, p<0.05). 
Additional information is provided in Appendix 8. 
Comparison of the single-domain and combination models 
When only the clinical features were used to build the predictive model, the 
prediction accuracy for the "Beijing HDxt" dataset was 68% (sensitivity: 58%, 
specificity: 77%, PPV: 70%, NPV:67%, F1 score:0.64), while for the "Guangzhou 
HDxt" dataset it was 83% (sensitivity: 100%, specificity:78%, PPV:60%, NPV:100%, 
F1 score:0.75). When only the imaging features were involved in the model, the 
prediction accuracy for the "Beijing HDxt" dataset was 80% (sensitivity: 67%, 
specificity: 92%, PPV: 89%, NPV:75%, F1 score:0.76), while for the "Guangzhou 
HDxt" dataset it was 79% (sensitivity: 100%, specificity:72%, PPV:55%, NPV:100%, 
F1 score:0.71).  
Using bootstrapping, we obtained the distribution of the prediction accuracies in 
the two testing datasets with each of the three types of models. In the "Beijing HDxt" 
testing dataset, the mean±standard deviation of the distribution of the prediction 
accuracies was 0.815±0.050, 0.811±0.044, and 0.666±0.037 for the combination 
model, the model using imaging features alone, and the model using clinical features 
alone, respectively. We found that there were significant differences between the 
means of the classification accuracies using the three types of models (repeated 
measures ANOVA, p<0.001). Subsequently, we conducted pairwise comparisons. We 
found that there was significant difference between the combination model and the 
model separately using the imaging feature alone (paired sample t-test, p=0.001) and


## Page 29


29 / 102 
 
using the clinical feature alone (paired sample t-test, p<0.001). We also found that 
there was significant difference between the model using the imaging feature alone 
and the model using the clinical feature alone (paired sample t-test, p<0.001). Using 
effect size analysis, we found that there was a mean difference of Ψ=0.004 (95% 
CI=[0.002, 0.007]) between the combination method and the method using only  
imaging features, and Ψ=0.149 (95% CI=[0.147, 0.152]) between the combination 
method and the method using only clinical features. We also observed a mean 
difference of Ψ=0.145 (95% CI=[0.142, 0.147]) between the methods using only  
imaging features and only clinical features.  
In the "Guangzhou HDxt" testing dataset, the mean±standard deviation of the 
distribution of the prediction accuracies was 0.863 ±0.051, 0.783 ± 0.044, and 
0.829±0.086 for the combination model, the model using imaging features alone, and 
the model using clinical features alone, respectively. Similarly, we found that there 
were significant differences between the mean of the classification accuracies using 
the three types of models (repeated measures ANOVA, p<0.001), and there was 
significant difference between the combination model and the models using imaging 
features alone (paired sample t-test, p<0.001) or using clinical features alone (paired 
sample t-test, p<0.001). Using effect size analysis, we found a mean difference of 
Ψ=0.080 (95% CI=[0.076, 0.084]) between the combination model and the model 
using the imaging features alone, and Ψ=0.034 (95% CI=[0.028, 0.040]) between the 
combination model and the model using only clinical features. We also observed a 
mean difference of Ψ= -0.046 (95% CI=[-0.053, -0.040]) between the model using


## Page 30


30 / 102 
 
imaging features alone and that using only clinical features. 
Therefore, in both testing datasets, the combination of imaging and clinical 
features demonstrated higher accuracy than the use of the single domain features 
alone. In addition, using the imaging features alone had higher predictive power in 
comparison to using the clinical features alone in the "Beijing HDxt" dataset, whereas 
the opposite condition was observed in the "Guangzhou HDxt" dataset, suggesting 
that the two testing datasets might be heterogeneous. More information about the 
single-domain models are provided in Supplementary file 2. 
Comparison between the proposed modeling method and linear SVM 
Using the OOB estimation, we found that the accuracy of the linear SVM-based 
classification method in the training dataset "Beijing 750" was 83% (sensitivity: 31%, 
specificity: 96%, PPV: 100%, NPV: 81%), which was lower than the accuracy of our 
proposed modeling method (i.e., accuracy: 89%, sensitivity: 69%, specificity: 94%, 
PPV: 100%, NPV: 87%). On the other hand, the linear SVM-based classification 
method achieved an accuracy of 76% (sensitivity: 58%, specificity: 92%, PPV: 88%, 
NPV: 71%) and 88% (sensitivity: 100%, specificity: 83%, PPV: 67%, NPV: 100%) in 
the "Beijing HDxt" testing dataset and the "Guangzhou HDxt" testing dataset, 
respectively. That is, the accuracy in the "Beijing HDxt" testing dataset was lower 
than that in our method, whereas the accuracy in the "Guangzhou HDxt" testing 
dataset was similar to that of our approach. Therefore, taking together the 
performance comparisons in both the training dataset and the two testing datasets, we 
believe that our method based on feature selection and PLSR should have higher


## Page 31


31 / 102 
 
prediction accuracy and better generalizability in comparison to linear SVM. 
DISCUSSION 
In this paper, we describe the development of a prognostic model that combines 
resting state fMRI with three clinical characteristics to predict one year outcomes at 
the single-subject level. The model discriminated between patients who would later 
recover consciousness and those who would not with an accuracy of around 88% on 
three datasets from two medical centers. It was also able to identify the prognostic 
importance of different predictors, including brain functions and clinical 
characteristics. To our knowledge, this is the first reported implementation of a 
multidomain prognostic model based on resting state fMRI and clinical characteristics 
in chronic DOC. We therefore suggest that this novel prognostic model is accurate, 
robust, and interpretable. For research only, we share the prognostic model and its 
Matlab code at a public download resource (https://github.com/realmsong504/pDOC). 
Brain functions are mediated by the interactions between neurons within different 
neural circuits and brain regions. Functional imaging can detect the local activity of 
different brain regions and explore the interactions between them, and has 
demonstrated potential for informing diagnosis and prognosis in DOC. On the one 
hand, many studies have focused on one modality of brain functional imaging, such as 
PET (Phillips et al., 2011), SPECT (Nayak and Mahapatra, 2011), task fMRI (Owen 
et al., 2006; Coyle et al., 2015), and resting state fMRI (Demertzi et al., 2015; Qin et 
al., 2015; Wu et al., 2015; Roquet et al., 2016). On the other hand, some 
cross-modality studies have compared the diagnostic precision between imaging


## Page 32


32 / 102 
 
modalities, for example, comparing PET imaging with task fMRI (Stender et al., 
2014), or comparing PET, EEG and resting state fMRI (Golkowski et al., 2017). In 
our study, by combining brain functional networks detected from resting state fMRI 
with three clinical characteristics, we built a computational model that allowed us to 
make predictions regarding the prognosis of DOC patients at an individual level. We 
compared the models separately using only the imaging features or only the clinical 
characteristics and found that the combination of these predictors achieved higher 
accuracy. This validated the need for the use of accumulative evidence stemming from 
multiple assessments, each of which has different sensitivity and specificity in 
detecting the capacity for recovery of consciousness (Demertzi et al., 2017). 
Validations in additional and unseen datasets were also undertaken to evaluate the 
feasibility of the predictive model. Our results showed about 88% average accuracy 
across the two testing datasets, and good sensitivity and specificity in both the 
"subacute" patients (i.e. 1 months ≤ duration of unconsciousness ≤3 months) and 
those in the prolonged phase (i.e. duration of unconsciousness >3 months), which 
suggested good robustness and the generalizability of our model. 
Further, the sensitivity of 83% and 100% obtained across the two testing datasets 
demonstrated a low false negative rate, which would avoid predicting non-recovery in 
a patient who can actually recover. Our method successfully identified 16 out of the 
total 18 patients who later recovered consciousness in the two testing datasets. In 
parallel, the specificity across the two testing datasets was up to 92% and 83%, 
respectively. Taken together, these results suggest that our method can precisely


## Page 33


33 / 102 
 
identify those patients with a high-potential for recovery consciousness and 
concurrently reduce false positives in predicting low-potential patients. In addition, 
although it has been widely considered that the prospect of a clinically meaningful 
recovery is unrealistic for prolonged DOC patients (Wijdicks and Cranford, 2005), 
our model correctly predicted 9 out of 10 DOC patients with longer than or equal to 
three months duration of DOC who subsequently recovered consciousness, including 
three patients with longer or equal to six months duration, suggesting that it can also 
be applied to prolonged DOC patients. 
According to the surviving consciousness level, DOC patients can be classified 
into distinct diagnostic entities, including VS/UWS and MCS. As MCS is often 
viewed as a state with a potentially more favorable outcome (Luaute et al., 2010), a 
misdiagnosis of VS/UWS could heavily bias the judgment of the prognosis, the 
medical treatment options and even the associated ethical decisions. Some influential 
studies have found that a few VS/UWS patients exhibit near-normal high-level 
cortical activation in response to certain stimuli or commands (Owen et al., 2006; 
Monti et al., 2010), and that late recovery of responsiveness and consciousness is not 
exceptional in patients with VS/UWS (Estraneo et al., 2010). Instead of predicting 
diagnosis, this study used one year outcome as a target for regression and 
classification. Our method based on the combined use of clinical and neuroimaging 
data successfully identified seven out of the eight VS/UWS patients in the testing 
dataset who were initially diagnosed as VS/UWS but subsequently achieved a 
promising outcome.


## Page 34


34 / 102 
 
By analyzing the sMC F-value for each predictor in the regression model, we 
investigated the prognostic effects of these predictors. In particular, the sMC F-value 
of the incidence age was greater than that of the other clinical characteristics, 
suggesting that incidence age might be the most important predictor among the 
clinical characteristics. Notably, the sMC F-value for the imaging features as a whole 
seemed to be greater than that of the clinical features, as shown in Figure 4B. We 
therefore speculate that the patient's residual consciousness capacity, indicated by 
brain networks and functional connectivity detected from resting state fMRI, might 
have a stronger prognostic effect than their clinical characteristics. 
Some previous studies have shown that the resting state functional connectivity 
within the default mode network is decreased in severely brain-damaged patients, in 
proportion to their degree of consciousness impairment, from locked-in syndrome to 
minimally conscious, vegetative and coma patients (Vanhaudenhuyse et al., 2010). 
Moreover, the reduced functional connectivity within the default mode network, 
specifically between the MPFC and the PCC, may predict the outcome of DOC 
patients (Silva et al., 2015). Our model also validates that the aMPFC and PCC in the 
default mode network play important roles in predicting prognosis.  
Above all, we found that the functional connectivity between the aMPFC and the 
DMPFC had the maximum sMC F-value in the prognostic regression model. The 
aMPFC is one of the core brain areas in the default mode network, whereas the 
DMPFC is located in the executive control network. Previous studies have 
demonstrated that this functional connectivity is negative connectivity in normal


## Page 35


35 / 102 
 
healthy populations, with the anti-correlation being proposed as one reflection of the 
intrinsic functional organization of the human brain (Fox et al., 2005). The default 
mode network directly contributes to internally generated stimulus-independent 
thoughts, self-monitoring, and baseline monitoring of the external world, while the 
executive control network supports active exploration of the external world. Correct 
communication and coordination between these two intrinsic anti-correlated networks 
is thought to be very important for optimal information integration and cognitive 
functioning (Buckner et al., 2008). A recent study reported that negative functional 
connectivities between the default mode network and the task-positive network were 
only observed in patients who recovered consciousness and healthy controls, whereas 
positive values were obtained in patients with impaired consciousness (Di Perri et al., 
2016). Further, our regression model suggests that the anti-correlations between these 
two diametrically opposed networks (i.e., default mode network and executive control 
network) should be the most crucial imaging feature for predicting the outcomes of the 
DOC patients. We therefore conclude that our prognostic model has good 
interpretability, and that it not only verifies the findings of previous studies but also 
provides a window to assess the relative significance of various predictors for the 
prognosis of DOC patients.  
This study involved two testing datasets, which were found to be quite different, as 
shown in Table 1. First, the distributions of the etiology of the patients were 
remarkably different in the two datasets. The numbers of patients suffering from 
trauma/stroke/anoxia were 12/6/7 and 8/0/16 in the "Beijing HDxt" and "Guangzhou


## Page 36


36 / 102 
 
HDxt" datasets, respectively. The outcomes were also different. In the "Beijing HDxt" 
dataset, 12 out of the total 25 patients recovered consciousness, compared with six out 
of the total 24 patients in the "Guangzhou HDxt" dataset. Given that the characteristics 
of the two medical centers and their roles in the local health care system are different, 
we speculate that this could be one of the main reasons that the enrolled patient 
populations were heterogeneous. As described in the Introduction, DOC can have 
many causes and be associated with several neuropathological processes and different 
severities, leading to the suggestion that information from different domains should be 
integrated to improve diagnosis and prognostication (Bernat, 2016). Our study 
demonstrates that the combination of imaging and clinical features can achieve a better 
performance than the use of single domain features. 
However, some caution is warranted. Firstly, although this study involved 112 
DOC patients, the patients who would later recover consciousness was relatively low 
(i.e. 31/112). So, a much larger cohort will be needed for further validation. Secondly, 
the PPVs for the two testing datasets were remarkably different, with that for the 
"Guangzhou HDxt" dataset being relatively low (67% versus 91%). Although our 
method predicted that nine patients in this dataset would recover consciousness, only 
six of them did (i.e. GOS≥3), with the other three remaining unconscious at the end of 
the follow-up (i.e. GOS≤2). Given that many additional factors are associated with the 
outcome of DOC patients, including medical complications, nutrition and so on, 
future work will need to integrate more information in order to provide more precise 
predictions. Thirdly, the signal-to-noise ratio of resting state fMRI can influence


## Page 37


37 / 102 
 
functional connectivity analysis, so calibrations will be necessary when applying the 
predictive model across different sites, including standardizing the MRI acquisition 
protocols (e.g. scanner hardware, imaging protocols and acquisition sequences) and 
the patients' management strategies (see Appendix 10 for more information). Finally, 
a DOC patient’s prognosis can be considered according to at least three dimensions: 
survival/mortality, recovery of consciousness, and functional recovery. This study 
focused on predicting recovery of consciousness, and the patients who died during the 
follow-up were excluded. In the future, we will consider more outcome assessments, 
including survival/mortality and functional recovery. 
In summary, our prognostic model, which combines resting state fMRI with 
clinical characteristics, is proposed to predict the one year outcome of DOC patients 
at an individual level. The average accuracy of classifying a patient as "consciousness 
recovery" or not was around 88% in the training dataset and two unseen testing 
datasets. Our model also has good interpretability, thereby providing a window to 
reassure physicians and scientists about the significance of different predictors, 
including brain networks, functional connectivities and clinical characteristics. 
Together, these advantages could offer an objective prognosis for DOC patients to 
optimize their management and deepen our understanding of brain function during 
unconsciousness.


## Page 38


38 / 102 
 
Acknowledgements 
The authors appreciate the help of Ms Rowan Tweedale with the use of English in 
this paper. 
 
Funding 
This work was partially supported by the Natural Science Foundation of China 
(Grant Nos. 81471380, 91432302, 31620103905), the Science Frontier Program of the 
Chinese Academy of Sciences (Grant No. QYZDJ-SSW-SMC019), National Key 
R&D Program of China(Grant No. 2017YFA0105203), Beijing Municipal Science& 
Technology Commission (Grant Nos. Z161100000216139, Z161100000216152, 
Z161100000516165), the Guangdong Pearl River Talents Plan Innovative and 
Entrepreneurial Team grant (2016ZT06S220) and Youth Innovation Promotion 
Association CAS. 
 
References  
Bernat JL. Chronic disorders of consciousness. Lancet 2006; 367(9517): 1181-92. 
Bernat JL. Prognostic limitations of syndromic diagnosis in disorders of 
consciousness. AJOB Neuroscience 2016; 7(1): 46-8. 
Booth CM, Boone RH, Tomlinson G, Detsky AS. Is this patient dead, vegetative, or 
severely neurologically impaired? Assessing outcome for comatose survivors of 
cardiac arrest. Jama-Journal of the American Medical Association 2004; 291(7): 
870-9.


## Page 39


39 / 102 
 
Bruno M-A, Ledoux D, Vanhaudenhuyse A, Gosseries O, Thibaut A, Laureys S. 
Prognosis of Patients with Altered State of Consciousness. In: Schnakers C, Laureys S, 
editors. Coma and Disorders of Consciousness. London: Springer London; 2012. p. 
11-23. 
Buckner RL, Andrews JR, Schacter DL. The Brain's Default Network. Ann N Y Acad 
Sci 2008; 1124: 1-38. 
Celesia GG. Vegetative State Two Decades After the Multi-Society Task Force 
(MSTF) Report.  Brain Function and Responsiveness in Disorders of Consciousness: 
Springer; 2016. p. 171-84. 
Chennu S, Annen J, Wannez S, Thibaut A, Chatelle C, Cassoi H, et al. Brain networks 
predict metabolism, diagnosis and prognosis at the bedside in disorders of 
consciousness. Brain 2017; 140: 2120-32. 
Corazzol M, Lio G, Lefevre A, Deiana G, Tell L, André-Obadia N, et al. Restoring 
consciousness with vagus nerve stimulation. Current Biology 2017; 27(18): R994-R6. 
Coyle D, Stow J, McCreadie K, McElligott J, Carroll A. Sensorimotor Modulation 
Assessment and Brain-Computer Interface Training in Disorders of Consciousness. 
Archives of Physical Medicine and Rehabilitation 2015; 96(3): S62-S70. 
Damoiseaux JS, Rombouts SA, Barkhof F, Scheltens P, Stam CJ, Smith SM, et al. 
Consistent resting-state networks across healthy subjects. Proc Natl Acad Sci U S A 
2006; 103(37): 13848-53. 
Demertzi A, Antonopoulos G, Heine L, Voss HU, Crone JS, de Los Angeles C, et al. 
Intrinsic 
functional 
connectivity 
differentiates 
minimally 
conscious 
from 
unresponsive patients. Brain 2015; 138: 2619-31. 
Demertzi A, Antonopoulos G, Voss HU, Crone JS, Schiff ND, Kronbichler M, et al. 
Audio-visual crossmodal fMRI connectivity differentiates single patients with


## Page 40


40 / 102 
 
disorders of consciousness.  Frontiers in Human Neuroscience: Belgian Brain 
Council 2014 MODULATING THE BRAIN: FACTS, FICTION, FUTURE; 2014a. 
Demertzi A, Gomez F, Crone JS, Vanhaudenhuyse A, Tshibanda L, Noirhomme Q, et 
al. Multiple fMRI system-level baseline connectivity is disrupted in patients with 
consciousness alterations. Cortex 2014b; 52: 35-46. 
Demertzi A, Sitt J, Sarasso S, Pinxten W. Measuring states of pathological 
(un)consciousness: research dimensions, clinical applications, and ethics; 2017. 
Di Perri C, Bahri MA, Amico E, Thibaut A, Heine L, Antonopoulos G, et al. Neural 
correlates of consciousness in patients who have emerged from a minimally conscious 
state: a cross-sectional multimodal imaging study. Lancet Neurology 2016; 15(8): 
830-42. 
Dolce G, Quintieri M, Serra S, Lagani V, Pignolo L. Clinical signs and early 
prognosis in vegetative state: A decisional tree, data-mining study. Brain Injury 2008; 
22(7-8): 617-23. 
Dosenbach NUF, Nardos B, Cohen AL, Fair DA, Power JD, Church JA, et al. 
Prediction of Individual Brain Maturity Using fMRI. Science 2010; 329(5997): 
1358-61. 
Drysdale AT, Grosenick L, Downar J, Dunlop K, Mansouri F, Meng Y, et al. 
Resting-state connectivity biomarkers define neurophysiological subtypes of 
depression. Nat Med 2016; advance online publication. 
Estraneo A, Moretta P, Loreto V, Lanzillo B, Cozzolino A, Saltalamacchia A, et al. 
Predictors of recovery of responsiveness in prolonged anoxic vegetative state. 
Neurology 2013; 80(5): 464-70. 
Estraneo A, Moretta P, Loreto V, Lanzillo B, Santoro L, Trojano L. Late recovery after 
traumatic, anoxic, or hemorrhagic long-lasting vegetative state. Neurology 2010;


## Page 41


41 / 102 
 
75(3): 239-45. 
Fan W, Li H, Shan Y, Lv H, Zhang H, Liang Y. Classification of vinegar samples 
based on near infrared spectroscopy combined with wavelength selection. Analytical 
Methods 2011; 3(8): 1872-6. 
Fan Y, Shen D, Gur RC, Gur RE, Davatzikos C. COMPARE: Classification of 
Morphological Patterns Using Adaptive Regional Elements. IEEE Transactions on 
Medical Imaging 2007; 26(1): 93-105. 
Fischer DB, Boes AD, Demertzi A, Evrard HC, Laureys S, Edlow BL, et al. A human 
brain network derived from coma-causing brainstem lesions. Neurology 2016; 87(23): 
2427-34. 
Fox MD, Snyder AZ, Vincent JL, Corbetta M, Van Essen DC, Raichle ME. The 
human brain is intrinsically organized into dynamic, anticorrelated functional 
networks. Proc Natl Acad Sci U S A 2005; 102(27): 9673-8. 
Galanaud D, Perlbarg V, Gupta R, Stevens RD, Sanchez P, Tollard E, et al. 
Assessment of White Matter Injury and Outcome in Severe Brain Trauma A 
Prospective Multicenter Cohort. Anesthesiology 2012; 117(6): 1300-10. 
Gardumi A, Ivanov D, Hausfeld L, Valente G, Formisano E, Uludag K. The effect of 
spatial resolution on decoding accuracy in fMRI multivariate pattern analysis. 
Neuroimage 2016; 132: 32-42. 
Giacino J, Kalmar K. Coma Recovery Scale-Revised.  2006  [cited 2018 June 21]; 
Available from: http://www.tbims.org/combi/crs  
Giacino JT, Schnakers C, Rodriguez-Moreno D, Kalmar K, Schiff N, Hirsch J. 
Behavioral assessment in patients with disorders of consciousness: gold standard or 
fool's gold? In: Laureys S, Schiff ND, Owen AM, editors. Coma Science: Clinical and 
Ethical Implications. Amsterdam: Elsevier Science Bv; 2009. p. 33-48.


## Page 42


42 / 102 
 
Golkowski D, Merz K, Mlynarcik C, Kiel T, Schorr B, Lopez-Rolon A, et al. 
Simultaneous EEG-PET-fMRI measurements in disorders of consciousness: an 
exploratory study on diagnosis and prognosis. Journal of Neurology 2017; 264(9): 
1986-95. 
Gosseries O, Zasler ND, Laureys S. Recent advances in disorders of consciousness: 
Focus on the diagnosis. Brain Injury 2014; 28(9): 1141-50. 
Greicius MD, Srivastava G, Reiss AL, Menon V. Default-mode network activity 
distinguishes Alzheimer's disease from healthy aging: Evidence from functional MRI. 
Proceedings of the National Academy of Sciences of the United States of America 
2004; 101(13): 4637-42. 
Guyon I, Elisseeff A. An introduction to variable and feature selection. Journal of 
Machine Learning Research 2003; 3(7-8): 1157-82. 
Hay E, Ritter P, Lobaugh NJ, McIntosh AR. Multiregional integration in the brain 
during resting-state fMRI activity. Plos Computational Biology 2017; 13(3). 
He JH, Cui Y, Song M, Yang Y, Dang YY, Jiang TZ, et al. Decreased functional 
connectivity between the mediodorsal thalamus and default mode network in patients 
with disorders of consciousness. Acta Neurologica Scandinavica 2015; 131(3): 
145-51. 
Hofmeijer J, van Putten MJAM. EEG in postanoxic coma: Prognostic and diagnostic 
value. Clinical Neurophysiology 2016; 127(4): 2047-55. 
Huettel SA, Song AW, McCarthy G. Functional Magnetic Resonance Imaging. 2 ed: 
Sinauer Associates; 2009. 
James G, Witten D, Hastie T, Tibshirani R. An Introduction to Statistical Learning: 
Springer; 2013. 
Jennett B. Thirty years of the vegetative state: clinical, ethical and legal problems. In:


## Page 43


43 / 102 
 
Laureys S, editor. Boundaries of Consciousness: Neurobiology and Neuropathology; 
2005. p. 537-43. 
Kaneko T, Kasaoka S, Miyauchi T, Fujita M, Oda Y, Tsuruta R, et al. Serum glial 
fibrillary acidic protein as a predictive biomarker of neurological outcome after 
cardiac arrest. Resuscitation 2009; 80(7): 790-4. 
Kang X-g, Li L, Wei D, Xu X-x, Zhao R, Jing Y-y, et al. Development of a simple 
score to predict outcome for unresponsive wakefulness syndrome. Critical Care 2014; 
18(1). 
Krishnan A, Williams LJ, McIntosh AR, Abdi H. Partial Least Squares (PLS) methods 
for neuroimaging: A tutorial and review. Neuroimage 2011; 56(2): 455-75. 
Kvalheim OM, Arneberg R, Bleie O, Rajalahti T, Smilde AK, Westerhuis JA. Variable 
importance in latent variable regression models. Journal of Chemometrics 2014; 28(8): 
615-22. 
Kvalheim OM, Karstang TV. INTERPRETATION OF LATENT-VARIABLE 
REGRESSION-MODELS. Chemometrics and Intelligent Laboratory Systems 1989; 
7(1-2): 39-51. 
Li H, Liang Y, Xu Q, Cao D. Key wavelengths screening using competitive adaptive 
reweighted sampling method for multivariate calibration. Analytica Chimica Acta 
2009; 648(1): 77-84. 
Li H, Xu Q, Liang Y. libPLS: an integrated library for partial least squares regression 
and discriminant analysis. PeerJ PrePrints 2014; 2: e190v1. 
Luaute J, Maucort-Boulch D, Tell L, Quelard F, Sarraf T, Iwaz J, et al. Long-term 
outcomes of chronic minimally conscious and vegetative states. Neurology 2010; 
75(3): 246-52. 
Luyt C-E, Galanaud D, Perlbarg V, Vanhaudenhuyse A, Stevens RD, Gupta R, et al.


## Page 44


44 / 102 
 
Diffusion Tensor Imaging to Predict Long-term Outcome after Cardiac Arrest A 
Bicentric Pilot Study. Anesthesiology 2012; 117(6): 1311-21. 
Maas AIR, Steyerberg EW, Butcher I, Dammers R, Lu J, Marmarou A, et al. 
Prognostic value of computerized tomography scan characteristics in traumatic brain 
injury: Results from the IMPACT study. Journal of Neurotrauma 2007; 24(2): 303-14. 
Magrassi L, Maggioni G, Pistarini C, Di Perri C, Bastianello S, Zippo AG, et al. 
Results of a prospective study (CATS) on the effects of thalamic stimulation in 
minimally conscious and vegetative state patients. Journal of Neurosurgery 2016; 
125(4): 972-81. 
Mehmood T, Liland KH, Snipen L, Saebo S. A review of variable selection methods 
in Partial Least Squares Regression. Chemometrics and Intelligent Laboratory 
Systems 2012; 118: 62-9. 
Monti MM, Vanhaudenhuyse A, Coleman MR, Boly M, Pickard JD, Tshibanda L, et 
al. Willful Modulation of Brain Activity in Disorders of Consciousness. New England 
Journal of Medicine 2010; 362(7): 579-89. 
Nayak P, Mahapatra AK. Single photon emission computed tomography scanning: A 
predictor of outcome in vegetative state of head injury. Journal of neurosciences in 
rural practice 2011; 2(1): 12-6. 
Noirhomme Q, Brecheisen R, Lesenfants D, Antonopoulos G, Laureys S. "Look at my 
classifier's result": Disentangling unresponsive from (minimally) conscious patients. 
Neuroimage 2017; 145: 288-303. 
Owen AM, Coleman MR, Boly M, Davis MH, Laureys S, Pickard JD. Detecting 
awareness in the vegetative state. Science 2006; 313(5792): 1402-. 
Phillips CL, Bruno M-A, Maquet P, Boly M, Noirhomme Q, Schnakers C, et al. 
"Relevance vector machine" consciousness classifier applied to cerebral metabolism


## Page 45


45 / 102 
 
of vegetative and locked-in patients. Neuroimage 2011; 56(2): 797-808. 
Pignat J-M, Mauron E, Johr J, de Keranflec'h CG, Van De Ville D, Preti MG, et al. 
Outcome Prediction of Consciousness Disorders in the Acute Stage Based on a 
Complementary Motor Behavioural Tool. Plos One 2016; 11(6). 
Power JD, Schlaggar BL, Petersen SE. Recent progress and outstanding issues in 
motion correction in resting state fMRI. Neuroimage 2015; 105: 536-51. 
Qin P, Wu X, Huang Z, Duncan NW, Tang W, Wolff A, et al. How are different neural 
networks nelated to consciousness? Ann Neurol 2015; 78(4): 594-605. 
Raichle ME. The restless brain. Brain connectivity 2011; 1(1): 3-12. 
Roquet D, Foucher JR, Froehlig P, Renard F, Pottecher J, Besancenot H, et al. 
Resting-state networks distinguish locked-in from vegetative state patients. 
Neuroimage-Clinical 2016; 12: 16-22. 
Rossetti AO, Rabinstein AA, Oddo M. Neurological prognostication of outcome in 
patients in coma after cardiac arrest. Lancet Neurology 2016; 15(6): 597-609. 
Rundgren M, Karlsson T, Nielsen N, Cronberg T, Johnsson P, Friberg H. Neuron 
specific enolase and S-100B as predictors of outcome after cardiac arrest and induced 
hypothermia. Resuscitation 2009; 80(7): 784-9. 
Schiff ND, Giacino JT, Kalmar K, Victor JD, Baker K, Gerber M, et al. Behavioural 
improvements with thalamic stimulation after severe traumatic brain injury. Nature 
2007; 448(7153): 600-U10. 
Seeley WW, Menon V, Schatzberg AF, Keller J, Glover GH, Kenna H, et al. 
Dissociable intrinsic connectivity networks for salience processing and executive 
control. Journal of Neuroscience 2007; 27(9): 2349-56. 
Sidaros A, Engberg A, Sidaros K, Liptrot MG, Herning M, Petersen P, et al. Diffusion


## Page 46


46 / 102 
 
tensor imaging during recovery from severe traumatic brain injury and relation to 
clinical outcome: a longitudinal study. Brain 2008; 131: 559-72. 
Silva S, de Pasquale F, Vuillaume C, Riu B, Loubinoux I, Geeraerts T, et al. 
Disruption of posteromedial large-scale neural communication predicts recovery from 
coma. Neurology 2015; 85(23): 2036-44. 
Stender J, Gosseries O, Bruno M-A, Charland-Verville V, Vanhaudenhuyse A, 
Demertzi A, et al. Diagnostic precision of PET imaging and functional MRI in 
disorders of consciousness: a clinical validation study. Lancet 2014; 384(9942): 
514-22. 
Steppacher I, Eickhoff S, Jordanov T, Kaps M, Witzke W, Kissler J. N400 predicts 
recovery from disorders of consciousness. Ann Neurol 2013; 73(5): 594-602. 
Stevens RD, Sutter R. Prognosis in Severe Brain Injury. Critical Care Medicine 2013; 
41(4): 1104-23. 
Steyerberg E. Clinical prediction models: a practical approach to development, 
validation, and updating: Springer Science & Business Media; 2008. 
Tan B, Liang Y, Yi L, Li H, Zhou Z, Ji X, et al. Identification of free fatty acids 
profiling of type 2 diabetes mellitus and exploring possible biomarkers by GC-MS 
coupled with chemometrics. Metabolomics 2010; 6(2): 219-28. 
The Multi-Society Task Force on PVS. Medical Aspects of the Persistent Vegetative 
State. New England Journal of Medicine 1994; 330(21): 1499-508. 
Tran TN, Afanador NL, Buydens LMC, Blanchet L. Interpretation of variable 
importance in Partial Least Squares with Significance Multivariate Correlation (sMC). 
Chemometrics and Intelligent Laboratory Systems 2014; 138: 153-60. 
Vanhaudenhuyse A, Noirhomme Q, Tshibanda LJF, Bruno MA, Boveroux P, 
Schnakers C, et al. Default network connectivity reflects the level of consciousness in


## Page 47


47 / 102 
 
non-communicative brain-damaged patients. Brain 2010; 133: 161-71. 
Wannez S, Heine L, Thonnard M, Gosseries O, Laureys S, Coma Sci Grp C. The 
Repetition of Behavioral Assessments in Diagnosis of Disorders of Consciousness. 
Ann Neurol 2017; 81(6): 883-9. 
Welvaert M, Rosseel Y. On the Definition of Signal-To-Noise Ratio and 
Contrast-To-Noise Ratio for fMRI Data. Plos One 2013; 8(11). 
Wijdicks EFM, Cranford RE. Clinical diagnosis of prolonged states of impaired 
consciousness in adults. Mayo Clinic Proceedings 2005; 80(8): 1037-46. 
Wold S, Sjostrom M, Eriksson L. PLS-regression: a basic tool of chemometrics. 
Chemometrics and Intelligent Laboratory Systems 2001; 58(2): 109-30. 
Wu X, Zou Q, Hu J, Tang W, Mao Y, Gao L, et al. Intrinsic Functional Connectivity 
Patterns Predict Consciousness Level and Recovery Outcome in Acquired Brain 
Injury. Journal of Neuroscience 2015; 35(37): 12932-46. 
Yao S, Song J, Gao L, Yan Y, Huang C, Ding H, et al. Thalamocortical Sensorimotor 
Circuit Damage Associated with Disorders of Consciousness for Diffuse Axonal 
Injury Patients. Journal of the Neurological Sciences 2015; 356(1-2): 168-74. 
Yu Y-t, Yang Y, Wang L-b, Fang J-l, Chen Y-y, He J-h, et al. Transcutaneous auricular 
vagus nerve stimulation in disorders of consciousness monitored by fMRI: The first 
case report. Brain Stimulation 2017; 10(2): 328-30. 
Zandbergen EGJ, de Haan RJ, Stoutenbeek CP, Koelman J, Hijdra A. Systematic 
review of early prediction of poor outcome in anoxic-ischaemic coma. Lancet 1998; 
352(9143): 1808-12.


## Page 48


48 / 102 
 
Legend 
Table 1 Demographic and clinical characteristics of the patients in the three datasets. 
 
Beijing_750
(n=63) 
Beijing_HDxt
(n=25) 
Guangzhou_HDxt
(n=24) 
Gender, M/F 
36/27 
18/7 
14/10 
Etiology 
  Trauma/Stroke/Anoxia 
 
17/21/25 
 
12/6/7 
 
8/0/16 
Age at the T0 (years)  
 
 
 
  Mean(SD) 
42.8(13.8) 
40.7(15.2) 
39.3(16.9) 
  Range 
18.0~71.0 
18.0~68.0 
15.0~78.0 
Time to MRI (months)  
 
 
 
  Range 
1.0~77.0 
1.0~44.0 
1.0~10.0 
  Mean(SD) 
7.4(12.8) 
5.4(8.4) 
2.3(2.4) 
  Median 
3.0 
3.0 
1.5 
  Band 
 
 
 
    [1,3] 
32 
13 
20 
    (3,6]     
15 
8 
2 
    (6,12] 
11 
3 
2 
    >12 
5 
1 
0 
Follow-up time (months)  
 
 
 
  Range 
12.0~51.0 
14.0~53.0 
27.0~78.0 
  Mean(SD) 
21.0(9.8) 
41.7(8.4) 
52.2(14.5) 
  Median 
15.0 
43.0 
53.0 
  Band  
 
 
 
    [12,24] 
38 
2 
0 
    (24,48] 
24 
20 
8 
    >48 
1 
3 
16 
   
Diagnosis at T0 
 
 
 
MCS/VS 
17/46 
5/20 
8/16 
CRS-R total score  
 
 
 
  Mean(SD) 
7.3(2.9) 
6.5(2.3) 
7.1(4.1) 
  Range 
3.0~18.0 
3.0~14.0 
3.0~17.0 
 
 
 
 
Outcome at T1 
 
 
 
CRS-R total score 
 
 
 
  Mean(SD) 
9.9(5.1) 
12.7(6.4) 
N/A 
  Range 
3.0~22.0 
5.0~23.0 
N/A 
GOS score 
 
 
 
  GOS=5 
0 
0 
0 
  GOS=4 
5 
5 
1 
  GOS=3 
8 
7 
5 
  GOS<=2 
50 
13 
18


## Page 49


49 / 102 
 
Abbreviations: CRS-R: Coma Recovery Scale–Revised; GOS: Glasgow Outcome 
Scale; MCS: minimally conscious state; N/A: not available; SD: standard deviation; 
VS: vegetative state/unresponsive wakefulness syndrome.


## Page 50


50 / 102 
 
Figure 1. Conceptual paradigm of the study. CRS-R: Coma Recovery Scale Revised 
scale; GOS: Glasgow Outcome Scale.


## Page 51


51 / 102 
 
Figure 2. Data analysis pipeline. All datasets involved in this study included resting 
state fMRI and clinical data. For the fMRI data in the training dataset, data analysis 
first encompassed preprocessing and imaging feature selection and extraction. Partial 
least square regression was then used to generate the regression model using the 
selected imaging features and clinical features in the training dataset. In this way, a 
prediction score that depicts the possibility of consciousness recovery was computed 
for each patient. The optimal cut-off value for classifying an individual patient as 
responsive or non-responsive was then calculated, and the prognostic classification 
model was obtained. The two testing datasets were only used to externally validate the 
regression and classification model.


## Page 52


52 / 102


## Page 53


53 / 102 
 
Figure 3. 
Imaging features involved in the prognostic regression model. 
DMN.aMPFC: anterior medial prefrontal cortex in the default mode network; 
DMN.PCC: posterior cingulate cortex/precuneus in the default mode network; 
ExecuContr.DMPFC: dorsal medial prefrontal cortex in the executive control network; 
Auditory.MCC: middle cingulate cortex in the auditory network; Visual.R.V1: right 
lateral 
primary 
visual 
cortex 
in 
the 
visual 
network. 
DMN.aMPFC 
- 
ExecuContr.DMPFC: the functional connectivity between DMN.aMPFC and 
ExecuContr.DMPFC; Auditory.MCC - Visual.R.V1: the functional connectivity 
between Auditory.MCC and Visual.R.V1.


## Page 54


54 / 102


## Page 55


Figure 4. Prognostic regre
particular predictor. (A)
predictor in prognostic r
F-test value. The larger
with respect to the regre
rendered on a 3D surface
 
 55 / 102 
ession model. In the three subplots, each c
) Regression formula. (B) Predictor impor
regression model. The vertical axis repre
r the sMC F-value, the more informative
ession model. (C) The imaging features in 
e plot template in medial view.  
 
color denotes a 
rtance for each 
sents the sMC 
e the predictor 
the model are


## Page 56


56 / 102 
 
Figure 5. 
The performance of the prediction model on the training dataset. (A) 
Individual predicted scores for each DOC patient in the training dataset. The CRS-R 
score at the T0 time point is shown on the x axis and the predicted score on the y axis. 
The patients diagnosed as VS/UWS at the T0 time point are shown to the left of the 
vertical red solid line, whereas the patients diagnosed as MCS at this time point are 
shown to the right. The purplish red pentagram, imperial purple triangle and blank 
circle mark the patients with a GOS score ≥4, =3 and ≤2, respectively, at the T1 time 
point. (B) Agreement between the CRS-R scores at the T1 time point and the 
predicted scores. The left panel shows the correlation between the CRS-R scores at 
the T1 time point and the predicted scores, and the right panel shows the differences 
between them using the Bland-Altman plot. (C) Bar chart showing the numbers or 
proportions of DOC patients in each band of predicted scores. In these two panels, the 
y axis shows the predicted score. (D) The area under the receiver-operating 
characteristic (ROC) curve. The star on the curve represents the point with the 
maximal sum of true positive and false negative rates on the ROC curve, which were 
chosen as the cut-off threshold for classification. Here, the corresponding predicted 
score=13.9.


## Page 57


57 / 102


## Page 58


58 / 102 
 
Figure 6. The performance of the prediction model on the two testing datasets. (A) 
The individual predicted score (top panel) and agreement between the CRS-R scores 
at the T1 time point and the predicted scores (bottom panel) for the testing dataset 
"Beijing HxDt". (B) The individual predicted score for each DOC patient in the 
testing dataset "Guangzhou HxDt". The legend description is the same as for Figure 5.


## Page 59


59 / 102


## Page 60


Figure 7. The sensitivity 
unconsciousness T0≤3 m
unconsciousness T0 >3 mo
 60 / 102 
and specificity in the "subacute" patients (
months) and those in the chronic phase (i
onths), respectively. 
(i.e. duration of 
i.e. duration of


## Page 61


61 / 102 
 
Supplementary file 1. Some examples of the warped ROIs in the default mode 
network for one healthy control and three DOC patients with a GOS score 2,3,4, 
respectively.  
 
Supplementary file 2. Details about single-domain prognostic models and 
comparisons of the single-domain and combination models.


## Page 62


62 / 102 
 
Appendix 1:  
Demographic and clinical characteristics of patients and normal controls in this study.  
The diagnosis in this study was made by experienced physicians according to the CRS-R scale. Patients were diagnosed as MCS when they 
demonstrated at least one of the following behaviors: (1) following simple commands; (2) yes/no responses (gestural or verbal); (3) intelligible 
verbalization; (4) purposeful behavior in response to an environmental stimulus; (5) vocalization or gestures in direct response to questions; (6) 
reaching for objects that demonstrates a clear relationship between the position of the object and the direction of the movement; (7) touching or 
holding objects; (8) following or staring at an object in direct response to its movement. Emergence from the MCS was signaled by the return of 
functional communication and/or object use.  
In this study, the patients underwent the CRS-R assessments twice weekly (or more) within the two weeks before MRI scanning. So, the CRS-R 
can be generally administered about 4-5 times for a patient. The highest CRS-R score was considered as the diagnosis and listed in the following 
tables. T0:  the time point of the MRI scanning; T1: the time point of follow-up.


## Page 63


63 / 102 
 
Appendix 1-table 1. Demographic and clinical characteristics of patients in the "Beijing_750" dataset.  
patient 
alias 
gender 
age 
(years) diagnose etiology 
structural 
lesions on 
MRI 
time to 
MRI 
(months) 
number of 
CRS-R 
assessments 
CRS-R 
score 
at T0 
CRS-R 
subscore 
at T0 
CRS-R 
score 
at T1 
CRS-R 
subscore 
at T1 
follow-up
（months） GOS predicted 
score 
001 
M 
36 
VS/UWS 
Anoxia 
Diffuse pons 
damage 
1 
6 
7 
022102 
22 
446323 
15 
4 
18.26 
002 
M 
29 
MCS 
Trauma 
Bilateral-temp
oro-parietal 
damage 
9 
4 
18 
355113 
22 
456223 
39 
4 
15.31 
003 
F 
33 
VS/UWS 
Trauma 
Bilateral-front
al lobe 
damage, 
atrophy 
12 
5 
7 
102202 
22 
455323 
12 
4 
22.88 
004 
F 
28 
MCS 
Trauma 
L-frontal-temp
oral lobe 
damage 
1 
4 
15 
335103 
22 
456223 
19 
4 
16.58 
005 
M 
23 
MCS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
3 
4 
10 
232102 
21 
455223 
13 
4 
17.08 
006 
M 
45 
MCS 
Stroke 
L-temporo-par
ietal damage 
9 
4 
9 
222102 
17 
334223 
12 
3 
13.94 
007 
M 
39 
MCS 
Stroke 
Brainstem 
damage 
1 
4 
17 
345113 
19 
445123 
12 
3 
14.39 
008 
F 
27 
MCS 
Trauma L-basal ganglia 
10 
6 
12 
332103 
18 
345123 
19 
3 
16.09


## Page 64


64 / 102 
 
damage 
009 
M 
23 
MCS 
Trauma 
Diffuse 
cortical & 
subcortical 
atrophy 
6 
4 
9 
132102 
19 
444223 
13 
3 
10.94 
010 
M 
42 
MCS 
Stroke 
L-basal ganglia 
damage 
3 
7 
7 
103102 
19 
416323 
12 
3 
14.72 
011 
M 
53 
MCS 
Stroke 
Diffuse 
cortical & 
basal ganglia 
(caudates) 
damage 
7 
5 
11 
332102 
14 
332123 
14 
3 
11.55 
012 
F 
40 
VS/UWS 
Stroke 
Diffuse 
cortical & 
basal ganglia 
damage 
5 
6 
7 
112102 
14 
333122 
12 
3 
14.67 
013 
M 
22 
VS/UWS 
Trauma 
L-frontal-temp
oro-parietal 
lobe damage 
3 
4 
7 
112102 
15 
334122 
27 
3 
15.48 
014 
F 
64 
VS/UWS 
Stroke 
L-thalamus, 
basal ganglia 
lesions 
1 
4 
7 
112102 
11 
233102 
17 
2 
8.28 
015 
F 
42 
VS/UWS 
Anoxia 
Diffuse anoxic 
cortical lesions 
1 
4 
7 
112102 
9 
222102 
14 
2 
9.02 
016 
M 
45 
VS/UWS 
Anoxia 
Diffuse anoxic 
cortical lesions 
9 
5 
5 
002102 
7 
112102 
15 
2 
8.65


## Page 65


65 / 102 
 
017 
F 
60 
VS/UWS 
Anoxia 
Diffuse anoxic 
cortical lesions 
4 
4 
6 
102102 
6 
102102 
13 
2 
7.71 
018 
M 
42 
VS/UWS 
Stroke 
R-cerebral 
hemisphere 
lesions 
6 
4 
7 
112102 
7 
112102 
14 
2 
12.44 
019 
M 
51 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
3 
4 
7 
112102 
7 
112102 
28 
2 
4.28 
020 
F 
35 
VS/UWS 
Anoxia 
Bilateral-front
al lobe 
damage, 
atrophy 
2 
4 
7 
112102 
7 
112102 
13 
2 
5.87 
021 
M 
71 
VS/UWS 
Trauma 
Diffuse 
cortical & 
subcortical 
atrophy 
6 
6 
3 
101100 
4 
101101 
13 
2 
4.46 
022 
F 
30 
VS/UWS 
Anoxia 
Bilateral-basal 
ganglia 
damage 
2 
4 
4 
002002 
7 
022102 
38 
2 
6.92 
023 
F 
58 
VS/UWS 
Trauma 
Diffuse 
cortical & 
subcortical 
atrophy 
2 
4 
3 
002100 
4 
002101 
14 
2 
5.09 
024 
M 
23 
MCS 
Trauma 
R-basal 
ganglia 
5 
5 
7 
103102 
11 
223202 
12 
2 
14.57


## Page 66


66 / 102 
 
(caudates) 
damage 
025 
F 
66 
VS/UWS 
Trauma 
Bilateral-temp
oro-parietal 
damage 
1 
4 
6 
102102 
8 
113102 
32 
2 
5.71 
026 
F 
25 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
3 
4 
5 
102002 
6 
112002 
36 
2 
6.75 
027 
M 
48 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
4 
5 
7 
112102 
8 
113102 
29 
2 
7.83 
028 
F 
28 
MCS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
5 
4 
9 
222102 
11 
233102 
32 
2 
11.36 
029 
M 
57 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
11 
4 
6 
102102 
6 
102102 
33 
2 
4.70 
030 
M 
61 
MCS 
Stroke 
Bilateral-temp
oro-parietal 
lobe damage 
2 
4 
11 
134102 
11 
223112 
12 
2 
10.34 
031 
M 
40 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
4 
4 
4 
001102 
5 
011102 
27 
2 
5.70


## Page 67


67 / 102 
 
subcortical 
atrophy 
032 
M 
39 
VS/UWS 
Stroke 
R-basal 
ganglia 
damage, 
atrophy 
3 
4 
7 
112102 
7 
112102 
12 
2 
8.03 
033 
M 
41 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
2 
4 
5 
002102 
5 
002102 
13 
2 
6.44 
034 
M 
26 
VS/UWS 
Stroke 
Diffuse 
cortical & 
subcortical 
atrophy 
54 
4 
7 
112102 
7 
112102 
38 
2 
7.28 
035 
F 
50 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
8 
6 
6 
102102 
9 
122202 
12 
2 
5.77 
036 
F 
53 
VS/UWS 
Stroke 
Bilateral 
brainstem, 
midbrain 
damage 
3 
4 
5 
112100 
7 
112102 
28 
2 
8.02 
037 
M 
67 
VS/UWS 
Stroke 
R- brainstem, 
cerebellar 
damage 
1 
4 
5 
112100 
3 
002001 
12 
2 
2.04 
038 
M 
45 
MCS 
Stroke 
Diffuse 
2 
5 
9 
132102 
10 
222112 
13 
2 
10.91


## Page 68


68 / 102 
 
cortical & 
subcortical 
atrophy 
039 
F 
35 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
3 
4 
6 
102102 
8 
112202 
19 
2 
10.24 
040 
F 
46 
MCS 
Trauma Diffuse axonal 
injury 
77 
7 
11 
222212 
13 
332212 
51 
2 
14.76 
041 
M 
49 
VS/UWS 
Stroke 
Bilateral-brain
stem, 
cerebellar 
damage 
10 
4 
7 
112102 
7 
112102 
28 
2 
10.87 
042 
M 
45 
VS/UWS 
Stroke 
Diffuse 
cortical & 
basal ganglia 
damage 
3 
4 
7 
112102 
8 
122102 
19 
2 
7.59 
043 
M 
18 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
8 
5 
6 
111102 
9 
123102 
12 
2 
10.85 
044 
M 
53 
VS/UWS 
Anoxia 
Bilateral-occipi
tal lobe 
damage, 
atrophy 
2 
4 
3 
002001 
7 
112102 
34 
2 
1.98 
045 
M 
46 
VS/UWS 
Trauma R-temporo-pa
4 
4 
6 
101202 
6 
101202 
13 
2 
7.23


## Page 69


69 / 102 
 
rietal damage 
046 
F 
29 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
28 
4 
7 
112102 
9 
123102 
12 
2 
8.31 
047 
F 
47 
MCS 
Stroke 
R-basal 
ganglia 
damage 
47 
5 
8 
113102 
11 
222212 
12 
2 
9.66 
048 
M 
58 
VS/UWS 
Stroke 
Bilateral-temp
oro-parietal 
lobe damage 
6 
4 
7 
112102 
8 
113102 
27 
2 
7.05 
049 
M 
66 
VS/UWS 
Anoxia 
L-frontal lobe 
damage 
4 
4 
4 
002002 
6 
102102 
38 
2 
4.79 
050 
M 
34 
VS/UWS 
Trauma Diffuse axonal 
injury 
3 
4 
6 
112101 
8 
122102 
14 
2 
10.28 
051 
F 
31 
MCS 
Trauma 
L-frontal-temp
oro-parietal 
lobe damage 
3 
5 
11 
133202 
8 
112202 
15 
2 
15.56 
052 
M 
33 
VS/UWS 
Stroke 
L-temporo-par
ietal lobe 
damage 
17 
4 
6 
102102 
8 
113102 
13 
2 
7.67 
053 
F 
31 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
basal ganglia 
(caudates) 
damage 
1 
4 
6 
102102 
6 
102102 
27 
2 
8.36


## Page 70


70 / 102 
 
054 
F 
28 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
3 
4 
6 
102102 
8 
112202 
32 
2 
9.23 
055 
F 
26 
VS/UWS 
Stroke 
L-basal ganglia 
damage 
4 
4 
6 
102102 
6 
102102 
12 
2 
10.96 
056 
M 
45 
VS/UWS 
Trauma Diffuse axonal 
injury 
1 
4 
6 
102102 
6 
102102 
29 
2 
9.05 
057 
F 
69 
VS/UWS 
Stroke 
Diffuse 
cortical & 
subcortical 
atrophy 
4 
4 
6 
102102 
7 
102202 
33 
2 
12.43 
058 
F 
68 
VS/UWS 
Trauma Diffuse axonal 
injury 
6 
6 
7 
112102 
9 
132102 
17 
2 
9.74 
059 
M 
50 
VS/UWS 
Stroke 
L-frontal-temp
oro-parietal 
lobe damage 
3 
4 
6 
111102 
8 
222002 
27 
2 
7.01 
060 
M 
60 
MCS 
Trauma 
Bilateral 
brainstem, 
midbrain 
damage 
7 
4 
11 
134102 
11 
223112 
30 
2 
11.69 
061 
M 
44 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
2 
4 
6 
102102 
4 
002101 
13 
2 
10.48 
062 
F 
35 
VS/UWS 
Anoxia 
Bilateral-basal 
3 
5 
7 
211102 
9 
231102 
27 
2 
9.07


## Page 71


71 / 102 
 
ganglia 
damage 
063 
F 
43 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
2 
4 
7 
112102 
8 
202112 
29 
2 
10.09


## Page 72


72 / 102 
 
Appendix 1-table 2. Demographic and clinical characteristics of patients in the "Beijing_HDxt" dataset. 
patient 
alias 
gender 
age 
(years) diagnose 
etiology 
structural 
lesions on 
MRI 
time to 
MRI 
(months) 
number of 
CRS-R 
assessments 
CRS-R  
score 
at T0 
CRS-R 
subscore 
at T0 
CRS-R  
score 
at T1 
CRS-R 
subscore 
at T1 
follow-up
（months） GOS predicted 
score 
001 
M 
19 
VS/UWS 
Trauma 
L-temporo-pa
rietal lobe 
damage 
6 
4 
7 
112102 
22 
456223 
40 
4 
20.37 
002 
M 
26 
MCS 
Trauma 
R-thalamus, 
basal ganglia 
lesions 
3 
6 
10 
232102 
23 
456323 
47 
4 
17.12 
003 
F 
22 
VS/UWS 
Trauma 
L-temporal 
lobe damage 
4 
4 
6 
102102 
22 
456223 
47 
4 
14.05 
004 
M 
41 
VS/UWS 
Stroke 
Bilateral 
brainstem, 
midbrain 
damage 
3 
4 
6 
112101 
23 
456323 
50 
4 
20.23 
005 
M 
36 
MCS 
Stroke 
Bilateral 
brainstem 
damage 
4 
4 
6 
003102 
23 
456323 
39 
4 
7.75 
006 
M 
34 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
1 
4 
6 
111102 
14 
323123 
31 
3 
17.25 
007 
F 
18 
VS/UWS 
Trauma 
Diffuse axonal 
injury 
3 
4 
5 
012002 
14 
332123 
41 
3 
14.86


## Page 73


73 / 102 
 
008 
M 
58 
MCS 
Trauma 
R-frontal lobe 
damage 
12 
4 
8 
113102 
15 
333123 
40 
3 
15.62 
009 
M 
41 
MCS 
Trauma 
R-frontal-tem
poro-parietal 
lobe damage 
1 
5 
11 
233012 
18 
344223 
42 
3 
18.89 
010 
M 
46 
VS/UWS 
Stroke 
L-brainstem, 
cerebellar 
damage 
7 
4 
6 
102102 
14 
332123 
53 
3 
17.05 
011 
M 
25 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
4 
6 
6 
102102 
14 
224123 
46 
3 
18.07 
012 
M 
58 
VS/UWS 
Trauma 
L-brainstem 
damage 
1 
7 
7 
112102 
19 
355123 
40 
3 
10.75 
013 
M 
36 
VS/UWS 
Trauma 
L-frontal-tem
poro-parietal 
lobe damage 
6 
4 
7 
112102 
10 
232102 
44 
2 
9.58 
014 
M 
58 
VS/UWS 
Trauma 
R-frontal-tem
poro-parietal 
lobe damage 
4 
4 
6 
102102 
6 
102102 
45 
2 
6.69 
015 
M 
65 
VS/UWS 
Stroke 
Diffuse 
cortical & 
subcortical 
atrophy 
3 
4 
3 
100002 
5 
101102 
43 
2 
4.01 
016 
F 
24 
VS/UWS 
Trauma 
Diffuse axonal 
injury 
44 
6 
6 
102102 
8 
122102 
44 
2 
14.03


## Page 74


74 / 102 
 
017 
F 
46 
VS/UWS 
Stroke 
L-pons 
damage 
2 
4 
7 
112102 
7 
112102 
40 
2 
12.11 
018 
M 
53 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
3 
4 
4 
101002 
6 
102102 
41 
2 
5.38 
019 
F 
32 
VS/UWS 
Trauma 
L-temporo-pa
rietal lobe 
damage 
3 
4 
6 
102102 
8 
112202 
23 
2 
13.76 
020 
M 
41 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
2 
4 
4 
101002 
8 
112202 
40 
2 
12.06 
021 
F 
33 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
7 
5 
6 
211002 
11 
232202 
47 
2 
4.55 
022 
M 
49 
VS/UWS 
Anoxia 
Diffuse 
cortical & 
subcortical 
atrophy 
2 
4 
6 
102102 
6 
102102 
14 
2 
8.97 
023 
F 
25 
MCS 
Anoxia 
Bilateral 
thalamus, 
brainstem 
damage 
4 
7 
14 
450023 
10 
240022 
50 
2 
12.42 
024 
M 
63 
VS/UWS 
Stroke 
L-basal 
5 
4 
4 
001102 
5 
101102 
48 
2 
8.22


## Page 75


75 / 102 
 
ganglia 
lesions 
025 
M 
68 
VS/UWS 
Trauma 
L-frontal-tem
poro-parietal 
lobe damage 
2 
4 
5 
002102 
6 
012102 
47 
2 
9.72


## Page 76


76 / 102 
 
Appendix 1-table 3. Demographic and clinical characteristics of patients in the "Guangzhou_HDxt" dataset. 
patient 
alias 
gender 
age 
(years) 
diagnose etiology 
time to 
MRI(months) 
CRS-R 
score at T0 
CRS-R 
subscore at T0 
follow-up
（months） GOS 
predicted 
score 
001 
F 
15 
MCS 
Anoxia 
1 
13 
135112 
59 
4 
20.92 
002 
M 
29 
MCS 
Trauma 
4 
9 
114012 
61 
3 
16.50 
003 
F 
27 
MCS 
Trauma 
1 
9 
105102 
29 
3 
16.67 
004 
F 
20 
MCS 
Trauma 
2 
8 
113102 
41 
3 
20.37 
005 
M 
30 
MCS 
Trauma 
1 
15 
116223 
63 
3 
17.34 
006 
M 
31 
MCS 
Trauma 
1 
20 
445223 
51 
3 
14.00 
007 
M 
28 
VS/UWS 
Anoxia 
1 
5 
102002 
69 
2 
9.71 
008 
M 
48 
MCS 
Trauma 
1 
12 
234102 
55 
2 
9.11 
009 
M 
46 
VS/UWS 
Trauma 
2 
4 
102001 
65 
2 
12.58 
010 
M 
78 
VS/UWS 
Anoxia 
1 
4 
100102 
49 
2 
9.20 
011 
M 
39 
VS/UWS 
Anoxia 
1 
5 
002102 
51 
2 
4.20 
012 
F 
46 
VS/UWS 
Anoxia 
2 
4 
001102 
46 
2 
14.49 
013 
M 
39 
VS/UWS 
Anoxia 
2 
5 
102002 
43 
2 
7.30 
014 
M 
16 
VS/UWS 
Anoxia 
2 
3 
001002 
71 
2 
14.17 
015 
M 
25 
MCS 
Anoxia 
1 
12 
135102 
78 
2 
8.56 
016 
F 
76 
VS/UWS 
Anoxia 
5 
4 
100102 
59 
2 
3.57 
017 
M 
36 
VS/UWS 
Trauma 
2 
5 
001202 
65 
2 
17.28 
018 
M 
32 
VS/UWS 
Anoxia 
10 
6 
102102 
56 
2 
5.66 
019 
F 
49 
VS/UWS 
Anoxia 
1 
6 
102102 
49 
2 
4.55 
020 
F 
52 
VS/UWS 
Anoxia 
1 
3 
000102 
27 
2 
5.08 
021 
M 
62 
VS/UWS 
Anoxia 
2 
3 
001002 
28 
2 
10.26


## Page 77


77 / 102 
 
022 
F 
33 
VS/UWS 
Anoxia 
2 
6 
102102 
29 
2 
9.09 
023 
F 
28 
VS/UWS 
Anoxia 
9 
6 
102102 
67 
2 
12.62 
024 
F 
57 
VS/UWS 
Anoxia 
1 
5 
002102 
42 
2 
4.72


## Page 78


78 / 102 
 
Appendix 1-table 4. Demographic of healthy controls in the "Beijing_750" dataset. 
alias 
gender 
age 
handedness 
NC001 
F 
40 
Right 
NC002 
M 
50 
Right 
NC003 
F 
34 
Right 
NC004 
M 
25 
Right 
NC005 
M 
28 
Right 
NC007 
F 
24 
Right 
NC008 
F 
47 
Right 
NC009 
F 
22 
Right 
NC010 
F 
60 
Right 
NC012 
F 
26 
Right 
NC013 
M 
21 
Right 
NC014 
F 
27 
Right 
NC015 
M 
40 
Right 
NC016 
M 
44 
Right 
NC017 
F 
22 
Right 
NC018 
M 
50 
Right 
NC019 
M 
27 
Right 
NC020 
F 
43 
Right 
NC021 
F 
25 
Right 
NC022 
M 
54 
Right 
NC023 
F 
52 
Right 
NC026 
M 
46 
Right


## Page 79


79 / 102 
 
NC027 
F 
52 
Right 
NC028 
M 
29 
Right 
NC029 
F 
46 
Right 
NC030 
M 
44 
Right 
NC031 
M 
30 
Right 
NC032 
M 
31 
Right 
NC033 
M 
32 
Right 
NC034 
M 
30 
Right 
 
Appendix 1-table 5. Demographic of healthy controls in the "Beijing_HDxt" dataset. 
alias 
gender 
age 
handedness 
NC001_HDxt 
M 
44 
Right 
NC002_HDxt 
M 
42 
Right 
NC003_HDxt 
M 
30 
Right 
NC004_HDxt 
M 
40 
Right 
NC005_HDxt 
M 
30 
Right 
NC006_HDxt 
M 
30 
Right 
NC007_HDxt 
F 
58 
Right 
NC008_HDxt 
F 
54 
Right 
NC009_HDxt 
F 
41 
Right 
NC010_HDxt 
F 
41 
Right


## Page 80


80 / 102 
 
Appendix 2:  
Brain networks and regions of interest in this study.  
The six brain networks investigated in this study and the names of regions of interest 
(ROI). The Appendix 2 - table 1 represented the six brain networks, the name of ROIs, 
the peak coordinates in the Montreal Neurological Institute (MNI) space and the 
corresponding references. All of ROI were defined as a spherical region with a radius 
of 6mm at the center of the peak coordinates of the ROI. 
Appendix 2 - table 1: Brain networks and ROIs in this study. 
Brain Network 
ROI name 
ROI 
Abbreviation
Peak 
MNI 
coordinates 
References 
Default mode  
 
 
 
(Raichle, 
2011; 
Demertzi 
et 
al., 
2015) 
 
Anterior medial prefrontal cortex 
aMPFC 
-1 54 27 
 
 
Posterior cingulate cortex/precuneus 
PCC 
0 -52 27 
 
 
Left lateral parietal cortex 
L.LatP 
-46 -66 30 
 
 
Right lateral parietal cortex 
R.LatP 
49 -63 33 
 
Executive control 
 
 
 
(Seeley et al., 2007; 
Raichle, 2011) 
 
Dorsal medial PFC 
DMPFC 
0 27 46 
 
 
Left anterior prefrontal cortex 
L.PFC 
-44 45 0 
 
 
Right anterior prefrontal cortex 
R.PFC 
44 45 0 
 
 
Left superior parietal cortex 
L. Parietal 
-50 -51 45 
 
 
Right superior parietal cortex 
R. Parietal 
50 -51 45 
 
Salience 
 
 
 
(Seeley et al., 2007; 
Raichle, 
2011; 
Demertzi 
et 
al., 
2015) 
 
Left orbital frontoinsula 
L.AIns 
-40 18 -12 
 
 
Right orbital frontoinsula 
R.AIns 
42 10 -12 
 
 
Dorsal anterior cingulate 
dACC 
0 18 30 
 
Sensorimotor  
 
 
 
(Raichle, 
2011; 
Demertzi 
et 
al., 
2015) 
 
Left primary motor cortex 
L.M1 
-39 -26 51


## Page 81


81 / 102 
 
Brain Network 
ROI name 
ROI 
Abbreviation
Peak 
MNI 
coordinates 
References 
 
Right primary motor cortex 
R.M1 
38 -26 51 
 
 
Supplementary motor area 
SMA 
0 -21 51 
 
Auditory  
 
 
 
(Raichle, 
2011; 
Demertzi 
et 
al., 
2015) 
 
Left Primary auditory cortex 
L.A1 
-62 -30 12 
 
 
Right Primary auditory cortex 
R.A1 
59 -27 15 
 
 
Middle cingulate cortex 
MCC 
0 -7 43 
 
Visual 
 
 
 
(Demertzi 
et 
al., 
2015) 
 
Left primary visual cortex 
L.V1 
-13 -85 6 
 
 
Right primary visual cortex 
R.V1 
8 -82 6 
 
 
Left associative visual cortex 
L.V4 
-30 -89 20 
 
 
Right associative visual cortex 
R.V4 
30 -89 20


## Page 82


82 / 102 
 
Appendix 3:  
Brain functional network templates.  
Although the neurobiological implications of the spontaneous neuronal activity are 
not very clear, spontaneous fluctuations in the blood oxygenation level-dependent 
signal have been found to be coherent within a variety of functionally relevant brain 
regions, which are denoted as representing a "network". Moreover, several networks 
have been found to be spatially consistent across different healthy subjects 
(Damoiseaux et al., 2006). Researchers suggested that the brain networks assessed by 
resting state fMRI may reflect an intrinsic functional architecture of the brain (Raichle, 
2011). As mentioned in the manuscript, multiple networks were reported to be 
disrupted in the DOC patients. Here, the connection templates of the six brain 
networks were investigated within the healthy control group of the "Beijing 750" 
dataset. This study focused on the cortex, so six functional networks were investigated, 
including default mode network, executive control network, salience, sensorimotor, 
auditory, and visual network. Group functional connectivity maps for each of the six 
networks were created with a one-sample t test as shown the following Appendix 3 - 
figure 1. These templates were separately shown on the brain surface using the 
SurfStat toolbox (SurfStat, RRID:SCR_007081). The color bar represented T value.  
Appendix 3 - figure 1. The six brain functional network templates in this study.


## Page 83


83 / 102


## Page 84


84 / 102 
 
Appendix 4:  
Quality control for resting state functional connectivity. 
During the MRI scanning, the foam pad and headphones were used to reduce head 
motion and scanner noise. The normal controls were instructed to keep still with their 
eyes closed, as motionless as possible and not to think about anything in particular. 
The same instructions were given to the patients but due to their consciousness and 
cognitive impairments, we could not fully control for a prolonged eye-closed yet 
awake scanning session. The Appendix 4-figure 1 showed cumulative distribution of 
head motion per volume (framewise displacement) for normal controls and the 
patients. The Appendix 4-figure 2 showed the results of control quality of resting state 
fMRI in this study. The Appendix 4-figure 3 showed the histogram of the remaining 
number of fMRI volumes after scrubbing.


## Page 85


Appendix 4-figure 1. Cum
displacement) for normal
"Beijing 750" (A1), the te
"Guangzhou HDxt" (A3).
the DOC patients were sho
for the Guangzhou centre
within 1.5 mm for the vast
 
 85 / 102 
mulative distribution of head motion per volu
controls and DOC patients separately in the 
esting dataset "Beijing HDxt" (A2), and the
. The normal controls were shown in left co
own in right column. No healthy control data
e. In both patients and controls, head positio
t majority (>95%) of brain volumes. 
 
ume (framewise 
training dataset 
e testing dataset 
olumn, whereas 
a were available 
on was stable to


## Page 86


Appendix 4-figure 2. Co
distance between the ROIs
tend to vary with neuroan
quality control analyses 
Specifically, we compute
resting state functional co
neuroanatomical distance 
the testing dataset "Beijin
(B3). Smoothing curves (i
 86 / 102 
orrelations between motion artifact and n
s in this study. Prior studies have shown that m
atomical distance between brain nodes. Here
as described in the previous study (Power
d correlations between head motion (mean
nnectivity (RSFC) feature and plotted them a
(mm) for subjects in the training dataset "Bei
ng HDxt" (B2), and the testing dataset "Gua
n red) were plotted using a moving average f
neuroanatomical 
motion artifacts 
e, we conducted 
r et al., 2015). 
n FD) and each 
as a function of 
ijing 750" (B1), 
angzhou HDxt" 
filter.


## Page 87


Appendix 4-figure 3. His
scrubbing for each popu
HDxt" dataset (C2), and "G
 
 87 / 102 
stogram of the remaining number of fMRI
ulation, specifically "Beijing 750" datatset 
Guangzhou HDxt" dataset (C3). 
 
I volumes after 
(C1), "Beijing


## Page 88


88 / 102 
 
Appendix 5:  
Warped regions of interest and brain network templates. 
The conventional fMRI preprocess normalizes individual fMRI images into a standard 
space defined by a specific template image. This study generated a functional 
connectivity image for each patient in his/her own fMRI space. During the 
preprocessing of each patient’s fMRI scans, the 22 ROIs and the 6 brain network 
templates were spatially warped to individual fMRI space and resampled to the voxel 
size of the individual fMRI image. To ensure the registration, we developed some 
tools to visually check the transformed ROIs and brain network templates for each 
subject in this study. 
Supplementary file 1 illustrated some examples of the warped ROIs in the default 
mode network (DMN) for the 3 DOC patients with a GOS score 2,3,4, respectively. 
Additionally, as a reference, we showed these figures for one normal control. The 
ROIs in the DMN include the anterior medial prefrontal cortex (aMPFC), the 
posterior cingulate cortex/precuneus (PCC), the left lateral parietal cortex (L.LatP), 
the right lateral parietal cortex (R.LatP). The details about these 4 ROIs were listed in 
Appendix 2, and the brain network template of the DMN was provided in Appendix 3.


## Page 89


89 / 102 
 
Appendix 6:  
Correlations between imaging features and CRS-R scores at T1. 
Appendix 6 - table 1. The brain area connection features and their Pearson's 
correlations to the CRS-R scores at the T1 time point across the DOC patients in the 
training dataset "Beijing 750".  
 
 ROI name 
Pearson's correlation coefficient and p value 
** 
 DMN.aMPFC  
r= 0.514, p=0.000 
** 
 ExecuContr.L.Parietal  
r= 0.429, p=0.000 
** 
 DMN.PCC  
r= 0.420, p=0.001 
** 
 DMN.R.LatP 
r= 0.407, p=0.001 
** 
 ExecuContr.DMPFC 
r= 0.405, p=0.001 
 * 
 ExecuContr.R.Parietal  
r= 0.363, p=0.003 
 * 
 Sensorimotor.SMA  
r= -0.332, p=0.008 
 * 
 ExecuContr.R.PFC  
r= 0.320, p=0.011 
 * 
 Auditory.R.A1 
r= 0.315, p=0.012 
 * 
 DMN.L.LatP  
r= 0.298, p=0.018 
 * 
 ExecuContr.L.PFC 
r= 0.291, p=0.021 
 * 
 Sensorimotor.L.M1  
r= 0.267, p=0.035 
   
 Auditory.L.A1  
r= 0.206, p=0.105 
   
 Salience.R.AIns  
r= -0.187, p=0.142 
   
 Sensorimotor.R.M1  
r= 0.167, p=0.191 
   
 Visual.L.V4  
r= -0.151, p=0.236 
   
 Salience.dACC  
r= -0.104, p=0.418 
   
 Salience.L.AIns  
r= 0.075, p=0.560 
   
 Visual.R.V1 
r= 0.065, p=0.611 
   
 Auditory.MCC 
r= 0.053, p=0.682 
   
 Visual.R.V4  
r= -0.031, p=0.809 
   
 Visual.L.V1  
r= -0.028, p=0.830 
**: p<0.05, FDR corrected; *: p<0.05, uncorrected. 
In addition, Appendix 6 - figure 1 illuminated these brain area connection features and 
their Pearson's correlations to the CRS-R scores at the T1 time point.


## Page 90


Appendix 6 - table 2. Fun
to the CRS-R scores at t
dataset "Beijing 750".  
 
Functional connecti
**
DMN.aMPFC - Execu
   *
DMN.L.LatP - Visual.L
   *
Auditory.MCC - Visua
   *
ExecuContr.R.PFC - E
   *
ExecuContr.DMPFC -
   *
ExecuContr.L.PFC - Sa
   *
Sensorimotor.R.M1 -
   *
Sensorimotor.R.M1 -
   *
Salience.dACC - Visua
   *
ExecuContr.DMPFC -
   *
DMN.R.LatP - Visual.
   *
ExecuContr.L.Parieta
   *
DMN.aMPFC - Salien
   *
DMN.aMPFC - Senso
   *
DMN.aMPFC - DMN.
   *
ExecuContr.R.Parieta
   *
DMN.aMPFC - Senso
 90 / 102 
ctional connectivity features and their Pearso
the T1 time point across the DOC patients 
ivity 
Pearson's correlatio
and p value 
Contr.DMPFC  
 r= -0.489, p=0.000
L.V4  
 r= -0.421, p=0.001
al.R.V1  
 r= 0.375, p=0.002 
xecuContr.R.Parietal  
 r= 0.361, p=0.004 
Auditory.MCC  
 r= -0.351, p=0.005
alience.dACC  
 r= -0.335, p=0.007
- Sensorimotor.SMA  
 r= -0.330, p=0.008
- Auditory.L.A1  
 r= 0.319, p=0.011 
al.R.V1  
 r= 0.319, p=0.011 
Sensorimotor.L.M1  
 r= -0.310, p=0.013
R.V4  
 r= -0.306, p=0.015
l - Sensorimotor.L.M1  
 r= -0.302, p=0.016
nce.dACC  
 r= -0.292, p=0.020
orimotor.L.M1  
 r= -0.286, p=0.023
PCC  
 r= 0.275, p=0.029 
al - Visual.R.V4  
 r= -0.270, p=0.033
orimotor.R.M1  
 r= -0.268, p=0.034
 
on's correlations 
in the training 
n coefficient


## Page 91


*
ExecuContr.R.Parieta
   *
Sensorimotor.L.M1 -
   *
DMN.R.LatP - Sensor
   *
ExecuContr.R.Parieta
   *
Salience.dACC - Visua
   *
ExecuContr.DMPFC -
   *
DMN.aMPFC - Visual
   *
Salience.R.AIns - Sen
   *
DMN.L.LatP - Sensor
Specifically, the function
between any pair of ROIs.
the space limitations, o
significantly correlated to
p<0.05, FDR corrected; *:
In addition, Appendix 6 -
that were significantly cor
 
 
 
 91 / 102 
al - Sensorimotor.R.M1  
 r= -0.263, p=0.037
Sensorimotor.SMA  
 r= -0.261, p=0.039
rimotor.R.M1  
 r= -0.261, p=0.039
al - Visual.L.V4  
 r= -0.257, p=0.042
al.L.V4  
 r= 0.256, p=0.043 
Sensorimotor.R.M1  
 r= -0.255, p=0.043
l.L.V1  
 r= 0.251, p=0.047 
nsorimotor.L.M1  
 r= 0.250, p=0.049 
imotor.SMA  
 r= 0.248, p=0.050 
nal connectivity features were the function
. Since there were more than 200 functional c
only the functional connectivity features
o the CRS-R scores at the T1 time point w
: p<0.05, uncorrected. 
- figure 2 illuminated these functional conne
rrelated to the CRS-R scores at the T1 time po
nal connectivity 
connectivity, for 
s which were 
were shown. **: 
ectivity features 
oint.


## Page 92


Appendix 6 - figure 3 sho
Circos manner. The red li
while the blue links repre
of link was proportional to
 
 92 / 102 
owed these significant functional connectivi
inks represented the within-network function
sented the inter-network functional connecti
o the strength of functional connectivity. 
ity features in a 
nal connectivity, 
vity. The width


## Page 93


93 / 102 
 
Appendix 7:  
Histogram depicting the imaging features included in CARS-PLSR models. 
We resampled 1000 times with replacement from the training dataset "Beijing 750". In each bootstrap sampling set, the CARS-PLSR was used 
for imaging feature subset selection. We then summarized the number of each imaging feature that was included in the CARS-PLSR model. 
Appendix 7 - figure 1 shows the histogram depicting the imaging features included in CARS-PLSR models. The horizontal bar represents the 
number.


## Page 94


94 / 102


## Page 95


Appendix 8:  
Validations in healthy cont
To test robustness, we eva
to the normal controls (N
testing dataset "Beijing H
Guangzhou centre. Since t
calculated the subscores 
subscores to that of the D
subscores for all of the sub
the normal controls in th
network templates, and no
 
We found that (1) in th
significantly larger imagin
consciousness recovery a
 95 / 102 
trols. 
aluated whether the prognostic regression mo
NC) in the training dataset "Beijing 750" (n
HDxt" (n=10). No normal control data was a
the NC subjects did not have the clinical cha
only using the imaging features and then
DOC patients. Appendix 8 -figure 1 showe
bjects in the three datasets. We would like to 
he training dataset were only used to esta
ot used for any training. 
he training dataset "Beijing 750", the NC
ng subscores in comparison to both the DO
and the DOC patients with consciousness
odel generalized 
n = 30) and the 
available in the 
aracteristics, we 
n compared the 
ed the imaging 
emphasize that 
ablish the brain 
 
C subjects had 
C patients with 
s non-recovery


## Page 96


96 / 102 
 
(one-way ANOVA, p<0.05, multiple comparison corrected), and the DOC patients 
with consciousness recovery had significantly larger imaging subscores in comparison 
to the DOC patients with consciousness non-recovery (one-way ANOVA, p<0.05, 
multiple comparison corrected); (2) in the testing dataset "Beijing HDxt", the NC 
subjects had significantly larger imaging subscores in comparison to the DOC patients 
with consciousness non-recovery (one-way ANOVA, p<0.05, multiple comparison 
corrected), and the DOC patients with consciousness recovery had significantly larger 
imaging subscores in comparison to the DOC patients with consciousness 
non-recovery (one-way ANOVA, p<0.05, multiple comparison corrected); (3) In the 
testing dataset "Guangzhou HDxt", the imaging subscores of the DOC patients with 
consciousness recovery were significantly larger than the one of DOC patients with 
consciousness non-recovery (two-sample t-tests, p<0.05).


## Page 97


97 / 102 
 
Appendix 9:  
Variations across different sites. 
To investigate variations across different sites, we did two experiments using the 
normal control (NC) subjects in this study. First, we explored whether the predicted 
imaging subscores of the NC subjects were significantly different between the 
training dataset "Beijing 750" (n = 30) and the testing dataset "Beijing HDxt" (n=10). 
We found that there was no significant difference between the two groups 
(two-sample T test, p=0.24). The distribution is shown as the following Appendix 9 - 
figure 1. 
 
Second, we investigated the relationships between the fMRI signal-to-noise ratio 
(SNR) and the predicted imaging subscores. Different MRI acquisition protocols (e.g. 
scanner hardware, imaging protocols and acquisition sequences) can influence the


## Page 98


98 / 102 
 
imaging SNR. But, it is not trivial to estimate the SNR in resting-state fMRI, since the 
noise is complex and also differs spatially. Here, we calculated the temporal SNR 
(tSNR) as the ratio between the mean fMRI signal and its temporal standard deviation 
in each voxel (Welvaert and Rosseel, 2013), and then averaged across all voxels in 
each region of interest (ROI) (Gardumi et al., 2016; Hay et al., 2017). Since there 
were 22 ROIs in this study, the median of these 22 ROI tSNR values was used as the 
measure for evaluating the SNR of the fMRI. We then correlated the median tSNR 
with the predicted imaging subscores across all of the NC subjects (n=40), and found 
that there were significant correlations between them (Pearson's correlation r=0.36, 
p=0.024) as shown in the following Appendix 9 - figure 2. 
 
From the above two experiments, we found that (1) the fMRI tSNR could be one of 
influencing factors in the application of the presented model; (2) the predicted


## Page 99


99 / 102 
 
imaging subscores for the NC subjects could be approximate across different sites 
when the tSNR was proximity. Therefore, we suggested that our presented model can 
be applied to different centers, although the calibration might be required. Further, the 
tSNR in fMRI is not only associated with instrumental noise but also modulated by 
subject-related noise, such as physiological fluctuations and motion artifacts (Huettel 
et al., 2009). Therefore, we suggest that, on the one hand, the quality of imaging 
acquisition, including MRI scanner and imaging sequence/ parameters, need to be 
guarantee; on the other hand, scanning protocols is required to be standardized to 
reduce the subject-related noise during the scanning.


## Page 100


100 / 102 
 
Appendix 1-table 1. Demographic and clinical characteristics of patients in the 
"Beijing_750" dataset. 
 
Appendix 1 - table 2. Demographic and clinical characteristics of patients in the 
"Beijing_HDxt" dataset. 
 
Appendix 1 - table 3. Demographic and clinical characteristics of patients in the 
"Guangzhou_HDxt" dataset. 
 
Appendix 1 - table 4. Demographic of healthy controls in the "Beijing_750" dataset. 
 
Appendix 1 - table 5. Demographic of healthy controls in the "Beijing_HDxt" dataset. 
 
Appendix 2 - table 1: Brain networks and ROIs in this study. 
 
Appendix 3 - figure 1. Six brain functional network templates. 
 
Appendix 4 - figure 1. Cumulative distribution of head motion per volume (framewise 
displacement) for normal controls and DOC patients. 
 
Appendix 4 - figure 2. Correlations between motion artifact and neuroanatomical 
distance between the ROIs.


## Page 101


101 / 102 
 
Appendix 4 - figure 3. Histogram of the remaining number of fMRI volumes after 
scrubbing for each population. 
 
Appendix 6 - table 1. The brain area connection features and their Pearson's 
correlations to the CRS-R scores at the T1 time point across the DOC patients in the 
training dataset "Beijing 750". 
 
Appendix 6 - figure 1. The brain area connection features sorted by their Pearson's 
correlations to the CRS-R scores at the T1 time point in the training dataset "Beijing 
750". 
 
Appendix 6 - table 2. The functional connectivity features and their Pearson's 
correlations to the CRS-R scores at the T1 time point across the DOC patients in the 
training dataset "Beijing 750". 
 
Appendix 6 - figure 2. The functional connectivity features sorted by their Pearson's 
correlations to the CRS-R scores at the T1 time point across the DOC patients in the 
training dataset "Beijing 750". 
 
Appendix 6 - figure 3. The Circos map for the functional connectivity features that 
were significantly correlated to the CRS-R scores at the T1 time point across the DOC 
patients in the training dataset "Beijing 750".


## Page 102


102 / 102 
 
 
Appendix 7 - figure 1. Histogram depicting the imaging features included in 
CARS-PLSR models. 
 
Appendix 8 - figure 1. The imaging subscores for all of the subjects in the three 
datasets. 
 
Appendix 9 - figure 1. The distribution of the predicted imaging subscores of the 
healthy controls at different sites. 
 
Appendix 9 - figure 2. The correlations between the fMRI signal-to-noise ratio (SNR) 
and the predicted imaging subscores in the healthy controls.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1801_03268v3_prognostication_of_chronic_disorders_of_consciousness_using_brain_functional_net
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1801_03268V3_PROGNOSTICATION_OF_CHRONIC_DISORDERS_OF_CONSCIOUSNESS_USING_BRAIN_FUNCTIONAL_NET.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

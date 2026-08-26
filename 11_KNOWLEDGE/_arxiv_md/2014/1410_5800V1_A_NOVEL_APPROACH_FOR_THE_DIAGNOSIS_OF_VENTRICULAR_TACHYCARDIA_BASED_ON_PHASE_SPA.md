---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1410.5800v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1410.5800v1_A_novel_approach_for_the_diagnosis_of_ventricular_tachycardia_based_on_phase_spa

> Source: 1410.5800v1_A_novel_approach_for_the_diagnosis_of_ventricular_tachycardia_based_on_phase_spa.pdf

> Pages: 7

---


## Page 1


A novel approach for the diagnosis of ventricular tachycardia based 
on phase space reconstruction of ECG 
 
Koulaouzidis G1, Das S2, Cappiello G2, Mazomenos EB2, Maharatna K2, Morgan J1 
1 University Hospital Southampton NHS Foundation Trust, Southampton, UK 
2 School of Electronics and Computer Science, University of Southampton, UK 
 
 
 
 
Keywords: Space phase reconstruction, ventricular fibrillation, ventricular 
tachycardia 
 
 
Corresponding Author    
Koulaouzidis George 
University Hospital Southampton NHS Foundation Trust, Southampton, UK 
geokoul@hotmail.com


## Page 2


Ventricular arrhythmias comprise a group of disorders which manifest clinically in a 
variety of ways from ventricular premature beats (VPB) and no sustained ventricular 
tachycardia (in healthy subjects) to sudden cardiac death due to ventricular 
tachyarrhythmia in patients with and/or without structural heart disease.  
Ventricular fibrillation (VF) and ventricular tachycardia (VT) are the most common 
electrical mechanisms for cardiac arrest. Accurate and automatic recognition of these 
arrhythmias from electrocardiography (ECG) is a crucial task for medical 
professionals. The purpose of this research is to develop a new index for the 
differential diagnosis of normal sinus rhythm (SR) and ventricular arrhythmias, based 
on phase space reconstruction (PSR).  
PSR can map a time-series to a phase space trajectory in multi-dimensional space 
using a time delay embedding technique. PSR is a technique widely used to observe 
nonlinear behaviour of dynamical system and detect such small desynchronisation 
phenomena, which is difficult to identified, by simple observation (1-3). Over the last 
decade, PSR of ECG has been successfully used in a number of heart disease 
detection related applications (4-7).  
For the analysis we used 32 ECGs with sinus rhythm from the PTB Diagnostic ECG 
database and 32 ECGs from subjects with VT/VF from the Creighton University 
Ventricular Tachyarrhythmia Database. First, a reconstruction of phase portrait was 
performed with the method of delays. In this method, we insert a delay “τ” in the 
original time-series X(t) which produces a delayed version of X(t), the Y(t)=X(t-τ). 
Afterwards, the phase-space diagram is reconstructed by plotting Y(t) against X(t). 
Thereafter, the method of box counting was applied to analyse the behaviour of the 
phase trajectories, e.g. the number of trajectories and their spread. In this technique, 
the entire phase-space diagram is represented as an image of N×N pixel, where N is 
an integer (Fig 1). The pixels through which at least one trajectory has passed are 
considered as black boxes (nb) and the others are considered as white boxes (nw). The 
degree of complexity of the phase-space portraits is described using a metric, defined


## Page 3


as the ratio of the number of black boxes (nb) or pixels visited by the trajectories and 
the total number of pixels (nw+nb=N2). 
In this study, a different approach is suggested. Run-time statistical measures like 
mean (µ), standard deviation (σ) and coefficient of variation (CV = σ/µ), skewness (γ), 
kurtosis (β) for the box counting in phase-space diagrams are studied for a sliding 
window of 10 beats of ECG signal.  
When the subjects are in SR the phase portraits show regular structure, while during 
the VT/VF period the phase portraits show chaotic motion (Fig 1). In the 32 health 
subjects with SR, the analysis showed that µ and σ trends are almost uniform 
throughout the time. On the other hand, in the arrhythmic subjects both µ and σ 
showed sudden increase at the stage of VT/VF onset. In order to identify accurately 
the onset of arrhythmia, CV = σ/µ trends was introduced. CV is always bounded 
within an upper limit of CV<0.05, having values between >0 and <0.05. On the other 
hand, the arrhythmic subjects showed increase in CV, an increase that correlates with 
the onset of arrhythmia. During the arrhythmia the CV remained stable above the 
value of >0.05. It is worth to mention that after the appearance of a VPB the value of 
CV normalized after an initial increase. Therefore, the upper threshold was considered 
for the healthy subjects CVth=0.05. Similar pattern was observed also with the kurtosis, 
in which despite the inter-person variability in each case, the kurtosis crossed an 
upper limit of βth<6 several times which was considered as the cut-off point between 
subjects with SR and VT/VF. In order to optimise the accuracy of our diagnosis a new 
index ( J ) was proposed as a combination of the trends β and CV. 
                                                        


1
th
th
CV
J
w
w
CV





 
The upper normal limit of index J is the value of Jth =1, while the crossing of upper 
bounds 
th
CV  and 
th
 will be reflected in crossing of the threshold for the index of Jth 
=1. In the above equation the weight w  keep the balance in the impact of CV and β 
trends in index J. So in healthy subjects with equal weights on the two parts the w 
would be 0.5. While in the arrhythmic subjects, it is observed that the trends cross the 
critical threshold of 
1
J  at different time instants. For 
0
w 
the full emphasis is on


## Page 4


the kurtosis and with gradual increase of w , the impact of CV increases slowly and 
consequently impact of kurtosis decreases. With
1
w , the prediction index simply 
represented the CV trend. In this way the chance of misdiagnosis of arrhythmia has 
been minimized. 
In conclusion, we propose a novel statistical index for diagnosis of ventricular 
arrhythmia, using the phase-space reconstruction method of long-term ECG time-
series. We found that two thresholds CV<0.05 and kurtosis β<6 and the mixture of 
these in the proposed index
1
J  identified the SR from VA. Therefore, the index can 
be a beneficial clinical tool especially for physicians, general practitioners and 
medical staff with limited expertise in cardiology.


## Page 5


References 
1. Chan HL, Fang SC, Chao PK, Wang CL, Wei JD. Phase-space 
reconstruction of electrocardiogram for heartbeat classification. IFMBE 
Proceedings 2010; 25 (4); 1234-1237. 
2. Fojt O, Holcik J. Applying nonlinear dynamics to ECG signal processing. 
IEEE Engineering in Medicine and Biology Magazine, 1998; 17 (2); 96-
101. 
3. Ravelli F, Antolini R. Complex dynamics underlying the human 
electrocardiogram. Biological Cybernetics 1992; 67(1), 57-65. 
 
4. Karvounis EC, Tsipouras MG, Fotiadis DI. Detection of fetal heart rate 
through 3-d phase space analysis from multivariate abdominal recordings, 
IEEE Transactions on Biomedical Engineering 2009; 56 (5), 1394-1406. 
 
5. Amann A, Tratnig R, Unterkofler K. Detecting ventricular fibrillation by 
time-delay methods, IEEE Transactions on Biomedical Engineering 2007; 
54(1): 174-177. 
 
6. Sarvestani RR, Boostani R, Roopaei M. VT and VF classification using 
trajectoriy analysis, Nonlinear Anlaysis: Theory, Methods & Applications 
2009; 71 (12): 55-61. 
 
7. Roopaei M, Boostani R, Sarvestani RR, Taghavi MA, Azimifar Z. Chaotic 
based reconstructed phase space features for detecting ventricular 
fibrillation, Biomedical Signal Processing and Control, 2010; 5(4); 318-
327.


## Page 6


Fig 1. Black and white image of a window of ten beats for (a) normal looking ECG 
before arrhythmia (b) with VPB before arrhythmia, (c) VT, (d) VF. 
 
 
 
(a) 
 
 
 
 
(b) 
 
 
(c)  
 
 
 
 
(d)


## Page 7


Fig 2. Box counting mean and standard deviation trends for patient with healthy and 
arrhythmic patient respectively.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1410_5800v1_a_novel_approach_for_the_diagnosis_of_ventricular_tachycardia_based_on_phase_spa
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1410_5800V1_A_NOVEL_APPROACH_FOR_THE_DIAGNOSIS_OF_VENTRICULAR_TACHYCARDIA_BASED_ON_PHASE_SPA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

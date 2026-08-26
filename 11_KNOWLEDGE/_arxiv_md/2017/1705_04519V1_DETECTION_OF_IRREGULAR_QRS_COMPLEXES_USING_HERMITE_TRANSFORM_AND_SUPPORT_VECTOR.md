---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.04519v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1705.04519v1_Detection_of_irregular_QRS_complexes_using_Hermite_Transform_and_Support_Vector_

> Source: 1705.04519v1_Detection_of_irregular_QRS_complexes_using_Hermite_Transform_and_Support_Vector_.pdf

> Pages: 4

---


## Page 1


Detection of irregular QRS complexes using Hermite 
Transform and Support Vector Machine 
Zoja Vulaj, Miloš Brajović, Anđela Draganić, Irena Orović 
University of Montenegro, Faculty of Electrical Engineering  
Džordža Vašingtona bb, 81000 Podgorica, Montenegro 
email: zojavulaj@gmail.com 
 
 
Abstract - Computer based recognition and detection of 
abnormalities in ECG signals is proposed. For this purpose, the 
Support Vector Machines (SVM) are combined with the 
advantages of Hermite transform representation. SVM represent 
a special type of classification techniques commonly used in 
medical applications. Automatic classification of ECG could 
make the work of cardiologic departments faster and more 
efficient. It would also reduce the number of false diagnosis and, 
as a result, save lives. The working principle of the SVM is based 
on translating the data into a high dimensional feature space and 
separating it using a linear classificator. In order to provide an 
optimal representation for SVM application, the Hermite 
transform domain is used. This domain is proved to be suitable 
because of the similarity of the QRS complex with Hermite basis 
functions. The maximal signal information is obtained using a 
small set of features that are used for detection of irregular QRS 
complexes. The aim of the paper is to show that these features 
can be employed for automatic ECG signal analysis.  
Keywords – ECG; QRS complex; detection; classification; 
feature; SVM; Hermite transform 
I. 
 INTRODUCTION 
The electrocardiogram (ECG) represents the measure of the 
electrical activity of the heart over certain period time. The 
ECG signals are periodic in nature because they are 
characterized by a sequence of periodical waves. The most 
important part of ECG signals are the QRS complexes [1]. The 
phenomenon related to QRS complex is the depolarization of 
the ventricles. Based on the analysis of QRS complexes, 
different health diagnoses can be established.  
The analysis of recorded ECG data, especially in the case 
of patient monitoring, when a huge amount of ECG data is 
acquired, can be time-demanding. One such a case happens 
with patients affected by obstructive sleep apnea, which is the 
phenomenon of cessation of breathing during the sleep [2], [3]. 
The main reason of diseased people not being diagnosed with 
sleep apnea is because a cardiologist would be required to 
monitor the patient overnight. Because of this, the fast response 
to the demanding tasks and efficient analysis of ECG data 
becomes a challenge. For the purpose of making the work of 
cardiologist easier and decreasing the rate of undiagnosed (or 
improperly diagnosed) irregularities, computer based analysis 
of ECG signals are developed.  
Artificial Neural Networks (ANN) proved to be a useful 
tool for solving classification tasks. The SVM have shown 
good performances, as well. Their application includes a large 
variety of cases: voice recognition, verification of signatures, 
diagnosis in medicine and microbiology, and even in automatic 
translation machines [4]. In this paper, the ECG signal 
processing using Support Vector Machines (SVM) is 
presented.  The detection of abnormal QRS complexes is based 
on the recognition of two different data sets by comparing the 
features that are used to represent the data [4]. The basic 
features included into most classifications are the R peaks. 
When the R peaks are not sufficient for obtaining the desired 
results, new or additional features need to be used. Features can 
be divided into three types: temporal, morphological and 
statistical. Temporal features include the interval between the 
beats or the waves in ECG signals, as well as the heart rate. 
The heart rate is the key information for detecting arrhythmia. 
Morphological features characterize the morphology of the 
signal parts and are usually represented using coefficients 
obtained when the signal is decomposed into some 
transformation domain. Statistical features represent the 
statistical data of the signal (mean, maximum, minimum, etc). 
If all the features were used, their number would be so large 
that it would result in heavy computation. The difficulty faced 
during feature selection is to determine the right ones and the 
best combination of them. The features must be chosen such 
that the maximal signal information can be obtained from a 
small set of them. Consequently, different domains are used to 
achieve an optimal compact signal representation: the time 
domain, frequency domain, their combination, or some other 
domain [6]-[9]. Due to the similarity of the shapes of ECG 
signals and Hermite basis functions, in this paper QRS 
complexes are represented in the Hermite transform domain 
[10]. This transform domain is very suitable because the signal 
is presented using a small amount of coefficients while 
retaining the signal information. This fact indicates that the 
Hermite transform can be appropriate for ECG signal analysis, 
for either classification or abnormality detection. The selected 
features later represent the input of the classifier.  
The paper is organized as follows: In Section II the 
theoretical background on the Hermite transform (HT) is given. 
The theory behind the SVM is explained in Section III. In 
section IV the experimental results are presented. The 
concluding remarks can be found in Section V. 
II. 
THE HERMITE TRANSFORM  
ECG signals can be approximated with a reduced number 
of coefficients, while keeping the signal information. For this 
purpose, the Hermite transform domain is extensively exploited 
[6], [11], [12]. Consider an ECG signal ECG(t). Since we use 
QRS complexes, our target signal of interest can be defined as


## Page 2


( ),
QRS t
 where 
/ 2
t
T

 and T is the definition interval of the 
QRS signal. The Hermite functions can be expressed using 
Hermite polynomials. The n-th order polynomial is defined 
using equation (1): 
 
 
2
2
(
)
( )
( 1)
.
n
t
n
t
n
n
d
e
P t
e
dt


 
(1) 
The Hermite functions can be expressed as follows:  
 
2 ( )
( )
.
2
!
t
n
n
e
P t
H
t
n



 
(2) 
Since ECG signals (and in particular the QRS complexes) are 
continuous in time, in order to obtain an error-free 
approximation, the number of Hermite functions used in the 
signal expansion must be infinite. However, sampling both 
basis functions and signal at points tz, z = 0, …, M -1 
proportional to the roots of the Hermite polynomial (1), the 
Hermite expansion becomes a finite discrete transform of the 
analyzed signal. In this case each QRS complex can be 
uniquely represented as:  
 
1
0
( )
( )
M
z
n
z
n
QRS t
C H t




 
(3) 
with M being equal to the discrete signal length. The Hermite 
coefficients are denoted with 
n
C . It is crucial to use the points 
zt  in the calculation of Hermite basis functions. Note that the 
signal should be resampled at these points, if it is already 
uniformly sampled [12]. The following formula is used to 
calculate 
n
C and it is based on the Gauss-Hermite quadrature 
method [11]-[19]: 
 
2
1
2
2
2
1
1
1
2
!
(
( )
)
( )
( )
2
!
zt
S
S
n
z
n
z
n
z
S
z
S
C
QRS t e
P t
S P
t
n







 
(4) 
S is the number of samples of the signal 
( )
QRS t . It can be 
shown that under previous assumptions regarding the 
sampling points, S = N holds. By using equation (2) and the 
following expression:  
 
1
2
1
( )
( )
( )
n
n
z
N
z
N
z
H
t
t
H
t




 
(5) 
the simplified form of expression (4) is obtained: 
 
1
1
1
( )
( )
N
n
n
N
z
z
z
C
t QRS t
N





 
(6) 
III. 
THE SVM CLASSIFICATION BASED ON HERMITE 
TRANSFORM FEATURES 
Consider the data sets 
1
1
2
2
(
,
), (
,
), ..., (
,
)
n
n
d c
d c
d c
where 
n
d represents the input data and 
nc  are the class labels which 
can take two values: 1 or -1. The aim of an automatic 
classificator is to design a decision algorithm which sorts the 
input data points in the class that they belong to. In order to 
design a good classificator, the maximum-margin hyperplane 
has to be introduced. If the training data is linearly separable, 
two parallel hyperplanes can be selected so that the data points 
of each class meet the following set of expressions [4], [5], 
[21]: 
 
1, if
1
1, if
1
T
n
T
n
w d
b
c
w d
b
c






 
(7) 
w is the weight vector and b is the bias. The maximum-
margin hyperplane is the one that lies halfway between the 
two selected hyperplanes [4], [5]. The distance between the 
data points that belong to different data classes is denoted with 
l and expressed using equation (8): 
 
2
l
w

 
(8) 
 By maximizing the margin, the possibility to get classification 
errors is decreased. A maximal l is obtained when the 
denominator is minimal, respectively [4]: 
 
2
1
min 2 w
 
(9) 
where the requirement 
(
)
1
T
n
n
c w d
b

needs to be met. For 
the purpose of minimization, the Lagrange multiplier 
n
is 
introduced [19]. Now the optimization problem becomes as 
follows: 
 
1
max
2
T
n
n
m
n
m
n
m
c c d d





 
(10) 
Knowing that 
0
n

and 
0
n
nc



, by analyzing equation 
(10) the following expressions are obtained: 
   
 
,
,
0
n
n
n
T
sv
sv
sv
sv
w
c d
b
c
w d
d








 
(11) 
The values of 
sv
d
that meet 
0
sv


are the support vectors. 
The support vectors are the closest data points to the 
separating hyperplane and represent the main component of 
the decision function 
( )
f d [20]: 
 
( )
T
n
n
n
f d
c d d
b




 
(12) 
Using this function, the class label for each data point d can 
be determined. Every linearly separable data will be 
successfully separated by applying equation (12). But, each 
classification solution can further be improved to avoid 
ambiguity and misclassification due to the influence of noise 
or for the cases of data that cannot be separated successfully 
using the proposed solution. Therefore, two new variables are 
introduced: the regularization parameter P and . The 
optimization problem can be rewritten in the form [21]: 
   
 1
, where 
(
)
1
,
0
2
T
T
n
n
n
n
n
w w
P
c w d
b








 (13)


## Page 3


The Langrange multiplier introduced in equation (10) in this 
case can take values in the range [0, ]
P . The input training 
data becomes separable when translated to a higher 
dimensional space by defining 
T
n
m
d d
in terms of Kernel 
function 
(
,
)
n
m
K d d
. 
If we represent the signal of interest using equation (3) which 
is obtained when the signal is expanded in the Hermite 
transform basis, then the coefficients 
n
C are the features used 
in the classification. 
IV. 
EXPERIMENTAL RESULTS 
Two sets of data made of five signals each, are analyzed in 
this paper. One of the data sets contains the QRS complexes of 
healthy people represented in the Hermite transform domain, 
while the other data set is the Hermite transform representation 
of the irregular QRS complexes showing heart health 
anomalies.  
The performance of the proposed method for all the 
available data is shown on Figure 1. All the diseased QRS 
complexes are detected and classified correctly, including the 
most critic QRS complex which is zoomed in Figure 1. The 
diseased QRS complexes are marked in red, while the healthy 
ones are plotted in green. The support vectors are represented 
using circles. The accuracy of detection of irregular QRS 
complexes is 100%. However, if observed as a general 
classificator between healthy and irregular QRS complexes, 
then we might introduce the following terms: true positive 
(TP), true negative (TN), false positive (FP) and false negative 
(FN). The total number of QRS complexes is 161. The number 
of healthy QRS complexes is 72, out of which 35 are classified 
as healthy (TN) and the rest of them is misclassified (FP). All 
the irregular (diseased) QRS complexes are classified as 
diseased, which makes the number of correctly classified 
diseased QRS complexes (TP) 89. There are 0 false negatives 
(FN). As the aim of this paper is the detection of irregular i.e. 
diseased QRS complexes, any detection of this kind is referred 
to as positive. Now that all this information is obtained the 
efficiency of the proposed method for classification between 
healthy/regular and diseased/irregular complexes can be 
calculated as follows: 
 
TP+TN
89
35
100%
100%
77%
total
161





 
(14) 
The true positive rate can be expressed as follows: 
 
TP/total_diseased=1 
(15) 
while the rate of false positives is: 
 
FP/total_healthy=1.06 
(16) 
This false positive rate amount decreases the efficiency of the 
method for classification. The main factor that influences the 
rate of misclassification is the presence of noise: motion 
artifacts, baseline wander, electrode contacts, measurement 
equipment noise, etc. Signals should be acquired in specialized 
laboratories in order to test the performance of any 
classificator.  
 
Figure 1.  The detection of diseased QRS complexes 
However, if we take into account these facts, the proposed 
classificator can give satisfactory results. For some cases, it 
can classify the two data sets with 100% of accuracy as shown 
on Figure 2. Two signals from both classes are selected and 
analyzed. The pair of signals is processed and the steps are 
displayed within the figure. The time domains of signals are 
shown on the top sub-figures of the first and the last figures, 
while the bottom sub-figures represent the Hermite transform 
coefficients of all the detected QRS complexes belonging to 
the appropriate signals. Observe that the Hermite coefficients 
of QRS complexes belonging to healthy (left figure) and 
diseased (right figure) people, differ significantly which 
indicates their potential for feature generation. The second 
figure shows the output of the classificator for the observed 
signals. The presented case is classified correctly.  
V. 
CONCLUSION 
In this paper, the detection of irregular (diseased) QRS 
complexes using SVM is proposed. Two data sets were 
analyzed. One data set contains QRS complexes of healthy 
persons, while the other QRS complexes are irregular showing 
certain anomalies. To ensure fast data analysis and 
transmission, a reduced number of features is employed by 
representing the data in the Hermite transform domain. The 
performance of the proposed method is evaluated real-world 
signals. The method proved to be very efficient when used for 
detection of anomalies. The accuracy in this case is 100%. 
Future work could be oriented to decrease the number of 
misclassified healthy QRS complexes, which can be achieved 
by including, additional parts of ECG signals in the analysis 
and classification. 
ACKNOWLEDGMENT 
This work is supported by the Montenegrin Ministry of 
Science, project grant funded by the World Bank loan: CS-ICT 
“New ICT Compressive sensing based trends applied to: 
multimedia, biomedicine and communications”.


## Page 4


Figure 2. The classification healthy – diseased (first figure – Time domain waveform of healthy people ECG signal (top sub-figure) and Hermite coefficients of its 
QRS complexes (buttom sub-figure)), second figure – The performance of the classificatory, third figure – Time domain waveform of diseased people ECG signal (top 
sub-figure) and Hermite coefficients of its QRS complexes (buttom sub-figure))). 
REFERENCES 
[1] P. Laguna, R. Jané, S. Olmos, N. V. Thakor, H. Rix, P. Caminal 
“Adaptive estimation of the QRS complex wave features of the ECG 
signal by the Hermite model”, Med. Biol. Eng. Comput. , vol. 34, pp. 
58–68, 1996.  
[2] C. Varon, D. Testelmans, B. Buyse, J. A. K. Suykens, S. Van Huffel, 
“Sleep apnea classification using least-squares support vector machines 
on single lead ECG”. 
[3] L. Almazaydeh, K. Elleithy, M. Faezipour, “Detection of Obstructive 
Sleep Apnea Through ECG Signal Features”, Department of Computer 
Science and Engineering, University of Bridgeport, USA. 
[4] T. Fletcher, “Support Vector Machines Explained”, University College 
London, March 1, 2009. 
[5] S. M. Woo, H. J. Lee, B. J. Kang, S. W. Ban, “ECG Signal Monitoring 
using One-class Support Vector Machine”, Dongguk University, 
Proceedings of the 9th WSEAS International Conference on Applications 
of Electrical Engineering, ISSN: 1790-2769.  
[6] S. Stanković, I. Orović, E. Sejdić, Multimedia Signals and Systems: 
Basic and Advanced Algorithms for Signal Processing, Springer 2015  
[7] I. Orović, S. Stanković, “Time-frequency-based speech regions 
characterization and eigenvalue decomposition applied to speech 
watermarking”, EURASIP Journal on Advances in Signal Processing 
2010 (1), 572748  
[8] I. Orović, S. Stanković, T. Chau, C.M. Steele, E. Sejdić, “Time-
frequency analysis and Hermite projection method applied to 
swallowing accelerometry signals”, EURASIP Journal on Advances in 
Signal Processing 2010 (1), 323125  
[9] S. Stanković, I. Orović, L. Stanković, “Polynomial Fourier domain as a 
domain of signal sparsity”, Signal Processing, vol. 130, pp.243-253  
[10] P. Laguna, R. Janè, P. Caminal, “Adaptive Feature Extraction for QRS 
Classification and Ectopic Beat Detection”, Institut de Cibernetica, 
(UPC-CSIC), Barcelona, SPAIN, 1992 IEEE. 
[11] M. Brajović, I. Orović, M. Daković, S. Stanković, “Gradient-based 
signal reconstruction algorithm in the Hermite transform domain”, 
Electronics letters, vol. 52, no. 1, pp. 41-43. 
[12] M. Brajović, I. Orović, M. Daković, and S. Stanković, “On the 
Parameterization of Hermite Transform with Application to the 
Compression of QRS Complexes,” Signal Processing, in print, vol. 131, 
pp. 113-119, February 2017. 
[13] A. Sandryhaila, S. Saba, M. Puschel, J. Kovačević, “Efficient 
compression of QRS complexes using Hermite expansion”, IEEE Trans. 
Signal Process. 60 (2) (2012) 947-955. 
[14] A. Sandryhaila, J. Kovacevic, M. Puschel, “Compression of QRS 
complexes using Hermite expansion”, IEEE int. Conference on Acoust., 
Speech and Signal Process. (ICASSP), Prague, 2011, pp. 581-584. 
[15] J. B. Martens, “The Hermite transform - Theory”, IEEE Trans. 
Acoustics, Speech and Signal Process. 38 (9) (1990) 1595-1605. 
[16] S. Stanković, LJ. Stanković, and I. Orović, “Compressive sensing 
approach in the Hermite transform domain,” Mathematical Problems in 
Engineering, Volume 2015 (2015), Article ID 286590, 9 pages 
http://dx.doi.org/10.1155/2015/286590. 
[17] M. Brajović, I. Orović, and S. Stanković, “The Optimization of the 
Hermite transform: Application Perspectives and 2D Generalization,” 
24th Telecommunications Forum TELFOR 2016, November 2016 
[18] M. Brajović, I. Orović, M. Daković, and S. Stanković, “Representation 
of Uniformly Sampled Signals in the Hermite Transform Domain,” 58th 
International Symposium ELMAR-2016, Zadar, Croatia, September 
2016 
[19] A. Krylov, D. Kortchagine, “Fast Hermite projection method”, Int. Conf. 
on Image Analysis and Recognition, Portugal: 329-338, 2006.  
[20] H. Bisgin, O. U. Kilinc, A. Ugur, X. Xu, V. Tuzcu, “Diagnosis of long 
QT syndrome via support vector machines classification”, J. Biomedical 
Science and Engineering, 2011, 4, 264-271. 
[21] S. S. Mehta, N. S. Lingayat, “Support Vector Machine for Cardiac Beat 
Detection in Single Lead Electrocardiogram”, IAENG International 
Journal of Applied Mathematics, 36:2, IJAM_36_2_4. 
[22] Sambhu D., Umesh A. C., “Automatic Classification of ECG Signals 
with Features Extracted Using Wavelet Transform and Support Vector 
Machines”, International Journal of Advanced Research in Electrical, 
Electronics and Instrumentation Engineering, Vol. 2, Special Issue 1, 
December 2013, ISSN: 2278-8875.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
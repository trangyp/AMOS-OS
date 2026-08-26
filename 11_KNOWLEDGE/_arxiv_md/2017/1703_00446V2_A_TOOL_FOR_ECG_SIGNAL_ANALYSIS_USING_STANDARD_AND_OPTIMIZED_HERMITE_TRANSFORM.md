---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.00446v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1703.00446v2_A_tool_for_ECG_signal_analysis_using_standard_and_optimized_Hermite_transform

> Source: 1703.00446v2_A_tool_for_ECG_signal_analysis_using_standard_and_optimized_Hermite_transform.pdf

> Pages: 4

---


## Page 1


6th Mediterranean Conference on Embedded Computing          MECO’2017, Bar, Montenegro 
A tool for ECG signal analysis using standard and 
optimized Hermite transform  
Zoja Vulaj, Andjela Draganić, Miloš Brajović and Irena Orović  
University of Montenegro, Faculty of Electrical Engineering  
Džordža Vašingtona bb, 81000 Podgorica, Montenegro 
Emails: zojavulaj@gmail.com, andjelad@ac.me, milosb@ac.me, irenao@ac.me 
 
Abstract— The development of a system that would ease the 
diagnosis of heart diseases would also fasten the work of the 
cardiologic department in hospitals and facilitate the monitoring 
of patients with portable devices. This paper presents a tool for 
ECG signal analysis which is designed in MATLAB. The Hermite 
transform domain is exploited for the analysis. The proposed 
transform domain is very convenient for ECG signal analysis and 
classification. Parts of the ECG signals, i.e. QRS complexes, show 
shape similarity with the Hermite basis functions, which is one of 
the reasons for choosing this domain. Also, the information about 
the signal can be represented using a small set of coefficients in 
this domain, which makes data transmission and analysis faster. 
The 
signal 
concentration 
in 
the 
Hermite 
domain 
and 
consequently, the number of samples required for signal 
representation, can additionally be reduced by performing the 
parametrization of the Hermite transform. For the comparison 
purpose, the Fourier transform domain is also implemented 
within the software, in order to compare the signal concentration 
in two transform domains.  The application of the proposed 
method in clinical practice includes arrhythmia and heart failure 
detection, as well as other abnormalities of the cardiac rhythm.  
Keywords: 
ECG; 
QRS 
complex; 
Hermite 
transform; 
parametrization 
of 
the 
Hermite 
transform; 
Fast 
Fourier 
Transform;  
I. 
 INTRODUCTION  
The electrocardiogram (ECG) represents the changes of the 
electrical activity of the heart over time. By analyzing the ECG 
signals, the information about the medical condition of the 
heart is provided. Cardiologists can sometimes determine 
different abnormalities by observing the electrocardiogram. In 
some cases, when a high level of accuracy is required, different 
analysis implemented into an application can provide better 
results. Due to the specificity of this kind of signals, in 
everyday application we cannot always rely on the results of 
the application, but a supervision of cardiologist is required. 
The development of a system (electrocardiograph) that can 
work on its own was a great revolution in the world of 
cardiology [1]. Especially, in the cases of patients real-time 
monitoring, at home (portable devices) or in hospital, setting an 
alarm when certain conditions appear could save lives.  
ECG signals are periodic signals, because they are 
composed of a sequence of waves that repeat periodically in 
time: P wave, then Q, R and S waves (which form the QRS 
complex) and T wave. Very rarely, a U wave can also be 
detected. The most characteristic part of an ECG signal is the 
QRS complex [2]. Particularly, when analyzed and classified, 
the ECG signals are observed beat-to-beat. The kind of features 
and the number of signals included into the analysis depend on 
the type of classification, analysis we are willing to perform, 
and the results we need.  
Signals can be analyzed in different domains: time domain, 
frequency domain, or the combined time – frequency domain 
[3]-[6]. There are many different approaches for ECG signal 
analysis. The choice of domain depends on the requirement of 
the particular application and information that is necessary.  
In this paper, the software for ECG signal representation in 
different transform domains is proposed. Time domain, the 
Hermite transform (HT) and the Fourier transform (FT) domain 
representations are considered [7]. The HT is proven to be a 
better choice for ECG signal analysis compared to the 
commonly used FT [8], [9]. Particularly, the ECG signals, i.e., 
their QRS complexes have a similar shape as the Hermite basis 
functions. Therefore, it is shown that, by using the HT for the 
signal analysis, we can retain the signal information using a 
small amount of coefficients. By introducing two changeable 
parameters (time shift and scaling factor) the HT can further be 
advanced to meet the requirements of the signal processing. 
Therefore, by performing the optimization of the HT, the signal 
can be additionally sparsified.  
The paper is organized as follows: In Section II the 
theoretical background on the HT is given. The optimization of 
the HT is given in this section as well. Section III contains the 
description of the proposed software for the analysis of the 
ECG signals and its functionality. In Section IV the 
performance of the proposed software for different types of 
ECG signals is presented. The concluding remarks can be 
found in Section V.      
II. 
THEORETICAL BACKGROUND 
A. The Hermite transform 
To approximate ECG signals using a reduced number of 
coefficients, while retaining the accuracy, the Hermite basis 
functions are considered to be efficient due to the similarity of 
the ECG and Hermite waveforms. The Hermite functions can 
be defined in terms of the Hermite polynomials. The n-th order 
Hermite polynomial is given as follows:
 
 
2
2
(
)
( )
( 1)
n
t
n
t
n
n
d
e
HP t
e
dt
−
= −
⋅
, 
 (1) 
while the Hermite functions, in terms of the Hermite 
polynomial, are defined as:


## Page 2


6th Mediterranean Conference on Embedded Computing          MECO’2017, Bar, Montenegro 
 
2
( )
( ) /
2
!
t
n
n
n
HF t
e
HP t
n
π
−
=
 . 
(2) 
Generally, in the case of signals that are continuous in time, an 
infinite number of Hermite functions is required in order to 
approximate the signal without an error. In real application, 
the finite number Hermite functions have to be used. As we 
denoted these functions by 
( )
n
HF t , the signal can be defined 
using the Hermite expansion as follows:  
 
1
0
( )
( )
M
n
n
n
ECG t
Coeff HF t
−
∧
=
= ∑
 
(3) 
where M is the number of functions used to represent the 
signal in the HT basis and it can be smaller than the signal 
length. For ideal signal approximation, the number of Hermite 
functions should be equal to the signal length N. In the 
discrete domain, the functions are calculated in the roots of the 
Hermite polynomials [10],[11]. The Hermite coefficients 
Coeff can be calculated using the Hermite polynomials, based 
on the Gauss-Hermite quadrature method [11]-[16] as: 
(
)
2
1
/2
2
2
1
1
1
2
!
( )
( )
( )
2
!
z
N
N
t
n
z
n
z
n
z
N
z
N
Coeff
ECG t e
HP t
N HP
t
n
π
π
−
=
−
=
∑
 (4) 
The parameter 
zt  represent the zeros of the polynomials, 
while N is the number of samples of the signal 
( )
ECG t . The 
expression for the Hermite coefficients can be significantly 
simplified if we implement the Hermite functions: 
 
1
1
1
( ) ( )
M
n
n
M
z
z
z
Coeff
t
f t
M
α
−
=
≈
∑
, 
(5) 
where: 
 
2
1
1
( )
( ) / (
( ))
n
M
z
n
z
M
z
t
HF t
HF
t
α
−
−
=
. 
(6) 
B. The parametrization of the Hermite transform 
The Hermite function can be defined by introducing the 
scaling factor δ, used to match functions to the signal, by 
stretching or compressing them [8]: 
 
2
2
/2
( , )
( /
) /
2
!
t
n
n
n
HF t
e
HP t
n
δ
δ
δ
δ
π
−
=
. 
(7) 
Beside the scaling factor, the functions can be shifted in 
time to get the optimal concentration in the HT domain. The 
rule that we use when determining these parameters in order to 
get the optimal signal concentration, is based on the 
1ℓ-norm. 
The value of the scaling factor, is determined experimentally. 
The signal expansion equation, in this case can be written as: 
 
1
0
( )
( , )
M
n
n
n
ECG t
Coeff HF t δ
−
=
= ∑
. 
(8) 
The Gauss-Hermite quadrature equation for calculation of the 
Hermite coefficients, becomes [11]-[14]: 
2
1
1
( , )
1
( ),
0,1,...,
1
[
( , )]
N
z
n
z
z
N
z
HF t
Coeff
ECG t
n
N
N
HF
t
δ
δ
=
−
=
=
−
∑
(9) 
Signals that are being represented by using the HT, are 
usually sampled at points that are proportional to the Hermite 
polynomials roots and those points are not uniformly 
distributed. To obtain the values at the non-uniform points, the 
interpolation is used [8]:        
 
sin( (
) /
)
( )
(
)
,
1,...,
(
) /
C
s
s
n
C
s
t
n t
t
ECG t
ECG n t
s
N
t
n t
t
π
π
=−
−∆
∆
≈
∆
=
−∆
∆
∑
, (10) 
ts are the sampling points, while 
t
∆ is the sampling period. 
 
The idea of scaling factor optimization procedure relies on 
the concentration measure of the Hermite coefficients Coeff. 
Namely, a suitable value of the scaling factor δ is chosen so 
that the vector of Hermite coefficients is as sparse as possible. 
Here, the 
1ℓ-norm of transform coefficients plays the main 
role. In the case of the HT, this norm can be calculated as 
follows: 
 
1
1
0
N
n
n
Coeff
Coeff
−
=
= ∑
 
(11) 
The optimal value of δ can now be determined as: 
 
1
arg min Coeff
δ
δ =
 
(12) 
Using equation (12) we have determined the range of the 
possible values of the scaling factor. The value that minimizes 
the concentration measure is optimal. On the other side, the 
shift parameter τ used to move the signal for a few samples 
left or right relative to the zero time instant, can be also 
considered when searching for an optimal δ. The optimization 
is done for every possible value of the τ from the set [τmin, τmax], 
and a measure vector L is formed. The optimal shift τ is the 
one that meets the following equation: 
 
argmin L
τ
τ =
. 
(13) 
III. 
THE SOFTWARE TOOL FOR THE ECG SIGNAL ANALYSIS 
The Graphical User Interface (GUI), i.e., the software tool 
for the representation of ECG signals and QRS complexes, is 
designed in Matlab 7. The outlook of the software is displayed 
in Figure 1. It contains two panels, Healthy and Diseased, for 
the presentation of two different classes of signals, from two 
different data sets. The two groups of signals contain nine 
different test signals (each), and these could be chosen from the 
dropdown menu.  
 
Figure 1.  The Virtual Instrument 
The chosen test signals can be plot using the button ‘Plot 
signals’ – the time domain of the peaks is represented. The


## Page 3


6th Mediterranean Conference on Embedded Computing          MECO’2017, Bar, Montenegro 
 
Figure 2. The Healthy and Diseased sub-GUIs 
peaks axes give us the preview of the extracted peaks for the 
selected signals. Using the buttons ‘Next’ and ‘Previous’, the 
user can switch among the peaks. On Figure 1, buttons 
‘Healthy’ and ‘Diseased’ are also marked. When these buttons 
are clicked, two sub-GUIs are called (Figure 2). Each of them 
displays the result of the analysis for the selected signal and 
peak that belongs to the appropriate signal class. The sub-GUI 
‘Healthy’, as well as the ‘Diseased’ one, contain two panels: 
HT and FT. The panel HT calculates and displays the 
coefficients of the HT and the coefficients of the optimized HT 
in the lower axes of the HT panel (Figure 2.). Both types of 
coefficients, are plot within the same axes, to make the 
difference between them more noticeable and the comparison 
of the proposed methods easier. In the upper axes of the same 
panel on the appropriate sub-GUIs, the representation of the 
chosen signal part in the Hermite domain, along with the same 
signal but shifted in time, are shown. In each sub-GUI a sub-
panel for the definition of the parameters used in calculating 
the HT, as well as the optimized HT, is also implemented. 
After the changes of these parameters, as well as the changes of 
the signals and desired peaks, the graphics are updated if button 
‘Update’ is clicked. The panel FT contains the axes in which 
the graphical result of the selected peak is shown when the 
Fourier transform domain is implemented.  
When speaking of the sets of signals used for this analysis, one 
of the data sets contains the signals and their R peak locations 
of healthy people, while the other is the data set of the 
diseased. QRS complexes in ECG signals of healthy and 
diseased people differ in duration, amplitude and morphology. 
Depending on these characteristics, the accurate diagnosis of 
diseases can be established. The extraction of QRS complexes 
is based, firstly, on the detection of R peaks. For the detection 
of certain diseases, such as arrhythmia, this information is 
sufficient. On the other side, when more information is 
required, it is still based on the R peak since more information, 
as a rule, means more sampling points around R peak. The 
number of sampling points, in the presented GUI, can be input 
by the user in the appropriate field shown on Figure 1. This is 
implemented in order to compare the changes in the HT and FT 
when different segments of ECG signals are used.  
IV. 
EXPERIMENTAL RESULTS 
The performance of the main GUI is shown in Figure 3. For 
the purpose of this analysis, two randomly selected signals are 
plot and the first peaks are analyzed. After the buttons 
‘Healthy’ and ‘Diseased’ are clicked, the sub-GUIs are started 
(Figure 5.). In the panel HT the graphical results of the 
calculations in the Hermite transform domain are displayed. 
The coefficients of the HT (marked in blue) and the 
coefficients of the optimized HT (marked in magenta), are plot 
within the same axes in order to visually enhance the effects of 
the HT optimization. The representation of the chosen signal 
part in the Hermite domain, is also plotted using a blue filled 
line, along with the preview of the same signal but in magenta 
and with a certain shift which can be defined by the user. The 
desired amount of shift, can be input within the same panel. In 
Figure 4. the changes in the HT and the optimized Hermite 
transform, for different cases of signal shifting are presented. 
    
 
Figure 3. The performance of the instrument 
 
As we can see from the figures, for τ=1 the signals almost 
overlap in time and the QRS complex, using the parametrized


## Page 4


6th Mediterranean Conference on Embedded Computing          MECO’2017, Bar, Montenegro 
HT, is represented with the two strongest among all the 
available coefficients, while retaining the desired accuracy. As 
we increase the time shift, the values of the coefficients drop 
significantly but more coefficients need to be used in order to 
maintain the same accuracy.  The effect of different values of 
the scaling factor δ on the coefficients of the parametrized HT 
(the signal chosen from the class of the diseased presented in 
Figure 3.) are shown on Figure 5. In order to get a better 
optimization of the HT, two values of the scaling factor are 
introduced, δ0 and δmax. These values can be also defined by the 
user in the fields ‘Define parameters’, shown in Figure 2. The 
optimal δ is then searched in the range: 
 
0
max
: 0.1:
δ
δ
δ
=
 
(14) 
The step parameter 0.1 is used for the scaling factor 
optimization [17]. The optimal δ is the one that enhances the 
coefficients concentration and meets the sparsity requirements. 
Note that not every signal will have the same optimal scaling 
factor even if it belongs to the same signal group, and for each 
signal there is a certain range of values that δ can take.    
 The FT panel, represents the signal in the Fourier 
transform domain. This domain is also implemented for the 
comparison with the HT based analysis method. The button 
‘Update’ is used to update the graphics when the user is willing 
to change the parameters of the analysis. 
 
 
Figure 4. The effect of time shift (the left figure (τ=1) and the right figure 
(τ=10)). 
 
 
Figure 5. The effect of the scaling factor (first row- left fig. (δ0=1; δmax=10), 
right fig. (δ0=1; δmax=5); second row (δ0=1; δmax=3). 
V. 
CONCLUSION 
 In this paper, the tool implementing the Hermite transform 
domain is proposed for analysis and representation of the ECG 
signals, namely their QRS complexes. For the comparison 
purpose, the Fourier transform is also implemented. The 
optimization of the Hermite transform is included in the tool, in 
order to choose suitable shift and scaling parameters. Further 
research could be oriented to implementing the proposed 
method for signal classification.  
ACKNOWLEDGMENT  
This work is supported by the Montenegrin Ministry of 
Science, project grant funded by the World Bank loan: CS-
ICT “New ICT Compressive sensing based trends applied to: 
multimedia, biomedicine and communications”. 
REFERENCES 
[1] A. Gil, G. Caffarena, D. G. Márquez, A. Otero, “Hermite Polynomial 
Characterization of Heartbeats with Graphics Processing Units”, 
University of Santiago de Compostela, Spain. 
[2] P. Laguna, R. Jané, S. Olmos, N. V. Thakor, H. Rix, P. Caminal 
“Adaptive estimation of the QRS complex wave features of the ECG 
signal by the Hermite model”, Med. Biol. Eng. Comput. , vol. 34, pp. 
58–68, 1996. 
[3] S. Stanković, I. Orović, E. Sejdić, Multimedia Signals and Systems: 
Basic and Advanced Algorithms for Signal Processing, Springer 2015 
[4] I. Orović, S. Stanković, “Time-frequency-based speech regions 
characterization and eigenvalue decomposition applied to speech 
watermarking”, EURASIP Journal on Advances in Signal Processing 
2010 (1), 572748 
[5] I. Orović, S. Stanković, T. Chau, C.M. Steele, E. Sejdić, “Time-
frequency analysis and Hermite projection method applied to 
swallowing accelerometry signals”, EURASIP Journal on Advances in 
Signal Processing 2010 (1), 323125 
[6] S. Stanković, I. Orović, L. Stanković, “Polynomial Fourier domain as a 
domain of signal sparsity”, Signal Processing, vol. 130, pp.243-253 
[7] P. Laguna, R. Jané, P. Caminal, “Adaptive Feature Extraction for QRS 
Classification and Ectopic Beat Detection”, Institut de Cibernetica, 
(UPC-CSIC), Barcelona, SPAIN, IEEE 1992. 
[8] M. Brajović, I. Orović, M. Daković, and S. Stanković, “On the 
Parameterization of Hermite Transform with Application to the 
Compression of QRS Complexes,” Signal Processing, in print, vol. 131, 
pp. 113-119, February 2017. 
[9] O. A. Kuruş, N. Kiliç, O. N. Uçan, “Hermitian transform approach in 
classification of ECG signals”, İstanbul Aydın Üniversitesi Dergisi. 
2013, 2(7):89-101 
[10] S. Stanković, LJ. Stanković, and I. Orović, “Compressive sensing 
approach in the Hermite transform domain,” Mathematical Problems in 
Engineering, Vol. 2015 (2015), Article ID 286590, 9 pages 
[11] M. Brajović, I. Orović, M. Daković, S. Stanković, “Gradient – based 
signal reconstruction algorithm in the Hermite transform domain, 
Electronics letters, vol. 52, no. 1, pp. 41-43. 
[12] A. Sandryhaila, S. Saba, M. Puschel, J. Kovacevic, “Efficient 
compression of QRS complexes using Hermite expansion”, IEEE Trans. 
Signal Process. 60 (2) (2012) 947-955. 
[13] A. Sandryhaila, J. Kovacevic, M. Puschel, “Compression of QRS 
complexes using Hermite expansion”, IEEE int. Conference on Acoust., 
Speech and Signal Process. (ICASSP), Prague, 2011, pp. 581-584. 
[14] L. R. L. Conte, R. Merletti, G. V. Sandri, “Hermite expansion of 
compact support waveforms: Application to myoelectric signals”, IEEE 
Trans. Biomedical Engineering 41 (12) (1994) 1147-1159. 
[15] J. B. Martens, “The Hermite transform - Theory”, IEEE Trans. 
Acoustics, Speech and Signal Process. 38 (9) (1990) 1595-1605. 
[16] A. Krylov, D. Kortchagine, “Fast Hermite projection method”, Int. Conf. 
on Image Analysis and Recognition, Portugal: 329-338, 2006. 
[17] M. Brajović, I. Orović, and S. Stanković, “The Optimization of the 
Hermite 
transform: 
Application 
Perspectives 
and 
2D 
Generalization,”  TELFOR 2016, Belgrade, Serbia

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
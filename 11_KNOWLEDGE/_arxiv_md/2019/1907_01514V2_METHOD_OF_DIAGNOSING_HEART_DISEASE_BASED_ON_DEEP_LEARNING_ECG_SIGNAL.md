---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.01514v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1907.01514v2_Method_of_diagnosing_heart_disease_based_on_deep_learning_ECG_signal

> Source: 1907.01514v2_Method_of_diagnosing_heart_disease_based_on_deep_learning_ECG_signal.pdf

> Pages: 9

---


## Page 1


1 
Method of diagnosing heart disease based on deep learning ECG sign 
Jie Zhang1 #, Lian Zou1 *, Bohao Li1, Kexin Xiang1, Xuegang Shi1, Cien Fan1 and Yifeng Liu2* 
1 School of Electronic Information,Wuhan University 
Wuhan,430072,  China 
2China Academy of Electronics and Information Technology, 
Beijing 100041, China 
*zoulian@whu.edu.cn 
#2016301200121@whu.edu.cn 
 
The state-of-the-art method to classify heart rhythms by electrocardiogram (ECG) is to combine 
cardiology and signal processing method. The classification accuracy has been improved using deep 
learning models, but it still can’t meet clinical needs. In this work, we propose a novel method to 
predict heart diseases from ECG signals with cardiology, signal processing methods and deep 
learning model. Firstly, we transform ECG signal into time-frequency diagram with wavelet 
transformation and cardiology. Then time-frequency diagram is then classified via a deep 
convolution network. Combing the advantages of signal processing method and deep learning 
methods, our method greatly improves classification accuracy. Extensive experiments show that our 
method achieved 0.87 F1-score (outperforming the best baseline by 0.11) in the 2017 
PhysioNet/Computing-in-Cardiology Challenge for arrhythmia detection from single lead ECG 
classification. Our method also achieves state-of-the art result on different data sets, which 
demonstrates its robustness. 
 
Keywords: Electrocardiogram; Deep learning; Neural Network; Wavelet transform. 
 
1.   Introduction 
Cardiovascular disease is the leading cause of death world-wide and the 
electrocardiogram (ECG) is a major tool in the diagnose26. Compared to determining 
whether ECG is normal or not, diagnosing heart disease is a more challenging task. 
Traditional ECG signal analysis and classification relies on the guidance of experienced 
medical experts, which is a time-consuming and labor-consuming job. Therefore, there is 
a growing need for fully automated ECG analysis using computer.


## Page 2


The difficulty in analyzing ECG is feature extraction. Current classification systems 
extract medical feature by signal processing means2 3 4 5 8. To classify the ECG, systems 
integrate the features and compare them with features extracted from various heart disease. 
However, due to noise interference, some features are difficult to extract12. Because ECG 
signals of different Cardiovascular disease have different features, it is impossible to design 
a system that can extract all the required features. This makes each diagnostic system poor 
scalability and low accuracy.  
Recently, the deep learning technique has emerged as a promising solution for ECG 
interpretation1 6 9 25. Deep convolutional neural networks extract features automatically 
from the original images / signals23 18. Due to its high performance in automated 
classification, deep neural networks based ECG interpretation becomes progressively 
promising. For example, Pranav Rajpurkar16 used a deep neural network to detect 
arrhythmias by the method of training a 34-layer convolutional neural network (CNN). 
Antônio H. Ribeiro and his research team used convolutional neural network a model for 
predicting electrocardiogram (ECG) abnormalities in short duration 12-lead ECG signals17. 
Although the two approaches mentioned above have their own advantages, the 
practical computer interpreted ECGs in clinical use have limitations in diagnostic accuracy 
and require human review and secondary interpretation. Given this, one might expect a 
complex method is required to achieve good results19. However, we show that a 
surprisingly simple and fast system can surpass prior state-of-the-art ECG classification 
results. 
To solve the above problems, we propose a novel method to predict heart diseases 
from ECG signals with cardiology, signal processing methods and deep learning model. 
As shown in Figure1, the proposed system composes of two main parts: pre-processing 
module and a neural network architecture to classify heart rhythms. The pre-processing 
module first extracts feature waves of ECG signals using cardiology knowledge and signal 
processing methods. Then through the wavelet transformation, the 1-D feature waves are 
converted into 2-D time-frequency diagrams. In fact, the time-frequency diagrams are 
coefficient matrix of wavelet transformations at different scales. In this way, we can 
simultaneously analyze the time-frequency features of signals at different scales. The deep 
neural network extracts deep features of time-frequency diagrams and predict heart disease.  
Our consolidated contribution is three-fold.  
1) we extract feature waves using cardiology knowledge and signal processing method. 
This method reduces the amount of computation while preserving the signal 
characteristics, which lead to better accuracy and faster execution.  
2) we use wavelet transformation to convert 1-D signals into 2-D images, which allows 
deep learning model to simultaneously analyze the characteristics of different 
frequency bands of the signal5 11 13.  
3) we take full advantage of cardiology, signal processing methods and deep learning 
model, which demonstrated the robustness and achieved state-of-the art result.  
The structure of this paper is as follows: in Section 2, we will focus on introducing our 
basic theory; in Section 3, we will discuss our experimental results. Finally, we will 
summarize our method in Section 4.


## Page 3


2.   Methodology 
Fig.1 illustrates our proposed system architecture. Since the variety of noise types may 
interfere the classification results, we preprocess the noise to improve accuracy and 
stability. First the raw ECG signals are filtered. Then, we extract R-waves in ECG using 
PT algorithm. According to the cardiology knowledge that the number of R-waves should 
be within a certain range, abnormal signals are replaced with zero sequences. This method 
can reduce the interference of noise to the classification of normal signals. Then, we extract 
a sequence containing four complete cardio cycles from each signal as feature wave. 
Afterwards, wavelet transformations of different scales are used to convert feature waves 
into time-frequency diagrams. Time-frequency diagrams are classified by convolutional 
neural networks. 
 
 
 (a) 
 
(b) 
Fig.1. Overall frame diagram. (a) Time-frequency diagram conversion. 
 (b) the framework of classification network. 
 
2.1 Noise removal filtering 
Our system classifies heartbeat from single-lead electrocardiogram (ECG), which is 
a very weak low-frequency physiological signal. The movement of the electrodes, poor 
contact between the electrodes and the skin or other physiological electrical signals may 
interfere with the measured ECG signals, that causes the raw ECG signals to contain noise 
signals21 22. The frequency of ECG signals is between 0.5-100Hz and mainly concentrated 
between 3~35Hz21. Therefore, based on our study of noise signals, we designed a six-order 
Butterworth low-pass filter to filter out the high-frequency noise of the original ECG signal. 
2.2 Feature wave extraction


## Page 4


Since the length of original ECG signals is a little long at the sampling frequency of 
200Hz and not the same, it is very difficult to process the signals further. Besides, the 
diversity of noise signals may interfere with the signal classification. Therefore, we 
designed a method to extract feature waves of each ECG that can preserve signal 
characteristics while reducing interference of noise. 
2.2.1 R wave extraction 
A normal ECG signal contains P, Q, R, S, T waves and heart disease may cause some 
waves to disappear in ECG15. For example, Atrial fibrillation (AF) may cause the 
disappearance of P waves. However, we find out that heart diseases generally do not result 
in the disappearance of R waves20. Therefore, we determine whether the signal is noise or 
not according to the number of the R waves.  
We extract R waves with the modified Pan-Tompkins algorithm14. First an integer-
coefficient band-pass filter is composed of cascaded low-pass and high-pass filters. Its 
function is noise rejection. Next a filter approximates a derivative. After an amplitude 
squaring process, the signal passes through a moving-window integrator. Adaptive 
thresholds then discriminate the locations of the QRS complexes. 
The band-pass filter reduces the influence of muscle noise, 60 Hz interference, 
baseline wander, and T-wave interference. The desirable passband to maximize the QRS 
energy is approximately 5-15 Hz. For our chosen sample rate, we could not design a band-
pass filter directly for the desired passband of 5-15 Hz using this specialized design 
technique. Therefore, we cascaded the low-pass and high-pass filters described below to 
achieve a 3 dB passband from about 5-12 Hz, reasonably close to the design goal. 
The transfer function of the second-order low-pass filter is: 
 
𝐻𝑙𝑝(𝑧) = (1 −𝑧−6)2
(1 −𝑧−1)2 
(1) 
The amplitude response is: 
 
|𝐻(𝜔𝑇)| = 𝑠𝑖𝑛2(3𝜔𝑇)
𝑠𝑖𝑛2(𝜔𝑇/2) 
(2) 
 
Where T=200 is the sampling period. 
The design of the high-pass filter is based on subtracting the output of a first-order 
low-pass filter from an all-pass filter. The transfer function for such a high-pass filter is: 
 
𝐻(𝑧) = (−1 + 32𝑧−16 + 𝑧−32)
(1 + 𝑧−1)
 
(3) 
The amplitude response is: 
 
|𝐻(𝜔𝑇)| =
[256 + 𝑠𝑖𝑛2(16𝜔𝑇)]1 2
⁄
𝑐𝑜𝑠(𝜔𝑇/2)
 
(4) 
 
After filtering, the signal is differentiated to provide the QRS complex slope 
information. We use a five-point derivative with the transfer function: 
 
𝐻(𝑧) = (1/8𝑇)(−𝑧−2 −2𝑧−1 + 2𝑧1 + 𝑧2) 
(5)


## Page 5


To ensure that each sample is positive and nonlinear amplification of the output of 
the derivative emphasizes the higher frequencies, the signal is squared point by point. The 
equation of this operation is: 
 
𝑦(𝑛𝑇) = [𝑥(𝑛T)]2 
 (6) 
Then we use moving-window integration to obtain waveform feature information in 
addition to the slope of the R wave. It is calculated from: 
 
𝑦(𝑛𝑇) = (1/N)[𝑥(𝑛𝑇−(𝑁−1)𝑇) + 𝑥(𝑛𝑇−(𝑁−2)𝑇)
+ ⋯+ 𝑥(𝑛𝑇)] 
 (7) 
Where N=30 is the number of samples in the width of the integration window. If N is too 
large, the wave group will be flooded and if N is too small, other clutters will be generated. 
Finally, Adaptive thresholds discriminate the locations of the R waves. Low 
thresholds are possible because of the improvement of the signal-to-noise ratio by the band-
pass filter. 
2.2.2 Feature wave interception 
Based on cardiology, the number of R-waves in a fixed ECG signal should be within 
a certain range. If the total number of R waves is more or less than the range of values, it 
will be considered as a noise signal. For the stability of the system, we replace the original 
signals with fixed zero sequences as the feature waves of the noise signals. For ECG signals, 
irregular vibration may appear in the early stage due to adjustment of the acquisition 
equipment and the patient's posture. These signals cannot reflect the characteristics of the 
whole ECG signal. Besides, when doctors classify heart rhythms by ECG, they need to 
observe ECG of several cardiac cycle. Therefore, we proposed a method to extract feature 
waves10 26. We intercept feature waves containing four cardio cycles from the middle of 
ECG signals. Our experience shows that this method will reduce computational complexity 
while improving classification accuracy. 
2.3 Time-frequency diagram conversion 
In the field of signal processing, the time-frequency characteristics of signals can be 
obtained through wavelet transformation at different scales13 10. The wavelet transform 
formula is as follows: 
 
𝑊𝑓(𝑎, 𝑏) =< 𝑓, 𝜓𝑎,𝑏>= 1
√𝑎
∫
𝑓(𝑡) × |𝑎|−1
2𝜑(𝑡−𝑏
𝑎
) 𝛥𝑡
(𝑘+1)𝛥𝑡
𝑘𝛥𝑡
 
 
(8) 
where<* ,*> is expressed as dot product, a is expressed as scale factor, b is expressed as 
displacement factor, * is expressed as complex conjugate and 𝜓𝑎,𝑏(𝑡) is expressed as 
wavelet basis function. In our method the wavelet basis function is db4 wavelet25. 
In order to apply the above formula to programming, we can achieve integration by 
discretizing the integral function and summing it. The discrete formula is as follows: 
 
𝑊𝑓(𝑎, 𝑏) = ∑
∫
𝑓(𝑡) × |𝑎|−1
2𝜑(𝑡−𝑏
𝑎
) 𝛥𝑡
(𝑘+1)𝛥𝑡
𝑘𝛥𝑡
𝑘
 
      = |𝑎|−1
2𝛥𝑡∑𝑓(𝑘𝛥𝑡) × 𝜑(𝑘𝛥𝑡−𝑏
𝑎
)
𝑘
 
 
 
(9)


## Page 6


Using different wavelets for wavelet transformation can extract different time 
frequency characteristics of the signal. In order to analyze these features together, we 
proposed the following methods: we store wavelet transformation coefficients at different 
scales in a matrix orderly. The transformation coefficients for each scale are stored on each 
row of the matrix. When using convolution neural network to predict classification results, 
the coefficient matrix can be processed as a single-channel grayscale image. Examples of 
time-frequency diagrams corresponding to each kind of signal are shown in Table.1. 
 
Table.1 the time-frequency diagrams of signal 
Class 
Feature Wave 
Time-Frequency Diagram 
Normal 
AF 
Other 
Rhythm 
Noise 
As can be seen from Table.1, images of different classes have different textures. 
Because most of the noise signals have been replaced by zero signals in the pre-processing, 
their time-frequency diagrams are pure black images. Images in other classes have 
similarity and differentiation, which is difficult to observe in 1-D ECG signals. 
 
 
 
2.4 Classification via ResNet 
Deep convolutional neural network can extract deep features of images, which is 
helpful to improve the accuracy of classification results. For the capability to geometric 
transformation invariance of convolution and pooling modules, our systems can be used 
without aligning signals. Due to the obvious differences in time-frequency diagrams of 
different classes, a light-weighted image classification network can achieve a good 
classification results. In our system, ResNet-34 is selected as the classification network. 
3.   Experimental result


## Page 7


We used 8528 single lead episodic ECG records in the dataset of 2017 
PhysioNet/Computing-in-Cardiology 
Challenge. 
Each 
ECG 
was 
annotated 
by 
cardiologists into four classes: normal, Atrial fibrillation (AF), other rhythm and noise.  
We test our system on the testing dataset. The confusion matrix for the model 
predictions is shown in Fig.2. Most of arrhythmias can be detected with a proper high 
accuracy. Precision and recall of each class are shown in Table.2. The noise signals 
interfere classification results. However, noise interference can be avoided if ECG signals 
are properly collected in application. When we classify the signals after removing the noise 
signals, the classification accuracy can reach more than 98.6% on average. 
 
 
Fig. 2. the classification results of using resnet34 
 
Table 2：the results on the test set 
Class 
Precision 
Recall 
Normal 
99.32% 
96.67% 
AF 
97.83% 
90.00% 
Other rhythm 
98.44% 
90.00% 
Noise 
68.18% 
100% 
 
According to the ranking method of competition, we calculated the F1 score of our 
system. As we can see in Table.3, the F1 score of our system is 0.11 higher than the winner 
of the competition. Our system is a surprisingly simple and fast, which can surpass prior 
state-of-the-art ECG classification results. Besides, our method also shows robust 
performance and achieved state-of-the-art result on different data sets. 
Table 3： Comparison with the first few 
 
Participant 
F1 score 
1st 
Guangyu Bin 
0.86 
2nd 
Zhaohanx 
0.85


## Page 8


Tomas.teijeiro 
0.85 
 
Fplesinger 
0.85 
5th 
Rmaka08 
0.84 
 
Our method 
0.87 
4.   Conclusion 
In this work, we propose a novel method to predict heart diseases from ECG signals 
with cardiology, signal processing methods and deep learning model. We use wavelet 
transformation to convert 1-D signals into 2-D images, which allows deep learning model 
to simultaneously analyze the characteristics of different frequency bands of the signal. 
Our system is simple, fast and shows the state-of-the-art performance. 
Due to the excellent performance of our system in the task of four classifications of 
ECG signals, we expect this method to apply to more complex tasks. We will experiment 
on larger data sets with finer annotations. In addition, since different wavelets can extract 
different features of frequency when using wavelet transform, the performance of our 
system is different. We will try to use other wavelets to process the signals. 
 
Acknowledgements 
This work was supported by the CETC Foundation (No. 6141B0801010a, No. 
6141B08010102 and No. 6141B08080101) 
 
References 
1.   U. R. Acharya, H. Fujita, O. S. Lih, Y. Hagiwara, J. H. Tan, and M. J. I. S. Adam, "Automated 
Detection of Arrhythmias Using Different Intervals of Tachycardia ECG Segments with 
Convolutional Neural Network," vol. 405, pp. 81-90, 2017. 
2.   A. Annavarapu and P. J. I. J. o. t. C. A. Kora, "ECG-based atrial fibrillation detection using 
different orderings of Conjugate Symmetric–Complex Hadamard Transform," vol. 2, no. 3, p. 
S2405818116300538, 2016. 
3.   J. S. Arteaga-Falconi, H. A. Osman, A. E. J. I. T. o. I. Saddik, and Measurement, "ECG 
Authentication for Mobile Devices," vol. 65, no. 3, pp. 591-600, 2016. 
4.   S. K. Berkaya et al., "A survey on ECG analysis," vol. 43, pp. 216-235, 2018. 
5.   A. D. C. Chan, M. M. Hamdy, A. Badre, V. J. I. T. o. I. Badee, and Measurement, "Wavelet 
Distance Measure for Person Identification Using Electrocardiograms," vol. 57, no. 2, pp. 248-
253, 2008. 
6.   H. Gao, L. Zhuang, and K. Q. Weinberger, "Densely Connected Convolutional Networks," 2016. 
7.   R. E. Gregg, D. C. Deluca, C. H. S. Chien, E. D. Helfenbein, and M. J. J. o. E. Ariet, "Automated 
serial ECG comparison improves computerized interpretation of 12-lead ECG," vol. 45, no. 6, 
pp. 561-565, 2012. 
8.   S. Gutta, Q. J. I. J. o. B. Cheng, and H. Informatics, "Joint Feature Extraction and Classifier 
Design for ECG Based Biometric Recognition," vol. 20, no. 2, pp. 460-468, 2016. 
9.   S. J. Kang, S. Y. Lee, H. I. Cho, and H. J. I. S. P. L. Park, "ECG Authentication System Design 
based on Signal Analysis in Mobile/Wearable Devices," vol. 23, no. 6, pp. 1-1, 2016.


## Page 9


10.   H. Li, D. Yuan, Y. Wang, D. Cui, and L. J. S. Cao, "Arrhythmia Classification Based on Multi-
Domain Feature Extraction for an ECG Recognition System," vol. 16, no. 10, p. 1744, 2016. 
11.   S. Liang-Yu, W. Ying-Hsuan, and H. J. B. E. I. T. o. Weichih, "Using wavelet transform and 
fuzzy neural network for VPC detection from the Holter ECG," vol. 51, no. 7, pp. 1269-1273, 
2004. 
12.   I. Odinaka et al., "ECG Biometric Recognition: A Comparative Analysis," vol. 7, no. 6, pp. 
1812-1824, 2012. 
13.   S. Pal and M. J. M. Mitra, "Detection of ECG characteristic points using Multiresolution 
Wavelet Analysis based Selective Coefficient Method," vol. 43, no. 2, pp. 255-261, 2010. 
14.   J. Pan, . and W. J. Tompkins, %J IEEE Transactions on Biomedical Engineering, "A real-time 
QRS detection algorithm," vol. BME-32, no. 3, pp. 230-236, 2007. 
15.   F. Porée, G. Kervio, G. J. S. I. Carrault, and V. Processing, "ECG biometric analysis in different 
physiological recording conditions," vol. 10, no. 2, pp. 267-276, 2016. 
16.   P. Rajpurkar, A. Y. Hannun, M. Haghpanahi, C. Bourn, and A. Y. Ng, "Cardiologist-Level 
Arrhythmia Detection with Convolutional Neural Networks," 2017. 
17.   A. H. Ribeiro et al., "Automatic Diagnosis of Short-Duration 12-Lead ECG using a Deep 
Convolutional Network," 2018. 
18.   M. Salem, S. Taheri, and J. Shiun-Yuan, "ECG Arrhythmia Classification Using Transfer 
Learning from 2-Dimensional Deep CNN Features," 2018. 
19.   A. P. Shah and S. A. J. J. o. E. Rubin, "Errors in the computerized electrocardiogram 
interpretation of cardiac rhythm," vol. 40, no. 5, pp. 385-390, 2007. 
20.   K. A. Sidek, I. Khalil, and M. Smolen, "ECG biometric recognition in different physiological 
conditions using robust normalized QRS complexes," 2012. 
21.   Y. Wang, F. Agrafioti, D. Hatzinakos, and K. N. J. E. J. o. A. i. S. P. Plataniotis, "Analysis of 
Human Electrocardiogram for Biometric Recognition," vol. 2008, no. 1, p. 19, 2007. 
22.   J. L. Willems et al., "The diagnostic performance of computer programs for the interpretation 
of electrocardiograms," vol. 325, no. 25, pp. 1767-73, 1991. 
23.   Z. Xiong, M. K. Stiles, and J. Zhao, "Robust ECG signal classification for detection of atrial 
fibrillation using a novel neural network," 2017 Computing in Cardiology (CinC), 2018. 
24.   Z. Zhao, S. Särkkä, and A. B. Rad, "Kalman-based Spectro-Temporal ECG Analysis using Deep 
Convolutional Networks for Atrial Fibrillation Detection," 2018. 
25.   M. Zihlmann, D. Perekrestenko, and M. Tschannen, "Convolutional Recurrent Neural Networks 
for Electrocardiogram Classification," 2017. 
26.   M. Zoni-Berisso, F. Lercari, T. Carazza, and S. J. C. E. Domenicucci, "Epidemiology of atrial 
fibrillation: European perspective," vol. 2014, no. default, pp. 213-220, 2014.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
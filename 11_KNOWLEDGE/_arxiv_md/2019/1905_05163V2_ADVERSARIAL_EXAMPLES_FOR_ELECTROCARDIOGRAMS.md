---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.05163v2
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1905.05163v2_Adversarial_Examples_for_Electrocardiograms

> Source: 1905.05163v2_Adversarial_Examples_for_Electrocardiograms.pdf

> Pages: 11

---


## Page 1


Adversarial Examples for Electrocardiograms
Xintian Han1∗, Yuxuan Hu2, Luca Foschini3, Larry Chinitz2, Lior Jankelson2, Rajesh Ranganath1,4,5∗
1 Center for Data Science, New York University
2 Leon. H. Charney Division of Cardiology, NYU Langone Health
3 Evidation Health, Inc.
4 Department of Population Health, NYU Langone Health
5 Courant Institute of Mathematics, New York University
In recent years, the electrocardiogram (ECG) has seen a large diffusion in both medical and commercial
applications, fueled by the rise of single-lead versions. Single-lead ECG can be embedded in medical de-
vices and wearable products such as the injectable Medtronic Linq monitor, the iRhythm Ziopatch wearable
monitor, and the Apple Watch Series 4. Recently, deep neural networks have been used to automatically
analyze ECG tracings, outperforming even physicians specialized in cardiac electrophysiology [19] in de-
tecting certain rhythm irregularities. However, deep learning classiﬁers have been shown to be brittle to
adversarial examples, which are examples created to look incontrovertibly belonging to a certain class to
a human eye but contain subtle features that fool the classiﬁer into misclassifying them into the wrong
class [6, 22]. Very recently, adversarial examples have also been created for medical-related tasks [4, 18].
Yet, traditional attack methods to create adversarial examples, such as projected gradient descent (PGD)
[16] do not extend directly to ECG signals, as they generate examples that introduce square wave artifacts
that are not physiologically plausible. Here, we developed a method to construct smoothed adversarial
examples for single-lead ECG. First, we implemented a neural network model achieving state-of-the-art
performance on the data from the 2017 PhysioNet/Computing-in-Cardiology Challenge for arrhythmia de-
tection from single lead ECG classiﬁcation [2]. For this model, we utilized a new technique to generate
smoothed examples to produce signals that are 1) indistinguishable to cardiologists from the original ex-
amples and 2) incorrectly classiﬁed by the neural network. Finally, we show that adversarial examples are
not unique and provide a general technique to collate and perturb known adversarial examples to create
new ones.
Background. Cardiovascular diseases represent a major health burden, accounting for 30% of deaths world-
wide [12]. The ECG is a simple and non-invasive test used for screening and diagnosis of cardiovascular disease.
It is widely available in multiple medical device applications, including standard 12-lead ECG, Holter recorders,
and monitoring devices [13]. In recent years, there has been further growth in ECG utilization in the form of
single-lead ECG used in miniature implantable medical devices and wearable medical consumer products such as
smart watches. These single-lead ECGs, such as the one incorporated in the Apple Watch Series 4, are expected
to be worn by tens of millions of Americans by the end of 2019 [10]. Moreover, consumer wearable devices are
utilized to collect data in clinical studies, such as the Health eHeart study [1] and the Apple Heart Study [17].
Large studies that make use of Patient-generated Health Data (PGHD) are expected to become more frequent after
the Food and Drugs Administration (FDA)’s recent release of a set of guidelines and tools to collect Real-World
Data (RWD) from research participants via apps and other mobile health sources [5]. Having clinicians analyze
such a large number of ECGs is impractical. Recently, driven by the introduction of deep learning methodologies,
automated systems have been developed, allowing rapid and accurate ECG classiﬁcation [8]. In the 2017 Phys-
ioNet Challenge for atrial ﬁbrillation classiﬁcation using single-lead ECG, multiple efﬁcient solutions utilized deep
neural networks [9]. Deep learning has been shown to be susceptible to adversarial examples in general [6, 22]
and very recently in medical applications [3]. However, to the best of our knowledge, it is unknown whether
deep learning algorithms are robust in ECG classiﬁcation.
1
arXiv:1905.05163v2  [eess.SP]  4 Jun 2019


## Page 2


Description of data.
ECGs were obtained from the publicly available 2017 PhysioNet/CinC Challenge [2]. The
goal of the challenge was to classify single lead ECG recordings to four types: normal sinus rhythm (Normal),
atrial ﬁbrillation (AF), an alternative rhythm (Other), or noise (Noise). The challenge data set contained 8,528
single-lead ECG recordings lasting from 9s to about 60s, including 5,076 Normal, 758 AF, 2,415 Other, and 279
Noise examples. 90% of the data set was used for training and 10% was used for testing.
Model and Performance.
We used a 13-layer convolutional network [7] that won the 2017 PhysioNet/CinC
Challenge. We evaluated both accuracy and F1 score. A high F1 score indicates good network performance, with
high true positive and true negative rates.
The model achieved an average accuracy rate of 0.88 and F1 score of 0.87 for the ECG classes (Normal, AF and
Other) on the test set, which is comparable to state of the art ECG classiﬁcation systems [7].
Original tracing
Prediction: AF
100% conﬁdence
+
Smooth Perturbation
Combined tracing
Prediction: Normal
100% conﬁdence
(a) AF to Normal
Original tracing
Prediction: Normal
99% conﬁdence
+
Smooth Perturbation
Combined tracing
Prediction: AF
100% conﬁdence
(b) Normal to AF
Figure 1: Demonstration of disruptive adversarial examples. We add ﬁne smooth perturbations to the original
tracings to create adversarial examples. Perturbation and tracing voltage are plotted at the same scale. The
neural network correctly diagnose normal sinus rhythm and AF with 99% and 100% conﬁdence when the original
tracings are used. However, when presented with adversarial examples indistinguishable to expert clinician, the
neural network misclassiﬁes normal sinus rhythm to AF and AF to normal sinus with 100% conﬁdence.
2


## Page 3


Adversarial Examples.
Adversarial examples are designed by humans to cause a machine learning algorithm
to make a mistake. An adversarial example is made by adding a small perturbation to the input of the machine
learning algorithm that keeps the label of the input, while also ensuring it still looks like a real input [6, 22].
These kinds of adversarial examples have been successfully created in the ﬁeld of medical imaging classiﬁca-
tion [4].
Traditional adversarial attack algorithms add a small imperceptible perturbation to lower the prediction accuracy
of a machine learning model.
However, attacking ECG deep learning classiﬁers with traditional methods creates examples that display square
wave artifacts that are not physiologically plausible (Extended Data ﬁg. 5). By taking weighted average of nearby
time steps, we crafted smooth adversarial examples that cannot be distinguished from original ECG signals but
will still fool the deep network to make a wrong prediction (See Methods section).
Figure 2: Network accuracy on our generated adversarial examples. We are able to generate adversarial examples,
leading to missclasiﬁcation in 74% of ECG tracings. We validate the generated tracings by asking clinicians to
determine whether 250 pairs of adversarial examples and original ECGs come from the same class. On average,
the clinicians conclude that 246.5/250 pairs belonged to the same class, conﬁrming that the attacks did not
substantially modify the tracings. This shows that the deep network failed to correctly classify most of the newly
generated examples, when a human would have assigned to a different class only 1.4% of them.
We generated adversarial examples on the test set. We transformed the test examples to make the network
change the label of Normal, Other and Noise to any other label. For AF, we altered the AF test examples so that
the deep neural network classiﬁes them as Normal. Misdiagnosis of AF as Normal may increase the risk of AF-
related complications such as stroke and heart failure. We showcase the generation of adversarial examples in
Figure 1.
After adversarial attacks, 74% of the test ECGs originally classiﬁed correctly by the network are now assigned a
different diagnosis, ultimately showing that deep ECG classiﬁers are vulnerable to adversarial examples.
To assess how the generated signals would be classiﬁed by human experts, we invited one board certiﬁed medicine
specialist and one cardiac electrophysiology specialist. We asked them to diagnose whether signals generated by
our methods and original ECGs come from the same class. From Figure 2, the model incorrectly diagnosed almost
all (98.6%) of the signals created by our method.
We also invited the clinical specialists to distinguish ECG signals from the adversarial examples generated by our
smooth method and the traditional attack method based on projected gradient descent (PGD) [16]. From Figure 3,
the adversarial examples generated by our method are signiﬁcantly harder for clinicians to distinguish from the
original ECG than the traditional attack method. On average, the clinicians were able to correctly identify the
smoothed adversarial examples from their original counterpart 62% of the time.1
1The EP specialist was slightly more accurate at 65% versus 59%.
3


## Page 4


Figure 3: Clinician success rate of distinguishing real ECG’s from adversarial examples. We asked clinician experts
in ECG reading to distinguish between 100 pairs of original ECGs and adversarial examples generated by the
traditional attack method. They, on average, correctly identiﬁed 95% of the adversarial examples. We then asked
them to distinguish between 100 pairs of original ECGs and adversarial examples generated by our smooth attack
method. This resulted in the correct identiﬁcation of only 62% of examples.
Existence of adversarial examples.
Here we provide a construction that shows that adversarial examples are
not rare. In particular, we show that it is possible to create more examples that remain adversarial by adding a
small amount of Gaussian noise to an original adversarial example and then smooth the result. We repeat this
process 1000 times and ﬁnd that the deep neural network still incorrectly classiﬁes all 1000 new, adversarial
examples. Adding Gaussian noise could still produce adversarial examples on 87.6% of the test examples from
which adversarial examples were generated. We plotted all of the newly crafted adversarial examples which
form a band around the original ECG signal in Figure 4. The signals in the band may intersect. We chose pairs of
intersecting signals and concatenate the left half of one signal with right half of the other to create a new example.
We found that signals created by concatenation are also adversarial examples. We also sampled random values
in the band for each time step and then smoothed them to create new adversarial examples. The fact that these
different perturbations on adversarial examples all led to new examples that remain adversarial reinforces the
notion that such examples should not be be considered rare isolated cases. (See Methods section for detailed
description.)
Discussion.
We demonstrated the ability to add imperceptible perturbations to ECG tracings in order to create
adversarial examples that fool a deep neural network classiﬁer into assigning the examples to an incorrect rhythm
class. Moreover, we showed that such examples are not rare. These ﬁndings raised several questions regarding
the use of deep learning in analyzing ECGs at scale where millions of tests may be run every week by widespread
consumer devices. To increase robustness to adversarial examples, it is crucial that classiﬁcation methods for ECGs,
especially those intended to operate without humans supervision, generalize well to new examples. Ensuring safe
generalization would require obtaining data acquired from multiple environments and from each new version of
the signal collecting device. Labeling data for new environments and devices would also require substantial
human effort, as clinical experts would be needed to provide correct labels for each new tracing. The extent to
which the rarity of examples increases as a function of training dataset size and composition warrants further
investigation.
One way to protect against adversarial examples is to include them in the training set of the model. However, such
an approach can only protect against known adversarial examples, created with a given speciﬁc attack method,
and will not protect against future attack methods. A more direct approach would be to certify deep neural
networks for robustness with mathematical proofs [21] as suggested for other safety-critical domains, such as the
aviation industry [11].
The possibility to construct even a single adversarial example may still enable malicious actors to inject small
perturbations into real-world data indistinguishable to the human eye. This could represent an important vul-
nerability with implications including the attacks of medical devices relying on ECG interpretation (pacemakers,
4


## Page 5


Figure 4: Existence of adversarial examples. We picked an ECG signal and we sampled 1,000 different adver-
sarial examples by adding small Gaussian noise and smoothing. We plotted all the newly generated adversarial
examples as well as the original ECG signal. The newly generated examples form a wide band around the original
signal. Sampling uniformly from the band and smoothing also produces adversarial examples. These ﬁndings
demonstrate that adversarial examples are not rare.
deﬁbrillators), the introduction of intentional bias into clinical trials, and the skew of data to alter insurance
claims [4]. To prevent such possibilities, it is paramount that platforms for collection and analysis of real-world
data implement principles from Trusted Computing to provide trusted data provenance guarantees that can certify
that data has not been tampered with from device acquisition to any downstream analysis [15].
One thing to note is that the lack of robustness observed is not inherent to the use of statistical methods to
classify ECGs. Humans tend to be more robust to small perturbations because they use coarser visual features
to classify ECGs, such as the R-R interval and the P-wave morphology. Coarser features change less under small
perturbations and generalize better to new domains. These coarser features often have underlying biophysical
meanings. To automate the classiﬁcation of less prevalent ECG diagnoses, it may be useful to incorporate known
electrocardiographic markers of biophysical phenomena along with deep learning to not only increase robustness
to adversarial attacks but also improve the network accuracy. Additionally, regularizing deep networks to prefer
coarser features can improve robustness. In conclusion, with this work, we do not intend to cast a shadow on the
utility of deep learning for ECG analysis, which undoubtedly will be useful to handle the volumes of physiological
signals available in the near future. This work should, instead, serve as an additional reminder that machine
learning systems deployed in the wild should be designed with safety and reliability in mind [20], with particular
focus on training data curation and provable guarantees on performances.
References
[1] S. Bennett. Wearables could catch heart problems that elude your doctor, Feb. 2018.
[2] G. D. Clifford, C. Liu, B. Moody, L.-w. H. Lehman, I. Silva, Q. Li, A. Johnson, and R. G. Mark. Af classiﬁcation
from a short single lead ecg recording: The physionet computing in cardiology challenge 2017. Computing
in cardiology, 2017.
5


## Page 6


[3] S. G. Finlayson, J. D. Bowers, J. Ito, J. L. Zittrain, A. L. Beam, and I. S. Kohane. Adversarial attacks on
medical machine learning. Science, 363(6433):1287–1289, 2019.
[4] S. G. Finlayson, I. S. Kohane, and A. L. Beam. Adversarial attacks against medical deep learning systems.
arXiv preprint arXiv:1804.05296, 2018.
[5] Food and D. A. (FDA).
Framework to advance use of real-world evidence to support development
of drugs and biologics.
https://www.fda.gov/downloads/ScienceResearch/SpecialTopics/
RealWorldEvidence/UCM627769.pdf.
[6] I. J. Goodfellow, J. Shlens, and C. Szegedy. Explaining and harnessing adversarial examples. arXiv preprint
arXiv:1412.6572, 2014.
[7] S. D. Goodfellow, A. Goodwin, R. Greer, P. C. Laussen, M. Mazwi, and D. Eytan. Towards understanding ecg
rhythm classiﬁcation using convolutional neural networks and attention mappings. Proceedings of Machine
Learning Research, 2018.
[8] A. Y. Hannun, P. Rajpurkar, M. Haghpanahi, G. H. Tison, C. Bourn, M. P. Turakhia, and A. Y. Ng. Cardiologist-
level arrhythmia detection and classiﬁcation in ambulatory electrocardiograms using a deep neural network.
Nature medicine, 25(1):65, 2019.
[9] S. Hong, M. Wu, Y. Zhou, Q. Wang, J. Shang, H. Li, and J. Xie. Encase: An ensemble classiﬁer for ecg
classiﬁcation using expert features and deep neural networks. In 2017 Computing in Cardiology (CinC),
pages 1–4. IEEE, 2017.
[10] I. D. C. (IDC). Idc reports strong growth in the worldwide wearables market, led by holiday shipments of
smartwatches, wrist bands, and ear-worn devices, Mar. 2019.
[11] K. D. Julian, M. J. Kochenderfer, and M. P. Owen. Deep neural network compression for aircraft collision
avoidance systems. Journal of Guidance, Control, and Dynamics, 42(3):598–608, 2018.
[12] B. B. Kelly, V. Fuster, et al. Promoting cardiovascular health in the developing world: a critical challenge to
achieve global health. National Academies Press, 2010.
[13] H. L. Kennedy. The evolution of ambulatory ecg monitoring. Progress in cardiovascular diseases, 56(2):127–
132, 2013.
[14] A. Kurakin, I. Goodfellow, and S. Bengio.
Adversarial machine learning at scale.
arXiv preprint
arXiv:1611.01236, 2016.
[15] J. Lyle and A. Martin. Trusted computing and provenance: better together. Usenix, 2010.
[16] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu. Towards deep learning models resistant to
adversarial attacks. arXiv preprint arXiv:1706.06083, 2017.
[17] A. C. of Cardiology (ACC). Apple heart study identiﬁes aﬁb in small group of apple watch wearers, Mar.
2019.
[18] M. Paschali, S. Conjeti, F. Navarro, and N. Navab. Generalizability vs. robustness: Adversarial examples for
medical imaging. arXiv preprint arXiv:1804.00504, 2018.
[19] P. Rajpurkar, A. Y. Hannun, M. Haghpanahi, C. Bourn, and A. Y. Ng. Cardiologist-level arrhythmia detection
with convolutional neural networks. arXiv preprint arXiv:1707.01836, 2017.
[20] S. Saria and A. Subbaswamy. Tutorial: Safe and reliable machine learning. arXiv preprint arXiv:1904.07204,
2019.
[21] G. Singh, T. Gehr, M. Mirman, M. Püschel, and M. Vechev. Fast and effective robustness certiﬁcation. In
Advances in Neural Information Processing Systems, pages 10802–10813, 2018.
[22] C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow, and R. Fergus. Intriguing properties
of neural networks. arXiv preprint arXiv:1312.6199, 2013.
6


## Page 7


Acknowledgements
We thank Wei-Nchih Lee, Sreyas Mohan, Mark Goldstein, Aodong Li, Aahlad Manas Puli, Harvineet Singh, Mukund
Sudarshan and Will Whitney.
7


## Page 8


Methods
Description of the Traditional Attack Methods.
Two traditional attack methods are fast gradient sign method
(FGSM) [6] and projected gradient descent (PGD) [14]. They are white-box attack methods based on the gradients
of the loss used to train the model with respect to the input.
Denote our input entry x, true label y, classiﬁer (network) f , and loss function L(f (x), y). We describe FGSM
and PGD below:
• Fast gradient sign method (FGSM). FGSM is a fast algorithm. For an attack level ε, FGSM sets
xadv = x + ε · sign(∇x L(f (x), y)),
The attack level is chosen to be sufﬁciently small so as to be undetectable.
• Projected gradient descent (PGD). PGD is an improved version that uses multiple iterations of FGSM. Deﬁne
Clipx,ε(x′) to project each x′ back to the inﬁnite norm ball by clamping the maximum absolute difference
value between x and x′ to ε. Beginning by setting x′
0 = x, we have
x′
i = Clipx,ε{x′
i−1 + α · sign(∇x L(f (x′
i−1), y))).}
(1)
After T steps, we get our adversarial example xadv = x′
T.
Our Smooth Attack Method.
In order to smooth the signal, we use the help of convolution. By convolution,
we take the weighted average of one position of the signal and its neighbors:
(a ⊛v)[n] =
2K+1
X
m=1
a[n −m + K + 1] · v[m],
where a is the objective function and v is the weights or kernel function. In our experiment, the weights are
determined by a Gaussian kernel. Mathematically, if we have a Gaussian kernel of size 2K+1 and standard
deviation σ, we have
v[m] =
exp(−(m −K −1)2/(2 ∗σ2))
P2K+1
i=1
exp(−(i −K −1)2/(2 ∗σ2))
.
We can easily see that when σ goes to inﬁnity, the convolution with Gaussian kernel becomes a simple average;
when σ goes to zero, the convolution becomes an identity function. Instead of getting an adversarial perturbation
and then convolving it with the Gaussian kernels, we could create adversarial examples by optimizing a smooth
perturbation that fools the neural network. We introduce our method of training smooth adversarial perturbations
(SAP). In our SAP method, we take the adversarial perturbation as the parameter θ and add it to the clean examples
after convolving with a number of Gaussian kernels. We denote K(s,σ) to be a Gaussian kernel with size s and
standard deviation σ. The resulting adversarial example could be written as a function of θ:
xadv(θ) = x + 1
m
m
X
i
θ ⊛K(s[i],σ[i]).
In our experiment, we let s be {5,7,11,15,19} and σ be {1.0,3.0,5.0,7.0,10.0}. Then we try to maximize the
loss function with respect to θ to get the adversarial example. We still use PGD but on θ this time:
θ ′
i = Clip0,ϵ{θ ′
i−1 + α · sign(∇θ L(f (xadv(θ ′
i−1), y)))}.
(2)
There are two major differences between updates (2) and (1). In (2), we update θ not xadv and clip around
zero not the input x. In practice, we initialize the adversarial perturbation θ to be the one obtained from PGD
(ε = 10,α = 1, T = 20) on x and run another PGD (ε = 10,α = 1, T = 40) on θ.
8


## Page 9


Existence of Adversarial Examples
We design experiments to show that adversarial examples are not rare.
Denote original signal to be x and adversarial example we generated to be xadv.
First, we generate Gaussian noise δ ∼N (0,25) and then add it to the adversarial examples. To make sure the
new examples are still smooth, we smooth the perturbation by convolving with the same Gaussian kernels in our
smooth attack method. We then clip the perturbation to make sure that it is still in the inﬁnite norm ball. The
newly generated example is
x′
adv = x + Clip0,ε
¨
1
m
m
X
i=1
(xadv + δ −x) ⊛K(s[i],σ[i])
«
.
We repeat the process of generating new examples 1000 times. These newly generated examples are still ad-
versarial examples. Some of them may intersect. For each intersected pair, we concatenate the left part of one
examples and the right part of the other to create new adversarial examples. Denote x1 and x2 to be a pair of
adversarial examples that intersect. Suppose they intersect at time step t and the total length of the example is
T. The new hybrid example x′ satisﬁes:
x′[1 : t] = x1[1 : t];
x′[t + 1 : T] = x2[t + 1 : T],
where [1 : t] means from time step 1 to time step t. All the newly concatenated examples are still misclassiﬁed
the network.
The 1000 adversarial examples form a band. To emphasize that all the smooth signals in the band are still
adversarial examples, we sample uniformly from the band to create new examples. Denote max[t] and min[t]
to be the maximum value and minimum value of 1000 samples at time step t. To sample a smooth signal from
the band, we ﬁrst sample a uniform random variable a[t] ∼U (min[t],max[t]) for each time step t and then we
smooth the perturbation. The example generated by uniform sampling and smoothing, this time is
x′
adv = x + Clip0,ε
¨
1
m
m
X
i=1
(a −x) ⊛K(s[i],σ[i])
«
.
We repeat this procedure 1000 times, and all the newly generated examples still cause the network to make
the wrong diagnosis. We visualize the three procedures to show the existence of adversarial examples above in
Figure 6.
9


## Page 10


Extended Data
Original ECG
Adversarial Example 
Figure 5: An adversarial example created by projected gradient descent (PGD) method. This adversarial example
contains square waves and is not smooth. A physician reading this tracing will likely detect that this adversarial
example is not a real ECG.
10


## Page 11


Adversarial 
Examples
+
Gaussian 
Noise
-
Original
Signal
~
Smooth
Smooth
Perturbation
+
Original
Signal
=
New
Signal
(a) Adding Gaussian noise
New Signal 1
New Signal 2
(b) Concatenating intersected pairs
~
Boundary of 
the Band
Uniformly
Sample
Sample from 
the Band
-
Original
Signal
Smooth
Smooth
Perturbation
Original
Signal
+
=
New 
Signal
(c) Sampling uniformly from the band
Figure 6: Demonstration of three procedures to show the existence of the adversarial examples. (a) We add small
amount of Gaussian noise to the adversarial example and smooth it to create a new signal. (b) For intersected
signals, we concatenate the left half of one signal with right half of the other to create a new one. (c) We sample
uniformly from the band and smooth it to create a new signal.
11

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
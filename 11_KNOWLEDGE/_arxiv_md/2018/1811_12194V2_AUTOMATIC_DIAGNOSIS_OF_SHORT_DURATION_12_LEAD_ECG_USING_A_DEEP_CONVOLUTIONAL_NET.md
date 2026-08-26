---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.12194v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1811.12194v2_Automatic_Diagnosis_of_Short-Duration_12-Lead_ECG_using_a_Deep_Convolutional_Net

> Source: 1811.12194v2_Automatic_Diagnosis_of_Short-Duration_12-Lead_ECG_using_a_Deep_Convolutional_Net.pdf

> Pages: 11

---


## Page 1


Automatic Diagnosis of Short-Duration 12-Lead ECG
using a Deep Convolutional Network
Antônio H. Ribeiro1, 2, *, Manoel Horta Ribeiro1, Gabriela Paixão1, 3, Derick Oliveira1,
Paulo R. Gomes1, 3, Jéssica A. Canazart1, Milton Pifano1, 3, Wagner Meira Jr.1,
Thomas B. Schön2, Antonio Luiz Ribeiro1, 3, †
1 Universidade Federal de Minas Gerais, Brazil, 2 Uppsala University, Sweden,
3 Telehealth Center from Hospital das Clínicas da Universidade Federal de Minas Gerais, Brazil.
*antonio-ribeiro@ufmg.br, †tom@hc.ufmg.br
Abstract
We present a model for predicting electrocardiogram (ECG) abnormalities in short-
duration 12-lead ECG signals which outperformed medical doctors on the 4th year
of their cardiology residency. Such exams can provide a full evaluation of heart
activity and have not been studied in previous end-to-end machine learning papers.
Using the database of a large telehealth network, we built a novel dataset with
more than 2 million ECG tracings, orders of magnitude larger than those used in
previous studies. Moreover, our dataset is more realistic, as it consist of 12-lead
ECGs recorded during standard in-clinics exams. Using this data, we trained a
residual neural network with 9 convolutional layers to map 7 to 10 second ECG
signals to 6 classes of ECG abnormalities. Future work should extend these results
to cover a large range of ECG abnormalities, which could improve the accessibility
of this diagnostic tool and avoid wrong diagnosis from medical doctors.
1
Introduction
Cardiovascular diseases are the leading cause of death worldwide [1] and the electrocardiogram
(ECG) is a major diagnostic tool for this group of diseases. As ECGs transitioned from analogue to
digital, automated computer analysis of standard 12-lead electrocardiograms gained importance in
the process of medical diagnosis [2]. However, limited performance of classical algorithms [3, 4]
precludes its usage as a standalone diagnostic tool and relegates it to an ancillary role [5].
End-to-end deep learning has recently achieved striking success in task such as image classiﬁcation [6]
and speech recognition [7], and there are great expectations about how this technology may improve
health care and clinical practice [8–10]. So far, the most successful applications used a supervised
learning setup to automate diagnosis from exams. Algorithms have achieved better performance
than a human specialist on their routine workﬂow in diagnosing breast cancer [11] and detecting
certain eye conditions from eye scans [12]. While efﬁcient, training deep neural networks using
supervised learning algorithms introduces the need for large quantities of labeled data which, for
medical applications, introduce several challenges, including those related to conﬁdentiality and
security of personal health information [13].
Standard, short-duration 12-lead ECG is the most commonly used complementary exam for the
evaluation of the heart, being employed across all clinical settings: from the primary care centers
to the intensive care units. While tracing cardiac monitors and long-term monitoring, as the Holter
exam, provides information mostly about cardiac rhythm and repolarization, 12-lead ECG can
provide a full evaluation of heart, including arrhythmias, conduction disturbances, acute coronary syn-
dromes, cardiac chamber hypertrophy and enlargement and even the effects of drugs and electrolyte
disturbances.
Machine Learning for Health (ML4H) Workshop at NeurIPS 2018.
arXiv:1811.12194v2  [eess.SP]  17 Feb 2019


## Page 2


Although preliminary studies using deep learning methods [14, 15] achieve high accuracy in detecting
speciﬁc abnormalities using single-lead heart monitors, the use of such approaches for detecting the
full range of diagnoses that can be obtained from a 12-lead, standard, ECG is still largely unexplored.
A contributing factor for this is the shortage of full digital 12-lead ECG databases, since most
ECG are still registered only on paper, archived as images, or in PDF format [16]. Most available
databases comprise a few hundreds of tracings and no systematic annotation of the full list of ECG
diagnosis [17], limiting their usefulness as training datasets in a deep learning setting.
This lack of systematically annotated data is unfortunate, as training an accurate automatic method of
ECG diagnosis from a standard 12-lead ECG would be greatly beneﬁcial.The exams are performed
in settings where, often, there are no specialists to analyze and interpret the ECG tracings, such
as in primary care centers and emergency units. Indeed, primary care and emergency department
health professionals have limited diagnostic abilities in interpreting 12-lead ECGs [18, 19]. This
need is most acute in low and middle-income countries, which are responsible for more than 75% of
deaths related to cardiovascular disease [20], and where, often, the population does not have access
to cardiologists with full expertise in ECG diagnosis.
The main contribution of this paper is to introduce a large-scale novel dataset of labelled 12-lead
ECGs exams and to train and validate a residual neural network in this relevant setup. We consider 6
types of ECG abnormalities: 1st degree AV block (1dAVb), right bundle branch block (RBBB), left
bundle branch block (LBBB), sinus bradycardia (SB), atrial ﬁbrillation (AF) and sinus tachycardia
(ST), considered representative of both rhythmic and morphologic ECG abnormalities.
2
Related work
Classical ECG software, such as University of Glasgow’s ECG analysis program [21], extracts
the main features of the ECG signal using signal processing techniques and use them as input for
classiﬁers. A literature review of these methods is given by [22]. In [23] a different approach is
taken, where the ECG features are learned using an unsupervised method and then used as input to a
supervised learning method.
End-to-end deep learning presents an alternative to these two-step approaches, where the raw signal
itself is used as input to the classiﬁer. In [24, 25, 14] the authors make use of a convolutional
neural network to classify ECG abnormalities. The network architecture used in [14] is inspired by
architectures used for image classiﬁcation and we make use of a similar architecture in this paper.
There are differences though, in particular when it comes to the number of layers, input type (we
use 12-leads, while [14] used a single lead) and the output layer used. Recurrent networks are used
in [26, 15]. A review of recent machine learning techniques applied for ECG automatic diagnosis is
given in [27]. The aforementioned methods and others (such as random forest and bayesian methods)
are compared and a more extensive list of references using those methods is provided.
The major difference between this paper and other previous applications of end-to-end learning for
ECG classiﬁcation is on the dataset used for training and validating the model. The most common
dataset used to design and evaluate ECG algorithms is the MIT-BIH arrhythmia database [28], which
was used for training in [25, 23] and for almost all algorithms in [22]. This data set contain 30-minutes
2-leads ECG records from 47 unique patients. In [15] they used a dataset of 24-hour Holter ECG
recordings collected from 2,850 patients at the University of Virginia (UVA) Heart Station. In [14]
they construct a new dataset containing labeled data of 64,121 ECG records from 29,163 unique
patients who have used Zio Patch monitor. The PhysioNet 2017 Challenge, made available 12,186
entries dataset captured from the AliveCor ECG monitor containing between 9 and 61 seconds
recordings [29]. All these datasets were obtained from cardiac monitors and holter exams, where
patients are usually monitored for several hours, and are restricted to one or two leads. Our dataset, on
the other hand, consists of short duration (7 to 10 seconds) 12-lead tracings obtained from in-clinics
exams and is orders of magnitude larger than those used in previous studies, with well over 2 million
entries.
3
Data
The dataset used for training and validating the model consists of 2,470,424 records from 1,676,384
different patients from 811 counties in the state of Minas Gerais/Brazil. The duration of the ECG
2


## Page 3


Figure 1: Unidimensional residual neural network used for ECG classiﬁcation.
recordings is between 7 and 10 seconds. The data was obtained between 2010 and 2016 by a
telediagnostic ECG system developed and maintained by the Telehealth Network of Minas Gerais
(TNMG), led by the Telehealth Center from the Hospital das Clínicas of the Federal University of
Minas Gerais. We developed an unsupervised methodology that classiﬁes each ECG according to the
free text in the expert report. We combine this result with two existing automatic ECG classiﬁers
(Glasgow and Minnesota), using rules derived from expert knowledge and from the manual inspection
of samples of the exams to obtain the ground truth. In several cases, we assigned the exams to be
manually reviewed by medical students. This was done with around 34, 000 exams. This process is
thoroughly explained in Appendix A.
We split this dataset into training and validation set. The training set contains 98% of the data. And
the validation set consist of 2% (approximately 50,000 exams) used for tuning the hyperparameters.
The dataset used for testing the model consists of 953 tracings from distinct patients. These were
also obtained from TNMG’s ECG system but using a more rigorous methodology for labelling the
abnormalities. Two medical doctors with experience in electrocardiography have independently
annotated the ECGs. When they agree, the common diagnosis is considered as ground truth. And, in
case of any disagreement, a third medical specialist, aware of the annotations from the other two,
decided the diagnosis. Appendix B contain information about the abnormalities that can be found in
both the training/validation set and the test set.
4
Model
We used a convolutional neural network similar to the residual network [30], but adapted to unidimen-
sional signals. This architecture allows deep neural networks to be efﬁciently trained by including
skip connections. We have adopted the modiﬁcation in the residual block proposed in [31], which
place the skip connection in the position displayed in Figure 1. A similar architecture has been
successfully employed for arrhythmia detection from ECG signals in [14] and the design choices
we make in this section are, indeed, strongly inﬂuenced by [14]. We should highlight that, despite
using a signiﬁcantly larger training dataset, we got the best validation results with an architecture
with, roughly, one quarter the number of layers and parameters of the network employed in [14].
The network consists of a convolutional layer (Conv) followed by nblk = 4 residual blocks with two
convolutional layers per block. The output of the last block is fed into a Dense layer with sigmoid
activation function (σ), which was used because the classes are not mutually exclusive (i.e. two or
more classes may occur in the same exam). The output of each convolutional layer is rescaled using
batch normalization, BN, [32] and feed into a rectiﬁed linear activation unit, ReLU. Dropout [33] is
applied after the non-linearity.
The convolutional layers have ﬁlter length 16, starting with 4096 samples and 64 ﬁlters for the ﬁrst
layer and residual block and increasing the number of ﬁlters by 64 every second residual block and
subsampling by a factor of 4 every residual block. Max Pooling and convolutional layers with ﬁlter
length 1 (1x1 Conv) may be included in the skip connection to make the dimensions match the ones
from signals in the main branch.
The loss function is the average cross-entropy
1
nclass
Pnclass
i=1 yi log ˆyi + (1 −yi) log(1 −ˆyi) where ˆyi
is the output of the sigmoid layer for the i-th class and yi is the corresponding observed value (0 or
1). The cost function (i.e. the sum of loss functions over the entire training set) is minimized using
the Adam optimizer [34] with default parameters and learning rate lr = 0.001. The learning rate
3


## Page 4


Precision (PPV)
Recall (Sensitivity)
Speciﬁcity
F1 Score
model
doctor
model
doctor
model
doctor
model
doctor
1dAVb
0.923
0.905
0.727
0.679
0.998
0.998
0.813
0.776
RBBB
0.878
0.868
1.000
0.971
0.995
0.994
0.935
0.917
LBBB
0.971
1.000
1.000
0.900
0.999
1.000
0.985
0.947
SB
0.792
0.833
0.864
0.938
0.995
0.996
0.826
0.882
AF
0.846
0.769
0.846
0.769
0.998
0.996
0.846
0.769
ST
0.870
0.938
0.952
0.833
0.993
0.998
0.909
0.882
Table 1: Performance of our deep neural network model and 4th year cardiology resident medical
doctors when evaluated on the test set. (PPV = positive predictive value)
is reduced by a factor of 10 whenever the validation loss does not present any improvement for 7
consecutive epochs. The neural network weights are initialized as in [35] and the bias are initialized
with zeros. The training runs for 50 epochs with the ﬁnal model being the one with best validation
results during the optimization process.
5
Results
Table 1 shows the performance on the test set. We consider our model to have predicted the abnormal-
ity when its output is above a threshold that is set manually for each of the classes. Each threshold
was chosen to be approximately in the inﬂection point of the precision-recall curve (presented in
Appendix C). High performance measures were obtained for all ECG abnormalities, with F1 scores
above 80% and speciﬁcity indexes over 99%.
The same dataset was evaluated by two 4th year cardiology medical doctors, each one annotating
half of the exams in the test set. Their average performance is given in the table for comparison and,
considering the F1 score, the model outperforms them for 5 out of 6 abnormalities.
6
Future Work
The training data was collected from a general Brazilian population and, since the database is large,
it contains even rare conditions with sufﬁcient frequency so we can try to build models to predict
them. In future work we intend to extend the results to progressively larger classes of diagnosis.
This process will happen gradually because: i) the dataset preprocessing can be time consuming
and demands a lot of work (Appendix A); ii) generating validation data demand work hours of
experienced medical doctors.
The Telehealth Center at the Hospital das Clínicas of the Federal University of Minas Gerais receives
and assesses more than 2,000 digital ECGs per day. With the progressive improvements in the
interface with the medical experts, the quality of this data should progressively increase, and it could
be used in training, validating and testing future models.
The Telehealth Center is currently serving more than 1000 remote locations in 5 Brazilians states
and have the means to deploy and evaluate such automatic classiﬁcation systems as a part of broader
telehealth solutions, which could help to improve its capacity, making it possible to provide access of
a broader population, with better quality reports.
7
Conclusion
These promising initial results point to end-to-end learning as a competitive alternative to classical
automatic ECG classiﬁcation methods. The development of such technologies may yield high-
accuracy automatic ECG classiﬁcation systems that could save clinicians considerable time and
prevent wrong diagnosis. Millions of 12-lead ECGs are performed every year, many times in places
where there is a shortage of qualiﬁed medical doctors to interpret them. An accurate classiﬁcation
system could help detecting wrong diagnosis and improve the access of patients from deprived and
remote locations to this essential diagnostic tool of cardiovascular diseases.
4


## Page 5


Acknowledgments
This research was partly supported by the Brazilian Research Agencies CNPq, CAPES, and
FAPEMIG, by projects InWeb, MASWeb, EUBra-BIGSEA, INCT-Cyber and Atmosphere, and
by the Wallenberg AI, Autonomous Systems and Software Program (WASP) funded by Knut and Alice
Wallenberg Foundation. We also thank NVIDIA for awarding our project with a Titan V GPU.
References
[1] GBD 2016 Causes of Death Collaborators, “Global, regional, and national age-sex speciﬁc
mortality for 264 causes of death, 1980-2016: A systematic analysis for the Global Burden of
Disease Study 2016,” Lancet (London, England), vol. 390, pp. 1151–1210, Sept. 2017.
[2] J. L. Willems, C. Abreu-Lima, P. Arnaud, J. H. van Bemmel, C. Brohet, R. Degani, B. Denis,
I. Graham, G. van Herpen, and P. W. Macfarlane, “Testing the performance of ECG computer
programs: The CSE diagnostic pilot study,” Journal of Electrocardiology, vol. 20 Suppl, pp. 73–
77, Oct. 1987.
[3] J. L. Willems, C. Abreu-Lima, P. Arnaud, J. H. van Bemmel, C. Brohet, R. Degani, B. Denis,
J. Gehring, I. Graham, and G. van Herpen, “The diagnostic performance of computer programs
for the interpretation of electrocardiograms,” The New England Journal of Medicine, vol. 325,
pp. 1767–1773, Dec. 1991.
[4] A. P. Shah and S. A. Rubin, “Errors in the computerized electrocardiogram interpretation of
cardiac rhythm.,” Journal of Electrocardiology, vol. 40, no. 5, pp. 385–390, 2007 Sep-Oct.
[5] N. A. M. Estes, “Computerized interpretation of ECGs: Supplement not a substitute,” Circula-
tion. Arrhythmia and Electrophysiology, vol. 6, pp. 2–4, Feb. 2013.
[6] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classiﬁcation with deep convolutional
neural networks,” in Advances in Neural Information Processing Systems, pp. 1097–1105, 2012.
[7] G. Hinton, L. Deng, D. Yu, G. E. Dahl, A. Mohamed, N. Jaitly, A. Senior, V. Vanhoucke,
P. Nguyen, T. N. Sainath, and B. Kingsbury, “Deep Neural Networks for Acoustic Modeling in
Speech Recognition: The Shared Views of Four Research Groups,” IEEE Signal Processing
Magazine, vol. 29, pp. 82–97, Nov. 2012.
[8] W. W. Stead, “Clinical implications and challenges of artiﬁcial intelligence and deep learning,”
JAMA, vol. 320, pp. 1107–1108, Sept. 2018.
[9] Naylor C, “On the prospects for a (deep) learning health care system,” JAMA, vol. 320, pp. 1099–
1100, Sept. 2018.
[10] G. Hinton, “Deep learning—a technology with the potential to transform health care,” JAMA,
vol. 320, pp. 1101–1102, Sept. 2018.
[11] B. E. Bejnordi, M. Veta, P. Johannes van Diest, B. van Ginneken, N. Karssemeijer, G. Litjens,
J. A. W. M. van der Laak, and the CAMELYON16 Consortium, M. Hermsen, Q. F. Manson,
M. Balkenhol, O. Geessink, N. Stathonikos, M. C. van Dijk, P. Bult, F. Beca, A. H. Beck,
D. Wang, A. Khosla, R. Gargeya, H. Irshad, A. Zhong, Q. Dou, Q. Li, H. Chen, H.-J. Lin,
P.-A. Heng, C. Haß, E. Bruni, Q. Wong, U. Halici, M. U. Öner, R. Cetin-Atalay, M. Berseth,
V. Khvatkov, A. Vylegzhanin, O. Kraus, M. Shaban, N. Rajpoot, R. Awan, K. Sirinukunwattana,
T. Qaiser, Y.-W. Tsang, D. Tellez, J. Annuscheit, P. Hufnagl, M. Valkonen, K. Kartasalo,
L. Latonen, P. Ruusuvuori, K. Liimatainen, S. Albarqouni, B. Mungal, A. George, S. Demirci,
N. Navab, S. Watanabe, S. Seno, Y. Takenaka, H. Matsuda, H. Ahmady Phoulady, V. Kovalev,
A. Kalinovsky, V. Liauchuk, G. Bueno, M. M. Fernandez-Carrobles, I. Serrano, O. Deniz,
D. Racoceanu, and R. Venâncio, “Diagnostic Assessment of Deep Learning Algorithms for
Detection of Lymph Node Metastases in Women With Breast Cancer,” JAMA, vol. 318, p. 2199,
Dec. 2017.
5


## Page 6


[12] J. De Fauw, J. R. Ledsam, B. Romera-Paredes, S. Nikolov, N. Tomasev, S. Blackwell,
H. Askham, X. Glorot, B. O’Donoghue, D. Visentin, G. van den Driessche, B. Lakshmi-
narayanan, C. Meyer, F. Mackinder, S. Bouton, K. Ayoub, R. Chopra, D. King, A. Karthike-
salingam, C. O. Hughes, R. Raine, J. Hughes, D. A. Sim, C. Egan, A. Tufail, H. Montgomery,
D. Hassabis, G. Rees, T. Back, P. T. Khaw, M. Suleyman, J. Cornebise, P. A. Keane, and O. Ron-
neberger, “Clinically applicable deep learning for diagnosis and referral in retinal disease,”
Nature Medicine, vol. 24, pp. 1342–1350, Sept. 2018.
[13] E. J. Beck, W. Gill, and P. R. De Lay, “Protecting the conﬁdentiality and security of personal
health information in low- and middle-income countries in the era of SDGs and Big Data,”
Global Health Action, vol. 9, p. 32089, 2016.
[14] P. Rajpurkar, A. Y. Hannun, M. Haghpanahi, C. Bourn, and A. Y. Ng, “Cardiologist-Level
Arrhythmia Detection with Convolutional Neural Networks,” arXiv:1707.01836, July 2017.
[15] S. P. Shashikumar, A. J. Shah, G. D. Clifford, and S. Nemati, “Detection of Paroxysmal Atrial
Fibrillation Using Attention-based Bidirectional Recurrent Neural Networks,” in Proceedings
of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining,
KDD ’18, (New York, NY, USA), pp. 715–723, ACM, 2018.
[16] R. Sassi, R. R. Bond, A. Cairns, D. D. Finlay, D. Guldenring, G. Libretti, L. Isola, M. Vaglio,
R. Poeta, M. Campana, C. Cuccia, and F. Badilini, “PDF-ECG in clinical practice: A model
for long-term preservation of digital 12-lead ECG data,” Journal of Electrocardiology, vol. 50,
no. 6, pp. 776–780, 2017 Nov - Dec.
[17] A. Lyon, A. Mincholé, J. P. Martínez, P. Laguna, and B. Rodriguez, “Computational techniques
for ECG analysis and interpretation in light of their contribution to medical advances,” Journal
of the Royal Society Interface, vol. 15, Jan. 2018.
[18] J. Mant, D. A. Fitzmaurice, F. D. R. Hobbs, S. Jowett, E. T. Murray, R. Holder, M. Davies,
and G. Y. H. Lip, “Accuracy of diagnosing atrial ﬁbrillation on electrocardiogram by primary
care practitioners and interpretative diagnostic software: Analysis of data from screening for
atrial ﬁbrillation in the elderly (SAFE) trial,” BMJ (Clinical research ed.), vol. 335, p. 380, Aug.
2007.
[19] G. Veronese, F. Germini, S. Ingrassia, O. Cutuli, V. Donati, L. Bonacchini, M. Marcucci, A. Fab-
bri, and Italian Society of Emergency Medicine (SIMEU), “Emergency physician accuracy in
interpreting electrocardiograms with potential ST-segment elevation myocardial infarction: Is it
enough?,” Acute Cardiac Care, vol. 18, pp. 7–10, Mar. 2016.
[20] World Health Organization, Global Status Report on Noncommunicable Diseases 2014: At-
taining the Nine Global Noncommunicable Diseases Targets; a Shared Responsibility. Geneva:
World Health Organization, 2014. OCLC: 907517003.
[21] P. W. Macfarlane, B. Devine, and E. Clark, “The university of glasgow (Uni-G) ECG analysis
program,” in Computers in Cardiology, 2005, pp. 451–454, 2005.
[22] S. H. Jambukia, V. K. Dabhi, and H. B. Prajapati, “Classiﬁcation of ECG signals using machine
learning techniques: A survey,” in 2015 International Conference on Advances in Computer
Engineering and Applications, (Ghaziabad, India), pp. 714–721, IEEE, Mar. 2015.
[23] M. A. Rahhal, Y. Bazi, H. AlHichri, N. Alajlan, F. Melgani, and R. Yager, “Deep learning
approach for active classiﬁcation of electrocardiogram signals,” Information Sciences, vol. 345,
pp. 340–354, June 2016.
[24] J. Rubin, S. Parvaneh, A. Rahman, B. Conroy, and S. Babaeizadeh, “Densely Connected
Convolutional Networks and Signal Quality Analysis to Detect Atrial Fibrillation Using Short
Single-Lead ECG Recordings,” arXiv:1710.05817, Oct. 2017.
[25] U. R. Acharya, H. Fujita, S. L. Oh, Y. Hagiwara, J. H. Tan, and M. Adam, “Application of
deep convolutional neural network for automated detection of myocardial infarction using ECG
signals,” Information Sciences, vol. 415-416, pp. 190–198, Nov. 2017.
6


## Page 7


[26] T. Teijeiro, C. A. Garcia, D. Castro, and P. Félix, “Arrhythmia Classiﬁcation from the Abductive
Interpretation of Short Single-Lead ECG Records,” in Computing in Cardiology, 2017, Sept.
2017.
[27] C. D. Cantwell, Y. Mohamied, K. N. Tzortzis, S. Garasto, C. Houston, R. A. Chowdhury, F. S.
Ng, A. A. Bharath, and N. S. Peters, “Rethinking multiscale cardiac electrophysiology with
machine learning and predictive modelling,” arXiv:1810.04227, Oct. 2018.
[28] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark,
J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, “PhysioBank, PhysioToolkit, and
PhysioNet,” Circulation, June 2000.
[29] G. D. Clifford, C. Liu, B. Moody, L.-w. H. Lehman, I. Silva, Q. Li, A. E. Johnson, and R. G.
Mark, “AF Classiﬁcation from a Short Single Lead ECG Recording: The PhysioNet/Computing
in Cardiology Challenge 2017,” Computing in Cardiology, vol. 44, Sept. 2017.
[30] K. He, X. Zhang, S. Ren, and J. Sun, “Deep Residual Learning for Image Recognition,”
arXiv:1512.03385, Dec. 2015.
[31] K. He, X. Zhang, S. Ren, and J. Sun, “Identity Mappings in Deep Residual Networks,”
arXiv:1603.05027, Mar. 2016.
[32] S. Ioffe and C. Szegedy, “Batch Normalization: Accelerating Deep Network Training by
Reducing Internal Covariate Shift,” arXiv:1502.03167, Feb. 2015.
[33] N. Srivastava, G. E. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, “Dropout:
A simple way to prevent neural networks from overﬁtting.,” Journal of Machine Learning
Research, vol. 15, no. 1, pp. 1929–1958, 2014.
[34] D. P. Kingma and J. Ba, “Adam: A Method for Stochastic Optimization,” arXiv:1412.6980,
Dec. 2014.
[35] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep into rectiﬁers: Surpassing human-level
performance on imagenet classiﬁcation,” in Proceedings of the IEEE International Conference
on Computer Vision, pp. 1026–1034, 2015.
A
Training data preprocessing
In this appendix, we detail the preprocessing of the data used for training and validating the model.
The exams were analyzed by doctors during routine workﬂow and are subject to medical errors,
moreover there might be errors associated with the semi-supervised methodology used to extract the
diagnoses. Hence, we combine the expert annotation with well established automatic classiﬁers to
improve the quality of the dataset. Given i) the exams in the database; ii) the diagnoses given by the
Glasgow and Minnesota automatic classiﬁers (automatic diagnosis); and, iii) the diagnoses extracted
from the expert free text associated with the exams using the unsupervised methodology (medical
diagnosis), the following procedure is used for obtaining the ground truth annotation:
1. We:
(a) Accept a diagnosis (consider an abnormality to be present) if both the expert and either
the Glasgow or the Minnesota automatic classiﬁers indicated the same abnormality.
(b) Reject a diagnosis (consider an abnormality to be absent) if only one classiﬁer indicates
the abnormality in disagreement with both the doctor and the other automatic classiﬁer.
After this initial step diagnoses there are two scenarios where we still need to accept or
reject diagnoses. They are: i) both classiﬁers indicate the abnormality but the expert doesn’t;
or ii) only the expert indicates the abnormality but no classiﬁer does.
2. We used some rules to reject some of the remaining diagnoses:
(a) Diagnoses of ST where the heart rate was below 100 (8376 medical diagnoses and 2
automatic diagnoses) were rejected.
7


## Page 8


(b) Diagnoses of SB where the heart rate was above 50 (7361 medical diagnoses and 16427
automatic diagnosis) were rejected.
(c) Diagnoses of LBBB or RBBB where the duration of the QRS interval was below 115
ms (9313 medical diagnoses for RBBB and 8260 for LBBB) were rejected.
(d) Diagnoses of 1dAVb where the duration of the PR interval was below 190 ms (3987
automatic diagnoses) were rejected.
3. Then, using the sensitivity analysis of 100 manually reviewed exams per abnormality, we
came up with the following rules to accept some diagnoses remaining:
(a) For RBBB, d1AVb, SB and ST we accepted all medical diagnoses. 26033, 13645,
12200 and 14604 diagnoses were accepted in such fashion, respectively
(b) For FA, we required not only that the exam was classiﬁed by the doctors as true but
also that the standard deviation of NN intervals was higher than 646. 14604 diagnoses
were accepted using this rule.
According to the sensitivity analysis the number of false positives that would be introduced
by this procedure was smaller than 3% of the total number of exams.
4. After this process, we were still left with a approximately 34000 exams whose diagnoses
had not been accepted or rejected. These were manually reviewed by medical students using
the Telehealth ECG diagnostic system. The process of manually reviewing these 34000
ECGs took several months.
B
ECG abnormalities
Table 2: Prevalence of each abnormality in the train/validation set and in the test set. It contains both
the percentage % and the absolute number of patients (in parentheses).
Abbrev.
Description
Prevalence
(Train+Val)
Prevalence (Test)
1dAVb
1st degree AV block
1.5 % (36,324)
3.5 % (33)
RBBB
Right bundle branch block
2.6% (64,319)
3.8 % (36)
LBBB
Left bundle branch block
1.5% (37,326)
3.5 % (33)
SB
Sinus bradycardia
1.6% (38,837)
2.3 % (22)
AF
Atrial ﬁbrilation
1.7% (42,133)
1.4 % (13)
ST
Sinus tachycardia
2.3% (56,186)
4.4 % (42)
8


## Page 9


Figure 2: A list of all the abnormalities the model classiﬁes. We show only 3 representative leads
(DII, V1 and V6).
9


## Page 10


C
Additional experiments
In Figure 3 we show the precision-recall curve for our model. This is a useful graphical representation
to assess the success of a prediction model when, as in our case, the classes are imbalanced. The
thresholds we used to generate Table 1 were chosen trying to get the inﬂection point of these curves.
And, for these same thresholds, Table 3 show the neural network confusion matrix for each of the
classes.
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Precision
(a) 1dAVb (average precision = 0.91)
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
(b) RBBB (average precision = 0.94)
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Precision
(c) LBBB (average precision = 1.00)
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
(d) SB (average precision = 0.87)
0.0
0.2
0.4
0.6
0.8
1.0
Recall
0.0
0.2
0.4
0.6
0.8
1.0
Precision
(e) AF (average precision = 0.90)
0.0
0.2
0.4
0.6
0.8
1.0
Recall
0.0
0.2
0.4
0.6
0.8
1.0
(f) ST (average precision = 0.96)
Figure 3: Precision-recall curve for our prediction model in the test set with regard to each ECG
abnormalities. The average precision (which is approximated by the area under the precision-recall
curve) is displayed in the captions.
10


## Page 11


Predicted Class
Predicted Class
Actual Class
1dAVb
Not 1dAVb
Actual Class
RBBB
Not RBBB
1dAVb
24
9
RBBB
36
0
Not 1dAVb
2
918
Not RBBB
5
912
Actual Class
LBBB
Not LBBB
Actual Class
SB
Not SB
LBBB
33
0
SB
19
3
Not LBBB
1
919
Not SB
5
926
Actual Class
AF
Not AF
Actual Class
ST
Not ST
AF
11
2
ST
40
2
Not AF
2
938
Not ST
6
905
Table 3: Confusion matrices for the neural network.
11

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
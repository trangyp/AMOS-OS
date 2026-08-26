---
canon-group: reference
rscf-state: source-claim
arxiv_id: 2503.17625v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 2503.17625v1_AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study

> Source: 2503.17625v1_AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study.pdf

> Pages: 17

---


## Page 1


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
75 
 
 
 
 
Research Paper 
 
AI-Based Screening for Depression and Social Anxiety Through Eye 
Tracking: An Exploratory Study. 
 
Karol Chlasta * 
Katarzyna Wisiecka ** 
Krzysztof Krejtz *** 
Izabela Krejtz **** 
 
 
ABSTRACT 
 
Well-being is a dynamic construct that evolves over time and fluctuates within individuals, presenting 
challenges for accurate quantification. Reduced well-being is often linked to depression or anxiety 
disorders, which are characterised by biases in visual attention towards specific stimuli, such as human 
faces. This paper introduces a novel approach to AI-assisted screening of affective disorders by 
analysing visual attention scan paths using convolutional neural networks (CNNs). Data were collected 
from two studies examining (1) attentional tendencies in individuals diagnosed with major depression 
and (2) social anxiety. These data were processed using residual CNNs through images generated from 
eye-gaze patterns. Experimental results, obtained with ResNet architectures, demonstrated an average 
accuracy of 48% for a three-class system and 62% for a two-class system. Based on these exploratory 
findings, we propose that this method could be employed in rapid, ecological, and effective mental 
health screening systems to assess well-being through eye-tracking.  
  
Keywords: Eye-tracking, Artificial intelligence, Convolutional neural networks, Depression, 
    
Social anxiety, Well-being 
 
 
 
 
 
______ 
 
* Kozminski University, Warsaw, Poland. Email: karol@chlasta.pl 
** University of Economics and Human Sciences, Warsaw, Poland. Email: k.wisiecka@vizja.pl 
*** SWPS University, Warsaw, Poland. Email: kkrejtz@swps.edu.pl 
**** SWPS University, Warsaw, Poland. Email: ikrejtz@swps.edu.pl 
 
 
 
International Journal of Marketing, Communication and New Media 
ISSN: 2182-9306. Special Issue on Marketing & Business Perspectives: Fostering AI as a 
Tool for Wellbeing, DECEMBER 2024 
 
DOI: https://doi.org/10.54663/2182-9306.2024.SpecialIssueMBP.75-91


## Page 2


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
76 
 
Received on:  2024.07.30 
Approved on: 2024.12.27 
Evaluated by a double-blind review system 
 
1. INTRODUCTION 
Well-being is a dynamic construct that changes over time and fluctuates within individuals, 
making it difficult to quantify (Sonnentag, 2015). This paper attempts to deepen our 
understanding of how predictive artificial intelligence (AI) methods can be applied to quantify 
person’s well-being. Although current methods, such as the WHO-5 questionnaire by Topp, 
Østergaard, Søndergaard, and Bech (2015), help explain respondents’ subjective well-being, we 
believe that future solutions should be more less subjective and more automated. They should be 
based not only on the self-assessment questionnaires, but also on the data gathered using a mental 
health screening system, that could leverage a range of digital technologies. This paper proposes 
a novel approach to quantify person’s well-being (or lack of thereof, when depression or social 
anxiety is present), using the well-established methods like eye tracking and convolutional neural 
networks (Sonnentag, 2015). 
Affective disorders may moderate typical patterns of facial emotional expressions. Several studies 
found that the natural bias to focus on positive stimuli, typically observed among non-dysphoric 
individuals, does not occur among dysphoric people (Ellis, Fischer, and Beevers, 2010); (Leyman, 
De Raedt, Vaeyens, & Philippaerts, 2011); (Sears, Newman, Ference, & Thomas, 2011). We are 
also typically attracted to those people who smile, and we tend to avoid people who express 
sadness (Van Kleef, Van Doorn, Heerdink, & Koning, 2011). 
Cognitive theories assume that attentional biases to negative emotional stimuli play an important 
role in the development and maintenance of depression (Armstrong and Olatunji, 2012); (Clark, 
1999); (Foland-Ross & Gotlib, 2012); (Williams & Scott, 1988). Eye-tracking studies have found 
that depression is associated with an increased number of fixations spent on negative information 
(Caseras, Garner, Bradley, & Mogg, 2007); (Eizenman et al., 2003); (Kellough, Beevers, Ellis, & 
Wells, 2008), and a decreased amount of time spent looking at positive stimuli (De Raedt & 
Koster, 2010); (Peckham, McHugh, & Otto, 2010). Dysphoric individuals are also slower in 
disengaging visual attention from depression-related images (Sears, Thomas, LeHuquet, & 
Johnson, 2010). Sanchez (2013) Sanchez, Vazquez, Marker, LeMoult, & Joormann (2013)


## Page 3


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
77 
showed that participants with Major Depressive Disorder (MDD) compared to control participants 
disengaged significantly longer from sad faces. Duque and Vázquez (2015) revealed that 
compared to non-depressive, participants, those with MDD showed also a negative bias for sad 
faces in attentional maintenance indices (i.e. first fixation duration and total fixation time). 
Furthermore, the MDD group spent a marginally less amount of time viewing happy faces 
compared to the non-depressive group. 
These attention biases are usually observed using valenced facial emotional expressions as stimuli 
(Armstrong & Olatunji, 2012). Tedious processing of social stimuli leads to more persistent 
negative affect (Disner, Shumake, & Beevers, 2017). Processing of social stimuli has been found 
to be related to greater rumination in depressed individuals (Donaldson, Lam, & Mathews, 2007); 
(Owens & Gibb, 2017) and a decrease in self-esteem among socially anxious individuals (Iancu, 
Bodner, & Ben-Zion, 2015). 
Cognitive models of social anxiety (Clark & Wells, 1995); (Rapee & Heimberg, 1997) also 
underline the role of biased processing of socially threatening information in the development of 
this disorder. Attentional biases in anxious individuals are guided by two theoretical approaches: 
the vigilance hypothesis, and/or the maintenance hypothesis. The vigilance hypothesis predicts 
faster orienting toward threat related stimuli. The maintenance hypothesis suggests difficulty in 
disengaging attention from threat. 
What combines the vigilance and maintenance approach is the emotional withdrawal from 
processing threatening facial expressions. For example, social phobics have been found to exhibit 
greater hyperscanning of face stimuli than controls (Horley, Williams, Gonsalvez, & Gordon, 
2003, 2004). This hyperscanning strategy, reflected by an increase in scan path length may suggest 
ambient processing of facial emotional expressions (Krejtz et al., 2018). 
The present study examines the automated depression and social anxiety detection in eye 
movements (scan paths) using deep learning among adults. We expect that eye movements during 
free viewing of emotional expressions can be a good predictor of these disorders. 
 
2. MATERIAL AND METHODS 
2.1 Participants 
The database contains eye-tracking data collected during two studies evaluating: (1) attentional 
tendencies among individuals diagnosed with depression (Holas, Krejtz, Wisiecka, Rusanowska,


## Page 4


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
78 
& Nezlek, 2020) and (2) social anxiety (Krejtz et al., 2018). Eligibility for the depression group 
required a diagnosis of a major depressive episode at the time of the study, determined using the 
Mini-International Neuropsychiatric Interview (MINI), a standard diagnostic tool for DSM-IV 
and ICD-10 (Sheehan et al., 1998). For the second, social anxiety group, participants first 
completed an online version of the Liebowitz Social Anxiety Scale (LSAS), a self-reported 
measure assessing fear and avoidance of social situations (Liebowitz, 1987). The LSAS has a total 
score range of 0 to 144, derived from the sum of fear and avoidance scores, with common 
thresholds for interpretation as follows: <55 indicates mild social anxiety, 55–65 moderate social 
anxiety, 66–80 marked social anxiety, 81–95 severe social anxiety, and >95 very severe social 
anxiety. Participants then completed the Centre for Epidemiological Studies-Depression Scale 
(CES-D), a 20-item inventory designed to measure depressive symptoms (Radloff, 1977). The 
CES-D has a total score range of 0 to 60, with scores of 16 or higher suggesting possible clinical 
depression and 27 or higher indicating a high level of depressive symptoms. 
Participants were invited to the laboratory for individual eye-tracking sessions based on their 
scores. Individuals were excluded from both studies if they had a current or lifetime psychotic 
disorder, bipolar disorder, substance abuse, or current suicidal tendencies. The sample contained 
53 depressive participants in total (39 Female, M age = 34.60, SD = 8.38) in the first study and 24 
socially anxious (19 Female, M age = 23.68, SD = 7.24) with 24 controls (17 Female, M age = 
25.76, SD = 6.64) in the second study, as described in Table 1. 
 
Table 1. Descriptive statistics of depression and social anxiety scales 
Group 
CES-D Score  
LSAS Score  
Anxious 
M = 25.67, SD = 11.12 
M = 78.92, SD = 13.68 
Control 
M = 15.75, SD = 8.62 
M = 32.83, SD = 13.44 
Depressive 
M = 43.59, SD = 6.67  
M = 71.06, SD = 23.65 
                    Note: M= Mean, SD= Standard Deviation  
  
2.2 Experimental Task 
Before participating in the experiments, participants signed an informed consent form and 
completed a 5-point calibration of the eye tracker. After that they were asked to free view a series 
of 12 slides. Each slide presented four categories of facial expressions: neutral, sad, angry, and


## Page 5


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
79 
happy expressed by the same person. There were 6 female and 6 male faces taken from the 
Karolinska Directed Emotional Faces database (Goeleven, De Raedt, Leyman, & Verschuere, 
2008). Each slide was presented for 10 seconds. Although 10 seconds might seem too long for a 
free viewing study, a 10-second stimulus display is frequently used in depression research with 
eye tracker (Armstrong & Olatunji, 2012). The slides were presented in the resolution of 
1680×1050 pixels in the viewing distance of 60 cm. 
2.3 Dataset Description and Pre-processing 
The eye movements were recorded with an SMI eye tracker at 120 Hz, as presented in Figure 1. 
Raw data were processed with SMI’s BeGaze software. SMI’s BeGaze dispersion-based algorithm 
was used for detection of fixations and saccades. Fixations were defined as stable eye movements, 
within 1 degree of visual angle, lasting for at least 80 ms. Fixations of duration 80–1200 ms were 
analysed as well as saccades of amplitude <10◦. 
 
 
         Figure 1. Experimental Setting and SMI 120 Hz eye tracker 
 
We selected a single slide from each free viewing session to ensure that the faces seen by 
participants were displayed. The visualisations of gaze patterns were extracted from BeGaze in a 
png format. We decided to extract scan paths with calculated fixations in Dataset A1, and raw 
scan path in Dataset B. In both approaches visualisations of gaze patterns were applied as an input 
to artificial neural networks.


## Page 6


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
80 
To balance the number of trials in each group the visualisations chosen for machine learning were 
selected based on calibration and data quality. In total we selected 60 scan path visualisations in 
Dataset A1 (scan paths and fixations), and 59 in Dataset B (raw scan paths), as presented in the 
below Figure 2. 
 
 
Figure 2. Exemplary scan paths of depressive participants before pre-processing 
 
One of our key considerations while applying machine learning algorithms to our problem was 
limited availability of data, which could cause the deep learning methods to capture the noise, 
rather than the predictive nature of the dataset. To overcome the problem, we added more data 
(by applying custom image augmentation using nine ImageMagick filters to create a larger 
Dataset A2), used batch normalisation, and regularisation in training neural networks (Shang, 
Chiu, and Sohn, 2017), and explored ResNet architectures with different complexities (from 18 
to 151 layers). 
Our initial approach was to extract eye-gaze patterns from the images to reduce the amount of 
noise that could affect the feature selection in the machine learning process. Extracting these 
patterns for scan paths with fixations drawn on faces (containing a level of opacity) proved to be 
a manual and time-consuming task with GIMP. Therefore, we decided to augment the data using 
image filters (Dataset A2), rather than denoise it by removing faces. As a result, we created three 
datasets A1, A2 and B that were used to train and test our approach. This allowed exploratory 
evaluation of both the method, and each dataset. 
For Datasets A1/A2 the image of each eye-gaze pattern was resized to fit a 224×224 px size. 
Standard Fastai (Howard and Gugger, 2020) transformations were applied at the time of training 
to create input for CNN. Additionally, a custom augmentation to increase the size of the dataset


## Page 7


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
81 
A1 was performed using a command-line ImageMagick (Still, 2006) to create a larger Dataset 
A2, as presented on Figure 3. 
 
 
     Figure 3. Demonstration of exemplary augmentations: gamma, negative, posterize (Dataset A2) 
 
Each image from Dataset A1 was enhanced with the following filters: negate, canny 10, posterize 
2, posterize 4, paint 1, paint 3, gamma 100, modulate 140, modulate 160. The filters were selected 
to retain the eye-gaze pattern in the image and applied on a folder with Dataset A1 images using 
a bash command1. 
For Dataset B, the image files were pre-processed with the GNU Image Manipulation Program 
(GIMP) (Van Gumster & Shimonski, 2011). We extracted the scan paths from each image, so that 
our method could identify key characteristics of eye-gaze patterns in the training data, and later 
match them in the test data. The image of each eye-gaze pattern was resized to fit 448×448 px 
size and saved in colour with a transparent background to create input for machine learning, as 
presented in Figure 4. 
 
        Figure 4. Sample image presenting raw scan path generated by an anxious participant (Dataset B) 
 
1 for file in *.png; do convert $file -filter $file; done


## Page 8


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
82 
Finally, the data were split into training and test sets by randomly assigning 80% of the items to 
the training set and 20% to the test set. 
 
Table 2. Number of samples in Dataset A1, extended Dataset A2 (Fixations) and in Dataset B (Scan paths) 
Category 
Dataset A1 
Dataset A2 
Dataset B 
Anxious 
20 
200 
24 
Control 
20 
200 
18 
Depressive 
20 
200 
17 
Total 
60 
600 
59 
 
2.4 Method 
Our method is based on deep CNNs (Krizhevsky, Sutskever, & Hinton, 2012), and built in Python 
as PyTorch models (Paszke et al., 2019). We extend the work presented in Chlasta et al. (2021), 
where a DemCNN model was 63.6% accurate in dementia screening. In the current study, we use 
graphical representation of all suitable eye-tracking data sourced from 53 depressive participants 
(39 Female, M age = 34.60, SD = 8.38), 24 socially anxious (19 Female, M age = 23.68, SD = 
7.24) with 24 controls (17 Female, M age = 25.76, SD = 6.64). 
We use this dataset to explore the transfer learning capabilities of ResNet-18, ResNet-34, ResNet-
50, ResNet-101, and ResNet-152 models, which employ a residual learning framework (He, 
Zhang, Ren, and Sun, 2016). We acknowledge that the use of recurrent networks for sequential 
data is intuitive; however, (1) the data we gathered were in the form of images, and (2) we 
anticipated that the predictive capabilities of the dataset would be more closely related to an 
overall 'map' of gaze patterns for a given task, rather than individual sequences of eye movements. 
The CNN models we employed conclude with several linear layers. The final convolutional layer 
extracts features from the image processed by the model and converts them into predictions for 
each output class. We utilised transfer learning by applying pre-trained weights from ImageNet 
(Deng et al., 2009) to all convolutional layers, while the final linear layers were randomly 
initialised. Fine-tuning was then conducted by unfreezing the entire model and re-training it on 
the target dataset. This methodology is detailed further in the Fastai library documentation 
(Howard & Gugger, 2020).


## Page 9


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
83 
3. RESULTS 
All our tests were performed in Python using Jupyter Notebook on Google Collaboratory 
platform. It enabled us to use Linux machines to run the code, and high performance nVidia Tesla 
V100 GPU for computations. We used PyTorch version 1.3.1+cu100, and fast.ai version 1.0.59 
libraries for neural network training. We achieved accuracy of 48% for the three-class system and 
62% for the two-class classification system, as presented in Table 3. 
 
Table 3. Summary of classification results for different CNN architectures on Datasets A1 & A2 
(Fixations) and Dataset B (Scan paths) 
Architecture 
Classes  
Accuracy 
ResNet-18 
ResNet-34 
(Dataset A1) C, D 
(Dataset A1) C, D 
62.5% 
50% 
ResNet-18 
ResNet-50 
(Dataset A1) A, C, D 
(Dataset A1) A, C, D 
41.7% 
58.3% 
ResNet-18 
ResNet-50 
(Dataset A2) C, D 
(Dataset A2) C, D 
55% 
53.8% 
ResNet-18 
ResNet-50 
ResNet-50 
(Dataset A2) A, C, D 
(Dataset A2) A, C, D 
(Dataset A2 448px) A, C, D 
35% 
27.5% 
48.3% 
ResNet-18 
ResNet-18 
(Dataset B) C, D 
(Dataset B) A, D 
85.7% 
50% 
ResNet-18 
ResNet-34 
ResNet-50 
ResNet-101 
ResNet-151 
(Dataset B) A, C, D 
(Dataset B) A, C, D 
(Dataset B) A, C, D 
(Dataset B) A, C, D 
(Dataset B) A, C, D 
45% 
54.5% 
63.6% 
45% 
63.6% 
                     Note: Groups: C - Control, D - Depressive, A – Anxious 
 
ResNet-18 network trained on Dataset B achieved the classification accuracy of 85.7%, but in the 
subsequent runs with a random train/test split that model achieved a much lower average accuracy 
of around 60%. The results indicate that our approach can differentiate between affective 
disorders and a control group. We also see that an increase in the number of the layers of ResNet


## Page 10


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
84 
does not automatically improve the results (e.g. simpler ResNet-18 and more complex ResNet-
101 produce the same classification results). 
Social anxiety and depression proved difficult to distinguish between each other. To investigate 
that further we repeated the ResNet-18 classification on randomised Dataset B five times (reduced 
to anxious and depressive participants) and received an average accuracy of 50%. The ResNet-50 
systems have achieved consistently better classification results reaching 63.6%. They classified 
seven out of eleven people correctly, with only four people classified incorrectly (Figure 5). 
 
 
Figure 5. Confusion matrices presenting results for ResNet-34 system (Accuracy of 54.5%) and ResNet-
50 (Accuracy of 63.6%) on Dataset B (Scan paths) 
 
Figure 6. Confusion matrices presenting results for ResNet-34 system (Accuracy of 50%) and ResNet-50 
system (Accuracy of 58.3%) on Dataset A1


## Page 11


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
85 
 
Figure 7. Confusion matrices presenting results for ResNet-50 system using image size of 224x224px 
(Accuracy of 27.5%) and 448x480px (Accuracy of 48.3%) on Dataset A2 
 
The CNN systems using a much larger Dataset A2 (see Table 2) did not produce better results 
than those fed with images of clean, raw scan paths of Dataset B. Extracting gaze pattern proves 
to be the best way to reduce noise in deep learning approach and could be explored further. The 
selected confusion matrices for both configurations are presented in Figures 6 and 7. 
 
4. DISCUSSION 
The main contribution of the present paper is the first attempt to build a three-class computer-
based system for screening of affective disorders, depression, and social anxiety, from gaze scan 
paths. This technique could complement traditional diagnostic methods, such as questionnaires 
and structured interviews. Unlike screenings for organic diseases, where false positives waste 
resources and cause anxiety, depression screening can identify subthreshold symptoms warranting 
follow-up (Zeng et al., 2024). 
Recent studies have highlighted the potential of eye-tracking as a tool for identifying psychiatric 
disorders. For example, a recent eye-tracking study found that patients with depression exhibit 
distinct eye movement patterns compared to healthy controls, suggesting that these features could 
serve as biomarkers for depressive disorders. While Gao et al. (2023) propose eye movement 
recognition as a supplementary method for diagnosing depression, their study did not report the 
accuracy of classification models.


## Page 12


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
86 
In another study, Kim et al. (2024) applied deep learning methods to classify psychosis and 
obsessive-compulsive disorder. Using a Long Short-Term Memory (LSTM) model implemented 
in Python with PyTorch, they achieved a binary classification accuracy of 80.7%. Their findings 
demonstrate that eye-tracking-based deep learning models can directly and rapidly identify 
impaired executive function during visuospatial memory encoding, underscoring the applicability 
of this approach across a range of psychiatric and neurological conditions. 
By comparison to the LSTM model, our model achieved lower accuracies of 48% for a three-
class system and 62% for a two-class system, primarily due to being trained on a smaller dataset. 
Nevertheless, these results support the feasibility of using eye-tracking data in AI-driven 
diagnostic tools. Future research should focus on expanding datasets and refining models to 
enhance classification accuracy and broaden the applicability of this technology to organisational 
and clinical settings. 
The Choi et al. (2024) study focuses on utilizing digital phenotypes and feature representation 
learning to classify social anxiety disorder. Their study achieved impressive accuracy in 
predicting the severity of social anxiety symptoms, with an 87% accuracy for the primary 
symptoms, but uses completely different dataset based on multiple digital phenotypes like app 
usage, phone usage, call patterns, call logs, movement patterns, environmental patterns, and 
physiological patterns. Obviously, such a dataset gathered over a 7 to 13-week period will have 
more predictive power than our dataset, which is based solely on scan paths generated as a result 
of a free viewing task. 
We tested five CNN architectures to choose the most suitable one. The results showed that 
ResNet-50 models achieved higher predication accuracy than ResNet-18 models for both 
depression and social anxiety classes. The method is fast, and computations related to training of 
our ResNet-150 model on small Dataset B using nVidia Tesla V100 GPU took 4 minutes only, 
whereas the average training time for ResNet-50 on a larger Dataset A2 was 15 minutes. Table 3 
compares our method with other recent studies in the field.


## Page 13


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
87 
Table 4. Comparison of recent studies focusing on similar mental health screening systems 
Study 
Year 
Disorder 
Methodology 
Key Findings 
Accuracy 
Gao 
et 
al. 
2023 
Depression 
only 
Statistical 
analysis of Eye-
tracking data 
Eye movement features 
differ in patients with 
depression, 
suggesting 
biomarkers 
Accuracy not 
reported 
Kim 
et 
al. 
2024 
Psychosis 
and OCD 
LSTM model for 
binary 
classification 
Eye-tracking 
deep 
learning models identify 
executive 
function 
impairment in psychosis 
and OCD 
80.7% 
(binary 
classification) 
Abinaya 
& 
Vadivu 
2024 
Social 
Anxiety 
only 
 
Machine learning, 
clustering, 
data 
exploration 
Identified 
subgroups 
with social anxiety using 
SPIN 
questionnaire; 
suggests VR and AR for 
therapy 
Not 
applicable 
(focus 
on 
clustering and 
machine 
learning) 
Choi et 
al. 
2024 
Social 
Anxiety 
only 
Digital 
phenotypes, 
feature 
representation 
learning 
Achieved 87% accuracy 
for 
predicting 
social 
anxiety severity using 
mobile phones and seven 
digital phenotypes 
87% (binary 
classification) 
Our 
Study 
2024 
Depression 
and Social 
Anxiety 
CNN 
(ResNet) 
models for binary 
and 
three-class 
classification 
(Python, 
PyTorch) 
Classifying 
depression 
and social anxiety using 
eye-tracking data (scan 
paths of visual attention) 
gathered during a 10-
second free viewing task 
48% 
(three-
class system), 
62% (binary 
classification) 
 
Although the selected augmentation of the datasets did not visibly improve the efficiency of the 
models, the result suggests that if transfer learning is used, even a small sample of a few hundred 
images (in our case a 600 sample) can be sufficient to predict the distortion of typical attention 
biases from scan paths of visual attention.


## Page 14


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
88 
5. CONCLUSION 
The results of this study show that gaze-pattern classification is a promising method to quantify 
person’s well-being through screening of affective disorders. Although the preliminary tests met 
our expectations, the approach can be improved further by generating better data using generative 
adversarial networks, and retraining the models on a larger, more balanced dataset. Adversarial 
networks, consisting of two neural networks—a generator and a discriminator—that are trained 
simultaneously in a competitive framework where the generator aims to create realistic data 
instances, and the discriminator attempts to distinguish between real and generated instances, are 
still state-of-the-art in image data generation (Goodfellow et al., 2020). Another option for future 
work is to re-evaluate the newer CNN architectures, that were proven useful in medical image 
classification (Iqbal, N. Qureshi, Li, & Mahmood, 2023). 
To conclude, we demonstrated a proof-of-concept and its practical applicability for gaze-based 
classification of social anxiety and depression. We propose that this computer-based method, 
designed to predict attentional biases, could serve as a foundation for an innovative mental health 
screening system. In the future, such systems could be developed using affordable and accurate 
eye-trackers integrated into virtual reality headsets, enabling organisations to proactively monitor 
and support employee well-being while fostering healthier and more productive work 
environments. 
 
ACKNOWLEDGEMENTS 
We thank Michael Connolly for proofreading. 
 
REFERENCES  
Abinaya, M., & Vadivu, G. (2024). Identification of Social Anxiety in High School: A Machine 
Learning Approaches to Real-Time Analysis of Student Characteristics. IEEE Access. 
Armstrong, T., & Olatunji, B. (2012). Eye Tracking of Attention in the Affective Disorders: a Meta-
Analytic Review and Synthesis. Clinical Psychology Review, 32, 704—723. 
Caseras, X., Garner, M., Bradley, B. P., & Mogg, K. (2007). Biases in visual orienting to negative 
and positive scenes in dysphoria: An eye movement study. Journal of Abnormal Psychology, 
116(3), 491. 
Chlasta, K., & Wołk, K. (2021). Towards computer-based automated screening of dementia 
through spontaneous speech. Frontiers in Psychology, 11, 623237.


## Page 15


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
89 
Choi, H., Cho, Y., Min, C., Kim, K., Kim, E., Lee, S., & Kim, J. J. (2024). Multiclassification of 
the symptom severity of social anxiety disorder using digital phenotypes and feature representation 
learning. Digital Health, 10, 20552076241256730. 
Clark, D. M. (1999). Anxiety disorders: Why they persist and how to treat them. Behaviour 
Research and Therapy, 37(1), S5. 
Clark, D. M., & Wells, A. (1995). A Cognitive Model of Social Phobia. Social Phobia: Diagnosis, 
Assessment, and Treatment, 41(68), 00022–3. 
Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., & Fei-Fei, L. (2009). ImageNet: A Large-Scale 
Hierarchical Image Database. In Cvpr09. 
De Raedt, R., & Koster, E. H. (2010). Understanding vulnerability for depression from a cognitive 
neuroscience perspective: A reappraisal of attentional factors and a new conceptual framework. 
Cognitive, Affective, & Behavioral Neuroscience, 10(1), 50–70. 
Disner, S. G., Shumake, J. D., & Beevers, C. G. (2017). Self-referential schemas and attentional 
bias predict severity and naturalistic course of depression symptoms. Cognition and Emotion, 
31(4), 632–644. 
Donaldson, C., Lam, D., & Mathews, A. (2007). Rumination and attention in major depression. 
Behaviour Research and Therapy, 45(11), 2664–2678. 
Duque, A., & Vázquez, C. (2015). Double attention bias for positive and negative emotional faces 
in clinical depression: Evidence from an eye-tracking study. Journal of Behavior Therapy and 
Experimental Psychiatry, 46, 107–114. 
Eizenman, M., Lawrence, H. Y., Grupp, L., Eizenman, E., Ellenbogen, M., Gemar, M., & Levitan, 
R. D. (2003). A naturalistic visual scanning approach to assess selective attention in major 
depressive disorder. Psychiatry research, 118(2), 117–128. 
Ellis, A. J., Fischer, K. M., & Beevers, C. G. (2010). Is dysphoria about being red and blue? 
potentiation of anger and reduced distress tolerance among dysphoric individuals. Cognition & 
Emotion, 24(4), 596–608. 
Foland-Ross, L. C., & Gotlib, I. H. (2012). Cognitive and neural aspects of information processing 
in major depressive disorder: an integrative perspective. Frontiers in Psychology, 3, 489. 
Gao, M., Xin, R., Wang, Q., Gao, D., Wang, J., & Yu, Y. (2023). Abnormal eye movement features 
in patients with depression: Preliminary findings based on eye tracking technology. General 
Hospital Psychiatry, 84, 25-30. 
Goeleven, E., De Raedt, R., Leyman, L., & Verschuere, B. (2008). The karolinska directed 
emotional faces: a validation study. Cognition and emotion, 22(6), 1094–1118. 
Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., ... Bengio, Y. 
(2020). Generative adversarial networks. Communications of the ACM, 63(11), 139–144. 
He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In The 
IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (pp. 770–778). 
Holas, P., Krejtz, I., Wisiecka, K., Rusanowska, M., & Nezlek, J. B. (2020). Modification of 
attentional bias to emotional faces following mindfulness-based cognitive therapy in people with a 
current depression. Mindfulness, 1–11. 
Horley, K., Williams, L. M., Gonsalvez, C., & Gordon, E. (2003). Social Phobics do not see eye to 
eye: a Visual Scanpath Study of Emotional Expression Processing. Journal of Anxiety Disorders, 
17(1), 33–44.


## Page 16


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
90 
Horley, K., Williams, L. M., Gonsalvez, C., & Gordon, E. (2004). Face to Face: Visual Scanpath 
Evidence for Abnormal Processing of Facial Expressions in Social Phobia. Psychiatry Research, 
127(1), 43–53. 
Howard, J., & Gugger, S. (2020). Fastai: A layered api for deep learning. Information, 11(2), 108. 
Iancu, I., Bodner, E., & Ben-Zion, I. Z. (2015). Self-esteem, dependency, self-efficacy and self-
criticism in social anxiety disorder. Comprehensive psychiatry, 58, 165–171. 
Iqbal, S., N. Qureshi, A., Li, J., & Mahmood, T. (2023). On the analyses of medical images using 
traditional machine learning techniques and convolutional neural networks. Archives of 
Computational Methods in Engineering, 30(5), 3173–3233. 
Kellough, J. L., Beevers, C. G., Ellis, A. J., & Wells, T. T. (2008). Time course of selective attention 
in clinically depressed young adults: An eye tracking study. Behaviour research and therapy, 
46(11), 1238–1243. 
Kim, M., Lee, J., Lee, S. Y., Ha, M., Park, I., Jang, J., ... & Kwon, J. S. (2024). Development of an 
eye-tracking system based on a deep learning model to assess executive function in patients with 
mental illnesses. Scientific Reports, 14(1), 18186. 
Krejtz, K., Wisiecka, K., Krejtz, I., Holas, P., Olszanowski, M., & Duchowski, A. T. (2018). 
Dynamics of Emotional Facial Expression Recognition in Individuals with Social Anxiety. In 
Proceedings of the 2018 ACM Symposium on Eye Tracking Research & Applications (pp. 43:1–
43:9). New York, NY, USA: ACM. doi: 10.1145/3204493.3204533 
Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep 
convolutional neural networks. In F. Pereira, C. J. C. Burges, L. Bottou, & K. Q. Weinberger (Eds.), 
Advances in neural information processing systems 25 (pp. 1097–1105). Curran Associates, Inc. 
Leyman, L., De Raedt, R., Vaeyens, R., & Philippaerts, R. M. (2011). Attention for emotional facial 
expressions in dysphoria: An eye-movement registration study. Cognition and Emotion, 25(1), 
111–120. 
Liebowitz, M. R. (1987). Social Phobia. In K. D.F. (Ed.), Anxiety (Vol. 22, pp. 141–173). Karger 
Publishers. 
Owens, M., & Gibb, B. E. (2017). Brooding rumination and attentional biases in currently non-
depressed individuals: An eye-tracking study. Cognition and Emotion, 31(5), 1062–1069. 
Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., ... others (2019). Pytorch: An 
imperative style, high-performance deep learning library. In Advances in neural information 
processing systems (pp. 8024–8035). 
Peckham, A. D., McHugh, R. K., & Otto, M. W. (2010). A meta-analysis of the magnitude of biased 
attention in depression. Depression and anxiety, 27(12), 1135–1142. 
Radloff, L. S. (1977). The CES-D Scale: A Self-Report Depression Scale for Research in the 
General Population. Applied Psychological Measurement, 1(3), 385–401. 
Rapee, R. M., & Heimberg, R. G. (1997). A Cognitive-behavioral Model of Anxiety in Social 
Phobia. Behaviour Research and Therapy, 35(8), 741–756. 
Sanchez, A., Vazquez, C., Marker, C., LeMoult, J., & Joormann, J. (2013). Attentional 
disengagement predicts stress recovery in depression: An eye-tracking study. Journal of Abnormal 
Psychology, 122(2), 303. 
Sears, C. R., Newman, K. R., Ference, J. D., & Thomas, C. L. (2011). Attention to emotional 
images in previously depressed individuals: An eye-tracking study. Cognitive Therapy and 
Research, 35(6), 517–528.


## Page 17


AI-Based Screening for Depression and Social Anxiety Through Eye Tracking: An Exploratory Study. 
International Journal of Marketing, Communication and New Media. ISSN: 2182-9306. Special Issue on MBP, DECEMBER 2024. 
91 
Sears, C. R., Thomas, C. L., LeHuquet, J. M., & Johnson, J. C. (2010). Attentional biases in 
dysphoria: An eye-tracking study of the allocation and disengagement of attention. Cognition and 
Emotion, 24(8), 1349–1368. 
Sheehan, D. V., Lecrubier, Y., Sheehan, K. H., Amorim, P., Janavs, J., Weiller, E., ... & Dunbar, 
G. C. (1998). The Mini-International Neuropsychiatric Interview (MINI): the development and 
validation of a structured diagnostic psychiatric interview for DSM-IV and ICD-10. Journal of 
clinical psychiatry, 59(20), 22-33. 
Shang, W., Chiu, J., & Sohn, K. (2017). Exploring normalization in deep residual networks with 
concatenated rectified linear units. In Thirty-first AAAI Conference on Artificial Intelligence. 
Sonnentag, S. (2015). Dynamics of well-being. Annu. Rev. Organ. Psychol. Organ. Behav., 2(1), 
261–293. 
Still, M. (2006). The definitive guide to ImageMagick. Apress. 
Topp, C. W., Østergaard, S. D., Søndergaard, S., & Bech, P. (2015). The who-5 well-being index: 
a systematic review of the literature. Psychotherapy and psychosomatics, 84(3), 167–176. 
Van Gumster, J., & Shimonski, R. (2011). GIMP bible. John Wiley and Sons. 
Van Kleef, G. A., Van Doorn, E. A., Heerdink, M. W., & Koning, L. F. (2011). Emotion is for 
influence. European Review of Social Psychology, 22(1), 114–163. 
Williams, J., & Scott, J. (1988). Autobiographical memory in depression. Psychological medicine, 
18(3), 689–695. 
Zeng, Z., Li, Q., Caine, E. D., Takwoingi, Y., Zhong, B., Tong, Y., ... & Gong, W. (2024). 
Prevalence of and optimal screening tool for postpartum depression in a community-based 
population in China. Journal of Affective Disorders, 348, 191-199. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
How to cite this article: 
Chlasta, K.; Wisiecka, K.;Krejtz, K.; & Krejtz, I. (2024). AI-Based Screening for Depression and Social 
Anxiety Through Eye Tracking: An Exploratory Study. International Journal of Marketing, 
Communication and New Media, Special Issue on Marketing & Business Perspectives: Fostering AI as a 
Tool for Wellbeing, December 2024, pp. 55-91.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.07683v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1902.07683v1_Modelling_and_Analysing_Behaviours_and_Emotions_via_Complex_User_Interactions

> Source: 1902.07683v1_Modelling_and_Analysing_Behaviours_and_Emotions_via_Complex_User_Interactions.pdf

> Pages: 176

---


## Page 1


Modelling and Analysing Behaviours and
Emotions via Complex User Interactions
Mohamed Mostafa Mohamed Sayed Ahmed
May 2018
arXiv:1902.07683v1  [cs.HC]  20 Feb 2019


## Page 2


Abstract
Over the past 15 years, the volume, richness and quality of data collected from the
combined social networking platforms has increased beyond all expectation, provid-
ing researchers from a variety of disciplines to use it in their research. Perhaps more
impactfully, it has provided the foundation for a range of new products and services,
transforming industries such as advertising and marketing, as well as bringing the chal-
lenges of sharing personal data into the public consciousness. But how to make sense
of the ever-increasing volume of big social data so that we can better understand and
improve the user experience in increasingly complex, data-driven digital systems. This
link with usability and the user experience of data-driven system bridges into the wider
ﬁeld of human-computer interaction (HCI), attracting interdisciplinary researchers as
we see the demand for consumer technologies, software and systems, as well as the in-
tegration of social networks into our everyday lives. The fact that the data largely posted
on social networks tends to be textual, provides a further link to linguistics, psychology
and psycholinguistics to better understand the relationship between human behaviours
ofﬂine and online.
In this thesis, we present a novel conceptual framework based on a complex digital
system using collected longitudinal datasets to predict system status based on the per-
sonality traits and emotions extracted from text posted by users. The system framework
was built using a dataset collected from an online scholarship system in which 2000 stu-
dents had their digital behaviour and social network behaviour collected for this study.
We contextualise this research project with a wider review and critical analysis of the
current psycholinguistics, artiﬁcial intelligence and human-computer interaction literat-
ure, which reveals a gap of mapping and understanding digital proﬁling against system
status.
Through developing and applying a hybrid approach of data science and data analysis
techniques to the datasets which ultimately led to the development of the novel concep-
tual model and PMSys system. The empirical foundation and validation is underpinned
by a chain of experiments exploring the association and interrelations between the key
parameters, linking back to the wider literature, which is used to improve the response
of the intelligent agents based on the reported errors, as well as predicting the emotions
raised by the user and selecting the appropriate answer. By extracting the user’s beha-
viour (personality traits and emotions), the proposed conceptual model predicted 68%
of the system statuses (idle, down, slow and error). Furthermore, a web-based applica-
tion was developed to simulate events to users and to verify the framework; this model


## Page 3


predicted 61% of the system statuses.
Alongside the wider academic dissemination of this work, features of this novel model
and system are currently being commercialised as part of an intelligent chatbot engine
to provides a customer services support to a range of commercial clients across a variety
of industrial sectors.
ii


## Page 4


Acknowledgements
Firstly, I would like to express my sincere gratitude to my advisor Prof. Tom Crick
MBE for his continuous support during my PhD study and related academic work – for
his patience, motivation, and immense knowledge. His guidance helped me throughout
the research and writing of this thesis; I could not have imagined having a better advisor
and mentor during this journey. Besides my advisor, I would like to thank my director
of studies Dr Jason Williams for always jumping in to help anytime and through my
academic career and for being a great head of a department. I would like to express
my special appreciation to Dr Giles Oatley for his massive support through the early
stages of my research and his guidance in my academic life. I would also like to thank
Dr Ana Calderon for always being there when needed for her insightful comments and
encouragement and continuous support on this journey at all levels.
My sincere thanks also go to Dr Yasser Elshayeb and Dr Ehab Abdelrahmen, for
their support during my early career start and for always being there, I am grateful for
their advice and support.
I would like to dedicate this thesis to my father, who always believed in me and
pushed me forward towards my goals, his guidance and encouragement were always
invaluable, I am forever grateful to him (may his soul rest in peace). My sincere thanks
to my mother, her prayer to me is what sustained me thus far. My brothers (Hossam and
Ahmed) and sisters (Hala and Heba) and all my family members for their continuing
support during my PhD journey.
Last but not least, words cannot express how grateful I am to my beloved wife
Marwa and my two darling daughters, I cannot thank her enough for her sacriﬁces,
companionship, love, support and encouragement you have provided in every minute of
this journey. I am beyond grateful to you – without your precious support it would not
be possible to ﬁnally complete this chapter of my life.


## Page 5


Contents
Abstract
i
List of Figures
vi
List of Tables
viii
List of Code Listings
1
1
Introduction
2
1.1
Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.2
Contribution to Knowledge . . . . . . . . . . . . . . . . . . . . . . . .
5
1.3
Publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.4
Ethics Approval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
1.5
Thesis Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2
Personality, Behaviour and Emotions
8
2.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2
Psycholinguistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3
Personality Theories
. . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.3.1
Cattell’s 16 Personality Factors
. . . . . . . . . . . . . . . . .
10
2.3.2
The Enneagram of Personality . . . . . . . . . . . . . . . . . .
11
2.3.3
Analytical Psychology (Jungian) . . . . . . . . . . . . . . . . .
12
2.3.4
Myers-Briggs Personality Types . . . . . . . . . . . . . . . . .
12
2.4
The “Big Five” Personality Traits . . . . . . . . . . . . . . . . . . . . .
12
2.4.1
Linking Online Social Networks and Personality . . . . . . . .
15
2.5
Language Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
2.5.1
Open Vocabulary Approaches . . . . . . . . . . . . . . . . . .
17
2.5.2
Closed Vocabulary Approaches
. . . . . . . . . . . . . . . . .
17
2.5.3
The Linguistic Inquiry and Word Count (LIWC) Tool . . . . . .
17
2.6
Cognitive Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
2.6.1
Emotional Intelligence . . . . . . . . . . . . . . . . . . . . . .
19
i


## Page 6


2.6.2
Self Assessment of Emotions
. . . . . . . . . . . . . . . . . .
21
2.6.3
Temporal Behaviour . . . . . . . . . . . . . . . . . . . . . . .
22
2.6.4
Applications of Cognitive Science . . . . . . . . . . . . . . . .
23
2.7
Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
3
Human-Computer Interaction
26
3.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.2
Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.3
User Experience and Usability . . . . . . . . . . . . . . . . . . . . . .
27
3.4
Usability of Complex Information Systems
. . . . . . . . . . . . . . .
29
3.4.1
System Events
. . . . . . . . . . . . . . . . . . . . . . . . . .
29
3.4.2
Response Times and Human Perceptions
. . . . . . . . . . . .
32
3.5
Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
4
Artiﬁcial Intelligence
34
4.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
4.2
Computational Intelligence . . . . . . . . . . . . . . . . . . . . . . . .
35
4.2.1
Neural Networks . . . . . . . . . . . . . . . . . . . . . . . . .
36
4.2.2
Natural Language Processing
. . . . . . . . . . . . . . . . . .
38
4.2.3
IBM Watson Tone Analyzer . . . . . . . . . . . . . . . . . . .
39
4.3
Machine Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
4.4
Classiﬁers and Regressions . . . . . . . . . . . . . . . . . . . . . . . .
41
4.4.1
Linear Regression
. . . . . . . . . . . . . . . . . . . . . . . .
42
4.4.2
Multiple Linear Regression . . . . . . . . . . . . . . . . . . . .
43
4.4.3
Ordinal Regression . . . . . . . . . . . . . . . . . . . . . . . .
44
4.4.4
Multinomial Logistics Regression . . . . . . . . . . . . . . . .
44
4.4.5
Binomial Logistic Regression
. . . . . . . . . . . . . . . . . .
44
4.4.6
Mahalanobis Distance
. . . . . . . . . . . . . . . . . . . . . .
44
4.4.7
Naive Bayes Classiﬁer . . . . . . . . . . . . . . . . . . . . . .
45
4.5
Sentiment Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
4.6
Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
5
Methodology
48
5.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
5.2
System Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
5.3
Data Sources and Workﬂows . . . . . . . . . . . . . . . . . . . . . . .
50
5.3.1
Motivation Letters
. . . . . . . . . . . . . . . . . . . . . . . .
51
5.3.2
Role of the Facebook Page . . . . . . . . . . . . . . . . . . . .
51
5.3.3
Help Desk Platform and Ticketing System . . . . . . . . . . . .
53
5.4
Identifying Computer System Status and Events . . . . . . . . . . . . .
53
5.4.1
Identifying System Status
. . . . . . . . . . . . . . . . . . . .
54
ii


## Page 7


5.5
Extracting Personality Traits . . . . . . . . . . . . . . . . . . . . . . .
58
5.5.1
Using the Mairesse Approach
. . . . . . . . . . . . . . . . . .
59
5.5.2
Rationale of Using the Big Five Personality Theory . . . . . . .
59
5.6
Extracting Emotions from Text . . . . . . . . . . . . . . . . . . . . . .
59
5.7
Mapping Facebook User Proﬁles . . . . . . . . . . . . . . . . . . . . .
60
5.8
Verifying Accuracy using the IBM Watson Tone Analyzer
. . . . . . .
63
5.8.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
5.8.2
Comparing Statistical Differences Between Traits . . . . . . . .
64
5.8.3
The Mann-Whitney U Test . . . . . . . . . . . . . . . . . . . .
65
5.8.4
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
5.9
Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
6
Empirical Grounding for the PMsys Engine
68
6.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
6.2
Proﬁling Complex Online Interactions . . . . . . . . . . . . . . . . . .
68
6.2.1
What Behaviour Can You Infer From a Digital Footprint?
. . .
68
6.2.2
Parameters and Feature Extraction . . . . . . . . . . . . . . . .
69
6.2.3
Relating a User’s Digital Behaviour and Personality Traits . . .
70
6.2.4
Extracting LIWC Data Features . . . . . . . . . . . . . . . . .
72
6.2.5
Discussion
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
76
6.3
Mapping User Behaviour to System Stages
. . . . . . . . . . . . . . .
77
6.3.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
6.3.2
Binomial Logistic Regression (Logistic Regression)
. . . . . .
83
6.3.3
Key Findings and Discussion . . . . . . . . . . . . . . . . . . .
84
6.4
Relationship Between Personality Traits and Emotion . . . . . . . . . .
85
6.4.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . .
85
6.4.2
Personality Traits and Temporal Behaviour . . . . . . . . . . .
86
6.4.3
Association between Personality Traits and Six Basic Emotions
88
6.4.4
Discussion
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
89
6.5
Investigating Behavioural and Emotional Change . . . . . . . . . . . .
90
6.5.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . .
90
6.5.2
Ordinal Regression Analysis . . . . . . . . . . . . . . . . . . .
90
6.5.3
Multinomial Logistics Regression . . . . . . . . . . . . . . . .
95
6.5.4
Key Findings and Discussion . . . . . . . . . . . . . . . . . . .
97
6.6
Incorporating Emotion and Personality-Based Analysis in User-centered
Modelling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
98
6.6.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . .
98
6.6.2
Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
6.6.3
Key Findings . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.6.4
Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . 106
6.7
Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
iii


## Page 8


7
Developing the Conceptual Framework for the PMSys Engine
108
7.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
7.2
Personality Traits vs. Emotions, Gender and Age
. . . . . . . . . . . . 108
7.2.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
7.2.2
Binomial Logistic Regression
. . . . . . . . . . . . . . . . . . 109
7.2.3
Pearson’s Partial Correlation . . . . . . . . . . . . . . . . . . . 111
7.2.4
Rationale of using Random Forest Tree . . . . . . . . . . . . . 116
7.2.5
Key Findings . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
7.3
Model Veriﬁcation: Observing Emotions in Real Time
. . . . . . . . . 118
7.3.1
Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
7.3.2
Web-Based Veriﬁcation Tool . . . . . . . . . . . . . . . . . . . 118
7.3.3
Dataset Veriﬁcation . . . . . . . . . . . . . . . . . . . . . . . . 122
7.3.4
Key Findings . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
7.4
Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
8
Experimental Meta-Analysis
126
8.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
8.2
Proﬁling Complex Online Interactions . . . . . . . . . . . . . . . . . . 126
8.3
Mapping User Behaviour to System Stages
. . . . . . . . . . . . . . . 126
8.4
Verifying Accuracy using the IBM Watson Tone Analyzer
. . . . . . . 127
8.5
Personality Traits and Temporal Behaviour
. . . . . . . . . . . . . . . 127
8.6
Mapping User Behaviour to System Stages
. . . . . . . . . . . . . . . 128
8.7
Investigating Behavioural and Emotional Change . . . . . . . . . . . . 128
8.8
Personality Traits vs. Emotions, Gender and Age
. . . . . . . . . . . . 128
8.9
Model Veriﬁcation: Observing Emotions in Real Time
. . . . . . . . . 129
8.10 Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
9
Conclusions and Future Work
131
9.1
Main Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
9.2
Limitations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
9.3
Commercialisation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
9.4
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
iv


## Page 9


List of Figures
1.1
Intersection of the key research areas for this thesis . . . . . . . . . . .
3
2.1
The “Big Five” personality traits, describing individual personality dif-
ferences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
2.2
The Self-Assessment Manikin (SAM) . . . . . . . . . . . . . . . . . .
21
2.3
The “Affective Slider” (AS) . . . . . . . . . . . . . . . . . . . . . . . .
22
5.1
Joomla! Framework Architecture . . . . . . . . . . . . . . . . . . . . .
49
5.2
MVC Framework Architecture . . . . . . . . . . . . . . . . . . . . . .
49
5.3
Average server response (in seconds) on 8 January 2012 . . . . . . . . .
54
5.4
Algorithm to match users from Facebook with users on our system . . .
61
5.5
Usage of username in a post
. . . . . . . . . . . . . . . . . . . . . . .
62
5.6
Usage of username in a post following is after username
. . . . . . . .
62
5.7
Population pyramid representing personality traits . . . . . . . . . . . .
67
6.1
Seven example user time-lines . . . . . . . . . . . . . . . . . . . . . .
71
6.2
Key ﬁndings: Extraversion . . . . . . . . . . . . . . . . . . . . . . . .
74
6.3
Key ﬁndings: Emotional Stability
. . . . . . . . . . . . . . . . . . . .
74
6.4
Key ﬁndings: Agreeableness . . . . . . . . . . . . . . . . . . . . . . .
75
6.5
Key ﬁndings: Conscientiousness . . . . . . . . . . . . . . . . . . . . .
75
6.6
Key ﬁndings: Openness to Experience . . . . . . . . . . . . . . . . . .
76
6.7
Normal P-P Plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
6.8
Scatterplot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
6.9
Timestamp of two users with respect to proposed stages . . . . . . . . .
81
6.10 Normal Q-Q plot for Big Five traits and basic emotion
. . . . . . . . .
89
6.11 Google Analytics proﬁle showing behaviour of the system over a 24
hour period
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
6.12 Overall emotion tone response to server failure/idle status . . . . . . . . 100
6.13 Scatter plot of Big Five dimension “Openness” and social emotion tones 102
6.14 Scatter plot of Big Five dimension “Extraversion” and social emotion
tones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
v


## Page 10


6.15 Scatter plot of Big Five dimension “Conscientiousness” and social emo-
tion tones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
6.16 Scatter plot of Big Five dimension “Neuroticism” and social emotion
tones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
6.17 Scatter plot of Big Five dimension “Agreeableness” and social emotion
tones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
7.1
Developing PMsys engine stages . . . . . . . . . . . . . . . . . . . . . 109
7.2
Veriﬁcation stages illustration . . . . . . . . . . . . . . . . . . . . . . . 119
7.3
Big Five Questionnaire (Web Version) . . . . . . . . . . . . . . . . . . 120
7.4
Big Five Questionnaire Output sample (Web Version) . . . . . . . . . . 121
7.5
Triggering slow event as part of the simulation . . . . . . . . . . . . . . 122
7.6
Capturing emotions from the user
. . . . . . . . . . . . . . . . . . . . 123
vi


## Page 11


List of Tables
4.1
Emotion codes for IBM Tone Analyzer . . . . . . . . . . . . . . . . . .
40
5.1
Keywords used to identify each server status . . . . . . . . . . . . . . .
54
5.2
Facebook posts with keyword error and server response
. . . . . . . .
55
5.3
Facebook posts with keyword “down” and server response
. . . . . . .
56
5.4
Facebook posts with keyword “idle” and server response . . . . . . . .
57
5.5
Facebook posts with keywords related to uploading/slow performance,
alongside server response . . . . . . . . . . . . . . . . . . . . . . . . .
58
5.6
The performance of the matching algorithm . . . . . . . . . . . . . . .
63
5.7
Independent samples t-test - Tests of Normality . . . . . . . . . . . . .
65
5.8
Independent Samples Test
. . . . . . . . . . . . . . . . . . . . . . . .
65
5.9
Hypothesis Test Summary - Mann-Whitney U Test
. . . . . . . . . . .
66
6.1
Average rank correlation for applicant group versus personality traits . .
70
6.2
Timeline periods as percentages of total timeline
. . . . . . . . . . . .
71
6.3
Applicants’ time-line actions assigned to segments
. . . . . . . . . . .
72
6.4
Description of each class . . . . . . . . . . . . . . . . . . . . . . . . .
73
6.5
Coefﬁcients of multicollinearity variance inﬂuence factor . . . . . . . .
78
6.6
Dataset sample
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
79
6.7
Evaluation of the model and ability to predicate the status values . . . .
79
6.8
Model summary after removing the multicollinearity features and above
critical value of Mahalanobis distance . . . . . . . . . . . . . . . . . .
79
6.9
Top effective coefﬁcient LIWC features over the model . . . . . . . . .
80
6.10 System Stages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
6.11 Sample of Stages Text collected per user [242] . . . . . . . . . . . . . .
82
6.12 Sample of the sentiment analysis output . . . . . . . . . . . . . . . . .
83
6.13 Logistic Regression – variables in the equation table . . . . . . . . . . .
84
6.14 Binomial Logistic regression Classiﬁcation
. . . . . . . . . . . . . . .
85
6.15 Shapiro-Wilk’s normality check for Big Five traits and EI traits.
. . . .
86
6.16 Pearson correlation coefﬁcient, Big Five and EI traits . . . . . . . . . .
87
6.17 Spearman’s Rank-Order correlation output . . . . . . . . . . . . . . . .
87
6.18 Pearson correlation coefﬁcient, Big Five and Basic emotions . . . . . .
88
vii


## Page 12


6.19 Sample of the emotion extraction output . . . . . . . . . . . . . . . . .
91
6.20 Multicollinearity output - Coefﬁcients (Dependent Variable: stageid) . .
91
6.21 Full likelihood ratio test - Test of Parallel Lines . . . . . . . . . . . . .
92
6.22 Parameter estimates and odd ratios for the dichotomised cumulative cat-
egories of the dependent variable . . . . . . . . . . . . . . . . . . . . .
93
6.23 Goodness-of-Fit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
6.24 Tests of Model Effects
. . . . . . . . . . . . . . . . . . . . . . . . . .
94
6.25 Parameter estimates using the GENLIN procedure . . . . . . . . . . . .
95
6.26 Linear Regression Coefﬁcients output (dependent variable: Stageid) . .
96
6.27 Multinomial regression output - Model Fitting . . . . . . . . . . . . . .
96
6.28 Multinomial Regression - Likelihood Ratio Tests
. . . . . . . . . . . .
97
6.29 Multinomial Regression - Parameter Estimates . . . . . . . . . . . . . .
98
6.30 Snapshot of the data used in the analysis . . . . . . . . . . . . . . . . . 101
6.31 Linear regression coefﬁcients . . . . . . . . . . . . . . . . . . . . . . . 104
6.32 Pearson correlations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
6.33 Re-evaluation output of proposed model . . . . . . . . . . . . . . . . . 105
6.34 Evaluate the limit model
. . . . . . . . . . . . . . . . . . . . . . . . . 106
7.1
Variables in the Equation - Gender . . . . . . . . . . . . . . . . . . . . 111
7.2
Casewise Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
7.3
Binomial Log – variables in the equation . . . . . . . . . . . . . . . . . 112
7.4
Pearson’s Partial Correlation (controlling variable: Gender) . . . . . . . 113
7.5
Pearson’s Partial Correlation (controlling variable: Age)
. . . . . . . . 114
7.6
Pearson’s Partial Correlation (controlling variables: Gender and Age . . 115
7.7
Weka Summary model output . . . . . . . . . . . . . . . . . . . . . . . 117
7.8
Weka output (detailed accuracy by class) . . . . . . . . . . . . . . . . . 117
7.9
Sample of the dataset used in the veriﬁcation process . . . . . . . . . . 124
7.10 Weka summary - evaluating model using test dataset
. . . . . . . . . . 124
7.11 Model evaluation - Detailed Accuracy By Class . . . . . . . . . . . . . 125
viii


## Page 13


List of Code Listings
5.1
Retrieve Facebook Posts and Store to local MySQL for further analysis
52
5.2
Matching Algorithm - PHP SnapShot Code: Searching for username . .
62
7.1
Model function to calculate score of each personality trait . . . . . . . . 118
1


## Page 14


Chapter 1
Introduction
1.1
Overview
Marc Andreessen – co-author of Mosaic, the ﬁrst widely used web browser – boldly
stated in 2011 that “software is eating the world” [12], with software and technology
playing a huge role in our daily life, from communication, entertainment, education and
across the economy. Changes in the software engineering domain have occurred just as
rapidly, with the increased requirements on the responsiveness, robustness, and usability
of software. Furthermore, we are seeing the emergence of artiﬁcial intelligence and
machine learning as general-purpose technologies that could transform whole industries
and even re-invent the process of invention itself [44] – with potentially serious positive
and negative consequences [43]; so, does this raise the question: will AI eat software?
In the broader software realm, there is the grand question of “how will users react
to this application?”. In the user experience and software design research domains,
there are some intersecting strands of research and development in an attempt to ad-
dress this question. Researchers have previously used a range of different approaches
to measuring the satisfaction of users and how they behave when using their products.
However, this currently does not provide the necessary level of insight into behaviours
and emotions of users; more so with the increasingly complex software systems that we
encounter today.
Our world has an ever-increasing economic, educational and socio-cultural depend-
ency on data, technology and computation – and thus interconnected computer systems
– from smart cities and {big,open,personal} data [69, 332, 333, 67]; supporting ad-
vancements in science and engineering [75, 76, 78, 77, 323, 322]; knowledge repres-
entation and reasoning [87, 37, 73, 74]; insight into political systems, processes and
policymaking [335, 357, 319, 45, 88]; innovation and the economy [66, 79, 52, 349];
to developing digitally competent and capable citizens [14, 42, 222, 219, 85]. People
use and interact with complex platforms and systems in various ways, providing insight
2


## Page 15


into aspects of their personality, behaviour and emotional responses [234, 300]. These
multiple interactions can be measured, proﬁled and modelled to critically analyse the
communications and related processes and provide valuable insight into improving sys-
tem architectures and designs. Furthermore, it provides a predictive capability to better
understand digital behaviours – particularly through big social media datasets and cor-
pora [186, 271, 220, 45, 5, 6, 4] – and thus develop systems that are more resilient
and robust against undesirable behaviour and security breaches, such as “insider threat”
scenarios [168, 236, 331], cyberhate [46, 352], as well as more generally for crime
informatics [238, 47, 237, 239].
Figure 1.1: Intersection of the key research areas for this thesis (adapted from [143,
266, 112, 159, 51])
3


## Page 16


This research project is grounded in the area of human-computer interaction where
it intercepts with the ﬁelds of artiﬁcial emotional intelligence and behavioural sciences
under the umbrella of computer science (see Figure 1.1). It aims to develop new theor-
etical modelling of digital behaviour in complex computer systems – namely, pervasive,
data-driven social networks. Data were initially collecting and analysed from Facebook
and through complex information systems, we demonstrate the intrinsic relationship
between ofﬂine behaviour and online behaviour. Moreover, by investigating the re-
lationship between personality and emotions encountered during different events, we
can describe the associations between the traits which eventually led to extracting the
ﬁne-grained features used in the model. Thus, evidence that user’s emotions correlate
with different complex computer system status, giving us deeper, predictive insight into
behaviours and sentiments.
The primary objective of the human-computer interaction (HCI) research ﬁeld is to
ultimately make systems more useful and usable. A key part of this research and de-
velopment improvement process is to understand user’s behaviour by developing user-
proﬁling. With the rise of social networks and “big social data” providing easily access-
ible large-scale datasets; furthermore, enhancing the user’s interactions of the system,
attracted researchers from different ﬁelds to develop robust methodologies to achieve
this objective. Furthermore, HCI is increasingly an inter-, multi- and trans-disciplinary
ﬁeld, embracing aspects of artiﬁcial intelligence, cognitive science, psychology and user
experience. This research project is an attempt to provide a solid theoretical foundation
– with practical validation and veriﬁcation – of proﬁling digital behaviour through the
intersection of HCI with other key research areas (see Figure 1.1). This work is based
on a unique and rich longitudinal dataset of user’s interaction with a complex online
computer system, supported by the use of social networking platform (Facebook) data
and other modes of interaction (e.g. help desk ticketing system). Thus, with these var-
ied data extracted from the complex system for each user, we are able to apply various
hybrid data mining, data science, artiﬁcial intelligence and machine learning methodo-
logies.
The large-scale longitudinal dataset consisting of interactions of applicants to a real-
world online scholarship mobility platform. These interactions constitute part of the
“digital footprint” of the users, including the important artefacts and communications,
as well as the user interactions and activities during a predetermined system failure
event. New conceptual models will be developed using these datasets and associated
empirical data, making theoretical contributions to domain knowledge, as well as an
adaptive framework for a range of real-world practical applications to some problem
domains
4


## Page 17


1.2
Contribution to Knowledge
The primary contribution to knowledge from this thesis is the development of novel con-
ceptual models and an adaptive framework to improve predictions of user interactions
and behaviours. Thus, this can be widely applied to enhance system design and user
experience for modern complex information systems across a number of domains. This
will provide a deeper critical understanding of the relationship between user emotions,
personality and behaviours and computer system interactions.
Speciﬁcally, this thesis:
• Critically reviews the state-of-the-art domain research, contextualised by the rel-
evant human-computer interaction, artiﬁcial intelligence (including natural lan-
guage processing, sentiment analysis, and machine learning) and human-computer
interaction literature with regards to relationships between user behaviour, emo-
tion and personality and their digital interactions and activities.
• Analyses and investigates the key relationships between emotion and personality
and online/digital behaviour to develop new conceptual models.
• This research study, provides robust empirical validation and evidence for rela-
tionships between user’s online behaviour and responses and associated personal-
ity/emotion, particularly during disruptive system events.
• Develops a novel adaptive framework to provide predictive capability for user’s
behaviour in various computer systems, providing new insight to enhancing the
design, usability and user experience of complex computer systems across some
domains.
• The is study, validates the new theoretical models and adaptive framework against
some challenging problem sets in various domains; including user experience,
software engineering, and system design.
1.3
Publications
To further reinforce the novel contributions to knowledge from this research project,
both theoretical foundations and applications derived from this work have been pub-
lished in (or submitted to) the following peer-reviewed journals and international con-
ferences:
• J. Rafferty, M. Mostafa, T. Crick, G. Oatley, C. Ranson, and I. S. Moore. Using
machine learning to predict concussions in professional rugby union. Submitted
to Artiﬁcial Intelligence in Medicine, 2019 [278] – in this paper, various data
5


## Page 18


science/machine learning techniques that have been used in this thesis has been
applied to a novel application areas (sports injuries).
• J. Rafferty, C. Ranson, G. Oatley, M. Mostafa, P. Mathema, T. Crick, and I. S.
Moore. On average, a professional rugby union player is more likely than not to
sustain a concussion after 25 matches. British Journal of Sports Medicine, 2018
https://doi.org/10.1136/bjsports-2017-098417 [279] – in this paper, vari-
ous data science/machine learning techniques that have been used in this thesis
has been applied to a novel application areas (sports injuries).
• M. Mostafa, T. Crick, A. C. Calderon, and G. Oatley. Incorporating Emotion and
Personality-Based Analysis in User-Centered Modelling in Research and Devel-
opment in Intelligent Systems XXXIII, pp. 383–389, Springer, 2016
https://doi.org/10.1007/978-3-319-47175-4 29 [220] – this paper directly
relates to the studies and outputs from this thesis, in particular as presented in
Chapter 6.
• G. Oatley, T. Crick, and M. Mostafa. Digital Footprints: Envisaging and Analys-
ing Online Behaviour in Proceedings of 2015 Symposium on Social Aspects of
Cognition and Computing Symposium (SSAISB), 2015
https://cronfa.swan.ac.uk/Record/cronfa43383 [242] – this paper directly
relates to the building of the conceptual model, as presented in Chapter 7.
1.4
Ethics Approval
The main dataset has been approved to be used as part of this research project by
the registered data owner: the International Ofﬁce at Cardiff Metropolitan University.
The wider PhD study and in particular, the veriﬁcation experiment presented in Sec-
tion 7.3, was approved by Cardiff Metropolitan University’s Ethics Committee (CSM:
2015S0054).
1.5
Thesis Outline
Following on from this introduction in Chapter 1, the rest of the thesis is structured as
follows, contextualised by three literature review chapters:
Chapter 2 provides the theoretical background and critical review of the psycholin-
guistics and personality theory literature, focusing on the Big Five personality
traits as it plays a vital role in the study. Furthermore, it provides an in-depth
background to the Linguistic Inquiry and Word Count (LIWC) approach from a
6


## Page 19


computer science perspective, and critically reviews the current literature in the
ﬁeld of LIWC and personality traits. Moreover, we present the key interaction
with cognitive science, highlighted the state of art in emotions and temporal be-
haviour with respect to the wider human-computer interaction ﬁeld.
Chapter 3 builds from the previous chapter to provide a deeper discussion of cognit-
ive science’s role in human-computer interaction (HCI); this chapter critically
reviews the relevant research themes and provides a summary of HCI, user ex-
perience and usability literature and background and state of art. Demonstrate
and deﬁne the complex computer system and how human perceptual to different
computer status.
Chapter 4 reviews the history of natural language processing (NLP) and provides an
in-depth background to data usage and applications. In addition, we provide a
summary of relevant regressions, classiﬁers, and analyses used in this research
study.
Then we present the main methodology and modelling, the underlying system and data
architecture, as well as the key experiments:
Chapter 5 gives an overview to the complex computer system used as part of this study
from a technical and non-technical perspective. In addition, it provides a detailed
information about the data sources and how it been extracted and highlights the
challenges and the developed application/tools used as part of the extraction pro-
cess. Furthermore, this chapter explains the algorithm used to identify the status
of the complex computer system and matching the users between Facebook and
the system. This chapter also deﬁnes the extraction of the personality traits and
emotions and providing a rational of usage the Big Five Personality traits as part
of the experiments.
Chapter 6 demonstrate list of experiments conducted as part of the study, structured to
provide a rationale and key contributions, as well as presenting summary ﬁndings
and analysis.
Chapter 7 concludes the features extracted from all experiments presented in Chapter 6,
focusing on the usage of the random forest tree classiﬁer to build the model,
demonstrating the main ﬁndings. Furthermore, it provides detailed information
about the veriﬁcation methodology used.
Finally, we present the key discussions in Chapter 8 and the concluding remarks in
Chapter 9, providing a summary of the key contributions and ﬁndings, as well as an
overview of future work.
7


## Page 20


Chapter 2
Personality, Behaviour and Emotions
2.1
Introduction
This chapter presents a review and analysis of the key literature at the intersection of per-
sonality, behaviour and emotions. Personality traits make us who we are and that what
attracted researchers from different disciplines to investigate how to describe the per-
sonality and human behaviour. For decades psychologists proposed different theories of
personality that contributed to towards a better understanding of how to reform a foot-
print of a person [202]. In this chapter we present different personality theories [201],
demonstrating the development of those theories and how computers contributed to this
development, drawing on an extraordinarily broad array of research from cognitive sci-
ence and emotion science. Different research studies suggested that it is possible to infer
emotion through the communication between people and computers [146], This chapter
presents a broader view of the role of emotions in communication between people and
computers in everyday life as [225].
2.2
Psycholinguistics
Psycholinguistics is a branch of psychology that deals with and aims at studying the re-
lationship between linguistics and psychology. It primarily studies the cognitive process
that forms the foundation of language understanding and the interactions between social
cultures, linguistics and psychology in a broader framework [141]. Researchers in this
ﬁeld try to obtain objective data regarding models of prediction of linguistic behaviours
by various users of the language. The study attempt to ﬁnd out the mental processes
that are involved and used during language use [163] psycholinguistics is crucial as it
creates a platform through which language gets a chance to be processed, developed,
used, broken down and interpreted.
8


## Page 21


2.3
Personality Theories
As with our genetic make-up, our personalities are unique and personal to each of us.
Over several decades, the term “personality” has not only been used to describe features
of a person but also denoted the characteristic patterns of thinking coupled with their
general feeling and acting towards others. Thus, the consistency of the way people think
feels and act derives models. However, the theories of personality view people and try
to associate their choices with the hereditary closeness that they share. The theories of
personality are thus a tool for not only learning but also understanding and questioning
personality as we currently understand it. There are four general personality theories,
that is a psychoanalytic theory, trait theory, behavioural theory / social learning theory
and lastly the humanistic view [170]. The discussed personality theories in this section
determine the general deﬁnition of the personality as we know it; however, from a large
population sample, regardless of how one views personality, it has to be denoted by spe-
ciﬁc elements. These elements are: stability of character, consistency, and uniqueness
of personality [170].
The psychoanalytic theory of personality was ﬁrst described by Freud [31], with the
foundation of the theory built on human consciousness. According to Freud [263], hu-
man behaviour is a factor of human thoughts, ideas, and wishes to originate in the brain.
Freud develops and expands this theory on the importance and position that is held by
the unconscious mind, sexual aggression and early life experiences on a persons per-
sonality [136]. Furthermore, Freud implies that characters are such that some thoughts
can be pushed off and not acted upon from the conscious state to the unconscious. He
proposes that awareness exists in various forms; unconscious state, conscious state and
pre-conscious state. During the conscious level, the experience is limited to present mo-
ments while the pre-conscious level reveals information one is currently unaware of but
can immediately enter the conscious level. We are unaware of the ideas and feelings are
marked by of the last level. However, has a direct impact on the conscious mind [105].
This version of personality was controversial at ﬁrst, since it implied that the brain
“knew” things that the mind did not. Freud tried to explain the theory further by creating
a clear structure to explain it [105]. This structure bases it is assumptions on the human
hormone libido which fuels anger, aggression, and sexual anxiety. He proposes three
structures that interact with each other: id, ego and superego. It is the primitive part
of people that are susceptible to morality and social expectations; it is a self-centred
behaviour and seeks to please itself. Ego, on the other hand, goes hand in hand with
the reality principle, implies that it acts as a balance between human emotion and ex-
ternal social demands. The superego is part of the conscious self and is inﬂuenced by
social upbringing and guidance on morality. Based on these three structures, a person’s
personality is deﬁned.
The second personality theory is the trait theory which was developed and analysed
9


## Page 22


by Sheldon (1977) [174], Allport (1937) [8] and Cattell (1943) [58]. This theory is
simple and speciﬁc elaborating that human behaviour is a factor of well-known effects
from the organisms passed on traits and capabilities from the past [102]. This theory was
labelled as a dependent theory since it relied heavily on past events and characterised
personality because humans engage in actions which form patterns and judgements that
a form a level of cross-situations uniformity.
The third theory which was the behavioural/social learning theory was from Ban-
dura, Miller and Dollard and is commonly referred to as the social cognitive theory [18].
It is termed and viewed as a factor of cognition, environmental factors, past and present
and behaviour. Bandura puts forth the argument that social learning is directly related
to experiences that a person has by observing the behaviours of other people. This form
of learning is principled by the action-reaction constant. That is, the consequences or
rewards derived from behaviour. This means that when confronted by situations, people
have to choose what response to offer with regards to either the beneﬁts or the con-
sequence that will come from the after effects. The major limitation of this theory is
that it fails to consider the conscious self and biological disposal as factors of personal-
ity and eventually behaviour [18].
The last theory presented here is the humanistic theory. To understand the human
behaviour the theory asserts with regards to a person’s internal perceptions of his or
herself and others leading toward personal fulﬁlment. It was developed by Rogers
and Maslow [195, 167]. The central features of this theory are the personal conscious
choice, freedom and free will which all lead to self-actualisation. This theory took over
a new leaf as it addressed human behaviour in a manner suggestive of human growth
and meaning. Maslow argues that self-actualisation directly inﬂuences human motives
which in the end are all with physiological and transcended needs [195], eventually
presenting us with the now-famous Maslow’s hierarchy of needs [209]. Moreover, fur-
ther leads to the conclusion that self-actualised individuals make decisions with more
spontaneity, ease, creativity and enjoy the positive aspects of life more which is in line
with Carls perspective on the actualisation tendencies. Although, there are other person-
ality theories, the discussion above sets forth the principal theories regarding personality
as a front.
2.3.1
Cattell’s 16 Personality Factors
Characters or behaviours associated with speciﬁc people deﬁne the Human traits. Traits
are unique with regards to the degree in which we exhibit them at a personal level. Over
4000 different traits represent the Human behaviour and personality in its nature. In a
bid to rationalise all the different traits into a simpliﬁed and meaningful manner, Cat-
tell made a list of 16 traits that he referred to as dimensions of the human personality
[57]. Cattells view of personality was that it reﬂected human being behaviour in cer-
tain situations. Leads to the face that, inferred the person’s behaviour through a set of
10


## Page 23


behaviours obtained from information about their personality traits.
Cattell initially carried out statistical analysis to come up with data. He considered
the experimental data, life data, and questionnaire data as a basis for his argument on the
dimensions of human personality and eventually the 16 Personality Factors (16PF) [291].
The arbitrary scale whose scores relate to speciﬁc personality type is the core of the
16PF is a personality assessment. The ﬁrst scale traits are; vigilance, sensitivity, per-
fectionism, tension, reliance, open-mindedness, social assertiveness, warmth, rational,
emotional ﬁrmness, pensiveness, tension, dominance, rule awareness, privateness, alert-
ness and perfectionism [57]. Its use is primarily in determining personality types and
holds the position of the most used model of personality test with each trait relating to
testing subjects in different ways.
The 16PF is a factor of primary and secondary level traits. The primary traits are
the most important and most potent and form the basis of human personality and be-
haviour. Upon analysis of the ﬁrst traits, the “Big Five” or the global order of human
traits emerged. The Big Five has been re-deﬁned in recent times to include; control
or lack of resistance, tough-mindedness or open-mindedness to ideas, extraversion or
introversion to social life, high or low levels of anxiety and independence of self or
accommodation towards others [57]. Research suggests that a variety of other person-
ality traits are all housed in the Big Five. For example, high anxiety/low anxiety is an
umbrella to bold-shy, self-reliant group-oriented, private-forthright, lively-serious and
warm-reserved. The Big Five personality traits demonstrate into a more straightforward
yet broader perspective [272].
2.3.2
The Enneagram of Personality
The Enneagram of personality is a branch of human psychology based upon the nine
personality types of humans. The original enneagram bases it is originality on some
ancient traditions and can be traced as far as back to the mystical Judaism, Christianity,
Islam, Buddhism and ancient Greek philosophy [284]. Despite its broad rooted history,
the enneagrams representation of human nature still stands as all the traits it represents
are still relevant.
As a concept, enneagram was taught and introduced by Ichazo [158] and based on
the three groups or three triads. The organisation of these triads is such that nine person-
ality types are birthed from three personality types in each of the three groups. These
three namely; 1-the instinctive triad, 2-feeling triad, 3-the thinking triad. As their names
suggest, each one of these triads is representative of the associated traits such that a per-
son who is oriented towards feelings and self-image belongs to the feeling triad [285].
The feeling triad sets forth the helper; who is encouraging, demonstrative, possessive,
the motivator; who is marked by ambition, pragmatism and image consciousness and
the individualist; who is sensitive, self-absorbed, and depressive. The thinking triad,
on the other hand, is composed of the investigator; perceptive, cerebral, provocative,
11


## Page 24


the loyalist; the active, dutiful and suspicious type and ﬁnally the enthusiast who are
spontaneous, fun-loving and excessive. The last triad, instinctive, we ﬁnd the leader
who shows assertiveness, self-conﬁdence and very confrontational. This triad also rep-
resents the peacemaker who is pleasant, easy-going and very complacent. The last trait
representation of this triad is the reformer who shows excellent heights of rationality,
idealistic nature and orderly [284].
2.3.3
Analytical Psychology (Jungian)
Analytical psychology or analytic psychology is a school of thoughts and teaching that
trace its roots from psychiatrist Carl Jung. Carls teachings and concepts idealise and
emphasise on psychology on a personal front at achieving wholeness [314]. The most
important concepts according to his teachings were archetypes, complexes, the persona,
the shadow, the anima and animus, individuation, symbols, collective unconsciousness,
and ﬁnally the unconscious. Jung developed the concept of pattern archetypes which
elaborated human complexes from his research on the human-response relationship.
The relationship bases its assumptions on previous experiments that showed if a person
takes a long time to respond to speciﬁc words generally read to them in the form of a list,
the person was most likely experiencing a complex in the form of experience [314]). For
instance, someone with a mother complex might have faced a lot of early experiences
with their mother.
2.3.4
Myers-Briggs Personality Types
Perception as a concept includes the process of becoming aware of things. The Meyer
Briggs Personality Type Indicator is a questionnaire that structured as a way of demon-
strating various psychological alignments concerning their environmental perceptions [154].
It was developed and constructed by Katherine Cook Briggs and her daughter and con-
sidered as an extension of the Jungian theory of human experience is a retrospect of
sensation, intuition, feeling and thinking [154].
2.4
The “Big Five” Personality Traits
In the late 19th century, Galton [116] solved one of the fundamental problems at the
time in the research of psychology, which is how to represent classiﬁcation of human
character traits based on the “lexical hypothesis”. In 1884, Galton [116], estimated the
personality characters traits in respect of the English Dictionary and in 1936, Allport and
Odbert, were the ﬁrst psychologists to put Galton’s hypothesis into practice, by extract-
ing adjectives that they believed would describe the personality traits from the language
style [9]. Cattell continued the work conducted by Allport and Odbert, and eliminated
12


## Page 25


synonyms to reduce the total to 171 instead of 4,504 [17]. In 1940, Raymond [58]
constructed a self-report methodology for the classifying the personality traits found
from the adjectives, which he later called the Sixteen Personality Factor Questionnaire.
Cattell limited the personality dimensions into 20 out of 36. Later in 1961, Christal and
Tupes suggested that all personality traits can be shorted to only ﬁve broad factors which
surgency, agreeableness, dependability, emotional stability and culture [336]. The trait
dependability has been relabelled to conscientiousness according to previous study by
Norman in 1936 [234].
Figure 2.1: The “Big Five” personality traits, describing individual personality differ-
ences (adapted from [164, 206, 70, 71])
The “Big Five” personality traits have been the centre of attention of the psychology
13


## Page 26


used to describe the constituent features of personality in the ﬁeld of contemporary psy-
chology [125, 126, 70, 164], there has been consensus on its superiority by researchers
in the ﬁeld of organisational behaviour upon its performance for two decades. The title
is an emphasis, not on the underlying greatness but in the broadness of the select factors
in the model. The Big Five personality traits are typically assessed along the constituent
ﬁve dimensions – see Figure 2.1.
As per John and Srivastava (1999) [164], every one of the ﬁve dimensions constitutes
character at the broadest level of abstraction, and each size summarises a number of dis-
tinct, extra and precise personality traits. A study conducted by McCrae in 2002 [205],
suggested that personality traits curve does not change over time.
Studies have deduced several characteristics of the Big Five traits [206]. First, data
suggest that the characteristics can be termed as universal due to their occurrence where
there are personality tests involving traits in various languages [204]. Secondly, along
with the consideration of the role of genetics or biological factors and environment [269,
89], research ﬁndings show the Big Five traits are highly stable over time [127]. Lastly,
the Big Five personality trait model has been accredited as the basic discovery model of
personality psychology due to its history of usage, use across different cultures and the
empirical evidence from several methods and experimentation [206].
According to Costa and McCrae [70], the Big Five personality dimensions can be
divided into ﬁve factors namely; extraversion, agreeableness, conscientiousness, open-
ness, and neuroticism [71, 206, 164]. Extraversion as the emotional aspects of people
characterised by positive feelings and inclination to seek the company of others. People
in this dimension are cheerful and sociable while being assertive, optimistic ad natur-
ally talkative. Besides their preference for company results to groups and they relish
stimulation. People in this group experience positive effect such as energy, zeal, and
excitement [71, 164]. On the other hand, Agreeableness is the predisposition to be
trusting, compliant, caring, kind, and tender. Such persons have a favourable view of
human kind. They are concerned about others and have a yearning to help others; in
return they expect others to be helpful. Agreeable individuals are pro-social and have
harmonious integration with the public [71, 164].
The third dimension in the Big Five, Conscientiousness, describes the group of
people who are very objective in life and show determination in their undertaking.
They are responsible for an aspect of self-discipline that is manifested in their ability to
work without supervision and surpass the expectations. According to John (1999) [164],
people in this category have a prescribed impulse control that results to goal oriented
tasks making them think displays tendency to think before act, strictly follow the rules,
regulations, and norms and observe the order of planning, organ sign and giving priority
to some tasks over others.
The fourth group deﬁned by Openness which can be described as an individual’s
tendency to the imagination while at the time being original in thinking. They have a
14


## Page 27


liking for art and are sensitive to beauty with an attachment to feelings [71, 164]. Due
to their liberal thought, they are intellectually curious and are willing to entertain new
ideas and unique values. Lastly, the neurotic dimension encompasses the individuals
who have an array of emotions such as fear, nervousness, sadness, tension, anger, and
guilt. These people are subject to emotional adjustment or stability and emotional mal-
adjustment or neuroticism [71].
The aspect of personality that makes its analysis complex is because it is an assort-
ment of behavioural, temperamental, emotional and mental attributes that make a person
unique. For instance, communication is a trait that depends on the behaviour, tempera-
ment, emotion and psychological status of a person [253, 124]. As such, a person’s
choice of words, the way they say it, their semantic content and their physical prompts
creates a signiﬁcant variation between people. As such, while evaluating a trait, the
behaviour, temperament, emotion and mental status of a person should be considered.
By applying factor analysis to the lists of the trait adjectives under the ﬁve factors
listed above, researchers have obtained the ﬁve personality traits [234, 253, 124]. The
analysis based on the lexical hypothesis [9], which follows the principle that the most
consistent personal varieties encoded into the language, and the more signiﬁcant the
difference, the more possible represented as a one word. Although there are some limit-
ations and drawbacks of the Big Five model [103, 252], through experiments, the model
has succeeded in becoming the standard evaluation technique in psychology. These
experiments have shown that personality has a signiﬁcant impact on task-related indi-
vidual behaviour. For instance, the personal traits inﬂuence how leaders conduct their
roles, workplace performance [151], attitude towards work tools and machinery [307],
sales [114], the effectiveness of instructors, trainers and observers [292] and academic
ability [115, 179].
2.4.1
Linking Online Social Networks and Personality
The global use of online social networks has increased dramatically over the last ﬁf-
teen years, across all age demographics [339, 265]. In 2005, a study of social net-
working websites concluded that an approximate number of users using online social
networks totalled 115 million [122]. Five years later in 2010, 200 million users were
actively using one social network: Twitter. In the process of building social networking
proﬁles, users share a signiﬁcant amount of detailed, personal, temporal and location-
based information about their lives: likes, thoughts, interactions, check-ins and activit-
ies. Through self-description, status updates, pictures, videos, group membership and
hobbies, much of a users emotional state – and personality – manifests through their so-
cial media proﬁles. More recently, studies have shown that online social networks have
attracted billions of users worldwide, many of whom view online social interactions as
a core part of their everyday lives. In a study conducted by Cosenza in 2012 [68], Face-
book had more than two billion active user around the globe and it is the largest online
15


## Page 28


social network, serving 127 countries [104]. Further statistics shown by the China Inter-
net Network Information Centre, the total number of users online social network users
increased to nearly three billion in early 2013 [60].
Psychology researchers have attempted to better understand and explain personality
more formally. After extended work to expand and verify commonly-accepted personal-
ity models, researchers have revealed relationships between The “Big Five” personality
traits and many types of behaviour. These studies have revealed a strong correlation
between personality and psychological disorders [295], job production [19] and well-
being [166].
One of the areas that attracted researchers is to Automatic recognition of personal-
ity traits based on linguistic analysis, in an attempt conducted by Alam [3] to classify
the personality using text , provides a very good result of accuracy. Further work has
revealed that the user’s Facebook proﬁle is a reﬂection of their real personalities, not
self-idealisation [16]. A 2011 study of Twitter [274] presented an attempt of predicting
a user’s personality traits using three public parameters from Twitter proﬁles: following,
followers, and listed counts. Identifying these three values will lead to predicting the
“big ﬁve” traits of this user [317]. In another study supporting Quercia’s ﬁndings, Gol-
beck et al. (2011) [123], applied the Big Five Personality traits to 279 twitter’s users,
and extracted their 2000 recent tweets, and were capable to produce a model that can
correctly predict each of the “big ﬁve” traits. The capability to predict personality traits
has associations in different areas existing research has shown associations between per-
sonality traits and success in different levels of social communications (i.e, professional
and personal relationships) [59]. Another research study, claims it is possible to use
Facebook Likes to recognise and potentially predict personality traits, age, gender and
sexual orientation [180].
2.5
Language Analysis
Studies based on the relationships between personality traits and language styles have
presented a variety of results and outcomes. Certain studies have presented a strong
correlation between personality traits and people’s writing style [142, 162, 94], on the
other hand other studies, resulted that there are low signiﬁcant relationship between
personality and language usage [63, 53]. Pennebaker [258] asserts that despite the body
of a message being similar, different people will express themselves differently and in
unique styles. This is due to the observed defence in the way people speak or write, with
varying accents and choice of words in writing. However, researchers have managed to
trace word use in an attempt to form “Linguistics Fingerprinting” for a generation. For
instance, analysis of the text and use of words have been used in the 1800s during
the wars to the differentiation between soldiers [273] allowing capturing of the way
people committed (both verbally and written) to be obtained as a form of a ﬁngerprint.
16


## Page 29


Another text analysis strategy used it the word-based counting system introduced in
Stone (1996) [260], Dunphy (1981) [41].
2.5.1
Open Vocabulary Approaches
Open vocabulary is a method of language analysis, which is a popular approach within
computational linguistics and relevant disciplines [244]. This approach is a data-driven
methodology to the researcher where the dependent class representation typically used
in linguistic research. One of the main differences between close and open vocabulary,
that the open vocabulary methods use statistical and probabilistic methods to recognise
related language patterns or topics. An example of an open-vocabulary method is topic
modelling, which handles unsupervised clustering algorithms (i.e., latent Dirichlet al-
location or LDA [30]) to ﬁnd possibly meaningful groups of words in big sample of
natural language.
2.5.2
Closed Vocabulary Approaches
The most modern implementation of closed vocabulary analysis in cognitive science is
the Linguistic Inquiry and Word Count (LIWC) tool [254], which automatically counts
words relating to more than sixty predeﬁned classiﬁcations. Such as positive sentiment
(e.g., “happy”, “love”, “nice”), Achievement (e.g., “make”, “star”, “acquire”), articles
(e.g., “some”, “an”) and Tentative words (e.g., “possibly”, “reasonably”, “maybe”).
The closed-vocabulary approach depends on researchers to deﬁne categories and
psychological labelling [221].
Deﬁne category points to divide the dictionary into
groups of words and assign each word to the afﬁliated group. For instance, a group
of ﬁrst-person singular words (e.g, “i”,“mine”) or precautions (e.g, “in”,“at). Psycho-
logical labelling, by identify the semantic context if the word belongs to the positive or
negative group [320].
2.5.3
The Linguistic Inquiry and Word Count (LIWC) Tool
As mentioned in the previous section, the Linguistic Inquiry and Word Count (LIWC)
tool is the most common applications of closed-vocabulary methods, it is broadly used
for quantitative text analysis in the social sciences [256]. Although LIWC is able to de-
tect features in text by quantiﬁng them, which allows a text classiﬁcation and predictions
and open the door for further text analysis and modelling, it has been fundamentally
used to detect word features that are informative of the underlying psychological states
of an individual or group of people [111]. LIWC was ﬁrst produced to address content
analytic issues in experimental psychology [260]; nowadays, it has wider applications
across different ﬁelds such as social science, computational linguistics, shopping, and
health care.
17


## Page 30


The core of the LIWC program is its dictionary engine, with the most modern ver-
sion based on the default dictionaries, built up of a total of approximately 4,500 words
and word stems. The default dictionaries commonly fall into one of four widespread
language dimensions that are grammatical match to the word type, e.g. pronouns, num-
bers, ,articles social, emotions and cognitive.
The wider literature shows that there has been a focus on critique traits by new
researchers in psychology [120, 294, 297, 346] which have utilised different units of
analysis on the same [260]. We have also identiﬁed several ways of computing the
Big Five and other personality traits. Pennebaker’s approach [262] developed a method
that derives the features from textual information, relying on the previous research and
corresponds with the traditional procedures. For instance, by using a LIWC psycholin-
guistic dictionary, meaningful word categories can be obtained, and used to improve the
user experience in interacting with computer systems [138].
The method inferred both values needed to compute the traits. For the values, coef-
ﬁcients between values and LIWC categories was missing from the recent literature. As
such, the coefﬁcients from the value scores from surveys with LIWC category scores
and texts written by more than 800 individuals which was compared and analysed[138].
As for the needs, ground-truth scores used to acquired from a needs survey and text
written by more than 200 users. Moreover, the textual features were calculated us-
ing a custom dictionary that was constructed from diverse text users. Therefore, using
three ground-truth scores associated with the textual elements, the generated a statistical
model to come up with the needs [138].
For the past decades, research into character tendencies increased rapidly to many
researchers in different ﬁelds, with interest in technology that has the capability to un-
derstand people’s personality and feelings [91]. A recent concern has been the rela-
tionship between online social behaviour and real-life behaviour; citing examples such
as the Facebook and Twitter, researchers assert that the proﬁles in these accounts have
relation to the personality of a person [274].
Previous studies to establish a correlation between posted interactions on social net-
works and personality traits suggested mixed evidence of correlations between social
network usage and social anxiety. In a study of the behaviour characters conducted by
Zahra [286], personality is a critical aspect to be examined to better understand the be-
havioural inﬂuences of a sample population. Quercia (2011) [274] argues that there is
a strong correlation between personality and online social behaviour on platforms such
as Facebook. By using the users’ status texts, Zahra [286] suggested that the ﬁndings
of the study shows that personality traits and social anxiety did not linked with high
usage of the Facebook [286]. However, according to another study conducted by Mc-
Cord [203], there are positive correlations between the usage of Facebook and social
anxiety, reﬂecting the emerging nature of this research domain.
A 1986 study conducted by Gottschalk [129] shows that there is a relationship
18


## Page 31


between the emotional and cognitive dimensions as observed from the way individu-
als talk and write. Moreover, empirical evidence over the last four decades shows that
a person’s choice of words and their utterances are linked to their physical and mental
health [129]. This has been substantiated by ﬁndings from an experiment that showed
improvements in psychological and physical health when individuals wrote or talked
sincerely about their emotional experiences. These ﬁndings can be explained by the
text analysis that shows tendency by those who write to use words of positive emotion
while avoiding or suing moderate words of negative emotion. Furthermore, the writers
tend to beneﬁt from increasing usage of cognitive words which invoke relatively high
rates of positive sentiment [259].
According to a 2004 study by Kendall [173], in an attempt to create a model that
allows learning about the emotional, mental and physical relations between the oral
and written texts of individuals, researchers developed the LIWC engine. LIWC has
undergone developments since the ﬁrst version which was developed as part of an ex-
ploratory study of language and disclosure. A further innovation, the second version,
LIWC2001 [257] was an upgrade of the dictionary alongside usage of more modern
software. The latest versions LIWC2007 offers the merit of a more advanced software
and dictionary options. However, despite the advancements, the software retains its
initial design objective of analysing one or more language ﬁles faster and better while
remaining transparent and ﬂexible in its operations.
LIWC is largely applied in the ﬁeld of social sciences to analyse texts quantitatively.
Hence it counts the number of words [254]. The software was initially developed to ad-
dress content analytic issues in experimental psychology and identify word features that
can be used to assess the primary hidden psychological states of the writer or speaker.
Moreover, by determining the elements in a text, it can classify it and predict the various
associated behaviour outcomes which can after that BE used for psychological applica-
tions [256].
2.6
Cognitive Science
2.6.1
Emotional Intelligence
In his work “What is emotion?” [48], Cabanac argues that the world has so far not
agreed or come to a consensus regarding a canonical deﬁnition of an emotion. However,
he identiﬁes a list of motivational states of consciousness that is largely dependant on
pleasure. These states include: anger, fear, disgust, joy, sadness, and surprise. However,
emotion can be regarded through the lens of events which humans get to experience he-
donic content (i.e. pleasure or displeasure). For the majority of humans, emotions make
up our everyday life, as very few people are in the position of being devoid of any emo-
tions since they originate from the same part of the brain, the limbic system. Emotions
19


## Page 32


may change over time as people mature, develop and encounter new experiences as they
require different triggers, but they are constant. In evolutionary psychology, emotions
are deemed necessary for normal day to day living whether they are positive or negat-
ive [188]. Behaviour has been deﬁned by the IRIS Center1 as activities which people
engage in and can be visually assessed, quantiﬁed and occurs in a repetitive manner.
This deﬁnition, however, does not bring to the attention of the reader that behaviour is a
direct factor of emotion and ultimately manifests through the pleasure principle [139].
There are many types of emotions, from the basic emotions identiﬁed by Ekman
and Friesen (2013) [99], to a range of secondary emotions. One differentiating factor is
the origin of these emotions. An analysis shows that a relationship between developing
of the brain and the emotion [328]. The basic emotion is the emotions a person has
from birth and are less likely to change as one grows up since they already ingrained
in the brain at infancy [137]. However, some of the basic emits can be modiﬁed by
saying, for instance, changing the environment although the changes would not develop
much over the life time. As for the secondary emotions, these are as a result of the
child’s experiences from infancy throughout life basing on social and environmental
experiences [326, 98]. For instance, as one interacts with friends and peers, parents,
siblings, caregivers, peers, etc, they will invoke and evoke different forms of emotions
depending on the nature of the interaction. Thus, secondary emotions are a factor of
how a child views his/her surroundings and how the environment treats the child.
There is one common characteristic of emotions whether basic or secondary: the
limited nature of uncontrollably of emotions and that emotions will always result in its
disturbance of the initial setup before the occurrence. If emotions were fully control-
lable them, we would be emotionless (Lewis). As such, Basic emotions such as fear,
anger, joy, sadness, disgust, interest, and surprise are all shown in early infancy expres-
sion and used by all cultures a basic emotions facial expressions are always done quickly
without thought [160]. Thus, research supports the theorem that basic emotions are uni-
versal. Another theory of emotion is by Tomkins (1963) [326] and Ekman (1984) [98]
who are part of the cognitive revolution of the 1960s and 1970s and its states that emo-
tions “were discrete entities, separate from though interacting with other psychological
systems including cognition” The theory had three components with the third being a
consequent of the ﬁrst to indent the subjective experience of emotions. The neurotic be-
havioural element is the most essential component [326, 98]. Supporting their research
on Darwin (1872) [84], Tomkins and Ekman conducted tests on infants in the category
of facial expressions across different cultures. The ﬁndings showed that the facial ex-
pressions in infants did not change regardless of different cultures, a reﬂection of the
basic emotions neural features component. These were the basic emotions also known
1The IRIS Center at Vanderbilt University in the USA is a national centre dedicated to im-
proving education outcomes for all children, especially those with disabilities birth through age
twenty-one, through the use of effective evidence-based practices and interventions:
https://
iris.peabody.vanderbilt.edu
20


## Page 33


as the primary emotions [95].
Primary emotions and behavioural sciences have widely studied emotions as an es-
sential element of human nature [306, 155]. Increasingly, this has been the case across
the cognate ﬁeld of computer science given the frontline applications of computers in
the area of human interactions. Through the advanced concept of textual analysis. It has
been possible to interpret the emotional aspect of communication into through compu-
tational linguistic. This has allowed the researcher to ensure moving detection through
sue of the new concepts of textual analysis. However, there has been inadequately min-
imal efforts into detecting emotion from text. Shivhare (2012) assumes that its word
appearance essentially represents emotional reaction of an input sentence [306].
2.6.2
Self Assessment of Emotions
Figure 2.2: The Self-Assessment Manikin (SAM) [23]
Extracting emotions using self assessment is one of the most common approaches
in the cognitive science, the Self-Assessment Manikin (SAM) (see Figure 2.2 has been
commonly used in the approach of self assessment, it was ﬁrst introduced by Lang in
1980 [185] and reported as a fast and simple method for self assessing emotions which
can be used in different various contexts, the SAM as methodology have been used for
decades [36], however, with the revolving usage of modern technology with advanced
interfaces and methods of communication, it was essential to design a new methodology
to support nowadays mindset[194]. The Affective Slider (AS) ﬁrst appeared in 2016,
21


## Page 34


and where the design of the slider was used to capture the emotions instead of the SAM
methodology and produced more efﬁcient in the usage of the AS [25](see Figure 2.3).
Figure 2.3: The “Affective Slider” (AS) [25]
2.6.3
Temporal Behaviour
Temporal behaviour is characterised by a change in behaviour patterns over a short
time. This is especially true with regards to the digital age which sees trend creation
develop and die on the daily. This is elaborated by Roenneberg (2017) [288] in his
research on studying temporal behaviour on Twitter. Temporal behaviour is especially
important in the marketing industry and can be taken advantage of to bring in num-
bers. Over the years, psychology as a ﬁeld of study has focused more on scientiﬁc
modelling and data collection of the ﬁeld as compared to emotional intelligence im-
portance and role [215].However, over the past two decades, emotional intelligence has
been categorised into ability and trait. The Trait Emotional Intelligence Questionnaire
(TEIQue) [264] is an emotional intelligence assessment developed to demonstrate how
individuals understand their emotions and how it reﬂects their communications with
others. TEIQue was originally developed by Petrides (2001) [264] as part of his re-
search at the University college of London. It offers variety in the type of audiences it
can serve from grown-ups to children. It is widely used in the business industry as a
tool of assessing employee’s capability adapt and cope at the work place by assessing
how intelligently they control their emotions. TEIQue assessment is an emotional intel-
ligence questionnaire that assesses emotional management from a personal perspective
to a social aspect which eventually leads to relationship management with self and the
rest [215].
22


## Page 35


2.6.4
Applications of Cognitive Science
As discussed in Section 2.4, the visual, vernal or written way of communication by
an individual can pinpoint their personality traits. For instance, in the social media
concept, a status update by a person when communication to the online community
can use a wide range of forms of speech depending on factors such as age, gender or
occupation. Though these updates, although primarily communicating, such a person
can leave evidence of a particular personality trait(s).
In 1992, Costa conducted a research study on the possibilities of acquiring person-
ality models of the Big Five personality traits through observation rather than directly
asking the author or user [70]. The view is made on the linguistic input of a person by
analysing his/her texts and conversation. The study also acknowledges other classiﬁca-
tion models that use the personality recognition in texts and blog postings. The results
reported by Maitresse in 2006 were the ﬁrst in the ﬁeld to examine the identiﬁcation
of personality in dialogue, and to apply regression and ranking models that allow us
to model personality recognition using the continuous scales traditional in psychology,
also systematically examine the use of different feature sets, suggested by psycholin-
guistic research, and report statistically signiﬁcant results [197].
A 2007 research study conducted by Pennebaker [254] determined which language
style are signiﬁcant of speciﬁc personality dimensions based on Facebook status updates
from myPersonality2 as a dataset to built an engine that counts words in psychologically
classiﬁed traits. The result of the research showed a capability to extract a different fea-
tures, emotions traits, social tones, and personality difference, which was later assessed
and veriﬁed by Appling in 2013 [13].
Another application is in using machine learning approach to make improvements
or investigations about the proﬁciency of play in avenues such as computer gaming [90].
The research and development in this direction, however, has not been exhausted with
little impact being observed. For instance, while the experience of play is entirely a
psychological phenomenon, it is noted that game designs have not widely adopted useful
psychological theories, such as the nature of dispositions [228, 72].
Personality traits have been employed in the wider ﬁeld of artiﬁcial intelligence (AI)
where current studies have ventured into scrutinising methods to automatically infer
other types of logical variations and differences in texts and conversations, such as emo-
tion [247, 190], deception [230, 101, 131, 147], speaker charisma [289], mood [217],
dominance in meetings [282], point of view or subjectivity [350, 355, 315, 312], and
sentiment or opinion [38, 270, 248, 337]. However, while the me consideration in AI
maybe contextualised or short-lived, the component personality is given a long-term
perspective and is viewed as a more stable aspect of individuals [296].
Further research in this area shows that personality also inﬂuences other aspects of
2myPersonality was a popular Facebook application that allowed users to take real psychometric tests,
and allowed recording – with explicit consent – their psychological and Facebook proﬁles.
23


## Page 36


linguistic production [139, 183]. Strong relations have been observed between the Big
Five dimensions with personality interacting and having an effect on them. For example,
there is a clear-cut relation between the traits of the extraverts and the conscientious
and the extraversion and conscientiousness traits and the constructive outcomes, and
amongst neurotic individuals and those with disagreeableness [344]. Another case is
personality “vices” – such as lying – which contradict the dimension of agreeableness
across modes such as visual and acoustic. It is such inconsistencies that create the
avenue for human judgement’s ability to ﬁgure out the cases of deception [144].
For instance, the individuals in the extraversion are outgoing and energetic with
higher scores at deception while those in neuroticism are not good at lying. Moreover,
the individuals in the agreeableness and openness category are good at identifying po-
tential fraud [283]. Similarly, extraverts have demonstrated excellent public speaking
skills [101] with a study on those who dominate meetings showing the extrovert fea-
tures. Thus, the functions used to pinpoint introversion and extraversion automatically
can also be used to detect cases of deception automatically [230].
Outgoing and active people – extraverts – are more successful at deception, while
worried – neurotic – people are not as successful in this area [283], and people that
score highly on the agreeableness and openness to experience characteristics are also
skilled at identifying deception [101]. Newman (2003) and Bono (2004) claimed that
features that used to automatically detect introversion and extraversion are also import-
ant for automatically identifying deception [230, 32], personality models can be applied
to other uses to improve the accuracy of results [130]. For instance, opinion mining can
use personality models to gain more valuable information. Also, the recognition of user
personality in computer systems such as social platforms can be applied to other com-
puter applications [32]. Such areas include but not limited to; online dating platforms
where character can be matched from analysis of the user text messages resulting to a
more prosperous relationships, identifying the right leaders in meetings that require ana-
lytical skills through examining the personality dimensions of the candidates, ensuring
that tutoring systems are tailored to ﬁt the learner’s personality traits and in language
systems. Automatically recognising the author’s persona in quantity, could also im-
prove language conception, as the differences among people affected in the manner of
expressing the concepts [282, 243].
Another major area of application is in language and conversation where automat-
ically Identiﬁcation of the author’s persona in quantity, could also improve language
conception, as the differences among people affected in the manner of expressing the
concepts. As per current research, there are only two studies on programmed identiﬁc-
ation of user personality [150, 334, 235] in addition to our research. These studies have
shown that users evaluation of conversational agents depends on their personality [55],
which suggests a requirement for such systems to adapt to the user’s personality like
humans are able to do [208, 113].
24


## Page 37


2.7
Summary
This chapter presented a critical review of the core psycholinguistic literature and the
state of the art personality theories in the social science domain, summarising the strengths
and limitations of personality theories as traits perspectives. A signiﬁcant advantage of
the trait perspectives is their capability to classify apparent behaviours. Several research
studies reveal that observing the aggregate actions of people over time and in various
situations provides substantial justiﬁcation for the personality traits and categorised in
the traits hypotheses [92]. Furthermore, the use of objective criteria for classiﬁcation
and identifying behaviours. A rationale for this that many trait theories (e.g. Big Five
traits) were developed independently of others and eventually concluded the same clas-
siﬁed personality traits [201, 264, 128, 92]. On the other hand, other studies argue that
trait theories provides a false prediction of the behaviour in some situation where in-
volves other environmental factors, and that combination of trait and situation paramet-
ers impact of the behaviour [35]. For instance, an extroverted person is excited by social
communications and tries out social situations, but trait theory does not offer any evid-
ence for why this might happen or why an introvert would avoid such situations [49].
Furthermore, this chapter highlights LIWC as a key application to analyse trait the-
ory; LIWC is a critical algorithm used to extract the personality traits and emotions
using lexicon-based approach. The broader application of this lexicon-based approach
is attractive to researchers, especially with the rise of the social networks; a recent study
[254] revealed a strong correlation between Facebook status and personality traits, open-
ing the doors for more application of cognitive science within our daily-life bases and
touching the human-computer interactions ﬁeld. This chapter sets the foundation for the
next chapter by highlighting the intersection between the cognitive science and human-
computer interaction.
25


## Page 38


Chapter 3
Human-Computer Interaction
3.1
Introduction
Human-computer interaction (HCI) is a branch of intellectual science-based practical
approaches and is aimed at establishing usage of devices and the components contained
in their systems [54, 90]. HCI as a ﬁeld of study is cognitive speciﬁc as it includes
processing of information in the form of solving problems,making decisions, perceived
concepts, alertness and pattern corresponding. HCI is becoming of signiﬁcant import-
ance as a method of achieving more high-quality, efﬁcient and effective designs that
are easier for the consumer to interact with. With the constant shift in consumer needs,
HCI’s importance cannot be underestimated [310, 90]. Technologies are constantly
changing and under signiﬁcant upgrades which may or may not suit consumers’ needs,
now and in the future. However, our world is shifting towards the concept of what
people can do with technology as opposed to what technology can do for them [310].
HCI was initially designed to meet and improve ﬁve core goals: safety, utility, effect-
iveness, efﬁciency, and usability with the latter being the least promoted and advanced.
However, these goals have changed over time and established a sense of revolution that
encompasses usability as the crucial role of HCI. HCI as a topic is widely research-
based and includes some areas that are progressive and some developing progressively.
These include; use of multimedia, gesture identiﬁcation,ampliﬁed reality; computer-
based cooperative work, natural language processing, simulated reality and gesture re-
cognition [210, 212]. As with any other form of technology, HCI is organised in a
basic manner that can be simpliﬁed as an umbrella of sorts [152]. This is because HCI
directly deals with various disciplines such as education, psychology, ergonomics, ef-
ﬁciency, and collaboration. HCI can be subdivided into smaller domains; for example,
computer-supported collaborative learning (CSCL), computer-supported collaborative
working (CSCW) and lastly computer-supported collaborative research [152, 90]. The
domains are organised in such a way that subsequent domains are sub divisions of pre-
26


## Page 39


vious ones.
Usability as a factor of HCI has to be measured and analysed to verify its effective-
ness and also as a way of ﬁnding out system gaps. There are ten rules which are pro-
posed as basic foundations to guide the HCI usability veriﬁcation criteria [152]. These
are; simple, and natural dialogues should be easily identiﬁable, using of a user familiar
language should be maintained, light memory loads for users to recall, consistency with
regards to the system, transparency from developers to the users regarding the system.
Others are; ease in exit executions, shortcut availability, easy error relay methods and
solutions, error prevention while using the system and help and documented information
regarding the systems to make clariﬁcations when need be [152].
3.2
Applications
HCI has found applications in a variety of ﬁelds, especially education [310, 304, 50,
211, 21]. A primary aim of HCI research is to make the interaction with users as pleas-
urable and effective as possible, allowing researchers to look at technology from the
user’s point of view. Humans interact with computers using all the channels that they
get computer output from in the form of sensory input on their end. These include;
visual channels, auditory channels, haptic channels and precise movement. This in-
formation has to be stored as various forms long term, short term and sensory. The aim
is however not to store the information but rather to create a reaction which can ulti-
mately be measured as the interaction with the computer. These reactions are factors of
other external variables giving developers a very critical function of enhancing computer
usability regardless of other factors [330].
3.3
User Experience and Usability
User experience – commonly referred to as UX – is a complex concept that can be
divided into three camps regarding the relation to usability [287]. Namely, UX encom-
passing usability, UX complementing usability and UX as a factor contained within the
spectrum of usability. It is important to note that UX and usability are very different
concepts dealing with very changing topics and concepts. While usability deals more
with making the users experience easier whilst using computer systems, UX deals with
engaging other emotions of the user such as their interest and amusement. This way,
computers may be usable but not necessarily engaging, thus failing on the spectrum of
UX.
UX can be categorised into three broad dimensions: the user, the product and the
interaction. These dimensions lay forth the foundation of UX development since it
is essential ﬁrst to understand the users needs for developers to make products [313].
27


## Page 40


Product aspects are primarily linked to the human emotions which the product evokes.
These include, but are not limited to; memorability of the experience, the ubiquity of
the system and the general perception revolving around the system. All these are con-
sidered as outputs from the system whose input include; appropriate product properties;
proper consumer needs tackling, the usability of the system, cognitive associations with
the system and ﬁnally the context in which the user is using the system from. The inter-
action in which the user ﬁnds themselves engaged in with the product sets forth a new
dimension of research and gaps in UX development. Through data generated from the
user and product interactions, developers can assess market gaps that lie not addressed
and not searched [287].
It is important to note that user experience and usability are different concepts; this
can be shown with the example of UX and usability creation. UX cannot be designed
but can instead be planned for. On the other hand, system usability is practical to design
as it does not inherently rely wholly on the user of the system. UX is composed of
two Meta levels that are exhibited in all dimensions of UX; these two are the sense-
making aspect of UX and the aesthetic appeal of UX. UX also addresses functional,
physical, perceptual, cognitive, social and holistic dimensions of computing systems.
As compared to system usability, UX is very subjective and depends wholly on the
attitudes of the user during the moment at which they access the system. It is also not
static as it progresses with time as users engage with it. This is a distinct similarity
between usability and UX; however, context is king when it comes to UX.
In recent years, we have witnessed signiﬁcant efforts to raise data and knowledge
explaining UX and its relationship with usability [287], as well as within the wider ﬁeld
of software sustainability [341]. Of key concern is human emotion during the use of
technology as it sets up the foundation on which user experience is laid upon. Based
on past research ﬁndings, it is difﬁcult to establish deﬁnite, speciﬁc results by studying
conscious human experiences. This is due to the technicalities related to the broad ﬁeld.
Tests techniques are destroyed by incompatible deﬁnitions, various assumptions and the
ever-changing human state of mind. These constrain thus bring forth human emotion
as a gateway for inferences regarding UX and their importance [313]. The emotional
facet of UX can be broken down into four main groups; competence frustration mod-
els, individual coping differences in human technology interaction, mental contents of
emotional experience and non-conscious cognitive process associated with the appraisal
process.
Emotional design is a branch of UX development that deals with the creation of
products in the form of systems that elicit appropriate emotions. The main aim of the
emotional design is to manipulate or evoke positive emotions from the users [191]. De-
velopers thus have to consider the relationships established between users and systems
constantly. These relationships can either be negative or positive. Negative relationships
curtail the amount of trust that a user gives to systems and becomes rather careful during
28


## Page 41


use. Positive relationships, on the other hand, create bonds with the users in the form
of memories which peek at the interest of the users. The context of the type of relation-
ship established inﬂuences the users ﬁnal emotional indulgence with the system. For
example, horror-themed games elicit fear which is a negative emotion, but at the same
time, fear adds to user adaptability by boosting adrenaline from game use.
Emotional connections act as central connectors between the world and human capa-
city to learn. Human emotion can be categorised into three levels; visceral, behavioural
and reﬂective [287]. Visceral emotions are those elicited when we ﬁrst encounter the
system. This forms the basis for adaptability of the system by the user and aesthetics
coupled with the products ability to address consumer needs play a great role. It is
therefore essential to ﬁrst obtain data regarding market opinions on the product before
exploring production. The behavioural, emotional design is the usability of the product.
Usability in this context is with regards to how effective the system is, how satisfying
its use is and how efﬁcient it is. General concept formation clouds this stage of emo-
tional acceptance regarding the product or system and clear opinions have already been
established [191]. The ﬁnal form of emotional design is experience based and makes
second purchase/adaptation predictable. It is dependent on the cognitive features of the
user and uses objective analysis to affect future decisions.
Every human interaction made by humans is emotionally aligned in a speciﬁc direc-
tion [191]. It is thus essential for developers to factor in how users feel while using their
products. User emotions are a factor of external and internal factors. Human emotions
are of two main streams; dimensional perspective and discrete perspective. The last sets
forth human emotion as a sum of categories that can be further divided into other sub-
categories that come about as a result of human action-reaction interaction, that is, ﬁght
or ﬂight coping mechanism [191]. However, this stream of human emotion is limited to
a controlled set of external factors that may affect the user thus making human emotion
dimensional since it can take various dimensions due to its context. Choosing emotion
is crucial as it directly determines the ﬁnal consumer adaptation of products.
3.4
Usability of Complex Information Systems
3.4.1
System Events
The computer systems world is organised into clusters and structures that could at ﬁrst
appear as very simple due to the ﬁnal user interface in which they are represented [182].
However, most systems are very complex and require input from various factors for
them to be successful. The complexity of systems includes; work complexity, informa-
tion complexity, technological complexity and topic complexity [182].
All forms of complications have a variety of input which exists in more than one
type and works synergistic-ally for the system. The systems in-processing is speciﬁc to
29


## Page 42


the system, and so are the outputs. However, outputs appear more straightforward than
the processing involved. A good example is the buying action of consumers. While it
may seem like a simple action brought about by the need to satisfy a need, buying is
a factor of both internal and external consumer-related factors and is affected by other
market drivers. With regards to system engineering, the term complexity is very diverse
and can range in its spectrum of meaning. Complexity may arise from the presentation
of data, non-linearity of data, numerosity of data, data organisation, lack of central
control of data, the spontaneity of data and feedback associated with the data [26].
Complex information systems have to be developed while paying close attention to
consumer usability and user experience. Despite their complexity, ease of use and user
emotions have to be well thought of and executed. Thus, complex information systems
are a broad set of information technology that deals with processing, evaluating and
analysing data. Computer systems can be categorised into complex systems as they
involve the incorporation of various aspects of computing to achieve set objectives and
functions [26]. This is shown by simple computer applications such as word processors
that use text formation and visual conﬁrmation which may sometimes be aided by audio
endorsement to create desired sets of documented info. Computer systems usability
may, however, be phased with challenges in the form of system status. These statuses
include system idle, system error, system down and system slow [117]. These status
couples the computer during usage and is set by default on the system’s framework.
Web-Based Applications
Web applications have been around even before the popularity of the World Wide Web.
For instance, Larry Wall (1987) [342], developed a server-side scripting language named
Perl before the mainstream of the internet. In the early 90s, the ﬁrst web applications
were developed to perform simple functions [246]. Nowadays, current web applications
classiﬁed as complex applications as it is used across the globe to perform complex func-
tions (e.g. taxes, online banking, socialising and more) [121].The web application uses
the Hypertext Transfer Protocol (HTTP) protocols [108]. The web application consists
of two main components: client and server. The “client” is the application used to enter
the information, and the “server” is the application used to store the information [24].
Web applications generally use a mixture of server-side script (e.g. PHP, JSP) [145]
and client-side script (e.g. Javascript, HTML5) to produce an application [110]. The
client-side script handles the visualisation of the data while the server-side script deals
with the back-end functions [24]; for instance, handling the server connections, storing
the information in the database, etc.
Hypertext Transport Protocol (HTTP) is a stateless application-level protocol that
is used for distributed, collaborative and hypermedia information systems [108].HTTP
integrates servers as the key information transfer mechanism between the user and itself.
Users send requests to the server which creates a response back to the consumer in the
30


## Page 43


form of an HTTP protocol. The chain of command is straightforward but may include
other parties designed to send out information within the request-response chain. An
excellent example of such an intermediary is the existence of a proxy that is used to
send out information and acts as a gateway or forwarding agent [108].
HTTP includes the following elements: text marked up using HTML and CSS,
scripts, and hypermedia [108]. Hypertext is ﬁrst media in the form of text that can
be viewed easily by uses and can contain connected networks called hyperlinks to other
hypertext. Hypermedia is the representation of hypertext in modes that represent pre-
determined sets of logical extensions. Hyperlinks, as the name suggests, are network
structures formed over and around the web to create links to related information from
one source to the other. Scripts are instructions that can be made and put into action by
the user from their end. HTTP as a concept is primarily built on its simplicity which
enhances the ease of use coupled with faster response based platforms that interact with
the user quickly. Client requests are independent and co-occur due to the amount of
capacity that is built on the framework of the HTTP system use [108].
Statuses of Web Applications
web applications are commonly to experience a variety of system status that includes
but are not limited to, system errors, hardware malfunction (Server Down) Runtime/Ap-
plication errors [358] and Server Slow Stop Error (Termination) [132]. Server errors
are more severe in effect as they affect a chain of user computers which rely on them
for functionality. It is thus important to constantly upgrade, maintain and assess data
provided by servers after they have decoded system information [165].
System idle is commonly displayed by computers on the task manager and comes
with clear declarations of the username it bears on the system, the memory it occupied
within the system, and a general descriptor used to describe it [313]. During system idle,
the process runs in the background with the primary aim being continuous processing
of instructions in the computing unit. The idle system status allows one to know how
much of the system is not under usage from other processes. System idle is constant and
appears in the task bar every time. The values of system idle range on a wide spectrum
between individual computers due to internal and external conditions.
System error is a default setting that acts as a warning mechanism to alert users of in-
compatibility of systems running on the computer and the inherently built system [117].
System error is a temporary status for most computer systems and requires the click of
a button for it to disappear. Most errors as indicated above show incompatibility and
are a result of safety concerns within the system. Fatal system errors lead to system
stop or crash [182]. In modern web systems each type of error has a standard HTTP
error code, in 1999, Internet Engineering Task Force (IETF) 1 divided the error codes as
1The Internet Engineering Task Force develops and promotes voluntary Internet standards, in particu-
31


## Page 44


following indicating any 5xx server error is an indication of error cause from the server
side. [108]:
System down is another form of computer status. This is mainly a concept of com-
puter software and applications. During system down, the system undergoes a crushing
event in which it loses its intended functionality and exits from the system. System
down is characterised by information hangs and in the worst case scenario [132], fatal
system errors which break down the whole computing system. This status is mainly as
a result of inputting the wrong set of information into the system primarily in the form
of key instructions. The instructions may overlap and have a ripple effect on the system
thus causing failure [117].
System slow as the name suggests is a system status primarily based on processing
speed. It is associated with the continuous ﬂow of information that may serve as inad-
equate in executing speciﬁc functions of the system. System slow is performance-based
and evaluated. System errors are either handled automatically by built in systems within
computers or manually by the users. If manually done, the system provides guidelines
which are in the form of displayed text for the user to follow. The instructions can range
from simple to complex actions with regards to the type of error [117]. It occurs due to a
variety of dynamics such as: internal computer factors such as space contained, number
of processes being run on the computer, type of computer and capacity. External factors
can include; data being input into the system which may be faulty, software introduced
into the system which could induce the lag, system hardware elements.
3.4.2
Response Times and Human Perceptions
For decades researchers investigated the relationship between the response time of a
system that satisﬁes the user [83]. According to Miller [216] and Myers [224], the server
response time can be clustered into three main points Discontinuity of waiting time at
15 seconds and Time recovery from errors and failures and linked to the performance of
the user after recovering from those two errors [231, 232] 0.1 seconds, 1.0 seconds and
10 seconds. The 0.1 second, indicate that the system is working idle and displayed the
requested output to the user. while in case of, 2 to 10 seconds, the user stars to lose that
the system is slow and that there is not operating as expected, furthermore, more than
10, 15 seconds, clearly indicates to the user that the tasks has occurs an error and the
system is not expected to return any feedback to the users.
Server Response Analytics
Technology as a ﬁeld has brought with it tools of trade that make everyday living ex-
periences much faster and simpler [268]. This is especially true in the analytics world.
lar the standards that comprise the Internet protocol suite
32


## Page 45


The diversity in types of internet based media has generated tones of data that needs to
be analysed as it represents the consumer directly. One of Googles most useful tools
in analysis is the Google Analytics which is an analytics tool that includes tracking
websites and accessing reports to view data that is collected from the websites [268].
The tool can thus be used to estimate the status of data servers as the reports suggest
direct relationships with website status and ultimately server status, part of the reports
provided by Google analytic is Average server response time, the time for the server to
respond to a user action or event.
3.5
Summary
This chapter has presented and critically reviewed the key domain literature of the wider
ﬁeld of human-computer interaction (HCI), recognising the importance and impact of
the HCI domain, providing the theoretical and practical foundation for design and de-
velopments that make it easier for users to interact with digital devices [194]. The
user usability is a critical factor of the HCI domain to measure the effectiveness and
systems and interfaces; however, the user experience interested more of the cognitive
science, emotions and user’s behaviours [310]. The emerging of the cognitive science
with user experience leads to the development of a new branch called emotional design
that deals with the user’s emotions and behaviours opening a new topic to attract re-
searchers from a different discipline (e.g. system design, marketing, business develop-
ment) [225]. The chapter sum up the system status and human-interactions from two
perspectives technical and human perception. With broadly identify four system status
from a technical perspective that includes System errors, hardware malfunction (System
Down) runtime/application errors [358] and System Slow and running idle mode System
idle. The technical classiﬁcation aligns with the three response time limit theory in-
troduced by Nielsen [231], a concept based on the human perception of server waiting
time. Nielsen argues that even a few seconds’ delays are enough to create an uNLPeas-
ant user experience, triggering various emotions that affect their interactions [232]. In
the following chapter, we will focus on the use of emerging – and increasingly impact-
ful – domain of artiﬁcial intelligence and machine learning in the context of linguistic
analysis and HCI.
33


## Page 46


Chapter 4
Artiﬁcial Intelligence
4.1
Introduction
The “digital” era has become almost ubiquitous – especially in the developed world –
with technology ﬁnding its way into the home, businesses, government, military, en-
vironment, education and healthcare [293, 192]. There is an ever-increasing market
demand for intelligent machines and intelligent approaches to a variety of domain prob-
lems. This is mainly because of demand and competitive nature – higher capacity and
ease of access, processing and analysing of data whether input or output [192]. This
need has thus lead to the awareness, growth, development and application of artiﬁ-
cial intelligence (AI). AI can be deﬁned as the science (and art) that aims to create
human-like intelligence capabilities in machines. While existing traditional computa-
tional paradigms are fundamentally limited by physical constraints, they are not limited
by the biological constraints as for human intelligence. The application areas of AI and
users are diverse (and widening), and certain AI applications have already surpassed
their expectations falling into a class of technology referred to as part of the singularity
event phenomenon; this category of AI has developed at a near-exponential rate [308].
With AI ﬁnding use in applications such as autonomous vehicles, statistical analysis (es-
pecially through the application of natural language processing approaches) and medical
diagnostics, its superiority over humans has already been established [200].
AI as a broader ﬁeld of study is founded on the basis that intelligent thoughts are a
way through which computation is established; that is, one that can be formalised and
ultimately mechanised [308]. This means that knowledge has to be ﬁrstly represented
and then manipulated. Knowledge representation is solely based on human imagination
and perception of speciﬁc items. Knowledge manipulation, on the other hand, is solution
based offering solutions to problems designed by the human imagination process [308].
The development and application of AI comes with both positives and negatives; the
advantages include: development of autonomous vehicles, lack of cognitive bias, high
34


## Page 47


ﬂexibility and adaptability, and variety regarding applications [308]. Furthermore, AI
systems are very ﬂexible since they can be easily re-purposed to suit speciﬁc needs as
compared to human experience which may be aligned in speciﬁc ﬁelds of interest and
savvy [233]. Its ﬂexibility also comes from the variety which it exists; this means that
the scope of application is very wide and easy to integrate [227]. Autonomous vehicles
are of a wide range including cars, industrial systems, analytic systems, cognitive sci-
ence [338] and medical systems to state a few. The introduction of the automated system
not only introduces more capacity in what can be done at a go but also creates a higher
chance of accuracy [65]. The disadvantages are primarily represented as risks associ-
ated with AI as a ﬁeld, as well as its potential applications – AI systems lack cognitive
bias in that they operate based on statistical data pre-fed into the systems and thus limit
chances of error as compared to systems that are human operated. AI has not been able
to function as full-brain activities such as self-consciousness, self-control, self-control
and self-motivation. Furthermore, other limitations of the AI, is lack of original creativ-
ity as any AI engine base it is choices and decision based on pre-deﬁned data [119].
The wide applicability and potential of AI use come with great risks that are directly
translated into challenges that are already taking shape. Risks as a challenge from AI
adaptation can be looked at as either being a positive or negative risk [308, 348]. Positive
risk is risks initiated by developers as a vision of the potential opportunity or failure of
the system. Negative risk, on the other hand, is the type of risk associated with loss of the
chance [308] – AI as a ﬁeld faces human misuse as a major risk in its implementation. AI
developers have to be extremely careful when carrying out a risk assessment to reduce
human misuse of their developments, with the emerging ﬁeld of “ethical AI” taking
shape. Humans tend to be selﬁsh and could manipulate AI to carry out agendas of
self-interest which fall back on the developers [175].
4.2
Computational Intelligence
Computational intelligence (CI) is the ability of a computer to learn a speciﬁc task from
data or experimental observation [97, 100, 96]; while there is no commonly accepted
deﬁnition of computational intelligence, it is recognised as a sub-branch of AI and com-
monly considered a synonym of soft computing. According to the IEEE Computational
Intelligence Society, CI is “a domain focusing on the natural intelligence and behavior”.
The main objective for researchers in this ﬁeld to link the Nature with artiﬁcial meth-
odologies to replicate the Nature activities inhuman to a computer intelligent activities
in an attempt to improve the efﬁciency and beneﬁt from the computer advantages. The
three main areas of CI are neural networks, fuzzy systems and evolutionary computa-
tion [97, 100, 96]. This section focuses on the core parts of CI that are used in this study
as following neural networks, with in-depth discussion to wide range of neural network
applied (see Section 4.2.1), natural language processing (NLP) (see Section 4.2.2 and
35


## Page 48


an application using NLP with IBM Watson (see Section 4.2.3).
4.2.1
Neural Networks
Neural networks are generated and developed as a way of increasing the effectiveness
of machine pattern classiﬁcation. As with biological neural networks, machine neural
networks are speciﬁc and bound to limitation s of their speciﬁcity and can be simple or
complex and highly integrated. This means that they only give an output of what they
are programmed to provide as output. Neural networks have anticipatory capacities
and are considered as new age mathematical, computational methods which are used
to solve unanticipated dynamic problems in developed behavioural systems during a
speciﬁc time or period [2]. These connections thus have the ability to unravel based on
pre-learned patterns by use of vast survey models that can anticipate various variables.
Neural networks can process information at increasingly faster speeds thus rationalising
the time that would have been used if other methods were used.
Neural networks are grouped into two broad paradigms: unsupervised and super-
vised. Unsupervised neural networks are best suited for the purposes of clustering pat-
terns and can be approached in three ways: self-organising feature maps, competitive
learning, and adaptive resonance theory (ART) networks [309]. Supervised paradigms
are established to be universal approximates of continuous/discontinuous functions and
are thus suitable for applications where approximations are made regarding the input
and the output data. In this case, the network is ﬁrst trained using speciﬁc input and out-
put that is approximated. Based on this, inputs are then fed into the network to counter
check that the output map reﬂects the original map from the comparative data. In soft-
ware engineering, neural networks have found practical use especially as test oracles,
effort estimators, and cost estimators.
Multilayer Perceptron
A multilayer perceptron (MLP) of neural networks is a variation of the novel perception
model proposed by Rosenblatt in 1957 [290], in his research work “The perceptron:
A theory of statistical separability in cognitive systems”, and is a class of feedforward
artiﬁcial neural network. Rosenblatt explains that future electric and electro-mechanical
systems would be able to learn and thus recognise similarities or identities between
patterns of optical, electrical or tonal information in a manner which may be closely
analogue to the human brain [199]. The systems would be dependent on a probabilistic
model of operation as compared to the use of a deterministic principle-based approach
for its operation. Further, the system would be able to work well with large populations
of diversiﬁed elements. Once the system had incorporated all the above, it would be
referred to as a perception [199].
36


## Page 49


The modern model for multilayer perceptron is not dissimilar from this model and
includes the use of backpropagation training algorithm [280]. The network is designed
to bear one or more hidden layers between its input and output layers. The neurons are
also arranged in layers, with connections arising from the lower end all the way to the
upper layers. However, neurons located in the same layer are not interconnected [280].
With regards to numbers, the network design is such that the number in the input layer is
equal to the number of the measurement for the pattern problem and the neurons number
in the output layer.
Random Forest Trees
Random Forests is data classiﬁcation approach that creates random trees and primar-
ily used in ﬁelds that classify data by creating random trees [40]. The main advantage
of random forests as a method of classiﬁcation is the ease of interpretation which it
offers to the end users. The data obtained is easy to explain and interpret. Random
forests can be as a factor of various variables as the trees formed different support vari-
ables. These trees can term as simple algorithms that show relationships in a tree-based
approach [40]. This approach solves problems from a bagging approach in which dif-
ferent variables clustered in different ways and the ﬁnal result obtained by getting the
average across the different trees. When creating random forests, it is crucial to con-
sider homogeneity of the data as this enables clusters to established on the right principle
background [40]. Random forests, in essence, work the same way as deeply connected
neural networks by creating simple multi-layers of information in the form of input or
output.
Random forests application is broad due to its ease of operation and interpreta-
tion [40]. They are however mainly applied in the analysis sector as they form the
broad range of algorithms, meaning that they can be used in regression and individually
as a tool in machine learning. Their efﬁciency in this speciﬁc ﬁeld based on pre-training
and input data previously provided. In classiﬁcation, random forests used for internet
trafﬁc interception, video and other media classiﬁcation, image classiﬁcation, and voice
classiﬁcation. All these uses can be termed as media classiﬁcation as they are different
forms of media.
Random trees are classiﬁcation tools that can also be used to solve regression prob-
lems as with random forests mentioned above [40]. Random tree classiﬁcation works
by the use of input information referred to as the vector which classiﬁed into a tress
classiﬁed in a forest. The outputs of the resulting class become the ﬁnal classes. Trees
within forests undergo the same type of training but have speciﬁc training sets for in-
dividual tree allocation. The vectors occur in random subsets that will be present or
absent in a random manner or subspace. Errors are unavoidable when using random
trees. However, by establishing reference error limits during the training, it reduces the
errors [40]. Random trees have advantages over other types of data in that they are easy
37


## Page 50


to read, can manage both statistical and categorical data, and perform well on large data-
sets, extremely fast, easy to understand. However, they also require algorithms which
demand allocation of various optical choices making them a centralised option for clas-
siﬁcation [40]. The other disadvantage is that they are inherently prone to over-ﬁtting
of items due to the amount of speciﬁcity required while making them. According to
Breiman and Cutler (2004) [40] random trees grow based on the following; ﬁrstly, if
the amount of instances in the training set is N, sample N cases at random - but with re-
placement, from the primary data. This training set will be consisted of the samples and
used as the training set for developing the tree. Secondly, if there are M input variables,
a number
m << M
(4.1)
is speciﬁed such that at each node, m variables are selected at random out of the M, and
the best split on this m is used to split the node. During the forest growing the value of
m is held constant. Lastly, each tree grows to the most signiﬁcant extent possible. There
is no pruning of the trees.
J48 Decision Tree Classiﬁer
The ID3 (Induction of Decision Tree) method is used generate a decision trees from the
dataset and were introduced by Quinlan (1979) [275]. In early 90s, Quinlan (1993) [277]
produced the C4.5 method is an extension of the ID3 methods, and has been used for
classiﬁcations purposes [153]. Furthermore, Quinlan (1996) [276] developed the J48
classiﬁer is an improvement classiﬁer based on the C4.5 method. The decision tree
generated by the J48 classiﬁer is referred to as a statistical classiﬁer as it creates trees
based on datasets [251]. J48 is part of a larger group of classiﬁers mentioned above;
supervised classiﬁers. It works by deciding the target value that is the dependent variable
of a sample based on a variety of characteristics. In between the branches of‘ different
classes exists nodes that dictate the outcomes that the characteristics can be seen in the
sample population. The predicted variable is referred to as the dependent variable [251].
4.2.2
Natural Language Processing
Natural language processing represents a programmed method of carrying out analysis
on writing founded on models and technological expertise [189]. The semantic is very
theory motivated, allowing very large variety of automated methods for carrying out
analysis and expressing normally. Output strings occur naturally relate to various lan-
guages, modes and genres which the text can take [189]. Natural language processing
originated from various disciplines; linguistics, computer science, cognitive psycho-
logy, electrical and electronics engineering, robotics, mathematics and artiﬁcial intelli-
gence [61]. Linguistics forms the formal structures of language while technology from
38


## Page 51


computer science developed in-house illustrations of information and proﬁcient hand-
ling of the models and ﬁnally, intellectual psychology. offers a way into the human
cognitive process [189]. The need for a linguistic way of analysing texts has been
essential over time due to constant technological innovations that are moving at an
exponential rate. Technology thus has to be used to facilitate change [333]. Natural
language processing is a form of technology consequentially referred to as human-like
language processing, this alludes to the fact that it is a discipline within the wider AI
domain [189].
The main aim of natural language processing is to build database or generate sum-
maries in a manner that was human-like. Artiﬁcial intelligence was denoted as natural
language understanding. It was mainly composed of: paraphrased input text, trans-
lated texts, answered questions regarding the context and drawn up inferences. On the
contrary, natural language processing has its main goal as achieving natural language
understanding [189]. The systems work by maintaining dialogue with the user as part of
database retrieval [7]. This means that other than information retrieval, natural language
processing is also used for machine translation, expert systems, speech recognition, ar-
tiﬁcial intelligence and question and answering as part of the analysis [61].
One of the common applications of NLP is with chatbots [305], which works as
an intelligent agent to respond to customer’s inquiry grounding on NLP to understand
the context of the conversation, which is able of managing any situation of dialogue
with people (for example, api.ai, Microsoft Language Understanding Intelligent Service
(LUIS)) [213].
4.2.3
IBM Watson Tone Analyzer
The IBM Watson “brand” is as a well-known term for a broad range of various in-
telligent applications including emotions recognition, expression recognition, NLP and
sentiment analysis [157]. The IBM Watson’s Tone Analyzer basic fundamental working
principle is rooted in human behaviour and thus factors in how humans interact with the
world. This can be simpliﬁed through the Big Five personality traits and emotion; fear,
disgust, anger, joy, and sadness. These ﬁve are both as a result of needs from people
and values imparted to them by the society. The tone analyser factors in these two while
generating output from language input made into its system as it generates answers of
questions depicted in the form of natural language, IBM Watson follows the LIWC
approach as discussed in Section 2.5.3, furthermore, in the emotion extraction, IBM
Watson based their research on emotion lexicon [343, 176]. Concerning the Big Five,
the system describes them in three major ways; facets, the range of characteristics and
primary and secondary dimensions [187]. Characteristics have descriptors that lead to
single term eluding personal traits. This kind of behavioural forecasting is essential, es-
pecially in emotional mining and marketing. According to a 2014 technical report from
IBM [157], for the human analysis, IBM used a well-known annotation crowdsourcing
39


## Page 52


Emotion
Description
Joy
Joy or happiness has suggestions of pleasure
and satisfaction. It is a feeling of safety and
comfort [133].
Fear
A reaction to threatening dangers. It is a sur-
vival approach that is a response to any negative
motive [245].
Sadness
Shows a perception of losing. Sometimes sad-
ness is noticeable when a person is seen to be
calm less active and isolated [169].
Disgust
An emotional response of disgust to something
considered offensive or uNLPeasant. It is a sen-
sation that refers to something revolting [62].
Anger
Triggered due to abuse, conﬂict, embarrass-
ment, carelessness or dishonesty [327].
Table 4.1: Emotion codes for IBM Tone Analyzer
platform called CrowdFlower, which ﬁlters the participant to choose the top-rated an-
notators for the task, ﬁve participant had to conﬁrm the classiﬁcation of the sentence to
ensure the highest quality of the annotation process and eventually comparing the F1
score for each analytic tone the overall difference were acceptable which indicate that
the tool is working in a good performance. The Tone Analyzer looked at ﬁve different
emotions (see Table 4.1) [157].
Earlier released of the engine used the LIWC with its machine-learning approach.
However, the open-vocabulary engine just performed better than the LIWC-based ap-
proach.
4.3
Machine Learning
Machine learning is one of the most popular and rapidly growing ﬁelds in the wider
AI/computer science domain. The increase in the digital technology and the social
networks played a major role in increasing the integration in our daily life and widen
our digital footprints and rate of data generation which require a quicker processing to
relay speciﬁc information [10]. This leeway from data has not only challenged machine
learning but also caused a push and diversity in the way we look and engage with at
machine learning as a concept [311]. Machine learning takes various forms of our
everyday technology use and is mainly used to re-arrange and re-organise data. For the
last decade, statistical data has been ﬂooded by estimation models of actual situations.
40


## Page 53


This is mainly due to the bulky nature of data. This means that the data classiﬁed was
not categorical, lacked data points and had spread out data points. Machine learning
is the science that deals with understanding the ways through which machines improve
how knowledge is acquired [309]. Machine learning allows systems to learn directly
from examples, data, and expertise. To increase expert performance, knowledge has to
be smart and very speciﬁc to enhance the process of knowledge engineering.
Machine learning can be categorised into two types: inductive and deductive ma-
chine learning [309]. As the name suggests, deductive learning works by deducing
information. It uses past knowledge and facts to infer outcomes or new knowledge.
The system works by clustering information from large data into simple easy to un-
derstand knowledge. On the other hand, inductive education forms establish computer
programs/knowledge by mining rules and designs from large data clusters [309]. Ma-
chine learning largely overlaps with statistics and ﬁnds its basis in statistics algorithms.
There are a variety of uses of machine learning including. These are search engines,
natural language processing, medical diagnosis, bioinformatics, cheminformatics, and
stock market analysis. Additionally, speech and handwriting recognition, genetic se-
quencing; game playing classifying DNA sequences, object recognition in computer
vision, robot locomotion, and banking; credit card fraud recognition [309].
The future of machine learning is of great importance to its users. This is mainly
because of the role which it plays in knowledge generation. It is therefore of key import-
ance for developers and societies, in general, to think critically and carefully regarding
the role of machine learning in the society [311]. Research has to change its focus
and aim at taming the various beneﬁts that can be brought forth by machine learning.
These beneﬁts also have to be shared across the society for them to be of great impact.
Some areas of machine learning require public acceptance for them to be impactful
in the community at large. Researchers can engage themselves in issues surrounding
algorithm interpretability, robustness, privacy, and fairness, the inference of causality,
human-machine interactions and security with regards to the future.
4.4
Classiﬁers and Regressions
Data mining is the process through which patterns are derived though analysis of in-
formation presented as data which later becomes a source of knowledge [135]. Data
mining uses co-relations and establishes various relationships among a given set of
stored datasets. Through data mining, businesses are able to predict the future trends
in consumerism and business approaches. Classiﬁers and classiﬁcation analysis as the
name implies classiﬁes data into various clusters and is used as a data mining technique.
It involves a dual-phased process, that is, model construction which precedes model us-
age. In model construction, the classes are pre-determined and classiﬁed under sets of
rules, decision trees and mathematical formulas [135]. Model usage on the other hand
41


## Page 54


classiﬁes unknown objects. It is very useful in estimating the accuracy of the model
since it uses a pre-determined label of experimental specimens which are related to the
categorised data from tested models . There are a variety of algorithms used for classiﬁc-
ation, namely; regression trees, decision tree induction, rule-based classiﬁers, Bayesian
classiﬁers, nearest neighbour classiﬁers, support vector machine, ensemble classiﬁer,
artiﬁcial neural network, rule based classiﬁers, decision tree induction, nearest neigh-
bour classiﬁers, Bayesian classiﬁers, artiﬁcial neural network, support vector machine,
ensemble classiﬁer, regression trees [135].
Regression analysis is a form of predictive modelling that is frequently used to de-
termine the relationship between dependent targets and independent variables otherwise
called predictors [161]. This form of analysis is thus primarily used to estimate or pre-
dict relationships between various variables. The model established through this form of
analysis indicates the importance of established relationships and the effect which more
than one variable may induce on the dependent variable. Factors are pre-determined
using the foundation that one factor is deﬁned as the dependent/explained while the
other factor is referred to as the independent/predicting variable. While working with
regression, the variables show elasticity in nature with regards to their economies of
scale or existence; regression thus helps ﬁnd out the average correlation amongst a
group of associated examinations that are expressed through the use of a regression
equation [161]. There are various forms of regression with the speciﬁc types being situ-
ational and variable speciﬁc. Namely, they include: polynomial regression, step-wise
regression, logistic regression, lasso regression, elastic net regression, linear regression
and ridge regression.
4.4.1
Linear Regression
Linear regression is an approach to statistical analysis that assumes that the relationship
established between a variable and an independent factor ﬁt in a linear scale. The vari-
ables can be one or more. There are various forms of linear relationships established
between different factors. In the case of a single variable, the relationship is termed as
a simple linear regression while in case the variable is more than one, the relationship
becomes a multiple linear regression. Multivariate linear regression on the other hand
involves multiple co-related dependent variables. Linear regression adopts the use of
predictor functions expressed in a linear manner making use of unfamiliar paradigm
limits that process set of data [303]. Linear regression is the most widely read on and
oldest form of regression known [316]. In simple linear regression, the predictor vari-
able x is represented with a scalar response variable y. The model however makes vari-
ous assumptions; that a weak erogenous exists between the predictors, linearity in the
relationship between the variables, constancy in the variance in errors, independence of
errors, and lack of perfect multicollinearity in the predictors. During data forecast and
with the use of linear regression, past information is used to forecast trends that vary in
42


## Page 55


usability depending on the person undertaking the analysis. This form of analysis is also
used widely in the business ﬁeld to pre-determine occurrences, manage product quality
and assess the differences established in data types as input in decision making [161].
4.4.2
Multiple Linear Regression
As indicated previously, multiple linear regressions include the existence of more than
one variable with relation to a single independent factor. The relationship works to
ﬁt the information obtained from data into a single linear equation and as with linear
regression, the relationship between x and y has to be established. The variables are
expressed as:
x1, x2, x3, ..., xp
(4.2)
where:
y = b0 + b1x1 + b2x2 + . . . + bpxp
(4.3)
This line shows how the mean response y changes with the explanatory variables [356].
The observed values for y vary about their means y and are assumed to have the same
standard deviation . The ﬁtted values b0, b1, . . ., bp estimate the parameters 0, 1, ..., p
of the population regression line. Multiple regression is great model for establishing
variable linear relationships.
Multiple linear regressions include the existence of more than one variable with
relation to a single independent factor. The relationship works to ﬁt the information
obtained from data into a single linear equation, and as with linear regression, the rela-
tionship between x and y has to be established. The relationship between independent
and dependent variables is established by using regression standard multiple regression
where all of the independent factors are combined within the regression equation at the
same time [161] R and R are used to determine the power of relations amongst the
dependent variables [161]. Multiple regressions are great model for establishing vari-
able linear relationships. This form of regression analysis best beﬁts the forecast of a
continuous dependent variable from a variety of independent factors. t Multiple linear
regression can be further categorised into either hierarchical or step-wise multiple re-
gression. In hierarchical or sequential regression, independent factors are submitted in
binary steps, and the statistical change in R is applied to determine the signiﬁcance of
the variables introduced in the second stage [161]. Step-wise or statistical regression,
on the other hand, is useful in identifying the subclass of independent factors which
display the strongest relations to the dependent factors more economically inclined with
regards to regression analysis [161].
43


## Page 56


4.4.3
Ordinal Regression
Ordinal regression can also be referred to as ordinal classiﬁcation. This model of re-
gression is widely used for the classiﬁcation of ordinal variables [356]. These are vari-
ables which have values on an arbitrary scale thus creating a situation whereby only
where the relative ordering between different values is of importance. There are two
main examples of ordinal regression; ordered logit and ordered probit. The main use
for ordinal regression is in social sciences where sociological literature is a factor of
importance [356].
4.4.4
Multinomial Logistics Regression
This is another model of regression that is commonly used to provide estimations re-
garding nominal dependent variable given one or more independent variables [64].
Through constant updates and research, this model has been consequentially referred
to as being somewhat an annex of binomial logistic regression that offers a platform for
the dependent factor to have more than two classes [20]. This means that it its use is
paramount if the dependent factor contains more than two nominal or ordered categor-
ies. Multinomial logistic regression results to dependent variables that exist in the form
of dual ship and independent variables that are incessant and or speciﬁc [20]. When
using multinomial logistic regression analysis, dummy codding is frequently used as a
tool of the trade. A close relationship with other types of regression is that multinomial
logistic regression also exhibits the ability for the nominal and continuous independent
variables to interact. It is widely used in risk analysis as it offers an advantage over
other types of regression analysis methods [20]
4.4.5
Binomial Logistic Regression
This model of regression is similar to the multinomial logistic regression model. It is
commonly referred to as logistic regression and predicts probability on the basis that
tendencies, as noted above are very binary with regards to the number of dependent
factors founded on more than one independent variable. If the groups are more than
one, we have a multinomial logistic regression [214].
4.4.6
Mahalanobis Distance
The Mahalanobis distance is a method of measuring distance between a point and a
distribution centre [207]. The points were deﬁned as P while the distribution was deﬁned
as D. This theory is a way of establishing proponents that could cause deviations from
the point P to the mean dimension of the distribution point D. It is commonly used in
44


## Page 57


classifying data and involves consideration of variances that may occur within different
data clusters [207].
4.4.7
Naive Bayes Classiﬁer
Naive Bayes classiﬁer is a cluster/classiﬁcation technique that users the Bayes theorem
which asserts a level of independence between variables [249] and features that are to
be classiﬁed. This means that the theory assumes the existence or non-existence of very
feature is not connected to other features of the objects to be classiﬁed [218]. As demon-
strated by Gabriele et al. (2016) [329], a Naive Bayes classiﬁer is best suited for dataset
that is heterogeneous, incomplete, of small set sizes and categorical variables. Different
datasets include data is very categorical and involves variables such as gender, national-
ity or race. The incomplete dataset is data that may have other attached variables to it. A
good example is education level which can be a factor of nationality and gender [329].
This type of classiﬁer is most widely used in machine learning that requires the use of
heterogeneous sources for data such as social sciences. Robotics integration into the
human world is increasing at a swift rate, and thus the need to study their cognitive
behaviour is important since it forms a basis of knowledge on how they adapt to various
social environments.
4.5
Sentiment Analysis
Sentiment Analysis is a form of information analysis primarily employing a range of
techniques to obtain individual clusters of information from test data provided [249].
Sentiment analysis uses include, though they are not constrained to; business intelli-
gence, politics, and sociology. Data used for sentiment analysis is not limited to what
users say but can also be analysed from what they prefer when they are on internet-
based platforms [22]. This includes the videos they choose to watch, the sites they visit,
the kind of information they look for and the items they upload. These leads to their
opinions and sentiments since they are ﬁrst-hand choices made by the user. Sentiment
analysis is readily available for data mining since the social media industry has been on
an upward growth curve. The ability to link different platforms also makes it easy to
obtain more speciﬁc and accurate data.
According to Ghazaleh et al. [22] sentiment analysis is multidisciplinary and exam-
ines attitudes, emotions, opinions analysis regarding people oriented organisations, ser-
vices and with other people. Other are events, topics and includes multiple ﬁelds such as
natural language processing, computational linguistics, information retrieval, machine
learning and artiﬁcial intelligence. However, sentiment classiﬁcation approaches can be
classiﬁed into three main methods: lexicon based, hybrid approach and machine learn-
ing [82]. In the machine learning approach, sentiment analysis is used to predict how
45


## Page 58


polarised sentiments are based on trained as well as test datasets. The lexicon approach
does not take into account previous training or induction but instead uses a pre-existing
list of words that have been previously deﬁned to assert certain sentiments. The last
approach; the hybrid approach is a combination of machine learning and lexicon-based
approach. This approach is the most diverse and has a better potential of improving
sentiment classiﬁcation performance [82].
The use of sentiment analysis dates back to the spread of the Web in the early 2000s.
It has undergone development into various morphological states but can be categoric-
ally classiﬁed into ﬁve major steps of analysis; sentiment classiﬁcation data collection
sentiment detection, text preparation, and lastly presentation output [82]. As the name
suggests, data collection involves gathering information from the source. Natural lan-
guage processing and test analytics are used to extract the data since it is bulky and
disorganised making it impossible to collect manually. Text preparation is a data clean-
up process before analysis and involves removing all the unwanted content. Sentiment
detection is an examination phase where the subjectivity and objectivity of the data
are veriﬁed. Objective data is discarded while subjective data is stored. The last step;
presentation of output is the end goal of sentiment analysis as it converts various per-
sonal information to speciﬁc and meaningful data [82].
However, despite its importance, sentiment analysis can pose challenges when using
it and often end up providing incorrect results. Opinions are shaped by trends, social
status, economic status, geographical factors and even political factors. This means that
opinions may not be as independent as they should be. The bias created by factors
affecting the opinion of people consequentially means incorrect results when it comes
to sentiment analysis. Sentiment analysis also faces the challenge that emanates from
ambiguity that can couple social media posts [226]. Posts being analysed contain may
contain forms of opinions that are ironical and sarcastic which is very difﬁcult for ana-
lysing tools to detect.
4.6
Summary
This chapter summarises keys elements of the intersections between social networks,
artiﬁcial intelligence, natural language processing and sentiment analysis. With the rise
of research on large, complex networks and their characteristics, a substantial number
of studies have investigated social networks in an attempt to Understand its structures
whose nodes represent persons in the social context, and whose edges represent commu-
nication, collaboration, or connections between nodes and entities. With the increased
usage of the social networks, increasing the availability of big, complex datasets leading
to the stimulated extensive study of their fundamental properties [1, 56, 230, 229, 345].
Attracting scientists from a different discipline, to contribute to revealing more proper-
ties of the social network. Artiﬁcial intelligence and linguistics analysis play a vital role
46


## Page 59


in such process [308]. AI attempts to simulate the human intelligence by the computer,
Language/text data is one of the primary sources of interactions and expressions for
human-intelligence [233]. Computational intelligent is a signiﬁcant part of the ﬁeld of
AI, especially with the growth of the Linguistics ﬁeld and natural process area [96]. The
core issue of computational intelligence is the modelling of the primary linguistics pro-
cess – “learning” the languages and context. Overlapping with the broader problem of
AI, to learn perception, interaction, planning, decision making based on reasoning [7].
A combination of sentiment analysis and NLP is frequently used to help machine un-
derstanding the text [226], using machine learning algorithms to enable the program to
learn from the previous dataset, popular applications include but not limited to chatbots,
detecting spam ﬁlters and opinion mining. This chapter also highlights cutting-edge
classiﬁers and statistics analysis used in the study, emphasises the usage of the senti-
ment analysis. Furthermore, describing state of the art technology presented by IBM
in the ﬁeld of extracting personality and emotions using state-of-art languages analysis
and AI [305].
47


## Page 60


Chapter 5
Methodology
5.1
Introduction
Building on from the wider domain context and critical review of the literature from the
previous chapters, this chapter provides an detailed overview of the research methods
that were developed and followed in the study. It provides information on how the data
have been extracted from the complex computer system used as part of the stud. Explain
different types of data sources and how they were sampled. The researcher describes
the research design that was chosen for the purpose of this study and the reasons for this
choice.
5.2
System Overview
The dataset used in this study was collected and extracted from the online portal for
a European Union (EU) international scholarship mobility hosted at a UK university,
which we will further explain in Section 5.3; however, this section gives an overview
about the architecture of the system from technical perspective. The primary framework
for the web portal was, Joomla! 1 and it is divided into three layers as presented in
Figure 5.1 [325].
Extension layer with responsibility of handling the modules displaying information
on the interface, components, producing a complete functionality and interactive
dynamic like mini application. template, handling the development and design of
front-end and back-end template.
Application Layer to allow developers to run other and integrate other application into
Joomla core functionality.
1Joomla! Is a free and open-source content management system (CMS) for publishing web content.
48


## Page 61


Figure 5.1: Joomla! Framework Architecture [324]
Framework Layer is for writing pure web and command line applications in PHP.
Figure 5.2: MVC Framework Architecture [80]
The underpinning software design architecture used in Joomla is the Model/View/-
Controller (MVC) paradigm, a software design model commonly used for developing
user interfaces that separate an application into three interconnected parts (see Fig-
ure 5.2). The MVC design pattern is a frequently used methodology for the developing
of well-structured modular applications [148]; it is the main design pattern using in
Joomla’s Components. The primary function is to split an application into three lay-
ers to give the application ﬂexibility of debugging and investigation process for any
49


## Page 62


performance issues. By separate models and views as shown in ﬁg 5.2, MVC helps to
improve the ease of the complexity in architectural design and to increase the refactoring
and reuse of programming code [80].
The primary programming language in the web-based system is PHP2 and in the
backend database, are MySQL and the server running Linux on an Apache web server.
5.3
Data Sources and Workﬂows
The digital footprint dataset used as part of this study is extracted from the behaviour of
the user on a web-based educational application portal: “Online Portal for Scholarship
Mobility”. We make use of textual data, analysing with these same psycholinguistic
techniques, and employ standard statistical methods on non-textual data. The textual
data also includes interaction with a dedicated Facebook Page for resolving problems
with the applications (of which there were many); and, the actual documents submitted,
including a free-text application motivation letter. The non-textual data includes the
ﬁnal scoring of the individual for the grant they applied for (e.g. success, reserved,
failure) and the individual’s behaviour on the site (when they uploaded their documents,
how close to the deadline and so on).
The data comes from an online portal for a European Union (EU) international
scholarship mobility hosted at a UK university. The mobility programme aims to en-
hance quality in higher education through scholarships and academic cooperation between
Europe and the rest of the world. It provides mobility grants for students at different
educational levels (Undergraduate, Masters, PhD, Post-Doctoral, Faculty) and has nu-
merous courses available from a wide range of institutions across the EU.
The features of the call were as follows: there were 2,706 applications submitted
by 1,170 candidates, applying to 10 EU universities and ten non-EU universities. The
system allows an applicant to use to up to three courses from all courses offered by
the ten universities, and the applicant is required to assign a priority for each module.
This priority ﬁeld is the primary source of ﬁnal selection status in the selection stage,
for instance, if the applicant Accepted at Course A as a priority (1) and Course B as a
priority (2), then the 1st priority will be offered.
Each mobility call has an opening date/time and closing date/time, with occasional
extensions given for speciﬁc reasons (for instance due to administrative reasons or tech-
nical issues with the portal). Applicants are required to submit for their application spe-
ciﬁc necessary ﬁles, such as motivation letter, passport/identiﬁcation, curriculum vitae),
as well as optional data (supporting documents). The primary modes of communication
between candidates and the project team are via emails, telephone and the dedicated
2PHP: Hypertext Preprocessor is a commonly-used open source multi-purpose scripting language that
is particularly suited for web development and can be embedded into HTML.
50


## Page 63


Facebook Page. The selection process divided into three stages: Eligibility, Evaluation
and Final Selection.
Based on which rank the applicant assigned to the host university, the ﬁnal selection
is the top n of applicants. n is calculated based on the host capacity and budget of the
project. This process results in the ﬁnal classiﬁcation of the applicant as either:
• Accepted (ranked highest);
• Reserved (passed but not selected);
• Rejected (below passing grade);
• Ineligible (missing documents or out-dated documents).
While the call is running there were three approaches used to provide the user with
a platform to communicate with the technical support team and the administrator’s team
in case of project coordinator team:
• Facebook Page;
• Ticketing (help desk platform);
• Emails.
5.3.1
Motivation Letters
All users asked to submit a motivation letter (personal statement) as part of the applica-
tion process; the uploading process applies certain technical restrictions to the ﬁle type,
in which only limits to image ﬁles, not PDF ﬁles. For this study, all motivation-letter
image ﬁles converted using an OCR Java SDK3 and Google Cloud Vision API for OCR
4, to save all image ﬁles into Text ﬁles.
5.3.2
Role of the Facebook Page
Facebook Pages play a vital role in improving the communication between users and
program coordinators, and the signiﬁcant positive inﬂuence of “Friends like”, “online
activities” in promoting to business [281]. In the current system, a Facebook created
and managed by project coordinators to interact and communicate with users, During
the scholarship calls as described previously, the Facebook page is used to receive an
administrator enquires and technical reports. Facebook provides an SDK to allow de-
veloped to retrieve and to interact with their database via the API [134]. A PHP with
3ABBYY FineReader v11.0.102.583 OCR Corporate Edition JAVA SDK
4https://cloud.google.com/vision/docs/ocr
51


## Page 64


Joomla Framework script was developed to retrieve all posts and store it in a local
MySQL DB for further analysis (see Section 5.1).
1 $db= J F a ct o ry : : getDBO ( ) ;
2 $graphEdge=$response −>getGraphEdge ( ) ;
3 do {
4 f o r e a c h
( $graphEdge
as
$graph )
5 {
6
i f
( i s s e t ( $graph [ ’ message ’ ] ) )
7
{
8
$message=$graph [ ’ message ’ ] ;
9
$msg id=$graph [ ’ id ’ ] ;
10
t r y
{
11
$response comments = $fb−>get ( ’ / ’ . $msg id . ’ / comments / ? l i m i t = ’ .
$maxPages ,
$accessToken ) ;
12
} catch ( Facebook \ Exceptions \ FacebookResponseException
$e ) {
13
echo
’ Graph
r e t u r n e d
an
e r r o r :
’
.
$e−>getMessage ( ) ;
14
e x i t ;
15
} catch ( Facebook \ Exceptions \FacebookSDKException $e ) {
16
echo
’ Facebook SDK r e t u r n e d
an
e r r o r :
’
.
$e−>getMessage ( ) ;
17
e x i t ;
18
}
19
$commentNext =0;
20
$graphComments=$response comments−>getGraphEdge ( ) ;
21
do {
22
/ / comments
23
f o r eac h ( $graphComments
as
$graphcomment )
24
{
25
$ f i l t e r
=
J F i l t e r I n p u t : : g e t I n s t a n c e ( ) ;
26
$msg= $ f i l t e r −>clean ( $graphcomment [ ’ message ’ ] ,
’ f i l t e r ’ ) ;
27
$msg = p r e g r e p l a c e ( ’ / [ ˆ A−Za−z0 −9]/ ’ ,
’
’ , $msg ) ;
28
29
$sql = ’INSERT INTO ‘ allCommentsData ‘
( ‘ id ‘ ,
‘ message id ‘ ,
‘ fb id
‘ ,
‘ date time ‘ ,
‘name ‘ ,
‘ message ‘ ,
‘ system ‘ ) VALUES (”NULL” ,
” ’ .
$graphcomment [ ’ id ’ ] . ’ ” ,
” ’ . $graphcomment [ ’ from ’ ] [ ’ id ’ ] . ’ ” ,
” ’ .
$graphcomment [ ’ c r e a t e d t i m e ’]−>format ( ’Y−m−d h : i : s ’ ) . ’ ” ,
” ’ .
$graphcomment [ ’ from ’ ] [ ’name ’ ] . ’ ” ,
” ’ . $msg . ’ ” ,
” ’ . $system . ’ ”) ; ’ ;
30
$db−>setQuery ( $sql ) ;
31
i f
( ! $db−>Query ( ) )
32
{
33
e x i t ( ) ;
34
}
35
36
$commentNext ++;
37
}
38
} while
( $commentNext < $maxPages && $graphComments = $fb−>next (
$graphComments ) ) ;
39
40
}
52


## Page 65


41
/ / p r i n t r ( $graph ) ;
42 }
43
$pageCount ++;
44 } while
( $pageCount < $maxPages && $graphEdge = $fb−>next ( $graphEdge )
) ;
45
46 }
Listing 5.1: Retrieve Facebook Posts and Store to local MySQL for further analysis
5.3.3
Help Desk Platform and Ticketing System
The ticketing help desk deployed and installed as part of the methods to communicate
with the uses in case they have any questions or problem using the system. The help
desk in our system 5 used MySQL as the backend database. The stored data has been
collected with all DateTime stamp and merged with the data gathering from Facebook
posts.
5.4
Identifying Computer System Status and Events
As presented in Section 3.4.1, we have a range of computer errors, system errors and
applications and that map on the HTTP/Web application to HTTP status codes for server
errors for server slow and both can be triggered by a different computer error. To identify
the system events to be able to investigate the personality and emotion. For this analysis
started by dividing the source of data into three types:
To investigate the Google Analytics data and speciﬁcally speed-time loading of the
page to monitor the page impression and detect the number of users on the system
and this point. And investigate the Apache log server to track the triggered errors at
the different time to understand more about the system behaviour. The four categories
reﬂect the detailed system status as an output from this process:
• Idle: The system reported as working ﬁne and server response time is fast.
• Slow: The system reported as slow in response by the users and the server re-
sponse time is below acceptable average.
• Down: The system reported as not accessible by the users and the server response
time is zero.
• Error: The system reported as accessible by the users but not working as expected
with a cretin error code or unexpected behaviour
5HESK – a free PHP help desk – https://www.hesk.com/
53


## Page 66


5.4.1
Identifying System Status
In this section we present the steps undertaken to identify the system status from the
dataset collected:
Step 1
Server Status
Keywords
Idle
Working ﬁne, thanks
Error
Error, FTP, SQL, code
Down
Down, not working, cannot access
Slow
Cannot upload, slow, upload
Table 5.1: Keywords used to identify each server status
For the dataset – collected from the system as explained in Section 5.3 – the users
had two platforms to submit their technical problem: a Facebook Page and the HESK
helpdesk platform. All text collected and search by keywords as following to identify
the status of the system as shown in Table 5.1.
Step 2
From the start of the project, Google Analytics is integrated into the web-application
system to monitor the system behaviour and to detect and verify of the reported sys-
tem status, the average server response (seconds) were all stored on MySQL database
and investigated in the next step. Figure 5.3 shows an indicative sample of the server
response from 8 January 2012.
Figure 5.3: Average server response (in seconds) from Google Analytics on 8 January
2012
54


## Page 67


Step 3
Searching through all posts posted by users during the usage of the system with a sample
of keywords as per Table 5.1. Investigating the Google Analytics, in the exact date and
time of each post and check if the server response time conﬁrms the status or not.
User ID
Facebook Post
Date time
Server
Response
(Seconds)
1466
i have this msg Database Error
Unable to connect to the database
Could not connect to MySQL
2012-01-08
21:26:50
2.16
2449
Database Error Unable to connect
to the database Could not connect
to MySQL this message error show
now
2012-01-08
21:42:51
4.95
2304
please advice about the below:An
Error has occurred!
Unable to
open JFTP connection
2012-01-08
22:57:58
15.33
Table 5.2: Facebook posts with keyword error and server response
• Table 5.3 shows a sample of the posts posted on Facebook page with the keyword
down, and the server response extracted from Google Analytics; as shown, the
server response reported were zero, which conﬁrms the server status as down.
• Table 5.4 shows a sample of the posts posted on the Facebook page with the
keyword thanks or working ﬁne, alongside with the server response rate reported
by Google Analytics in same time and date. The server response rate stated was
below 0.1 and above 0 and according to Nielsen (1993) [232] that considered as
acceptable idle system behaviour for the users, which conﬁrms the server status
as Idle.
• Table 5.2 shows sample of the posts posted on Facebook page with the keyword
error, and ﬁgure 5.3 shows the Server response time reported in Google Ana-
lytics. At the time of the posts reported in the 5.2 the server response reported
were above the idle system response reported by Nielsen [232] which conﬁrms
the server status as error
• Table 5.5 shows sample of the posts posted on Facebook page with the keyword
slow or uploading. Using Google analytics as the main source of extracting the
55


## Page 68


User ID
Facebook Message
Datetime
Server
Response
(Seconds)
4669
the site is down i just need to upload
few doc only
2012-01-22
05:32:38
0
163
i didnt complete the upload of my
papers and i am trying from friday
and the site give me always error
and always down please if you can
help me Youssif Rady please send
me the solution
2012-01-23
11:02:26
0
3650
i know time is over now but i am
one of many people who wanted to
just click submit the application but
the site was down due to high trafﬁc
and that s not just today yesterday
and 2 days before Justice is needed
Admin
2012-01-22
22:10:53
0
4895
i just want to click my submission
button and the system is down
2012-01-21
20:57:36
0
4895
everything
is
already
uploaded
since yesterday i just need to click
on the submission button and the
system have bee down for the past
24 hours and i dont know what to
do
2012-01-21
21:03:16
0
3396
Thanks it wasn t necessary to ex-
tend it 13 days more 6 or 7 days
would have been enough to downs-
ize the trafﬁc load but anyway
thanks a lot
2012-01-09
19:45:50
0
3339
The site is down Element Scholar-
ships Program
2012-01-20
19:15:19
0
1841
Please check the website it is down
to complete the uploading
2012-01-21
12:58:43
0
Table 5.3: Facebook posts with keyword “down” and server response
server response a shown in the Table 5.5. The average seconds reported is above
10 seconds which conﬁrms the status as slow assumed by Nielsen (1993) [232].
56


## Page 69


User ID
Facebook posts
Datetime
Server
Response
(Seconds)
2016
Thanks for considering me I think
the problem is not only the trafﬁc
because I haven t wait to the last
minutes I ve tried to upload my doc-
uments since lots of days
2012-01-22
16:32:05
0.03
1918
thanks I received am to login and
submit but I already logged in
2012-01-22
18:01:28
0.04
1918
Dear Element Scholarships Pro-
gram admin I received an email but
I can t to submit can you help please
thanks
2012-01-22
18:19:09
0.04
2498
i am the only student who ap-
plied from the faculty of science ain
shams university only only only i
need to submit my application to
graz university could you do that
please username ahmed mounir
email bashkora yahoo com thanks
very much
2012-01-22
18:28:25
0.04
Table 5.4: Facebook posts with keyword “idle” and server response
Server response time
, as part of Google Analytics, there are behaviour reports, to
indicate how system behaviour over time, as Reduce back-end processing time or place
a server closer to users. According to Nielse (1993)n [232], to determine an excel-
lent acceptable server response time from the server is measured as following with the
three Important Limits, there are three primary time limits (which are deﬁned by human
perceptual abilities) to keep in mind when optimising web and application performance.
The fundamental knowledge regarding response times has been about the same for thirty
years as it is human perceptual abilities.
• 0.1 second is approximately the limit for having the user sense that the system is
reacting immediately, meaning that no particular feedback is required except to
display the result.
• 1.0 second is approximately the boundary for the user’s stream of thought to stay
constant, even though the user will notice the lag. Typically, no feedback expected
during stoppages of longer than 0.1 but less than 1.0 second, but this may cause
57


## Page 70


User ID
Facebook Message
Date time
Server
Response
(Seconds)
1361
when i upload any word ﬁle not ac-
cpted what is the type of ﬁle you
need to submit
2012-01-07
14:23:47
14.72
339
i have a question this error mes-
sage means that the paper is not
uploaded although this massege ap-
peared i saw correct sign in the
front of the required paper so that
i submitted my application
2012-01-09
00:31:27
28.89
2022
am tryn 2 upload only 2 ﬁles for7
hours still didn t succeed
2012-01-09
02:49:27
16.42
3598
i have one document left plzzz i
struggled to get my documents ﬁxed
i need to upload the last one
2012-01-09
14:39:44
22.77
3937
Same here I cannot upload all my
documents due to lack of access to
the programme s website
2012-01-09
16:10:44
19.51
3339
The site is not working at all please
help I wanna upload the invitation
letter
2012-01-19
11:46:49
54.15
Table 5.5: Facebook posts with keywords related to uploading/slow performance, along-
side server response
the user to lose interest in continue working on the data directly.
• 10 seconds is approximately the limit for retaining the user’s concentration on the
system interface. For continued delays, users will want to accomplish other jobs
while waiting for the system to ﬁnish, in such cases it is suggested to give the user
an indicates about the system’s progress. In many cases, the user will lose interest
and might interrupt or cancel the task.
5.5
Extracting Personality Traits
As part of the feedback process, and for propose of this research. A Big Five Ques-
tionnaire sent to users used this system to for further analysis as part of this study. The
number of responders if 80 users ﬁlled out the questionnaire. For extracting the per-
58


## Page 71


sonality traits, a Java engine developed to check if the user ﬁlled out the survey it will
be the primary source of Big Five Traits. However, in case the user did not ﬁll in the
questionnaire, then the motivation letter combined with all Facebook and Help Desk
correspondents will be used as the primary source to extract Big Five Personality Traits
(Using either Mairesse tool or IBM Watson Tool).
5.5.1
Using the Mairesse Approach
Mairesse (2007) [196], research study, presented a model to extract the personality and
posted the source code publicly to be used.6. Suggested model built based on querying
the Medical Research Council (MRC) Psycholinguistic Database 7 and LIWC, also, the
Mairesse’s tool were validated and assessed [354, 255, 320]. Mairesse’s tool used as
one of the leading approaches to extract the personality traits until IBM released a new
tool to allow us to retrieve the personality traits more efﬁciently (See Section 5.8 for
further information).
5.5.2
Rationale of Using the Big Five Personality Theory
According to the literature we reviewed in Section 2.4, the Big Five personality traits is
state of the art in classifying the personality, furthermore, the classiﬁcation based on the
lexical hypothesis, which was ﬁrst produced in 1884, by Sir Francis Galton [116]. For
last decades psychology researchers have used the adjectives to describe personality and
classify the traits according to the adjective in English dictionary till it is now limited
to ﬁve factors [17][336] [234]. As the Big Five personality traits original based in the
lexical hypothesis, it was decided the best ﬁt in this study, as the main dataset stream
(see Section 5.3) to extract social networks interactions as text posted or motivation
letters uploaded to the system.
5.6
Extracting Emotions from Text
As the literature revealed a powerfull produced by IBM (See section - 4.2.3) Using
emotion tone the methodology is output from their emotion analysis research, which is
an ensemble framework to infer emotions from a given text.
Generalisation-based ensemble framework is applied To derive emotion scores from
the text. A stacked generalization is a general method of using a high-level model to
combine lower-level models to achieve more signiﬁcant predictive accuracy.
6Online Java code based on Mairesse model
7Psycholinguistic information about more than 150,000 words over 14 linguistic features.
59


## Page 72


Features such as n-grams (unigrams, bigrams and trigrams), punctuation, emoticons,
curse words, greeting words (such as “hello”, “hi”, and “thanks”), and sentiment polar-
ity are fed into state-of-the machine learning algorithms to classify emotion categories.
Emotion categories are the benchmark against standard emotion datasets such as
ISEAR8 and SEMEVAL9. The emotion tone engines outcomes reveal that the average
performance of the model (macro-average F110 score is approximately 41% and 68%,
sequentially). The output is stated to be statistically better than the top efﬁciency by the
state-of-the-art models (F1 are approximately 37% and 63% sequentially) [157].
5.7
Mapping Facebook User Proﬁles
As explained previously, the primary dataset of this study is coming from Facebook
as social interactions and professional interaction with the complex computer system
used to accept an application for the particular program. The dataset collected from
web-application and Facebook, however, one of the challenges were to match Facebook
User and their account on the system, since the EU Scholarship System did not deploy
the Login using Facebook OAuth. OAuth is a login protocol introduced in late 2007 to
support login by social networks[178].
Figure 5.4 shows the ﬂowchart of the matching algorithm to achieve this task as well
as manual detection is included in different stages and a random sample of the output of
the algorithm to ensure the accuracy.
The primary objective of the matching algorithm is to match between users from the
Facebook page detected to the system and with the users from the system. Furthermore,
the number of Facebook posts collected is 2,681. Therefore, an automation algorithm
suggested producing to obtain all text from the social network (Facebook) and start to
classify the interactions text by FacebookID 871 user. However, although the automa-
tion model proofed an excellent accuracy the nature of the Facebook privacy restrictions
and the use of Nicknames rather than the real names, impacted on the outcome of the
automation process.
The usage of the Facebook Page was not only for social or announcement purposes.
The project coordinators decided to lunch the page as for technical errors support. Fur-
thermore, the administrators of the project meant to ask the Facebook users to post their
username on their correspondences on social media to allow the administrator team to
located the user’s quickly especially when it is related to technical support. Therefore,
part of the automation process is to search for the word Username and return the next
word as the username as shown in Figure 5.5, however, as shown in Figures 5.6 some
8ISEAR Databank: Over a period of several years during the 1990s, a large group of psychologists all
over the world gathered data in the ISEAR project [298].
9Sentiment Analysis in Twitter [351].
10F1 score is a means of a test’s accuracy
60


## Page 73


Figure 5.4: Algorithm to match users from Facebook with users on our system
other cases the next word was is. Therefore, the algorithm as shown in Figure 5.4 and
see Listing 5.2 check if the following word number of characters is less than three (Min-
imum number accepted by Joomla!) then escape this word and pass the word after to
the matchUserName function to return the username is found.
The function matchUserName veriﬁes if the username matches the name of the user
on Facebook and returns the User ID on the system; if not then Return False, and move
to the other process to match the user details from Facebook to the User’s Basic Inform-
ation.
The outcome of the ﬁrst phase ﬁnd username in the post successful matched 9% of
the dataset. The next phase in the automation process is to match the user’s details from
61


## Page 74


Figure 5.5: Example 1: Usage of username in a post
Figure 5.6: Example 2: Usage of username in a post following is after username
the Facebook with the essential information from the system, the primary limitation for
this process was the privacy applied by each user is different from each. The algorithm
managed to successfully match 39% of the dataset by matching Name, Gender, City,
University. The ﬁnal output of the automation process is 58% successful matches.
As shown in Table 5.6 the semi-manual veriﬁcation phase, is to match the rest of
42% of the dataset that failed to be matched by the previous automated system, by
manually match the proﬁle picture of the user with proposed users from the system. The
reason it is called semi-manual, the proposed list of users is generated by the algorithm
to get the closest users from the system to the Facebook proﬁle with the available data
although, it is not totally match, it is still suggested to the manual veriﬁcation due to the
fact the users on Facebook uses a nicknames instead of the real names. The outcome of
the semi-manual veriﬁcation is 15%. And the overall failed to match is 36%.
1 /∗∗
2 ∗Function
getUsername
3 ∗@param :
$message
String , $name
String , $system
4 ∗@param :
Return
f a l s e
i f
not
found ,
u s e r i d
i f
found
5 ∗@throws :
none
6 ∗/
7 f u n c t i o n
getUsername ( $message , $name , $fb id , $sys )
8 {
9
/ / Param Sys
r e f e r
to
which
system
s i n c e
t h e r e
was
t h r e e
systems
running
on same time .
10
$message= s t r t o l o w e r ( $message ) ;
11
$msg=explode ( ” ” , $message ) ;
12
f o r
( $i =0; $i<count ( $msg ) ; $i ++)
13
{
14
i f
( $msg [ $i ]== ” username ”
| |
( $msg [ $i ]== ”name” && $msg [ $i −1]==”
user ” ) )
15
{
62


## Page 75


16
$next=$msg [ $i +1];
17
i f
( s t r l e n ( $next ) <=3)
18
{
19
$check= $ th i s −>matchUserName ( $msg [ $i +2] , $name , $fb id ,
s t r t o l o w e r ( $sys ) ) ;
20
i f
( $check )
21
{
22
r e t u r n
$check ;
23
}
24
}
25
e l s e
26
{
27
$check= $ th i s −>matchUserName ( $next , $name , $fb id , s t r t o l o w e r (
$sys ) ) ;
28
i f
( $check )
29
{
30
r e t u r n
$check ;
31
}
32
}
33
}
34
}
35
r e t u r n
f a l s e ;
36 }
Listing 5.2: Matching Algorithm - PHP SnapShot Code: Searching for username
Process
Progress of matching
Find username in post
9%
Match Basic Information
39%
Semi-Manual Veriﬁcation
15%
Failed to match
36%
Table 5.6: The performance of the matching algorithm
5.8
Verifying Accuracy using the IBM Watson Tone Ana-
lyzer
5.8.1
Introduction
In 2013, IBM announced the release of its Watson Tone Analyzer service to allow the
identiﬁcation of personality traits based on how people write. The tool is based on uses
linguistic analysis to read and demonstrate emotions, personality traits, and language
63


## Page 76


usage found in text. Emotions extracted based on basic emotion methodology as dis-
cussed in Section 4.2.3.
The Personality Insights service suggests personality traits from textual data based
on an open-vocabulary method. This tool represents the latest research developments
in inferring personality [301, 267]. This section will highlight a speciﬁc service inside
IBM Watson tool, which used mainly to extract personality traits. The service ﬁrst seg-
ment the input text to develop the design in a n-dimensional space. The service uses an
open-source word-embedding method called GloVe11 to obtain a vector representation
for the words in the input document [262]. It then provides this output to a machine
learning algorithm that predicts a personality proﬁle with the “Big Five”. The tool uses
scores collected from questionnaires carried between thousands of users along with data
from their Twitter supplies to train the model.
This experiment is to verify the accuracy of the IBM Watson Engine before using
it for further analysis. Although, IBM conducted a validation study to understand the
accuracy of the service’s approach to understanding a personality proﬁle. IBM collec-
ted questionnaire responses, and Twitter feeds for more than 2000 active users for all
features and languages [301, 267]. It is thus essential to verify the tool for the dataset
used in this thesis (as presented in Section 5.3).
The dataset of all experiments extracted from a complex web-based application de-
signed to accept scholarship applications from users. After the result is announced the
program administration posted certain questions in order to get a feedback about the
scholarship and services in general for propose of improving user experience and sys-
tem quality. Approaching administration team to post Big Five questionnaire as part of
the follow up stages in order to improve user experience by understand more about the
user’s personality type.
The Big Five Questionnaire were ﬁlled out by 87 participant as it was posted the
Facebook page of the scholarship program, and were open for anyone to ﬁll in the
Questionnaire, however, not all of the 87 participant were an existed user of the previ-
ous existed dataset. Using the matching algorithm in Section 5.7, to match users from
Facebook with users from the system 67 users have been found. Only 43 users from
the 67 dataset reported to have ﬁlled in the motivation letter which will be used as Text
Source for the this experiment. The ﬁnal dataset consist of 43 user ﬁlled out the Big
Five questionnaire and had records of the motivation letter and Facebook interactions
on the database.
5.8.2
Comparing Statistical Differences Between Traits
Independent-samples t-test, the independent-samples t-test is used to determine if a dif-
ference exists between the means of two independent groups on a continuous dependent
11GloVe is an unsupervised training algorithm for getting vector representations for words [261].
64


## Page 77


variable. More speciﬁcally, it will let you determine whether the difference between
these two groups is statistically signiﬁcant. Before applying the t-test to the dataset, a
check to determine if the dataset is normally distributed or not is part of the assumption
before using t-test. Table 5.7 shows the Tests of Normality, independent variables are
Big Five traits and groups divided into Questionnaire result and IBM Watson Personality
insight.
Kolmogorov-Smirnova
Shapiro-Wilk
Statistic
df
Sig.
Statistic
df
Sig.
Extraversion
.114
86
.008
.960
86
.009
Agreeableness
.118
86
.005
.922
86
.000
Conscientiousness
.145
86
.000
.931
86
.000
Neuroticism
.094
86
.057
.966
86
.023
Openness
.159
86
.000
.922
86
.000
Table 5.7: Independent samples t-test - Tests of Normality
The Big Five traits (Extraversion, Agreeableness, Conscientiousness, Neuroticism
and Openness) were usually not distributed, as assessed by Shapiro-Wilk’s test (p < .05).
The assumption is not met, however, the decision is to run the test regardless because
the independent-samples t-test is relatively robust to deviations from normality and in
the run the Mann-Whitney U test to conﬁrm the result.
There was a statistically signiﬁcant difference in mean traits score between Big Five
Questionnaire and IBM Watson Personality Insight across all traits as reported in the
Table 5.8.
5.8.3
The Mann-Whitney U Test
The Mann-Whitney U test is a non-parametric method to verify the output of the previ-
ous independent-samples t-test, used to conﬁrm the t-test result.
The Mann-Whitney U test was run to determine if there were differences in traits
score between personality traits produced from IBM Watson and the questionnaire.
Independent Samples Test
Levene’s Test for Equality of Variances
t-test for Equality of Means
F
Sig.
t
df
Sig. (2-tailed)
Mean Difference
Std. Error Difference
95% Conﬁdence Interval of the Difference
Lower
Upper
Extraversion
Equal variances assumed
2.505
.117
1.836
84
.070
.09279
.05054
-.00771
.19329
Equal variances not assumed
1.836
80.811
.070
.09279
.05054
-.00777
.19335
Agreeableness
Equal variances assumed
.004
.951
1.065
84
.290
.05837
.05483
-.05066
.16741
Equal variances not assumed
1.065
83.990
.290
.05837
.05483
-.05066
.16741
Conscientiousness
Equal variances assumed
2.981
.088
1.814
84
.073
.07674
.04230
-.00737
.16085
Equal variances not assumed
1.814
80.459
.073
.07674
.04230
-.00742
.16091
Neuroticism
Equal variances assumed
19.769
.000
.972
84
.334
.03907
.04018
-.04083
.11897
Equal variances not assumed
.972
68.676
.334
.03907
.04018
-.04109
.11923
Openness
Equal variances assumed
3.754
.056
-1.258
84
.212
-.06674
.05307
-.17227
.03878
Equal variances not assumed
-1.258
82.017
.212
-.06674
.05307
-.17231
.03882
Table 5.8: Independent Samples Test
65


## Page 78


Null Hypothesis
Test
Sig.
Decision
The distribution of Extraversion is the same across categories of Group
Independent C5- Samples Mann-Whitney U Test
0.056
Retain the null hypothesis
The distribution of Agreeableness is the same across categories of Group
Independent C5- Samples Mann-Whitney U Test
0.188
Retain the null hypothesis
The distribution of Conscientiousness is the same across categories of Group
Independent C5- Samples Mann-Whitney U Test
0.89
Retain the null hypothesis
The distribution of Neuroticism is the same across categories of Group
Independent C5- Samples Mann-Whitney U Test
0.344
Retain the null hypothesis
The distribution of Openness is the same across categories of Group
Independent C5- Samples Mann-Whitney U Test
0.327
Retain the null hypothesis
Table 5.9: Hypothesis Test Summary - Mann-Whitney U Test
Distributions of the all traits for both IBM Watson and the Questionnaire were sim-
ilar, as assessed by visual inspection 5.7. Extraversion for IBM Watson (48.64) and
Questionnaire (38.36) was not statistically signiﬁcantly different, U = 43, p = 0.056,
Agreeableness for IBM Watson (47.05) and Questionnaire (39.95) was not statistically
signiﬁcantly different, U = 43, p = 0.188, Conscientiousness for IBM Watson (48.07)
and Questionnaire (38.93) was not statistically signiﬁcantly different, U = 43, p = 0.89,
Neuroticism for IBM Watson (46.05) and Questionnaire (40.95) was not statistically
signiﬁcantly different, U = 43, p = 0.344 and Openness for IBM Watson (40.86) and
Questionnaire (46.14) was not statistically signiﬁcantly different, U = 43, p = 0.327.
5.8.4
Summary
The output from The Mann-Whitney U tests shows no signiﬁcantly statistically dif-
ferent between both groups. Furthermore, it agrees with the evaluation report pro-
duced by IBM discussed previously in Chapter 4.2.3 and conﬁrms the conclusion from
Independent-samples t-test.
5.9
Summary
Following on from the discussion and analysis in this chapter, the following chapter
outlines the ﬂow of the experiments and how each experiment builds upon the previous
one, underpinned by the literature review ﬁndings.
66


## Page 79


Figure 5.7: Population pyramid representing personality traits
67


## Page 80


Chapter 6
Empirical Grounding for the PMsys
Engine
6.1
Introduction
This chapter presents the experiments conducted as part of this study towards extracting
the key features, to allow the development of the conceptual model. It starts by explor-
ing the structure of the available variables of the dataset and demonstrates the ﬂow the
feature process. Furthermore, this chapter examines the underlying association between
personality and emotions, and its impact on users behaviour in a digital domain, identi-
fying the main features and elements of our proposed model.
6.2
Proﬁling Complex Online Interactions
6.2.1
What Behaviour Can You Infer From a Digital Footprint?
Understanding the software development process is essential to facilities it’s effective
and efﬁcient to use as a core part of the broad ﬁeld of human-computer interaction.
Different users from different conceptual models about their interactions and have dif-
ferent ways of obtaining and developing knowledge and skills; cultural and national
differences may also play a signiﬁcant role. Another consideration in human-computer
interaction is that technology – and in particular, user interface technology – changes
rapidly, offering new interaction possibilities to which previous research ﬁndings may
not necessarily apply. Alongside this, user preferences (and the way in which they inter-
act with the software) change as they gradually master new interfaces and environments.
Personality and behaviour is determined from digital data [256, 340, 156, 236, 242].
Previously, the textual information consisted of the container of the blogs, status posts
and photo comments [28, 29], there is also a wealth of information in the other ways
68


## Page 81


of interacting with digital artefacts; for instance, it is possible to observe the ordering
(and frequency) of button clicks for a user[196]. Demonstrating the use of features from
the psycholinguistic databases LIWC [256] and MRC [353] to create a range of statist-
ical models for each of the Big Five personality traits [234, 253, 124]. As discussed
previously, these ﬁve traits are: Extraversion, Emotional Stability, Agreeableness, Con-
scientiousness and Openness to Experience. Equation 6.1 describes Extraversion, where
each feature is preﬁxed by the containing database.
Extraversion =
-0.0379 * MRC.K_F_NSAMP +
-0.0803 * LIWC.UNIQUE +
-0.6074 * LIWC.ABBREVIATIONS +
0.1445 * LIWC.PRONOUN +
-0.3941 * LIWC.HEARING +
17.1407;
(6.1)
Initially, in this analysis it is divided into three different types of experiments:
Experiment 1 comparing the motivation letters against the Facebook interactions;
Experiment 2 examining the interaction footprints against the motivation letters;
Experiment 3 validating the raw data using multiple regression.
6.2.2
Parameters and Feature Extraction
Applicants are required to upload a description of why they are applying for this particu-
lar mobility grant, the motivation letter. Applicants also communicated with the project
team through the project Facebook page [242].
This experiment is part of the feature extraction process, one of the objectives it to
the determination whether to include ﬁnal selection as part of the features or not (see
Section 5.3). The text was extracted from all motivation letters and Facebook interac-
tions and analysed both blocks of text according to the Five Factor personality traits
as discussed previously. To examine the strength of the relationship between the two
extracted ﬁve big personality traits list. Kendalls Tau and Spearmans rank correlation
coefﬁcient assess statistical associations based on the ranks of the data. Kendall’s tau!
Roger News (1990) [172] argues that the distribution of Kendalls tau has better stat-
istical properties that Spearman’s rank and the interpretation of Kendalls tau regarding
the probabilities of observing the agreeable (concordant) and non-agreeable (discord-
ant) pairs are very direct. Kendall rank is used to investigate the relative position of
each and compare both lists, after extracting the ﬁve factors for each applicant. Kendall
rank correlation statistic [171]. For these groups, the average Kendall’s tau coefﬁcient
69


## Page 82


value is reported, for each of the Five Factor features. By considering rank position and
not absolute value, we mitigate against explaining values without baseline experiment-
ation [242].
Key Findings
Experiment 1, Table 6.1 shows the results of the Kendall’s tau coefﬁ-
cient, speciﬁcally the variant that makes adjustments for ties (Tau-b). Values of Tau-b
range from -1 (100% negative association, or perfect inversion) to +1 (100% positive
association, or perfect agreement). A value of zero indicates the absence of association.
Group
E
ES
A
C
O
All
−0.094
0.099
0.145
0.025
−0.379
Accepted
0.000
0.000
0.000
0.000
0.800
Rejected
−0.244
0.333
−0.067
0.022
−0.244
Reserved
0.010
0.010
0.162
0.153
−0.6
Table 6.1: Average rank correlation for applicant group versus personality traits (E: Ex-
traversion; ES: Emotional Stability; A: Agreeableness; C: Conscientiousness; O: Open-
ness to Experience)
The most signiﬁcant positive relationship is between those applicants Accepted and
the feature Openness to Experience (Tau-b = 0.8). A strong negative relationship exists
between those applicants Reserved and the feature Openness to Experience (Tau-b =
-0.6).
6.2.3
Relating a User’s Digital Behaviour and Personality Traits
Classiﬁcation the applicant’s timeline by simpliﬁed an applicant’s interaction, or timeline,
with the portal to include the following milestones: T0 Registration Time; T1 First Ac-
tion; T2 Last Action; and, T3 Submission. Additionally, representing the extension
to the submission deadline as T4 Extension. In this way it is possible to represent an
applicant’s interaction as shown in Figure 6.1, which shows seven example timelines.
Using these milestones it is possible to identify interesting behaviours that compare
and contract with personality traits and other sources of information. Behaviours such
as: how long it was before an applicant became aware of the call, and when they re-
gistered; how long after registration did the applicant carry out their ﬁrst action with
the system; how long did they take to complete their application; and, how close to the
deadline did they submit their application.
The timeline of the call was divided into ﬁve segments as presented in the following
Table 6.2. The complete timeline from opening to ﬁnal close was 125 days. There was
an extension from day 112 until day 125. The presentation of the segments or timeline
periods is as percentage chunks of the entire timeline, for instance, segment S0 is the
70


## Page 83


Figure 6.1: Seven example user time-lines. T0 (black bar) is when the applicant ﬁrst
registered with the call. T1 (red bar) represents when the applicant uploaded their ﬁrst
document, or First Action. T2 (green bar) represents an applicants’ Last Action. T3
(blue bar) represents the applicants’ Submission. T4 (aquamarine bar) represents the
ﬁrst deadline (certain calls had initial deadlines extended)
ﬁrst 20% of the timeline, and so ranges from day one until day 25, segment S1 ranges
from day 26 until day 50, and so on [242].
Segment
Start
Finish
S0
0
20
S1
20
40
S2
40
60
S3
60
90
S4
90
100
Table 6.2: Timeline periods as percentages of total timeline
Using these segments it is possible to assign the various applicant actions (T0 Regis-
tration, T1 First Upload, T2 Last Upload, T3 Submission) to various time periods. The
segmentation allowed us to assign applicants to statistically signiﬁcant categories, and
also to add in a few categories from observations. These shown in Table 6.3; a small
number of applicants (n=4) registered within the segment S1 (20-40% of the timeline),
71


## Page 84


and then uploaded all of their documents and submitted within the segment S3 (60-90%
of the timeline). Class A represent this segment. The rest of rows applies the same
classiﬁcation.
Class
n
T0
T1
T2
T3
A
4
S1
S3
S3
S3
B
14
S2
S2
S2
S2
C
128
S2
S3
S3
S3
D
29
S2
S3
S4
S4
E
678
S3
S3
S3
S3
F
202
S3
S3
S4
S4
G
9
S3
S4
S4
S4
H
54
S4
S4
S4
S4
Table 6.3: Applicants’ time-line actions assigned to segments
We do not want to be too quick to ascribe an alias to the behaviours, as we recognise
that there are several possible interpretations; nevertheless, we have used the ‘Potential
Alias’ column in Table 6.4 to indicate some initial thoughts.
Key Findings
The following Figures 6.2–6.6 show box and whisper plots for each of
the ﬁve factors, with the y-axis of each ﬁgure displaying the range for that particular fea-
ture. For example, Figure 6.2 displays the Extraversion feature, and the y-axis displays
these values accordingly. The x-axis is comprised of the various classes from Figure 6.2,
combined with the status of the application (1. Accepted, 2. Rejected, 3. Reserved, 4.
Ineligible). Therefore, A1 are the Class A applicants who were Accepted, distinguished
from A2, who were the same class (i.e. same activity based on timeline/milestones), but
who were Rejected.
Mahalanobis Distance
Checking the Mahalanobis distance, we found that 102 re-
cords exceed the critical values, so we have removed these records since it is more than
2% of the total number.
6.2.4
Extracting LIWC Data Features
While the compound features of the ﬁve factors are an interesting perspective, we also
needed to check the raw data underneath this, in the form of the psycholinguistic features
LIWC and MRC. For this investigation we chose multiple regression.
We extracted the LIWC row data features (87 features) from the motivation letters
and analysed the input dataset against the ‘status’ of the application. The method used
72


## Page 85


Class
Description
Potential Alias
A
Register early, and take some time
to upload documents, but submit
with plenty of time before deadline
EverythingEarly
B
Register
reasonably
early,
but
then upload documents and sub-
mit straight after with plenty of
time before deadline, making no
amendments
QuiteEarlyAndQuick
C
Similar to Class B, but submitting
more slowly
Cautious
D
Registers reasonably early, and then
takes time to upload, and only sub-
mits at the last days
VeryCautious
E
Latecomer to registration, but then
uploads and submits quickly there-
after
Cautious
F
Latecomer to registration, but then
uploads and submits slowly
Cautious
G
Latecomer
to
registration,
but
delays uploading and submission to
last days
Cautious
H
Does everything at the last days,
from registration to submission
EverythingLastMinute
Table 6.4: Description of each class
was multiple regression, the dependent variable being ‘status’ and the independent vari-
ables are the LIWC features. We proceeded as follows:
• Our ﬁrst assumption is multicollinearity, which refers to the relationship when
two independents variables are highly correlated;
• Removing the above features, carry out regression;
• Detecting outliners using Mahalanobis distance, and since we have 60 features
remaining after the multicollinearity elimination, our critical value is: 99.607 (see
Table 6.6);
73


## Page 86


Figure 6.2: Extraversion. All features are hard to distinguish between, excepting that
B2 is signiﬁcantly smaller than B3 and B4
Figure 6.3: Emotional Stability. No real features larger or smaller, although the range
on all of the E features seems much greater than the other features
• Screening for outliners, since multiple regression is very sensitive regarding out-
liners;
• Making sure that we have linear relationship between the independent variables
and the outcome.
Key Findings
We extracted the LIWC row data features (87 features) from the motiv-
ation letters and analysed the input dataset against the ﬁnal selection of the application.
The method used was multiple regression, the dependent variable being ‘status’ and the
74


## Page 87


Figure 6.4: Agreeableness. D4 is signiﬁcantly smaller than D1, D2, and D3. G2 appears
signiﬁcantly less conscientious than G3
Figure 6.5: Conscientiousness. G2 appears signiﬁcantly less conscientious than G3. To
a lesser degree D4 is smaller than D1, D2, and D3
independent variables are the LIWC features (see Table 6.6).
The ﬁrst result set shows the correlation between a dependent variable (status) and
independents variables (LIWC features). In our ﬁrst assumption multicollinearity, we
75


## Page 88


Figure 6.6: Openness to Experience. As with Emotional Stability, there are no excep-
tional features, although the range on all of the E features seems much greater than the
other features. The Class E were the applicants that were relative late comers to registra-
tion, but who then uploaded and submitted quickly thereafter. Openness to Experience
would seem to have very little relationship with this class of applicant
use an R-value of 0.7 or higher to say two predictable values have multicollinearity.
Based on Table 6.6, if the tolerance is smaller than 0.1 then we have the probability of
multicollinearity, while VIF is the inverse of the tolerance, and so in the case of VIF
greater than 10 then we have a case of multicollinearity. In this way, we found that the
below LIWC features are related through multicollinearity.
6.2.5
Discussion
There seems to be a strong relationship between the Five Factor feature Openness to Ex-
perience with a strong correlation with the Accepted group. The exploration of timeline
behaviour is dependent on our representation used for interactions, and the classes de-
rived. The same feature Openness to Experience has no group/class combinations that
are signiﬁcantly different than others. The outcome suggests to ignore the Final selec-
76


## Page 89


Figure 6.7: Normal P-P Plot
Figure 6.8: Scatterplot
tion as a feature in any further analysis as it only correlates with one personality trait
and also, has different other parameter affecting it.
6.3
Mapping User Behaviour to System Stages
6.3.1
Introduction
Previous experiment encourage to progress forward in more investigation specially in
relationship between user’s personality and different stages or events in the system.
In this experiment the data collected from the main dataset and consist of 322 record.
The experiment objective is to explore the relationship between personality, stages, and
sentiment of the users.
The typical approaches investigate extracting the personality traits and emotion from
77


## Page 90


Model
Collinearity Statistics
Tolerance
VIF
1
(Constant)
REFERENCE PEOPLE
0.003
290.011
LEISURE ACTIVITY
0.004
266.827
AFFECTIVE PROCESS
0.006
181.557
PHYSICAL STATES
0.006
181.512
POSITIVE EMOTION
0.006
176.569
SPORTS
0.007
139.147
OTHER
0.007
138.914
BODY STATES
0.008
122.386
YOU
0.009
108.779
SENSORY PROCESS
0.011
89.824
HOME
0.015
67.555
PRONOUN
0.022
46.061
DIC
0.023
43.246
SEEING
0.025
39.69
SELF
0.029
34.103
WE
0.033
30.494
MUSIC
0.037
27.254
TV OR MOVIE
0.041
24.26
FEELING
0.043
23.21
SLEEPING
0.044
22.841
HEARING
0.047
21.488
SEXUALITY
0.049
20.536
OCCUPATION
0.05
19.857
SOCIAL PROCESS
0.07
14.252
COGNITIVE PROCESS
0.075
13.407
NEGATIVE EMOTION
0.089
11.213
Table 6.5: Coefﬁcients of multicollinearity variance inﬂuence factor
text using linguistic analysis [256] with the recent growth of human-computer interac-
tion on daily bases the need to understand how personality and emotions incorporate
in different stages. In the current dataset the web-application involved different stages
before submission of the application form. Therefore, for this analysis the system have
been divided into stages as shown on Table 6.10.
Retrieve user’s timeline in the proposed stages
each user has his own time stamp on
the system, which represents the user’s interactions during the life cycle of the call [242].
78


## Page 91


UID
WC
WPS
UNIQUE
SIXLTR
1003
364
24.2667
41.4835
37.9121
1008
275
22.9167
61.4545
22.5455
1010
197
8.20833
68.0203
37.0558
1014
577
19.2333
53.7262
28.9428
1016
348
19.3333
55.4598
29.5977
1023
538
16.8125
53.9033
26.9517
1033
517
23.5
54.352
35.9768
1035
165
23.5714
62.4242
27.8788
1039
388
16.1667
56.1856
31.701
1040
491
14.8788
58.2485
33.4012
1049
462
25.6667
55.8442
33.1169
1058
293
32.5556
55.2901
26.9625
1069
436
29.0667
52.5229
26.1468
1073
162
27
61.1111
25.9259
1078
334
17.5789
55.988
34.4311
Table 6.6: Sample of the dataset: 87 LIWC features and more than 1000 candidates;
UID represent the user and rest of the columns represent the LIWC features
Sum of Sq.
df
Mean Sq.
F
Sig.
Regress.
41.602
56
0.743
1.172
0.187b
Residual
563.465
889
0.634
-
-
Total
605.067
945
-
-
-
Table 6.7: Evaluation of the model and ability to predicate the status values
Model Summary
Model
R
R Square
Adjusted R Square
Std. Error of the Estimate
1
.262a
0.069
0.01
0.796
Table 6.8: Model summary after removing the multicollinearity features and above crit-
ical value of Mahalanobis distance
In this study, user’s timeline will be segmented with respect to the proposed stages as
shows on Table 6.10. To give an illustration of such classiﬁcation. Figure 6.9, shows
a timeline of one of the users on the system and how the proposed stages are cross
overlapped. Code A used to pick the text associated with the user at each stage and
saved it with the StageID based on Start-End date explained on Table 6.10.
An algorithm responsible to detect the stage of each user by identifying the dates
of each stage from the system interaction timestamps. Start and end of each stage have
been identiﬁed as per the Figure 6.9 the algorithm automatically detect the start/end of
79


## Page 92


Model
Stnd. Coeff.
Sig.
1
(Constant)
0.000
NEGATIONS
0.109
0.004
QMARK
0.107
0.199
SPACE
0.098
0.044
ABBREVIATIONS
0.076
0.038
CAUSATION
0.073
0.051
DASH
0.068
0.093
UNIQUE
0.068
0.247
INHIBITION
0.062
0.072
JOB OR WORK
0.051
0.188
DISCREPANCY
0.045
0.289
SCHOOL
0.044
0.279
Table 6.9: Top effective coefﬁcient LIWC features over the model
StageID
Phase Name
Description
1
Start Stage
From start of the call till the ﬁrst engagement from the user with the
system
2
Uploading Stage
During the uploading process of the documents.
3
Submission Stage
The period after the uploading and submission
4
After Submission Stage
Stage after submission and before end of the call
5
Extension Stage
Stage where an extension have been granted for users to continue ap-
plying (After deadline - Extension date)
Table 6.10: System Stages
each stage and identify which stage and extract all text associated with the user. The
Table 6.11 shows a sample of the data after preparation, notice for each user there are
different text associated with different stageID, which associated with Table 6.10.
Applying sentiment analysis allowed us to label each text as positive or negative with
respect to each stages, with the expected output for each text being positive, negative.
The API Text-Processing used 1 where it expect the text input and the output consist of
3 attributes (Pos,Neg and Natural) as shown in Table 6.12, the ﬁrst column StageTextID
represent a record on the Table 6.11 to match the text, stageID with the output of this
text. Negative, Neutral and Positive represent the probability of each label. negative
and positive adding up to 1, however, neutral is standalone. If neutral is greater than
0.5 then the label marked as neutral. For this experiment this rule will be ignored the
study focus in the probability of positive and negative only. Therefore, the neutral label
replaced with other higher probability. For example in the Table 6.12 in the case of
record number 12 of StageTextID the positive = 0.492328951 , Neutral = 0.670260584
1http://www.text-processing.com
80


## Page 93


Figure 6.9: Timestamp of two users (Users 199 and 2698) with respect to proposed
stages
and negative = 0.507671049 while it is labelled neutral the negative probability is higher
than positive therefore, the label changed to neg
The text processing uses the NLTK Naive Bayes Classiﬁcation in the methodology
with a dictionary of movies review labelled as following a movie reviews corpus has
1000 positive ﬁles and 1000 negative ﬁles. 75% of the dataset use as the training set,
and the rest as the test set. Training and Testing the Naive Bayes Classiﬁer. The outcome
of the modelling is 73% accuracy.
There are two sources for extracting the personality traits motivation letter and Big
Five Questionnaire as part of the user’s experience the program coordinator encourage
users to ﬁll in the Big Five Questionnaire. Therefore, before an attempt to extract the
personality traits from the motivation letter 2, ﬁrst checking the if the User ﬁlled out the
2Personal statement document submitted as part of the application process
81


## Page 94


user id
stageid
text
3254
1
I have 3 questions 1-for the required selected documents there are
two requirements MASTER TRANSCRIPT and TRANSCRIPTS What is
meant by the Transcripts because there is a slot already to upload the
master certiﬁcate . 2- you say it is needed to I have 3 questions
3254
2
i have only two documents to upload the site sometimes open but when
it does i cant reach the upload page my username amrnawar what about
me i only have two documents left because the research proposal needed
to be revised by college staff and they just did revising yesterday i need
to upload it and submit please admin please thanks alot thats very kind
of you thak you very very much
3254
5
admin thankkkkkkkkkkkkkks to you i think i uploaded necessary docu-
ments but i cant submit now please help me to submit user amrnawar i
have only two documents to upload the site sometimes open but when it
does i cant reach the upload page my username amrnawar what about
me i only have two documents left because the research proposal needed
to be revised by college staff and they just did revising yesterday i need
to upload it and submit please admin please thanks alot thats very kind
of you please urgently help istarted uploading everything only 2 pages
of research proposal left when site crashed all my work will go in vain
2878
5
username Luis Olano tried to apply for Mass Communication program
Ain Shams University several times but it s impossible to upload any
document please tell me if i can send by email so we spent two weeks
fully dedicated to obtaining every document needed to apply for this
scholarship and in the end all the effort made was not worth at all it is
very sad
2766
5
My username is mo3taz elsawy i already uploaded my papers and only
want to submit my application it still isn t working for me up tell now
i can log in but i can not do any thing after that the site is very slow
mo3taz elsawy is my user name
6223
5
Thaaaaaaaaaaaaaaaaaaaaaanks Reassure for my Documents
2937
5
my username is Hatem Hassan plz just one document to complete my
submission
3094
2
whenever i upload any ﬁle with it’s required extension (JPG )website
says message appears BAD REQUEST Your browser sent a request that
this server could not understand
Table 6.11: Sample of Stages Text collected per user [242]
82


## Page 95


StageTextID
Negative
Neutral
Positive
Label
1
0.518402657
0.366022022
0.481597343
neg
2
0.733416831
0.167587171
0.266583169
neg
9
0.606781287
0.165370162
0.393218713
neg
10
0.823030133
0.176314817
0.176969867
neg
11
0.780114198
0.303985047
0.219885802
neg
12
0.803123608
0.229718524
0.196876392
neg
13
0.810792691
0.168979215
0.189207309
neg
14
0.740935943
0.235929961
0.259064057
neg
15
0.762828024
0.768115205
0.237171976
neg
16
0.762828024
0.768115205
0.237171976
neutral
17
0.38153628
0.420256869
0.61846372
pos
18
0.332127272
0.3738164
0.667872728
pos
19
0.492328951
0.670260584
0.507671049
neutral
20
0.715223337
0.310831638
0.284776663
neg
21
0.549909425
0.661750668
0.450090575
neutral
Table 6.12: Sample of the sentiment analysis output
Big Five Questionnaire if not then move to the personality trait extraction methodology
stated on Section 5.5.
6.3.2
Binomial Logistic Regression (Logistic Regression)
The dataset consists of the Big Five traits, stages of the system and the sentiment posit-
ive/negative output. Since the “Big Five” traits are continues values and sentiment out-
put are either positive or negative (dichotomous dependent variable ), and the stageID is
a ordinal variables. Therefore, the mix of data types suggests to use Binomial logistic
regression, to calculate the probability sentiment behaviour of a user based on person-
ality trait and stage. To observe the possibility of modelling the user’s behaviour based
on speciﬁc stages.
For a logistic regression to be accurate, the “big ﬁve” traits values need to be lin-
early related to the logit transformation of the Sentiment Output. This hypothesis can
be examined using the Box-Tidwell (1962) method. The Box-Tidwell is a method to
examine this assumption [34].To achieve this, we follow the below steps:
• Using IBM SPSS, the transformation of all “big ﬁve” traits to its natural logs.
• Create interactive term for each of all “big ﬁve” traits to its original values and
respective natural logs.
83


## Page 96


• It is well-known practice to use Bonferroni correction based on all terms in the
model when evaluating this linearity hypothesis [34, 318].
B
S.E.
Wald
df
Sig.
Exp(B)
stageid
21.862
4
0
stageid(1)
-1.575
0.435
13.084
1
0
0.207
stageid(2)
-0.472
0.458
1.065
1
0.302
0.624
stageid(3)
0.031
0.705
0.002
1
0.965
1.032
stageid(4)
-1.554
0.459
11.481
1
0.001
0.211
Openness
-0.017
1.306
0
1
0.989
0.983
Conscientiousness
-0.296
1.296
0.052
1
0.819
0.744
Extraversion
-1.305
0.835
2.443
1
0.118
0.271
Agreeableness
2.031
0.798
6.475
1
0.011
7.624
Neuroticism
-0.272
0.929
0.086
1
0.77
0.762
Log OP by Openness
3.508
3.293
1.135
1
0.287
33.365
Conscientiousness by Log Cons
0.843
3.154
0.071
1
0.789
2.324
Extraversion by Log ext
0.141
2.595
0.003
1
0.957
1.151
Agreeableness by Log Agree
-2.017
2.288
0.778
1
0.378
0.133
Log neuro by Neuroticism
1.965
2.538
0.599
1
0.439
7.133
Constant
3.505
2.205
2.527
1
0.112
33.297
Table 6.13: Logistic Regression – variables in the equation table
According to the Logistic Regression result, Table 6.13 Linearity of the “big ﬁve”
traits concerning the logit transformation of the “Sentiment Analysis” was evaluated via
the Box-Tidwell method [34]. A Bonferroni correction was applied using all twelve
(Big ﬁve, Log Big Five, StageID and Sentiment Output) terms in the model occurring
in a valid statistical signiﬁcance, since p < .00416 [318]. Based on this evaluation, all
the “big ﬁve” traits were observed to be linearly correlated to the logit of the sentiment
output.
6.3.3
Key Findings and Discussion
There was one studentised residual with a value of −5.817511standarddeviations, whichretainedinthein
= 31.853, p < .0005. The model explained 9% (Nagelkerke R2) of the change in sen-
timent raised in different stages and accurately classiﬁed 80.2% of cases as shown in
Table 6.14. Sensitivity was 99.2%, speciﬁcity was 7.4%, the positive predictive value
was 19.5%, and the negative predictive value was 80.4%, of the nine predictor vari-
ables, there were statistically signiﬁcant: Stages (1,4), Extraversion, Agreeableness,
84


## Page 97


Conscientiousness Table 6.13. It is notable that there is a big gap between the positive
predictive value and the negative value.
Observed
Predicted
Sentiment
Percentage Correct
Pos
Neg
sentiment label
Pos
5
63
7.4
Neg
2
259
99.2
Overall Percentage
80.2
Table 6.14: Binomial Logistic regression Classiﬁcation
6.4
Relationship Between Personality Traits and Emo-
tion
6.4.1
Introduction
The increase usage of online platform which involve the daily bases life has challenge
us to develop a model for the type of users using these platform, by understanding the
personality and emotion raised while using the system, that would lead to signiﬁcation
improvement in the architecture of the complex computer system not only the design, it
is delivering the information to the users.
Research into personality traits have been challenge for many researchers in dif-
ferent ﬁelds , for past 100 years interest in developing technology that has the ability
to recognise peoples personality and emotions [321] has grown rapidly . Recently re-
searchers have started to investigate the relation between the social on-line behaviour
and the real life behaviour. This research interested in capturing the emotions used in
the test, and according to the literature as discussed in Section 2.6, different approach
has been introduced to capture the emotions, one of them is using IBM Watson (see
Section 4.2.3) and other is using TEIQue assessment [264], therefore, it was vital to
investigate the association between Big Five Personality Traits and the EI traits using
TEIQue Assessment.
This experiment focus on investigating the relation between the personality traits
(Big Five) and the Emotional Intelligent behaviour (TEIQue), for the Facebook dataset,
in order to decide either to use TEIQue or Lexicon Basic Emotion approach.
85


## Page 98


6.4.2
Personality Traits and Temporal Behaviour
The dataset using in this experiment is retrieved from the web-based scholarship system
(see Section 5.3), 72 participants completed a Big Five Personality Traits personality
questionnaire and TEIQue assessment questionnaire after submitting their application,
as part of the user experience improvement suggested by Scholarship Administrator
team.
The type variables in the dataset suggested a use of Pearson’s correlation o investig-
ate the association between the Big Five Personality traits and the EI traits.
Pearson Correlations
Tests of Normality
Kolmogorov-Smirnova
Shapiro-Wilk
Statistic
df
Sig.
Statistic
df
Sig.
Extraversion
0.088
28
.200*
0.98
28
0.857
Agreeableness
0.135
28
.200*
0.938
28
0.096
Conscientiousness
0.148
28
0.122
0.948
28
0.178
Neuroticism
0.176
28
0.026
0.93
28
0.06
Openness
0.131
28
.200*
0.966
28
0.477
Wellbeing
0.192
28
0.01
0.81
28
0
Selfcontrol
0.15
28
0.106
0.942
28
0.121
Emotionality
0.083
28
.200*
0.986
28
0.965
Sociability
0.118
28
.200*
0.932
28
0.068
Table 6.15: Shapiro-Wilk’s normality check for Big Five traits and EI traits.
To assess the statistical signiﬁcance of Pearson’s correlation coefﬁcient, a normality
assumption need to be veriﬁed ﬁrst and test the level of normality for all variables in-
volved before proceeding to Pearson Correlation. Table 6.15 shows that none of the vari-
ables were normally distributed, as assessed by Shapiro-Wilk’s test (p < 0.05), There-
fore, Spearman’s rank-order correlation suggested to be used instead as it can be used
to measure the strength and direction of the association between either two continuous
variables. Furthermore, it is still possible to run Pearson’s Correlation Coefﬁcient as the
test is somewhat robust to deviations from normality.
According to Table 6.16, there was a moderate positive correlation between Well
being, Agreeableness, Conscientiousness and Openness, r = .452, r=0.465 and r=0.393
and negative moderate correlation, between Neuroticism and Well being, Self control
and Sociability, r=-.550, r=-.506 and r=-.492.
86


## Page 99


Correlations
Wellbeing
Selfcontrol
Emotionality
Sociability
Extraversion
Pearson Correlation
.255
.026
.222
.350
Sig. (2-tailed)
.190
.895
.256
.067
Agreeableness
Pearson Correlation
.452*
.219
.297
.175
Sig. (2-tailed)
.016
.263
.125
.373
Conscientiousness
Pearson Correlation
.465*
.076
.173
.143
Sig. (2-tailed)
.013
.702
.379
.468
Neuroticism
Pearson Correlation
-.550**
-.506**
-.235
-.492**
Sig. (2-tailed)
.002
.006
.229
.008
Openness
Pearson Correlation
.393*
.296
.263
.323
Sig. (2-tailed)
.039
.127
.177
.094
Table 6.16: Pearson correlation coefﬁcient, Big Five and EI traits
Correlation
Wellbeing
Selfcontrol
Emotionality
Sociability
Extraversion
Correlation Coefﬁcient
.158
-.023
.278
.288
Sig. (2-tailed)
.423
.907
.153
.137
Agreeableness
Correlation Coefﬁcient
.413*
.193
.255
.066
Sig. (2-tailed)
.029
.324
.190
.737
Conscientiousness
Correlation Coefﬁcient
.514**
-.035
.178
.114
Sig. (2-tailed)
.005
.859
.364
.563
Neuroticism
Correlation Coefﬁcient
-.383*
-.484**
-.212
-.357
Sig. (2-tailed)
.044
.009
.280
.062
Openness
Correlation Coefﬁcient
.329
.214
.260
.236
Sig. (2-tailed)
.087
.274
.182
.227
Table 6.17: Spearman’s Rank-Order correlation output
87


## Page 100


Spearman’s Rank-Order Correlation
As the normality check on Table 6.15 reported that none of the variables were nor-
mally disrupted and to verify the output of the Pearson Correlation Coefﬁcient reported
on Table 6.16. Spearman’s rank-order correlation has been suggested to conﬁrm the
association. Table 6.17, shows that there was a positive correlation between Conscien-
tiousness and Well being, rs = .514, and Negative correlation between Neuroticism and
self control. rs=-.484.
6.4.3
Association between Personality Traits and Six Basic Emo-
tions
This experiment is a replication of the previous experiment to investigate the association
between Big Personality Traits and basic emotions (as initially presented in Section 2.6).
The dataset used in this experiment is consisted of 477 interaction extracted from schol-
arship system, through different data source as explaind previously in Section 5.3. IBM
Watson (as presented in Section 4.2.3) used as an API to extract Big Personality Traits
and Basic Emotions, based on the lexicon approach.
Pearson Correlation
Figure 6.10, shows the assumption of normality for Big Five Traits and Basic Emotions
was satisﬁed for most of the variables as assessed by visual inspection of Normal Q-Q
Plots.
Pearson’s Correlations
Openness
Conscientiousness
Extraversion
Agreeableness
Neuroticism
Anger
Pearson Correlation
.045
.014
-.002
-.068
.012
Sig. (2-tailed)
.330
.759
.963
.140
.799
Disgust
Pearson Correlation
.071
.041
.006
-.086
-.074
Sig. (2-tailed)
.122
.369
.895
.062
.107
Fear
Pearson Correlation
.015
-.092*
.003
-.021
-.248**
Sig. (2-tailed)
.752
.044
.944
.650
.000
Joy
Pearson Correlation
.083
.126**
-.016
-.046
.106*
Sig. (2-tailed)
.069
.006
.731
.311
.021
Sadness
Pearson Correlation
-.123**
.025
-.053
.069
.068
Sig. (2-tailed)
.007
.590
.244
.134
.136
Table 6.18: Pearson correlation coefﬁcient, Big Five and Basic emotions
Table 6.18 shows a Pearson’s correlation coefﬁcient was run to assess the relation-
ship between Big Five traits and basic emotions. Preliminary analyses showed the re-
lationship to be linear with both variables normally distributed, as assessed by visual
inspection of Normal Q-Q Plots, and there were no outliers. There was a moderate
88


## Page 101


Figure 6.10: Normal Q-Q plot for Big Five traits and basic emotion
negative correlation between fear and Conscientiousness,Neuroticism, r(447) = −.092,
p < .05, r(447) = −.248, p < .05 and moderate positive correlation between joy and
Conscientiousness, Neuroticism, r(447) = −.126, p < .05, r(447) = −.106, p < .05.
6.4.4
Discussion
The ﬁndings from experiment (see Section 6.4.2) is relevant to, and can be interpreted
from the perspective of, the emerging literature on the general factor of personality [109,
149, 223]. The output agrees with the the reported ﬁndings in study conducted by Mc-
Crae [205], there are a moderate correlation between Neuroticism, self control and well
being. Well being has a moderate correlation to agreeableness and conscientiousness.
Beyond the theoretical value of these data, the results demonstrate the practical equi-
valence of TEIQue and in relation to their associations with Big Five personality traits.
However, according to the literature as previously discussed in Section 4.2.3, emotions
can be captured using linguistic analysis, therefore, further experiments presented in
Section 6.4.3 were conducted to explore the association between Big Five traits and
89


## Page 102


basic emotions. The ﬁndings suggested a moderate correlations between the traits as
explained previously. Furthermore, as both theories interested in capturing the emo-
tions it was decided to move forward with the basic emotions (lexion approach) as it
can capture the emotions from the text which ﬁts the direction of this study.
6.5
Investigating Behavioural and Emotional Change
6.5.1
Introduction
The experiments presented in Section 6.3 suggest an 80.2% accuracy of the proposed
model, which proves the assumption of strong correlation between personality traits,
sentiment and the stages of the application form. Therefore, this experiment has been
introduced as an extension to the previous model to extend the sentiment instead of
being negative and positive to include the emotion extracted using IBM Watson Tone
Analyzer stated on Section 5.6. This experiment will focus on incorporating the emo-
tion tone Anger, Fear, Disgust, Joy and Sadness. Although, according to the literature
discussed in Section 4.2.3, it is essential to investigate the fundamental emotions and it
is an association with Big Five Personality trait.
The dataset is prepared from the previous experiment in Section 6.3, however, an
extension preparation is required to cover the new requirements for this experiment.
In this respect, the data in Table 6.11 is used again to extract the emotion based on
the stages reported in the Table 6.10. Table 6.19 shows sample of the output from the
IBM Watson Tone Analyzer. The column StagesTextID associated with the text from
Table 6.11, and the attributes Anger, Disgust , Fear, Joy and Sadness all adding to 1.
6.5.2
Ordinal Regression Analysis
The Ordinal regression analysis suggested to be used on this dataset, as noted earlier in
Section 6.3, the dataset consist of different types of variables (Big Five and Emotions)
considered as continues variables however, the stages is a grouped variable (Ordinal
Variable). Therefore, the ordinal regression analysis suggested for this experiment.
A critical part of the process involves veriﬁcation phase to make sure that the data
being analyse can actually be analysed using this test. The ordinal logistic regression has
four assumptions that you have to consider. (a) you have an ordinal dependent variable,
(b) dataset consist of one or more independent variables that are continuous. (c) There
should be no multicollinearity (d) There should be a proportional odds. The assumption
(a) and (b) is valid in the dataset, as shown previously the dependent variable StageID
– Table 6.10 is type of ordinal values scale from 1 to 5. The (b) assumption is valid
as The Big Five and emotions values is type of continuous as shown in Tables 6.19 and
6.18.
90


## Page 103


StagesTextID
Anger
Disgust
Fear
Joy
Sadness
1
0.236374
0.148785
0.167954
0.116915
0.517816
2
0.164751
0.015199
0.263669
0.01941
0.615725
3
0.099684
0.005159
0.224768
0.003826
0.740602
4
0.322635
0.007574
0.032424
0.000671
0.742377
5
0.159617
0.029623
0.130249
0.004624
0.765329
6
0.176493
0.02529
0.196468
0.101357
0.493553
7
0.237498
0.066133
0.136312
0.185933
0.331277
8
0.36853
0.119263
0.175762
0.000132
0.508752
9
0.103784
0.014536
0.205593
0.004806
0.748736
10
0.109112
0.002726
0.338946
0.002019
0.638848
11
0.249994
0.047278
0.137731
0.002621
0.684495
12
0.654401
0.012053
0.143045
0.00026
0.333567
13
0.127089
0.047328
0.196604
0.003453
0.723312
14
0.215104
0.011095
0.106291
0.015954
0.729163
15
0.23544
0.004584
0.092963
0.06229
0.624768
16
0.23544
0.004584
0.092963
0.06229
0.624768
Table 6.19: Sample of the emotion extraction output
Testing the assumption of multicollinearity
Discovering whether there is multicol-
linearity is an essential step in ordinal logistic regression. To test the Multicollinearity,
we need to check if two or multiple variables (independent) are correlacted with each
other. If this occurs will lead to a lack of understanding which independent variable
explains the dependent, and this will give an inaccurate association for the model.
Model
Tolerance
VIF
Anger
.674
1.484
Disgust
.927
1.079
Fear
.662
1.510
Joy
.273
3.661
Sadness
.385
2.599
Openness
.782
1.279
Conscientiousness
.836
1.197
Extraversion
.715
1.398
Agreeableness
.618
1.619
Neuroticism
.846
1.182
Table 6.20: Multicollinearity output - Coefﬁcients (Dependent Variable: stageid)
91


## Page 104


In examining the Tolerance values and variance inﬂation factor (VIF) values, ac-
cording to Table 6.20 all the Tolerance > 0.1 (the lowest is 0.273), and VIF values are
much less than 10. Therefore, it is fairly certain that there is no issue with collinearity
in this dataset. The ﬁndings conﬁrm the validity of the assumption (c).
The assumption of proportional odds
Progressing to assumption (d), the assump-
tion of proportional odds is essential to the kind of ordinal logistic regression. Each
independent variable has the same inﬂuence at each developing separation of the or-
dinal dependent variable. This assumption can be examined using two approaches: (a)
with a full likelihood ratio test associating the ﬁt of the proportional odds model to a
model with different location parameters, and (b) by running separate binomial logistic
regressions on cumulative dichotomous dependent variables.
• Full likelihood ratio test This test works by measuring the model ﬁt within two
separate models. That two models that we are interested in for this test are the
proportional odds model - null hypothesis row- and the proportional odds con-
straint/assumption (the “General” row). That where the slope coefﬁcients are
provided to be different in each logit value.
The assumption of proportional odds will be valid only if the difference in model
ﬁt is small and not statistically signiﬁcant p > 0.05. On the other hand, the as-
sumption of is invalid p < 0.05, which means the model ﬁt is substantial and
statistically signiﬁcant.
According to Table 6.21, p = 0.001, which is less than 0.05. Therefore, the as-
sumption of proportional odds is violated. By violating this assumption, therefore
each independent variable cannot be treat as having the same impact for each
cumulative logit.
Model
-2 Log Likelihood
Chi-Square
df
Sig.
Null Hypothesis
1226.624
General
1167.651
58.974
30
.001
Table 6.21: Full likelihood ratio test - Test of Parallel Lines
• Separate binomial logistic regressions
The full likelihood ratio test ﬂagged violations of the assumption of proportional
odds that do not exist. Therefore, a wider examination of the assumption of pro-
portional odds needed by running separate binomial logistic regressions on the
dichotomous dependent variables. According to Hardy (1993) [140], many re-
gression procedures, such as linear regression or logistic regression, do not accept
92


## Page 105


B (Parameter estimates)
Exp(B) (Odds Ratio, OR)
Independent variable
Stage1
Stage2
Stage3
Stage4
Stage 1
Stage 2
Stage 3
Stage 4
Anger
2.246
.775
.620
-.316
9.455
2.171
1.859
.729
Disgust
7.918
6.394
8.632
8.630
2745.452
598.318
5606.564
5596.071
Fear
-1.559
-.517
-.241
.317
.210
.596
.786
1.373
Joy
-.770
-.130
.458
1.039
.463
.878
1.581
2.825
Sadness
-2.869
-1.689
-1.147
-1.383
.057
.185
.318
.251
Openness
-.257
.121
.204
.312
.773
1.129
1.227
1.366
Conscientiousness
-.373
-.005
-.595
-.810
.689
.995
.551
.445
Extraversion
-.531
-.179
-.360
-.321
.588
.836
.698
.726
Agreeableness
.070
.035
.166
.320
1.072
1.036
1.181
1.377
Neuroticism
-.391
-.220
-.183
-.687
.676
.802
.833
.503
Constant
.491
.601
.702
1.544
1.634
1.824
2.018
4.684
Table 6.22: Parameter estimates and odd ratios for the dichotomised cumulative cat-
egories of the dependent variable
categorical variables directly into the model: they have to recoded ﬁrst. This re-
cording can take many different forms, with the most popular called indicator
coding [250]. This process will perform a separation method which will divide
the dependent dichotomous variable into separate parameters that number one less
than the number of classes of the dichotomous variable. Creating a new variables
Stage1, Stage 2, Stage 3 and Stage 4.
Table 6.22 presents the information extracted from the Variables in the Equation
tables to allow more straightforward comparison. Essentially, the assumption of
proportional odds states that the estimated parameters, except the intercept (i.e.,
just the slope coefﬁcients), are equal for each binomial logistic regression run on
each dichotomised cumulative category; only the intercept - called the threshold in
ordinal regression - is free to vary. If this assumption is tenable, the coefﬁcients
above should be similar for Stage1, Stage 2, Stage 3 and Stage 4. However, it
usually makes more sense to look at the differences or similarities between the
odds ratios.
Openness,Extraversion and Agreeableness in the Table 6.22, odd ratios for four
different binomial logistic regression are similar (i.e, 1.072, 1.036, 1.181 and
1.377). It would appear that, for this variable, the assumption of proportional odds
appears tenable. However, consider anger, disgust, fear, joy, sadness, conscien-
tiousness, extraversion, agreeableness and neuroticism (i.e, 2745.452, 598.318
5606.564 and 5596.071). The assumption of similar odds for this variables might
not be tenable. Therefore, treating those variable in the ﬁnal ordinal regression
with more caution.
93


## Page 106


Chi-Square
df
Sig.
Pearson
1299.332
1326
.694
Deviance
1098.406
1326
1.000
Table 6.23: Goodness-of-Fit
Source
Wald Chi-Square
df
Sig.
Anger
1.341
1
.247
Disgust
12.046
1
.001
Fear
.102
1
.749
Joy
.127
1
.721
Sadness
6.986
1
.008
Openness
.054
1
.816
Conscientiousness
1.556
1
.212
Extraversion
.612
1
.434
Agreeableness
.203
1
.652
Neuroticism
1.214
1
.271
Table 6.24: Tests of Model Effects
Ordinal Regression Key Findings
. A cumulative odds ordinal logistic regression
with partial proportional odds was run to understand the impact of Big Five traits
and emotions on different stages of the system reported in Table 6.10. The propor-
tional odds were violated, as assessed by a full likelihood ratio test comparing the ﬁt-
ted model to a model with varying location parameters, x2(40) = 58.974, p = .001.
The deviance goodness-of-ﬁt test indicated that the model was a good ﬁt to the ob-
served data, x2(1326) = 1098.406136, p = 1.0 as shown table 6.23, but most cells
were sparse with zero frequencies in 74.8% of cells. However, the ﬁnal model statist-
ically signiﬁcantly predicted the dependent variable over and above the intercept-only
model, x2(10) = 42.840503, p < .001. The disgust and sadness parameters had a stat-
istically signiﬁcant effect on the prediction of stageID, x2(1) = 12.046, p = .001 and
x2(1) = 6.086, p = .008 as shown in Table 6.24. Table 6.25 shows an increase in dis-
gust is associated with an increase in the odds of being in later stages (4 or 5), with
an odds ratio of .041 (95% CI, 5.04 to .034), Wald x2(1) = 12.046, p < .005. Fur-
thermore, an increase in Sadness was associated with an increase in the odds of being
in later stages (4 or 5) with an odds ratio of 5.356 (95% CI, 1.543 to 18.589), Wald
x2(1) = 6.986, p < .008.
94


## Page 107


Parameter
B
Std. Error
95% Wald Conﬁdence Interval
Hypothesis Test
Exp(B)
95% Wald Conﬁdence Interval for Exp(B)
Threshold
Lower
Upper
Wald Chi-Square
df
Sig.
Lower
Upper
Stage=1
-.489
.6809
-1.823
.846
.515
1
.473
.614
.162
2.330
Stage=2
.707
.6810
-.627
2.042
1.079
1
.299
2.028
.534
7.706
Stage=3
1.016
.6818
-.321
2.352
2.220
1
.136
2.761
.726
10.507
Stage=4
1.536
.6837
.196
2.876
5.048
1
.025
4.647
1.217
17.747
Anger
-1.018
.8790
-2.741
.705
1.341
1
.247
.361
.065
2.024
Disgust
-7.796
2.2462
-12.198
-3.393
12.046
1
.001
.041
5.040E-06
.034
Fear
.312
.9753
-1.600
2.223
.102
1
.749
1.366
.202
9.238
Joy
-.274
.7679
-1.779
1.231
.127
1
.721
.760
.169
3.425
Sadness
1.678
.6349
.434
2.923
6.986
1
.008
5.356
1.543
18.589
Openness
-.108
.4639
-1.017
.802
.054
1
.816
.898
.362
2.229
Conscientiousness
.470
.3769
-.269
1.209
1.556
1
.212
1.600
.765
3.349
Extraversion
.314
.4013
-.473
1.101
.612
1
.434
1.369
.623
3.006
Agreeableness
-.175
.3895
-.939
.588
.203
1
.652
.839
.391
1.800
Neuroticism
.339
.3076
-.264
.942
1.214
1
.271
1.403
.768
2.565
Table 6.25: Parameter estimates using the GENLIN procedure
6.5.3
Multinomial Logistics Regression
The ordinal regression analysis from the experiment in Section 6.5.2 reported disgust,
sadness and conscientiousness as statistically signiﬁcation with StageID. However, the
proportional odd assumption treated with very caution and it suggested partial propor-
tional odd relationship with some parameters. Therefore, it is suggested to use multino-
mial logistics regression analysis to predict a nominal dependent variable with more than
one value. Multinomial Regression required the data to pass six assumption 1-dependent
variable should be measured at the nominal level, 2- One or more independent variables
that are continuous, 3-Independence of observations and the dependent variable should
have mutually exclusive and exhaustive categories – according to Table 6.10 the de-
pendent variable stageID are mutually exclusive and exhaustive (i.e. each record fall
into one and only one category) , 4-There should be no multicollinearity, 5-linear rela-
tionship between any continuous independent variables and the logit transformation of
the dependent variable, 6- No outliers, high leverage values or highly inﬂuential points.
From the previous experiment in Section 6.5.2 the data passes assumption 1,2,3,4 and
6.
Assumptions
Assumption number 5, linear relationship between any continuous in-
dependent variables and the logit transformation of the dependent variable (see Sec-
tion 6.2).
logit(StageID) = ln
StageID
1 −StageID
(6.2)
Using linear regressing to investigate the relationship between the Big Five, Emo-
tions and out dependent value (StageID). Table 6.26 shows the output of the linear re-
gression. According to the table, there is a signiﬁcant correlation with Disgust (B=-.158,
p-value=0.001) and Sadness (B=.183, p-value=.011). The assumption number 5 is not
violated and passed since the two independent variable have signiﬁcant statistics correl-
ation with the logit of StageID.
95


## Page 108


Unstandardised Coefﬁcients
Standardised Coefﬁcients
t
Sig.
Correlations
B
Std. Error
Beta
Zero-order
Partial
Part
(Constant)
2.373
.588
4.033
.000
Anger
-.698
.760
-.050
-.918
.359
-.067
-.043
-.041
Disgust
-6.392
1.863
-.158
-3.432
.001
-.173
-.157
-.153
Fear
.294
.842
.019
.349
.727
.005
.016
.016
Joy
-.207
.665
-.026
-.311
.756
-.112
-.014
-.014
Sadness
1.394
.546
.183
2.551
.011
.213
.117
.113
Openness
-.095
.401
-.012
-.238
.812
-.034
-.011
-.011
Conscientiousness
.370
.324
.056
1.144
.253
.051
.053
.051
Extraversion
.272
.345
.041
.788
.431
.009
.036
.035
Agreeableness
-.114
.336
-.019
-.340
.734
.043
-.016
-.015
Neuroticism
.292
.265
.053
1.100
.272
.070
.051
.049
Table 6.26: Linear Regression Coefﬁcients output (dependent variable: Stageid)
All assumption for multinomial regression analysis is validated for the dataset, the
next section will show the output of the multinomial logistics analysis.
Model
Model Fitting Criteria
Likelihood Ratio Tests
-2 Log Likelihood
Chi-Square
df
Sig.
Intercept Only
1269.465
Final
1186.030
83.435
40
.000
Table 6.27: Multinomial regression output - Model Fitting
Analysis Findings
According to Table 6.27, p-value=.000, the model ﬁts the data
signiﬁcantly better than the null model. Table 6.28, variables Disgust, Sadness and
Conscientiousness with p-values .006,0.017 and 0.051 has a signiﬁcant overall effect
on the dependent StageID.
According to Table 6.29 Disgust likely to increase ratio odds while in Stage 1 over
being in Stage 53 with in odds ratio of 194325.6 (95% CI, 156.670380 to 241031239.97),
Wald x2(1) = 11.227, p < .001. Output suggested Sadness more likely to increase with
ratio odds of .040 (95% CI, .005 to .355), Wald x2(1) = 8.358, p < .004, while in Stage
1 decrease over being in Stage 5. Findings reported, odds increase Disgust with odd ra-
tio 179275.939 to be in Stage 3 (95% CI, 9.041 to 3554947303.3), Wald x2(1) = 5.741,
p < .017. For every one-unit increase in the Conscientiousness the ratio odds of being
in Stage 3 decrease by .081 than on Stage 5 (95% CI,0.14 to .460), Wald x2(1) = 8.028,
p < .005. For every one-unit increase in the Neuroticism the ratio odds of being in
Stage 4 increase by .225 than on Stage 5 (95% CI,0.066 to .769), Wald x2(1) = 5.656,
p < .017.
3Reference outcome
96


## Page 109


Effect
Model Fitting Criteria
Likelihood Ratio Tests
-2 Log Likelihood of Reduced Model
Chi-Square
df
Sig.
Intercept
1190.707
4.678
4
.322
Anger
1191.875
5.846
4
.211
Disgust
1200.616
14.587
4
.006
Fear
1188.317
2.287
4
.683
Joy
1189.467
3.438
4
.487
Sadness
1198.063
12.033
4
.017
Openness
1187.017
.987
4
.912
Conscientiousness
1195.475
9.445
4
.051
Extraversion
1187.510
1.481
4
.830
Agreeableness
1186.722
.692
4
.952
Neuroticism
1192.894
6.864
4
.143
Table 6.28: Multinomial Regression - Likelihood Ratio Tests
6.5.4
Key Findings and Discussion
The aim of the experiment to extend the previous model as presented in Section 6.3 to
include the emotion parameters to investigate how a model would ﬁt and if there is any
signiﬁcant statistical correlation between the independent variables (BigFive+emotions)
and the dependent variable (StageID) as shown in table6.10. The Ordinal Regression
suggested a ﬁnal model statistically signiﬁcantly predicted the dependent variable over
and above the intercept-only model, 2(10) = 42.840503, p < .001. The disgust and
sadness parameters had a statistically signiﬁcant effect on the prediction of stageID,
2(1) = 12.046, p = .001 and 2(1) = 6.086, p = .008 as shown in table 6.24. However,
the ordinal assumption Partial Proportion Odds have been violated in some parameters
in the model which suggested an inaccurate outcome. Therefore, Multinomial Regres-
sion has been used to conﬁrm the output since all six assumptions of the multinomial
regression is passed. The output reported is from Table 6.28, variables Disgust, Sadness
and Conscientiousness with p-values .006,0.017 and 0.051 has a signiﬁcant overall ef-
fect on the dependent StageID. The output from Ordinal and Multinomial Regression
analysis agreed on that the variables Disgust, Sadness, Conscientiousness, and Neur-
oticism has a statistically signiﬁcant impact on the dependent value StageID.
97


## Page 110


stageid (Stage 5 is reference)
B
Std. Error
Wald
df
Sig.
Exp(B)
95% Conﬁdence Interval for Exp(B)
Lower Bound
Upper Bound
Stage 1
Intercept
1.603
1.165
1.892
1
.169
Anger
1.436
1.346
1.139
1
.286
4.205
.301
58.815
Disgust
12.177
3.634
11.227
1
.001
194325.644
156.670
241031239.977
Fear
-1.157
1.623
.509
1
.476
.314
.013
7.562
Joy
.090
1.377
.004
1
.948
1.094
.074
16.268
Sadness
-3.217
1.113
8.358
1
.004
.040
.005
.355
Openness
.001
.739
.000
1
.999
1.001
.235
4.265
Conscientiousness
-.851
.603
1.992
1
.158
.427
.131
1.392
Extraversion
-.645
.653
.977
1
.323
.524
.146
1.886
Agreeableness
.288
.624
.213
1
.644
1.334
.393
4.529
Neuroticism
-.789
.495
2.544
1
.111
.454
.172
1.198
Stage 2
Intercept
-.035
1.009
.001
1
.972
Anger
-1.245
1.354
.845
1
.358
.288
.020
4.093
Disgust
6.481
3.806
2.899
1
.089
652.527
.376
1133879.043
Fear
.584
1.438
.165
1
.684
1.794
.107
30.034
Joy
.967
1.127
.736
1
.391
2.631
.289
23.971
Sadness
-.812
.925
.771
1
.380
.444
.072
2.720
Openness
.522
.696
.563
1
.453
1.685
.431
6.590
Conscientiousness
-.308
.552
.312
1
.576
.735
.249
2.167
Extraversion
-.090
.581
.024
1
.877
.914
.293
2.852
Agreeableness
.219
.574
.146
1
.703
1.245
.404
3.836
Neuroticism
-.468
.455
1.058
1
.304
.626
.257
1.528
Stage 3
Intercept
-1.535
1.418
1.173
1
.279
Anger
-.944
2.172
.189
1
.664
.389
.006
27.492
Disgust
12.097
5.049
5.741
1
.017
179275.939
9.041
3554947303.303
Fear
.945
2.161
.191
1
.662
2.572
.037
177.816
Joy
2.562
1.534
2.790
1
.095
12.964
.641
262.113
Sadness
.834
1.315
.402
1
.526
2.302
.175
30.320
Openness
.565
1.035
.298
1
.585
1.759
.231
13.379
Conscientiousness
-2.517
.888
8.028
1
.005
.081
.014
.460
Extraversion
-.751
.958
.616
1
.433
.472
.072
3.082
Agreeableness
.527
.902
.341
1
.559
1.693
.289
9.921
Neuroticism
-.507
.654
.601
1
.438
.602
.167
2.171
Stage 4
Intercept
-.150
1.288
.013
1
.908
Anger
-2.805
1.994
1.979
1
.159
.060
.001
3.014
Disgust
3.907
5.125
.581
1
.446
49.763
.002
1147335.006
Fear
1.603
1.820
.776
1
.378
4.970
.140
175.957
Joy
1.551
1.467
1.117
1
.291
4.715
.266
83.649
Sadness
-1.002
1.210
.686
1
.408
.367
.034
3.934
Openness
.497
.887
.314
1
.575
1.644
.289
9.346
Conscientiousness
-.731
.765
.915
1
.339
.481
.108
2.154
Extraversion
-.074
.753
.010
1
.922
.929
.212
4.063
Agreeableness
.510
.744
.470
1
.493
1.665
.388
7.149
Neuroticism
-1.493
.628
5.656
1
.017
.225
.066
.769
Table 6.29: Multinomial Regression - Parameter Estimates
6.6
Incorporating Emotion and Personality-Based Ana-
lysis in User-centered Modelling
6.6.1
Introduction
As computer systems and applications have become more widespread and complex,
with increasing demands and expectations of ever-more intuitive human-computer in-
teractions, research in modelling, understanding and predicting user behaviour demands
has become a priority across a number of domains [220]. In these application domains, it
is useful to obtain knowledge about user proﬁles or models of software applications, in-
98


## Page 111


cluding intelligent agents, adaptive systems, intelligent tutoring systems, recommender
systems, e-commerce applications and knowledge management systems [86, 87, 299].
Furthermore, understanding user behaviour during system events leads to a better in-
formed predictive model capability, allowing the construction of more intuitive inter-
faces and an improved user experience. This work further builds upon our research
published in 2016 [220].
We are particularly interested in the relationship between digital footprint and beha-
viour and personality [236, 240, 28, 29]. A wide range of pervasive and often publicly
available datasets encompassing digital footprints, such as social media activity, can be
used to infer personality [184, 242]. Big social data offers the potential for new insights
into human behaviour and development of robust models capable of describing indi-
viduals and societies [186]. Social media has been used in varying computer system
approaches; in the past this has mainly been the textual information contained in blogs,
status posts and photo comments [28, 29], but there is also a wealth of information in the
other ways of interacting with online artefacts. Research in an image or video analysis
includes promising studies on YouTube videos for classiﬁcation of speciﬁc behaviours
and indicators of personality traits [27]. This work uses crowdsourced impressions, so-
cial attention, and audio-visual behavioural analysis on slices of conversational video
blogs extracted from YouTube. From sharing and gathering of information and data to
catering for marketing and business needs; it is now widely used as technical support
for computer system platforms.
The work presented in this experiment is based on previous work in psycholinguistic
science and aims to provide further insight into how the words and constructs we use
in our daily life and online interactions reﬂect our personalities and our underlying
emotions. As part of this active research ﬁeld, it is widely accepted that written text
reﬂects more than the words and syntactic constructs, but also conveys emotion and
personality traits [255]. As part of our work, the IBM Watson Tone Analyzer (part of
the IBM Watson Developer Cloud toolchain) has been used to identify emotion tones in
the textual interactions in an online system, building on previous work in this area that
shows a strong correlation between the word choice and personality, emotions, attitude
and cognitive processes, providing further evidence that it is possible to proﬁle and
potentially predict users identity [106]. The Linguistic Inquiry and Word Count (LIWC)
psycholinguistics dictionary [256, 320] is used to ﬁnd psychologically meaningful word
categories from word usage in writing; the work presented here provides a modelling
and analysis framework, as well as associated toolchain, for further application to larger
datasets to support the research goal of improving user-centered modelling [220].
The dataset used in this experiment (see Section 5.3) consists of users (N=391), in-
teractions and comments (N=1390) as responses to system status and reporting their
experience with using the system. Google Analytics has been used to track user beha-
viour and web statistics (such as impressions); this data from has been used to identify
99


## Page 112


the server’s status and categorised the status as two stages: Idle, where the system had a
higher number of active sessions; and marked as Failure, where the system had a lower
number of sessions engaged. Figure 6.11 provides a plot of web trafﬁc from Google
Analytics over a speciﬁc day, clearly showing the drop at 20:00 where the system had
been identiﬁed as in the Failure state.
Figure 6.11: Google Analytics proﬁle showing behaviour of the system over a 24 hour
period (timeline during the day vs. number of active sessions)
6.6.2
Analysis
All communications had been collected and grouped by server status, then sent to the
IBM Watson Tone Analyzer to produce the emotion social tone scores, to present an
overview of the system behaviour and users interaction with Facebook at the same time.
Figure 6.12 shows the association between the server behaviour and emotions of the
users; in the system, Failure status gives a signiﬁcant difference in overall Anger in
different status; furthermore, the Joy parameter shows a signiﬁcant difference with the
system in Idle and Failure status. However Fear and Sadness parameters is about the
same, even with the system in Idle status.
Figure 6.12: Overall emotion tone response to server failure/idle status
We recognised the user’s personality based on analysis of their Facebook interac-
tions, namely by collecting all comments from the users, again using the IBM Watson
100


## Page 113


Openness
Conscientiousness
Extraversion
Agreeableness
Neuroticism
anger
disgust
fear
joy
sadness
Server Status
0.528
0.523
0.537
0.653
0.511
0.217821
0.793375
0.501131
0.031477
0.284936
Failure
0.252
0.063
0.037
0.266
0.989
0.542857
0.084615
0.178302
0.224453
0.264283
Failure
0.817
0.571
0.157
0.012
0.401
0.162798
0.166694
0.213870
0.410916
0.220049
Failure
0.197
0.130
0.180
0.419
0.990
0.468938
0.259794
0.350803
0.037265
0.636412
Failure
0.155
0.079
0.081
0.226
0.975
0.539162
0.219993
0.431932
0.011625
0.642158
Failure
0.158
0.281
0.332
0.510
0.869
0.419015
0.162022
0.213941
0.066892
0.686369
Failure
0.817
0.571
0.157
0.012
0.401
0.041602
0.026298
0.141606
0.651962
0.106500
Failure
0.058
0.038
0.147
0.375
0.989
0.449222
0.057946
0.181654
0.158412
0.547968
Idle
0.178
0.138
0.800
0.564
0.828
0.207497
0.096643
0.093218
0.769316
0.162241
Idle
0.105
0.463
0.792
0.704
0.041
0.134487
0.257145
0.195858
0.181699
0.509379
Idle
0.589
0.479
0.147
0.339
0.828
0.360527
0.240875
0.321188
0.117492
0.212762
Idle
0.338
0.235
0.104
0.304
0.869
0.164107
0.015058
0.230148
0.629562
0.356028
Idle
0.204
0.203
0.480
0.329
0.892
0.625891
0.193692
0.242459
0.153679
0.166561
Idle
0.689
0.968
0.805
0.465
0.029
0.246246
0.080353
0.123761
0.807537
0.135646
Idle
0.093
0.175
0.642
0.563
0.875
0.279503
0.045658
0.207278
0.088724
0.505607
Idle
0.277
0.296
0.276
0.332
0.892
0.499199
0.143897
0.269725
0.188664
0.285462
Idle
0.055
0.095
0.783
0.699
0.935
0.450997
0.153940
0.263070
0.350778
0.116282
Idle
Table 6.30: Snapshot of the data used in the analysis
Personality Insights tool. However, some users in the dataset had completed the Big
Five Questionnaire (N = 44); for these users, their “Big Five” scores have been used
instead. The second stage involved grouping the comments based on server status and
segmenting these communications by the user; this allowed us to investigate the impact
of server status in the emotion of the user and investigate the Big Five dimension as a
constant parameter. By investigating the association between the personality trait di-
mensions and the social emotion tones, we can ﬁnd the highest correlation to identify
the critical elements of the potential model by applying linear regression and Pearson
correlation. The output will allow the building of a neural network multilayer perception
using the possible signiﬁcant aspects with higher associations [220].
The previous overview encourages further study to understand the correlation between
user’s behaviour and complex computer system behaviours. The data collected from the
social media communications have been grouped by users and using the IBM Watson
Personality Insights, we were able to identify the Big Five personality traits for each
user. Using the IBM Watson Tone Analyzer, the data has been grouped by user’s com-
ments and server status (Failure, Idle) to identify social emotion tone for each user.
Table 6.30 shows an example of data used in this investigation, with each row repres-
enting a unique user, and each column represents the Big Five traits, social emotion
tones, and server status.
6.6.3
Key Findings
As part of modelling the users’ responses and behaviour, one of the approaches to build-
ing the conceptual framework model is to apply linear regression to investigate the rela-
tionship between the Big Five personality dimensions and the emotion tones features.
During the analysis, the linear regressions (presented in Table 6.31 and Figures 6.13,
6.14, 6.15, 6.16 and 6.17) does show signiﬁcant correlations between the Big Five di-
mensions and the social emotion tones; however, certain correlations can be highlighted
101


## Page 114


Figure 6.13: Scatter plot of Big Five dimension “Openness” (dependent variable) and
social emotion tones (independent variables)
Figure 6.14: Scatter plot of Big Five dimension “Extraversion” (dependent variable)
and social emotion tones (independent variables)
and used as key elements for the model. The correlation of Openness and Disgust, is
0.479; the correlation of Extraversion and Joy is 0.446 with p-value of zero. Conscien-
tiousness and Joy with 0.436 correlation and Disgust with 0.255. Agreeableness, does
not appear to have a high impact in the social emotion parameters, with the highest
correlation being 0.188 with Joy, which can be overlooked as a useful factor in the
102


## Page 115


Figure 6.15: Scatter plot of Big Five dimension “Conscientiousness” (dependent vari-
able) and social emotion tones (independent variables)
Figure 6.16: Scatter plot of Big Five dimension “Neuroticism” (dependent variable) and
social emotion tones (independent variables)
model. Neuroticism and Disgust is -0.363, Joy is -0.487 and p-value is zero is both
cases; and Sadness with 0.233. All correlation values are < 0.5; however, it is noticed
that Agreeableness does not have a linear relationship with any of the social emotion
tones. Furthermore, the social emotion tones that have a potential linear relationship are
Disgust, Joy and Sadness, since the three tones have a correlation between > 0.3 and
103


## Page 116


Figure 6.17: Scatter plot of Big Five dimension “Agreeableness” (dependent variable)
and social emotion tones (independent variables)
Openness
Extraversion
Conscientiousness
Agreeableness
Neuroticism
B
t
Sig
B
t
Sig
B
t
Sig
B
t
Sig
B
t
Sig
(constant)
0.356
3.282
0.001
0.162
1.642
0.101
0.16
1.623
0.105
0.297
2.831
0.005
0.828
9.934
0
anger
-0.063
-0.735
0.463
0.064
0.831
0.406
0.124
1.592
0.112
0.024
0.293
0.769
0.116
1.767
0.078
disgust
0.478
4.354
0
0.114
1.142
0.253
0.255
2.551
0.011
-0.061
-0.574
0.566
-0.363
-4.303
0
fear
0.065
0.534
0.594
0.172
1.549
0.122
0.04
0.356
0.722
0.093
0.783
0.434
-0.023
-0.241
0.81
joy
0.066
0.561
0.575
0.446
4.179
0
0.436
4.058
0
0.188
1.652
0.099
-0.487
-5.39
0
sadness
-0.226
-2.118
0.035
-0.185
-1.906
0.057
-0.03
-0.313
0.754
0.014
0.132
0.895
0.233
2.841
0.005
Table 6.31: Linear regression coefﬁcients
< 0.5.
Previous linear regression analysis suggested that the following Big Five dimensions
(Openness, Extraversion, Conscientiousness and Neuroticism) have the highest correla-
tion with the social emotion tones (Joy, Sadness and Disgust). For further analysis, the
Pearson correlation for the same dataset has been performed to compare the output with
the linear regression correlations. As you can see in Table 6.32, there is no signiﬁcant
correlation in both; however, in the Pearson correlation, Neuroticism has the highest
correlation values across emotion tones, especially Anger, Joy and Sadness. Joy does
have a correlation with all Big Five dimensions except for Agreeableness which agrees
with the previous analysis. However, Disgust does not have a strong correlation with
any of the Big Five dimensions, which deviates from the previous analysis.
Key Elements of the Model
According to the output of the statistical analysis presen-
ted in Table 6.31 (linear regression) and Table 6.32 (Pearson correlation), the Big Five
dimension identiﬁed as the key elements from the personality traits are: Openness,
104


## Page 117


Anger
Disgust
Fear
Joy
Sadness
Openness
-0.098
0.231
0.043
0.035
-0.151
Conscientiousness
-0.111
-0.001
-0.113
0.267
-0.19
Extraversion
-0.175
-0.077
-0.071
0.349
-0.291
Agreeableness
-0.068
-0.089
-0.027
0.14
-0.069
Neuroticism
0.375
-0.037
0.153
-0.488
0.379
Table 6.32: Pearson correlations
Extraversion, Conscientiousness and Neuroticism. The statistical analysis agrees that
Agreeableness does not have a signiﬁcant correlation across any of the social emotion
tones. The social emotion tones to be used as key input elements for the proposed
model are Joy, Sadness, Anger and Disgust; although the Anger tone did not show any
signiﬁcant correlation in linear regression analysis, the value of the Pearson correlation
coefﬁcient is between 0.3 and 0.5 which can be used as input for the model.
Correctly classiﬁed instances:
43
(75.44%)
Incorrectly classiﬁed instances:
14
(24.56%)
Kappa statistic:
0.5295
Mean absolute error:
0.3432
Root mean squared error:
0.4246
Total number of instances:
57
Table 6.33: Re-evaluation output of proposed model
The dataset used to build this model is based upon a number of users (N=391),
eight inputs (Openness, Extraversion, Conscientiousness, Neuroticism, Joy, Sadness,
Anger and Disgust) and the class/output variable as the server status (where No: Sys-
tem Failure and Yes: System Idle). As shown in Table 6.33, the total number of the
instances for the testing set is 57. The output of the model shows a 75.44% correc-
ted predicted instances and 24.56% incorrectly classiﬁed instances. As this has been
performed on a small subset of the overall larger project dataset, the output data is en-
couraging and provides the infrastructure for further analysis and research to exploit the
full dataset [220].
This experiment presents preliminary results from the previous ﬂow of experiments [236,
241, 240, 220], which could provide the conceptual framework to improve user experi-
ence (UX) and computer system architecture design. Social media is now not only being
used as a content and sharing platform but also as a platform for technical support for
several of online applications and services. We have produced a model that can predict
server status based on personality traits and social emotion tones, by investigating the
linear regression and Pearson correlation to identify the key components to be used as
input for the neural network to build this model (Openness, Extraversion, Conscien-
105


## Page 118


tiousness, Neuroticism, Joy, Sadness, Anger and Disgust). The model developed shows
a good potential starting point for further data analysis, with 75% accuracy in prediction
based on 57 test cases.
6.6.4
Model Evaluation
Model
Score learn
Result mean
Result std
Logistic Regression
0.703389831
0.568717949
0.229815122
Linear Discriminant Analysis
0.711864407
0.581538462
0.189468963
KNeighborsClassiﬁer
0.559322034
0.565769231
0.125269007
DecisionTreeClassiﬁer
0.669491525
0.583782051
0.116959357
GaussianNB
0.584745763
0.555192308
0.121590399
C-Support Vector Classiﬁcation.
0.63559322
0.48974359
0.359056767
Table 6.34: Evaluate the limit model
Using python
Table 6.34 shows what would be the best classiﬁer to build the model,
the score learn shows Logistic Regression and Linear Discriminant analysis
6.7
Summary
This section provides a summary of the feature extraction process grounding the selec-
tion process on the experiments conducted in Chapter 6.
• The experiment presented in Section 6.2, Openness to Experience reported a
strong correlation with the “Accepted” groups within the dataset sample, how-
ever, the “ﬁnal selection” result parameter for the scholarship system has a differ-
ent other evaluation criteria such as Personality of the evaluator, Language level,
Academic qualiﬁcation, number of spaces available, etc which was not included
in the analysis, therefore, Openness to Experience was not selected as part of the
features.
• In the experiment presented in Section 6.3, there were statistically signiﬁcant:
Stages (1,4), Extraversion, Agreeableness and Conscientiousness, however, Con-
scientiousness and Agreeableness reported a higher correlation value of 0.01 and
0.04, therefore, Conscientiousness and Agreeableness selected from this experi-
ment.
• In the experiment presented in Section 6.5, two analysis methods were used to
conﬁrm the result, Ordinal and Multinomial Regression analysis, the output re-
ported from ordinal that variables Disgust, Sadness and Conscientiousnesswith
106


## Page 119


p-values .006,0.017 and 0.051 has a signiﬁcant overall effect on the dependent
StageID. While, the two analysis methods agreed on Disgust, Sadness and Con-
scientiousness, the parameter Neuroticism was excluded from the selection as it
was has not signiﬁcant contribution to the model in Ordinal Regression and low
p-value on Multinomial Regression Analysis of 0.143. Therefore, only Disgust,
Sadness and Conscientiousness were selected from this experiment.
• The experiment presented in Section 6.4 suggested a weak correlation between
personality traits and temporal behaviour using the dataset extracted from the
system and the questionnaire ﬁlled with the same users. Therefore, no features
selected from this experiment.
• The experiment presented in Section 6.6 suggested that Neuroticism a very strong
Pearson’s correlation values with Anger, Joy and Sadness. While Joy does have
a correlation with all Big Five Traits except for Agreeableness. Therefore, Neur-
oticism, Anger, Joy and Sadness were selected from this experiment.
107


## Page 120


Chapter 7
Developing the Conceptual Framework
for the PMSys Engine
7.1
Introduction
During this research project, several experiments and studies were conducted to explore
and understand the correlation between personality traits, emotions, and server status.
To enhance user’s experience and to understand more how user’s behaviour changes ac-
cording to the system’s response. The results of these experiments and studies provided
us with a good understanding of how user’s traits and emotions changes in different
server status from the perspective of the categories presented in our classiﬁcation (Sec-
tion 5.4). The ﬂow of experiments leads us to build our conceptual model, using the
features extracted from the analyses as presented in Chapter 5. In this chapter, we offer
a novel conceptual framework to model user’s behaviour in different computer status
(see Figure 7.1.
7.2
Personality Traits vs. Emotions, Gender and Age
7.2.1
Introduction
The previous analyses suggested a strong association between personality traits and
emotions. Furthermore, the attempt of modelling server status, suggested a strong and
possible method to model the user behaviour in different complex system behaviour.
This analysis to explore the big personality traits and emotions association and cor-
relation, a further correlation between Gender/Age and Personality traits – Emotions.
According to research by Schwartz (2013)[301], Gender and Age correlate with the per-
sonality traits. However, the same study did not mention the emotions. Therefore, this
experiment is essential a cross-validating the methodology used in Schwartz study [301]
108


## Page 121


Figure 7.1: Developing PMsys engine stages
and with extended features to the model to verify the connection between the emotions
and gender/age.
The same dataset (See section:
5.3) will be used in the analysis as Personality
Traits retrieved from the Motivation letter and emotions extracted from a different plat-
form that was used in communication (i.e., Facebook and HelpDesk). The necessary
information will be retrieved to include the gender and age as extra parameters, and the
analysis will be running separately.
7.2.2
Binomial Logistic Regression
The dataset combination suggested using Binomial Logistic Regression, as the dataset
similar to what is presented in Section 6.3, with Gender instead of StageID as a depend-
ent variable. The experiment is to examine the probability of being able to predicate
the gender based on Big Five traits and Emotions, and according to the result, it will be
decided whether to include the Gender as controlling variable in the conceptual model.
Adding the Age variable alongside with Big Five Traits and Emotions to examine if it
would improve the model or not.
In order to apply, Binomial Logistic Regression, the data needs to pass the following
assumptions:
• Linear relationship between the Big Five Traits, Emotions and logit transforma-
tion of the gender variable.
109


## Page 122


• Data must not show multicollinearity
• There should be no signiﬁcant outliers, high leverage points or highly inﬂuential
points.
Linear relationship between the Big Five Traits, Emotions and logit transforma-
tion of the gender variable
The ﬁrst part of the Box-Tidwell (1962) [34] method
expects that all continuous independent variables to transformed into their natural logs,
this means that we need to perform natural log transformations on our continuous inde-
pendent variables: Big Five Traits and Emotions. The second part of the Box-Tidwell
(1962) procedure requires creating interaction terms for each of your continuous inde-
pendent variables and their respective natural log-transformed variables. Since we have
12 continuous independent variables in this study, this means that we have to create Big
Five Trait and Emotions – interaction terms: ln_sadness * sadness (i.e., the product
of ln_sadness by sadness ). Moreover, need to be entered into the Binomial Logistic
Regression procedure, together with the Gender and Age.
According to Tabachnick (2001) [318], to calculate the new alpha () level (i.e., p-
value) for current dataset, it is by dividing the alpha level (p < .05) by the number of
terms in the model. Formulaically, this is:
adjustedalphalevel =
OriginalAlphaLevel
numberofComparisons
(7.1)
The new adjusted alpha level in this case is 0.002, (i.e., 0.05 / 23= 0.002). The
linearity of the Big Five Traits and Emotions concerning the logit of the Gender variable
was assessed via the Box-Tidwell (1962) [34] procedure. A Bonferroni correction was
applied using all twenty-one terms in the model resulting in statistical signiﬁcance being
accepted when p ¡ 0.002 [318]. According to Table 7.1, all continuous independent
variables were found to be linearly related to the logit of the dependent variable.
Data must not show multicollinearity
, next step to investigate if the data shows or
does not show multicollinearity to validate the possibility of applying binomial logistic
regression. According to Table 7.2 there was one studentized residual with a value of
-2.376743 standard deviations, which was kept in the analysis.
Bionomial Findings
This experiment aims to investigate which variable is statistically signiﬁcant of the Big
Five Traits, Emotions and Age concerning the Gender; only three were statistically
signiﬁcant: Openness (p < 0.072), Conscientiousness and Age (as shown in Table 7.3).
The result reported does not give enough accuracy regarding the correlation between
Big Five Traits, Emotions and Age to predict the Gender. Therefore, another form of
110


## Page 123


Variables in the Equation
B
S.E.
Wald
df
Sig.
Exp(B)
Step 1a
Anger
1.248
2.244
0.309
1
0.578
Disgust
-0.332
23.43
0
1
0.989
0.717
Fear
1.667
2.822
0.349
1
0.555
5.294
Joy
1.961
1.496
1.719
1
0.19
7.107
Sadness
-1.251
0.854
2.145
1
0.143
0.286
Openness
-2.494
1.152
4.691
1
0.03
0.083
Conscientiousness
2.303
1.266
3.311
1
0.069
10.008
Extraversion
0.484
0.911
0.282
1
0.595
1.622
Agreeableness
0.155
0.954
0.026
1
0.871
1.167
Neuroticism
0.166
0.832
0.04
1
0.842
1.181
Age
0.289
0.584
0.245
1
0.621
1.335
Anger by ln anger
1.945
3.032
0.412
1
0.521
6.992
Disgust by ln disgust
2.757
11.198
0.061
1
0.806
15.75
Fear by ln fear
-0.623
3.262
0.036
1
0.849
0.536
Joy by ln joy
4.399
2.49
3.121
1
0.077
81.354
Sadness by ln sadness
-1.914
2.128
0.81
1
0.368
0.147
Openness by ln openness
7.291
3.366
4.693
1
0.03
1466.912
Conscientiousness by ln conscientiousness
1.096
2.669
0.169
1
0.681
2.992
Extraversion by ln extraversion
-3.599
2.282
2.487
1
0.115
0.027
Agreeableness by ln agreeableness
-0.662
2.413
0.075
1
0.784
0.516
Neuroticism by ln neuroticism
1.957
2.622
0.557
1
0.456
7.076
Age by ln age
-0.053
0.129
0.17
1
0.68
0.948
Constant
-0.39
4.891
0.006
1
0.936
0.677
Table 7.1: Variables in the Equation - Gender
Casewise Listb
Case
Selected Statusa
Observed
Predicted
Predicted Group
Temporary Variable
gender
Resid
ZResid
7
S
F**
0.85
M
-0.85
-2.377
Table 7.2: Casewise Diagnostics
analysis is applied next to explore and investigate a potential association between the
above variables.
7.2.3
Pearson’s Partial Correlation
As the Binomial Logistic Regression, suggested a correlation between Openness, Con-
scientiousness and Age to predict the Gender, the Pearson’s partial correlation was run
to assess the relationship between Big Five Traits, Emotions, Age and Gender and to
111


## Page 124


Variables in the Equation
B
S.E.
Wald
df
Sig.
Exp(B)
95% C.I.for EXP(B)
Lower
Upper
Anger
0.329
1.518
0.047
1
0.828
1.39
0.071
27.209
Disgust
-5.201
7.187
0.524
1
0.469
0.006
0
7219.283
Fear
1.405
1.635
0.739
1
0.39
4.075
0.165
100.404
Joy
0.169
0.951
0.031
1
0.859
1.184
0.184
7.631
Sadness
-0.567
0.731
0.6
1
0.438
0.567
0.135
2.379
Openness
-1.556
0.866
3.229
1
0.072
0.211
0.039
1.152
Conscientiousness
1.261
0.764
2.722
1
0.099
3.529
0.789
15.786
Extraversion
0.389
0.78
0.249
1
0.618
1.476
0.32
6.801
Agreeableness
0.262
0.778
0.113
1
0.736
1.3
0.283
5.974
Neuroticism
0.234
0.644
0.132
1
0.717
1.263
0.358
4.46
Age
0.059
0.031
3.664
1
0.056
1.061
0.999
1.127
Constant
-1.395
1.175
1.41
1
0.235
0.248
Table 7.3: Binomial Log – variables in the equation
conﬁrm the output of the Binomial or include more variable as a strong association.
According to the analysis performed in Section 6.2, there were linear relationships
between Big Five Traits and Emotions, as assessed by scatterplots and partial regression
plots. There was univariate normality, as evaluated by Shapiro-Wilk’s test (p > .05), and
there were no univariate or multivariate outliers, as assessed by Mahalanobis Distance
respectively – see Figure 6.7 and 6.8.
Key Findings and Discussion
The above tables shows the output of Pearson’s Partial Correlation. In Table 7.4, the
controlling variable is Gender, a bivariate Pearson’s correlation established that there
was a strong, statistically signiﬁcant linear relationship between Conscientiousness and
Anger, r(204) = −.141, p < .05 , Neuroticism and Fear r(204) = −.166, p < .05. Pear-
son’s partial correlation showed that the strength of this linear relationship was improved
when Gender was controlled for Conscientiousness and Anger rpartial(203) = −.139,
p = 0.47 and it is still the same between Neuroticism and Fear rpartial(203) = −.166
- p = .017 and still statistically signiﬁcant. In Table 7.5, the controlling variable is Age.
Pearson’s partial correlation showed that the strength of this linear relationship was
improved when Age was controlled, in respect to the relationship between Conscien-
tiousness and Anger rpartial(203) = −.138 - p = 0.49 and between Neuroticism and
Fear rpartial(203) = −.152 −p = 0.030 and still statistically signiﬁcant. In Table 7.6,
the controlling variable is Gender and Age. Pearson’s partial correlation showed that
the strength of this linear relationship was improved when Age was controlled, in re-
spect to the relationship between Conscientiousness and Anger and Neuroticism and
112


## Page 125


Pearson’s partial correlation
Anger
Disgust
Fear
Joy
Sadness
Controlling Variable: None
Openness
Correlation
.044
-.008
-.038
.024
-.015
Signif. (2-tailed)
.529
.913
.586
.729
.833
df
204
204
204
204
204
Conscientiousness
Correlation
-.141
-.093
-.099
.057
-.040
Signif. (2-tailed)
.043
.183
.155
.418
.566
df
204
204
204
204
204
Extraversion
Correlation
.040
.056
-.035
-.079
.003
Signif. (2-tailed)
.567
.421
.616
.262
.960
df
204
204
204
204
204
Agreeableness
Correlation
.010
.041
.026
-.094
.053
Signif. (2-tailed)
.881
.556
.715
.178
.447
df
204
204
204
204
204
Neuroticism
Correlation
-.038
-.058
-.166
-.006
.030
Signif. (2-tailed)
.585
.407
.017
.937
.664
df
204
204
204
204
204
Age
Correlation
-.042
-.082
-.187
.170
-.085
Signif. (2-tailed)
.551
.241
.007
.015
.222
df
204
204
204
204
204
Controlling Variable: Gender
Openness
Correlation
.041
-.014
-.039
.029
-.020
Signif. (2-tailed)
.558
.844
.579
.681
.772
df
203
203
203
203
203
Conscientiousness
Correlation
-.139
-.086
-.100
.052
-.034
Signif. (2-tailed)
.047
.219
.155
.463
.632
df
203
203
203
203
203
Extraversion
Correlation
.041
.058
-.035
-.080
.005
Signif. (2-tailed)
.560
.410
.617
.256
.946
df
203
203
203
203
203
Agreeableness
Correlation
.013
.046
.026
-.098
.057
Signif. (2-tailed)
.855
.514
.711
.163
.413
df
203
203
203
203
203
Neuroticism
Correlation
-.036
-.054
-.166
-.008
.034
Signif. (2-tailed)
.606
.439
.017
.904
.627
df
203
203
203
203
203
Age
Correlation
-.038
-.075
-.188
.166
-.080
Signif. (2-tailed)
.587
.282
.007
.017
.257
df
203
203
203
203
203
Table 7.4: Pearson’s Partial Correlation (controlling variable: Gender)
113


## Page 126


Pearson’s partial correlation
Anger
Disgust
Fear
Joy
Sadness
Controlling Variable: None
Openness
Correlation
.044
-.008
-.038
.024
-.015
Signif. (2-tailed)
.529
.913
.586
.729
.833
df
204
204
204
204
204
Conscientiousness
Correlation
-.141
-.093
-.099
.057
-.040
Signif. (2-tailed)
.043
.183
.155
.418
.566
df
204
204
204
204
204
Extraversion
Correlation
.040
.056
-.035
-.079
.003
Signif. (2-tailed)
.567
.421
.616
.262
.960
df
204
204
204
204
204
Agreeableness
Correlation
.010
.041
.026
-.094
.053
Signif. (2-tailed)
.881
.556
.715
.178
.447
df
204
204
204
204
204
Neuroticism
Correlation
-.038
-.058
-.166
-.006
.030
Signif. (2-tailed)
.585
.407
.017
.937
.664
df
204
204
204
204
204
Gender
Correlation
.030
.056
.005
-.041
.050
Signif. (2-tailed)
.668
.423
.947
.558
.473
df
204
204
204
204
204
Age
Correlation
-.042
-.082
-.187
.170
-.085
Signif. (2-tailed)
.551
.241
.007
.015
.222
df
204
204
204
204
204
Controlling Variable Age
Openness
Correlation
.050
.003
-.014
.002
-.004
Signif. (2-tailed)
.475
.964
.842
.978
.960
df
203
203
203
203
203
Conscientiousness
Correlation
-.138
-.084
-.080
.038
-.031
Signif. (2-tailed)
.049
.229
.257
.592
.664
df
203
203
203
203
203
Extraversion
Correlation
.041
.058
-.032
-.083
.005
Signif. (2-tailed)
.559
.407
.650
.235
.940
df
203
203
203
203
203
Agreeableness
Correlation
.001
.023
-.018
-.057
.035
Signif. (2-tailed)
.990
.743
.796
.413
.622
df
203
203
203
203
203
Neuroticism
Correlation
-.034
-.051
-.152
-.022
.039
Signif. (2-tailed)
.623
.471
.030
.753
.580
df
203
203
203
203
203
Gender
Correlation
.025
.046
-.020
-.019
.040
Signif. (2-tailed)
.724
.513
.772
.785
.574
df
203
203
203
203
203
Cells contain zero-order (Pearson) correlations.
Table 7.5: Pearson’s Partial Correlation (controlling variable: Age)
114


## Page 127


Pearson’s partial correlation
Correlation
Anger
Disgust
Fear
Joy
Sadness
Controlling Variable: None
Openness
Correlation
.044
-.008
-.038
.024
-.015
Signif. (2-tailed)
.529
.913
.586
.729
.833
df
204
204
204
204
204
Conscientiousness
Correlation
-.141
-.093
-.099
.057
-.040
Signif. (2-tailed)
.043
.183
.155
.418
.566
df
204
204
204
204
204
Extraversion
Correlation
.040
.056
-.035
-.079
.003
Signif. (2-tailed)
.567
.421
.616
.262
.960
df
204
204
204
204
204
Agreeableness
Correlation
.010
.041
.026
-.094
.053
Signif. (2-tailed)
.881
.556
.715
.178
.447
df
204
204
204
204
204
Neuroticism
Correlation
-.038
-.058
-.166
-.006
.030
Signif. (2-tailed)
.585
.407
.017
.937
.664
df
204
204
204
204
204
Age
Correlation
-.042
-.082
-.187
.170
-.085
Signif. (2-tailed)
.551
.241
.007
.015
.222
df
204
204
204
204
204
Gender
Correlation
.030
.056
.005
-.041
.050
Signif. (2-tailed)
.668
.423
.947
.558
.473
df
204
204
204
204
204
Controlling Variable: Age and Gender
Openness
Correlation
.047
-.003
-.012
.004
-.009
Signif. (2-tailed)
.501
.969
.870
.950
.902
df
202
202
202
202
202
Conscientiousness
Correlation
-.136
-.079
-.083
.036
-.026
Signif. (2-tailed)
.053
.260
.239
.614
.714
df
202
202
202
202
202
Extraversion
Correlation
.042
.059
-.032
-.084
.006
Signif. (2-tailed)
.554
.399
.646
.233
.930
df
202
202
202
202
202
Agreeableness
Correlation
.004
.028
-.021
-.060
.039
Signif. (2-tailed)
.958
.686
.770
.394
.576
df
202
202
202
202
202
Neuroticism
Correlation
-.033
-.048
-.153
-.023
.041
Signif. (2-tailed)
.639
.495
.029
.741
.557
df
202
202
202
202
202
a Cells contain zero-order (Pearson) correlations.
Table 7.6: Pearson’s Partial Correlation (controlling variables: Gender and Age
115


## Page 128


Fear , rpartial(203) = −.138 - p = 0.49 , and between and Neuroticism and Fear
rpartial(203) = −.152 - p = 0.030 and still statistically signiﬁcant. The above ﬁnd-
ings suggests that Gender and Age as controlled variable combined (as per Table 7.6)
would improve the linear relationship between Big Five and Emotions variables spe-
cially Conscientiousness, Neuroticism , Anger and Fear and improve strength of linear
relationship between Extraversion and Anger, Disgust, Fear, Joy and Sadness although
the linear relationship was not statistically signiﬁcant. Those ﬁndings are aligned with
the output from the Binomial Logistic Regression (see Section 7.2.2), in the correlation
of the Conscientiousness and Age and impact of Gender in improving the association
between variables.
Summary
In the experiment presented in Section 7.2, Age was found to improve the association
between Conscientiousness and Anger and also, between Neuroticism and Fear. There-
fore, Age were selected as feature in the proposed model. While, gender were found
also, to improve the association between same traits, the gender variable could not be
used in the model as it is built using Neural Network and it is not possible to use dicho-
tomy variable as input to the model. However, it is noted for future work.
Based on the previous justiﬁcation discussed on section 7.2.3 and section 6.7 , the
features extracted for the model are anger, disgust,joy, sadness, conscientiousness,
agreeableness, neuroticism and age. We build upon these results in the next chapter
to develop and reﬁne the conceptual framework for the PMSys engine.
7.2.4
Rationale of using Random Forest Tree
According to the literature, random forests (RF) were based on decision trees and com-
bined with aggregation and bootstrap ideas and were ﬁrst introduced by Breiman in
1999 [39]. It is a powerful non-parametric statistical methodology; it is working to
improve the efﬁciency with regression problems as well two-class and multi-class clas-
siﬁcation problems, in a single and versatile framework. In 2015, Erwan Scornet et al.
proved the consistency of RF in a paper published on The Annals of Statistics [302]. Ac-
cording to a 2014 research survey conducted by Khaled Fawagreh et al. to investigate
the RF applications in ecology [81], medicine [177], astronomy [118], autopsy [181],
trafﬁc and transport planning [359], agriculture [193] and bioinformatics and compu-
tational biology [33], result shows in that RF has improved to be excellent due to its own
characters in classiﬁcation [107]. According to Zaklouta et al. [359], RFs performed
better than K-d trees by improving the classiﬁcation rate up to 97.2% and 81.8%. Other
beneﬁts as listed in the original paper about RF [39]:
• Accuracy is as good as Adaboost and sometimes better;
116


## Page 129


• It is faster than bagging or boosting;
• It gives useful internal estimates of error, strength, correlation and variable im-
portance;
• It is simple and easily parallelised.
Therefore, the literature supports the choice of the RF as the primary classiﬁer for
the model. Nevertheless, the mixture of the dataset used as input for the classiﬁer ﬁts
well with the best performance required for the RF as previous application reported
reasonably similar variables data type (see Section 4.2.1).
7.2.5
Key Findings
=== Summary ===
Correctly Classiﬁed Instances 965
68.5856 %
Incorrectly Classiﬁed Instances 442
31.4144 %
Kappa statistic
0.5811
Mean absolute error
0.1972
Root mean squared error
0.3228
Relative absolute error
52.5898 %
Root relative squared error
74.5455 %
Total Number of Instances
1407
Table 7.7: Weka Summary model output
TP Rate
FP Rate
Precision
Recall
F-Measure
MCC
ROC Area
PRC Area
Class
0.716
0.079
0.752
0.716
0.734
0.648
0.9
0.829
Down
0.658
0.107
0.672
0.658
0.665
0.555
0.872
0.778
Error
0.662
0.202
0.522
0.662
0.584
0.428
0.835
0.58
Idle
0.707
0.031
0.883
0.707
0.785
0.731
0.886
0.849
Slow
Weighted Avg.
0.686
0.105
0.707
0.686
0.692
0.591
0.873
0.759
Table 7.8: Weka output (detailed accuracy by class)
As showing in Table 7.7, correlation coefﬁcient 0.685856 implies 68.58% of the
variance in your data is explained by the model. Further details reported on Table 7.8,
TP rate, instances correctly classiﬁed as a given class show high average value at down
and slow status. ROC area, suggested high value across all classes with average weight
of 0.759 suggesting a high performance for the classiﬁer.
117


## Page 130


7.3
Model Veriﬁcation: Observing Emotions in Real Time
7.3.1
Overview
The output of the model reported as 68.5% accuracy using cross ﬁtting same dataset;
however, to verify the model performance with a new dataset, a new web-based applic-
ation developed to collect a data similar to the dataset used in training the model (see
Figure 7.2).
7.3.2
Web-Based Veriﬁcation Tool
The web-based tool was built using Joomla, PHP, MySQL, JQuery and JavaScript, the
main point of the veriﬁcation model is to replicate the same scholarship system as a
simulation to collect a new dataset in same system statues idle, error,down and slow.
The web-based veriﬁer staged to two stages:
• Stage 1: Big Five Questionnaire;
• Stage 2: Collect emotion in different system status.
In the live simulation all participants were given maximum one hour to complete the
experiments, the experiment was robust and were given same conditions.
Stage 1: Big Five Questionnaire
1 /∗∗
2 ∗Function
C a l c u l a t e
3 ∗@param :
$ t y p e i d INT , $ t e s t
INT , $uid INT
4 ∗@param :
Return
f l o a t
score
of
the
user
5 ∗@throws :
none
6 ∗/
7 f u n c t i o n
c a l c u l a t e ( $type id , $ t e s t , $uid )
8
{
9
$db= JF a ct o ry : : getDBO ( ) ;
10
$sql = ’SELECT ∗FROM b ig 5 el em en t s WHERE type =” ’ . $ t y p e i d . ’ ” ORDER
BY id ’ ;
11
$db−>setQuery ( $sql ) ;
12
$db−>Query ( ) ;
13
$num=$db−>getNumRows ( ) ;
14
$rows=$db−>l o a d O b j e c t L i s t ( ) ;
15
$ t o t a l =0;
16
f o r eac h
( $rows
as $row )
17
{
18
$score = $ t h is −>getScore ( $row−>id , $ t e s t , $uid ) ;
19
i f
( $score )
118


## Page 131


Figure 7.2: Veriﬁcation stages illustration
20
{
21
22
119


## Page 132


23
i f
( $ t h is −>checkQuestionReverse ( $row−>id , $ t e s t ) )
24
{
25
$score = $ t h is −>r e v e r s e ( $score ) ;
26
}
27
e l s e
28
{
29
$score = $score ;
30
}
31
$ t o t a l = $score + $ t o t a l ;
32
}
33
}
34
r e t u r n
$ t o t a l / $num ;
35
}
Listing 7.1: Model function to calculate score of each personality trait
Figure 7.3: Big Five Questionnaire (Web Version)
As per the discussion in the literature review, the Big Five Questionnaire is used to
extract the user’s personality by providing the questionnaire in the Annexes; the liter-
ature proposed an equation to calculate each trait [164]. The “Big Five” questionnaire
is developed in a web application to make it accessible to distribute, using PHP, JQuery
and MySQL as the database to hold the date. Figure 7.3 is a screenshot of the question-
naire as web-version. Figure 7.4, shows the output of the Big Five Questionnaire.
The architecture of the web veriﬁer tool is based on the MVC design pattern to
match the original EU scholarship system architecture, the code in Listing 7.1 refer to
the model function responsible in calculating the score of each personality traits [164].
120


## Page 133


Figure 7.4: Big Five Questionnaire Output sample (Web Version)
Stage 2: Collecting Emotions vs. System Status
After storing the personality traits of the user based on the questionnaire, the next step
is to collect the emotion from the user in different computer status. A web application
has been developed particularly to ask the user four question and triggered a one of
the four status idle, error,down and slow, after triggering the event a pop message is
shown for the user to provide his/her emotion. According to the literature, Alberto et al.
(2016) [25] suggested that The “Affective Slider” is an away to capture the emotion and
reactions of the user, by introducing a novel tool for the measurement of effect. [25].
The similar methodology followed in capture the user’s emotion, and reactions to the
event occur.
121


## Page 134


Figure 7.5: Triggering slow event as part of the simulation
Figure 7.5, shows the simulation of the slow status. After a user asked to complete
a question the user is prompted to save and move to the next question. A spinning bar
is represented to show that the transmission is slow and that the process is taking more
than 10 seconds to save, and for each of rest of system status is a simulation to capture
the user’s reaction, and emotions. Figure 7.6 shows a pop-up message appears after each
event to capture how the user felt about the previous event and that based on the affective
slider [25] supported by the ﬁndings in the literature as discussed in Section 2.6.2.
7.3.3
Dataset Veriﬁcation
The data stored in a MySQL database; for each user, the Big Five personality traits
extracted from the questionnaire and the emotions alongside with the computer system
status. The number of a participant in both stages is 47 participant. The number dropped
from initially registered participants and that because some of the participants assumed
the system was down for real while triggering the down, event and they did not get back
to complete the assessment. Table 7.9 shows sample of the data used to test the model
using Weka tool.
7.3.4
Key Findings
The Weka explorer was used to verify and evaluate the model against new dataset col-
lected from using the web veriﬁer tool as explained in the previous step, the table below
shows the output of the Weka evaluation report, as shown in table 7.10 the model cor-
rectly classiﬁed 61.17% of the data. The dataset consists of 188 instances, that four
record for each of the 47 participants.
122


## Page 135


Figure 7.6: Capturing emotions from the user (adapted from “The affective slider meth-
odology”)
Furthermore, Table 7.11 shows more detailed regarding the performance of the
model, the highest value for ROC Area is when the status is down and the lowest value
is when the status is idle, however, the average ROC Area is 0.644 which shows a good
performance for the model. Overall, the TP Rate, FP Rate and PRC Area is consider-
able low in case of status idle and slow, which shows the performance of the model in
those two cases are not good as expected.
123


## Page 136


Anger
Disgust
Joy
Openness
Conscientiousness
Agreeableness
Neuroticism
serverStatus
0.088
0.016
0.03
0.082
0.076
0.067
0.053
Error
0.054
0.051
0.049
0.058
0.056
0.08
0.048
Error
0.061
0.054
0.04
0.058
0.056
0.08
0.048
Down
0.055
0.05
0.041
0.058
0.056
0.08
0.048
Slow
0.05
0.05
0.05
0.058
0.056
0.08
0.048
Idle
0.09
0.04
0.045
0.073
0.084
0.076
0.038
Error
0.074
0.073
0.05
0.071
0.056
0.053
0.073
Error
0.069
0.031
0.05
0.058
0.067
0.06
0.07
Idle
0.05
0.05
0.05
0.058
0.067
0.06
0.07
Slow
0.076
0.031
0.064
0.058
0.067
0.06
0.07
Down
0.085
0.034
0.062
0.058
0.067
0.06
0.07
Error
0.06
0.065
0.036
0.064
0.053
0.062
0.068
Error
0.03
0.02
0.068
0.064
0.053
0.062
0.068
Down
0.01
0.03
0.047
0.064
0.053
0.062
0.068
Slow
0.19
0.015
0.057
0.064
0.053
0.062
0.068
Idle
0.01
0.002
0.077
0.067
0.062
0.064
0.068
Error
0.064
0.027
0.027
0.073
0.071
0.056
0.073
Error
0.075
0.063
0.018
0.073
0.071
0.056
0.073
Down
0.058
0.04
0.02
0.073
0.071
0.056
0.073
Slow
0.09
0.012
0.089
0.073
0.071
0.056
0.073
Idle
Table 7.9: Sample of the dataset used in the veriﬁcation process
=== Summary ===
Correctly Classiﬁed Instances
115
61.17%
Incorrectly Classiﬁed Instances
73
38.83%
Kappa statistic
0.4407
Mean absolute error
0.3055
Root mean squared error
0.3474
Total Number of Instances
188
Table 7.10: Weka summary - evaluating model using test dataset
7.4
Summary
This chapter presents the development process of the conceptual model grounded on the
features extracted from the ﬂow experiments in chapter 6. The model contributes to the
identiﬁed gap in the literature towards producing a conceptual model in an attempt to
digital proﬁle the user in different computer status. The model achieved 68% accuracy in
predicting the system status. For instance, in case of users are posing in social networks
(e.g. Facebook, Twitter) or any other median of communication, the PMsys engine will
be able to tell (with 68% accuracy) if the user complaints about the server being slow,
124


## Page 137


TP Rate
FP Rate
Precision
Recall
F-Measure
MCC
ROC Area
PRC Area
Class
0.747
0.139
0.823
0.747
0.783
0.615
0.804
0.683
Down
0.535
0.026
0.927
0.535
0.679
0.598
0.772
0.799
Error
0.4
0.191
0.154
0.4
0.222
0.14
0.451
0.144
Idle
0.4
0.133
0.207
0.4
0.273
0.2
0.603
0.19
Slow
Weighted Avg.
0.612
0.1
0.76
0.612
0.658
0.538
0.748
0.644
Table 7.11: Model evaluation - Detailed Accuracy By Class
down, error or idle. In case of idle means it is not relevant to the system issue. As
previously stated the engine is currently being part of a KTP project to integrate it with
in a intelligent chatbot custom service platform to improve user’s communication and
ﬁrst level support. With emerging approaches to language analysis, it is expected to
be able to improve the accuracy of the engine by improving the personality traits and
emotions; this will be discussed in further detail in Section 9.4.
125


## Page 138


Chapter 8
Experimental Meta-Analysis
8.1
Introduction
As each experiment and model has been discussed and presented separately in the pre-
vious chapter, this chapter will give an overview of all ﬁndings and discussion. The
design of the experiments structure started by exploring the data with reference to the
objective of the research question, to investigate the associations and correlations of the
current dataset parameter.
8.2
Proﬁling Complex Online Interactions
The experiment indicates a strong correlation between the Openness to Experience traits
and the Accepted group and that agrees with the literature. Costa [71] and Srivast-
ava [164] described people with high Openness to Experience as wanting to learn and
explore new ideas, and creative in general, and that agrees with the outcome of the ex-
periment presented in Section 6.2 conducted in our dataset. However, the ﬁnal selection
and evaluation process in the scholarship system 1, had many other parameters such as
(Evaluator personality, language qualiﬁcations, academic background..etc) and that was
the main reason why the Openness to Experience was not selected as part of the ﬁnal
developed model. Also, that was the reason why the ﬁnal selection parameter was not
selected as part of the input to the model.
8.3
Mapping User Behaviour to System Stages
The experiment presented by dividing the usage of the system over stages to investigate
the changes of the personality traits over time, the outcome, suggested that Extraversion,
1The system used to extract the data
126


## Page 139


Agreeableness and Conscientiousness were statistically signiﬁcant in the an attempt to
calculate the probability of predicate the stage, the logistic regression model, successful
correctly classiﬁed 80.2% of the cases., which indicate the personality traits can play
a vital role in proﬁling the digital behaviour of a user in using the complex system.
Furthermore, as indicated in a study conducted by McCrae in 2002 [205], agrees with
the outcome of the experiment that there is no change of personality over time, however,
the experiment indicates a possibility to identify the personality of the user in the system
based on his/her sentiment.
8.4
Verifying Accuracy using the IBM Watson Tone Ana-
lyzer
IBM Watson was made available in 2014, to extract personality traits and emotions
from text (as initially discussed in Section 4.2.3), the output reported was encouraging
to use as part of the study, however, it was essential to verify the IBM Watson tool result
without current Java tool (see Section 5.5.1). The experiment presented in Section 5.8
was conducted to verify the result using current collected Big Five Questionnaire and
Emotions reported by users, two methods used to investigate the difference between
the two groups IBM Watson and Data collected from the Questionnaire, Independent
samples of t-test and The Mann-Whitney U test, both conﬁrmed that there is no signi-
ﬁcant statistical difference between both groups, therefore, in further experiments IBM
Watson has been used as a tool to extract personality traits and emotions.
8.5
Personality Traits and Temporal Behaviour
As per our review of the literature in Section 2.6, there are two commonly used ap-
proaches to capture emotions Emotions Lexicon and using temporal behaviour. The
experiment presented in Section 6.4.2 suggested a moderate correlation between Neur-
oticism, self control and well being. Well being has a moderate correlation to agreeable-
ness and conscientiousness. Furthermore, the experiment presented in Section 6.4.3 also
suggest a moderate correlation between fear and Conscientiousness,Neuroticism, and
moderate positive correlation between joy and Conscientiousness, Neuroticism. How-
ever, it was decided to move forward with the Emotions Lexicon approach as the main
source of extracting emotions from the text as demonstrated in the literature in Sec-
tion 4.2.3, the main source of data as part of this study is in the form of interactive text.
The temporal behaviour experiment in Section 6.4.2 had to be conducted to compare
between both approaches in case there is a signiﬁcation statistical correlation, and how-
ever, since both reported reasonably same consistent result, then it is decided to move
forward with basic emotions.
127


## Page 140


8.6
Mapping User Behaviour to System Stages
The previous experiment reported an encouraging result to in the association between
sentiment values and the “big ﬁve” personality traits. The classiﬁer accurately identiﬁes
80.2% of the cases (See the section: Section 6.3), which contributes to the understand
more about user’s behaviour in the system. Therefore, it was essential to extend the
experiment to include Emotions lexicon approach to investigate a further association.
The Ordinal Regression suggested used to investigate further association, because of
the continues variables and dependent variable the Stage ID. The disgust and sadness
emotion had a statistically signiﬁcant effect on the performance of the classiﬁer. Mul-
tinomial Regression has been used to verify the output of previous of analysis, and it
reported the variables Disgust, Sadness and Conscientiousness has a signiﬁcant overall
effect on the dependent Stage ID2 The suggested output from this experiments shows a
good potential towards including other forms of system behaviour (I.e, server status).
8.7
Investigating Behavioural and Emotional Change
In light of building a conceptual framework to improve user experience and computer
system architecture design, the previous ﬂow of experiment demonstrated written text
reﬂects more than words agreeing with the literature [255], emotions captured cor-
relate with the activity of the user in the system (see Section 6.5). Moving towards
developing a conceptual framework to predicate the system status based on user’s be-
haviour. It was suggested to integrate the system status idle, down with the personality
traits and emotions extracted as explain in the experiment presented in Section 6.6,
the output suggested a strong correlation in predicating the server status as follow-
ing personality traits Openness, Extraversion, Conscientiousness, and Neuroticism, and
from basic emotions Joy, Sadness, Anger and Disgust, and that conﬁrms the literature
founding as reported by Fast Funder in 2008, that it is possible to include cognitive
science in the process of identifying the digital identity of the users [106] and other
studies [139, 99, 184, 130, 183]. A model was built using Linear Discriminant Analysis
using the below-reported traits to predicate the system status idle, down, and with good
potential performance 75% accuracy evaluated using cross-validation.
8.8
Personality Traits vs. Emotions, Gender and Age
The literature suggested that gender and age, plays a vital role in personality traits
and emotions, according to Weisberg in his study published in 2011 and Donnellan in
2StageID: System divided two four stages to investigate the change of emotion in different system
stages.
128


## Page 141


2008. [347] [93], the ﬁndings of the experiment presented in Section 7.2, agrees with
the literature as the The above ﬁndings suggests that Gender and Age as controlled vari-
able improves the linear relationship between Big Five and Emotions variables specially
Conscientiousness, Neuroticism , Anger and Fear and improve strength of linear rela-
tionship between Extraversion and Anger, Disgust, Fear, Joy and Sadness. However, in
the feature selection process as presented in Section 6.7, the gender has been excluded
from the features as it is not possible to include a dichotomy variable part of neural
network.
8.9
Model Veriﬁcation: Observing Emotions in Real Time
The developed model conceptual framework produced an accuracy of 68.5% and evalu-
ated using a new dataset in the veriﬁcation process and produced an accuracy of 61.17%,
the numbers suggested a good start into continue researching in this direction to produce
better performance by investigating a different other ranges of parameters that can con-
tribute the the skeleton of the model, however, I believe the objective of this study is
met by producing a good model supported by literature review to towards proﬁling the
digital behaviour in the different system status.
8.10
Summary
We have summarised all of the experiments in order, based upon our robust design
methodology. Furthermore, the dataset used as part of this study was extracted from a
system that was not pre-deﬁned for this study. Therefore, the initial stage was a range
of exploratory statistics analysis applied to decided how to approach the data to achieve
the objectives. Moreover, the in-depth literature review supported the direction of the
methodology and identiﬁed the gap in the digital proﬁling of the user over a complex
system using the personality and emotions as the main fundamental parameters to build
the stricture of the experiments. The primary idea was to identify the features that may
have any association with the key objectives of the study. The nature of the EU Sys-
tem used here involves different parameters that may have a direct impact on the data,
for instance, the Final Selection parameters. It was important to investigate the impact
of this parameter in the behaviour of the system and the personality type. However,
the selection criteria and lack of enough data on the ﬁnal selection process prevented
the selection of this parameter, which moves to the future work plan. Further analysis
revealed that the “Big Five” personality traits Conscientiousness, Agreeableness and
Neuroticism and the emotions namely, Disgust, Joy and Sadness with the Age associate
together to build a model based on Random Forest Tree predict the server status with
accuracy of 68%. The real-time veriﬁcation process of the model conﬁrmed that model
129


## Page 142


accuracy with 61%. The accuracy provided at this stage is encouraging to investigate
further by expanding the parameters involved in the human-computer interactions life
cycle. However, the PMSys pilot version is currently integrated into a commercial in-
dustrial application to enhance the selection of responding in an intelligent agent and
chatbot-based service, and the output of this integration will be used as a stimulus for
further research and development activities. The following chapter will frame these
challenges through an overall project summary, well as the potential future work..
130


## Page 143


Chapter 9
Conclusions and Future Work
9.1
Main Conclusions
The increased usage – and wider impact – of social networking platforms on our daily
life has provided the motivation and foundation for developing a new conceptual model
and thus deeper insight for proﬁling the types of users using these platform. by un-
derstanding the personality and emotion raised while using the system. Leading to
signiﬁcation improvement in the architecture of the complex computer system not only
the design, but it is also delivering the information to the users.
Reﬂecting on my experience as a professional software engineer for more than ten
years, the motivation and underpinning rationale of this study was to provide more in-
sight into how to improve the user experience and the architecture design of complex
systems. It is always a challenge for the software developer to read how the system
developed will help the user and how the user will behave in a different stage. This
study provides the software developers and UX communities with a conceptual model
to answer this question based on cognitive science, how the user will behave in different
stages.
In this thesis, the work presented led to the development of a conceptual framework
for predicting system status based on personality traits and emotions captured from the
interactive text with reasonably good accuracy. The broad classiﬁcation of the literature
survey conducted as part of the thesis demonstrated a potential led to the categories pro-
posed for understanding gestures as a human interaction technique and was developed
to enable us to gain a more theoretical perspective on the ﬁeld of gesture interactions.
The experiments conducted during this research project has revealed encouraging
ﬁndings at the intersection of cognitive science, human-computer interaction, psycho-
linguistics and user experience. Exploring the dataset extracted from the system triggered
the ﬂow of the experiment suggested in this study coupled with the literature. The lit-
erature supported that the emotions are dynamic factors were it could affect events and
131


## Page 144


surrounding environments; researchers suggested that the weather can have a posit-
ive/negative impact on the emotions of the person. A recent study revealed the weather
has a direct impact on people emotions; this is because the weather is part of the daily
life routine. The structure of this experiment built on this bases, as the computer/mobile
is currently part of our daily-life routing. It is crucial to investigate the relationship
between the emotions and the digital behaviour of the user, the ﬁndings suggested from
the experiments conducted is there is a very positive relationship between personality
traits of the users and the emotions raised in the different stages during the usage of
the system. Sentiment analysis has been used to identify the association between the
personality of the user and the change in sentiment in different stages in using the sys-
tem and was found to have a strong statically correlation, which led to expanding the
investigation to include more emotion variables. Another objective is to investigate the
personality and motions association as part of this study. The ﬁndings revealed that
there is a moderate correlation between personality traits and emotions, for instance,
people with high well being more likely to have agreeableness and conscientiousness.
Furthermore, the literature suggested that age and gender correlates with the personality
and emotions of people with a strong correlation and that was conﬁrmed by the ﬁnd-
ings and included in the ﬁnal produced model. The suggested conceptual model shows
that it is possible to proﬁle the digital behaviour of the user to the usage of the system.
Furthermore, the proposed model produced to demonstrate that the system status raises
emotions of the users to the personality type, gaining such information would beneﬁt the
software development community to take into account how different user with different
personality will behave in different system status.
9.2
Limitations
This study involves extracting data from different sources, Facebook, EU Scholarship
system, Help desk and the Veriﬁcation tool; extracting the data from these sources had
various challenges. Facebook constantly updates its API and permission model, mak-
ing it hard for researchers to harvest data for research purposes, these changes and re-
strictions affected this study to explore more parameters from the user’s proﬁle. It is
expected to be harder next upcoming years especially with the major data breach occurs
in March 2018, involves 50 million users, causing Facebook to act accordingly and add
more restriction and changes to extract data from Facebook even with user’s consent.
One more challenge was the EU Scholarship system was developed in-house with not
enough documentation of the ﬂow of the data or database structure to investigate further
interactions and parameters to include it in the model. Furthermore, the system did not
include Login using Facebook[178] developed by EU team, therefore, it was essential
to develop a matching algorithm as explained on section 5.7, however, the output of the
matching algorithm led to excluding of 35% of the available data set. Limitation of the
132


## Page 145


Computer system status to idle, down, slow and error due to the lack of documentation
to the EU Scholarship System and there was no pre-deﬁned installed plugin to monitor
the user’s behaviour, which limited the system’s parameters as part of the engine.
9.3
Commercialisation
Further to the peer-reviewed publications presented in Section 1.3, aspects of this re-
search (and thus the PMSys system) is currently being commercialised as part of a two-
year Innovate UK-funded Knowledge Transfer Partnership (KTP) project to apply the
research in industry with a company based in Cardiff focusing on developing intelligent
chatbot technologies for customer service. The proposed model is currently being integ-
rated into the main chatbot engine to enhance the selection of the statements based on
the user’s mood and provide the agent with a possible system issue based on the user’s
digital behaviour. The company offers the chatbot services to various industry and one
of the common requirements is to handle the technical inquiries and integrate and as the
model is suggested to improve the user experience and usability it can save some time
for the ﬁrst line support by producing the potential problem with the user with an option
for the agent to manually override the conversation and take over.
9.4
Future Work
The last ﬁve years of research for this project has opened up a wide range potential future
research areas, especially using our model and the PMSys system to further explore how
personality traits and emotions can play a signiﬁcant role in software development and
user experience while using a complex system. These future work themes are as follows:
Exploring other software environments: The output model was built in a dataset re-
trieved from a web complex system, it is suggested to integrate to another software
environment to explore the change in emotions in different system status, such as
ofﬂine applications, mobile applications, tablet applications, etc.
New and larger datasets: The recent events occurs regarding Facebook, suggested to
explore other social networks (e.g. Twitter, LinkedIn) to extract a new dataset,
number of companies are using Twitter as a main context of the communication
between their customers and commonly used to report technical issues, Twitter of-
fers a rich API [198] makes it a productive environment for researchers to collect
and analyse large-scale longitudinal datasets [5, 6, 4]. Furthermore, since Twitter
is largely an open, public platform the data can be used in investigating further
and verifying the model outcome and improving the accuracy of the model.
133


## Page 146


Topic modelling: A number of research studies suggested a strong association between
personality traits, emotions and topics [11, 15]. In upcoming studies, it is sugges-
ted to integrate topic classiﬁcation as one more parameter to verify the potential
association.
Focus experiments: This study were focused on data collected from Facebook and
EU System, with some limitation to the type of the data collected as explained
previously, to continue working in same direction it is important to collect data in
more controlled environment to expand the input variables (i.e, facial expression,
video observation, pre-deﬁned system to monitor behaviour, eye tracker).
Deeper analysis of personality traits throgh emotion extraction with emerging NLP
tools and technologies, different companies are producing a NLP tool to extract
personality traits and emotions from text. It is suggested to track the state-of-art
tools and verify the efﬁcient to use it in further analysis. Furthermore, extracting
emotions emerged to include facial expression with high efﬁcient quality tools
(e.g. Affectiva1, Emotient2 and EmoVu3).
Expanding the system status functionality: as the current study suggested only four
status of the system idle, down, slow and error, it is planned to explore further
sub types for each main classiﬁcation, such as Error 404 not found, Internal 500
server error.
Investigating the ﬁnal selection parameter: , as discussed in Section 8.10, based on
the outcome analysis from the proﬁling complex experiment 6.2, it is sugges-
ted to investigate the process of selection further to understand more about the
personality of each group.
1Affectiva: is a solution for massive scale engagement detection. Offer SDKs and APIs for mobile
application, and provide an analytics API to track expressions over time - http://www.affectiva.com/
2Emotient: is an ad campaign that tracks attention, engagement, and sentiment from viewers. The
RESTful Emotient Web API can be integrated into application - http://emotient.com/
3EmoVu: is a facial detection products incorporate machine learning and micro expression detection.
Provides a very powerful SDK, Mobile SDK, and an API for application integration - http://emovu.com/e/
134


## Page 147


Bibliography
[1] L. A. Adamic and E. Adar. Friends and neighbors on the Web. Social Networks,
25(3):211–230, 2003.
[2] M. Adya and F. Collopy. How effective are neural networks at forecasting and
prediction? a review and evaluation. Journal of Forecasting, 17(5-6):481–495,
1998.
[3] F. Alam, E. A. Stepanov, and G. Riccardi. Personality Traits Recognition on
Social Network - Facebook. Seventh international AAAI Conference on Weblogs
and Social Media (ICWSM), pages 5–8, 2013.
[4] N. Albishry, T. Crick, T. Fagade, and T. Tryfonas. Popularity and Geospatial
Spread of Trends on Twitter: A Middle Eastern Case Study. In Computational
Collective Intelligence, volume 11055 of Lecture Notes in Computer Science,
pages 167–177. Springer, 2018.
[5] N. Albishry, T. Crick, and T. Tryfonas. “Come Together!”: Interactions of Lan-
guage Networks and Multilingual Communities on Twitter. In Computational
Collective Intelligence, volume 10449 of Lecture Notes in Computer Science.
Springer, 2017.
[6] N. Albishry, T. Crick, T. Tryfonas, and T. Fagade. An Evaluation of Performance
and Competition in Customer Services on Twitter: A UK Telecoms Case Study.
In Companion of The Web Conference 2018, Social Sensing and Enterprise Intel-
ligence: Towards a Smart Enterprise Transformation, 2018.
[7] J. F. Allen. Natural language processing. Encyclopedia of Computer Science,
pages 1218–1222, 2003.
[8] G. W. Allport.
Personality: A Psychological Interpretation.
Jenry Holt and
Company, 1937.
[9] G. W. Allport and H. S. Odbert. Trait-names: A psycho-lexical study. Psycholo-
gical Monographs, 47:171–220, 1936.
135


## Page 148


[10] E. Alpaydin. Introduction to machine learning. MIT Press, 2014.
[11] E. Andr´e, M. Klesen, P. Gebhard, S. Allen, and T. Rist. Integrating models of
personality and emotions into lifelike characters. In Affective interactions, pages
150–165. Springer, 2000.
[12] M. Andreessen. Why software is eating the world. The Wall Street Journal,
2011-08. Available online: http://online.wsj.com/news/articles/
SB10001424053111903480904576512250915629460.
[13] D. S. Appling, E. J. Briscoe, H. Hayes, and R. L. Mappus. Towards automated
personality identiﬁcation using speech acts. In AAAI Workshop - Technical Re-
port, volume WS-13-01, pages 10–13, 2013.
[14] S. Arthur, T. Crick, and J. Hayward.
The ICT Steering Group’s Re-
port
to
the
Welsh Government.
Technical report,
September 2013.
https://beta.gov.wales/future-computer-science-and-
information-technology-schools-ict-steering-group-
report.
[15] E. J. Austin, T. C. Dore, and K. M. ODonovan.
Associations of personality
and emotional intelligence with display rule perceptions and emotional labour.
Personality and Individual Differences, 44(3):679–688, 2008.
[16] M. D. Back, J. M. Stopfer, S. Vazire, S. Gaddis, S. C. Schmukle, B. Egloff, and
S. D. Gosling. Facebook proﬁles reﬂect actual personality, not self-idealization.
Psychological Science, 21(3):372–374, 2010.
[17] R. M. Bagby, M. B. Marshall, and S. Georgiades. Dimensional personality traits
and the prediction of DSM-IV personality disorder symptom counts in a nonclin-
ical sample. Journal of Personality Disorders, 19(1):53–67, 2005.
[18] A. Bandura. Social learning theory. Prentice-Hall series in social learning theory.
Prentice Hall, 1977.
[19] M. R. Barrick and M. K. Mount. The Big Five Personality Dimensions and Job
Performace: A Meta-Analysis. Personnel Psychology, 44(1):1–26, 1991.
[20] A. Bayaga. Multinomial logistic regression: Usage and application in risk ana-
lysis. Context, 5(2):288–297, 2001.
[21] G. Beauchamp, A. Joyce-Gibbons, J. McNaughton, N. Young, and T. Crick.
Exploring Synchronous, Remote Collaborative Interaction between Learners us-
ing Multi-Touch Tables and Skype to Solve History Mysteries in UK Primary
Schools. British Journal of Educational Technology, 2019.
136


## Page 149


[22] G. Beigi, X. Hu, R. Maciejewski, and H. Liu. An overview of sentiment analysis
in social media and its applications in disaster relief. In Studies in Computa-
tional Intelligence, volume 639, pages 313–340. Springer International Publish-
ing, 2016.
[23] P. Bergman, D. Vastfjall, N. Fransson, and A. Skold. Emotion and meaning in
interpretation of sound sources. Journal of the Acoustical Society of America,
123(5):3567, 2008.
[24] A. Berson. Client-Server Architecture. McGraw-Hill, 1992.
[25] A. Betella and P. F. Verschure. The affective slider: A digital self-assessment
scale for the measurement of human emotions. PLoS ONE, 11(2), 2016.
[26] S. K. Bhavnani and B. E. John. The strategic use of complex computer systems.
HumanComputer Interaction, 15(2-3):107–137, 2000.
[27] J. Biel and D. Gatica-Perez. The YouTube Lens: Crowdsourced Personality Im-
pressions and Audiovisual Analysis of Vlogs. IEEE Transactions on Multimedia,
15(1):41–55, 2012.
[28] B. Blamey, T. Crick, and G. Oatley. R U :-) or :-( ? Character- vs. Word-Gram
Feature Selection for Sentiment Classiﬁcation of OSN Corpora. In Research and
Development in Intelligent Systems XXIX, pages 207–212. Springer, 2012.
[29] B. Blamey, T. Crick, and G. Oatley. ‘The First Day of Summer’: Parsing Tem-
poral Expressions with Distributed Semantics. In Research and Development in
Intelligent Systems XXX, pages 389–402. Springer, 2013.
[30] D. M. Blei, A. Y. Ng, and M. I. Jordan. Latent dirichlet allocation. Journal of
machine Learning research, 3:993–1022, 2003.
[31] G. S. Blum. Psychoanalytic theories of personality. McGraw-Hill, 1953.
[32] J. E. Bono and T. A. Judge. Personality and transformational and transactional
leadership: A meta-analysis. Journal of Applied Psychology, 89(5):901–910,
2004.
[33] A. L. Boulesteix, S. Janitza, J. Kruppa, and I. R. Knig. Overview of random forest
methodology and practical guidance with emphasis on computational biology
and bioinformatics. Wiley Interdisciplinary Reviews: Data Mining and Know-
ledge Discovery, 2(6):493–507, 2012.
[34] G. E. P. Box and P. W. Tidwell. Transformation of the Independent Variables.
Technometrics, 4(4):531–550, 1962.
137


## Page 150


[35] G. J. Boyle. Critique of the ﬁve-factor model of personality. The SAGE handbook
of personality theory and assessment, 1:295–312, 2008.
[36] M. M. Bradley and P. J. Lang. Measuring emotion: the self-assessment manikin
and the semantic differential. Journal of behavior therapy and experimental psy-
chiatry, 25(1):49–59, 1994-03.
[37] M. Brain, T. Crick, M. De Vos, and J. Fitch. TOAST: Applying Answer Set
Programming to Superoptimisation.
In Logic Programming, volume 4079 of
Lecture Notes in Computer Science, pages 270–284. Springer, 2006.
[38] E. Breck and C. Cardie. Identifying expressions of opinion. Proceedings of the
20th International Joint Conference on Artiﬁcial Intelligence, 2007.
[39] L. Breiman. Random forests. Machine Learning, 45(1):5–32, 2001.
[40] L. Breiman. The 2002 wald memorial lectures population theory for boosting
ensembles. Annals of Statistics, 32(1):1–11, 2004.
[41] W. G. Broehl and V. E. McGee. Content analysis in psychohistory: a study of
three lieutenants in the indian mutiny, 1857-58. The Journal of psychohistory, 8
3:281–306, 1981.
[42] N. C. C. Brown, S. Sentance, T. Crick, and S. Humphreys. Restart: The Re-
surgence of Computer Science in UK Schools. ACM Transactions on Computer
Science Education, 14(2):1–22, 2014.
[43] M. Brundage, S. Avin, J. Clark, H. Toner, P. Eckersley, B. Garﬁnkel, A. Dafoe,
P. Scharre, T. Zeitzoff, B. Filar, H. Anderson, H. Roff, G. C. Allen, J. Steinhardt,
C. Flynn, S. higeartaigh, S. Beard, H. Belﬁeld, S. Farquhar, C. Lyle, Rebecca,
Crootof, O. Evans, M. Page, J. Bryson, R. Yampolskiy, and D. Amodei. The
Malicious Use of Artiﬁcial Intelligence: Forecasting, Prevention, and Mitigation.
Technical report, February 2018. https://maliciousaireport.com/.
[44] E. Brynjolfsson, D. Rock, and C. Syverson. The Economics of Artiﬁcial Intel-
ligence: An Agenda, chapter Artiﬁcial Intelligence and the Modern Productivity
Paradox: A Clash of Expectations and Statistics. National Bureau of Economic
Research, 2018.
[45] P. Burnap, R. Gibson, L. Sloan, R. Southern, and M. Williams. 140 characters
to victory?: Using Twitter to predict the UK 2015 General Election. Electoral
Studies, 41:230–233, 2016.
138


## Page 151


[46] P. Burnap and M. L. Williams. Cyber Hate Speech on Twitter: An Application of
Machine Classiﬁcation and Statistical Modeling for Policy and Decision Making.
Policy & Internet, 7(2):223–242, 2015.
[47] P. Burnap, M. L. Williams, L. Sloan, O. Rana, W. Housley, A. Edwards,
V. Knight, R. Procter, and A. Voss. Tweeting the terror: modelling the social
media reaction to the Woolwich terrorist attack. Social Network Analysis and
Mining, 4(206), 2014.
[48] M. Cabanac. What is emotion? Behavioural Processes, 60(2):69–83, 2002-10.
[49] J. M. Cahill and J. Polich. P300, probability, and introverted/extroverted person-
ality types. Biological Psychology, 33(1):23–35, 1992.
[50] A. C. Calderon and T. Crick. Using Interface Design to Develop Computational
Thinking Skills. In Proceedings of 10th International Workshop in Primary and
Secondary Computing Education (WiPSCE 2015). ACM, 2015.
[51] S. K. Card. The psychology of human-computer interaction. CRC Press, 2017.
[52] M. Carr and T. Crick. The Problem of the P3: Public-Private Partnerships in
National Cyber Security Strategies. In Proceedings of International Conference
on Cyber Security for Sustainable Society, 2015. ISSN: 2052-8604.
[53] P. L. Carrell, M. S. Prince, and G. G. Astika. Personality types and language
learning in an EFL context, 1996.
[54] P. Z. Carroll J.M, Dennis Galletta.
Soft versus hard: The essential tension.
In Human-Computer Interaction in Management Information Systems. M. E.
Sharpe, Inc, 2006.
[55] J. Cassell.
Negotiated collusion: Modeling social language and its relation-
ship effects in intelligent agents. User Modeling and User-Adapted Interaction,
13(1/2):89–132, 2003.
[56] R. Castro and J. W. Grossman. Famous trails to Paul Erds. The Mathematical
Intelligencer, 21(3):51–53, 1999.
[57] H. E. Cattell and A. D. Mead. The sixteen personality factor questionnaire (16pf).
In The SAGE Handbook of Personality Theory and Assessment: Volume 2 - Per-
sonality Measurement and Testing, pages 135–159. SAGE Publications Ltd; 1
edition (24 Jun. 2008), 2008.
[58] R. B. Cattell. The description of personality: basic traits resolved into clusters.
The Journal of Abnormal and Social Psychology, 38(4):476–506, 1943.
139


## Page 152


[59] F. Celli, F. Pianesi, D. Stillwell, and M. Kosinski. Workshop on Computational
Personality Recognition : Shared Task. Proceedings of the Workshop on Person-
ality Recognition, 2006:2–5, 2013.
[60] X. Chen, Y. Pan, and B. Guo.
The inﬂuence of personality traits and social
networks on the self-disclosure behavior of social network site users. Internet
Research, 26(3):566–586, jun 2016.
[61] G. G. Chowdhury. Natural language processing. Annual Review of Information
Science and Technology, 37(1):51–89, 2005.
[62] J. M. Cisler, B. O. Olatunji, J. M. Lohr, and N. L. Williams. Attentional bias dif-
ferences between fear and disgust: Implications for the role of disgust in disgust-
related anxiety disorders. Cognition and Emotion, 23(4):675–687, 2009.
[63] A. D. Cohen. Second Language Learning and Use Strategies: Clarifying the
Issues. Technical report, Center for Advanced Research on Language Acquisition
University of Minnesota, Minneapolis, USA, July 1996.
[64] J. Cohen, P. Cohen, S. G. West, and L. Aiken. Applied Multiple Regression /
Correlation Analysis for the Behavioral Sciences. Routledge, 2003.
[65] P. R. Cohen and E. A. Feigenbaum.
The handbook of artiﬁcial intelligence,
volume 3. Butterworth-Heinemann, 2014.
[66] P. Cooper, T. Crick, T. Tryfonas, and G. Oikonomou. Whole-Life Environmental
Impacts of ICT Use. In Proceedings of IEEE International Workshop on Green
Standardizations for ICT and Relevant Technologies (GSICT 2015). IEEE, 2015.
[67] P. Cooper, T. Tryfonas, T. Crick, and A. Marsh. Electric Vehicles As-a-Service:
Exploring the ‘Tri-Opt’ of Novel Private Transport Business Models. Journal of
Urban Technology, 26(1):3556, 2019.
[68] V. Cosenza. Social media ROI: seconda edizione aggiornata. Apogeo Editore,
2014.
[69] E. Cosgrave, T. Tryfonas, and T. Crick. The Smart City from a Public Value
Perspective. In Proceedings of 2nd International Conference on ICT for Sustain-
ability (ICT4S), 2014.
[70] P. T. Costa and R. R. McCrae. Professional manual: revised neo personality
inventory (neo-pi-r) and neo ﬁve-factor inventory (neo-fﬁ). Odessa FL Psycho-
logical Assessment Resources, 3:101, 1992.
140


## Page 153


[71] P. T. Costa and R. R. McCrae. Revised NEO Personality Inventory (NEO-PI-R)
and NEO Five-Factor Inventory (NEO-FFI) Manual. Psychological Assessment
Resources, 1992.
[72] B. Cowley, D. Charles, M. Black, and R. Hickey. Real-time rule-based classi-
ﬁcation of player types in computer games. User Modelling and User-Adapted
Interaction, 23(5):489–526, 2013.
[73] T. Crick. Superoptimisation: Provably Optimal Code Generation using Answer
Set Programming. PhD thesis, Department of Computer Science, University of
Bath, August 2009. http://opus.bath.ac.uk/20352.
[74] T. Crick, M. De Vos, M. Brain, and J. Fitch. Generating Optimal Code using An-
swer Set Programming. In Logic Programming and Nonmonotonic Reasoning,
volume 5753 of Lecture Notes in Computer Science, pages 554–559. Springer,
2009.
[75] T. Crick, P. Dunning, H. Kim, and J. Padget. Engineering Design Optimization
using Services and Workﬂows. Philosophical Transactions of the Royal Society
A, 367(1898):2741–2751, 2009.
[76] T. Crick, B. A. Hall, and S. Ishtiaq. “Can I Implement Your Algorithm?”: A
Model for Reproducible Research Software. In 2nd International Workshop on
Sustainable Software for Science: Practice and Experiences (WSSSPE2), 2014.
[77] T. Crick, B. A. Hall, and S. Ishtiaq. Reproducibility in Research: Systems, Infra-
structure and Culture. Journal of Open Research Software, 5(1), 2017.
[78] T. Crick, B. A. Hall, S. Ishtiaq, and K. Takeda. “Share and Enjoy”: Publishing
Useful and Usable Scientiﬁc Models. In Proceedings of 7th IEEE/ACM Interna-
tional Conference on Utility and Cloud Computing, pages 957–961. IEEE, 2014.
[79] T. Crick, J. Mateos-Garcia, H. Bakhshi, and S. Westlake. Innovation Policy-
Making in the Big Data Era.
In Data for Policy 2015, 2015.
https:
//cronfa.swan.ac.uk/Record/cronfa43755.
[80] W. Cui, L. Huang, L. Liang, and J. Li.
The Research of PHP Development
Framework Based on MVC Pattern. In 2009 Fourth International Conference on
Computer Sciences and Convergence Information Technology, pages 947–949.
IEEE, 2009.
[81] D. R. Cutler, T. C. Edwards, K. H. Beard, A. Cutler, K. T. Hess, J. Gibson, and
J. J. Lawler. Random forests for classiﬁcation in ecology. Ecology, 88(11):2783–
2792, 2007-10.
141


## Page 154


[82] A. D’Andrea, F. Ferri, P. Grifoni, and T. Guzzo. Approaches, tools and applica-
tions for sentiment analysis implementation. International Journal of Computer
Applications, 125(3):26–33, 2015.
[83] G. L. Dannenbring. The effect of computer response time on user performance
and satisfaction: A preliminary investigation. Behavior Research Methods &
Instrumentation, 15(2):213–216, 1983.
[84] C. Darwin. The expression of the emotions in man and animals. John Marry,
page 374, 1872.
[85] J. H. Davenport, T. Crick, A. Hayes, and R. Hourizi. The Institute of Coding:
Addressing the UK Digital Skills Crisis. In Proceedings of Computing Education
Practice, 2019.
[86] M. De Vos, O. Cliffe, R. Watson, T. Crick, J. Padget, J. Needham, and M. Brain.
T-LAIMA: Answer Set Programming for Modelling Agents with Trust. In Pro-
ceedings of the 3rd European Workshop on Multi-Agent Systems (EUMAS 2005),
2005.
[87] M. De Vos, T. Crick, J. Padget, M. Brain, O. Cliffe, and J. Needham. LAIMA:
A Multi-agent Platform Using Ordered Choice Logic Programming. In Declar-
ative Agent Languages and Technologies III, volume 3904 of Lecture Notes in
Computer Science, pages 72–88. Springer, 2006.
[88] M. Del Vicario, F. Z. G. Caldarelli, A. Scala, and W. Quattrociocchi. Mapping
social dynamics on Facebook: The Brexit debate. Social Networks, 50:6–16,
2017.
[89] J. M. Digman. Five robust trait dimensions: Development, stability, and utility.
Journal of Personality, 57(2):195–214, 1989-06.
[90] A. Dix. Human-Computer Interaction. In Encyclopedia of Database Systems,
pages 1327–1331. Springer, 2009.
[91] E. Domahidi, R. Festl, and T. Quandt. To dwell among gamers: Investigating
the relationship between social online game use and gaming-related friendships.
Computers in Human Behavior, 35:107–115, 2014-06.
[92] M. Donnellan, R. D. Conger, and C. M. Bryant. The big ﬁve and enduring mar-
riages. Journal of Research in Personality, 38(5):481–504, 2004.
[93] M. B. Donnellan and R. E. Lucas. Age differences in the big ﬁve across the life
span: Evidence from two national samples. Psychology and Aging, 23(3):558–
566, 2008.
142


## Page 155


[94] Z. D¨ornyei and P. Skehan. Individual differences in second language learning. In
The Handbook of Second Language Acquisition, pages 589–630. John Wiley &
Sons, 2003.
[95] S. E. Duclos, J. D. Laird, E. Schneider, M. Sexter, and E. Al. Emotion-speciﬁc
effects of facial expressions and postures on emotional experience. Journal of
Personality and Social Psychology, 57(1):100–108, 1989.
[96] R. Eberhart, P. Simpson, and R. Dobbins. Computational intelligence PC tools.
Academic Press Professional, Inc., 1996.
[97] R. C. Eberhart and Y. Shi. chapter two - computational intelligence. In R. C.
Eberhart and Y. Shi, editors, Computational Intelligence, pages 17 – 38. Morgan
Kaufmann, Burlington, 2007.
[98] P. Ekman. Expression and the Nature of Emotion. In K. Scherer and P. Ekman,
editors, Approaches to Emotion, pages 319–343. Lawrence Erlbaum, 1984.
[99] P. Ekman, W. V. Friesen, and P. Ellsworth.
Emotion in the human face:
Guidelines for research and an integration of ﬁndings. Elsevier, 2013.
[100] A. P. Engelbrecht. Fundamentals of computational swarm intelligence. John
Wiley & Sons, 2006.
[101] F. Enos, S. Benus, R. L. Cautin, M. Graciarena, J. Hirschberg, and E. Shriberg.
Personality factors in human deception detection: Comparing human to machine
performance. Proceedings of the Annual Conference of the International Speech
Communication Association, INTERSPEECH, 2:813–816, 2006.
[102] S. Epstein. Trait theory as personality theory: Can a part be as great as the whole?
Psychological Inquiry, 5(2):120–122, 1994.
[103] H. Eysenck. Dimensions of personality: 16, 5 or 3? Criteria for a taxonomic
paradigm. Personality and Individual Differences, 12(8):773–790, 1991-01.
[104] Facebook.
Newsroom.
https://newsroom.fb.com/company-info/,
2018.
[105] W. R. D. Fairbairn. Psychoanalytic Studies of the Personality. Routledge 1 edi-
tion (1 Sept. 1994), 2001.
[106] L. A. Fast and D. C. Funder.
Personality as manifest in word use: Correla-
tions with self-report, acquaintance report, and behavior. J. Pers. Soc. Psychol.,
94(2):334–346, 2008.
143


## Page 156


[107] K. Fawagreh, M. M. Gaber, and E. Elyan.
Random forests: from early de-
velopments to recent advancements. Systems Science & Control Engineering,
2(1):602–609, 2014-12.
[108] R. Fielding, J. Gettys, J. Mogul, H. Frystyk, L. Masinter, P. Leach, and
T. Berners-Lee. RFC2616 – Hypertext Transfer Protocol (HTTP/1.1). Internet
Engineering Task Force, pages 1–114, 1999.
[109] A. J. Figueredo and J. P. Rushton.
Evidence for shared genetic dominance
between the general factor of personality, mental and physical health, and life
history traits. Twin research and human genetics : the ofﬁcial journal of the
International Society for Twin Studies, 12(6):555–563, 2009.
[110] D. Flanagan. JavaScript: the deﬁnitive guide. ” O’Reilly Media, Inc.”, 2006.
[111] H.-C. Friederich, T. Brockmeyer, B. Wild, G. Resmark, M. de Zwaan, A. Dinkel,
S. Herpertz, M. Burgmer, B. L¨owe, S. Tagay, E. Rothermund, A. Zeeck, S. Zipfel,
and W. Herzog. Emotional Expression Predicts Treatment Outcome in Focal Psy-
chodynamic and Cognitive Behavioural Therapy for Anorexia Nervosa: Findings
from the ANTOP Study. Psychotherapy and Psychosomatics, 86(2):108–110,
2017.
[112] J. Fulcher. Computational intelligence: an introduction. In Computational intel-
ligence: a compendium, pages 3–78. Springer, 2008.
[113] D. C. Funder and C. D. Sneed. Behavioral manifestations of personality: An
ecological approach to judgmental accuracy. Journal of Personality and Social
Psychology, 64(3):479–490, 1993.
[114] A. Furnham, C. J. Jackson, and T. Miller. Personality, learning style and work
performance. Personality and Individual Differences, 27(6):1113–1122, 1999.
[115] A. Furnham and J. Mitchell.
Personality, needs, social skills and academic
achievement: A longitudinal study.
Personality and Individual Differences,
12(10):1067–1073, 1991-01.
[116] F. Galton. Inquiries Into Human Faculty and Its Development. JM Dent & Co.,
1907.
[117] W. P. Galuten A., Monica S. Method and system for handling errors in a distrib-
uted computer system, US Patent No. US6918059, 2005.
[118] D. Gao, Y.-X. Zhang, and Y.-H. Zhao. Random forest algorithm for classiﬁcation
of multiwavelength data. Research in Astronomy and Astrophysics, 9(2):220–
226, 2009-02.
144


## Page 157


[119] A. Garnham. Artiﬁcial intelligence: An introduction. Routledge, 2017.
[120] H. Giles and W. Robinson. Handbook of language and social psychology. Wiley,
1990.
[121] A. Ginige and S. Murugesan. Web engineering: An introduction. IEEE multime-
dia, 8(1):14–18, 2001.
[122] J. Golbeck. Computing and applying trust in web-based social networks. PhD
thesis, University of Maryland, 2005.
[123] J. Golbeck, C. Robles, M. Edmondson, and K. Turner. Predicting personality
from twitter. In Proceedings - 2011 IEEE International Conference on Privacy,
Security, Risk and Trust and IEEE International Conference on Social Comput-
ing, PASSAT/SocialCom 2011, pages 149–156, 2011.
[124] L. Goldberg. An alternative “description of personality”: The big ﬁve factor
structure. Journal of Personality and Social Psychology, 59(6):1216–1229, 1990.
[125] L. R. Goldberg. Language and individual di erences: The search for universals
in personality lexicons. Journal of Personality and Social Psychology, 1981.
[126] L. R. Goldberg. An alternative ”description of personality”: The big-ﬁve factor
structure. Journal of Personality and Social Psychology, 1991.
[127] S. D. Gosling, P. J. Rentfrow, and W. B. Swann. A very brief measure of the big-
ﬁve personality domains. Journal of Research in Personality, 37(6):504–528,
2003.
[128] S. D. Gosling, P. J. Rentfrow, and W. B. Swann Jr. A very brief measure of the
big-ﬁve personality domains. Journal of Research in personality, 37(6):504–528,
2003.
[129] L. A. Gottschalk. Research using the gottschalk-gleser content analysis scales
in english since 1969. In Content Analysis of Verbal Behavior, pages 29–46.
Springer Berlin Heidelberg, 1986.
[130] L. Gou, M. X. Zhou, and H. Yang. Knowme and shareme: understanding auto-
matically discovered personality traits from social media and user sharing pref-
erences. In Proceedings of the SIGCHI Conference on Human Factors in Com-
puting Systems, pages 955–964. ACM, 2014.
[131] M. Graciarena, E. Shriberg, A. Stolcke, F. Enos, J. Hirschberg, and S. Kajarekar.
Combining prosodic lexical and cepstral systems for deceptive speech detec-
tion. In 2006 IEEE International Conference on Acoustics Speed and Signal
Processing Proceedings, volume 1, pages I–1033–I–1036. IEEE, 2006.
145


## Page 158


[132] J. Gray. Why do computers stop and what can be done about it? In Symposium
on reliability in distributed software and database systems, pages 3–12, 1986.
[133] P. E. Grifﬁths. What emotions really are: The problem of psychological categor-
ies. University of Chicago Press, 2008.
[134] D. Guide. Facebook API Developers Guide. Facebook, 2008.
[135] M. Gupta and N. Aggarwal. Classiﬁcation techniques analysis. National Confer-
ence on Computational Instrumentation, pages 128–131, 2010.
[136] R. H. and W. R. D. Fairbairn. Psychoanalytic studies of the personality. The
British Journal of Sociology, 4(1):108, 1953.
[137] T. G. Halle and K. E. Darling-Churchill. Review of measures of social and emo-
tional development. Journal of Applied Developmental Psychology, 45:8–18, jul
2016.
[138] S. Hampson. State of the art: Personality. Psychologist, 12(6):284–288, 1999.
[139] S. E. Hampson. Personality Processes: Mechanisms by Which Personality Traits
“Get Outside the Skin”. Annual Review of Psychology, 63(1):315–339, jan 2012.
[140] M. A. Hardy. Regression with dummy variables. Sage university paper series on
quantitative applications in the social sciences, pages 07–093, 1993.
[141] H. Harley. How do verbs get their names? denominal verbs, manner incorpor-
ation, and the ontology of verb roots in english. In The Syntax of Aspect, pages
42–64. University Press, 2005.
[142] V. Harris and M. Grenfell.
Language-learning Strategies: A Case for Cross-
curricular Collaboration. Language Awareness, 13(2):116–130, 2004.
[143] S. Harrison, D. Tatar, and P. Sengers. The three paradigms of HCI. In Alt. Chi.
Session at the SIGCHI Conference on Human Factors in Computing Systems,
pages 1–18, 2007.
[144] C. U. Heinrich and P. Borkenau. Deception and deception detection: The role of
cross-modal inconsistency. Journal of Personality, 66(5):687–712, 1998-10.
[145] T. Heninger and R. Rasmussen. Server-side scripting language and programming
tool, Oct. 22 2002. US Patent 6,470,349.
[146] M. Hibbeln, J. L. Jenkins, C. Schneider, J. S. Valacich, and M. Weinmann. How
is your user feeling? inferring emotion through human–computer interaction
devices. MIS Quarterly, 41(1), 2017.
146


## Page 159


[147] J. Hirschberg, S. Benus, J. M. Brenier, F. Enos, S. Friedman, S. Gilman, C. Gir,
M. Graciarena, A. Kathol, and L. Michaelis. Distinguishing deceptive from non-
deceptive speech. In In Proceedings of Interspeech2005 - Eurospeech, pages
1833–1836, 2005.
[148] C. Hofmeister, R. Nord, and D. Soni. Applied Software Architecture. Addison
Wesley, 2009.
[149] W. K. B. Hofstee. Intelligence and personality: Do they mix?
In t. Messick
and personality: Do they mix J M Collis S, editors, Intelligence and personality:
Bridging the gap in theory and measurement, pages 43–60. Lawrence Erlbaum
Associates Publishers, 2001.
[150] R. Hogan, G. J. Curphy, and J. Hogan. What we know about leadership: Effect-
iveness and personality. American psychologist, 49(6):493, 1994.
[151] R. Hogan and R. B. Kaiser. What we know about leadership. Review of General
Psychology, 9(2):169–180, 2005.
[152] H. Hogendoorn, T. A. Carlson, and F. A. J. Verstraten. The time course of attent-
ive tracking. Journal of Vision, 7(14):2, 2007-10.
[153] B. Hssina, A. Merbouha, H. Ezzikouri, and M. Erritali. A comparative study of
decision tree ID3 and C4.5. International Journal of Advanced Computer Science
and Applications, 4(2), 2014.
[154] D. Huber, H. Kaufmann, and M. Steinmann. The missing link: The innovation
gap. In Management for Professionals, pages 21–41. Springer International Pub-
lishing, 2017.
[155] G. Huysamen. Methodology for the social and behavioural sciences. Southern
Book Publishers, 1994.
[156] F. Iacobelli, A. J. Gill, S. Nowson, and J. Oberlander. Large scale personality
classiﬁcation of bloggers. In Proceedings of the 4th International Conference
on Affective Computing and Intelligent Interaction (ACII 2011), volume 6975 of
Lecture Notes in Computer Science, pages 568–577. Springer, 2011.
[157] IBM.
IBM Cloud Docs.
https://console.bluemix.net/docs/
services/tone-analyzer/science.html#the-science-
behind-the-service, 2018.
[158] O. Ichazo. Interviews with Oscar Ichazo. Arica Institute Press, 1982.
147


## Page 160


[159] D. Isac and C. Reiss. I-language: An introduction to linguistics as cognitive
science. Oxford University Press, 2013.
[160] C. E. Izard. Basic emotions, relations among emotions, and emotion cognition
relations. Psychological Review, 99(3):561–565, 1992.
[161] P. V. Jadhav and A. M. Shendkar. Application of regression analysis in numerous
times. International Journal of Science, Engineering and Technology Research
(IJSETR), 0(1):1002–1005, 2015.
[162] L. Jie. Language Learning Styles and Learning Strategies of Tertiary-Level Eng-
lish Learners in China. RELC Journal, 37(1):67–90, 2006.
[163] H. Jodai. An Introduction to Psycholinguistics. Technical report, The University
of Guilan, June 2011.
[164] O. P. John and S. Srivastava. The big ﬁve trait taxonomy: History, measurement,
and theoretical perspectives. Handbook of personality: Theory and research,
2(510):102–138, 1999.
[165] C. Jones. Patterns of large software systems: failure and success. Computer,
28(3):86–87, 1995.
[166] T. A. Judge, C. A. Higgins, C. J. Thoresen, and M. R. Barrick. The big ﬁve
personality traits, general mental ability, and career success across the life span.
Personnel Psychology, 52(3):621–652, 1999.
[167] C. Jung. Psychological Types: Collected Works of C.G. Jung, volume 6. Prin-
ceton University Press; 3rd ed., 1971.
[168] R. Kang, S. Brown, and S. Kiesler. Why do people seek anonymity on the inter-
net?: informing policy and design. In Proceedings of the SIGCHI Conference on
Human Factors in Computing Systems, pages 2657–2666, 2013.
[169] D. A. Karp. Speaking of sadness: Depression, disconnection, and the meanings
of illness. Oxford University Press, 2016.
[170] R. A. Kasschau. Psychology: Exploring Behavior. Prentice-Hall, 1980.
[171] M. Kendall. A new measure of rank correlation. Biometrika, 30(1-2):68–80,
1938.
[172] M. Kendall and J. D. Gibbons. Rank correlation methods. Edward Arnold, 1990.
[173] S. Kendall. Framing authority: Gender, face, and mitigation at a radio network.
Discourse & Society, 15(1):55–79, 2004-01.
148


## Page 161


[174] I. O. Kenneth and B. M. Matthew. Investigation of William H. Sheldon’s Con-
stitutional Theory of Personality: A Case Study of the University of the Gambia.
Mediterranean Journal of Social Sciences, aug 2013.
[175] J. O. Kephart and W. E. Walsh. An artiﬁcial intelligence perspective on auto-
nomic computing policies. In Proceedings of 5th IEEE International Workshop
on Policies for Distributed Systems and Networks (POLICY 2004), pages 3–12.
IEEE, 2004.
[176] S. M. Kim, A. Valitutti, and R. a. Calvo. Evaluation of unsupervised emotion
models to textual affect recognition. Proceedings of the NAACL HLT 2010 Work-
shop on Computational Approaches to Analysis and Generation of Emotion in
Text, pages 62–70, 2010.
[177] M. Klassen, M. Cummings, and G. Saldana. Investigation of random forest per-
formance with cancer microarray data. In 23rd International Conference on Com-
puters and Their Applications, CATA 2008, pages 64–69, 2008.
[178] M. N. Ko, G. P. Cheek, M. Shehab, and R. Sandhu. Social-networks connect
services. Computer, 43(8):37–43, 2010.
[179] M. Komarraju and S. J. Karau. The relationship between the big ﬁve person-
ality traits and academic motivation.
Personality and Individual Differences,
39(3):557–567, 2005-08.
[180] M. Kosinski, D. Stillwell, and T. Graepel. Private traits and attributes are pre-
dictable from digital records of human behavior. Proceedings of the National
Academy of Sciences, 110(15):5802–5805, 2013.
[181] A. D. Labeaud, F. Bashir, and C. H. King. Measuring the burden of arboviral
diseases: the spectrum of morbidity and mortality from four prevalent infections.
Population health metrics, 9(1):1, 2011-01.
[182] J. Ladyman, J. Lambert, and K. Wiesner. What is a complex system? European
Journal for Philosophy of Science, 3(1):3367, 2013.
[183] R. Lambiotte and M. Kosinski. Tracking the digital footprints of personality.
Proceedings of the IEEE, 102(12):1934–1939, 2014.
[184] R. Lambiotte and M. Kosinski. Tracking the digital footprints of personality.
Proc. of the IEEE, 102(12):1934–1939, 2014.
149


## Page 162


[185] P. J. Lang. Behavioral treatment and bio-behavioral assessment: Computer ap-
plications. In J. B. Sidowski, J. H. Johnson, and T. A. Williams, editors, Tech-
nology in mental health care delivery systems, pages 119–137. Norwood, NJ:
Ablex, 1980.
[186] D. Lazer, A. Pentland, L. Adamic, S. Aral, A.-L. Barabsi, D. Brewer, N. Christa-
kis, N. Contractor, J. Fowler, M. Gutmann, T. Jebara, G. King, M. Macy, D. Roy,
and M. V. Alstyne. Computational Social Science. Science, 323(5915):721–723,
2009.
[187] J. Lerner, L. Tiedens, and R. Gonzalez. Toward a model of emotion-speciﬁc in-
ﬂuences on judgment and decision making: Portrait of the angry decision maker.
Journal of Behavioral Decision Making, 19:115–137, 2006.
[188] M. E. Lewis and J. M. E. Haviland-Jones. Handbook of emotions (2nd ed.).,
2000.
[189] E. D. Liddy. Natural language processing. In Natural Language Processing.
Marcel Decker Inc., 2001.
[190] J. Liscombe, J. Venditti, and J. Hirschberg. Classifying subject ratings of emo-
tional speech using acoustic features. Eighth European Conference on Speech
Communication and Technology, 2003.
[191] D. Lockner and N. Bonnardel. Emotion and interface design how to measure
interface design emotional effect? International Conference on Kansei Engin-
eering and Emotion Research, pages 10–25, 2014.
[192] G. F. Luger. Artiﬁcial Intelligence: Structures and Strategies for Complex Prob-
lem Solving, volume 6th. Pearson, 2005.
[193] F. Lw, U. Michel, S. Dech, and C. Conrad. Impact of feature selection on the ac-
curacy and spatial uncertainty of per-ﬁeld crop classiﬁcation using support vector
machines. ISPRS Journal of Photogrammetry and Remote Sensing, 85:102–119,
2013.
[194] I. S. MacKenzie. Human-Computer Interaction. Cambridge University Press,
2013.
[195] A. R. Mahrer. The case for fundamentally different existential-humanistic psy-
chologies. Journal of Humanistic Psychology, 29(2):249–262, 1989.
[196] F. Mairesse, M. Walker, M. Mehi, and R. Moore. Using linguistic cues for the
automatic recognition of personality in conversation and text. Journal of Artiﬁcial
Intelligence Research, 30:457–500, 2007.
150


## Page 163


[197] F. Mairesse and M. a. Walker. Automatic recognition of personality in conversa-
tion. Proceedings of the Human Language Technology Conference of the NAACL,
pages 85–88, 2006.
[198] K. Makice. Twitter API: Up and running: Learn how to build applications with
the Twitter API. ” O’Reilly Media, Inc.”, 2009.
[199] V. D. Malsburg. Analysis of perceptions. In Papers presented at the May 9-11,
1961, western joint IRE-AIEE-ACM computer conference on - IRE-AIEE-ACM
’61 (Western), page 281. ACM Press, 1961.
[200] J. Martınez-Miranda and A. Aldea. Emotions in human and artiﬁcial intelligence.
Computers in Human Behavior, 21(2):323–341, 2005.
[201] G. Matthews, I. J. Deary, and M. C. Whiteman. Personality traits. Cambridge
University Press, 2003.
[202] D. P. McAdams. The person: An introduction to personality psychology. Har-
court Brace Jovanovich, 1990.
[203] B. McCord, T. L. Rodebaugh, and C. A. Levinson. Facebook: Social uses and
anxiety. Computers in Human Behavior, 34:23–27, 2014.
[204] R. R. McCrae and J. Costa, Paul T. Personality trait structure as a human univer-
sal. American Psychologist, 52(5):509–516, 1997.
[205] R. R. McCrae, P. T. Costa, A. Terracciano, W. D. Parker, C. J. Mills, F. De Fruyt,
and I. Mervielde. Personality trait development from age 12 to age 18: longit-
udinal, cross-sectional, and cross-cultural analyses. Journal of personality and
social psychology, 83(6):1456–68, 2002-12.
[206] R. R. McCrae and O. P. John. An introduction to the ﬁve-factor model and its
applications. Journal of personality, 60(2):175–215, 1992.
[207] G. J. McLachlan. Discriminant analysis and statistical pattern recognition. John
Wiley and Sons, Inc, 2004.
[208] A. R. McLarney-Vesotski, F. Bernieri, and D. Rempala.
Personality percep-
tion: A developmental study. Journal of Research in Personality, 40(5):652–674,
2006-10.
[209] S. McLeod. Maslow’s hierarchy of needs. Simply Psychology, 1, 2007.
[210] J. McNaughton, T. Crick, and A. Hatch. Determining Device Position through
Minimal User Input.
Human-centric Computing and Information Sciences,
7(1):37, 2017.
151


## Page 164


[211] J. McNaughton, T. Crick, A. Joyce-Gibbons, G. Beauchamp, N. Young, and
E. Tan. Facilitating Collaborative Learning Between Two Primary Schools Using
Large Multi-Touch Devices. Journal of Computers in Education, 4(3):307–320,
2017.
[212] J. McNaughton, T. Crick, and S. P. Smith. Resolving Display Shape Dependence
Issues on Tabletops. Computational Visual Media, 4(4):349–365, 2018.
[213] M. L. McNeal and D. Newyear. Introducing chatbots in libraries. Library tech-
nology reports, 49(8):5–10, 2013.
[214] S. Menard. Logistic Regression: From Introductory to Advanced Concepts and
Applications. SAGE Publications, Inc., 2010.
[215] M. Mikolajczak, O. Luminet, C. Leroy, and E. Roy. Psychometric properties of
the trait emotional intelligence questionnaire: factor structure, reliability, con-
struct, and incremental validity in a french-speaking population. Journal of per-
sonality assessment, 88(3):338–53, 2007-06.
[216] R. B. Miller. Response time in man-computer conversational transactions. In
Proceedings of the December 9-11, 1968, fall joint computer conference, part I
on - AFIPS ’68 (Fall, part I), page 267, 1968.
[217] G. Mishne. Experiments with mood classiﬁcation in blog posts. Proceedings of
ACM SIGIR 2005 Workshop on Stylistic Analysis of Text for Information Access,
page 19, 2005.
[218] T. M. Mitchell. Machine Learning. ACM Computing Surveys (CSUR), 1997.
[219] F. Moller and T. Crick. A University-Based Model for Supporting Computer
Science Curriculum Reform. Journal of Computers in Education, 5(4):415–434,
2018.
[220] M. Mostafa, T. Crick, A. C. Calderon, and G. Oatley. Incorporating Emotion
and Personality-Based Analysis in User-Centered Modelling. In Research and
Development in Intelligent Systems XXXIII, pages 383–389. Springer, 2016.
[221] A. Mulac. The gender-linked language effect: Do language differences really
make a difference? Lawrence Erlbaum Associates Publishers, 2006.
[222] E. Murphy, T. Crick, and J. H. Davenport. An Analysis of Introductory Pro-
gramming Courses at UK Universities. The Art, Science, and Engineering of
Programming, 1(2)(18), 2017.
152


## Page 165


[223] J. Musek. A general factor of personality: Evidence for the big one in the ﬁve-
factor model. Journal of Research in Personality,, 2007.
[224] B. A. Myers. The importance of percent-done progress indicators for computer-
human interfaces. ACM SIGCHI Bulletin, 16(4):11–17, 1985.
[225] C. Nass and S. Brave. Emotion in human-computer interaction. In The human-
computer interaction handbook, pages 94–109. CRC Press, 2007.
[226] T. Nasukawa and J. Yi. Sentiment analysis : Capturing favorability using nat-
ural language processing. In Proceedings of the 2nd international conference on
Knowledge capture, pages 70–77, 2003.
[227] M. Negnevitsky. Artiﬁcial intelligence: a guide to intelligent systems. Pearson
Education, 2005.
[228] A. Newell and S. K. Card. The prospects for psychological science in human-
computer interaction. Human-computer interaction, 1(3):209–242, 1985.
[229] M. Newman, A.-L. Barabasi, D. J. Watts, and M. Bogu˜n´a. The Structure and
dynamics of networks, 2006.
[230] M. L. Newman, J. W. Pennebaker, D. S. Berry, and J. M. Richards. Lying words:
Predicting deception from linguistic styles. Personality and Social Psychology
Bulletin, 29(5):665–675, 2003-05.
[231] J. Nielsen. Response times: The 3 important limits. Usability Engineering, 1993.
[232] J. Nielsen. Usability Engineering, volume 44. Morgan Kaufmann; 1 edition
(September 23, 1993), 1993.
[233] N. J. Nilsson. Principles of artiﬁcial intelligence. Morgan Kaufmann, 2014.
[234] W. T. Norman. Toward an adequate taxonomy of personality attributes: Replic-
ated factor structure in peer nomination personality ratings. Journal of Abnormal
and Social Psychology, 66(6):574–583, 1963.
[235] S. Nunn. Preventing the next terrorist attack: The theory and practice of home-
land security information systems. Journal of Homeland Security and Emergency
Management, 2(3), 2005-01.
[236] G. Oatley and T. Crick. Changing Faces: Identifying Complex Behavioural Pro-
ﬁles. In Human Aspects of Information Security, Privacy and Trust, volume 8533
of Lecture Notes in Computer Science, pages 282–293. Springer, 2014.
153


## Page 166


[237] G. Oatley and T. Crick.
Exploring UK Crime Networks.
In Proceedings of
2014 International Symposium on Foundations of Open Source Intelligence and
Security Informatics (FOSINT-SI 2014). IEEE, 2014.
[238] G. Oatley and T. Crick. Measuring UK Crime Gangs. In Proceedings of 2014
IEEE/ACM International Conference on Advances in Social Networks Analysis
and Mining (ASONAM 2014). IEEE, 2014.
[239] G. Oatley and T. Crick. Measuring UK Crime Gangs: A Social Network Problem.
Social Network Analysis and Mining, 5, 2015.
[240] G. Oatley, T. Crick, and D. Bolt. CCTV as a Smart Sensor Network. In Pro-
ceedings of 13th IEEE International Conference on Dependable, Autonomic and
Secure Computing (DASC-2015). IEEE, 2015.
[241] G. Oatley, T. Crick, and R. Howell. Data Exploration with GIS Viewsheds and
Social Network Analysis. In Proceedings of 23rd GIS Research UK Conference
(GISRUK 2015), 2015.
[242] G. Oatley, T. Crick, and M. Mostafa. Digital Footprints: Envisaging and Analys-
ing Online Behaviour. In Proceedings of 2015 Symposium on Social Aspects of
Cognition and Computing Symposium (SSAISB), 2015.
[243] J. Oberlander and S. Nowson. Whose thumb is it anyway?: classifying author
personality from weblog text. Proceedings of the COLING/ACL on Main , pages
627–634, 2006.
[244] B. O’Connor, D. Bamman, and N. A. Smith. Computational Text Analysis for
Social Science: Model Complexity and Assumptions. In Proceedings of the NIPS
Workshop on Computational Social Science and the Wisdom of Crowds, 2011.
[245] A. Ohman. Fear and anxiety: Evolutionary, cognitive and clinical perspectives.
Hand-book of Emotions, pages 511–536, 1993.
[246] T. O’Reilly. What is Web 2.0: Design Patterns and Business Models for the Next
Generation of Software. O’Reilly, 2005.
[247] P.-Y. Oudeyer. Novel useful features and algorithms for the recognition of emo-
tions in speech. In B. B. and M. I., editors, Proceedings of the 1st International
Conference on Speech Prosody, pages 547–550, 2002.
[248] B. Pang and L. Lee. Seeing stars. Proceedings of the 43rd Annual Meeting on
Association for Computational Linguistics - ACL ’05, 1:115–124, 2005.
154


## Page 167


[249] B. Pang and L. Lee. Seeing stars: Exploiting class relationships for sentiment
categorization with respect to rating scales. In Proceedings of ACL, pages 115–
124, 2005.
[250] D. J. Pasta. Parameterizing models to test the hypotheses you want: coding indic-
ator variables and modiﬁed continuous variables. In Proceedings of the Thirtieth
Annual SAS Users Group International Conference, pages 212–30, 2005.
[251] T. R. Patil. Performance analysis of naive bayes and j48 classiﬁcation algorithm
for data classiﬁcation. International Journal Of Computer Science And Applica-
tions, ISSN: 0974-1011, 6(2):256–261, 2013.
[252] S. V. Paunonen and D. N. Jackson. What is beyond the Big Five? Plenty! Journal
of Personality, 68(5):821–836, 2000.
[253] D. Peabody and L. Goldberg.
Some determinants of factor structures from
personality-trait descriptor.
Journal of Personality and Social Psychology,
57(3):552–567, 1989.
[254] J. Pennebaker and C. Chung. The development and psychometric properties of
liwc2007. , TX, LIWC. Net, pages 1–22, 2007.
[255] J. Pennebaker and L. King.
Linguistic styles: language use as an individual
difference. J. of Personal. & Soc. Psychol, 77(6):1296–1312, 1999.
[256] J. W. Pennebaker, M. E. Francis, and R. J. Booth. Linguistic inquiry and word
count. Erlbaum Publishers, 2001.
[257] J. W. Pennebaker, M. E. Francis, and R. J. Booth. Linguistic inquiry and word
count: Liwc 2001. Mahway: Lawrence Erlbaum Associates, 71(2001):2001,
2001.
[258] J. W. Pennebaker and L. A. King. Linguistic styles: language use as an individual
difference. Journal of personality and social psychology, 77(6):1296–312, 1999-
12.
[259] J. W. Pennebaker, T. J. Mayne, and M. E. Francis. Linguistic predictors of ad-
aptive bereavement. Journal of personality and social psychology, 72(4):863–71,
1997-04.
[260] J. W. Pennebaker, M. R. Mehl, and K. G. Niederhoffer. Psychological aspects
of natural language use: Our words, our selves. Annual Review of Psychology,
54(1):547–577, 2003. PMID: 12185209.
[261] J. Pennington. Glove: Global vectors for word representation, 2018.
155


## Page 168


[262] J. Pennington, R. Socher, and C. Manning.
Glove: Global vectors for word
representation.
In Proceedings of the 2014 conference on empirical methods
in natural language processing (EMNLP), pages 1532–1543, 2014.
[263] F. S. Perls. Ego, hunger and aggression: A revision of Freud’s theory and method.
Gestalt Journal Press, 1992.
[264] K. V. Petrides and A. Furnham. Trait emotional intelligence: Psychometric in-
vestigation with reference to established trait taxonomies. European Journal of
Personality, 15(6):425–448, 2001.
[265] Pew
Research
Centre.
Social
Media
Use
in
2018.
http://
www.pewinternet.org/2018/03/01/social-media-use-in-
2018/, 2018.
[266] R. W. Picard. Affective Computing for HCI. In Proceedings of 8th International
Conference on Human-Computer Interaction, pages 829–833, 1999.
[267] B. Plank and D. Hovy. Personality traits on twitter or how to get 1,500 personality
tests in a week. Proceedings of the 6th Workshop on Computational Approaches
to Subjectivity, Sentiment and Social Media Analysis, pages 92–98, 2015.
[268] B. Plaza. Google analytics for measuring website performance. Tourism Man-
agement, 32(3):477–481, 2011.
[269] R. Plomin, J. DeFries, and G. McClearn. Behavioral genetics: A primer (2nd
ed.). San Francisco: Freeman, 1990.
[270] A.-M. Popescu and O. Etzioni. Extracting product features and opinion from
reviews. Human Language Technology and Empirical Methods in Natural Lan-
guage Processing, Vancouver, British Columbia, pages 339–346, 2005.
[271] POST. Social Media and Big Data. Technical Report POST-PN-460, UK Parlia-
mentary Ofﬁce of Science and Technology, March 2014.
[272] R. Primi, C. F. Ferreira-Rodrigues, and L. De Francisco Carvalho.
Cattell’s
personality factor questionnaire (cpfq): Development and preliminary study.
Paideia, 24(57):29–37, 2014.
[273] S. Psychology.
Linguistic styles : Language use as an individual difference.
Journal of personality and social psychology, 2000.
[274] D. Quercia, M. Kosinski, D. Stillwell, and J. Crowcroft. Our twitter proﬁles,
our selves: Predicting personality with Twitter. In Proceedings of 2011 IEEE
International Conference on Privacy, Security, Risk and Trust, pages 180–185,
2011.
156


## Page 169


[275] J. R. Quinlan. Induction of decision trees. Machine learning, 1(1):81–106, 1986.
[276] J. R. Quinlan. Improved use of continuous attributes in C4.5. Journal of Artiﬁcial
Intelligence Research, 4:77–90, 1996.
[277] J. R. Quinlan. C4. 5: programs for machine learning. Elsevier, 2014.
[278] J. Rafferty, M. Mostafa, T. Crick, G. Oatley, C. Ranson, and I. S. Moore. Using
machine learning to predict concussions in Welsh rugby union. Artiﬁcial Intelli-
gence in Medicine, 2018. (submitted, under review).
[279] J. Rafferty, C. Ranson, G. Oatley, M. Mostafa, P. Mathema, T. Crick, and I. S.
Moore. On average, a professional rugby union player is more likely than not to
sustain a concussion after 25 matches. British Journal of Sports Medicine, 2018.
[280] H. Ramchoun, M. Amine, J. Idrissi, Y. Ghanou, and M. Ettaouil. Multilayer
perceptron: Architecture optimization and training. International Journal of In-
teractive Multimedia and Artiﬁcial Intelligence, 4(1):26, 2016.
[281] J. E. Richard and S. Guppy. Facebook: Investigating the inﬂuence on consumer
purchase intention. Asian Journal of Business Research, 4(2), 2014-12.
[282] R. J. Rienks and D. K. J. Heylen. Automatic dominance detection in meetings
using easily obtainable features. In H. Bourlard and S. Renals, editors, Revised
Selected Papers of the 2nd Joint Workshop on Multimodal Interaction and Re-
lated Machine Learning Algorithms MLMI 2005, volume 3869 of Lecture Notes
in Computer Science, pages 76–86. Springer Verlag, 2006. ISBN=978-3-540-
32549-9.
[283] R. E. Riggio, C. Salinas, and J. Tucker. Personality and deception ability. Per-
sonality and Individual Differences, 9(1):189–191, 1988.
[284] D. Riso and R. Hudson.
Personality Types: Using the Enneagram for Self-
Discovery. Houghton Mifﬂin Harcourt, 1996.
[285] D. Riso and R. Hudson. Understanding the Enneagram: The Practical Guide to
Personality Types. Houghton Mifﬂin, 2000.
[286] A. Z. Rizvi. Personality , social anxiety and excessive use of facebook. Interna-
tional Journal of Psychology and Behavioral Sciences, 6(3):119–127, 2016.
[287] J. Robert and A. Lesage. Designing and evaluating user experience. Handbook
of Human-Machine Interaction, pages 1–22, 2010.
157


## Page 170


[288] T. Roenneberg. Twitter as a means to study temporal behaviour. Current Biology,
27(17):R830–R832, 2017.
[289] A. Rosenberg and J. Hirschberg. Acoustic / prosodic and lexical correlates of
charismatic speech. Ninth European Conference on Speech Communication and
Technology, 2005.
[290] F. Rosenblatt. The Perceptron: A Probabilistic Model for Information Storage
and Organization in The Brain. Psychological Review, 65(6):386–408, 1958.
[291] S. Rosenthal, R. Aitken, and A. Zealley. The Cattell 16PF personality proﬁle of
asthmatics. Journal of Psychosomatic Research, 17(1):9–14, 1973.
[292] J. P. Rushton, H. G. Murray, and S. Erdle.
Combining trait consistency and
learning speciﬁcity approaches to personality, with illustrative data on faculty
teaching performance. Personality and Individual Differences, 8(1):59–66, 1987.
[293] S. J. Russell and P. Norvig. Artiﬁcial intelligence: a modern approach. Malaysia;
Pearson Education Limited,, 2016.
[294] F. H. Sanford. Speech and Personality: A Comparative Case Study. Journal of
Personality, 10(3):169–198, 1942.
[295] L. M. Saulsman and A. C. Page.
The ﬁve-factor model and personality dis-
order empirical literature: A meta-analytic review. Clinical psychology review,
23(8):1055–85, jan 2004.
[296] K. Scherer. Vocal communication of emotion: A review of research paradigms.
Speech Communication, 40(1-2):227–256, 2003.
[297] K. R. Scherer and H. Giles, editors. Social Markers in Speech. European Studies
in Social Psychology. Cambridge University Press, 1980.
[298] K. R. Scherer and H. Wallbott. International Survey On Emotion Antecedents
And Reactions (ISEAR).
https://www.affective-sciences.org/
research/materials-and-online-research/research-
material/, 2018.
[299] S. Schiafﬁno and A. Amandi. Intelligent user proﬁling. In Artiﬁcial Intelligence:
An International Perspective, volume 5640 of LNCS, pages 193–216, 2009.
[300] H. A. Schwartz, J. C. Eichstaedt, M. L. Kern, L. Dziurzynski, S. M. Ramones,
M. Agrawal, A. Shah, M. Kosinski, D. Stillwell, M. E. P. Seligman, and L. H.
Ungar. Personality, Gender, and Age in the Language of Social Media: The
Open-Vocabulary Approach. PLoS ONE, 8(9), 2013.
158


## Page 171


[301] H. A. Schwartz, J. C. Eichstaedt, M. L. Kern, L. Dziurzynski, S. M. Ramones,
M. Agrawal, A. Shah, M. Kosinski, D. Stillwell, M. E. P. Seligman, and L. H.
Ungar. Personality, gender, and age in the language of social media: The open-
vocabulary approach. PLOS ONE, 8(9):1–16, 2013-09.
[302] E. Scornet, G. Biau, and J. P. Vert. Consistency of random forests. Annals of
Statistics, 43(4):1716–1741, 2015.
[303] H. L. Seal. Studies in the history of probability and statistics. xv the historical
development of the gauss linear model. Biometrika, 54(1-2):1–24, 1967.
[304] S. Sentance, M. Dorling, A. McNicol, and T. Crick. Grand Challenges for the
UK: Upskilling Teachers to Teach Computer Science Within the Secondary Cur-
riculum. In Proceedings of the 7th Workshop in Primary and Secondary Com-
puting Education (WiPSCE 2012), pages 82–85. ACM, 2012.
[305] B. A. Shawar and E. Atwell. Machine learning from dialogue corpora to generate
chatbots. Expert Update journal, 6(3):25–29, 2003.
[306] S. N. Shivhare and S. Khethawat.
Emotion detection from text.
CoRR,
abs/1205.4(07):371–377, 2012.
[307] J. F. Sigurdsson. Computer experience, attitudes toward computers and person-
ality characteristics in psychology undergraduates. Personality and Individual
Differences, 12(6):617–624, 1991-01.
[308] S. Singh and S. Singh. Artiﬁcial intelligence. International Journal of Computer
Applications, 6(6):21–23, 2010.
[309] Y. Singh, P. Bhatia, and O. Sangwan. A review of studies on machine learning
techniques. International Journal of Computer Science and Security, pages 70–
84, 2007.
[310] S. Smith-Atakan. Human-computer Interaction. FastTrack (Series). Thomson,
2006.
[311] A. Smola and S. Vishwanathan. Introduction to machine learning. Cambridge
University Press, pages 1–59, 2008.
[312] S. Somasundaran, J. Ruppenhofer, and J. Wiebe. Detecting arguing and senti-
ment in meetings. Proceedings of the 8th SIGdial Workshop on Discourse and
Dialogue, 1(September):26–34, 2007.
159


## Page 172


[313] J. Stage. Deﬁning and measuring user experience: Are they two sides of the
same coin?
In Proceedings of the Workshop on User Experience, NordiCHI
2006., pages 146–149, 2006.
[314] A. Stevens. Jung: A Very Short Introduction. Oxford University Press, 2001.
[315] V. Stoyanov, C. Cardie, and J. Wiebe.
Multi-perspective question answering
using the opqa corpus. Proceedings of the conference on Human Language Tech-
nology and Empirical Methods in Natural Language Processing, pages 923–930,
2005.
[316] X. Su, X. Yan, and C.-L. Tsai. Linear regression. Wiley Interdisciplinary Reviews:
Computational Statistics, 4(3):275–294, 2012.
[317] C. Sumner, A. Byers, R. Boochever, and G. J. Park. Predicting dark triad per-
sonality traits from twitter usage and a linguistic analysis of tweets.
In Ma-
chine learning and applications (icmla), 2012 11th international conference on,
volume 2, pages 386–393. IEEE, 2012.
[318] B. G. Tabachnick and L. S. Fidell. Using Multivariate Statistics. Pearson, 2001.
[319] L. Tan, S. Ponnam, P. Gillham, B. Edwards, and E. Johnson. Analyzing the im-
pact of social media on social movements: A computational study on Twitter and
the Occupy Wall Street movement. In Proceedings of IEEE/ACM International
Conference on Advances in Social Networks Analysis and Mining (ASONAM),
2013.
[320] Y. R. Tausczik and J. W. Pennebaker. The psychological meaning of words: Liwc
and computerized text analysis methods. J. of Lang. & Soc. Psychol., 29(1):24–
54, 2010.
[321] J. G. Taylor and N. Fragopanagos. Modelling the interaction of attention and
emotion. In Proceedings of the International Joint Conference on Neural Net-
works, volume 3, pages 1663–1668, 2005.
[322] J. Tennant, J. Beamer, J. Bosman, B. Brembs, N. Chung, G. Clement, T. Crick,
J. Dugan, A. Dunning, D. Eccles, A. Enkhbayar, D. Graziotin, R. Harding,
J. Havemann, D. S. Katz, K. Khanal, J. Kjaer, T. Koder, P. Macklin, C. Madan,
P. Masuzzo, L. Matthias, K. Mayer, D. Nichols, E. Papadopoulou, T. Pasquier,
T. Ross-Hellauer, M. Schulte-Mecklenbeck, D. Sholler, T. Steiner, P. Szczesny,
and A. Turner. Foundations for Open Scholarship Strategy Development. BITSS,
2019. https://doi.org/10.31222/osf.io/b4v8p.
160


## Page 173


[323] J. P. Tennant, J. M. Dugan, D. Graziotin, D. C. Jacques, F. Waldner, D. Mietchen,
Y. Elkhatib, L. B. Collister, C. K. Pikas, T. Crick, P. Masuzzo, A. Caravaggi, D. R.
Berg, K. E. Niemeyer, T. Ross-Hellauer, S. Mannheimer, L. Rigling, D. S. Katz,
B. Greshake, J. Pacheco-Mendoza, N. Fatima, M. Poblet, M. Isaakidis, D. Irawan,
S. Renaut, C. R. Madan, L. Matthias, J. Nørgaard Kjær, D. O’Donnell, C. Neylon,
S. Kearns, M. Selvaraju, and J. Colomb. A multi-disciplinary perspective on
emergent and future innovations in peer review [version 3; referees: 2 approved].
F1000Research, 6(1151), 2017.
[324] The Joomla!
Project.
Joomla!
CMS Architecture.
https://
docs.joomla.org/Archived:CMS Architecture in 1.5 and 1.6,
2011.
[325] E. Tiggeler. Joomla! 2.5 Beginner’s Guide. Joomla Inc, 2012.
[326] S. S. Tompkins.
Affect, imagery, consciousness: II. The Negative Affects.,
volume 1. Springer Publishing Company, 1963.
[327] B. T¨orestad. What is anger provoking? a psychophysical study of perceived
causes of anger. Aggressive Behavior, 16(1):9–26, 1990.
[328] E. Z. Tronick. Emotions and emotional communication in infants. American
psychologist, 44(2):112, 1989.
[329] G. Trovato, G. Chrupaa, and A. Takanishi. Application of the naive bayes clas-
siﬁer for representation and use of heterogeneous and incomplete knowledge in
social robotics. Robotics, 5(1):6, 2016-02.
[330] C. Tryfona, T. Crick, A. C. Calderon, and S. Thorne. Software Requirements
Engineering in Digital Healthcare: A case study of the diagnosis and monitoring
of Autism Spectrum Disorders in the UKs National Health Service. In Digital
Human Modeling, volume 10287 of Lecture Notes in Computer Science, pages
91–98. Springer, 2017.
[331] T. Tryfonas, M. Carter, T. Crick, and P. Andriotis. Mass Surveillance in Cy-
berspace and the Lost Art of Keeping a Secret: Policy Lessons for Government
After the Snowden Leaks. In Human Aspects of Information Security, Privacy
and Trust, volume 9750 of Lecture Notes in Computer Science, pages 174–185.
Springer, 2016.
[332] T. Tryfonas and T. Crick.
What skills will we need to live in future smart
cities?
Technical report, Government Ofﬁce for Science, Department for
Business, Innovation & Skills, August 2015.
https://www.gov.uk/
161


## Page 174


government/publications/future-of-cities-smart-
cities-citizenship-skills-and-the-digital-agenda.
[333] T. Tryfonas and T. Crick. Public Policy and Skills for Smart Cities: The UK
Outlook. In Proceedings of 11th International Conference on PErvasive Tech-
nologies Related to Assistive Environments (PETRA’18), pages 116–117. ACM,
2018.
[334] S. Tucker and S. Whittaker. Accessing multimodal meeting data: Systems, prob-
lems and possibilities. In International Workshop on Machine Learning for Mul-
timodal Interaction, pages 1–11. Springer International Publishing, 2005.
[335] A. Tumasjan, T. O. Sprenger, P. G. Sandner, and I. M. Welpe. Predicting Elec-
tions with Twitter: What 140 Characters Reveal about Political Sentiment. In
Proceedings of the 4th International AAAI Conference on Web and Social Media
(ICWSM), 2010.
[336] E. C. Tupes and R. E. Christal. Recurrent personality factors based on trait rat-
ings. Journal of personality, 60(2):225–51, 1992-06.
[337] P. D. Turney. Thumbs up or thumbs down? semantic orientation applied to un-
supervised classiﬁcation of reviews. Proceedings of the 40th Annual Meeting of
the Association for Computational Linguistics (ACL), pages 417–424, 2002.
[338] D. Tveter. The pattern recognition basis of artiﬁcial intelligence. IEEE, 1997.
[339] UK Ofﬁce for National Statistics.
Home internet and social media us-
age. https://www.ons.gov.uk/peoplepopulationandcommunity/
householdcharacteristics/homeinternetandsocialmediausage,
2017.
[340] S. Vazire and S. Gosling. e-perceptions: Personality impressions based on per-
sonal websites. Journal of Personality and Social Psychology, 87(1):123–132,
2004.
[341] C. C. Venters, R. Capilla, S. Betz, B. Penzenstadler, T. Crick, S. Crouch, E. Yumi
Nakagawa, C. Becker, and C. Carrillo. Software Sustainability: Research and
Practice from a Software Architecture Viewpoint. Journal of Systems and Soft-
ware, 138:174–188, 2018.
[342] L. Wall, T. Christiansen, and R. L. Schwartz. Programming Perl. O’Reilly, 1999.
[343] Y. Wang and A. Pal. Detecting emotions in social media: A constrained optimiz-
ation approach. Proceedings of the Twenty-Fourth International Joint Conference
on Artiﬁcial Intelligence, pages 996–1002, 2015.
162


## Page 175


[344] D. Watson and L. A. Clark.
On traits and temperament: General and spe-
ciﬁc factors of emotional experience and their relation to the ﬁve-factor model.
Journal of Personality, 60(2):441–476, 1992.
[345] D. J. Watts and S. H. Strogatz. Collective dynamics of small-world’ networks.
Nature, 393(6684):440–442, 1998.
[346] W. Weintraub. Verbal Behavior in Everyday Life. Springer, 1989.
[347] Y. J. Weisberg, C. G. DeYoung, and J. B. Hirsh. Gender differences in personality
across the ten aspects of the big ﬁve. Frontiers in Psychology, 2, 2011.
[348] E. Wenger. Artiﬁcial intelligence and tutoring systems: computational and cog-
nitive approaches to the communication of knowledge. Morgan Kaufmann, 2014.
[349] A. Whicher and T. Crick. Co-Design, Evaluation and the Northern Ireland Innov-
ation Lab. Public Money & Management, 2019. Special Issue on “Co-Production
of Public Services and Outcomes”, (to appear).
[350] J. Wiebe, T. Wilson, R. Bruce, M. Bell, and M. Martin. Learning subjective
language. Computational Linguistics, 30(3):277–308, 2004.
[351] Wikipedia.
Semeval.
https://en.wikipedia.org/wiki/SemEval,
2018.
[352] M. L. Williams and P. Burnap. Cyberhate on Social Media in the aftermath of
Woolwich: A Case Study in Computational Criminology and Big Data. The
British Journal of Criminology, 56(2):211–238, 2016.
[353] M. Wilson. The mrc psycholinguistic database: Machine readable dictionary,
version 2.00. Behavior Research Methods, Instruments & Computers, 20(1):6–
10, 1988.
[354] M. Wilson. MRC psycholinguistic database: Machine-usable dictionary, version
2.00. Behavior Research Methods, Instruments, & Computers, 20(1):6–10, 1988.
[355] T. Wilson, T. Wilson, J. Wiebe, J. Wiebe, R. Hwa, and R. Hwa. Just how mad
are you? ﬁnding strong and weak opinion clauses. Proceedings of the National
Conference on Artiﬁcial Intelligence, pages 761–769, 2004.
[356] C. Winship and R. D. Mare. Regression models with ordinal variables. American
Sociological Review, 49(4):512, 1984.
[357] G. Wolfsfeld, E. Segev, and T. Sheafer. Social Media and the Arab Spring: Polit-
ics Comes First.
The International Journal of Press/Politics, 18(2):115–137,
2013.
163


## Page 176


[358] J. Yen. System for automatic recovery from software problems that cause com-
puter failure, Apr. 30 2002. US Patent 6,381,694.
[359] F. Zaklouta, B. Stanciulescu, and O. Hamdoun. Trafﬁc sign classiﬁcation using
K-d trees and random forests. In Proceedings of the International Joint Confer-
ence on Neural Networks, pages 2151–2155, 2011.
164

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
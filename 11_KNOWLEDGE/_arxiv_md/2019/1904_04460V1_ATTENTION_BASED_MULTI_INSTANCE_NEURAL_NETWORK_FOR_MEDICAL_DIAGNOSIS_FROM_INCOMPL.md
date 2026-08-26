---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.04460v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1904.04460v1_Attention-based_Multi-instance_Neural_Network_for_Medical_Diagnosis_from_Incompl

> Source: 1904.04460v1_Attention-based_Multi-instance_Neural_Network_for_Medical_Diagnosis_from_Incompl.pdf

> Pages: 8

---


## Page 1


Attention-based Multi-instance Neural Network for Medical 
Diagnosis from Incomplete and Low Quality Data  
Zeyuan Wang1,3, Josiah Poon1, Shiding Sun2, Simon Poon1* 
1School of Computer Science, The University of Sydney, Syndey, Australia 
2School of Mathematics, Renmin University of China, Beijing, China 
3Beijing Medicinovo Technology Co.,Ltd., Beijing, China 
1,3zwan7221@uni.sydeny.edu.au, 1{josiah.poon, simon.poon}@sydney.edu.au, 2sunshiding@ruc.edu.cn 
Abstract— One way to extract patterns from clinical records is to 
consider each patient record as a bag with various number of 
instances in the form of symptoms. Medical diagnosis is to discover 
informative ones first and then map them to one or more diseases. 
In many cases, patients are represented as vectors in some feature 
space and a classifier is applied after to generate diagnosis results. 
However, in many real-world cases, data is often of low-quality 
due to a variety of reasons, such as data consistency, integrity, 
completeness, accuracy, etc. In this paper, we propose a novel 
approach, attention based multi-instance neural network (AMI-
Net), to make the single disease classification only based on the 
existing and valid information in the real-world outpatient records. 
In the context of a patient, it takes a bag of instances as input and 
output the bag label directly in end-to-end way. Embedding layer 
is adopted at the beginning, mapping instances into an embedding 
space which represents the individual patient condition. The 
correlations among instances and their importance for the final 
classification are captured by multi-head attention transformer, 
instance-level multi-instance pooling and bag-level multi-instance 
pooling. The proposed approach was test on two non-standardized 
and highly imbalanced datasets, one in the Traditional Chinese 
Medicine (TCM) domain and the other in the Western Medicine 
(WM) domain. Our preliminary results show that the proposed 
approach outperforms all baselines results by a significant margin.  
Keywords—medical diagnosis, low-quality data, multi-instance 
learning, attention mechanism, deep learning 
 
I. 
INTRODUCTION 
In many real-world observational studies, data is collected from 
various real-life applications instead of controlled experiment 
settings. These observational data are subject to data quality 
concerns such as: (i) data accuracy, (ii) data completeness, (iii) 
data consistency, and (iv) data balance [1]. More importantly, in 
real life, clinical decisions are made only from a few informative 
and valuable attributes, i.e., features, instead of the entire patient 
record. The use of computational models to find key information 
from a large amount of incomplete and low-quality data to 
generate the solid diagnosis results, has become a topic of broad 
interest. 
From the machine learning perspective, this scenario is 
known as weakly supervised learning (WSL) and multi-instance 
learning (MIL) is a typical one [2]. This perspective considers 
the input sample as a bag of instances and only the bag label is 
given. Through learning and training, MIL models allow to 
predict the labels of new bags with containing instances. MIL 
was first proposed by Dietterich et. al [3] for drug molecule 
activity prediction, and has been widely applied in many fields, 
including medical imaging and video analysis [4, 5], syndrome 
differentiation in Tradition Chinese Medicine (TCM) [6, 7], 
pulmonary embolism and colon cancer detection [8] and retinal 
nerve fiber layer visibility classification [9]. In this paper, we 
mainly emphasize the application of MIL for the single disease 
diagnosis, i.e., binary classification on a single task. 
Based on the definition of MIL, the bag is labeled positive 
only if at least one instance is positive, otherwise, the bag is 
labeled negative. In the context, capturing correlations among 
instances and finding the most informative instances play major 
roles. In many previous studies, the focus was on the latter, i.e., 
important instances detection, such as EM-DD [10], mi-SVM 
[11], mi-Graph [12] and miFV [13]. It is important to note that 
in some circumstances, if the correlations among instances are 
neglected, the prediction might be misled. For example, the bag 
is labeled as beach, only if the sky, ocean and sand co-occur [14]. 
Considering a complex progress like medical diagnosis, not only 
clinicians need to assess risk factors independently, but also take 
the influence of their co-occurrence into account. This is one of 
our starting points that we aim to measure instance correlations 
in the model building process. 
Multi-instance neural network was first proposed by Ramon 
et al. [15]. This approach computes instance probabilities to be 
further processed by the log-sum-exp operator to get the bag 
probability and the whole process is trained in end-to-end way. 
Their work demonstrates the effectiveness and simplicity of the 
neural networks to solve the MIL problem. Subsequently, more 
neural network-based MIL architectures are proposed for 
different applications [16, 17, 18]. And different from the 
instance probabilities calculation first way, Wang et al. [19] 
propose a novel framework that obtains the bag embedding via 
instance-level MIL pooling first and a classifier is built based on 
it to get the bag probability. Their work supplies a new approach 
for developing the multi-instance neural networks. 
Moreover, with respect to the ability in capturing relations 
among instances, and between instances and bags, the attention 
mechanism has shown some performance advantages. It has 
been widely used in image and text analysis [20, 21] for now 
with two sub-categories: (i) task-supervised attention, and (ii) 
self-supervised attention. The former captures the relations 
between the source and target [22], and the latter computes the 
intra-relationship of the source [23]. Both sub-categories are 
essential for the MIL.  
*Corresponding Author


## Page 2


In this study, we integrate them into a multi-instance neural 
network. We approach the main tasks of medical diagnosis from 
incomplete and low-quality data as follows: (i) mapping input 
instances in an embedding space [24], and instances correlating 
to each other over different embedding dimensions, representing 
some body condition, (ii) capturing the instance correlations in 
different embedding subspaces, (iii) learning the bag embedding, 
and (iv) selecting informative instances via attention mechanism 
to obtain the bag score. All modules are parameterized through 
the MIL neural network, which makes the architecture flexible 
and simple. This approach doesn’t require data collection on 
purpose or data screening manually, but deal with them 
automatically, capturing the most useful information among a 
large amount of low-quality data to support the final medical 
diagnosis. 
II. 
METHODOLOGY 
The overall architecture consists of an embedding layer, a multi-
head attention transformer with the residual connection [25], a 
set of instance-wise fully connected layers, an instance-level 
MIL pooling layer and a bag-level MIL pooling layer followed 
by a sigmoid function. The overview of AMI-Net is shown in 
Figure 1. 
A. Multi-instance Learning 
Common supervised learning aims to learn a function, mapping 
the input dataset Χ to the label set Υ, in which, each object ݔ௜∈
Χ is represented by an instance and labeled by a category or a 
class ܻ௜∈Υ. 
In MIL, the task is to learn a function mapping the input 
dataset ሼܺଵ, ܺଶ, … , ܺ௠ሽ to 
the 
corresponding 
label 
set 
ሼܻଵ, ܻଶ, … , ܻ௠ሽ where ܻ௜∈ሼ0, 1ሽ. ܺ௜ is a bag with a set of instances 
൛ݔ௜ଵ, ݔ௜ଶ, … , ݔ௜,௡೔ൟ and ݊௜ denotes to the number of instances in ܺ௜. 
When predicting, for each bag ܺ௜, if there is at least one instance 
labeled positive, then the bag labeled positive and otherwise is 
negative. The assumption can be formulated as follows: 
ܻ௜= ൜0,    ݈݈ܽ ݕ௜௝= 0
 1,    ݋ݐ݄݁ݎݓ݅ݏ݁                             (1) 
where ݕ௜௝ is the label of the ݆௧௛ instance in the ݅௧௛ bag.  
The assumption above implies the underlying basis of MIL, 
permutation invariance property, and any permutation invariant 
symmetric function for solving the MIL problem can be denoted 
as the following function [26, 27]: 
݂(ܺ) = ߠ(ߟ௫∈௑߮(ݔ))                         (2) 
where ߮ and ߠ are suitable transformations. ߟ is the permutation 
invariance function, that is well known as MIL pooling, and ߠ is 
the scoring function for a bag of instances. 
About the different choices of choosing suitable ߮, ߟ and ߠ, 
there are two main MIL approaches:  
(i) Instance-level MIL pooling approach: ߮ is the instance 
transformer and the MIL pooling function ߟ is adopted 
on each instance to obtain the bag embedding for the 
further procession by a bag classifier ߠ. 
(ii) Bag-level MIL pooling approach: ߮ is a transformation 
to return the instance scores, that are further processed 
by the MIL pooling ߟ to obtain the bag score and ߠ is an 
injective function. 
MIL with Neural Networks Since the MIL underlying function 
above leaves flexibility that we can model any transformation 
and score function only if they follow the permutation-invariant 
property. Therefore, we parameterize a class of transformations 
through the neural network. Let ܺ be a bag of ܯ instances, the 
transformer ߮ఛ, where ߬ are parameters, transforms instances to 
the embedding space with ܭ dimensions, that is ݒ௠,௄= ߮ఛ(ݔ௠), 
݉∈ܯ. Then the bag probability of ݔ௠ is determined by the 
transformation ߠఠ: ߟథೖ∈಼൫ݒ௠,௞൯→[0, 1]. If using the bag-level 
MIL pooling approach, ߠఠ is an injective function or otherwise 
is parameterized by the neural networks with parameters ߱, and 
if the trainable MIL pooling methods are utilized, ߶ are also 
parameters. 
MIL pooling As shown above, MIL pooing ߟ is the key step for 
bridging instances to bags, and different applications have their 
own preference for choosing MIL pooling methods. The only 
restriction of them on neural networks is differentiable. In MI-
Net [19], max pooling, mean pooling, and log-sum-exp pooling 
are adopted on each instance as the instance-level MIL pooling 
approach and Yan et. al [18] proposed a novel dynamic pooling 
method integrating both instance-level and bag-level approaches. 
In our proposed method, we also adopt them all on the neural 
network. Inspired from the sentence representation way in the 
 
 
                                                                        Figure 1: The overview of AMI-Net


## Page 3


document classification problem [28], we use the sum pooling 
as the instance-level MIL pooling method: 
 ∀௠ୀଵ,ଶ,…,ெ∶ ݒ௠= ∑
ݒ௠,௞
௄
௞ୀଵ
                          (3) 
where ܯ and ܭ denotes the bag containing instances, and the 
embedding dimensions. Moreover, we propose to use attention-
based MIL pooling on the bag-level to obtain the bag score, 
which is further mapped to the bag probability through sigmoid 
function.  
B. Attention-based MIL Pooling 
The attention-based MIL pooling aims to assign weights, trained 
by the neural network, over instances. In our proposed method, 
it is employed in the bag-level, which is formulated as follows: 
ݒ= ∑
ܽ௠ݒ௠
ெ
௠ୀଵ
                                       (4) 
where: 
ܵ=  ܹଵ
்(ݐ݄ܽ݊(ݒ௠ܹଶ) ⨀ ݏ݅݃݉݋݅݀(ݒ௠ܹଷ)))              (5) 
ܽ௠= ݏ݋݂ݐ݉ܽݔ(ܵ)                                      (6) 
where ܹଵ∈Թௗ೘೚೏೐೗ൈଵ and ܹଶ, ܹଷ∈Թௗ೘೚೏೐೗ൈௗ೗ are parameters, 
and ⨀ is the element-wise multiplication. 
Since the ݐ݄ܽ݊ function lacks the ability to learn the complex 
relations and limits the expression of non-linearity, a ݏ݅݃݉݋݅݀ 
based function is element-wise multiplied after, which is also 
known as the gated mechanism [29]. 
Attention mechanism allows to supervise the neural network 
to pay more attention on the instances which are most likely to 
be labeled as positive [30]. It makes the model interpretable and 
able to detect key information from a large amount of dirty data, 
which is consistent to medical diagnosis process in the real life.  
C. Multi-head Attention 
In our method, we propose to integrate the multi-head attention 
transformer [23] on the MIL neural network, to capture the intra-
relationship of instances in different embedding subspaces, that 
perfectly fits for the medical domain since symptoms are often 
related to each other in different body parts or organs, and each 
one can be seen as a subspace. Also, standard expressions of 
symptoms and non-standard ones can also be linked via multi-
head attention, improving model robustness to low-quality data. 
The transformer takes query and a set of key-value pairs as 
input and output the weighted sum of values. The weights of 
values are calculated through the query and the corresponding 
key with the cosine similarity-based function. In our method, we 
mainly focus on the exploration of correlations among instances, 
therefore, query, key and value are all instances themselves. In 
practice, it consists of two computational parts: scaled dot-
product attention and multi-head attention transformation. The 
architecture of the transformer is depicted as Figure 2. 
Scaled dot-product attention Cosine similarity is computed in 
the subspace first for instances themselves. ܵ݋݂ݐ݉ܽݔ function is 
used after for obtaining the final weights vector, representing the 
similarities and correlations of instances. Considering that the 
large value of instance dimensions ݀௜ likely makes the ݏ݋݂ݐ݉ܽݔ 
function to have the extremely small gradients, 
ଵ
ඥௗ೔ is taken as 
the scaling factor. The final output is computed as follows: 
݈ܵ݅݉݅ܽݎ݅ݐݕ(ܾ, ܿ) = 
௕∙௖
‖௕‖‖௖‖ = ்ܾܿ                          (7) 
ܣݐݐ(ܺ, ܺ, ܺ) = ݏ݋݂ݐ݉ܽݔ൬
ௌ௜௠௜௟௔௥௜௧௬(௑,௑)
ඥௗ೔
൰ܺ               (8) 
where ∙ is dot-product function and ܺ denotes a bag of instances. 
Multi-head transformation It splits instance dimensions into a 
number of subspaces and performs scaled dot-product attention 
on each one in parallel, capturing the instance correlations in 
different subspaces. The results are concatenated together at last 
as the final output. Linear transformations are alternately applied 
in the middle. The whole process is formulated as follows: 
ܯݑ݈ݐ݅ܪ݁ܽ݀(ܺ, ܺ, ܺ) = ܥ݋݊ܿܽݐ(݄݁ܽ݀ଵ, … , ݄݁ܽ݀௡)ܹ௠      (9) 
݄݁ܽ݀௜= ܣݐݐ(ܹܺ௜
ଵ, ܹܺ௜
ଶ, ܹܺ௜
ଷ)                         (10) 
where ܹ௜
ଵ , ܹ௜
ଶ, ܹ௜
ଷ ∈Թௗ೘೚೏೐೗ൈௗೖ, ܹ௠ ∈Թ௛ௗೖൈௗ೘೚೏೐೗, ݄ denotes 
the number of heads and ݄݁ܽ݀௜ denotes the ݅௧௛ subspace. 
III. 
RELATED WORK 
A. MIL Pooling 
Recently, various MIL pooling methods on the neural networks 
have been proposed which can be divided into two categories: 
non-trainable and trainable. Non-trainable methods are some 
simple operators such as max [19] and mean [31]. On one hand, 
since they are not trainable, the ability of informative instances 
selection is limited, but on the other hand, this way keeps the 
model simple and flexible, and makes sure the gradient doesn’t 
vanish. On the contrary, the other methods are trainable ones, 
which are more effective and sufficient to detect the key instance, 
such as attention-based MIL pooling, gated attention-based MIL 
 
Figure 2: The architecture of multi-head attention


## Page 4


pooling [4] and adaptive pooling [32]. They highly enhance the 
performance and applicability of MIL models.  
Here, we propose to use both of them as instance-level and 
bag-level MIL pooling respectively to keep the model simple but 
efficient when capturing the valid information. 
B. Self-Attention Mechanism 
Self-attention mechanism is first proposed by Vaswani et. al [23] 
to solve the long-distance dependency problem and capture the 
relations among words in different subspaces for the natural 
machine translation. Their work has proven the efficiency and 
effectiveness of self-attention mechanism to capture syntactic 
and semantic information among words in text. Follow this line 
of research, that Shen et al. [33] use self-attention mechanism 
for language understanding and Tan et al. [34] adopt it for the 
semantic role labeling (SRL) task. Additionally, Verga et. al [35] 
expand this idea further to the task of biological relationship 
extraction and their proposed method performs noticeable well. 
Motivated by the mechanism of self-attention for capturing 
intra-relations among words in text, we consider each patient 
record as a sentence with unordered words, i.e., symptoms, to 
explore the intra-relations of symptoms and link their standard 
and non-standard expressions. 
IV. 
EXPERIMENTS 
In the experiments, we evaluated the proposed method AMI-Net 
on two real-world medical datasets, suitable for our approach to 
be applied, one from the Traditional Chinese Medicine (TCM) 
domain and the other from the Western Medicine (WM) domain, 
for the diagnosis purpose. The examples of two datasets are 
shown in Table 1. 
A. Datasets 
Traditional Chinese Medicine (TCM): The TCM dataset is 
collected from diabetic patients’ records in a Chinese Medical 
Hospital in Beijing, which has been analyzed for capturing vital 
herb-herb interactions [36] and symptom-herb patterns [37]. In 
the dataset, there are 1617 outpatient records with 186 different 
symptoms. From patient to patient, the number of symptoms is 
various in 1-17. Also, the expressions of symptoms are not 
standardized and consistent, such as the sweat and perspiration 
existing in the same patient record. 
The binary classification task is whether the patient has the 
meridian obstruction, a syndrome of TCM. Among all patients, 
there are 1436 labeled as negative and 181 labeled as positive. 
So, the dataset is highly imbalanced with the positive rate 0.112. 
Most importantly, there are a large number of missing values in 
the dataset, since it is difficult for clinicians to complete patient 
examinations due to the lack of patient’s compliance and non-
standardization of TCM information collection. 
Western Medicine (WM): The WM dataset is provided by an 
AI company specialized on the medical real-world study, which 
collects 3927 inpatient records of schizophrenic patients, who 
have taken the modified electro-convulsive therapy (MECT) 
and improved the condition on discharge. The model aims to 
diagnose whether the schizophrenia relapse in three months 
based on the 88 physical and clinical features, such as married, 
unemployed, high levels of prolactin, MECT in 1-10 times and 
5mg haloperidol injection. For each patient, there are at most 21 
features existing and 5 at least, representing the individual 
patient condition. The dataset is also extremely imbalanced, that 
the positive rate of labels is only 0.057. 
B. Experimental Setup 
For both datasets, we padded each input record to the maximum 
size and the number of embedding dimensions was 128, close to 
the number of human organs [38]. The number of heads in the 
following multi-head attention transformer was set at 4. About 
the instance-wise fully connected layers, hidden sizes were 64 
and 32 respectively. Cross-entropy was used for the final loss 
calculation and Adam optimizer [39] was adopted to minimize 
it over the training data. In relation to the hyper-parameters of 
Adam, we set the learning rate at 0.01, momentum parameters 
ߚଵ at 0.9, ߚଶ at 0.98 and ߝ at 1݁ି଼.  In order to compare the 
performance, we set the binary threshold as 0.5, using AUC, 
Accuracy, Precision, Recall and F1-score as evaluation metrics. 
During the training process, the number of epochs was set at 
1000 and early stopping was utilized for the best model selection 
according to the F1 score over the validation dataset. For the fair 
comparison, all experiments were run in 10-fold cross validation 
with five repetitions. 
C. Baselines 
The task is not only considered as a MIL problem, but also a 
traditional binary classification problem on the dataset in the 
one-hot format, that is, in the predefined feature space, learn a 
transformation ݃: ܺ→[0, 1], where ܺ= ሼ(ߣ௜, ߧ௜)ሽ|௑|
௜ୀଵ is a set of 
(feature, value) pairs [40] and values are all binary. If the value 
is missing, in the most common way, 0 is imputed to represent 
TABLE I.  
EXAMPLES OF TCM AND WM DATASETS 
Dataset 
Features 
Diagnosis 
TCM 
Urine color yellow, Sweat, Pruritus, Coldness of extremities, Perspiration 
Meridian obstruction 
Dark red tongue, Palpitation 
Not meridian obstruction 
WM 
Personal income 3000~5000, Unmarried, LOS<10 days, MECT<=1, Onset age<17, Total course<1095 
days, Lorazepam tablets=0.5mg 
Schizophrenia relapse 
Personal income 1000~3000, Married, High levels of prolactin, hyperglycemia, High levels of 
corticotrophin, LOS 25~49 days, MECT 1~10, Onset age 1-10, Risperidone<=1mg, Total course 
1095~5840 days, Haloperidol injection 5mg 
Not relapse


## Page 5


the unknown condition. The following models were used as the 
baseline comparisons to our proposed method. The first four 
were built on the datasets transformed in the one-hot format. 
• 
Logistic Regression (LR) [41]: A classic linear model 
which has been widely applied for binary classification, 
risk factors selection and the risk assessment scales 
development [42]. 
• 
SVM [43]: Nonlinearly mapping the input space to be 
high-dimensional and constructing the hyperplane set 
for the regression and classification tasks. 
• 
Random Forest [44] and XGBoost [45]: Classic decision 
tree based algorithms, which solve the classification and 
regression tasks through bagging and boosting methods 
respectively. Both of them have gained wide attention 
in the medical domain for their interpretability, efficient 
training speed and excellent performance. 
• 
mi-Net [19]: A MIL neural network using the bag-level 
MIL pooling approach with the max operator.  
• 
MI-Net, MI-Net with DS and MI-Net with RC [19]: They 
are all proposed by Wang et al. using the instance-level 
MIL pooling approaches, which have achieved state-of-
art performance on several classic MIL datasets. 
• 
Att. Net and Gated Att. Net [4]: Two recent state-of-art 
MIL neural networks, utilizing the attention based MIL 
pooling on instance level to capture the relations of 
instance attributes. 
Also, hyper-parameters of all baseline models were tuned on 
the validation dataset in terms of the F1-score. 
V. RESULTS AND ANALYSIS 
A. Comparison with Different Models 
The results on two medical datasets are shown in the Table II 
and III. Our method, AMI-Net, had the best performance in 
terms of Precision and F1-score with the WM dataset (Table II). 
In fact, the F1-score from our method outperformed all other 
models by a large margin, although our scores on the AUC and 
Accuracy were slightly lower than the four classical machine- 
learning algorithms. Regarding the TCM dataset, which was 
highly imbalanced, our method outperformed all other models 
on Precision, Recall and F1-score. 
The two datasets were incomplete and low-quality. No 
positive sample could be found sometimes, but our method was 
shown to be more robust and reliable than other models in this 
kind of situation. In addition, in terms of Precision, Recall and 
F1-score, multi-instance neural networks performed efficiently 
and effectively in capturing the vital information from positive 
samples, demonstrating the superiority of MIL in the real-life 
applications, with the medical domain in particular. 
B. Comparison of Different Number of Heads 
In order to verify how different number of heads in multi-head 
attention transformer could influence the performance of AMI-
net, experiments with 0, 2, 4, 8, 16 and 32 heads on both the 
TCM and WM datasets were set up, where 0 denoted the model 
without multi-head attention, using F1-score for evaluation. 
As shown in Figure 3, when the transformer had 4 heads, our 
method achieved the best performance. This indicated that 4 
subspaces allowed the model to have the most efficient and 
effective capture of intra-relations of symptoms. If it is to be 
interpreted using medical knowledge, it means that the condition 
of a patient is best considered from 4 aspects such that the 
symptoms are highly correlated to each other in each aspect. 
Coincidentally, symptoms in the TCM dataset were collected 
from four diagnostic methods, inspection, listening and smelling, 
inquiry and pulse-taking, representing four main aspects of the 
body condition. The experimental result was consistent with the 
TCM diagnosis. The results also showed that the model without 
the multi-head attention had the worst performance, indicating 
the necessity to find the correlation among symptoms, as well as 
linking standardized and unstandardized symptom expressions 
via the multi-head attention. 
C. Comparison of Different MIL Pooling Methods 
In order to measure the impact of different instance-level and 
bag-level MIL pooling methods, the F1-scores were compared 
on different combinations. The max pooling [19] and the 
attention-based pooling [4] have previously been attempted, 
thus sum pooling, max pooling, attention based pooling and 
TABLE II. 
PERFORMANCE ON THE WM DATASET
Models 
AUC 
Accuracy 
Precision 
Recall 
F1 
LR 
0.760 
0.944 
0.200 
0.017 
0.031 
SVM 
0.657 
0.946 
0 
0 
0 
Random Forest 
0.767 
0.946 
0 
0 
0 
XGBoost 
0.706 
0.945 
0.100 
0.007 
0.013 
mi-Net 
0.565 
0.624 
0.088 
0.469 
0.125 
MI-Net 
0.545 
0.787 
0.154 
0.251 
0.116 
MI-Net+DS 
0.510 
0.621 
0.045 
0.383 
0.064 
MI-Net+RC 
0.588 
0.867 
0.313 
0.228 
0.164 
Att. Net 
0.608 
0.849 
0.342 
0.143 
0.074 
Gated Att. Net 
0.576 
0.832 
0.248 
0.140 
0.060 
AMI-Net 
0.702 
0.907 
0.356 
0.283 
0.264 
 
TABLE III.  
PERFORMANCE ON THE TCM DATASET 
Models 
AUC 
Accuracy 
Precision 
Recall 
F1 
LR 
0.755 
0.882 
0.396 
0.116 
0.173 
SVM 
0.703 
0.889 
0 
0 
0 
Random Forest 
0.737 
0.889 
0 
0 
0 
XGBoost 
0.729 
0.886 
0.327 
0.063 
0.104 
mi-Net 
0.597 
0.641 
0.220 
0.422 
0.231 
MI-Net 
0.665 
0.813 
0.364 
0.414 
0.356 
MI-Net+DS 
0.586 
0.731 
0.358 
0.290 
0.179 
MI-Net+RC 
0596 
0.861 
0.353 
0.358 
0.312 
Att. Net 
0.642 
0.861 
0.368 
0.244 
0.281 
Gated Att. Net 
0.607 
0.755 
0.319 
0.354 
0.262 
AMI-Net 
0.702 
0.818 
0.399 
0.468 
0.379


## Page 6


gated attention-based pooling, would be tested and reported in 
this paper. 
The results were shown in Figure 4 and 5. The performance 
of sum pooling and gated-attention based pooling on instance-
level and bag-level respectively were better than other MIL 
pooling methods. Moreover, the model with max pooling on 
instance-level was the worst, revealing that symptoms were 
correlated to each other on different embedding dimensions. It 
would be insufficient for a diagnosis if the information was only 
captured in one dimension, 
D. Influence of Data Noise 
Since data collected from real-world studies are often in various 
degrees of inaccuracy and fuzziness, experiments were carried 
out to evaluate how the performance of the proposed model 
fluctuated with different data noise ratios using F1-score. There 
are two dimensions in data noise, namely feature noise and label 
noise. To test the feature noise, 1, 2, 3, 4 and 5 symptoms were 
randomly changed in each training sample. If the number of 
symptoms in a sample was lower than the required number of 
symptoms to change, new symptoms were added randomly. 
Regarding the test of label noise, the ratio of labels was inverted 
from 0.1 to 1.0 with the 0.1 increment in the training set.  
The results of feature noise influence on different models 
were shown in Figure 6. Although some symptoms were 
randomly changed, the performance of our proposed method 
was still better than all other models and did not have much 
fluctuations. The MIL methods had more steady performance 
than all other machine learning algorithms, because of their 
ability to capture and to utilize effective information, that made 
them reliable in the real-life applications. The influence of label 
noise was displayed in Figure 7. When the proportion of inverted 
labels increased, the F1-score converged around 0.2 and 0.1 
respectively, labelling all samples in validation set to be positive. 
Hence, our proposed method still performed the best in most of 
the time, suggesting that it is more noise resistant than others. 
E. Influence of Incomplete Data 
In this section, the performance of our proposed method was 
studied using the incomplete datasets. 1, 2, 3, 4 and 5 symptoms 
were randomly deleted from each training sample. If the number 
of symptoms in a sample was less than the number of deletions, 
all symptoms would be removed. The F1-score was used for the 
performance comparison. 
The results, illustrated in Figure 8, showed that the AMI-Net 
was found to be more robust than all other models under the 
condition of incomplete data. Since a patient does not always 
take all examinations and clinical measurements, a clinician 
very often infers missing information using his/her experience 
and knowledge during the diagnosis. Our proposed method 
offers a feasible strategy, shown to be resistant to the incomplete 
data, for the medical diagnosis. 
F. Visualization of Attention 
The gated attention-based MIL pooling layer was able to select 
the most informative instances, i.e., symptoms. To make our 
proposed method interpretable, the visualization of attention 
mechanism on two examples were given in Figure 9. With the 
darker the color, the more important it would be. In the WM 
dataset, personal income 3000-5000, unmarried, length of 
stay<25 days and MECT<=1 dominated the prediction of 
schizophrenia relapse. In the prediction of meridian obstruction 
in the TCM dataset, decreased defecation, urine color is yellow, 
heavy legs and dropping had larger weights to indicate their 
significance. 
 
Figure 3. Comparison of different number of heads. 0 
denotes the model without multi-head attention. 
 
Figure 4. Comparison of different MIL pooling 
methods on the TCM dataset. 
 
Figure 5. Comparison of different MIL pooling 
methods on the WM dataset.


## Page 7


VI. 
CONCLUSION 
To develop an effective and efficient framework for medical 
diagnosis from incomplete and low-quality data, a novel 
attention based multi-instance neural network (AMI-Net) was 
proposed, that firstly captured intra-relations among instances 
and, secondly, selected key instances for the final classification. 
The experimental results demonstrated the superiority of our 
proposed method and MIL methods in real-life applications, in 
terms of Precision, Recall and F1-score. Further analysis 
suggested our method was interpretable, very steady and more 
preferable than other models under noisy and incomplete data 
conditions. 
The study shown that AMI-Net was very effective to deal 
with medical diagnosis problem in real life and support the real-
world study in medicine. 
REFERENCES 
[1] Sun, X., Tan, J., Tang, L., Guo, J.J. and Li, X., 2018. Real world evidence: 
experience and lessons from China. Bmj, 360, p.j5262. 
[2] Zhou, Z.H., 2017. A brief introduction to weakly supervised learning. 
National Science Review, 5(1), pp.44-53. 
[3] Dietterich, T.G., Lathrop, R.H. and Lozano-Pérez, T., 1997. Solving the 
multiple instance problem with axis-parallel rectangles. Artificial 
intelligence, 89(1-2), pp.31-71.  
[4] Ilse, M., Tomczak, J.M. and Welling, M., 2018. Attention-based deep 
multiple instance learning. arXiv preprint arXiv:1802.04712. 
[5] Quellec, G., Cazuguel, G., Cochener, B. and Lamard, M., 2017. Multiple-
instance learning for medical image and video analysis. IEEE reviews in 
biomedical engineering, 10, pp.213-234. 
[6] Wang, Z., Poon, J., Sun, S. and Poon, S., 2018. CNN based Multi-Instance 
Multi-Task Learning for Syndrome Differentiation of Diabetic Patients. 
arXiv preprint arXiv:1812.07764. 
[7] Zhao, Y., He, L., Xie, Q., Li, G., Liu, B., Wang, J., Zhang, X., Zhang, X., 
Luo, L., Li, K. and Jing, X., 2015. A novel classification method for 
syndrome differentiation of patients with AIDS. Evidence-Based 
Complementary and Alternative Medicine, 2015. 
[8] Dundar, M., Krishnapuram, B., Rao, R.B. and Fung, G.M., 2007. Multiple 
instance learning for computer aided diagnosis. In Advances in neural 
information processing systems (pp. 425-432). 
[9] Manivannan, S., Cobb, C., Burgess, S. and Trucco, E., 2017. Subcategory 
classifiers for multiple-instance learning and its application to retinal 
nerve fiber layer visibility classification. IEEE transactions on medical 
imaging, 36(5), pp.1140-1150. 
[10] Zhang, Q. and Goldman, S.A., 2002. EM-DD: An improved multiple-
instance learning technique. In Advances in neural information 
processing systems (pp. 1073-1080). 
[11] Andrews, S., Tsochantaridis, I. and Hofmann, T., 2003. Support vector 
machines for multiple-instance learning. In Advances in neural 
information processing systems (pp. 577-584). 
[12] Zhou, Z.H., Sun, Y.Y. and Li, Y.F., 2009, June. Multi-instance learning 
by treating instances as non-iid samples. In Proceedings of the 26th 
annual international conference on machine learning (pp. 1249-1256). 
ACM. 
[13] Wei, X.S., Wu, J. and Zhou, Z.H., 2014, December. Scalable multi-
instance learning. In Data Mining (ICDM), 2014 IEEE International 
Conference on (pp. 1037-1042). IEEE. 
[14] Foulds, J. and Frank, E., 2010. A review of multi-instance learning 
assumptions. The Knowledge Engineering Review, 25(1), pp.1-25. 
[15] Ramon, J. and De Raedt, L., 2000, January. Multi instance neural 
networks. In Proceedings of the ICML-2000 workshop on attribute-value 
and relational learning (pp. 53-60). 
 
 
Figure 6. Test for the influence of feature noise                                       Figure 7. Test for the influence of label noise 
 
 
 
Figure 8. Test for the influence of incomplete data 
 
 
Figure 9. An example of informative instances selection


## Page 8


[16] Zhou, Z.H. and Zhang, M.L., 2002, August. Neural networks for multi-
instance learning. In Proceedings of the International Conference on 
Intelligent Information Technology, Beijing, China (pp. 455-459). 
[17] Zhang, M.L. and Zhou, Z.H., 2004. Improve multi-instance neural 
networks through feature selection. Neural Processing Letters, 19(1), 
pp.1-10. 
[18] Yan, Y., Wang, X., Guo, X., Fang, J., Liu, W. and Huang, J., 2018, 
November. Deep Multi-instance Learning with Dynamic Pooling. In 
Asian Conference on Machine Learning (pp. 662-677). 
[19] Wang, X., Yan, Y., Tang, P., Bai, X. and Liu, W., 2018. Revisiting 
multiple instance neural networks. Pattern Recognition, 74, pp.15-24. 
[20] Xu, K., Ba, J., Kiros, R., Cho, K., Courville, A., Salakhudinov, R., Zemel, 
R. and Bengio, Y., 2015, June. Show, attend and tell: Neural image 
caption generation with visual attention. In International conference on 
machine learning (pp. 2048-2057). 
[21] Lin, Z., Feng, M., Santos, C.N.D., Yu, M., Xiang, B., Zhou, B. and 
Bengio, Y., 2017. A structured self-attentive sentence embedding. arXiv 
preprint arXiv:1703.03130. 
[22] Qi, C.R., Su, H., Mo, K. and Guibas, L.J., 2017. Pointnet: Deep learning 
on point sets for 3d classification and segmentation. Proc. Computer 
Vision and Pattern Recognition (CVPR), IEEE, 1(2), p.4. 
[23] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, 
A.N., Kaiser, Ł. and Polosukhin, I., 2017. Attention is all you need. 
In Advances in Neural Information Processing Systems (pp. 5998-6008). 
[24] Mikolov, T., Sutskever, I., Chen, K., Corrado, G.S. and Dean, J., 2013. 
Distributed 
representations 
of 
words 
and 
phrases 
and 
their 
compositionality. In Advances in neural information processing systems 
(pp. 3111-3119). 
[25] e, K., Zhang, X., Ren, S. and Sun, J., 2016. Deep residual learning for 
image recognition. In Proceedings of the IEEE conference on computer 
vision and pattern recognition (pp. 770-778). 
[26] Zaheer, M., Kottur, S., Ravanbakhsh, S., Poczos, B., Salakhutdinov, R.R. 
and Smola, A.J., 2017. Deep sets. In Advances in Neural Information 
Processing Systems (pp. 3391-3401). 
[27] Qi, C.R., Su, H., Mo, K. and Guibas, L.J., 2017. Pointnet: Deep learning 
on point sets for 3d classification and segmentation. Proc. Computer 
Vision and Pattern Recognition (CVPR), IEEE, 1(2), p.4. 
[28] Yang, Z., Yang, D., Dyer, C., He, X., Smola, A. and Hovy, E., 2016. 
Hierarchical attention networks for document classification. In 
Proceedings of the 2016 Conference of the North American Chapter of 
the Association for Computational Linguistics: Human Language 
Technologies (pp. 1480-1489). 
[29] Dauphin, Y.N., Fan, A., Auli, M. and Grangier, D., 2017, August. 
Language modeling with gated convolutional networks. In Proceedings 
of the 34th International Conference on Machine Learning-Volume 
70 (pp. 933-941). JMLR. org. 
[30] Hu, D., 2018. An Introductory Survey on Attention Mechanisms in NLP 
Problems. arXiv preprint arXiv:1811.05544. 
[31] Shen, Z., Li, J., Su, Z., Li, M., Chen, Y., Jiang, Y.G. and Xue, X., 2017, 
July. Weakly supervised dense video captioning. In 2017 IEEE 
Conference on Computer Vision and Pattern Recognition (CVPR) (pp. 
5159-5167). IEEE. 
[32] Zhou, Y., Sun, X., Liu, D., Zha, Z. and Zeng, W., 2017. Adaptive pooling 
in multi-instance learning for web video annotation. In The IEEE 
International Conference on Computer Vision (ICCV).(Oct 2017). 
[33] Shen, T., Zhou, T., Long, G., Jiang, J., Pan, S. and Zhang, C., 2018, April. 
Disan: Directional self-attention network for rnn/cnn-free language 
understanding. In Thirty-Second AAAI Conference on Artificial 
Intelligence. 
[34] Tan, Z., Wang, M., Xie, J., Chen, Y. and Shi, X., 2018, April. Deep 
semantic role labeling with self-attention. In Thirty-Second AAAI 
Conference on Artificial Intelligence. 
[35] Verga, P., Strubell, E. and McCallum, A., 2018. Simultaneously Self-
Attending to All Mentions for Full-Abstract Biological Relation 
Extraction. arXiv preprint arXiv:1802.10569. 
[36] Poon, S.K., Poon, J., McGrane, M., Zhou, X., Kwan, P., Zhang, R., Liu, 
B., Gao, J., Loy, C., Chan, K. and Man-yuen Sze, D., 2011. A novel 
approach in discovering significant interactions from TCM patient 
prescription 
data. 
International journal 
of 
data 
mining and 
bioinformatics, 5(4), pp.353-368. 
[37] Chen, J., Poon, J., Poon, S.K., Xu, L. and Sze, D.M., 2015. Mining 
symptom-herb patterns from patient records using tripartite graph. 
Evidence-Based Complementary and Alternative Medicine, 2015. 
[38] Coffey, J.C. and O'Leary, D.P., 2016. The mesentery: structure, function, 
and role in disease. The lancet Gastroenterology & hepatology, 1(3), 
pp.238-247. 
[39] Kingma, D.P. and Ba, J., 2014. Adam: A method for stochastic 
optimization. arXiv preprint arXiv:1412.6980. 
[40] Grangier, D. and Melvin, I., 2010. Feature set embedding for incomplete 
data. In Advances in Neural Information Processing Systems (pp. 793-
801). 
[41] Hosmer Jr, D.W., Lemeshow, S. and Sturdivant, R.X., 2013. Applied 
logistic regression (Vol. 398). John Wiley & Sons. 
[42] Xu, W., Zhao, Y., Nian, S., Feng, L., Bai, X., Luo, X. and Luo, F., 2018. 
Differential analysis of disease risk assessment using binary logistic 
regression with different analysis strategies. Journal of International 
Medical Research, p.0300060518777173. 
[43] Wang, L. ed., 2005. Support vector machines: theory and applications 
(Vol. 177). Springer Science & Business Media. 
[44] Ho, T.K., 1995, August. Random decision forests. In Document analysis 
and recognition, 1995., proceedings of the third international conference 
on (Vol. 1, pp. 278-282). IEEE. 
[45] Chen, T. and Guestrin, C., 2016, August. Xgboost: A scalable tree 
boosting system. In Proceedings of the 22nd acm sigkdd international 
conference on knowledge discovery and data mining (pp. 785-794). 
ACM.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1904_04460v1_attention_based_multi_instance_neural_network_for_medical_diagnosis_from_incompl
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1904_04460V1_ATTENTION_BASED_MULTI_INSTANCE_NEURAL_NETWORK_FOR_MEDICAL_DIAGNOSIS_FROM_INCOMPL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.08514v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1904.08514v2_DeepNovoV2__Better_de_novo_peptide_sequencing_with_deep_learning

> Source: 1904.08514v2_DeepNovoV2__Better_de_novo_peptide_sequencing_with_deep_learning.pdf

> Pages: 9

---


## Page 1


DEEPNOVOV2: BETTER DE NOVO PEPTIDE SEQUENCING BY
DEEP LEARNING
A PREPRINT
Rui Qiao
Department of Statistics and Actuarial Science
University of Waterloo
rqiao@uwaterloo.ca
Ngoc Hieu Tran
David R. Cheriton School of Computer Science
University of Waterloo
nh2tran@uwaterloo.ca
Lei Xin
Bioinformatic Solution Incorporation
lxin@bioinfor.com
Baozhen Shan
Bioinformatic Solution Incorporation
bshan@bioinfor.com
Ming Li
David R. Cheriton School of Computer Science
University of Waterloo
nh2tran@uwaterloo.ca
Ali Ghodsi
Department of Statistics and Actuarial Science
University of Waterloo
ali.ghodsi@uwaterloo.ca
May 23, 2019
ABSTRACT
Personalized cancer vaccines are envisioned as the next generation rational cancer immunotherapy.
The key step in developing personalized therapeutic cancer vaccines is to identify tumor-speciﬁc
neoantigens that are on the surface of tumor cells. A promising method for this is through de novo
peptide sequencing from mass spectrometry data. In this paper we introduce DeepNovoV2, the state-
of-the-art model for de novo peptide sequencing1. In DeepNovoV2, a spectrum is directly represented
as a set of (m/z, intensity) pairs, therefore it does not suffer from the accuracy-speed/memory trade
off problem. The model combines an order invariant network structure (T-Net) and recurrent neural
networks and provides a complete end-to-end training and prediction framework to sequence patterns
of peptides. Our experiments on a wide variety of data from different species show that DeepNovoV2
outperforms previous state-of-the-art methods, achieving 13.01-23.95 % higher accuracy at the
peptide level.
1
Introduction
1.1
Personalized Cancer Vaccines
The human leukocyte antigen (HLA) system regulates the immune system by bringing short peptides to the surface of
cells. These peptides, often referred to as HLA peptides, are produced from digested proteins that are broken down
in the proteasomes. When a cell is infected by a virus or grows malignant, non-self HLA peptides (from the virus or
mutated proteins) will be presented on the surface of the cell so that T cells could recognize and subsequently kill the
cell[1]. For cancer cells, these mutated tumor-speciﬁc HLA peptides are referred to as neoantigens.
Based our current understanding of immunology, the generation of an antitumor immune response relies on the
activation of professional antigen-presenting cells (APCs)[2]. Personalized cancer vaccines are designed to activate
APCs, and to hopefully promote an efﬁcient antitumor immune response in the patient’s immune system. Neoantigens
1Our
pytorch
implementation
of
DeepNovoV2
and
the
test
dataset
could
be
downloaded
here:
https://github.com/volpato30/DeepNovoV2
arXiv:1904.08514v2  [cs.LG]  22 May 2019


## Page 2


A PREPRINT - MAY 23, 2019
are peptides that are found on cancer cells and not on normal cells, so they represent ideal targets for cancer vaccines.
Up until now, several independent studies have shown successful clinical trials for patients with melanoma[3][4][5].
However, a major challenge for personalized cancer vaccine therapy remains the efﬁcient identiﬁcation and validation
of neoantigens (tumor-speciﬁc antigens) for each patient[6]. Currently, candidate neoantigens could be identiﬁed with a
proteogenomics method that involves three steps: First, perform whole exome sequencing and RNA sequencing on
the patient’s tumor samples to ﬁnd somatic mutations, and then build a tailored protein database from those identiﬁed
mutations. Second, perform a tailored database search on the mass spectrums of tumor samples to ﬁnd candidate tumor
speciﬁc antigens[7]. Third, the reported candidate neoantigens are further ﬁltered with binding afﬁnity prediction tools
like NetMHCpan[8].
However, Tran et al. (2019) noted that this proteogenomics method might be suboptimal because existing database
search engines (used in step two) are not designed for HLA peptides and have bias towards trypic peptides, and because
database search engines might have sensitivity and speciﬁcity issues when dealing with the large search space created
by exome sequencing[9]. Alternatively, Tran et al. (2019) proposed a workﬂow that could identify neoantigens directly
and solely from mass spectrometry (MS) data. In this workﬂow, a personalized de novo peptide sequencing model is
trained by the identiﬁed peptide-spectrum matches from a database search result. The trained model is then applied on
the unidentiﬁed mass spectrums to predict new peptide sequences. The authors reported that their workﬂow was capable
of ﬁnding highly conﬁdent neoantigens which had not been reported by the proteogenomics method. The success of
this novel workﬂow relies heavily on an accurate and efﬁcient de novo peptide sequencing algorithm.
1.2
Mass Spectrometry (MS)
MS is a popular and powerful tool for chemical analysis which has contributed in different areas of research including,
but not limited to, chemistry, physics and biochemistry[10]. In MS, samples (typically in liquid or gas form) are
loaded into a mass spectrometer which consists of an ion source, a mass analyzer, and an ion detector. The ion source
would produce gas phase ions from the sample being studied, the mass analyzer would separate those ions according
to their mass-to-charge ratio (m/z), and the ion detector would detect the ions and record their relative abundance.
Therefore the outputs of a mass spectrometer are spectrums. Each spectrum is a set of (m/z, intensity) pairs where
the intensity value represents the abundance of ions with the mass-to-charge ratio m/z.
Figure 1: Diagram of tandem mass spectrometry
Tandem mass spectrometry (MS/MS) is a technique for utilizing two or more different types of mass analyzers to
enhance analysis through fragmentation of the input molecules[11]. It is widely used in proteomics to analyze protein
and peptide sequences. In this approach, biological samples (e.g. tumor tissues, plasma and urine) would be pre-
processed with a certain protease (e.g. trypsin and Endoproteinase Lys-C) such that the proteins are cleaved into short
peptides. These peptides are then fed into a spectrometer and the output is denoted as MS1 spectrum. Each signal in the
MS1 spectrum is called a precursor ion, which typically represents a certain kind of peptide. Next, some precursor ions
are selected to be fragmented into smaller pieces called fragment ions. These fragments are further fed into another
mass spectrometer. The ﬁnal output is denoted as MS2 spectrums. Figure 1 shows the process of MS/MS.
From the precursor mass (i.e. mass of the peptide) and the fragment ion signals contained in the MS2 spectrum it
is possible to recover the exact amino acid sequence of the original peptide. This solution is called de novo peptide
sequencing. To some extent this challenge is similar to the image captioning problem in computer vision. We need to
2


## Page 3


A PREPRINT - MAY 23, 2019
Figure 2: Sample MS2 spectrum
ﬁnd a sequence of amino acids (or words), under some constraints (the total mass of the sequence should equal the
precursor mass), that best describe the spectrum (or image). A sample MS2 spectrum for peptide "SDGVIKVF" is
shown in Figure 2.
1.3
De novo Peptide Sequencing
In proteomics, de novo peptide sequencing is the key technology for ﬁnding new peptide or protein sequences.
It has successful applications in assembling monocolonal antibody sequences (mAbs)[12] and great potential in
identifying neoantigens for personalized cancer vaccines[9][13]. Given the importance of the de novo peptide sequencing
technology, substantial research has been done in this area and different tools have been proposed[14][15][16][17][18].
In 2017, Tran et al. ﬁrst introduced deep learning to de novo peptide sequencing and proposed DeepNovo, a neural
network based de novo peptide sequencing model[19] for Data Dependent Acquisition (DDA) MS data. Inspired
by the success of image captioning models[20], DeepNovo integrated two fundamental types of neural networks,
Convolutional Neural Networks (CNNs) and Long short-term memory (LSTM), to extract features from both the
spectrum and the "language model" of peptides. In DeepNovo, each spectrum is represented as a long intensity vector
and CNNs are applied on segments of this vector to extract features and make predictions of the next amino acid. CNNs
have been proven as effective tools for pattern recognition in different applications such as image classiﬁcation, object
detection, and sentiment analysis[21][22][23]. By applying CNNs to the intensity vector, DeepNovo could learn from
the noise spectrum. It is reported that DeepNovo outperformed the decade-long state-of-the-art records of de novo
sequencing algorithms (PEAKS[24]) by a large margin of 38.1–64.0% at the peptide level[19].
In 2019, Tran et al. further extended DeepNovo on Data Independent Acquisition (DIA) MS data and proposed
DeepNovo-DIA[13], the ﬁrst de novo peptide sequencing algorithm for DIA MS/MS spectrums. Compared to DDA,
DIA data are in general harder to interpret because the spectrum generated by DIA often contains fragment ions from
multiple peptides. However, the multiplexity and noise in the DIA spectrums make deep neural networks a more
reasonable choice. In DeepNovo-DIA each detected feature is represented by 5 spectrums, where each spectrum is
discretized into an intensity vector as in DeepNovo. Thus the input to DeepNovo-DIA is a matrix of shape 5 by the
length of intensity vector. DeepNovo-DIA then applies 2D convolution on the input to utilize the information provided
by the extra dimension of retention time and hopefully to learn the coeluting patterns. It is also worth noting that Tran
et al. reported that by changing cross entropy loss to focal loss[25], they observed a signiﬁcant improvement on peptide
accuracy[13].
In this paper we propose DeepNovoV2: a model combining an order invariant network structure (T-Net) and recurrent
neural networks. In addition, this method utilizes local dynamic programming to solve the complex optimization task of
de novo sequencing. Our experiments on datasets from a wide variety of species show that DeepNovoV2 outperforms
the current state-of-the-art model DeepNovo by a signiﬁcant margin of at least 13%, on a peptide level.
In Section 2 of this paper we will explain how we extract features from spectrums and the structure of our proposed
model, and in Section 3 we will demonstrate our experiment results on different datasets.
3


## Page 4


A PREPRINT - MAY 23, 2019
2
Methods
2.1
Spectrum Representation
Previously in DeepNovo, spectrums are represented as intensity vectors where each index of the vector represents a
small m/z bin and the value represents the sum of intensities of all peaks which fall into that bin. This representation of
spectrum naturally has the problem of accuracy versus speed/memory trade-off. For example, by default, DeepNovo use
a spectrum resolution of 10 which means every peak within a 0.1 Da m/z bin will be merged together and represented
as an element of the intensity vector. However, we lose a lot of useful information about the exact location of each
peak during the merging. Conversely, if we need to build a more accurate model and increase the resolution, the
result will be a signiﬁcantly longer intensity vector and the model will need more memory and time to be trained. In
DeepNovoV2, to solve the accuracy-speed/memory trade off problem, we propose to directly represent the spectrum as
a set of (m/z, intensity) pairs. For each spectrum we select the top n most intense peaks (by default we choose n = 500),
and represent the spectrum as {(m/zk, ik)}n
k=1. Further, we denote Mobserved = (m/z1, · · · , m/zn) as the observed
m/z vector and i = (i1, · · · , in).
2.2
Feature Extraction
We denote the number of tokens as nvocab and number of ion types as nion. To make a fair comparison with DeepNovo,
we keep nvocab = 26 (20 amino acid residues, three variable modiﬁcations, and three special tokens: "start", "end"
and "pad") and use the same eight ion types (b, y, b(2+), y(2+), b-H2O, y-H2O, b-NH3, and y-NH3) as in the original
implementation of DeepNovo[19]. Similar to DeepNovo, at each step we compute the theoretical m/z location for
each token and ion type pair. The result is a matrix of shape (nvocab, nion) and denoted as Mtheoretical. Next we
expand the dimension of Mobserved to make it a 3-dimensional tensor of shape (n, 1, 1), and then repeat Mobserved on
second dimension for nvocab times and on third dimension for nion times. The result is denoted as M′
observed and it is
a tensor of shape (n, nvocab, nion). Similarly, we expand Mtheoretical to the shape of (1, nvocab, nion), repeat on ﬁrst
dimension for n times, and denote the result as M′
theoretical. We can then compute the m/z difference tensor (denoted
as D) in which each element represents the difference between the m/z value for an observed peak and the theoretical
m/z for a token and ion type pair.
D = M′
observed −M′
theoretical
(1)
It is worth noting that Equation 1 could be computed efﬁciently by using the "broadcast" behaviour in popular
frameworks like Tensorﬂow[26] and PyTorch[27].
σ(D) = exp{−|D| ∗c}
(2)
Based on expert knowledge of de novo peptide sequencing, we designed an activation function σ shown in Equation 2.
Here the exponential and absolute operations are all element-wise operations. The intuition for σ is that an observed
peak could only be considered matching a theoretical m/z location if the absolute m/z difference is small. For example,
if we set c = 100, then an observed peak that is 0.02 Da away from a theoretical location would generate a signal of
e−2 ≈0.135, which is only one seventh of the signal of a perfect match. In our experiments, we tried setting c to be
a trainable parameter and updating it through backpropagation. It shows similar performance with setting c = 100;
therefore, for the simplicity of the model, we choose to ﬁx c to be 100.
F = σ(D)′ ⊕I
(3)
Finally, the feature matrix F for prediction is simply the concatenation of σ(D) and i, as shown in Equation 3. Here
σ(D)′ is a n by nvocab × nion matrix reshaped from σ(D), I is a N by 1 matrix reshaped from i and ⊕represents
concatenation along the second dimension.
2.3
T-Net
A spectrum is set of (m/z, intensity) pairs, which means the order of peaks should be irrelevant. Therefore, the
prediction network should have an order invariant property with respect to the ﬁrst dimension of F. To the best of our
knowledge, T-Net (the building block of Point Net[28]) is the ﬁrst model designed for this kind of order invariant data,
so we choose to use it to process F. In essence, T-Net is composed of three 1d convolutional layers with kernel size
one, followed by a global max pooling layer and three fully connected layers. As with DeepNovo[19], we could add
a LSTM aside from the T-net to make use of the language model information of peptides. The structure for T-Net is
shown in Figure 3 and the full model structure of DeepNovoV2 is shown in Figure 4. As suggested by Tran et al.[13],
we used focal loss[25] instead cross entropy loss when training the model.
4


## Page 5


A PREPRINT - MAY 23, 2019
Figure 3: T-Net
2.4
Initial State for LSTM
Similar to DeepNovo[19], we could include a LSTM module to capture the "language model" for peptides. To make
good predictions about the next amino acid, it is important for the LSTM to be initialized with information about
the original spectrum. DeepNovo used a spectrum CNN to extract features from intensity vectors and then used the
extracted features to initialize the LSTM. In DeepNovoV2, we replaced the spectrum CNN structure with a simple
embedding matrix. Speciﬁcally, we created a sinusoidal m/z positional embedding, as suggested by Vaswani et al[29]:
PE(loc,2k) = sin(loc/10000
2k
dlstm )
PE(loc,2k+1) = cos(loc/10000
2k
dlstm )
Here loc represents the m/z location after discretization, and dlstm represents the dimension of the LSTM module. The
sinusoidal embedding has a desired property that any distance m, PEloc+m could be represented as a linear function of
PEloc[29]. This property is important because in mass spectrums the m/z differences between observed peaks contains
useful information that indicates which amino acids could possibly exist. By using the sinusoidal positional embeddings,
we anticipate that the model could easily learn to extract information from the m/z difference between peaks.
For each spectrum {(m/zk, ik)}n
i=1, we denote the positional embedding for m/zk as ek. The spectrum representation
s is computed by:
s =
n
X
k=1
ikek
(4)
Next, the initial hidden states of the LSTM module (i.e. h0 and c0) will be initialized to S. By replacing spectrum CNN
to a ﬁxed positional embedding matrix, we reduced the number of parameters and computation needed in the model.
Our experiment results show that initializing with s gives similar results when comparing to initializing with the result
of spectrum CNN.
2.5
Training Parameters
We train DeepNovoV2 with Adam algorithm[30] with an initial learning rate of 10−3. After every 300 training steps, the
loss on validation set is computed. If the validation loss has not achieved a new low in the most recent ten evaluations,
then the learning rate is dropped by half.
5


## Page 6


A PREPRINT - MAY 23, 2019
Figure 4: Structure of DeepNovoV2
DeepNovo
without lstm
DeepNovo
with lstm
DeepNovoV2
without lstm
DeepNovoV2
with lstm
amino acid recall
66.44%(±0.18%)
67.81%(±0.21%)
71.59%(±0.18%)
72.46%(±0.15%)
amino acid precision
66.42%(±0.22%)
67.67%(±0.25%)
71.65%(±0.24%)
72.25%(±0.20%)
peptide recall
30.33%(±0.15%)
32.96%(±0.31%)
38.10%(±0.06%)
39.24%(±0.29%)
Table 1: Amino acid recall, amino acid precision and peptide recall on ABRF DDA data
3
Results and Analysis
3.1
Evaluation Metrics
To evaluate the performance of de novo sequencing models, we use the same metrics as proposed by DeepNovo[19]. A
predicted amino acid is considered "matched" with a real amino acid if their mass difference is less than 0.1 Da and if
the preﬁx masses before them are different by less than 0.5 Da. The amino acid level recall (or precision) is deﬁned as
the ratio of the total number of matched amino acids over the total number of amino acids in real peptide sequences (or
predicted peptide sequences). And the peptide level recall denotes the fraction of real peptide sequences that are fully
correctly predicted.
3.2
Experiment Results
We tested our model on a DDA dataset of Hela samples2 (denoted as ABRF dataset). The train-valid-test split is done
in the same way suggested by DeepNovo[19], i.e. train, valid and test sets do not share any common peptides. Both
DeepNovo and DeepNovoV2 models are trained for 20 epochs. The weights with the smallest validation error are then
2PRG 2018: Evaluation of Data-Independent Acquisition (DIA) for Protein Quantiﬁcation in Academic and Core Facility Settings.
https://abrf.org/research-group/proteomics-research-group-prg
6


## Page 7


A PREPRINT - MAY 23, 2019
selected to do beam search. We also use the knapsack dynamic programming algorithms as described by Tran et al.
(2017) to limit the search space[19].
The mean value and standard deviation of metrics from 5 independent runs on ABRF dataset are shown in Table 1. The
results show that DeepNovoV2 outperforms DeepNovo by 6.85% on amino acid recall, 6.76% on amino acid precision
and 19.05% on peptide recall.
We also tested DeepNovoV2 with the cross species data published by Tran et al.[19] (MSV000081382). This data set
contains DDA mass spectrums from nine species. For each species we train a model using spectrums from the other 8
species and then test the model. In these experiments we set n = 1000.
Figure 5: Amino acid recall, amino acid precision and peptide recall of DeepNovo and DeepNovoV2
As we can see from Figure 5, DeepNovoV2 outperforms DeepNovo consistently on peptide recall, by a large margin of
13.01–23.95%.
4
Conclusion and Future Research
We propose DeepNovoV2: a neural network based de novo peptide sequencing model that outperforms the previous
state-of-the-art model by a signiﬁcant margin (at least 13% on peptide recall). This improvement is achieved through
the change in spectrum representations and the use of an order invariant network structure. We believe these techniques
could be applied to other important problems in MS such as database search or feature detection, and we continue to
research in this direction.
7


## Page 8


A PREPRINT - MAY 23, 2019
References
[1] Michal Bassani-Sternberg and David Gfeller. Unsupervised hla peptidome deconvolution improves ligand
prediction accuracy and predicts cooperative effects in peptide–hla interactions. The Journal of Immunology,
197(6):2492–2499, 2016.
[2] Zhuting Hu, Patrick A Ott, and Catherine J Wu. Towards personalized, tumour-speciﬁc, therapeutic vaccines for
cancer. Nature Reviews Immunology, 18(3):168, 2018.
[3] Patrick A Ott, Zhuting Hu, Derin B Keskin, Sachet A Shukla, Jing Sun, David J Bozym, Wandi Zhang, Adrienne
Luoma, Anita Giobbie-Hurder, Lauren Peter, et al. An immunogenic personal neoantigen vaccine for patients
with melanoma. Nature, 547(7662):217, 2017.
[4] Ugur Sahin, Evelyna Derhovanessian, Matthias Miller, Björn-Philipp Kloke, Petra Simon, Martin Löwer, Valesca
Bukur, Arbel D Tadmor, Ulrich Luxemburger, Barbara Schrörs, et al. Personalized rna mutanome vaccines
mobilize poly-speciﬁc therapeutic immunity against cancer. Nature, 547(7662):222, 2017.
[5] Beatriz M Carreno, Vincent Magrini, Michelle Becker-Hapak, Saghar Kaabinejadian, Jasreet Hundal, Allegra A
Petti, Amy Ly, Wen-Rong Lie, William H Hildebrand, Elaine R Mardis, et al. A dendritic cell vaccine increases
the breadth and diversity of melanoma neoantigen-speciﬁc t cells. Science, 348(6236):803–808, 2015.
[6] Antonella Vitiello and Maurizio Zanetti. Neoantigen prediction and the need for validation. Nature biotechnology,
35(9):815, 2017.
[7] Michal Bassani-Sternberg, Eva Bräunlein, Richard Klar, Thomas Engleitner, Pavel Sinitcyn, Stefan Audehm,
Melanie Straub, Julia Weber, Julia Slotta-Huspenina, Katja Specht, et al. Direct identiﬁcation of clinically relevant
neoepitopes presented on native human melanoma tissue by mass spectrometry. Nature communications, 7:13404,
2016.
[8] Vanessa Jurtz, Sinu Paul, Massimo Andreatta, Paolo Marcatili, Bjoern Peters, and Morten Nielsen. Netmhcpan-4.0:
Improved peptide–mhc class i interaction predictions integrating eluted ligand and peptide binding afﬁnity data.
The Journal of Immunology, 199(9):3360–3368, 2017.
[9] Ngoc Hieu Tran, Rui Qiao, Lei Xin, Xin Chen, Baozhen Shan, and Ming Li. Identifying neoantigens for cancer
vaccines by personalized deep learning of individual immunopeptidomes. bioRxiv, page 620468, 2019.
[10] Pawel L Urban. Quantitative mass spectrometry: an overview, 2016.
[11] Russell P Newton, A Gareth Brenton, Chris J Smith, and Edward Dudley. Plant proteome analysis by mass
spectrometry: principles, problems, pitfalls and recent developments. Phytochemistry, 65(11):1449–1485, 2004.
[12] Ngoc Hieu Tran, M Ziaur Rahman, Lin He, Lei Xin, Baozhen Shan, and Ming Li. Complete de novo assembly of
monoclonal antibody sequences. Scientiﬁc reports, 6:31730, 2016.
[13] Ngoc Hieu Tran, Rui Qiao, Lei Xin, Xin Chen, Chuyi Liu, Xianglilan Zhang, Baozhen Shan, Ali Ghodsi, and
Ming Li. Deep learning enables de novo peptide sequencing from data-independent-acquisition mass spectrometry.
Nature methods, 16(1):63–66, 2019.
[14] Vlado Danˇcík, Theresa A Addona, Karl R Clauser, James E Vath, and Pavel A Pevzner. De novo peptide
sequencing via tandem mass spectrometry. Journal of computational biology, 6(3-4):327–342, 1999.
[15] J Alex Taylor and Richard S Johnson. Implementation and uses of automated de novo peptide sequencing by
tandem mass spectrometry. Analytical chemistry, 73(11):2594–2604, 2001.
[16] Bin Ma, Kaizhong Zhang, Christopher Hendrie, Chengzhi Liang, Ming Li, Amanda Doherty-Kirby, and Gilles
Lajoie. Peaks: powerful software for peptide de novo sequencing by tandem mass spectrometry. Rapid communi-
cations in mass spectrometry, 17(20):2337–2342, 2003.
[17] Ari Frank and Pavel Pevzner. Pepnovo: de novo peptide sequencing via probabilistic network modeling. Analytical
chemistry, 77(4):964–973, 2005.
[18] Bernd Fischer, Volker Roth, Franz Roos, Jonas Grossmann, Sacha Baginsky, Peter Widmayer, Wilhelm Gruissem,
and Joachim M Buhmann. Novohmm: a hidden markov model for de novo peptide sequencing. Analytical
chemistry, 77(22):7265–7273, 2005.
[19] Ngoc Hieu Tran, Xianglilan Zhang, Lei Xin, Baozhen Shan, and Ming Li. De novo peptide sequencing by deep
learning. Proceedings of the National Academy of Sciences, 114(31):8247–8252, 2017.
[20] Kelvin Xu, Jimmy Ba, Ryan Kiros, Kyunghyun Cho, Aaron Courville, Ruslan Salakhudinov, Rich Zemel, and
Yoshua Bengio. Show, attend and tell: Neural image caption generation with visual attention. In International
conference on machine learning, pages 2048–2057, 2015.
8


## Page 9


A PREPRINT - MAY 23, 2019
[21] Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition.
arXiv preprint arXiv:1409.1556, 2014.
[22] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali Farhadi. You only look once: Uniﬁed, real-time object
detection. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 779–788,
2016.
[23] Yoon Kim. Convolutional neural networks for sentence classiﬁcation. arXiv preprint arXiv:1408.5882, 2014.
[24] Bin Ma, Kaizhong Zhang, Christopher Hendrie, Chengzhi Liang, Ming Li, Amanda Doherty-Kirby, and Gilles
Lajoie. Peaks: powerful software for peptide de novo sequencing by tandem mass spectrometry. Rapid communi-
cations in mass spectrometry, 17(20):2337–2342, 2003.
[25] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and Piotr Dollár. Focal loss for dense object detection. In
Proceedings of the IEEE international conference on computer vision, pages 2980–2988, 2017.
[26] Martin Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay
Ghemawat, Geoffrey Irving, Michael Isard, Manjunath Kudlur, Josh Levenberg, Rajat Monga, Sherry Moore,
Derek G. Murray, Benoit Steiner, Paul Tucker, Vijay Vasudevan, Pete Warden, Martin Wicke, Yuan Yu, and
Xiaoqiang Zheng. Tensorﬂow: A system for large-scale machine learning. In 12th USENIX Symposium on
Operating Systems Design and Implementation (OSDI 16), pages 265–283, 2016.
[27] Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang, Zachary DeVito, Zeming Lin,
Alban Desmaison, Luca Antiga, and Adam Lerer. Automatic differentiation in pytorch. In NIPS-W, 2017.
[28] Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas. Pointnet: Deep learning on point sets for 3d
classiﬁcation and segmentation. In Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition, pages 652–660, 2017.
[29] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser,
and Illia Polosukhin. Attention is all you need. In Advances in Neural Information Processing Systems, pages
5998–6008, 2017.
[30] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980,
2014.
9

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
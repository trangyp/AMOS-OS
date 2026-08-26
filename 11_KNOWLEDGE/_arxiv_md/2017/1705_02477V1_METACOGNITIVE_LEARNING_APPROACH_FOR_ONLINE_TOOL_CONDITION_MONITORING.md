---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.02477v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1705.02477v1_Metacognitive_Learning_Approach_for_Online_Tool_Condition_Monitoring

> Source: 1705.02477v1_Metacognitive_Learning_Approach_for_Online_Tool_Condition_Monitoring.pdf

> Pages: 16

---


## Page 1


1 
Metacognitive Learning Approach for Online Tool Condition Monitoring 
Mahardhika Pratamaa, Eric Dimlab, Chow Yin Laic, Edwin Lughoferd 
a)School of Computer Science and Engineering, Nanyang Technological University, Singapore, pratama@ieee.org    
b)Mechanical Engineering Programme Area, Faculty of Engineering, Universiti Teknologi Brunei, Jalan Tungku Link, Gadong BE1410, 
Bandar Seri Begawan, Brunei Darussalam, dimla@utb.edu.bn 
c)School of Engineering, RMIT University, Carlton, 3053, Victoria, Australia, chowyin.lai@rmit.edu.au  
d) Department of Knowledge-Based Mathematical Systems, Johannes Kepler University, Linz, Austria, edwin.lughofer@jku.at  
Abstract 
As manufacturing processes become increasingly automated, so should tool condition monitoring (TCM) as it is 
impractical to have human workers monitor the state of the tools continuously. Tool condition is crucial to ensure 
the good quality of products – Worn tools affect not only the surface quality but also the dimensional accuracy, 
which means higher reject rate of the products. Therefore, there is an urgent need to identify tool failures before 
it occurs on the fly. While various versions of intelligent tool condition monitoring have been proposed, most of 
them suffer from a cognitive nature of traditional machine learning algorithms. They focus on the how-to-learn 
process without paying attention to other two crucial issues – what-to-learn, and when-to-learn. The what-to-learn 
and the when-to-learn provide self-regulating mechanisms to select the training samples and to determine time 
instants to train a model. A novel tool condition monitoring approach based on a psychologically plausible 
concept, namely the metacognitive scaffolding theory, is proposed and built upon a recently published algorithm 
– recurrent classifier (rClass). The learning process consists of three phases: what-to-learn, how-to-learn, when-
to-learn and makes use of a generalized recurrent network structure as a cognitive component. Experimental 
studies with real-world manufacturing data streams were conducted where rClass demonstrated the highest 
accuracy while retaining the lowest complexity over its counterparts.   
Keyword – Prognostic Health Management, Online Learning, Evolving Intelligent System, Lifelong Learning, Nonstationary Environments, 
Concept Drifts 
1. Introduction 
To survive in the current competitive manufacturing 
industry, 
a 
company 
must 
improve 
its 
manufacturing productivity and product quality. 
Automation is a natural way forward, as automated 
machines and robots can produce parts with high 
precision and continuously without fatigue. Human 
workers can then be re-trained to perform less 
laborious and less dangerous tasks such as 
programming the machines or supervising the 
overall workflow. 
For machining operations with cutting tools such as 
drilling, milling or turning, “automation” involves 
machine tending (loading and unloading of parts), 
the actual cutting operation itself, and tool condition 
monitoring. The latter is extremely important 
because worn tools affect surface quality and 
dimensional accuracy (Dimla et al., 1997; Rehorn et 
al., 2005; Ambhore et al., 2015), thereby increasing 
reject rates and wastage, creating a detrimental 
effect on both the profit and image of the company.  
Furthermore, the cutting force needs to be increased 
when the tool is blunt, which translates to higher 
energy cost. On the whole, in the worst-case 
scenario, a catastrophic failure of the machine tool 
would result in a significant cost incur as 
replacement parts or whole machines have a very 
high capital outlay. 
While replacing worn tools too late is undesired, the 
other extreme of replacing tools to sharper ones too 
early and too frequently is also not a good idea, as 
this increases the tool costs and downtime related to 
tool replacement. As such, the ideal method is to 
have an online tool condition monitoring (TCM) 
system which constantly detects the state of the tool, 
and initiates a tool change only when this is required. 
An automated TCM system needs to perform two 
main tasks, namely sensing and monitoring 
(Elbestawi et al., 2006). Sensing means using 
sensors to obtain cutting process signals, and this 
can further be divided into two categories – direct or 
indirect sensing (Ambhore et al., 2015; Elbestawi et 
al., 2006). Indirect sensing method, the tool or the 
workpiece is analyzed at the end of the machining 
cycle, through optical measurement, surface-
finishing measurement, chip size measurement, etc. 
Disadvantages of this approach include production 
time loss for the purpose of measurement, as well as 
the inability to detect tool failure between 
measurements at an early stage before the failure 
becomes visible on the final product. Thus, it cannot 
prohibit any production waste, but just sort out bad 
items and waste in an a posteriori fashion. The 
indirect sensing technique, on the other hand, uses 
correlated variables such as machining force, 
spindle current, acoustic emission and vibration to 
determine the status of the tools.  It is intuitively 
clear that as the tool becomes blunt, it takes higher 
force and spindle current to cut through the metal. 
Therefore, by sensing these signals, one can have a 
good estimate of the tool condition.  
The 
second 
task, 
i.e. 
monitoring, 
involves 
processing the measured signals and performing 
classification or decision making. Signal processing 
may include sensor fusion (Khaleghi et al., 2013), 
transforming the time-domain signal into frequency 
domain data using Fourier Transformation (Ding, 
2008), statistical analysis, etc. Lastly, the decision-
making process will determine whether a tool is still 
usable or replacement is required. The earliest and 
simplest method is to trigger a tool change when 
certain threshold values are exceeded (Elbestawi et 
al., 2006).  Significant research efforts have been put


## Page 2


2 
into this area to make the decision making more 
reliable, for e.g. making systems which have the 
ability to learn and adapt to new information, extract 
features, learn from their experience (e.g. false 
alarm) and changes themselves to be more robust. 
This is done using a data-driven approach where a 
machine learning algorithm such as NN, etc (Dimla 
et al., 1997) is deployed to learn a set of 
manufacturing data. 
Neural networks are mathematical processing 
devices consisting of some highly interconnected 
elements, and they are excellent in performing 
nonlinear modeling, function approximation and 
pattern classification (Dimla et al., 1997). They are 
also capable of handling a large amount of data. 
Because of these strengths, they are a natural 
candidate for the decision-making task of TCM 
systems.  A survey in 1997 (Dimla et al., 1997) 
reveals that there were already at least 40 
publications discussing the use of neural networks 
for TCM, and this number continues to rise due to 
better computing power and newer algorithms for 
the training of the neural networks. Interested 
readers are also referred to (Elbestawi et al., 2006) 
for a more recent survey in 2006.  
It is understood from the literature that the vast 
majority of data-driven TCMs works in a batch 
mode due to the use of an offline machine learning 
algorithm. This drawback hinders their viability to 
deal with sensory data streams collected in an online 
real-time fashion from in-service machinery. 
Moreover, data are sampled in a very fast rate in 
modern manufacturing processes with limited 
interruption only. It is inter-correlated and means 
any shutdown leads to a complete shutdown to the 
overall production cycle. Existing works in the TCM 
have a limited capability to cater different process 
parameters because they have a fixed model 
capacity (Pratama et al., 2013). 
Recent advances in the area of Evolving Intelligent 
System (EIS) (Angelov et al., 2010, Mouchaweh. 
Lughofer, 2012) offers a promising breakthrough for 
the TCM because it strengthens the so-called 
“maintenance on-demand” paradigm (Scheffer, 
2004) which makes continuous monitoring of tool 
condition on the fly possible, while engaging the 
cutting process. The salient feature of the EIS is 
perceived in its online learning trait providing an 
effective avenue in dealing with data streams and 
appropriately updating models in dynamically 
changing, non-stationary processes with low 
memory complexity and fast training speed. They 
play vital roles to the success of the TCM in the 
high-speed milling process. The EIS adopts an open 
structure, which can start its training process from 
scratch with an empty rule base. Its structure is self-
evolved in the single-pass learning mode, which 
suits to the degree of nonlinearity and non-stationary 
characteristics of a system (Lughofer, 2011). This 
trait brings significant advantage to the TCM 
because the machining parameters vary to meet 
production 
requirements. 
Furthermore, 
cutter 
degradation often leads to a gradual change of 
machining behaviors which demand a self-
organizing scenario to adapt to such conditions. For 
real-time deployment, the EIS, however, carries 
some bottlenecks as a result of its cognitive trait. The 
vast majority of existing EISs are crafted in the fully 
supervised training scenario which results in costly 
labeling cost. On top of that, current EISs have not 
characterized a plug-and-play characteristic due to 
the absence of important learning modules making 
them over-dependent on pre-and/or post-processing 
steps (Pratama et al, 2015(b)).  
This paper presents a metacognitive learning 
approach for an online tool condition monitoring. A 
novel TCM is developed using a recently published 
metacognitive scaffolding learning machine, termed 
Recurrent Classifier (rClass) (Pratama et al., 
2015(b)). rClass actualises three components of 
metacognition in psychology, namely what-to-learn, 
how-to-learn, when-to-learn, into the machine 
learning context with sample deletion strategy, 
sample learning strategy, sample reserved strategy 
respectively (Suresh et al., 2010). The sample 
deletion strategy is developed under the roof of an 
online active learning scenario – the conflict 
measure – which puts into perspective the semi-
supervised working principle (Lughofer, 2013). The 
semi-supervised working principle comes into the 
picture because it prevents continuous labeling of 
data streams which leads to a significant reduction 
of execution time, annotation efforts by an operator 
as 
well 
as 
an 
improvement 
of 
model’s 
generalization. Also, the original version of the 
what-to-learn module of rClass is enhanced here to 
address the class imbalanced issue. The how-to-
learn scenario is constructed under the Scaffolding 
theory – a prominent tutoring theory for a learner to 
study a complex learning task (Wood, 2001). The 
Scaffolding theory supports the plug-and-play 
paradigm because of its three components: 
complexity reduction, fading and problematizing. 
The complexity reduction aims to simplify learning 
complexity and is realized with the input weighting 
scenario to cope with the curse of dimensionality. 
The problematizing is meant to address concept 
drifts in the data stream and includes rule growing 
scenario to cope with the sudden concept drift, rule 
forgetting scenario to handle the gradual concept 
drift, rule splitting scenario to address the 
incremental concept drift and rule recall scenario to 
overcome the cyclic concept drift. Fading scenario 
targets model’s complexity and is implemented 
using the rule pruning scenario.  
rClass is developed under a generalized recurrent 
network structure where it combines a generalized 
Takagi-Sugeno-Kang (TSK) fuzzy rule and a local 
recurrent network structure (Juang et al., 2010). The 
local recurrent network structure is put forward to


## Page 3


3 
overcome dependency on time-delayed input 
variable and temporal system dynamic while 
maintaining the local property playing a key role to 
flexibility and stability of EIS. The generalized TSK 
fuzzy system synergies the multivariate Gaussian 
function as the rule premise while integrating a 
Chebyshev polynomial up to a second order. The 
multivariate Gaussian function aims to generate a 
non-axis parallel ellipsoidal cluster while the 
Chebyshev function is meant to rectify the mapping 
capability of first order TSK polynomial (Patra, 
2002). The metacognitive TCM methodology here 
conveys the following advantages over existing 
approaches: 1) it works fully in the single-pass 
learning mode, which renders it compatible for 
online real-time deployment; 2) it adopts an open 
structure which adapts flexibly to any variations of 
data streams. Furthermore, the problematizing of the 
Scaffolding theory helps to handle various concept 
drifts; 3) it incurs low labelling cost by operators and 
is seen as a semi-supervised machine in some sense; 
4) it realises the plug-and-play working principle 
where all learning modules are embedded in a single 
training process without any pre-and/or post-
training steps; 5) its recurrent structure makes 
possible to cope with the temporal characteristic of 
a machining process. It is evident that many real-
world industrial processes feature strong temporal 
dependencies among subsequent patterns whereas a 
feedforward network architecture discounts the 
order of data presentation unless with the use of 
time-delayed input variables; 6) a modification of 
the what-to-learn part in this paper makes possible 
to cope with the class imbalanced issue.     
The contributions of this paper are summed up as 
follows: 1) this paper presents a novel TCM inspired 
by 
prominent 
concepts 
of 
Metacognitive 
Scaffolding 
learning; 
2) 
the 
what-to-learn 
component of rClass is generalized here to 
overcome the class imbalance problem; 3) Real-time 
experiment using a real-world manufacturing plant 
was done where raw manufacturing data were 
collected, pre-processed; 4) The efficacy of a novel 
TCM was numerically validated using real-world 
manufacturing data. It was also compared against 
state-of-the-art algorithms. It is shown that our 
algorithm outperformed its counterparts in both 
accuracy and complexity.  
The remainder of this paper is structured as follows: 
Section 2 outlines literature survey over existing 
TCMs, Section 3 elaborates learning policy of 
rClass, Section 4 discusses problem description of a 
real-world manufacturing plant, Section 5 describes 
our experiments and comparisons with prominent 
algorithms, concluding remarks are drawn in the last 
section of this paper.  
2. Literature Survey 
A. Tool Wear 
Cutting tool wear can be classified into several types 
as follows (Dimla, 2000): 
i. Adhesive wear associated with shear plane 
deformation, 
ii. Abrasive wear resulting from hard particles 
cutting action, 
iii. Diffusion 
wear 
occurring 
at 
high 
temperatures, and 
iv. Fracture wear such as chipping due to 
fatigue. 
 
 
Figure 1:  Cutting tool wear forms in orthogonal metal cutting 
(Dimla, 2000) 
Tool wear processes occur in combination with the 
predominant wear mode, dependent upon the cutting 
conditions, workpiece and tooling material, and the 
tool inserts geometry.  For a given cutting tool and 
workpiece material combination, the tool wear form 
may depend exclusively on the cutting conditions, 
principally cutting speed V and the undeformed chip 
thickness t, and a combination of the wear 
mechanisms above.  Ranges of cutting speed where 
each type of wear is predominant can be identified 
by considering the product of these values as Vt 
which is proportional to the cutting speed (Shaw, 
1984).  Sometimes, the tool life can be considerably 
reduced if the area of cut, the area swept by the 
cutting tool, is significantly increased (i.e. by 
increasing the depth of cutting mainly).  At low 
cutting speeds, the tool wears predominantly by a 
rounding-off of the cutting point and subsequently 
loses sharpness.  As the cutting speed increases the 
wear-land pattern changes to accommodate the 
ensuing change with extremely high values leading 
to plastic flow at the tool point.  The various forms 
of wear-land pattern and prevailing cutting speed in 
Figure 1.  The more predominantly occurring forms 
of cutting tool wear often identified as the principal 
types of tool wear in metal turning using single-point 
tools are the nose, flank, notch and crater wear.  
Figure 2 shows how wear features are measured. 
Nose Wear or edge rounding occurs predominantly 
through the abrasion wear mechanism on the cutting 
tool’s major edges resulting in an increase in 
negative rake angle.  Nose wear can be dependent 
entirely on the implemented cutting conditions with 
tool sharpness lost through plastic or elastic 
deformation.  At high cutting speeds, the edge 
deforms plastically and may result in the loss of the 
entire nose, Figure 1(a) and Figure 2(b).  Edge 
(a) Nose wear (low cutting speed)
(b) Flank and notch wear  
      (medium cutting speed)
(c) Cratering (high cutting speed) 
(d) Plastic/breakage      
 (very high cutting speed)


## Page 4


4 
chipping and cracking occur during periodic breaks 
of the ‘built up edge’ in interrupted cuts with the 
brittle tool and thermal fatigue.  Catastrophic failure 
may also occur if the nose is considerably worn or 
as a result of the utilization of inappropriate 
machining conditions and brittle tools such as 
ceramics and cemented carbide (Schey, 1987). 
Flank wear arises due to both adhesive and abrasive 
wear mechanisms from the intense rubbing action of 
the two surfaces in contact, i.e. the clearance face of 
the cutting tool and the newly formed surface of the 
workpiece.  Its rate of increase at the beginning of 
the tool life is rapid, settling down to a steady-state 
then accelerating rapidly again at the end of tool life 
(Figure 3). Note that this figure just presents a rough 
estimated of the tool wear time cycle during the 
machining process. The tool wear does not occur in 
a specific interval time.  Flank wear leads to a 
deterioration of surface quality, increased contact 
area and consequently to increased heat generation 
(Figure 1(b) and Figure 2(c)). Wear notch forms at a 
depth of cut line as the tool rubs against the shoulder 
of the workpiece (Figures 1(b) and 2(c).  Wear notch 
can lead to abrasion setting by the surface layers 
accelerated by oxidation or chemical reactions, 
possibly leading to total tool failure. 
 
Figure 2:  Conventional features of tool wear measurements 
(Dimla, 2000) 
Crater wear results from a combination of high 
cutting temperatures and high shear stresses creating 
a crater on the rake face some distance away from 
the tool edges, quantified by the depth and cross-
sectional area (Fig. 1(c)).  Crater wear also arises due 
to a combination of wear mechanisms: adhesion, 
abrasion, diffusion or thermal softening, and plastic 
deformation.  Severe depths of Crater may trigger a 
catastrophic collapse of the cutting point (Fig. 1(d)). 
B. Tool Condition Monitoring 
Techniques for on-line TCM system can be grouped 
into two main categories: direct sensing and indirect 
sensing techniques.  While direct methods of wear 
measurement have been attempted, the majority of 
methods have been indirect (Dimla 2000; Rangwala 
and Dornfeld, 1990;). 
Direct methods are of less benefit because the 
cutting area is largely inaccessible, and therefore 
monitoring cannot be performed while the tool is 
actively engaged in in-process cutting.  These 
methods include amongst others, touch trigger 
probes, optical, radioactive, proximity sensors and 
electrical resistance measurement techniques. 
 
Figure 3:  Generalized tool flank and nose wear progression 
(Dimla, 1998) 
Indirect methods take measurements while the tool 
is actively engaged since it involves recording a 
variable that can be correlated to tool wear (i.e. 
indirect methods measure factors that result as a 
consequence of tool wear).  Commonly used 
methods include amongst others cutting forces, 
acoustic emission, temperature, vibration, spindle 
motor current, cutting conditions, torque, and strain.  
These factors reflect far more than tool wear alone 
and parameters associated with tool wear must, 
therefore, be extracted from them and correlated to 
give a measure or extent of tool wear.  The main 
practical drawback with this popular method is the 
need for calibration of the associated parameters in 
monitoring the cutting process.  The cutting 
conditions (speed, feed-rate, and depth of cut) are 
known to affect the sensor signals and a range of 
methods have been suggested for separating the 
effects of these conditions from those of wear on the 
measured parameter (Karmathi, 1994). 
Methods for correlating the measured process 
parameters to tool wear, breakage or chipping fall 
primarily into three categories.  The first class 
consists of methods that can be viewed as heuristic 
based rules with a priori knowledge only of the 
process parameters, and use as mathematical 
modeling and adaptive observers.  The second 
category consists of methods that could be viewed 
as requiring formal knowledge of the process, and 
these can be grouped together as analytically based 
models such as time series analyses and Fast Fourier 
Transform peak tracking.  The last category is one 
of example based models with inductive learning 
capabilities such as pattern recognition, decision 
surfaces, mapping techniques, clustering, and ANN. 
Methods for Detecting Tool Wear 
Most indirectly measured sensor signals are affected 
by workpiece material variation, the geometry of the 
cutting tool and the cutting conditions (Lister, 1993).  
An on-line monitoring system designed to take the 
VB
Ktd
Flank face
Crater
wear
Nose wea
Flank wear
Wear notch
V max
B
V mean
B
time
tool wear
Secondary wear area
(linear)
Tertiary Wear
(Rapid breakdown leading
to catastrophic failure)
Primary wear
(initial breakdown)


## Page 5


5 
above factors into consideration is extremely 
demanding.  In many cases, the machining system 
does not need to have a global knowledge of the 
machining process, as it only requires knowledge of 
the machining operation in the neighborhood of the 
optimum for the operating process (Byrne et al., 
1995).  The cutting conditions cannot be neglected, 
as their variable parameters affect the sensor signals 
and therefore the cutting tool state. 
The use of these indirect methods requires accurate 
predictive models that link the un-measurable 
parameter of interest (tool wear), with the indirectly 
detectable variables (Oraby and Hayhurst, 1991).  
The process of tapping useful signals or process 
parameters directly or indirectly from a cutting 
process constitutes what Burke (1989) symbolically 
terms, the detection level.  This level in any TCMS 
is primarily concerned with choosing the relevant 
sensory signal. 
Identification of Tool Wear 
The choice of a suitable sensor type and its point of 
application (sensor location) are inextricably linked, 
with a suitable location for any such sensor being 
where the specified signal has the highest 
concentration and best reproducibility.  Certain 
limitations, however, do exist due to the structure of 
the machine.  A school of thought (Dimla, 1998) has 
it that information from a variety of different sensors 
has to be collected and these signals of varying 
reliability integrated (fused).  The primary benefit of 
sensor fusion would seem the fact that it serves to 
enhance the richness of the underlying information 
(wear level) contained in each signal thereby 
increasing the reliability of the monitoring process 
(Dornfeld, 1990).  The lack of an accurate model for 
wear prediction has thus led researchers resorting to 
other methods of sensor integration which do not 
rely on any theoretical or empirical process. 
The fusion and subsequent correlation of sensor 
signal features to tool wear is viewed as constituting 
the identification of wear, thus the characteristic 
identification level (Burke, 1989).  The utilization of 
single sensor signals offers incomplete sensory 
information as to the wear state (condition) of an 
engaged cutting tool.  This shortfall can be obviated 
by pursuance of a sensor fusion strategy (Lui and 
Ko, 1990).  This method has proven highly 
successful as more reliable information on the tool 
state was extractable.  In addition to pattern 
recognition 
techniques, 
hyperplane 
decision 
surfaces mapping techniques, neural networks, 
clustering techniques and perceptron techniques are 
reported by Noori-Khajavi and Komanduri (1995) in 
their literature survey as other fusion techniques.  
Methods primarily based on neural networks have 
proven particularly popular because tool wear 
intrinsically 
is 
a 
non-linear 
process. 
 
Its 
representation via a neural network is viable, reliable 
and an attractive alternative to previously employed 
empirical methods (Elanayar et al., 1990). The 
proposal of EISs - a successor of standard neural 
network for online and dynamic environments - has 
attracted growing research interest in the TCM field. 
Li et al, (2010) come up with the fuzzy regression 
technique for tool performance prediction and 
degradation detection. Wang et al, (2010) applied 
the so-called FAOS-PFNN for tool wear prediction 
of ball nose end-milling cutter. Nonetheless, they 
work in the offline mode which imposes a 
prohibitive computational cost for the strictly online 
environment. A fully online approach for predictive 
analytics of tool wear was proposed in (Oentaryo et 
al, 2011). The so-called DFNN was deployed for 
machine health condition prediction by Pan et al, 
(2014). To date, existing TCM systems rely on 
conventional EIS variants. Such systems are 
cognitive nature since two important facets, namely 
what-to-learn and when-to-learn, are uncharted.  
3. Evolving Intelligent Systems – Theory and 
Algorithm 
A. Cognitive Component of rClass 
Recurrent Classifier (rClass) is driven by a 
generalized Takagi-Sugeno-Kang (TSK) fuzzy 
system where the premise part is built upon a 
multivariable Gaussian function (Pratama et al., 
2014(a)), while the rule consequent is constructed 
with the Chebyshev polynomial up to the second 
order (Patra et al., 2002). This fuzzy rule is 
structured under a local recurrent network structure 
generating the spatiotemporal trait. 
The advantage of the Chebyshev polynomial over 
the standard zero- or first-order TSK rule 
consequent lies in a better approximation of a local 
output behavior of a nonlinear functions (Patra et al., 
2002) because it features a higher Degree of 
Freedom. It is also more convenient to compute than 
the trigonometric function (Pao, 1989) because it 
involves less number of parameters as follows: 
𝑇𝑛+1(𝑥𝑗) = 2𝑥𝑗𝑇𝑛(𝑥𝑗) −𝑇𝑛−1(𝑥𝑗)  
(1) 
If the second order is the order of interest and we 
deal with a 2-D input space [𝑥1, 𝑥2]. The extended 
input vector 𝑥𝑒is formed as follows: 
𝑥𝑒= [1, 𝑇1(𝑥1), 𝑇2(𝑥1), 𝑇1(𝑥2), 𝑇2(𝑥2)] 
(2) 
where 𝑥𝑒∈ℜ1×(2𝑢+1)and u is the number of input 
dimension. It is worth noting that the zero or first-
order TSK rule consequent suffers from a high bias 
problem which does not suffice in modelling a 
highly nonlinear characteristic.  
 The rule premise of the generalized TSK fuzzy rule 
relies on the multivariate Gaussian function with a 
non-diagonal covariance matrix (Pratama et al., 
2014(a)). This function generates a non-axis parallel 
ellipsoidal cluster which rotates to any direction. 
This trait lowers fuzzy rule demand which 
compensates a possible increase of network 
parameters as a result of the non-diagonal 
covariance matrix. The multivariate Gaussian 
function is expressed as follows: 
𝑅𝑖= exp⁡(−(𝜆𝑋𝑛−𝐶𝑖)Σ𝑖
−1(𝜆𝑋𝑛−𝐶𝑖)𝑇) 
(3)


## Page 6


6 
where 𝑋𝑛∈ℛ1×𝑢and  𝜆∈ℛ1×𝑢 are respectively an 
input vector of interest and an input weight vector. 
The input weight vector is obtained from the online 
input weighting strategy based on the L1 LDA 
method which is meant to induce the soft-
dimensionality reduction approach. 𝐶𝑖∈ℛ1×𝑢  is a 
Centroid of the i-th rule and Σ𝑖
−1 ∈ℛ𝑢×𝑢is an 
inverse non-diagonal covariance matrix whose 
elements govern orientation of a non-axis parallel 
ellipsoidal cluster. Equation (3) produces a spatial 
firing strength of a fuzzy rule which also defines a 
compatibility degree of a data point but excludes the 
temporal characteristic of the problem. This 
downside is overcome by putting forward a local 
recurrent network structure generating a spatio-
temporal firing strength as follows: 
𝜑𝑖,𝑜= 𝛾𝑖,𝑜𝑅𝑖+ (1 −𝛾𝑖,𝑜)𝜑𝑖,𝑜(𝑛−1) 
(4) 
where 𝛾𝑖,𝑜is a local recurrent weight of the i-th rule 
and o-th class and also controls a tradeoff between 
previous and current information. The rClass’s 
output is defined as a weighted average of the spatio-
temporal firing strength and the rule consequent: 
𝑦𝑜=
∑
𝜑𝑖,𝑜Ψ𝑖,𝑜
𝑀
𝑖=1
∑
𝜑𝑖,𝑜
𝑀
𝑖=1
=
∑
𝜑𝑖,𝑜𝑥𝑒𝑊𝑖,𝑜
𝑀
𝑖=1
∑
𝜑𝑖,𝑜
𝑀
𝑖=1
 
 
(5) 
where M is the number of fuzzy rules and 𝑊𝑖,𝑜∈
ℜ(2𝑢+1)×1is the output weight vector of the i-th rule 
and o-th class.  The normalization in equation (5) is 
to assure the partition of unity. The classification 
decision is inferred using the so-called MIMO 
architecture as follows: 
𝑂= max
𝑜=1,…,𝐶(𝑦𝑜)  
 
 
(6) 
where C is the number of classes. The MIMO 
architecture is deemed reliable in predicting a class 
label in an overlapping region because each rule 
features different rule consequents per class.    
B. Metacognitive Component of rClass 
This section outlines the metacognitive part of 
rClass which consists of three components: what-to-
learn, how-to-learn and when-to-learn.  
B.1 What-To-Learn 
Unlike the sample deletion strategy (Suresh et al., 
2010), the online active learning strategy is 
incorporated in rClass and contributes to significant 
relieve of the operator’s annotation efforts because 
sample contribution is estimated with the absence of 
labeled samples. It brings rClass’s working 
principles to go one step ahead to the semi-
supervised principle (Xiong et al., 2014).   
rClass makes use of the so-called Bayesian conflict 
method to run the what-to-learn strategy. This 
method offers more advanced traits than some of its 
counterparts in (Lughofer et al., 2013; Pratama et al., 
2014(c)) because it features a dynamic conflict level 
which adapts to speed and severity of concept drifts 
(Zlibaite, 2014). It takes into account the 
overlapping class problem because it utilizes the 
class-prior probability in measuring the conflict 
level. The conflict is formalised in both input and 
output spaces to cope with the so-called virtual and 
real concept drifts. The conflict in the output space 
is measured by the Bayesian posterior probability: 
𝑝(𝑦𝑜,𝑜𝑢𝑡𝑝𝑢𝑡|𝑋) = min⁡(max(𝑐𝑜𝑛𝑓, 0) , 1) 
(7) 
𝑐𝑜𝑛𝑓=
𝑦1
𝑦1+𝑦2 
 
 
 
(8) 
where 𝑦1, 𝑦2are the most and second most dominant 
output classes of rClass. It is observed from (7), (9) 
that the conflict in the output space is set as a spatial 
proximity between a target sample to a decision 
boundary. A sample sitting adjacent the decision 
boundary incurs a high conflict which pinpoints the 
need for a reshape of decision boundary. The 
conflict in the input space is measured using the 
Bayesian posterior probability as follows: 
𝑃(𝑦𝑜,𝑖𝑛𝑝𝑢𝑡|𝑋) =
∑
𝑃(𝑦𝑜|𝑅𝑖)𝑃(𝑋|𝑅𝑖)𝑃(𝑅𝑖)
𝑀
𝑖=1
∑
∑
𝑃(𝑦𝑜|𝑅𝑖)𝑃(𝑋|𝑅𝑖)𝑃(𝑅𝑖)
𝑀
𝑖=1
𝐶𝑜=1
 (9)   
where 𝑃(𝑦𝑜|𝑅𝑖), 𝑃(𝑋|𝑅𝑖), 𝑃(𝑅𝑖)are the class prior 
probability, the likelihood function and the prior 
probability. The advantage of (9) over a standard 
compatibility measure as shown in (Lughofer, 2013) 
is seen in its class prior probability which enables 
unclean clusters to be handled properly. That is, the 
unclean cluster portrays a situation where a cluster 
is occupied by different-classes samples. Unclean 
samples are inherent to misclassifications because 
one cluster cannot be assigned with a unique class. 
The class posterior probability, the prior probability 
and the likelihood function (Vigdor et al, 2007) are 
written as follows: 
𝑃(𝑦𝑜|𝑅𝑖) =
log⁡(𝑁𝑖,𝑜+1)
∑
log⁡(𝑁
𝐶
𝑜=1
𝑖,𝑜+1)  
 
(10) 
𝑃(𝑅𝑖) =
log⁡(𝑁𝑖+1)
∑
log⁡(𝑁𝑖+1)
𝑀
𝑖=1
 
 
 
(11) 
𝑃(𝑋|𝑅𝑖) =
1
(2𝜋𝑉𝑖)1/2 exp⁡(−(𝑋−𝐶𝑖)Σ𝑖
−1(𝑋−𝐶𝑖)𝑇) 
(12) 
The log operator is added to the class prior 
probability and the prior probability to soften its 
effect to a new rule. A sample is admitted for the 
training process provided its conflicts in both input 
and output spaces exceed a conflict threshold 𝜃:    
𝑃(𝑦𝑜,𝑖𝑛𝑝𝑢𝑡|𝑋)𝑎𝑛𝑑𝑃(𝑦𝑜,𝑜𝑢𝑡𝑝𝑢𝑡|𝑋) < 𝜃 
(13) 
To avoid having expensive labeling cost, a budget B 
is set and determines the maximum number of 
annotations during the training process. The training 
process is terminated, and a model is fixed if the 
actual labeling effort calculated as 𝑏= 𝑍𝑁
⁄ goes 
beyond this level where Z is the number of 
annotations made so far and N is the number of 
queried samples. This strategy plays important roles 
in real-world data stream cases because the labelling 
effort can be intractable due to infinite nature of data 
streams. The actual budget b can be insensitive when 
the number of samples is large. A slight 
modification is made for the actual labelling cost as 
follows: 
 𝑍(𝑛+ 1) = 𝑍(𝑛)𝑜+ 𝑙𝑎𝑏𝑒𝑙𝑙𝑖𝑛𝑔⁡  
 
𝑜=
(𝜉−1)
𝜉,⁡𝑏=
𝑍
𝜉  
 
 
(14) 
where 𝜉  is the window size, fixed at 100 in all our 
simulations in this paper and labelling signifies


## Page 7


7 
whether a sample of interest is labelled or not. In 
addition to (13), another criterion to accept a data 
sample is added where a sample is labelled only 
when a budget is not fully spent as follows: 
𝑏≤𝐵 
 
 
 
 
(15) 
Because of non-stationary learning environments, 
the conflict threshold should not be kept constant. 
Otherwise, it results in running out the budget too 
quickly since concept drifts impose a high labeling 
demand due to uncertainties in data distributions. 
Assuming that ℎ= 𝑃(𝑦𝑜|𝑋)is a random variable 
with the minimum 1 𝐶
⁄ and the maximum 1, we can 
derive a good estimate of the conflict threshold 
under the constraint  𝑏≤𝐵  as follows: 
𝑃(ℎ≤𝜃) = 𝑃(ℎ∈[1
𝐶, 1]) = ∫𝑝(ℎ)𝑑ℎ≤𝐵
1
1 𝐶
⁄
 
The final formula is reliant on the assumption of data 
distributions. Given that the uniform distribution is 
applied, we arrive at the following expression.  
𝜃=
1
𝐶+ 𝐵(1 −
1
𝐶) 
 
 
(16) 
This formula is further adjusted to adapt to concept 
changes in data streams. The adaptive strategy is 
also required to compensate the labeling cost in the 
presence of concept drifts and is formalized as 𝜃=
𝜃(1 ± 𝑠) where s is assigned its default value s=0.05 
(Zliobaite et al, 2..014). The conflict threshold 
increases 𝜃(1 + 𝑠)when a sample is discarded – (13) 
and (16) are not satisfied, whereas it diminishes 
𝜃(1 −𝑠)when a data point is accepted for the 
training process – (13) and (16) are satisfied.  
The so-called class imbalance problem has to be 
addressed in the online active learning scenario 
because under this circumstance a classifier has poor 
generalization performance for an under-represented 
class although it delivers a decent overall 
classification rate. The active learning scenario of 
rClass is generalized here to take into account the 
class imbalance problem. A minority-class sample is 
given a priority to be accepted for model updates and 
this is done by inspecting the estimated class-
posterior probability in the input and output space: 
max
𝑜=1,..,𝐶𝑃(𝑦𝑜,𝑖𝑛|𝑋) = max
𝑜=1,…,𝐶𝑃(𝑦𝑜,𝑜𝑢𝑡|𝑋) = 𝑜̂ (17) 
where 𝑜̂ is a minority class. This situation implies a 
queried sample most likely lies in a minority target 
class. Such samples should not be ignored to prevent 
the decision boundary to be skewed toward a 
majority class. This scenario is activated given that 
the class imbalance is detected. That is, the 
imbalance factor is defined as follows: 
𝐼𝐹= 1 −
𝐶
𝑁min
𝑜=1,..,𝐶𝑁𝑜 
 
 
(18)  
where the higher the value reveals the more severe 
the class imbalance exists (Subramanian et al, 
2014(a)). The imbalance factor is set at 𝐼𝐹≥0.3 to 
turn on (17) which shows about 15% of total 
samples belong to a minority class. The minority 
class is set as that of 𝑜̂ < 0.3𝑁.    
B. 2 How-to-Learn 
This section focuses on the how-to-learn part which 
updates the cognitive component and is derived 
from the Scaffolding theory (Wood et al., 2001). 
• 
Rule Growing Strategy: rClass is equipped 
by two rule growing scenarios, namely Datum 
Significance (DS) and Data Quality (DQ) methods 
(Pratama et al., 2015(b)) which coexist to estimate 
the significance of training samples. The DS method 
estimates the statistical contribution of training 
samples which reflects their possible contribution to 
the overall training process. The DS method is 
devised under the uniform data distribution 
assumption, which ignores the zone of influence of 
training samples in the feature space. The DQ 
method is incorporated to overcome this drawback 
because it essentially forms a recursive density 
estimation of a data point. It examines whether or 
not a data sample is located at a strategic location in 
the input space. The DS method is expressed: 
   𝑉𝑀+1 ≥max
𝑖=1,…,𝑀(𝑉𝑖) 
 
 
(19) 
where 𝑉𝑀+1is the volume of hypothetical rule and 
𝑉𝑖is the volume of i-th rule. This expression is 
obtained 
from 
∫
𝑅𝑖𝑝(𝑥)𝑑𝑥
𝑋
where 
𝑝(𝑥)is 
a 
probability density function assuming that data 
follow the uniform distribution. Although it 
encompasses overall contribution of a rule, its 
uniform data distribution assumption obscures a 
sample’s location.  
The DQ method is put forward as another rule 
growing mechanism to measure fuzzy rule relevance 
through its density. The difference is, however, 
observed in the facts that the DQ method involves a 
weighting factor 𝑈𝑁to address an outlier bottleneck, 
uses the inverse multi-quadratic function and is 
well-suited to the multivariable Gaussian function. 
It adopts similar concept of the recursive density 
estimation (Angelov et al, .2004) where a rule 
density is defined as an accumulated distance of a 
cluster’s prototype to all other samples seen so far: 
𝐷𝑄𝑁= √
𝑈𝑁
𝑈𝑁(1+𝑎𝑁)−2𝑏𝑁+𝑐𝑁 
 
 
𝑈𝑁= 𝑈𝑁−1 + 𝐷𝑄𝑁−1,𝑎𝑁= 𝑋𝑁Σ𝑁
−1𝑋𝑁,𝑏𝑁=
𝐷𝑄𝑁−1𝑋𝑁𝛼𝑁, 𝛼𝑁= 𝛼𝑁−1 + Σ𝑁
−1𝑋𝑁−1
𝑇
,𝑐𝑁= 𝑐𝑁−1 +
𝐷𝑄𝑁−1𝑋𝑁−1Σ𝑁
−1𝑋𝑁−1
𝑇
 
where Σ𝑁
−1is an inverse covariance matrix of the 
hypothetical rule created by a current data point 
(22)-(24). The DQ rule growing condition is written: 
𝐷𝑄𝑁≥max
𝑖=1,…,𝑀(𝐷𝑄𝑖)or𝐷𝑄𝑁≤min
𝑖=1,…,𝑀(𝐷𝑄𝑖) (20)  
Note that 𝑋𝑁in (19) is replaced by the focal point of 
i-th cluster 𝐶𝑖 for 𝐷𝑄𝑖. The first condition in (20) 
reveals a case where a new data point brings the 
most relevant concept to the training process 
because it occupies the most populated input region. 
The second condition in (20) signifies a possible 
concept change because a data point is situated at a 
remote region which is outside influence zones of a 
current rule base. Such samples are vital to introduce 
new concepts in the current rule base. A new rule is


## Page 8


8 
added to the current rule base if both (19) and (20) 
are satisfied. The growing strategy is consistent with 
the problematizing part of the Scaffolding theory. 
• 
Parameterization of a New rule: once a 
new rule is added, its parameters have to be 
initialized. This step warrants in-depth investigation 
because of the class overlapping case which leads to 
performance deterioration (Subramanian et al., 
2014(a)). That is, a local region is populated by 
different-classes samples, or a class is not clearly 
separated. There exist two types of overlapping: 
inter-class 
and 
intra-class. 
The 
inter-class 
overlapping leads to classifier’s confusion and 
imposes a dramatic increase of nonlinearity of 
decision boundary.  
rClass is endued with the class overlapping strategy 
to ensure a decent input partition of a new rule. At 
first, the compatibility degree of a new rule with 
respect to other rules is checked where it can be 
examined through a firing strength of the winning 
rule𝑅𝑤𝑖𝑛. The winning rule is here determined by the 
one with the closest distance to a new rule. Given 
that it beats a distance threshold 𝑅𝑤𝑖𝑛≥𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑 
where threshold is chosen as a critical value of 
𝜒2distribution with u degree of freedom and 
significance level 𝛼, the potential per-class concept 
is executed - 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑= exp⁡(−𝜒2(𝛼)). The 
potential per-class concept aims to investigate the 
relationship of a new rule to target classes whether it 
is more adjacent to the same class than other classes 
or not. The potential per-class method is 
mathematically written as follows: 
𝜍𝑜= √
(𝑁𝑜−1)
(𝑁𝑜−1)(𝑎𝑏𝑛+1)+𝑐𝑏𝑛𝑜−2𝑏𝑏𝑛𝑜 
 
(21)  
𝑎𝑏𝑛= ∑
𝑥𝑗,𝑁
2
𝑢+𝑚
𝑗=1
, 
𝑐𝑏𝑛𝑜= 𝑐𝑏𝑛𝑜−1 + ∑
𝑥𝑗,𝑁𝑜
2
𝑢+𝑚
𝑗=1
, 
𝑏𝑏𝑛𝑜= ∑
𝑥𝑗,𝑁𝑑𝑑𝑗,𝑛𝑜
𝑚+𝑢
𝑗=1
, 𝑑𝑛𝑜= 𝑑𝑛𝑜−1 + 𝑥𝑁𝑜.   
where 𝑥𝑁𝑜is the latest sample of the o-th class and 
𝑥𝑁is the newest sample, while 𝑁𝑜is the number of 
samples of the o-th class. The class overlapping 
occurs when the closest class differs from the true 
class label max
𝑜=1,…,𝐶(𝜍𝑜) ≠𝑡𝑟𝑢𝑒_𝑐𝑙𝑎𝑠𝑠_𝑙𝑎𝑏𝑒𝑙. Based 
on these two criteria, three scenarios, namely class 
overlapping, 
cluster 
overlapping 
and 
non-
overlapping, are devised to tackle each possible 
combination. We start by defining two important 
variables: 𝑟𝑖𝑒, 𝑟𝑖𝑎which stand for a distance between 
a new rule to the closest inter-class rule and the 
closest intra-class rule respectively.  The three 
conditions are elaborated as follows: 
The class-overlapping condition: this condition 
occurs when max
𝑜=1,…,𝐶(𝜍𝑜) ≠𝑡𝑟𝑢𝑒_𝑐𝑙𝑎𝑠𝑠_𝑙𝑎𝑏𝑒𝑙is met. 
This implies that a new rule sits in the overlapping 
region of different-class samples. A new rule is 
initialised as follows: 
𝑐𝑗,𝑀+1 = 𝑥𝑗,𝑁−0.1(𝑐𝑗,𝑖𝑒−𝑥𝑗,𝑁), 𝑑𝑖𝑠𝑡= 𝑓𝑎𝑐(𝑐𝑗,𝑀+1 −𝑐𝑗,𝑖𝑒)(22) 
where fac is an overlapping factor determined as a 
distance ratio between the intra-class cluster and the 
inter-class cluster 𝑓𝑎𝑐=
𝑟𝑗,𝑖𝑎
𝑟𝑗,𝑖𝑒. This setting aims to 
shrink the coverage of a new rule proportionally to 
its overlapping degree. Furthermore, the centre of a 
new rule is shifted away from the inter-class cluster 
to alleviate the effect of class overlapping.  
The rule-overlapping condition: this condition 
portrays a case where a new rule is neighboring to 
the intra-class cluster. It is pinpointed by 
max
𝑜=1,…,𝐶(𝜍𝑜) = 𝑡𝑟𝑢𝑒_𝑐𝑙𝑎𝑠𝑠_𝑙𝑎𝑏𝑒𝑙. This incurs the 
risk of overlapping in the rule level which is less 
harmful than the class-overlapping condition. The 
following is undertaken to address this condition. 
𝑐𝑗,𝑀+1 = 𝑥𝑗,𝑁−0.1(𝑐𝑗,𝑖𝑎−𝑐𝑗,𝑖𝑒), 𝑑𝑖𝑠𝑡= 𝑓𝑎𝑐(𝑐𝑗,𝑀+1 −𝑐𝑗,𝑖𝑒)(23) 
This setting is required to move a new rule away 
from the intra-class cluster since two rules may 
move together and end up in the significantly 
overlapping position. The rule merging strategy is 
incorporated in the rClass and functions also to 
handle the rule overlapping case.  
The non-overlapping condition: this condition 
delineates a case when a new rule is sufficiently 
distant from other rules and is indicated by𝑅𝑤𝑖𝑛<
𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑. It is safe to construct a new rule: 
𝑐𝑗,𝑀+1 = 𝑥𝑗,𝑁, 𝑑𝑖𝑠𝑡= 𝑓𝑎𝑐(𝑥𝑗,𝑁−𝑐𝑗,𝑖𝑎) 
(24) 
A new rule is out of scope of existing rules. A new 
inverse covariance matrix for all conditions is 
initialized as Σ𝑀+1
−1
= (𝑑𝑖𝑠𝑡𝑇𝑑𝑖𝑠𝑡)−1. A new rule is 
initialized as a classical cluster in the main axes but 
rotates after receiving the premise adaptation (28).    
The output weight, recurrent weight, and output 
covariance matrix are crafted as follows: 
𝑊𝑀+1 = 𝑊𝑤𝑖𝑛, Ψ𝑀+1 = 𝜔𝐼, 𝛾𝑀+1 =
∑
𝛾𝑖
𝑀
𝑖=1
𝑀
 (25) 
where 𝜔= 105is a large positive constant and it 
assures a convergence toward a batch learning 
process which has been mathematically proven in 
(Lughofer, 2010). Moreover, a new weight vector is 
set as that of the winning rule since it portrays the 
most compatible concept to the new rule. The 
recurrent weight is assigned as an average of 
existing ones to be proportional to the current 
weights. The self-construction of fuzzy rules here 
depicts the problematizing facet of the Scaffolding 
theory because it is capable of addressing rapidly 
changing process environments by introducing a 
new rule when needed.  
There exist situations where the rule growing criteria 
in (19) and (20) are not met. Data streams in these 
conditions merely induce minor conflict to the 
current belief and do not suffice to trigger the rule 
adding a scenario. This condition is formalized: 
𝑉𝑀+1 ≥max
𝑖=1,…,𝑀(𝑉𝑖) 
min
𝑖=1,…,𝑀(𝐷𝑄𝑖) < 𝐷𝑄𝑁< max
𝑖=1,…𝑀( 𝐷𝑄)𝑖 
(26) 
This condition exhibits a data point having a 
substantial statistical contribution but is still within 
the coverage of existing rules. Only the antecedent 
of the winning rule is refined in this scenario to be 
well-suited to the currently seen concept. The online 
adaption of the rule premise is derived from the


## Page 9


9 
modified version of sequential maximum likelihood 
estimation for the multivariate Gaussian function: 
𝐶𝑤𝑖𝑛=
𝑁𝑤𝑖𝑛𝐶𝑤𝑖𝑛
𝑁𝑤𝑖𝑛+1 +
(𝑋−𝐶𝑤𝑖𝑛)
𝑁𝑤𝑖𝑛+1  
 
(27) 
Σ𝑤𝑖𝑛
−1 =
Σ𝑤𝑖𝑛
−1
1−𝛼+
𝛼
𝛼+1
Σ𝑤𝑖𝑛
−1 ((𝑋−𝐶𝑤𝑖𝑛)Σ𝑤𝑖𝑛
−1 (𝑋−𝐶𝑤𝑖𝑛)𝑇)
1+𝛼(𝑋−𝐶𝑤𝑖𝑛)Σ𝑤𝑖𝑛
−1 (𝑋−𝐶𝑤𝑖𝑛)𝑇(28) 
𝑁𝑤𝑖𝑛= 𝑁𝑤𝑖𝑛+ 1  
 
 
(29) 
where 𝛼=
1
𝑁𝑤𝑖𝑛+1. (28) features a direct update of 
the covariance matrix with the absence of 
reinversion step and is inspired by the Neuman 
series (Lughofer et al., 2015). This strategy is 
desirable since the reinversion step tends to be 
unstable in the case of an ill-defined matrix and is 
intractable when dealing with a high input 
dimension. The adaptation of rule antecedent 
complements the rule growing scenario to adapt to 
variations of data streams and functions as the 
problematizing component of the Scaffolding 
theory. Only the winning rule is subject to the tuning 
phase to prevent the overlapping situation and to the 
fact that it is the closest one to the current sample. 
The movement of the winning rule decreases as the 
increase of its supports since a cluster is encouraged 
to capture more supports initially but should be 
made less sensitive at the later stage to avoid sample 
redundancies. Note that the winning rule can be 
determined as the closest rule or that of the highest 
posterior probability (Pratama et al, 2015(a)).     
• 
Rule Pruning Strategy: rClass is equipped 
by two rule pruning scenarios, namely the Extended 
Rule Significance (ERS) method and the Potential+ 
(P+) method, which aim to simplify the rule base 
complexity as well as to prevent the overfitting. The 
ERS method shares the same principles as the DQ 
method, but it quantifies the statistical contribution 
of existing rules instead. It targets superfluous rules 
which play little during their lifespan. The P+ 
method is designed to detect obsolete rule which is 
no longer relevant to the current training concept. It 
also functions as a rule recall scenario, which 
overcomes the recurring drift. The DQ method is 
mathematically expressed as follows: 
𝐸𝑅𝑆𝑖= ∑
∑
𝑤𝑖,𝑜
𝑉𝑖
∑
𝑉𝑖
𝑀
𝑖=1
2𝑢+1
𝑗=1
𝐶
𝑜=1
 
 
(30)   
It is also seen from (30) that the ERS method also 
takes into account the contribution of the output 
weight. A fuzzy rule is pruned provided that 𝐸𝑅𝑆𝑖<
𝐸𝑅𝑆𝑖
̂ −𝐸𝑅𝑆𝑖,𝜎condition 
is 
satisfied 
where 
𝐸𝑅𝑆𝑖
̂, 𝐸𝑅𝑆𝑖,𝜎are mean and standard deviation of the 
ERS of the i-th rule. The ERS method realises the 
fading of the Scaffolding theory which aims to 
alleviate the rule base complexity. The P+ method is 
formulated as follows: 
ℵ𝑖,𝑛= √
(𝑁−1)ℵ𝑖,𝑛−1
2
(𝑁−1)ℵ𝑖,𝑛−1
2
+(𝑁−2)(1−ℵ𝑖,𝑛−1
2
)+ℵ𝑖,𝑛−1
2
𝑑𝑖,𝑛  (31) 
where 𝑑𝑖,𝑛is the Mahalabobis distance between a 
newly observed sample and the focal point of i-th 
rule. ℵ𝑖,0is initialized as zero. As with the ERS 
method, a fuzzy rule is pruned if this condition 
ℵ𝑖,𝑛< ℵ̂𝑖,𝑛−ℵ𝑖,𝑛
𝜎 is met. This condition aims to 
check decline of the P+ value of i-th rule during its 
lifespan and portrays a situation when a rule loses its 
relevance. The P+ method is in line with the 
problematizing of the Scaffolding theory because it 
deals with obsolete rules due to concept change.   
• 
Rule Recall Strategy: the recurring or 
cyclic drift pinpoints a condition where an old 
concept reappears again in the future. This issue 
causes a previously pruned rule to be valid again in 
the future (Pratama et al., 2015(a)) and such rules 
should be recalled to cope with current data 
distribution instead of creating a new rule from 
scratch because it may impose catastrophic 
forgetting of previously learned concept. The P+ 
method also functions to reactivate previously 
pruned rule because it can precisely monitor the 
relevance of fuzzy rules by inspecting the evolution 
of local density. An old rule should be recalled when 
its relevance beats any existing rule including that of 
the hypothetical rule as follows: 
max
𝑖∗=1,…,𝑃∗(ℵ𝑖∗,𝑛) >
max
𝑖=1,…,𝑃+1(𝐷𝑄𝑖,𝑛)  
(32) 
where P* is the number of rules discarded by the P+ 
method. It is observed from (23) that the P+ method 
can be compared directly with the DQ method 
because both of which estimates the local density. 
The P+ method is, however, updated when a new 
sample is learned. The rule recall mechanism is 
undertaken as follows: 
𝐶𝑃+1 = 𝐶𝑖∗, Σ𝑃+1
−1 = Σ𝑖∗
−1, 𝑊𝑃+1 = 𝑊𝑖∗, Ψ𝑃+1 = Ψ𝑖∗(33) 
Although previously pruned rules are retained in the 
memory, computational complexity and memory 
demand still diminish since old rules are excluded 
from other learning scenarios.  
• 
Cluster Splitting Mechanism: an over-sized 
cluster undermines the generalization capability of a 
model because it opens a chance for one cluster to 
cover two or more distinct data clouds. In the 
presence of local drift, it causes a cluster to blow-up 
(over-sized) 
because 
of 
gradual 
change 
of 
distribution in one local region. This situation calls 
for the rule splitting mechanism which divides a 
cluster to two disjoint cluster subject to the 
following condition. 
𝑉𝑤𝑖𝑛> 𝛿∑
𝑉𝑖
𝑀
𝑖=1
  
 
 
(34) 
where 𝛿∈[0.5,0.9]  is a tolerance threshold which 
steers the intensity of splitting process and is fixed 
at 0.8 in all our simulations. Furthermore, only the 
winning rule is to be checked in (34) because it is the 
only cluster receiving the adaptation. The splitting 
mechanism is defined as follows:  
𝐶𝑀+1 = 𝐶𝑤𝑖𝑛± (𝑔𝑚𝑎𝑥√𝛼𝑚𝑎𝑥+ 𝑞√𝛼𝑚𝑎𝑥) 
Σ𝑀+1
−1
= Σ𝑤𝑖𝑛
−1 −((𝑔𝑚𝑎𝑥√𝛼𝑚𝑎𝑥)𝑇(𝑔𝑚𝑎𝑥√𝛼𝑚𝑎𝑥))−1  
𝑊𝑀+1 = 𝑊𝑤𝑖𝑛, Ψ𝑀+1 = Ψ𝑤𝑖𝑛, 𝑁𝑀+1 = 𝑁𝑤𝑖𝑛
2  
where 𝛼𝑚𝑎𝑥, 𝑔𝑚𝑎𝑥are the largest eigenvalue and its 
corresponding eigenvector, while q is a predefined 
constant which controls a distance of two clusters of 
the splitting mechanism. Because the eigenvalue


## Page 10


10 
signifies the variance of Σ𝑤𝑖𝑛toward the direction of 
eigenvector, the maximum eigenvalue is selected to 
prevent the loss of orientation and population since 
it indicates the underlying direction of a cluster. The 
rule splitting mechanism is consistent with the 
problematizing of the Scaffolding theory.  
• 
Rule Forgetting Mechanism: the rule 
forgetting mechanism is an effective avenue in 
handling the gradual concept drift because it 
strengthens the evolution of a cluster to follow the 
concept drift. It is also applicable to cope with the 
local concept drift because unique forgetting levels 
for every local region are assigned in accordance 
with drift intensity and velocity. Forgetting levels 
for every local region are determined: 
𝜆𝑖= 1 −0.1(ℵ𝑖,𝑛−ℵ𝑖,𝑛−1) 
 
(35) 
𝜆𝑡𝑟𝑎𝑛𝑠,𝑖= −9.9𝜆𝑖+ 9.9 
 
 
(36) 
𝑁𝑖= 𝑁𝑖−𝑁𝑖min⁡(𝜆𝑡𝑟𝑎𝑛𝑠,𝑖, 0.99) 
 
(37) 
The forgetting level 𝜆𝑖∈[0.9,1]is measured from 
the rate of the P+ values (31) in two consecutive 
measurements where the lower the value indicates a 
stronger forgetting level. Since the P+ method is 
concerned with the local density, a change of local 
density discloses an indication of a local concept 
change. The local concept drift is handled in both 
input and output space where the forgetting level is 
inserted in the FWGRLS formulate to deal with the 
local concept change in the output space while a 
reduction of cluster population (28) is performed to 
overcome the concept drift in the input space.   
• 
Rule Merging Strategy: The rule merging 
scenario is realized using the Bhattacharyya distance 
and the blow-up check (Lughofer, 2015(a)). The 
advantage of the Bhattacharyya similarity measure 
lies in its aptitude to approximate the spread of the 
multivariate 
Gaussian 
distribution 
which 
is 
equivalent to the multivariable Gaussian function. It 
is furthermore threshold-free which is appealing in 
dealing with online data streams. The blow-up check 
copes with the so-called cluster delamination which 
delineates an over-sized cluster covering two or 
more distinguishable data clouds. Such cluster 
hinders the model’s generalization because the 
specificity of the cluster lowers. The Bhattacharyya 
similarity measure is expressed as follows: 
𝑆𝑤𝑖𝑛,𝑖= 1
8 (𝐶𝑤𝑖𝑛−𝐶𝑖)Σ𝑐𝑜𝑚𝑏
−1
(𝐶𝑤𝑖𝑛−𝐶𝑖)𝑇
+ 1
2 ln⁡(
det⁡(Σ𝑐𝑜𝑚𝑏
−1
)
det⁡(Σ𝑤𝑖𝑛
−1 )det⁡(Σ𝑖
−1)) 
where Σ𝑐𝑜𝑚𝑏
−1
=
Σ𝑤𝑖𝑛
−1 +Σ𝑖
−1
2
. 𝑆𝑤𝑖𝑛,𝑖= 0 indicates that 
two clusters are touching and two clusters are 
overlapping when it results in a positive value 
𝑆𝑤𝑖𝑛,𝑖> 0 while a negative value 𝑆𝑤𝑖𝑛,𝑖< 0 
signifies that two clusters are disjoint.  
The blow-up check is carried out by inspecting the 
volume of a merged cluster whether it beats a total 
volume of two independent clusters. This aims to 
assess whether two clusters are homogeneous 
because two non-homogenous clusters lead to an 
over-sized merged cluster which is prone to the 
cluster delamination condition. We arrive at the 
following condition in coalescing two clusters: 
𝑆𝑤𝑖𝑛,𝑖> 0, 𝑉𝑚𝑒𝑟𝑔𝑒𝑑≤𝑢(𝑉𝑤𝑖𝑛+ 𝑉𝑖)  
(29) 
u is inserted in (29) to deal with the curse of 
dimensionality. The rule merging mechanism is 
undertaken provided that (29) is satisfied. The 
merging process is performed using the weighted 
average strategy: 
𝐶𝑚𝑒𝑟𝑔𝑒𝑑=
𝐶𝑤𝑖𝑛𝑁𝑤𝑖𝑛+𝐶𝑖𝑁𝑖
𝐶𝑤𝑖𝑛+𝐶𝑖
  
 
(30) 
Σ𝑚𝑒𝑟𝑔𝑒𝑑
−1
=
Σ𝑤𝑖𝑛
−1 𝑁𝑤𝑖𝑛+Σ𝑖
−1𝑁𝑖
𝑁𝑤𝑖𝑛+𝑁𝑖
  
 
(31) 
𝑁𝑚𝑒𝑟𝑔𝑒𝑑= 𝑁𝑖+ 𝑁𝑤𝑖𝑛 
 
 
(32) 
The weighted average strategy allows a rule with a 
higher support to be more influential to the final 
shape of a merging result. The rule consequent is 
merged by taking into account the degree of 
contradiction between the rule antecedent and the 
rule consequent because a contradiction exists when 
the two rule consequents are dissimilar, but their 
antecedents are similar. The similarity of rule 
consequents is first measured where it is pinpointed 
by the angle created between two rule consequents 
in the output space. Note that we just consider the 
linear terms of the rule consequent while excluding 
their higher order terms as follows: 
𝑆𝑤𝑖𝑛,𝑖
𝑜𝑢𝑡= {
1 −
2
𝜋𝜙, 𝜙∈[0,
𝜋
2]
2
𝜋(𝜙−
𝜋
2) , 𝜙∈[
𝜋
2 , 𝜋]
 
 
(33) 
𝜙𝑜= arccos⁡(
𝑎𝑜𝑇𝑏𝑜
|𝑎𝑜||𝑏𝑜|) 
 
 
(34) 
𝜙= max
𝑜=1,…,𝐶(𝜙𝑜)  
 
 
(35) 
𝑎𝑜= [𝑤0,𝑤𝑖𝑛
𝑜
, 𝑤1,𝑤𝑖𝑛
𝑜
, 𝑤3,𝑤𝑖𝑛
𝑜
, … , 𝑤𝑢,𝑤𝑖𝑛
𝑜
]   
𝑏𝑜= [𝑤0,𝑖
𝑜, 𝑤1,𝑖
𝑜, 𝑤3,𝑖
𝑜, … , 𝑤𝑢,𝑖
𝑜]   
It is worth noting the higher order term of the 
Chebyshev polynomial merely fashions its nonlinear 
oscillation while its orientation is steered by its 
linear terms. This similarity measure is referred to 
when merging the rule consequent. The old rule 
consequent is retained when the similarity of the rule 
consequent is lower than the similarity of the rule 
consequent. The merging process is carried out 
using the Yager’s participatory learning inspired 
approach as follows: 
Ω𝑚𝑒𝑟𝑔𝑒𝑑= Ω1 + 𝛾𝛿(Ω1 −Ω2) 
 
(36) 
𝛾=
𝑁1
𝑁1+𝑁2 
 
 
 
(37) 
𝛿= {1, 𝑆𝑤𝑖𝑛,𝑖
𝑜𝑢𝑡≥𝑆𝑤𝑖𝑛,𝑖
0, 𝑆𝑤𝑖𝑛,𝑖> 𝑆𝑤𝑖𝑛,𝑖
𝑜𝑢𝑡 
 
 
(38) 
About the Yager’s participatory learning scheme, 
𝛾∈[0,1], 𝛿 can be regarded as the basic learning 
rate and the compatibility index between two models 
respectively, while the arousal index is set constant 
at 0. Ω1here denotes the rule consequent of the 
dominant rule having more supports than Ω2, 𝑁1 >
𝑁2. The rule merging process focusses on the 
winning rule because it has a higher risk of 
overlapping than others due to the rule antecedent


## Page 11


11 
learning (27) - (29). The rule merging strategy 
represents the complexity reduction of the 
Scaffolding theory.  
• 
Input Weighting Strategy: The online 
feature weighting scenario based on the L1-norm 
Fisher Discriminant Analysis (FDA) is integrated 
into rClass. This differs from an earlier version of 
the online feature weighting utilizing the L2-norm 
(Lughofer, 2011) leading to at least three problems: 
outliers, rank limit, and small sample size. The L1 
norm FDA was proposed in (Wang et al., 2014) and 
its cost function is written as follows: 
𝐽(𝜔) =
∑
𝑁𝑜|𝜔(𝑥̅𝑜−𝑥̅)𝑇|
𝐶
𝑜=1
∑
∑
|𝜔(𝑥𝑛,𝑜⁡−𝑥̅)𝑇|
𝑁𝑜
𝑛=1
𝐶𝑜=1
 
 
(39) 
where 𝜔∈ℜ1×𝑢is a transformation vector. The 
online version of the L1 norm FDA is derived by 
formulating recursive expressions of the mean of the 
o-th class data samples 𝑥̅𝑜, the mean of the data 
samples 𝑥̅ as follows: 
𝑥̅𝑜=
(𝑁𝑜−1)
𝑁𝑜
𝑥̅𝑜+
𝑥𝑁𝑜.𝑜
𝑁𝑜,⁡𝑥̅ =
(𝑁
−1)
𝑁
𝑥̅ +
𝑥𝑁
𝑁      (40) 
With 𝑥𝑁 the latest (the N-th) data sample loaded and 
𝑥𝑁𝑜.𝑜 the latest (the No-th) data sample from class o. 
The online version of within-class scatter matrix is 
formalized as follows: 
∑
∑
|𝜔(𝑥𝑜−𝑥̅)𝑇| = ∑
𝜔Σ𝑜
𝐶
𝑜=1
𝑁𝑜
𝑛=1
𝐶
𝑜=1
  
(41) 
Σ𝑜= Σ𝑜+ |𝑥𝑜−𝑥̅| 
 
 
(42) 
The projection vector 𝜔 is fine-tuned using the 
gradient ascent procedure maximizing the cost 
function (39) as follows: 
𝜔= 𝜔+ 𝜂
𝜕𝐽(𝜔)
𝜕𝜔  
 
 
(43) 
where 𝜂= 10^(−3) is a learning rate. The first 
order derivative of the cost function with respect to 
the projection vector is defined as follows: 
𝜕𝐽(𝜔)
𝜕𝜔=
∑
𝑠𝑜𝑁𝑜(𝑥̅𝑜−𝑥̅)
𝐶𝑜=1
∑
𝑁𝑜
𝐶𝑜=1
|𝜔(𝑥̅𝑜−𝑥̅)| −
∑
𝑟𝑜Σ𝑜
𝐶𝑜=1
∑
𝜔Σ𝑜
𝐶𝑜=1
  
(44) 
The denominator sometimes goes to zero quickly. 
This is addressed by replacing it with 𝜔=
𝜔+ Δ𝜔‖𝜔+ Δ𝜔‖
⁄
 where Δ𝜔is a small nonzero 
random vector if the denominator becomes too 
small. 𝑠𝑜, 𝑟𝑜are two sign functions:  
𝑠𝑜= 𝑠𝑔𝑛(𝜔(𝑥̅𝑜−𝑥̅)),𝑟𝑜= 𝑠𝑔𝑛(𝜔(𝑥𝑜−𝑥̅𝑜))(45) 
The input weight is produced by the Leave-One-
Feature-Out (LOFO) scheme which studies the 
contribution of an input feature by masking it for the 
training process. An important input attribute should 
have a high discriminatory power. Therefore, when 
it is ruled out, the cost function (39) should 
significantly reduce. The input weight is then 
quantified as follows:  
𝜆𝑗= 1 −
𝐽𝑗−min
𝑗=1,…,𝑢(𝐽𝑗)
max
𝑗=1,…,𝑢(𝐽𝑗)−min
𝑗=1,…,𝑢(𝐽𝑗) 
 
(46) 
where 𝐽𝑗is the value of the cost function (39) when 
an input attribute j is ignored from the training 
process. The input weight 𝜆𝑗is involved in all parts 
of learning process: inference scheme, etc. The 
online weighting mechanism is in line with the 
complexity reduction of the Scaffolding.   
• 
Parameter Learning Strategy: rClass 
utilizes the so-called Fuzzily Weighted Generalized 
Least Square (FWGRLS) method to fine-tune the 
rule consequent. The FWGRLS forms a local 
learning version of the GRLS method (Xu et al., 
2006) which puts forward a weight decay term in the 
cost function of the RLS method. The weight decay 
term navigates the weight vector such that it hovers 
around in a small and bounded interval. Such 
property is vital for the generalization’s capability of 
a model and compactness of a rule base since a 
superfluous rule usually tends to have a very small 
rule consequent. This issue eases the task of the ERS 
method (22) in capturing inconsequential rules. The 
FWGRLS method is formulated: 
𝐾(𝑁) = Ψ𝑖(𝑁−1)𝐹(𝑛)(𝜆𝑖Δ(𝑁)
Λ𝑖(𝑁) + 𝐹(𝑁)Ψ𝑖(𝑛−1)𝐹(𝑁)𝑇) 
Ψ𝑖(𝑁) = Ψ𝑖(𝑁−1) −𝐾(𝑁)𝐹(𝑛)Ψ𝑖(𝑁−1) 
𝑊𝑖(𝑁) = 𝑊𝑖(𝑁−1) −𝜔Ψ𝑖(𝑁)∇ξ(𝑊𝑖(𝑁−1)) + Ψ𝑖(𝑁)(𝑡(𝑁) −𝑦(𝑁)) 
𝑦(𝑁) = 𝑥𝑒𝑊𝑖, 𝐹(𝑁) =
𝜕𝑦(𝑁)
𝜕Ψ𝑖(𝑁) = 𝑥𝑒𝑛 
 
where Δ(𝑁)is a Hessian matrix whose diagonal 
elements consist of the spatial firing strength 𝑅𝑖 and 
Λ𝑖(𝑁) is a covariance matrix of the modelling error 
simply set as the Hessian matrix. 𝜆𝑖is the forgetting 
factor determined through the rate of change of the 
P+ values in two consecutive instants (31). Note that 
the forgetting factor aims to intensify the movement 
of the rule consequent in the presence of concept 
drift. 𝐾(𝑁) is the Kalman gain and Ψ𝑖is the output 
covariance matrix which is unique per rule because 
of the local learning principle. The adaptation 
process is carried out separately per rule as the local 
learning principle. This strategy provides flexibility 
because the training process of a rule does not affect 
the stability and convergence of other rules.  
∇𝜉(𝑊𝑖(𝑁−1)) is the gradient of the weight decay 
function where the quadratic weight decay function 
is selected because it is capable of shrinking the 
weight vector proportionally from its current values. 
𝜔 is a predefined constant which governs the 
dominance of the weight decay term and set as its 
default value 10−3.  
The recurrent weight of rClass is adjusted using the 
Zero Error Density Maximization (ZEDM) method 
(Subramanian et al., 2013), which modifies the 
classical gradient descent method. The ZEDM 
method replaces the cost function of the gradient 
descent method with the error entropy concept to 
attain a reliable approximation of high order 
statistical behavior. The goal of the ZEDM method 
is to minimize the distance between the probability 
distribution of the target class and the classifier’s 
output. This strategy is equivalent to forcing the 
system’s error toward zero. Because the exact 
expression of the error entropy is difficult to be 
modeled, the Parzen Window estimation is put 
forward as follows: 
𝑓(0) =
1
𝑁ℎ√2𝜋∑
exp⁡(−
𝑒𝑛,ℎ
2
2ℎ2)
𝑁
𝑛=1
 
 
(47)


## Page 12


12 
where N denotes the number of training samples 
seen thus far, and h stands for a smoothing parameter 
set as one while 𝑒𝑛,𝑜 is the system error at the n-th 
observation and o-th class label. The optimization 
procedure is carried out using the gradient descent 
method as follows: 
𝛾𝑖,𝑜(𝑁) = 𝛾𝑖,𝑜(𝑁−1) −𝜂
1
𝑁√2ℎ∑
exp⁡(−
𝑒𝑛,ℎ
2
2 )
𝜕𝐸
𝜕𝛾𝑖,𝑜
𝑁
𝑛=1
 
(48) 
where 𝜂 denotes the learning rate. (30), however, 
revisits preceding training samples which is 
intractable for the life-long learning case. It is 
therefore modified as follows: 
∑exp (−𝑒𝑛,ℎ
2
2 ) = 𝐴𝑁= 𝐴𝑁−1 + exp⁡(−𝑒𝑛,ℎ
2
2 )
𝑁
𝑛=1
 
    
The gradient term in (30) is derived using the chain 
rule as follows: 
𝜕𝐸
𝜕𝛾𝑖,𝑜
= 𝜕𝐸
𝜕𝑦
𝜕𝑦
𝜕𝜑𝑖,𝑜
𝜕𝜑𝑖,𝑜
𝜕𝛾𝑖,𝑜
 
𝜕𝐸
𝜕𝛾𝑖,𝑜= (𝑦𝑜−𝑡𝑜)(𝑅𝑖−𝜑𝑖,𝑜)
(𝑥𝑒𝑊𝑖,𝑜−𝑦0)
∑
𝜑𝑖,𝑜
𝑀
𝑖=1
 
 
The learning rate is well-known to greatly influence 
the convergence of learning process. A stable 
interval of the learning rate is derived using the 
Lyapunov stability criterion as follows: 
0 < 𝜂<
2𝑁√𝜋
(𝑃𝑜,𝑚𝑎𝑥)2𝐴𝑁 
 
 
(49) 
where 𝑃𝑜,𝑚𝑎𝑥≈
1
𝑀. This interval, however, does not 
guarantee fast convergence because of its static 
nature. This drawback, usually, warrants an adaptive 
learning rate as follows: 
 
𝜂= {𝜌1𝜂, 𝑓(0)𝑛≥𝑓(0)𝑛−1
𝜌2𝜂, 𝑓(0)𝑛< 𝑓(0)𝑛−1 
(50) 
where 𝜌1 ∈(1,1.5], 𝜌2 ∈[0.5,1) are learning rate 
factors which steer the fluctuation of learning rates. 
The learning rate goes up when the cost function 
augments to expedite the convergence rate. The 
learning rate decreases when the cost function 
lessens to mitigate the convergence rate. The 
parameter 
learning 
scenario 
actualises 
the 
problematizing of the Scaffolding theory as it 
contributes in handling the concept drift. 
B.3 When-to-Learn 
The when-to-learn strategy encompasses a sample 
coming through the what-to-learn strategy but does 
not satisfy the sample learning criteria in (19), (20), 
and (26). Such sample is set as reserved samples and 
intended for future use because it may be fruitful to 
refine the rule base for possible uncovered states of 
already seen training samples. These samples are 
learned when all training samples have been finished 
or in the realm of data streams when the system is 
idle, and no new samples are received.  
4. Problem Descriptions 
In this section, the experimental setup and the design 
of the evolving intelligent system is discussed. The 
experimental setup is the same as described in 
(Dimla et al., 2000) but is detailed here for the 
convenience of readers. The machine used in the 
experiment was a variable speed centered lathe of 
type Lang Swing J6. 
Workpiece
PCwith DAC
Coupler
Dynamometer
Triaxial accelerometer
Insert
Toolholder
Charge
amplifier
Junction
Box
Monitoring
(oscilloscope)
 
Figure 4.  The Schematic of experimental test rig (Dimla et al, 
2000) 
The two tool inserts used, P15 and P25, were 
cemented carbide coated via chemical vapor 
deposition and consisted of grades of ‘throw-away’ 
indexable 
inserts 
with 
integral 
chip-breaker 
geometry, held in place by a negative rake tool 
holder.  P15 had a thick wear resistant coating on a 
hard, resistant substrate while P25 had a thick 
(10m) layer of Al2O3 on top of a medium size 
titanium carbon nitride (TiCN) giving it a high wear 
resistance. No cutting fluid was used. The workpiece 
material used was low carbon alloy steel of the EN24 
type (oil quenched, rolled and tempered) which is 
relatively hard to accelerate tool-wear at the expense 
of a shorter tool life. 
The sensors for the vibrations and cutting forces 
were a tri-axial Kistler mini accelerometers (type 
8730A) for acceleration signal measurement and a 
Kistler tool post dynamometer platform (type 
9263A) for cutting force measurement in three 
planes respectively. The signals from the sensors 
were passed through a signal conditioning unit and 
various peripheral signal conditioning instruments 
as shown in the schematic diagram (Figure 4).  
Sampling was performed at a frequency of 30 kHz 
while recording 4096 data samples per channel. 
In the traditional TCM, interrupted test cuts were 
conducted at fixed cutting conditions with fresh tool 
inserts until failure or when wear levels had 
accumulated at which continued cutting risked 
catastrophic failure.  The metacognitive TCM offers 
a flexible avenue where the training process was 
carried out on the fly and importantly incurs low 
labelling cost because each cutting process does not 
necessarily lead to manual labelling effort by 
operator through visual inspection of cutting 
condition. Due to the rate of tool wear, cuts normally 
lasted less than 10 seconds at the beginning of each 
run.  As the cutting process progressed, the duration 
of each cut was systematically increased to well over 
30 seconds for complete stabilization of the cutting 
process to be achieved while at the same time 
allowing significant tool wear accumulation.


## Page 13


13 
We assigned different machining parameters in 
terms of cutting speed, feed-rate and depth of cut for 
each cut to suit the production requirement. During 
each run, the cutting force and vibration picked up 
by the force sensor and accelerometer were recorded 
online and generated data streams. When operator’s 
intervention is needed to feed the ground truth of the 
cutter’s condition, the cutting tool is manually 
inspected – with the flank and nose being measured. 
The measurement is then compared against a pre-set 
threshold to determine the state of the tool, as 
follows (Dimlan et al., 2000): 
 
 
Table 1: Examples of machining parameters, measured signals, and tool wear 
Cutting 
speed 
Feed-
rate 
Depth 
of cut 
Static 
Force 
X 
Static 
Force 
Y 
Static 
Force 
Z 
Dyna-
mic 
Force 
X 
Dyna-
mic 
Force 
Y 
Dyna-
mic 
Force 
Z 
Acce-
lera-
tion 
X 
Acce-
lera-
tion 
Y 
Acce-
lera-
tion  
Z 
Flank 
Nose 
Chip-
ped 
0.857 
0.5 
0.571 
0.604 
0.603 
0.726 
0.475 
0.296 
0.43 
0.545 
0.502 
0.485 
1 
1 
1 
0.786 
0.75 
0.571 
0.133 
0.088 
0.682 
0.681 
0.394 
0.632 
0.748 
0.537 
0.546 
0 
0 
0 
0.786 
0.25 
0.571 
0.087 
0.063 
0.261 
0.235 
0.097 
0.169 
0.217 
0.147 
0.118 
1 
0 
0 
0.786 
0.25 
0.571 
0.086 
0.061 
0.276 
0.167 
0.083 
0.128 
0.191 
0.133 
0.113 
0 
0 
0 
• 
000 – nominally sharp 
• 
100 – high flank wear 
• 
010 – high nose wear 
• 
001 – chipped/fractured nose 
• 
110 – high flank and high nose wear 
• 
111 – high flank and chip / fractured nose 
The aforementioned pre-set threshold is as follows: 
• 
Flank wear mark value ≤ 0.15mm, tool 
insert nominally sharp 
• 
Flank wear mark value > 0.15mm, tool 
insert worn (high flank) 
• 
Nose wear length ≤ 0.2mm, nominally 
sharp 
• 
Nose wear length > 0.2mm, tool worn 
(nose fractured / chipped) 
Table 2. Consolidated Numerical Results of Benchmarked 
Algorithms 
Algorithms 
CR 
RT 
NS 
FR 
rClass 
0.84 
0.56 
26 
2 
eClass 
0.75 
1.3 
50 
10 
pClass 
0.75 
0.65 
50 
1 
GENEFIS-
class 
0.78 
0.6 
50 
10 
gClass 
0.71 
0.68 
50 
2 
IT2McFIS 
0.83 
0.7 
36 
9 
CR: Classification Rate, RT: Runtime, NS: Number of Samples, 
Fuzzy Rules 
The monitoring process was carried out fully in the 
online mode with an intermittent stoppage to label 
data streams. Note that the cutting force and 
vibration are continuously recorded during each run. 
The advantage of rClass is seen in the absence of a 
retraining phase when a new data record is observed. 
All training samples are processed on the fly without 
revisiting preceding samples. Examples of historical 
data captured in the experiment is shown in Table 1. 
Note: The depth of cut is an important parameter for 
the experiment because a deeper cut will naturally 
induce higher cutting force. To avoid confusion as 
to whether the increase in cutting force is due to 
worn tools or depth of cut, the latter should be 
included as the input parameter. Besides the 
measured cutting force and vibration, other signals 
such as spindle current, acoustic emission and 
temperature can be added as inputs to the predictive 
analytics in the future.  
Table 3. Consolidated Numerical Results of Benchmarked 
Algorithms 
Algorithms 
CR 
RT 
NS 
FR 
rClass 
0.84 
0.05 
26 
2 
eClass 
0.71 
0.28 
50 
11 
pClass 
0.77 
0.35 
50 
1 
GENEFIS-
class 
0.83 
0.45 
50 
8 
gClass 
0.8 
0.74 
50 
2 
IT2McFIS 
0.88 
0.34 
34 
14 
CR: Classification Rate, RT: Runtime, NS: Number of Samples, 
Fuzzy Rules 
5. Experiment 
The input of the EIS are the first 12 columns of Table 
1: cutting speed, feed-rate, depth of cut, static force 
(X,Y,Z), acceleration (X,Y,Z), while the remaining 
three columns are the cause of tool wear observed 
during the experiment. It is worth noting that there 
are three factors of the tool wear, namely flank wear, 
nose wear and chipped or fractured nose. The tool 
wear is attributed by a combination of the three 
factors: high flank wear and chip/fractured nose. Our 
dataset forms a four-classed multiclassification 
problem where the target classes covers four 
conditions: nominally sharp, high flank wear, high 
flank and nose wear, high flank wear and 
chipped/fractured nose. 50 samples were used to 
build our hypothesis, and subsequent 69 samples 
were utilized as the testing samples. rClass was 
compared against five state-of-the-art classifiers: 
• 
eClass (Angelov et al., 2008(a)) is a 
prominent evolving classifier in the literature, which 
forms an extension of eTS (Angelov, 2004) for 
classification problems. It takes advantage of 
eClustering to cluster the input space on the fly.


## Page 14


14 
• 
GENEFIS-class (Pratama et al., 2014(c)) is 
a modified version of GENEFIS to deal with the 
classification problem. It actualises a holistic 
concept of the EIS where a rule can be generated, 
merged, pruned on demands, while it is equipped 
with an online feature selection.  
• 
pClass (Pratama et al., 2015(a)) is an 
evolving classifier which enhances the GENEFIS-
class. It targets the uniform distribution assumption 
of the GENEFIS-class and is capable of addressing 
the recurring drift due to its rule recall scenario.  
• 
gClass (Pratama et al., 2015(b)) is a 
metacognitive classifier, which works fully in the 
single-pass learning mode. It goes beyond the 
standard metacognitive learning by introducing the 
Scaffolding theory into the how-to-learn phase. It 
can be seen as a semi-supervised learner as a result 
of the online active learning scenario.  
• 
McITSFIS (Subramanian, 2014(a)) is a 
metacognitive classifier which combines the theory 
of 
interval 
type-2 
fuzzy 
system 
into 
the 
metacognitive 
learning. 
It 
modifies 
McFIS 
(Subramanian, 2014(b)) into the interval type-2 
fuzzy system. 
All benchmarked algorithms are structured in the 
MIMO architecture. The consolidated algorithms 
are evaluated against four evaluation criteria: 
classification rate, the number of hidden nodes, the 
number of network parameters and the number of 
samples. 
Numerical 
results 
of 
benchmarked 
algorithms are summed up in Table 2.  
The advantage of rClass over its counterpart is 
obvious in Table 2 where it delivered the most 
encouraging accuracy while attaining the lowest 
complexity in terms of both the number of rule and 
the execution time. rClass achieved this result by 
exploiting the lowest number of samples confirming 
the success of the active learning scenario. 
We also simulated the performance of consolidated 
algorithms under a reduced input dimension – only 
7 input attributes. Cutting speed, deep of cut, which 
happen to be fixed machining parameters, are 
excluded. Figure 6(a) displays the trace of fuzzy rule 
during the training process, while Figure 6(b) 
visualizes the evolution of feature weights.  
Under a reduced input dimension, rClass still 
produced consistent performance with negligible 
deterioration in accuracy. Significant performance 
improvement is seen in IT2McFIS but it should be 
noted that it comes with higher complexities – 
number of rule, execution time and training samples. 
The self-evolving property of the rClass is 
confirmed in Figure 6(a) where it starts its learning 
process from scratch with an empty rule base and 
fuzzy rules are grown, pruned and merged flexibly 
during 
the 
training 
process. 
Figure 
6(b) 
demonstrates the feature weighting capability of 
rClass where feature weights can be dynamically 
assigned to input attributes in accordance with their 
significance to the training process. The feature 
weighting strategy induces the so-called soft 
dimensionality reduction minimizing the impact of 
poor input attributes. It differs from the hard input 
selection paradigm which causes discontinuity of the 
training process because once pruned an input 
attribute cannot be retrieved. The feature weighting 
mechanism also contributes positively to the 
compactness of the rule base since it results in a 
small distance to inconsequential input attributes.  
To 
further 
investigate 
the 
consistency 
of 
consolidated 
algorithms, 
another 
series 
of 
experiments using historical data instead of data 
streams was undertaken. Here 50-fold random 
permutation was followed where data are randomly 
shuffled to avoid data-order dependency. The data 
proportion for training and testing remained the 
same as the online scenario. Table 4 tabulates 
consolidated numerical results.  
From Table 4, it is seen that rClass delivered 
comparable predictive accuracy with significantly 
less complexity in terms of NS, FR, and RT. It is 
understood that this problem has a small sample size 
and this causes no significant difference in accuracy 
between the metacognitive classifier and the 
evolving classifier. However, rClass and gClass 
impose low labeling cost because not all samples are 
subject to a labeling effort.  
Table 4. Consolidated Numerical Results of Benchmarked 
Algorithms 
Algorithms 
CR 
RT 
NS 
FR 
rClass 
0.94±0.21 
0.01±0.01 
24.4 
2.4±0.5 
eClass 
0.92±0.03 
0.11±0.02 
50 
9.4±1.9 
pClass 
0.93±0.007 
0.01±0.005 
50 
3 
GENEFIS-
class 
0.91±0.05 
0.14±0.03 
50 
11.5±8.9 
gClass 
0.93±0.15 
0.33±0.11 
32.3 
3.9±1.1 
IT2McFIS 
0.93±0.21 
0.01±0.005 
34.4 
13.3±3.6 
CR: Classification Rate, RT: Runtime, NS: Number of Samples, 
Fuzzy Rules 
As with in the online procedure, we tested 
benchmarked algorithms with a lower input 
dimension. Seven input variables, namely feed rate, 
static components of cutting force in three cutting 
axis (X,Y,Z), dynamic components of cutting force 
in two cutting axis (X,Z) and accelerometer signal in 
Y axis are extracted to perform predictive analytics. 
Numerical results are tabulated in Table 5.  
Table 5. Consolidated Numerical Results of Benchmarked 
Algorithms 
Algorithms 
CR 
RT 
NS 
FR 
rClass 
0.93±0.2 
0.05±0.03 
32.4 
3.2±2.9 
eClass 
0.9±0.04 
0.22±0.08 
50 
9.2±2.3 
pClass 
0.88±0.00 
0.09±0.09 
50 
4 
GENEFIS-
class 
0.91±0.02 
0.32±0.17 
50 
6.9±4.7 
gClass 
0.71±0.14 
0.34±0.16 
33.5 
3.8±1.3 
McIT2FIS 
0.91±0.11 
0.38±0.16 
34.6 
13.3±3.4 
CR: Classification Rate, RT: Runtime, NS: Number of Samples, 
Fuzzy Rules 
It is observed that no significant performance 
difference exists with a lower dimensional dataset. 
rClass consistently outperforms its counterparts in 
all 
evaluation 
criteria. 
Notwithstanding 
that 
McIT2FIS consumed the same number of samples,


## Page 15


15 
it charged expensive labeling cost because the 
sample selection scenario was undertaken with full 
manual intervention.  
6. Conclusion 
A metacognitive approach to tool condition 
monitoring is proposed. It is designed using a 
recently 
published 
metacognitive 
learning 
algorithm, namely Recurrent Classifier (rClass). 
rClass presents a synergy between the metacognitive 
model and the Scaffolding theory which brings a 
step closer to a plug-and-play learner. The efficacy 
of rClass for PHM was investigated in the tool wear 
prediction of a variable speed centered lathe of type 
Lang Swing J6. It was compared against state-of-
the-art classifiers, and it was found that rClass 
produced the most encouraging accuracy, while 
retaining the most compact and parsimonious 
structure. Furthermore, rClass offered lower 
labeling cost and fast training speed than its 
counterparts. Our future work will be devoted 
toward improving the robustness of our algorithm 
against noisy data and missing values.   
Acknowledgements 
This work is fully supported by the LTU start-up grant. The fourth 
author acknowledges the Austrian research funding association 
(FFG) within the scope of the ’IKT of the future’ programme 
(contract # 849962), as well as the Austrian COMET-K2 
programme of the Linz Center of Mechatronics (LCM).  
 
Figure 6: (a) fuzzy rule evolution during the training process, (b) evolution of feature weights during the training process
References 
Ambhore, N., Kamble, D., Chinchanikar, S., Wayal, V .Tool 
Condition Monitoring System: A Review. Materials Today: 
Proceedings, 2015, 2(4)-(5), 3419-3428 
Angelov,P.P.,Filev,D.An approach to online identification of 
Takagi-Sugeno fuzzy models. IEEE Transactions on Systems, 
Man, and Cybernetics, Part B: Cybernetics, 2004, 34, 484-498. 
Angelov,P.P.,Zhou,X.Evolving fuzzy-rule-based classifiers from 
data 
streams. 
IEEE 
Transactions 
on 
Fuzzy 
Systems, 
2008(a),16(6), 1462-1475. 
Angelov,P.P.,Lughofer,E.,Zhou,X. Evolving fuzzy classifiers 
using different model architectures. Fuzzy Sets and Systems, 
2008(b),159(23), 3160-3182. 
Angelov, P.P, et al., Evolving Intelligent Systems - Methodology 
and Applications, John Wiley & Sons, New York, 2010 
Burke L. I.  Automated identification of tool wear states in 
machining processes : an application of self-organising neural 
networks.  PhD Thesis, Depart. of Ind. Eng. and Operations 
Research, UC at Berkeley, USA, 1989 
Byrne G., et al.  Tool Condition Monitoring  Systems (TCMS) - 
the state of research and industrial application.  Annals of CIRP, 
1995, 44(2), 541-567  
Cheng W.Y. and Juang, C.F., A Fuzzy Model With Online 
Incremental SVM and Margin-Selective Gradient Descent 
Learning for Classification Problems, IEEE Transactions on 
Fuzzy Systems, vol. 22 (2), pp. 324-337, 2014 
Dimla, D. E. Sr., Lister. P. M., Leighton, N. J. Neural Network 
Solutions to the Tool Condition Monitoring Problem in Metal 
Cutting – A Critical Review of Methods. International Journal of 
Machining Tools Manufacture, 1997, 37(9), 1219-1241 
Dimla, D. E. Snr.  Multivariate tool condition monitoring in a 
metal cutting operation using neural networks.  Ph.D. Thesis, 
School of Engineering, The University of Wolverhampton, 1998 
Dimla, D. E. Sr., Lister, P.M. On-line Metal Cutting Tool 
Condition Monitoring. II: Tool-state Classification using Multi-
Layer Perceptron Neural Networks. International Journal of 
Machine Tools and Manufacture. 2000, 40, 769-781 
Dimla D. E. Snr., Sensor signals for tool wear monitoring in metal 
cutting operations - a review of methods.  International Journal of 
Machine Tools & Manufacture, 2000, 40(8), 1073-1098 
Ding, S.X., Model-based fault diagnosis techniques, Springer 
2008 
Dornfeld D. A.  Neural network sensor fusion for tool condition 
monitoring.  Annals CIRP, 1990,  39/1, 101-105 
Elanayar S. V. T., Shin Y. C. and Kumara S.  Machining 
condition monitoring for automation using neural networks.  
ASME's Winter Annual Meeting, Monitoring and Control of 
Manufacturing Processes, PED, 1990, 44, 85-100. 
Elbestawi, M.A., Dumitrescu, M. Tool Condition Monitoring in 
Machining – Neural Networks. in IFIP International Federation 
for Information Processing, Vol. 220, Information Technology 
for Balanced Manufacturing Systems, ed. W. Shen (Boston: 
Springer), pp. 5-16 
Juang, C.F., Lin, Y.Y., Tu, C.C. A recurrent self-evolving fuzzy 
neural network with local feedbacks and its application to 
dynamic system processing. Fuzzy Sets and Systems, 2010, 
161(19), 2552-2568 
Khaleghi, B., Khamis, A., Karray F.O., Razavi S.N., Multisensor 
data fusion: A review of the state-of-the-art, Information Fusion, 
vol. 14 (1), pp. 28-44, 2013 
Karmathi, S. V.  On-line tool wear estimation in turning through 
sensor data fusion and neural networks.  Ph.D Thesis, Department 
of Industrial and Manufacturing Engineering, The Pennsylvania 
State University, USA, 1994 
Li, X., Er, M. J., Lim, B. S., Zhou, J. H., Gan, O.P., Rutkowski, 
L. Fuzzy Regression Modelling for Tool Performance Prediction 
and Degradation Detection. International Journal of Neural 
Systems, 2010, 20(5), 405-419,  
Lister, P. M.  On-line measurement of tool wear.  Ph.D. Thesis, 
Manufacturing and Machine Tools Division, Department of 
Mechanical Engineering, UMIST, 1993 
Liu T. I. and Ko E. J.  On-line recognition of drill wear via 
artificial neural networks.  ASME’s Winter Annual Meeting, 
Monitoring and Control for Manufact. Processes, PED, 1990, 44, 
101-110. 
Lughofer, E.. Evolving Fuzzy Systems --- Methodologies,


## Page 16


16 
Advanced Concepts and Applications, 2011 (a), Springer, 
Heidelberg. 
Lughofer, E. On-line incremental feature weighting in evolving 
fuzzy classifiers. Fuzzy Sets and Systems, 2011 (b), 163(1), 1-23. 
Lughofer, E., Single-Pass Active Learning with Conflict and 
Ignorance, Evolving Systems, vol. 3 (4),  pp. 251-271, 2012 
Lughofer, E., Sayed-Mouchaweh, M,. Autonomous Data Stream 
Clustering 
implementing 
Incremental 
Split-and-Merge 
Techniques --- Towards a Plug-and-Play Approach, Information 
Sciences, 2015(a), 204, 54-79. 
Lughofer, E., Cernuda, C., Kindermann, S., Pratama, M. 
Generalized Smart Evolving Fuzzy Systems. Evolving Systems, 
2015(b), 6(4), 54-79. 
Noori-Khajavi A. and Komanduri R.  Frequency and time domain 
analyses of sensor signals in drilling-II. Investigation on some 
problems associated with sensor integration International Journal 
of Machine Tools Manufacture., 1995, 35(6), 795-815. 
Oentaryo, R.J et al. Bayesian ART-based fuzzy inference system: 
A new approach to prognosis of machining processes. in 
Proceedings of the IEEE International Conference on Prognostics 
and Health Management (PHM), Denver, Colorado, 2011, 1-10 
Oraby, S. E. and Hayhurst, D. R.  Development of models for tool 
wear force relationships in metal cutting.  International Journal of 
Machine Tools Manufacture, 1991, 33(2), 25-138 
Patra, J.C., Kot, A.C..Nonlinear dynamic system identification 
using Chebyshev functional linkartificial neuralnetworks, IEEE 
Transactions 
on 
Systems, 
Man, 
Cybernetics—Part 
B: 
Cybernetics, 2002, 32(4), 505–511. 
Pao, Y.H. Adaptive Pattern Recognition and Neural Networks. 
Reading, MA: Addison-Wesley, 1989  
Pan, Y., et al. Machine health condition prediction via online 
dynamic fuzzy neural networks. Engineering Applications of 
Artificial Intelligence, 2014, 25, 105-113 
Pratama.M.,Anavatti,S.,Angelov,P.P.,Lughofer,E. PANFIS: A 
novel incremental learning machine. IEEE Transactions on 
Neural Networks and Learning Systems, 2014(a), 25(1),55-68. 
Pratama,M., et al. GENEFIS: towards a localist network. IEEE 
Transactions on Fuzzy Systems, 2014(b), 22(3),547-562. 
Pratama, M., et al. A novel meta-cognitive-based scaffolding 
classifier to sequential non-stationary classification problems”, In 
proceeding of 2014 International Conference on Fuzzy Systems, 
2014(c), 369-376 
Pratama,M.,Anavatti,S.,Lughofer,E. 
pClass: 
an 
effective 
classifier to streaming examples. IEEE Transactions on Fuzzy 
Systems, 2015(a), 3(2), 369-386. 
Pratama,M.,Anavatti,S.,Lu,J. Recurrent classifier based on an 
incremental 
meta-cognitive 
scaffolding 
algorithm. 
IEEE 
Transactions on Fuzzy Systems, 2015(b), 23(6), 2048-2066. 
Rangwala, S. and Dornfeld, D.  Sensor integration using neural 
networks for intelligent tool condition monitoring.  Transactions 
of the American Society of Mechanical Engineers, Journal of 
Engineering for Industry., 1990, 112(3), 219-228 
Rehorn, A.G., et al. State-of-the-art Methods and Results in Tool 
Condition Monitoring: A Review. International Journal of 
Advanced Manufacturing Technology, 2005, 26, 693-710 
Sayed-Mouchaweh, M. and Lughofer, E., Learning in Non-
Stationary Environments: Methods and Applications, Springer, 
New York, 2012 
Shaw, M. C.  Metal cutting principles.  Clarendon Press, Oxford, 
1984, Chapter 3, pp 18-46 
Scheffer, C., Practical Machinery Vibration Analysis and 
Predictive Maintenance, Elsevier, Oxford, 2004. Schey J.A. 
Introduction to Manufacturing Processes. 2nd Edition, McGraw-
Hill Book Company, 1987, Chapter 8, pp 441 
Suresh,S., Dong, K., Kim.H. A sequential learning algorithm for 
self-adaptive 
resource 
allocation 
network 
 
classifier,” 
Neurocomputing, 2010, 73(16), 3012–3019. 
Subramanian, K., Savitha, R., Suresh, R. Zero-Error Density 
Maximization Based Learning Algorithm for a Neuro-Fuzzy 
Inference System‖, in proceeding of IEEE Conference on Fuzzy 
System (Fuzz-IEEE), Hyderabad, India, 2013,1-7 
Subramanian,K.,Suresh,S., Sundararajan,N.A Meta-Cognitive 
Neuro-Fuzzy 
Inference 
System 
(McFIS) 
for 
sequential 
classification systems. IEEE Transactions on Fuzzy Systems, 
2014(a), 21(6), 1080-1095. 
Subramanian,K.,Das,A.K,Suresh,S.,Savitha,R. A meta-cognitive 
interval type-2 fuzzy inference system and its projection based 
learning algorithm. Evolving Systems, 2014(b), 5(4),219-230. 
Wang, H., et al, W. Fisher Discriminant Analysis with L1-
Normal. IEEE Transactions on Cybernetics, 2014, 44(6), 828-842 
Wang, N., Er, M. J., Meng, X., Li, X. An Online Self-organizing 
Scheme for Parsimonious and Accurate Fuzzy Neural Networks. 
International Journal of Neural Systems, 2010, 20(5), 389-403 
Wood,D. Scaffolding contingent tutoring and computer-based 
learning”, International Journal of Artificial Intelligence in 
Education, 2001, 12(3), 280-292. 
Xu, Y., Wong, K.W., Leung, C.S. Generalized Recursive Least 
Square to The Training of Neural Network. IEEE Transaction on 
Neural Networks, 2006, 17(1). 
Xiong,S.,Azimi,J.,Fern,X.Z.(2014). 
Active 
Learning 
of 
Constraints for Semi-Supervised Clustering. . IEEE Transactions 
on Knowledge and Data Engineering.26(1),43-54. 
Vigdor,B.,Lerner.B.The 
Bayesian 
ARTMAP,” 
IEEE 
Transactions on Neural Networks, 2007, 18(6).1628–1644. 
Yager, R.R., Filev, D.P. Generation of Fuzzy Rules by Mountain 
Clustering. Journal of Intelligent and Fuzzy Rules, 1994, 2(3), 
209-219 
Zliobaite,I., Bifet,A., Pfahringer.B., Holmes, B.Active Learning 
with Drifting Streaming Data. IEEE Transactions on Neural 
Networks and Learning Systems, (2014), 25(1), 27-39.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.00499v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1906.00499v1_Budgeted_Policy_Learning_for_Task-Oriented_Dialogue_Systems

> Source: 1906.00499v1_Budgeted_Policy_Learning_for_Task-Oriented_Dialogue_Systems.pdf

> Pages: 10

---


## Page 1


Budgeted Policy Learning for Task-Oriented Dialogue Systems
Zhirui Zhang†
Xiujun Li‡§
Jianfeng Gao‡
Enhong Chen†
†University of Science and Technology of China
‡Microsoft Research AI
§University of Washington
†zrustc11@gmail.com
†cheneh@ustc.edu.cn
‡{xiul,jfgao}@microsoft.com
Abstract
This paper presents a new approach that ex-
tends Deep Dyna-Q (DDQ) by incorporating
a Budget-Conscious Scheduling (BCS) to best
utilize a ﬁxed, small amount of user interac-
tions (budget) for learning task-oriented dia-
logue agents. BCS consists of (1) a Poisson-
based global scheduler to allocate budget over
different stages of training; (2) a controller to
decide at each training step whether the agent
is trained using real or simulated experiences;
(3) a user goal sampling module to generate
the experiences that are most effective for pol-
icy learning. Experiments on a movie-ticket
booking task with simulated and real users
show that our approach leads to signiﬁcant im-
provements in success rate over the state-of-
the-art baselines given the ﬁxed budget.
1
Introduction
There has been a growing interest in exploiting
reinforcement learning (RL) for dialogue policy
learning in task-oriented dialogue systems (Levin
et al., 1997; Williams, 2008; Young et al., 2013;
Fatemi et al., 2016; Zhao and Esk´enazi, 2016; Su
et al., 2016; Li et al., 2017; Williams et al., 2017;
Dhingra et al., 2017; Budzianowski et al., 2017;
Chang et al., 2017; Liu and Lane, 2017; Liu et al.,
2018; Gao et al., 2019).
This is a challenging
machine learning task because an RL learner re-
quires real users to interact with a dialogue agent
constantly to provide feedback. The process in-
curs signiﬁcant real-world cost for complex tasks,
such as movie-ticket booking and travel planning,
which require exploration in a large state-action
space.
In reality, we often need to develop a dialogue
agent with some ﬁxed, limited budget due to lim-
ited project funding, conversational data, and de-
velopment time.
Speciﬁcally, in this study we
measure budget in terms of the number of real user
interactions. That is, we strive to optimize a dia-
logue agent via a ﬁxed, small number of interac-
tions with real users.
One common strategy is to leverage a user sim-
ulator built on human conversational data (Schatz-
mann et al., 2007; Li et al., 2016). However, due
to design bias and the limited amounts of pub-
licly available human conversational data for train-
ing the simulator, there always exists discrepan-
cies between the behaviors of real and simulated
users, which inevitably leads to a sub-optimal dia-
logue policy. Another strategy is to integrate plan-
ning into dialogue policy learning, as the Deep
Dyna-Q (DDQ) framework (Peng et al., 2018),
which effectively leverages a small number of real
experiences to learn a dialogue policy efﬁciently.
In DDQ, the limited amounts of real user experi-
ences are utilized for: (1) training a world model to
mimic real user behaviors and generate simulated
experiences; and (2) improving the dialogue pol-
icy using both real experiences via direct RL and
simulated experiences via indirect RL (planning).
Recently, some DDQ variants further incorporate
discriminators (Su et al., 2018) and active learn-
ing (Wu et al., 2019) into planning to obtain high-
quality simulated experiences.
DDQ and its variants face two challenges in the
ﬁxed-budget setting. First, DDQ lacks any explicit
guidance on how to generate highly effective real
dialogue experiences.
For example, the experi-
ences in the state-action space that has not, or less,
been explored by the dialogue agent are usually
more desirable. Second, DDQ lacks a mechanism
of letting a human (teacher) play the role of the
agent to explicitly demonstrate how to drive the
dialogue (Barlier et al., 2018). This is useful in the
cases where the dialogue agent fails to respond to
users in conversations and the sparse negative re-
wards fail to help the agent improve its dialogue
policy. To this end, DDQ needs to be equipped
arXiv:1906.00499v1  [cs.CL]  2 Jun 2019


## Page 2


Dialogue
Agent
User
World 
Model
Controller
Human 
Conversational Data
Scheduler
Budget
Real 
Experience
Simulated 
Experience
User Goal 
Sampling Module
Planning
Direct Reinforcement Learning
Acting
BCS
Figure 1: Proposed BCS-DDQ framework for dialogue policy learning. BCS represents the Budget-Conscious
Scheduling module, which consists of a scheduler, a controller and a user goal sampling module.
with the ability to decide whether to learn from
human demonstrations or from agent-user interac-
tions where the user can be a real user or simulated
by the world model.
In this paper, we propose a new framework,
called Budget-Conscious Scheduling-based Deep
Dyna-Q (BCS-DDQ), to best utilize a ﬁxed, small
number of human interactions (budget) for task-
oriented dialogue policy learning. Our new frame-
work extends DDQ by incorporating Budget-
Conscious Scheduling (BCS), which aims to con-
trol the budget and improve DDQ’s sample efﬁ-
ciency by leveraging active learning and human
teaching to handle the aforementioned issues. As
shown in Figure 1, the BCS module consists of
(1) a Poisson-based global scheduler to allocate
budget over the different stages of training; (2)
a user goal sampling module to select previously
failed or unexplored user goals to generate experi-
ences that are effective for dialogue policy learn-
ing; (3) a controller which decides (based on the
pre-allocated budget and the agent’s performance
on the sampled user goals) whether to collect
human-human conversation, or to conduct human-
agent interactions to obtain high-quality real ex-
periences, or to generate simulated experiences
through interaction with the world model. During
dialogue policy learning, real experiences are used
to train the world model via supervised learning
(world model learning) and directly improve the
dialogue policy via direct RL, while simulated ex-
periences are used to enhance the dialogue policy
via indirect RL (planning).
Experiments on the movie-ticket booking task
with simulated and real users show that our ap-
proach leads to signiﬁcant improvements in suc-
cess rate over the state-of-the-art baselines given a
ﬁxed budget. Our main contributions are two-fold:
• We propose a BCS-DDQ framework, to best uti-
lize a ﬁxed, small amount of user interactions
(budget) for task-oriented dialogue policy learn-
ing.
• We empirically validate the effectiveness of
BCS-DDQ on a movie-ticket booking domain
with simulated and real users.
2
Budget-Conscious Scheduling-based
Deep Dyna-Q (BCS-DDQ)
As illustrated in Figure 2, the BCS-DDQ di-
alogue system consists of six modules:
(1)
an LSTM-based natural language understanding
(NLU) module (Hakkani-T¨ur et al., 2016) for
identifying user intents and extracting associated
slots; (2) a state tracker (Mrksic et al., 2017) for
tracking dialogue state; (3) a dialogue policy that
chooses the next action based on the current state
and database results; (4) a model-based natural
language generation (NLG) module for producing
a natural language response (Wen et al., 2015);
(5) a world model for generating simulated user
actions and simulated rewards; and (6) the BCS
module incorporating a global scheduler, a user
goal sampling module and a controller, to man-
age the budget and select the most effective way to
generate real or simulated experiences for learning
a dialogue policy.
To leverage BCS in dialogue policy learning,
we design a new iterative training algorithm,
called BCS-DDQ, as summarized in Algorithm 1.
It starts with an initial dialogue policy and an ini-


## Page 3


Natural Language 
Generation (NLG)
Natural Language 
Understanding (NLU)
𝑜1
𝑜2
Dialogue State Tracker
𝑜𝑡
Dialogue Policy Learning
Dialogue Manager
System Action (Policy)
𝑠𝑡
𝑠1
𝑠2
𝑠𝑛
𝑎1
𝑎2
𝑎𝑘
……
…
Semantic Frame
State Representation
𝑎∗= max
𝑎
𝜋𝑎|𝑠
Backend 
Database
Controller
Scheduler
Budget
User Goal 
Sampling Module
Budget-Conscious 
Scheduling (BCS)
User
World Model
Human-Human
1
2
3
4
5
6
Figure 2: Illustration of the proposed BCS-DDQ dia-
logue system.
tial world model, both trained with pre-collected
human conversational data. Given the total bud-
get b and maximum number of training epochs
m, the scheduler allocates the available budget bk
at each training step. Then, the user goal sam-
pling module actively selects a previously failed
or unexplored user goal gu. Based on the agent’s
performance and the current pre-allocated bud-
get, the controller chooses the most effective way,
with cost cu = {0, 1, 2}, to generate real or sim-
ulated experiences Br/Bs for this sampled user
goal. For convenience, the cost of different dia-
logue generation methods is deﬁned as the number
of people involved:
• cost cu = 2 for collecting human-human demon-
strated conversational data.
• cost cu = 1 for conducting the interactions be-
tween human and agent.
• cost cu = 0 for performing the interactions be-
tween world model and agent.
The generated experiences are used to update the
dialogue policy and the world model. This pro-
cess continues until all pre-allocated budget is ex-
hausted.
In the rest of this section, we detail
the components of BCS, and describe the learn-
ing methods of the dialogue agent and the world
model.
2.1
Budget-Conscious Scheduling (BCS)
As illustrated in Figure 2 and Algorithm 1, BSC
consists of a budget allocation algorithm for the
scheduler, an active sampling strategy for the user
Algorithm 1 BCS-DDQ for Dialogue Policy
Learning
Input: The total budget b, the maximum number
of training epochs m, the dialogue agent A and
the world model W (both pre-trained with pre-
collected human conversational data);
1: procedure TRAINING PROCESS
2:
while k < m do
3:
bk ←Scheduler(b, m, k);
4:
repeat
5:
gu ←UserGoalSampler(A);
6:
Br, Bs, cu ←Controller(gu, bk,
A, W);
7:
bk ←bk −cu;
8:
until bk ≤0
9:
Train the dialogue agent A on Br ∪Bs
10:
Train world model W on Br
11:
end while
12: end procedure
goal sampling module, and a selection policy for
the controller.
2.1.1
Poisson-based Budget Allocation
The global scheduler is designed to allocate bud-
get {b1, . . . , bm} (where m is the ﬁnal training
epoch) during training. The budget allocation pro-
cess can be viewed as a series of random events,
where the allocated budget is a random variable.
In this manner, the whole allocation process es-
sentially is a discrete stochastic process, which can
be modeled as a Poisson process. Speciﬁcally, at
each training step k, the probability distribution of
a random variable bk equaling n is given by:
P{bk = n} = λn
k
n! e−λk, λk = m + 1 −k
m
λ (1)
The global scheduling in BCS is based on a De-
cayed Possion Process, motivated by two consid-
erations: (1) For simplicity, we assume that all
budget allocations are mutually-independent. The
Poisson process is suitable for this assumption.
(2) As the training process progresses, the dia-
logue agent tends to produce higher-quality dia-
logue experiences using the world model due to
the improving performance of both the agent and
the world model. As a result, the budget demand
for the agent decays during the course of training.
Thus, we linearly decay the parameter of the Pois-
son distribution so as to allocate more budget at
the beginning of training.


## Page 4


In addition, to ensure that the sum of the allo-
cated budget does not exceed the total budget b,
we impose the following constraint:
m
X
k=1
E[bk] =
m
X
k=1
m + 1 −k
m
λ ≤b
(2)
Using this formula, we can calculate the range of
the parameter value: λ ≤
2b
m+1. In our experi-
ments, we set λ =
2b
m+1 and sample bk from the
probability distribution deﬁned in Equation 1.
2.1.2
Active Sampling Strategy
The active sampling strategy involves the deﬁni-
tion of a user goal space and sampling algorithm.
In a typical task-oriented dialogue (Schatzmann
et al., 2007), the user begins a conversation with
a user goal gu which consists of multiple con-
straints. In fact, these constraints correspond to
attributes in the knowledge base. For example, in
the movie-ticket-booking scenario, the constraints
may be the name of the theater (theater), the
number of tickets to buy (numberofpeople) or
the name of the movie (moviename), and so on.
Given the knowledge base, we can generate large
amounts of user goals by traversing the combina-
tion of all the attributes, and then ﬁltering unrea-
sonable user goals which are not similar to real
user goals collected from human-human conver-
sational data. We then group the user goals with
the same inform and request slots into a category.
Suppose there are altogether l different categories
of user goals. We design a Thompson-Sampling-
like algorithm (Chapelle and Li, 2011; Eckles and
Kaptein, 2014; Russo et al., 2018) to actively se-
lect a previously failed or unexplored user goal in
two steps.
• Draw a number pi for each category follow-
ing pi ∼N(fi,
q
l ln N
ni ), where N represents
the Gaussian distribution, fi denotes the fail-
ure rate of each category estimated on the val-
idation set, ni is the number of samples for
each category and N = P
i ni.
• Select the category with maximum pi, then
randomly sample a user goal gu in the cate-
gory.
Using this method, user goals in the categories
with higher failure rates or less exploration are
more likely to be selected during training, which
encourages the real or simulated user to generate
dialogue experiences in the state-action space that
the agent has not fully explored.
2.1.3
Controller
Given a sampled user goal gu, based on the agent’s
performance on gu and pre-allocated budget bk,
the controller decides whether to collect human-
human dialogues, human-agent dialogues, or sim-
ulated dialogues between the agent and the world
model. We design a heuristic selection policy of
Equation 3 where dialogue experiences B are col-
lected as follow: we ﬁrst generate a set of simu-
lated dialogues Bs given gu, and record the suc-
cess rate Sgu. If Sgu is higher than a threshold λ1
(i.e. λ1 = 2/3) or there is no budget left, we use
Bs for training. If Sgu is lower than a threshold
λ2 (i.e. λ2 = 1/3) and there is still budget, we
resort to human agents and real users to generate
real experiences Br
hh. Otherwise, we collect real
experiences generated by human users and the di-
alogue agent Br
ha.
(B, cu) =



(Bs , 0)
if Sgu ≥λ1 or bk = 0
(Br
hh, 2)
if Sgu ≤λ2 and bk ≥2
(Br
ha, 1)
otherwise
(3)
Combined with the active sampling strategy,
this selection policy makes fuller use of the bud-
get to generate experiences that are most effective
for dialogue policy learning.
2.2
Direct Reinforcement Learning and
Planning
Policy learning in task-oriented dialogue using RL
can be cast as a Markov Decision Process which
consists of a sequence of <state, action, reward>
tuples. We can use the same Q-learning algorithm
to train the dialogue agent using either real or sim-
ulated experiences. Here we employ the Deep Q-
network (DQN) (Mnih et al., 2015).
Speciﬁcally, at each step, the agent observes the
dialogue state s, then chooses an action a using an
ϵ-greedy policy that selects a random action with
probability ϵ, and otherwise follows the greedy
policy a = arg maxa′ Q(s, a′; θQ). Q(s, a; θQ)
approximates the state-action value function with
a Multi-Layer Perceptron (MLP) parameterized by
θQ. Afterwards, the agent receives reward r, ob-
serves the next user or simulator response, and up-
dates the state to s′. The experience (s, a, r, au, s′)
is then stored in a real experience buffer Br1 or
simulated experience buffer Bs depending on the
source. Given these experiences, we optimize the
1Br = {Br
hh, Br
ha}


## Page 5


value function Q(s, a; θQ) through mean-squared
loss:
L(θQ) = E(s,a,r,s′)∼Br∪Bs[(y −Q(s, a; θQ))2]
y = r + γ max
a′
Q′(s′, a′; θQ′)
(4)
where γ ∈[0, 1] is a discount factor, and Q′(·) is
the target value function that is updated only peri-
odically (i.e., ﬁxed-target). The updating of Q(·)
thus is conducted through differentiating this ob-
jective function via mini-batch gradient descent.
2.3
World Model Learning
We utilize the same design of the world model
in Peng et al. (2018), which is implemented as a
multi-task deep neural network. At each turn of
a dialogue, the world model takes the current di-
alogue state s and the last system action a from
the agent as input, and generates the correspond-
ing user response au, reward r, and a binary ter-
mination signal t. The computation for each term
can be shown as below:
h = tanh(Wh[s, a] + bh)
r = Wrh + br
au = softmax(Wah + ba)
t = sigmoid(Wth + bt)
(5)
where all W and b are weight matrices and bias
vectors respectively.
3
Experiments
We evaluate BCS-DDQ on a movie-ticket booking
task in three settings: simulation, human evalua-
tion and human-in-the-loop training. All the ex-
periments are conducted on the text level.
3.1
Setup
Dataset.
The dialogue dataset used in this study
is a subset of the movie-ticket booking dialogue
dataset released in Microsoft Dialogue Chal-
lenge (Li et al., 2018).
Our dataset consists of
280 dialogues, which have been manually labeled
based on the schema deﬁned by domain experts, as
in Table 1. The average length of these dialogues
is 11 turns.
Dialogue Agents.
We benchmark the BCS-
DDQ agent with several baseline agents:
• The SL agent is learned by a variant of imita-
tion learning (Lipton et al., 2018). At the begin-
ning of training, the entire budget is used to col-
Intent
request, inform, deny, conﬁrm question,
conﬁrm answer, greeting, closing, not sure,
multiple choice, thanks, welcome
Slot
city, closing, date, distanceconstraints,
greeting, moviename, numberofpeople,
price, starttime, state, taskcomplete, theater,
theater chain, ticket, video format, zip
Table 1: The dialogue annotation schema
lect human-human dialogues, based on which
the dialogue agent is trained.
• The DQN agent is learned by standard DQN
At each epoch of training, the budget is spent
on human-agent interactions, and the agent is
trained by direct RL.
• The DDQ agent is learned by the DDQ method
(Peng et al., 2018). The training process is sim-
ilar to that of the DQN agent, differing in that
DDQ integrates a jointly-trained world model
to generate simulated experience which can fur-
ther improve the dialogue policy. At each epoch
of training, the budget is spent on human-agent
interactions.
• The BCS-DDQ agent is learned by the proposed
BCS-DDQ approach. For a fair comparison, we
use the same number of training epochs m used
for the DQN and DDQ agents.
Hyper-parameter Settings.
We use an MLP to
parameterize function Q(·) in all the dialogue
agents (SL, DQN, DDQ and BCS-DDQ), with
hidden layer size set to 80.
The ϵ-greedy pol-
icy is adopted for exploration. We set discount
factor γ = 0.9. The target value function Q′(·)
is updated at the end of each epoch. The world
model contains one shared hidden layer and three
task-speciﬁc hidden layers, all of size 80.
The
number of planning steps is set to 5 for using
the world model to improve the agent’s policy in
DDQ and BCS-DDQ frameworks. Each dialogue
is allowed a maximum of 40 turns, and dialogues
exceeding this maximum are considered failures.
Other parameters used in BCS-DDQ are set as
l = 128, d = 10.
Training Details.
The parameters of all neu-
ral networks are initialized using a normal dis-
tribution with a mean of 0 and a variance of
p
6/(drow + dcol), where drow and dcol are the
number of rows and columns in the structure (Glo-
rot and Bengio, 2010). All models are optimized
by RMSProp (Tieleman and Hinton, 2012). The
mini-batch size is set to 16 and the initial learn-


## Page 6


10
20
30
40
50
60
70
80
90
50
100
150
200
250
300
Success Rate(%)
Budget
SL
DQN
DDQ
BCS-DDQ
Figure 3: The success rates of different agents (SL,
DQN, DDQ, BCS-DDQ) given a ﬁxed budget (b =
{50, 100, 150, 200, 250, 300}). Each number is aver-
aged over 5 runs, each run tested on 50 dialogues.
ing rate is 5e-4. The buffer sizes of Br and Bs
are set to 3000. In order to train the agents more
efﬁciently, we utilized a variant of imitation learn-
ing, Reply Buffer Spiking (Lipton et al., 2018), to
pre-train all agent variants at the starting stage.
3.2
Simulation Evaluation
In this setting, the dialogue agents are trained and
evaluated by interacting with the user simulators
(Li et al., 2016) instead of real users. In spite of
the discrepancy between simulated and real users,
this setting enables us to perform a detailed analy-
sis of all agents without any real-world cost. Dur-
ing training, the simulator provides a simulated
user response on each turn and a reward signal
at the end of the dialogue. The dialogue is con-
sidered successful if and only if a movie ticket is
booked successfully and the information provided
by the agent satisﬁes all the user’s constraints (user
goal). When the dialogue is completed, the agent
receives a positive reward of 2 ∗L for success, or
a negative reward of −L for failure, where L is
the maximum number of turns allowed (40). To
encourage shorter dialogues, the agent receives a
reward of −1 on each turn.
In addition to the user simulator, the train-
ing of SL and BCS-DDQ agents requires a high-
performance dialogue agent to play the role of the
human agent in collecting human-human conver-
sational data. In the simulation setting, we lever-
age a well-trained DQN agent as the human agent.
0
50
100
150
200
250
300
Simulation Epoch
0
10
20
30
40
50
60
70
80
90
Success Rate(%)
SL
DQN
DDQ
BCS-DDQ
Figure 4:
The learning curves of different agents
(DQN, DDQ and BCS-DDQ) with budget b = 300.
Main Results.
We evaluate the performance of
all agents (SL, DQN, DDQ, BCS-DDQ) given a
ﬁxed budget (b = {50, 100, 150, 200, 250, 300}).
As shown in Figure 3, the BCS-DDQ agent con-
sistently outperforms other baseline agents by a
statistically signiﬁcant margin. Speciﬁcally, when
the budget is small (b = 50), SL does better than
DQN and DDQ that haven’t been trained long
enough to obtain signiﬁcant positive reward. BCS-
DDQ leverages human demonstrations to explic-
itly guide the agent’s learning when the agent’s
performance is very bad. In this way, BCS-DDQ
not only takes advantage of imitation learning,
but also further improves the performance via ex-
ploration and RL. As the budget increases, DDQ
can leverage real experiences to learn a good pol-
icy. Our method achieves better performance than
DDQ, demonstrating that the BCS module can
better utilize the budget by directing exploration to
parts of the state-action space that have been less
explored.
Learning Curves.
We also investigate the train-
ing process of different agents. Figure 4 shows
the learning curves of different agents with a ﬁxed
budget (b = 300). At the beginning of training,
similar to a very small budget situation, the per-
formance of the BCS-DDQ agent improves faster
thanks to its combination of imitation learning
and reinforcement learning. After that, BCS-DDQ
consistently outperforms DQN and DDQ as train-
ing progresses. This proves that the BCS module
can generate higher quality dialogue experiences
for training dialogue policy.


## Page 7


Agent
Epoch=100
Epoch=150
Epoch=200
Success
Reward
Turns
Success
Reward
Turns
Success
Reward
Turns
DQN
0.3032
-18.77
32.31
0.4675
2.07
30.07
0.5401
18.94
26.59
DDQ
0.4204
-2.24
27.34
0.5467
15.46
22.26
0.6694
32.00
18.66
BCS-DDQ
0.7542
43.80
15.42
0.7870
47.38
16.13
0.7629
44.45
16.20
Table 2: The performance of different agents at training epoch = {100, 150, 200} in the human-in-the-loop experi-
ments. The differences between the results of all agent pairs evaluated at the same epoch are statistically signiﬁcant
(p < 0.05). (Success: success rate)
0
0.1
0.2
0.3
0.4
SL
Suc
0.7
0.8
0.9
34.39
54.05
64.12
81.94
0
10
20
30
40
50
60
70
80
90
SL
DQN
DDQ
BCS-DDQ
Success Rate(%)
70
74
78
72
p=0.013
Figure 5: The human evaluation results for SL, DQN,
DDQ and BCS-DDQ agents, the number of test dia-
logues indicated on each bar, and the p-values from a
two-sided permutation test. The differences between
the results of all agent pairs are statistically signiﬁcant
(p < 0.05).
3.3
Human Evaluation
For human evaluation, real users interact with dif-
ferent agents without knowing which agent is be-
hind the system. At the beginning of each dia-
logue session, we randomly pick one agent to con-
verse with the user. The user is provided with a
randomly-sampled user goal, and the dialogue ses-
sion can be terminated at any time, if the user be-
lieves that the dialogue is unlikely to succeed, or
if it lasts too long. In either case, the dialogue is
considered as failure. At the end of each dialogue,
the user is asked to give explicit feedback about
whether the conversation is successful.
Four agents (SL, DQN, DDQ and BCS-DDQ)
trained in simulation (with b = 300) are selected
for human evaluation. As illustrated in Figure 5,
the results are consistent with those in the simu-
lation evaluation (the rightmost group with bud-
get=300 in Figure 3). In addition, due to the dis-
crepancy between simulated users and real users,
the success rates of all agents drop compared to the
simulation evaluation, but the performance degra-
0
50
100
150
200
Epoch
0
10
20
30
40
50
60
70
80
90
Success Rate(%)
DQN
DDQ
BCS-DDQ
Figure 6: Human-in-the-Loop learning curves of dif-
ferent agents with budget b = 200.
dation of BCS-DDQ is minimal. This indicates
that our approach is more robust and effective than
the others.
3.4
Human-in-the-Loop Training
We further verify the effectiveness of our method
in human-in-the-loop training experiments. In this
experiment, we replace the user simulator with
real users during training. Similar to the human
evaluation, based on a randomly-sampled user
goal, the user converses with a randomly-selected
agent and gives feedback as to whether the con-
versation is successful. In order to collect human-
human conversations during the training of the
BCS-DDQ agent, human agents are interacting di-
rectly with real users through the dialogue system.
In a dialogue session, the human agent has access
to the conversation history, as well as the current
search results from the knowledge base, before se-
lecting each dialogue action in response to the real
user. Each learning curve is trained with two runs,
with each run assigning a budget of 200 human
interactions.
The main results are presented in Table 2 and
Figure 6. We can see that the BCS-DDQ agent
consistently outperforms DQN and DDQ during
the course of training, conﬁrming the conclusion


## Page 8


Real User Dialogue Sample
movie-ticket booking user goal:
{
“constraint slots”: {
“request slots”: {
“numberofpeople”: “four”
“ticket”:“?”
“moviename”: “creed”
“theater”: “?”
“city”: “regency”
}
“date”: “tomorrow”
“starttime”: “around noon”
}
}
DDQ agent
1
usr: I want to watch creed at around noon.
2
agt: around noon is available.
3
usr: I want four tickets please!
4
agt: Which city would you like?
5
usr: I want to watch at regency.
6
agt: Which theater would you like?
7
usr: Which theater is available?
8
agt: What date would you like to watch it?
9
usr: I want to set it up tomorrow.
10
agt: Which theater would you like?
11
usr: Which theater is available?
12
agt: Which city would you like?
13
usr: I want to watch at regency.
14
agt: Which theater would you like?
15
usr: Which theater is available?
16
agt: What date would you like to watch it?
...
Failure: Agent does not book the right ticket within the
max turns.
BCS-DDQ agent
1
usr: I want to watch creed at around noon.
2
agt: Which city would you like?
3
usr: I want to watch at regency.
4
agt: What date would you like to watch it?
5
usr: I want to set it up tomorrow.
6
agt: Which theater would you like?
7
usr: Which theater is available?
8
agt: century eastport 16 is available.
9
usr: Could you help me to book the tickets?
8
agt: How many tickets do you need?
9
usr: I want four tickets please!
10
agt:
Great - I was able to purchase 4 tickets for you
to see creed tomorrow at century eastport 16
theater in regency at around noon.
11
usr: Thank you.
12
agt: Thank you.
Success
Table 3: Sample dialogue sessions by DDQ and BCS-
DDQ agents trained at epoch 200 (with total budget
b = 200) in the human-in-the-loop experiments: (agt:
agent, usr: user)
drawn from the simulation evaluation. Besides,
Table 3 shows example dialogues produced by two
dialogue agents (DDQ and BCS-DDQ) interacting
with human users respectively. We can see that
DDQ agent fails to respond to the user question
“which theater is available?”, which lead to the re-
peated inquiry of theater information. By intro-
ducing human demonstrations for agent training,
0
50
100
150
200
250
300
Simulation Epoch
0
10
20
30
40
50
60
70
80
90
Success Rate(%)
BCS-DDQ
BCS-DDQ-var1
BCS-DDQ-var2
Figure 7: The learning curves of BCS-DDQ and its
variants agents with budget b = 300.
BCS-DDQ agent can successfully respond to the
available theater information.
3.5
Ablation Study
We investigate the relative contribution of the bud-
get allocation algorithm and the active sampling
strategy in BCS-DDQ by implementing two vari-
ant BCS-DDQ agents:
• The BCS-DDQ-var1 agent: Replacing the de-
cayed Poisson process with a regular Pois-
son process in the budget allocation algorithm,
which means that the parameter λ is set to
b
m
during training.
• The BCS-DDQ-var2 agent: Further replacing
the active sampling strategy with random sam-
pling, based on the BCS-DDQ-var1 agent.
The results in Figure 7 shows that the budget allo-
cation algorithm and active sampling strategy are
helpful for improving a dialogue policy in the lim-
ited budget setting. The active sampling strategy
is more important, without which the performance
drops signiﬁcantly.
4
Conclusion
We presented a new framework BCS-DDQ for
task-oriented dialogue policy learning. Compared
to previous work, our approach can better utilize
the limited real user interactions in a more efﬁcient
way in the ﬁxed budget setting, and its effective-
ness was demonstrated in the simulation evalua-
tion, human evaluation, including human-in-the-
loop experiments.
In future, we plan to investigate the effective-
ness of our method on more complex task-oriented
dialogue datasets.
Another interesting direction


## Page 9


is to design a trainable budget scheduler. In this
paper, the budget scheduler was created indepen-
dently of the dialogue policy training algorithm, so
a trainable budget scheduler may incur additional
cost. One possible solution is transfer learning, in
which we train the budget scheduler on some well-
deﬁned dialogue tasks, then leverage this sched-
uler to guide the policy learning on other complex
dialogue tasks.
5
Acknowledgments
We appreciate Sungjin Lee, Jinchao Li, Jingjing
Liu, Xiaodong Liu, and Ricky Loynd for the fruit-
ful discussions. We would like to thank the volun-
teers from Microsoft Research for helping us with
the human evaluation and the human-in-the-loop
experiments. We also thank the anonymous re-
viewers for their careful reading of our paper and
insightful comments. This work was done when
Zhirui Zhang was an intern at Microsoft Research.
References
Merwan
Barlier,
Romain
Laroche,
and
Olivier
Pietquin. 2018. Training dialogue systems with hu-
man advice. In AAMAS.
Pawel Budzianowski,
Stefan Ultes,
Pei hao Su,
Nikola Mrksic, Tsung-Hsien Wen, I˜nigo Casanueva,
Lina Maria Rojas-Barahona, and Milica Gasic.
2017. Sub-domain modelling for dialogue manage-
ment with hierarchical reinforcement learning. In
SIGDIAL.
Cheng Chang, Runzhe Yang, Lu Chen, Xiang Zhou,
and Kai Yu. 2017. Affordable on-line dialogue pol-
icy learning. In EMNLP.
Olivier Chapelle and Lihong Li. 2011. An empirical
evaluation of thompson sampling. In NIPS.
Bhuwan Dhingra, Lihong Li, Xiujun Li, Jianfeng
Gao, Yun-Nung Chen, Faisal Ahmed, and Li Deng.
2017.
End-to-end reinforcement learning of dia-
logue agents for information access. In ACL.
Dean Eckles and Maurits Kaptein. 2014.
Thomp-
son sampling with the online bootstrap.
CoRR,
abs/1410.4009.
Mehdi Fatemi, Layla El Asri, Hannes Schulz, Jing He,
and Kaheer Suleman. 2016. Policy networks with
two-stage training for dialogue systems.
In SIG-
DIAL Conference.
Jianfeng Gao, Michel Galley, and Lihong Li. 2019.
Neural approaches to conversational ai.
Founda-
tions and Trends R⃝in Information Retrieval, 13(2-
3):127–298.
Xavier Glorot and Yoshua Bengio. 2010. Understand-
ing the difﬁculty of training deep feedforward neural
networks. In AISTATS.
Dilek Z. Hakkani-T¨ur, G¨okhan T¨ur, Asli elikyilmaz,
Yun-Nung Chen, Jianfeng Gao, Li Deng, and Ye-
Yi Wang. 2016. Multi-domain joint semantic frame
parsing using bi-directional rnn-lstm.
In INTER-
SPEECH.
Esther Levin, Roberto Pieraccini, and Wieland Eck-
ert. 1997. Learning dialogue strategies within the
markov decision process framework. In ASRU 1997,
pages 72–79.
Xiujun Li, Yun-Nung Chen, Lihong Li, and Jianfeng
Gao. 2017. End-to-end task-completion neural dia-
logue systems. In IJCNLP.
Xiujun Li, Zachary C Lipton, Bhuwan Dhingra, Lihong
Li, Jianfeng Gao, and Yun-Nung Chen. 2016.
A
user simulator for task-completion dialogues. arXiv
preprint arXiv:1612.05688.
Xiujun Li, Sarah Panda, Jingjing Liu, and Jianfeng
Gao. 2018. Microsoft dialogue challenge: Building
end-to-end task-completion dialogue systems. arXiv
preprint arXiv:1807.11125.
Zachary C Lipton, Jianfeng Gao, Lihong Li, Xiujun
Li, Faisal Ahmed, and Li Deng. 2018. Efﬁcient ex-
ploration for dialogue policy learning with bbq net-
works & replay buffer spiking. AAAI.
Bing Liu and Ian Lane. 2017. Iterative policy learning
in end-to-end trainable task-oriented neural dialog
models. ASRU, pages 482–489.
Bing Liu, G¨okhan T¨ur, Dilek Z. Hakkani-T¨ur, Pararth
Shah, and Larry P. Heck. 2018.
Dialogue learn-
ing with human teaching and feedback in end-to-
end trainable task-oriented dialogue systems.
In
NAACL-HLT.
Volodymyr Mnih, Koray Kavukcuoglu, David Silver,
Andrei A. Rusu, Joel Veness, Marc G. Bellemare,
Alex Graves, Martin A. Riedmiller, Andreas Fidje-
land, Georg Ostrovski, Stig Petersen, Charles Beat-
tie, Amir Sadik, Ioannis Antonoglou, Helen King,
Dharshan Kumaran, Daan Wierstra, Shane Legg,
and Demis Hassabis. 2015.
Human-level con-
trol through deep reinforcement learning. Nature,
518:529–533.
Nikola Mrksic, Diarmuid ´O S´eaghdha, Tsung-Hsien
Wen, Blaise Thomson, and Steve J. Young. 2017.
Neural belief tracker: Data-driven dialogue state
tracking. In ACL.
Baolin Peng, Xiujun Li, Jianfeng Gao, Jingjing Liu,
and Kam-Fai Wong. 2018. Integrating planning for
task-completion dialogue policy learning. In ACL.
Daniel J Russo, Benjamin Van Roy, Abbas Kazerouni,
Ian Osband, Zheng Wen, et al. 2018. A tutorial on
thompson sampling. Foundations and Trends R⃝in
Machine Learning, 11(1):1–96.


## Page 10


Jost Schatzmann, Blaise Thomson, Karl Weilhammer,
Hui Ye, and Steve J. Young. 2007. Agenda-based
user simulation for bootstrapping a pomdp dialogue
system. In HLT-NAACL.
Peihao Su, Milica Gasic, Nikola Mrksic, Lina Maria
Rojas-Barahona,
Stefan Ultes,
David Vandyke,
Tsung-Hsien Wen, and Steve J. Young. 2016. Con-
tinuously learning neural dialogue management.
CoRR, abs/1606.02689.
Shang-Yu Su, Xiujun Li, Jianfeng Gao, Jingjing Liu,
and Yun-Nung Chen. 2018.
Discriminative deep
dyna-q: Robust planning for dialogue policy learn-
ing. In EMNLP.
Tijmen Tieleman and Geoffrey Hinton. 2012. Lecture
6.5-rmsprop: Divide the gradient by a running av-
erage of its recent magnitude. COURSERA: Neural
networks for machine learning, 4(2):26–31.
Tsung-Hsien Wen, Milica Gasic, Nikola Mrksic, Pei
hao Su, David Vandyke, and Steve J. Young. 2015.
Semantically conditioned lstm-based natural lan-
guage generation for spoken dialogue systems. In
EMNLP.
Jason D Williams. 2008.
The best of both worlds:
Unifying conventional dialog systems and pomdps.
In Ninth Annual Conference of the International
Speech Communication Association.
Jason D. Williams, Kavosh Asadi, and Geoffrey Zweig.
2017. Hybrid code networks: practical and efﬁcient
end-to-end dialog control with supervised and rein-
forcement learning. In ACL.
Yuexin Wu, Xiujun Li, Jianfeng Gao, Jingjing Liu, and
Yiming Yang. 2019. Switch-based active deep dyna-
q: Efﬁcient adaptive planning for task-completion
dialogue policy learning. In AAAI.
Steve J. Young, Milica Gasic, Blaise Thomson, and Ja-
son D. Williams. 2013. Pomdp-based statistical spo-
ken dialog systems: A review. Proceedings of the
IEEE, 101:1160–1179.
Tiancheng Zhao and Maxine Esk´enazi. 2016. Towards
end-to-end learning for dialog state tracking and
management using deep reinforcement learning. In
SIGDIAL Conference.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
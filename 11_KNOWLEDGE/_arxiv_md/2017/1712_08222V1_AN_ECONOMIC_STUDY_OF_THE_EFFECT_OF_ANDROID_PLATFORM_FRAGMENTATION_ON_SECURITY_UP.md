---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1712.08222v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1712.08222v1_An_Economic_Study_of_the_Effect_of_Android_Platform_Fragmentation_on_Security_Up

> Source: 1712.08222v1_An_Economic_Study_of_the_Effect_of_Android_Platform_Fragmentation_on_Security_Up.pdf

> Pages: 30

---


## Page 1


An Economic Study of the Eﬀect of Android
Platform Fragmentation on Security Updates
Sadegh Farhang1, Aron Laszka2, and Jens Grossklags3
1 Pennsylvania State University
2 University of Houston
3 Technical University of Munich
farhang@ist.psu.edu, alaszka@uh.edu, jens.grossklags@in.tum.de
Abstract. Vendors in the Android ecosystem typically customize their
devices by modifying Android Open Source Project (AOSP) code, adding
in-house developed proprietary software, and pre-installing third-party
applications. However, research has documented how various security
problems are associated with this customization process.
We develop a model of the Android ecosystem utilizing the concepts
of game theory and product diﬀerentiation to capture the competition
involving two vendors customizing the AOSP platform. We show how
the vendors are incentivized to diﬀerentiate their products from AOSP
and from each other, and how prices are shaped through this diﬀerentia-
tion process. We also consider two types of consumers: security-conscious
consumers who understand and care about security, and na¨ıve consumers
who lack the ability to correctly evaluate security properties of vendor-
supplied Android products or simply ignore security. It is evident that
vendors shirk on security investments in the latter case.
Regulators such as the U.S. Federal Trade Commission have sanctioned
Android vendors for underinvestment in security, but the exact eﬀects of
these sanctions are diﬃcult to disentangle with empirical data. Here, we
model the impact of a regulator-imposed ﬁne that incentivizes vendors to
match a minimum security standard. Interestingly, we show how product
prices will decrease for the same cost of customization in the presence of
a ﬁne, or a higher level of regulator-imposed minimum security.
1
Introduction
Android, the mobile operating system released under open-source licenses as
the Android Open Source Project (AOSP), has the largest market share among
smartphone platforms worldwide with more than one billion active devices [2].
Due to the openness of the platform, vendors and carriers can freely customize
features to diﬀerentiate their products from their competitors. This diﬀerentia-
tion includes customizing the hardware, but there is also a substantial fragmen-
tation in the software packages utilized in the Android ecosystem [11,15].
The fragmentation of the software base available from various vendors is due
to various customization steps, including the modiﬁcation of the open source
arXiv:1712.08222v1  [cs.CR]  21 Dec 2017


## Page 2


Android codebase as well as the addition of proprietary software. Product dif-
ferentiation may beneﬁt consumers by providing Android devices for sale that
better match consumer tastes, and may also beneﬁt businesses by helping them
to sidestep intense price competition of homogeneous product markets [17].
However, we also observe that Android platform fragmentation is associated
with a number of security challenges [16,18,19]. For example, Wu et al. showed
that a large proportion of security vulnerabilities in the Android ecosystem are
due to vendor customization. They calculated that this proportion is between
64% to 85% for diﬀerent vendors [18]. Similarly, Zhou et al. showed how cus-
tomized drivers for security-sensitive operations on Android devices available
by diﬀerent vendors often compare unfavorably to their respective counterparts
on the oﬃcial Android platform [19]. Thomas et al. provided evidence for the
substantial variability of security patch practices across diﬀerent vendors and
carriers [16]. Using a dataset about over 20,000 Android devices, they showed
that on average over 87% of the devices are exposed to at least one of 11 known
critical (and previously patched) vulnerabilities.4
The Android ecosystem fragmentation and the associated security problems
have caused consumer protection agencies to intervene in the marketplace. In
2013, the Federal Trade Commission (FTC) charged a leading vendor because it
“failed to employ reasonable and appropriate security practices in the design and
customization of the software on its mobile devices” [8]. The case was settled
and the vendor was required to “establish a comprehensive security program
designed to address security risks during the development of new devices and
to undergo independent security assessments every other year for the next 20
years” [8]. Not observing signiﬁcant improvements in the Android ecosystem,
the FTC recently solicited major vendors to provide detailed information about
their security practices including what vulnerabilities have aﬀected their devices
as well as whether and when the company patched those vulnerabilities [7].
In this paper, we propose a product diﬀerentiation model that captures key
facets of the Android ecosystem with a focus on the quality of security. We con-
sider multiple competing vendors, who can customize Android for their products
in order to diﬀerentiate themselves from their competitors. We consider both
security-conscious consumers, who value security quality, and na¨ıve consumers,
who do not take security issues into consideration when they make adoption
choices. When consumers are na¨ıve, vendors do not have any incentives to ad-
dress security issues arising from the customization. In order to incentivize in-
vesting in security, a regulator may impose a ﬁne on vendors that do not uphold
a desired level of security. We show that ﬁnes can achieve the desired eﬀect, and
we study how they impact the competitive landscape in the Android ecosystem.
Roadmap. In Section 2, we provide background on Android customization
and the associated security challenges. Section 3 presents the economic model on
Android customization. We analyze the model without a ﬁne in Section 4 and
4 Further compounding the problem scenario is how third-party apps targeting out-
dated Android versions and thereby disabling important security changes to the
Android platform cause additional fragmentation [14].


## Page 3


consider how to calculate the parameters in our model in Section 5. We extend
the model to the case with a regulator-imposed ﬁne in Section 6. We support
our analysis with numerical results in Section 7. We conclude in Section 8.
2
Background
Customization: One approach to measure the level of customization by vendors
is provenance analysis [18], which studies the distribution and origin of apps
on Android devices. There are mainly three sources of app origins on Android
devices: (1) AOSP: apps available in the default AOSP that, however, can be
customized by a vendor; (2) Vendor: apps that were developed by that vendor;
and (3) Third-party: apps that are not in AOSP and were not developed by the
vendor.
Table 1 summarizes the published ﬁndings of a provenance analysis of ﬁve
popular vendors: Google, Samsung, HTC, Sony, and LG [18]. The authors found
that on average 18.22%, 64.41%, and 17.38% of apps originate from AOSP, ven-
dors, and third parties, respectively. Further, the number of apps and lines of
code (LoC) associated with the devices are increasing with newly released ver-
sions. Likewise, the complexity of the baseline AOSP is increasing over time [18].
AOSP
vendor
3rd-party
Vendor
Device
Version and Build# #apps #LOC #apps #LOC #apps #LOC #apps #LOC
Samsung
Galaxy S2
2.3.4; 19100XWKI4
172
10M
26
2.4M
114
3.5M
32
4.1M
Samsung
Galaxy S3
4.0.4; 19300UBALF5
185
17M
30
6.3M
119
5.6M
36
5.3M
HTC
Wildfire S
2.3.5; CL362953
147
9.6M
24
2.7M
94
3.5M
29
3.3M
HTC
One X
4.0.4; CL100532
280
19M
29
4.7M
190
7.3M
61
7.5M
LG
Optimus P350
2.2; FRG83
100
6.1M
27
1.1M
40
0.6M
33
4.4M
LG
Optimus P880
4.0.3; IML74K
115
12M
28
3.1M
63
3.2M
24
5.6M
Sony
Xperia Arc S
2.3.4; 4.0.2.A.0.62
176
7.6M
28
1.1M
123
2.6M
25
3.8M
Sony
Xperia SL
4.0.4; 6.1.A.2.45
209
10M
28
1.8M
156
4.1M
25
4.7M
Google
Nexus S
2.3.6; GRK39F
73
5.2M
31
1M
41
2.8M
1
1.3M
Google
Nexus 4
4.2; JOP40C
91
15M
31
2.5M
57
12M
3
1.1M
Table 1. Provenance analysis [18].
One of the challenges in this fragmented ecosystem is the security risk that
arises from the vendors’ and carriers’ customization to enrich their systems’
functionality without fully understanding the security implications of their cus-
tomizations. In this paper, our focus is on security issues resulting from such
customization. Hence, we focus on this issue in the following subsection.
Security Impact of Customization: The problems related to security as-
pects of Android customization are mainly due to vendors’ change of critical
conﬁgurations. These changes include altering security conﬁgurations of Linux
device drivers and system apps, etc. One approach for better understanding
the eﬀect of customization is to compare security features of diﬀerent Android
devices with each other, which is called diﬀerential analysis. Aafer et al. pro-
posed a number of security features to take into account [1]. First, permissions
which protect data, functionalities, and inner components can be analyzed. In
Android, we have four level of permissions: Normal, Dangerous, Signature, Sys-
temOrSignature. The goal of diﬀerential analysis is to ﬁnd a permission with
a diﬀerent (and typically lower) level of protection on some devices. Second,
group IDs (GIDs) are another feature to take into account. Some lower-level
GIDs are given Android permissions, which could potentially be mapped into a


## Page 4


privileged permission due to customization. Protected broadcasts sent by system
level processes are a third important security feature. Due to customization, some
protected broadcasts could be removed and, as a result, apps can be triggered
by not only system-level processes but also by untrusted third-party apps.
By comparing these security features, Aafer et al. found that the smaller the
vendor is, the more signiﬁcant inconsistencies are observable for the diﬀerent
security features. One interpretation is that the cost of investment in security
is too high for those vendors (e.g., hiring of security experts). The results also
imply that diﬀerent vendors invest in security to diﬀerent degrees.
Research aiming to understand Android customization is clearly demonstrat-
ing that customization is a pervasive feature in Android, and this is associated
with a wide variety of security challenges and vulnerabilities. Further, we are
unaware of any research that provides evidence for security improvements re-
sulting from customization, which outweighs the aforementioned risks. At the
same time, research is missing that aims to understand the economic forces as-
sociated with the customization process which is the objective of our work.
3
Model Deﬁnition
In this section, we propose our baseline model in the tradition of game theory
and the theory of product diﬀerentiation [17,12]. Our model considers three types
of entities: (1) AOSP, (2) vendors, such as Samsung or LG, and (3) consumers.
AOSP: Google, the developer of Android, provides monthly security updates
for its devices and for base Android. However, other vendors have to adjust
AOSP security updates for their Android devices because of their customization.
Further, customization may also introduce new security vulnerabilities.
To incorporate these eﬀects into our model, we assume that a customized ver-
sion of Android can be represented by a point on the segment [0, 1]. Our analysis
could be extended to multidimensional customizations in a straightforward way,
but we assume one dimension for ease of presentation, since our focus is on the
relative level of customization rather than its direction. Moreover, the location
of each Android customization is independent of objective measures of product
quality. In other words, we map the features of a mobile device to a point on
the segment [0, 1] to quantify its diﬀerence (e.g., percentage of customized code)
from the base version of Android provided by AOSP. In our model, ZA denotes
the point corresponding to the base version of AOSP. Since AOSP aims to pro-
vide a base version that maximizes the market share of Android, it provides a
version that can attract the widest range of consumers. Hence, in the numerical
analysis, we assume that AOSP is in the middle, i.e., ZA = 0.5.
Vendor: There are multiple vendors selling Android devices. Carriers can
sell the vendors’ Android devices with their own prices and customizations too.
Here, we will use the term “vendor” to refer to both vendors and carriers. The
price and the market share of the device sold by vendor i are denoted by pi and
Di, respectively. Further, qi denotes the security quality of patches delivered by
vendor i. We assume that pi ≥0 (product prices are non-negative) and qi ≥0


## Page 5


(security quality is represented by a non-negative number) for every vendor i.
Similar to the AOSP base version, a point zi ∈[0, 1] represents the customization
of the Android version of vendor i.
We consider two types of costs for customization. First, through customiza-
tion, the vendor makes its product diﬀerent from what Google has developed in
AOSP. Hence, the vendor incurs development cost, which is related to the de-
gree of customization. Here, we model this cost as a convex quadratic function
of the diﬀerence between the vendor’s position and the positions of the AOSP
base version. Second, the security related cost of a vendor depends not only on
the quality and frequency of security updates provided by the vendor, but also
on the diﬀerence due to customization. Vendors receive security patch updates
from AOSP, but due to customizations, vendors need to adapt these security
patches before distribution. Often, vendors degrade the quality or frequency of
security patches in order to save development and distribution costs [16]. Hence,
the security-related cost is aﬀected by both the customization level and the se-
curity quality. In our model, we employ a convex quadratic function to capture
how the security cost of vendor i depends on qi. The utility of vendor i is equal
to:
πi = piDi −Ci (zi −ZA)2 −Siq2
i (zi −ZA)2 ,
(1)
where Ci and Si are constants representing cost per unit of customization and
security quality, respectively. Here, we focus on security issues resulting from
Android customization rather than security-related cost of AOSP explicitly.
We have considered quadratic functions for the cost terms, which is a common
assumption for modeling customization costs, e.g., see [4] and [6]. The quadratic
cost function captures the fact that the cost of customization increases as the
customization increases. In a similar way, with an increase in the cost of cus-
tomization or the quality of security, the security cost resulting from customiza-
tion increases. It would be possible to use any functional form with increasing
marginal cost, such as an exponential cost function, which would lead to the
same qualitative results as the ones presented here.
We also consider the quality of security patch updates provided by AOSP,
denoted by Q, to be an exogenous parameter in our model, which applies to all
vendors in the same way. Note that we observe that in practice, vendors virtu-
ally never provide better security quality. Further, we are primarily interested
in studying the eﬀect of customization on security; hence, we will not consider
vendors implementing additional security measures that are independent of cus-
tomization. Hence, we assume that the value of qi is upper bounded by Q.
Consumers: Consumers choose mobile devices primarily based on prices
and how well the devices match their preferences, but they may also consider
security quality. A consumer’s preference, similar to a vendor’s customization,
can be represented by a point x in [0, 1]. Consumers’ preferences for smartphone
selection are heterogeneous and we assume that the consumers’ preferences are
distributed uniformly in [0, 1]. We consider security-conscious consumers who
take security into account when choosing their product. The utility of consumer j


## Page 6


for choosing Android type i given that consumer j is at xj is:
ui
j = βqi −pi −T
 xj −zi
2 ,
(2)
where T represents the consumer’s utility loss for one unit of diﬀerence between
its preference and the location of the product, which we call customization-
importance. Similarly, β represents the consumer’s utility gain for one unit of
security quality, which we call security-importance. Na¨ıve consumers, who do not
understand or care about security quality, can be modeled by letting β = 0.
Our utility for consumers is in agreement with literature in economics [5]. It
is common to consider quadratic term in economics to model utility.
Game Formulation: For tractability, we consider a two-player game be-
tween vendor 1 and vendor 2 without any other vendors.5 In our analysis, we
assume that vendors are on diﬀerent sides of AOSP. Further, we let a = z1 and
1−b = z2. Without loss of generality, we assume that 0 ≤a ≤1−b ≤1. Figure 1
shows the location of vendor 1 and vendor 2.
The utilities of vendors 1 and 2 are then as follows:
π1 = p1D1 −C1 (a −ZA)2 −S1q2
1 (a −ZA)2 ,
(3)
π2 = p2D2 −C2 (1 −b −ZA)2 −S2q2
2 (1 −b −ZA)2 .
(4)
0
1
Vendor 1
AOSP
Vendor 2
a
b
Fig. 1. Location of vendor 1 and vendor 2.
To calculate the Nash equilibrium, we need to deﬁne the stages of the game,
i.e., the order in which the two players choose their prices, locations, and security
levels. For our analysis, we consider the following stages:
• Stage 1: Both vendors simultaneously choose their location parameters a
and b. They also choose their level of security quality, i.e., q1 and q2.
• Stage 2: Both vendors simultaneously choose their prices p1 and p2.
The reason is that a vendor freely modiﬁes the AOSP code base, adds its
developed proprietary software, and installs a diverse set of third-party apps to
customize its device. These changes, however, result in the change of critical
conﬁgurations leading to security issues [16,18,19]. Therefore, it is reasonable
to consider that the customization and security quality eﬀort happen at the
same stage. Then, by taking into account its eﬀort in customization and security
quality, the vendor chooses its price. We use backward induction to solve our
game. First, we consider stage 2 and calculate the price Nash equilibrium for
5 While we restrict our model to two vendors, we are aware that in practice, there
are more than two vendors competing with each other. However, we believe that
similar to classic economic studies with two companies in the context of product
diﬀerentiation, our model provides a meaningful understanding of the customization
in the Android ecosystem and of security quality.


## Page 7


given locations and quality. Then, we consider stage 1 and calculate the location
and quality equilibrium assuming a price equilibrium in stage 2.
Table 2 shows a list of the symbols used in our model.
Table 2. List of Symbols
Symbol Description
ZA
Point corresponding to AOSP
Di
Market share of vendor i
zi
Customization of the Android version of vendor i
pi
Price of vendor i
qi
Security quality of patches delivered by vendor i
Si
Cost per unit of security quality
Ci
Cost per unit of customization
πi
Utility of vendor i
Q
Quality of security patch updates provided by AOSP
β
Consumer’s security-importance
T
Consumer’s customization-importance
xj
Consumer’s location
ui
j
Utility of consumer j for choosing Android type i
qmin
Minimum level of security from the regulator’s point of view
fi
Fine function for vendor i
F
Monetary value of ﬁne for each unit of violation from qmin
4
Analytical Results
In this section, we analyze our proposed model. Before considering the two stages,
we ﬁrst have to ﬁnd the market shares of both vendors. To do so, we need to
ﬁnd the point in which a consumer j is indiﬀerent between choosing vendor 1’s
product and vendor 2’s product. This means that a user’s preference at this
point is identical for the two products. Hence, we have:
u1
j = u2
j
⇒βq1 −p1 −T
 xj −a
2 = βq2 −p2 −T
 1 −b −xj
2 .
(5)
Solving the above equation yields:
D1 = xj = a + 1 −a −b
2
+
β (q1 −q2)
2T (1 −a −b) +
p2 −p1
2T (1 −a −b).
(6)
All of the consumers that are on the left side of xj choose the product of
vendor 1. As a result, the market share of vendor 1 is D1 = xj. This means
that for equal prices and security qualities, vendor 1 controls its own “turf” of
size a and the consumers located between vendor 1 and vendor 2 that are closer
to vendor 1 than vendor 2. The last two terms represent the eﬀect of security
quality and price diﬀerentiation on the demand, respectively.
We restrict the model to consumers who deﬁnitely choose between these two
products, which is a reasonable assumption for a wide range of parameters given


## Page 8


the “cannot-live-without-it” desirability of modern phones, which is a valid as-
sumption in economics, see [17]. Hence, the remaining consumers choose vendor
2’s product and its demand is:
D2 = 1 −D1 = b + 1 −a −b
2
+
β (q2 −q1)
2T (1 −a −b) +
p1 −p2
2T (1 −a −b).
(7)
If two vendors are at the same location, they provide functionally identical
products. For a consumer who takes into account customization, price, and se-
curity quality, the factors that matter in this case are security quality and price.
To increase their market share, vendors have to decrease their prices or increase
their security quality. This will lead to lower product prices and higher costs
due to higher security quality, and signiﬁcantly lower – and eventually zero –
utility for both vendors. Hence, vendors have no incentives for implementing
customizations that result in identical product locations.
Price Competition: In the following, we state the price Nash equilibrium.
Theorem 1 The unique price Nash equilibrium always exists, and it is
p∗
1 = β
3 (q1 −q2) + T (1 −a −b)

1 + a −b
3

,
(8)
p∗
2 = β
3 (q2 −q1) + T (1 −a −b)

1 + b −a
3

.
(9)
Proof of Theorem 1 can be found in Appendix B.1.
In Theorem 1, the price of a product depends on both the security quality
and the customization level of both vendors. Further, the price depends on the
customization importance T and security-importance β constants, which model
the consumers in our model. A vendor can increase its price by improving its
security quality or customizing its devices more.
Quality and Product Choice: To calculate the Nash equilibrium of both
vendors in terms of location and security quality, we consider the following op-
timization problems.
Vendor 1 maximizes its utility in q1 and a considering that p1 is calculated
according to Equation 8. For vendor 1, we have:
maximize
a, q1
p∗
1D1 −C1 (a −ZA)2 −S1q2
1 (a −ZA)2
subject to
p∗
1 ≥0,
0 ≤a ≤ZA,
0 ≤q1 ≤Q.
(10)
The constraints in the above optimization problem reﬂect our previous as-
sumptions about the parameters in our model deﬁnition. For each value of b
and q2, the solution of the above optimization problem provides vendor 1’s best
response. In a similar way, for vendor 2, we have:
maximize
b, q2
p∗
2D2 −C2 (1 −b −ZA)2 −S2q2
2 (1 −b −ZA)2
subject to
p∗
2 ≥0,
0 ≤b ≤ZA,
0 ≤q2 ≤Q.
(11)


## Page 9


For given values of a and q1, the above optimization problem provides vendor
2’s best response. Based on the Nash equilibrium deﬁnition, the intersection of
these two optimization problems gives the Nash equilibrium of our proposed
game, i.e., a∗, b∗, q∗
1, and q∗
2. In Appendix B.2 , we provide our method for
solving these two optimization problems and for ﬁnding the Nash equilibrium.
Lemma 1 When consumers take into account security, zero investment in se-
curity for both vendors, i.e., q1 = q2 = 0, is not a Nash equilibrium.
Proof of Lemma 1 is provided in Appendix B.3.
The above lemma shows that when consumers take into account security,
then vendors have to invest to improve their security quality. However, it is
challenging for the majority of consumers to measure by themselves the security
quality of a product, or in this case, to make a comparison between the security
quality of many versions of Android provided by the vendors. Consumers mainly
rely on information that is made available to them.6 However, in the absence of
any reliable market signal, any unsubstantiated communication/advertisements
by vendors about security quality have to be considered with caution.7
Previous research has shown that businesses aim to exploit such information
barriers. In particular, the theory of informational market power posits that
when it is hard for consumers to understand and/or observe certain features
of a product (e.g., security quality), then businesses are incentivized to under-
invest in these product features and rather focus on easily observable aspects
such as product design and price [3].8 Any eﬀect of informational market power
is emphasized by well-known human biases such as omission neglect [13]. This
describes the human lack of sensitivity about product features that are not the
focus of advertisements or product communications; to paraphrase, consumers
will not include in their perceived utilities product features which are not empha-
sized. Therefore, in Appendix A, we consider an important baseline case of na¨ıve
consumers. In particular, we show that our model is in agreement with what we
have seen in practice, i.e., vendors do not invest in security when consumers are
na¨ıve. Further, we determine under what conditions maximal diﬀerentiation, i.e.,
a∗= b∗= 0, is Nash equilibrium; see Proposition 2 in Appendix A.
6 While we have identiﬁed a small set of research projects which aim to understand
the security impact of customization, e.g., [16,18,19], we are unaware of any well-
known market signals regarding the security of diﬀerent Android versions. The recent
FTC initiative to solicit security-relevant data from vendors may contribute to such
signals in the future [7].
7 In fact, research by Wu et al. shows that vendors of diﬀerent reputation (which
may also inﬂuence perceptions regarding Android security) all suﬀer from similar
challenges due to Android customization [18].
8 Note that it is not required that businesses have an accurate assessment of the
security quality of their own product (or competitors’ products) for informational
market power to be exploited.


## Page 10


5
Parameter Selection
In the previous section, the goal of our analyses was to ﬁnd these six variables:
p1, p2, q1, q2, a, and b. In addition to these six variables, we have six parameters,
which are β, T, C1, C2, S1, and S2. In this section, we discuss how we can quantify
these six parameters in practice. In doing so, we use a reverse approach. First,
we measure the values of p1, p2, q1, q2, a, and b. Then, based on our analyses in
the previous section, we calculate the values of the constants in our model.
AOSP
vendor
3rd-party
Vendor
Device
Version
and Build#
#apps #LOC #apps #LOC #apps #LOC #apps #LOC
HTC (vendor 1)
One X
4.0.4;
CL100532
280
19M
29
4.7M
190
7.3M
61
7.5M
Samsung (vendor 2) Galaxy S3 4.0.4;
19300UBALF5
185
17M
30
6.3M
119
5.6M
36
5.3M
Table 3. Origin of apps in two devices [18].
Location Quantiﬁcation: In order to quantify customization and map it
to a location, we need to quantify how diﬀerent two Android versions are in
terms of the pre-loaded apps. To do so, we can access the image of an Android
OS version, e.g., see [18] and [1], and investigate how many apps a vendor has
developed for a speciﬁc version.
To quantify customization, we use the results of Table 3 and calculate the
proportion of the code that was developed by a vendor. Note that in our model,
we assume that the locations are in the interval [0, 1]. First, we need to specify
the location of ZA and then select the location of other vendors. Here, we assume
that ZA = 0.5. In HTC One X (i.e., vendor 1), 7,354,468 LoC were developed
by the vendor and 7,550,704 LoC were from third-party apps. This means that
about 75.95% of lines of code were added by that vendor to the baseline AOSP
version. Here, we interpret this number as the level of diﬀerence between its
device and AOSP. In order to keep the value of a in the interval [0, 0.5], we let
a = ZA −(percentage/2). Therefore, we have a = ZA −(0.7595/2) = 0.1203.
In a similar way, for Samsung Galaxy 3 (i.e., vendor 2) 5,660,569 LOC were
developed by the vendor in addition to 5,334,152 LoC selected from third-party
apps, which is equal to 63.41% of the total number of LOC. In a similar way, we
let b = 1 −ZA −(0.6341/2) = 0.1830.
Quality: To quantify q1 and q2, we use the analysis reported in [18]. Ac-
cording to their analysis, the maximum number of vulnerabilities for a device
among these 10 devices is 40. Some of these vulnerabilities are the result of ven-
dor customization. For HTC One X, they have found 15 vulnerabilities, and 10
of these vulnerabilities are due to vendor customization. By dividing the num-
ber of vulnerabilities resulting from customization with the maximum number
of vulnerabilities, we get 0.25. In order to calculate security quality, we let
q1 = 1 −#Customization V ulnerabilities
Maximum#V ulnerabilities
= 0.75.
In a similar way, for Samsung Galaxy S3, they found 40 vulnerabilities, and 33
of these are the result of customization. Hence, we have q2 = 1 −33
40 = 0.1750.


## Page 11


Price: The prices of HTC One X and Samsung Galaxy S3 are equal to
e170 [9] and e190 [10], respectively. GSM Arena (http://www.gsmarena.com/)
groups both of these devices as group 4 out of 10 for their price. Here, we consider
p1 = p2 = 4.
Parameter Estimation: By assigning these six parameters into our model
analysis, we can calculate the six constants in our model. Here, we assume that
both vendors are completely rational and as result, they have chosen their cus-
tomization levels, prices, and security qualities according to our proposed model.
Therefore, we can calculate constant parameters in our model in a reverse way.
By inserting our quantiﬁed parameters, i.e., a, b, q1, q2, p1, and p2, into Equa-
tions 8 and 9, we have two equations and two variables, i.e., β and T. The
answer of this system of equations gives the values of β and T. Note that these
two equations are linear in T and β. Therefore, the resulting answer is unique.
To calculate the values of C1, C2, S1, and S2, we assume that the measured
values of q1, q2, a, b form a Nash equilibrium of our game. Since the vendors’
strategies are mutual best responses in a Nash equilibrium, q1, q2, a, b are so-
lutions to the corresponding best-response equations, i.e., Equations 34, 47, 40,
and 52, respectively. We have four variables and four equations. The solution of
this system of equations provides the values of S1, C1, S2, C2, which are unique.
Therefore, based on the measured values, we have β = 0.4362, T = 5.7414,
S1 = 0.6723, C1 = 1.4882, S2 = 4.1338, and C2 = 2.4875.
6
Fine Model and Analysis
Our previous analysis shows vendors’ poor practice of security issues arising
from customization. In particular, we have shown that vendors will not invest
in security issues of customization if the consumers do not take security into
account. Here, we propose a mechanism to force a vendor to invest in adequate
security quality. In doing so, we introduce a regulator whose role is to deﬁne the
policy that forces every vendor to invest in an adequate level of security. More
speciﬁcally, we propose a ﬁne function for a regulatory policy which takes as
input the vendor’s security quality and outputs the monetary value of the ﬁne
imposed on the vendor. In doing so, we deﬁne the following ﬁne function for
vendor i:
fi(qi) =
(
F
 qmin −qi

if qmin ≥qi
0
otherwise,
(12)
where F and qmin are constants deﬁned by the regulator. qmin is the minimum
acceptable level of security from the regulator’s point of view and the regulator
tries to force each vendor to satisfy at least this security level. F is a coeﬃcient
relating quality to monetary value and denotes the monetary value of ﬁne for
each unit of security violation from qmin for a vendor. The monetary value of
the ﬁne should be proportional to the market share, since a higher market share
of a vendor with security issues results in a higher number of consumers with
vulnerabilities. In our model, we multiplied fi by the market share of that vendor.


## Page 12


In this section, we show that under certain conditions, a regulator can force
a vendor to spend on security issues resulting from customization. Moreover, we
prove that the product’s price decreases as the vendor invests in the adequate
level of security imposed by the regulator, for the same value of customization
cost. More speciﬁcally, our analysis shows that under some conditions, the higher
the security quality imposed by the regulator is, the lower the product’s price is.
By imposing a ﬁne, the vendors’ utilities change to the following:
π1 = p1D1 −C1 (a −ZA)2 −S1q2
1 (a −ZA)2 −f1D1.
(13)
π2 = p2D2 −C2 (1 −b −ZA)2 −S2q2
2 (1 −b −ZA)2 −f2D2.
(14)
It is worth mentioning that the consumers’ utility does not change. Hence,
all of Equations 5, 6, and 7 are still valid for the case when there is a ﬁne. The
validity of these equations implies that the formulae for the vendors’ market
share is the same for both cases. However, the vendors’ equilibrium prices are
diﬀerent compared to the previous case.
Similar to the case without a ﬁne, here we have the same two stages with
the same ordering. The regulator’s goal is to force the vendors to invest in an
adequate security level. Hence, in our analysis, we focus on the case where the
regulator forces the vendor to invest in an adequate security quality level.
Theorem 2 characterizes both vendors’ prices in Nash equilibrium when the
regulator imposes a ﬁne.
Theorem 2 The Nash equilibrium in prices, which always exists, is
p∗
1 = β
3 (q1 −q2) + T (1 −a −b)

1 + a −b
3

+ 2f1
3
+ f2
3 ,
(15)
p∗
2 = β
3 (q2 −q1) + T (1 −a −b)

1 + b −a
3

+ 2f2
3
+ f1
3 .
(16)
This theorem is proved in Appendix B.4. By comparing the above two equa-
tions with Equations 8 and 9, we observe that the introduction of a ﬁne will
increase the product price of the vendors for ﬁxed locations and security level.
Na¨ıve Consumers: Based on Theorem 2, by letting β = 0, we can characterize
the price NE for na¨ıve consumers (which is shown in Appendix A.2). Lemma 2
introduces the suﬃcient conditions to force vendors to invest in adequate level
of security, when consumers do not take into account security.
Lemma 2 Both vendors invest in q∗
1 = q∗
2 = qmin, if the following conditions
are satisﬁed for the optimal locations of both vendors:
F 2 −18TS1 (1 −a −b) (a −ZA)2 ≥0,
(17)
F 2 −18TS2 (1 −a −b) (1 −b −ZA)2 ≥0,
(18)
3 + a −b −
Fqmin
T (1 −a −b) ≥0.
(19)


## Page 13


Proof of the above lemma is provided in Appendix B.6.
Lemma 3 calculates the location Nash equilibrium of both vendors consider-
ing that the regulator forces the vendors to invest in adequate levels of security.
Lemma 3 For given b, the vendor 1’s best response for location when the con-
sumers do not take into account security and conditions of Lemma 2 are satisﬁed,
is as follows:
• C1 + S1
 qmin2 ≤
T
12ZA : Vendor 1 diﬀerentiates its product the most, i.e.,
a∗(b) = 0.
• C1+S1
 qmin2 ≥
T
9ZA : The positive root of the following quadratic equation
is called a2. In this case, for vendor 1 we have a∗(b) = min{a2, ZA}.
−3Ta2 + a
 
2Tb −10T −36

C1 + S1

qmin2!
+ T

b2 −2b −3

+ 36

C1 + S1

qmin2
ZA = 0
(20)
•
T
12ZA < C1+S1
 qmin2 <
T
9ZA and b ≤min{1−
r
4 −
36

C1+S1(qmin)
2
T
ZA, ZA}:
Vendor 1 chooses its location as a∗(b) = min{a2, ZA}.
•
T
12ZA < C1 + S1
 qmin2 <
T
9ZA and 1 −
r
4 −
36

C1+S1(qmin)
2
T
ZA ≤ZA
and 1−
r
4 −
36

C1+S1(qmin)
2
T
ZA ≤b ≤ZA: Vendor 1 diﬀerentiates its product
the most, i.e., a∗(b) = 0.
By changing C1 to C2, S1 to S2, a to b, and ZA to (1 −ZA), in the above
lemma, we can derive the same results for vendor 2. Proof of Lemma 3 is provided
in Appendix B.7.
Comparing this lemma with Lemma 4 (Appendix A.1), we see maximal dif-
ferentiation occurs when the cost of customization is lower than when there is
no ﬁne, since a vendor’s cost is aﬀected by both the costs of customization and
security quality. Further, according to Equation 20, the location NE depends
on qmin rather than F. However, both F and qmin have the eﬀect to satisfy
the conditions for forcing a vendor to invest in adequate level of security, i.e.,
Lemma 2.
7
Numerical Illustration
In this section, we evaluate our ﬁndings numerically. First, we evaluate the case
where there are no ﬁnes and the consumers are na¨ıve. Second, we evaluate the
case in which consumers are na¨ıve, but a regulator imposes ﬁnes. Then, we
compare the equilibrium prices and locations in the absence and in the presence
of the regulatory ﬁne. Interestingly, we observe that the products’ prices (of
both vendors) decrease in the presence of ﬁnes, and both vendors invest in the


## Page 14


adequate level of security qmin set by the regulator. Finally, we evaluate the case
in which there are no ﬁnes but the consumers take into account security quality.
Figure 2 shows both vendors’ equilibrium locations for various values of cus-
tomization costs C1 and C2. To ﬁnd Nash equilibrium, we use Lemma 4 and
its counterpart for vendor 2 to calculate each vendor’s best-response location.
Then, considering that NE is mutual best response, the intersection of these two
best responses gives the equilibrium locations of both vendors. Once we have the
equilibrium locations, we can easily calculate the equilibrium prices according to
Lemma 1. Based on Figure 2, the higher the cost of customization (e.g., C1) is,
the lower a vendor’s diﬀerentiation from AOSP baseline model is (e.g., the higher
the value of a∗is). Note that in Figure 2(b) for C2 = 0, vendor 2 chooses the
maximum level of customization (i.e., b∗= 0) regardless of the vendor 1’s cus-
tomization level. According to Lemma 4 and its counterpart for vendor 2, when
the cost of customization is lower than a threshold (i.e., when C2 ≤
T
12(1−ZA)),
vendor 2 chooses the maximum level of customization. As we see in Figure 2(c),
the customization level of vendor 1, i.e., a∗, changes only a little with changes in
vendor 2’s customization cost. For example, when the customization cost of ven-
dor 2 increases, vendor 2 chooses lower level of customization (i.e., higher value
of b∗), while vendor 1 increases its customization level (i.e., lowers the value of
a∗) a little compared to its opponent. However, as we observe in Figures 2(c)
and 2(d), the prices of both vendors change more signiﬁcantly compared to their
locations with respect to changes in customization costs. Based on Lemma 1 (see
Equation 21), a decrease in the customization level of vendor 2 lowers the values
of both (1 −a −b) and

1 + a−b
3

. As a result, vendors enter price competition
and decrease their prices, which is shown in Figures 2(c) and 2(d).
In Figure 3, we examine the eﬀect of regulation on location, price, and secu-
rity quality for various values of C1 and C2. In our evaluation, in the presence of
a regulator, the conditions of Lemma 2 are satisﬁed. As a result, both vendors
invest in qmin set by the regulator. Similar to the case without any ﬁne, the
higher the customization cost (e.g., C1) is, the lower the diﬀerentiation from
the baseline AOSP is (e.g., the higher the value of a∗is). Similarly, we again
observe little changes in a vendor’s location in response to changes in its oppo-
nent’s customization cost and the customization level. Further, the equilibrium
prices of both vendors are decreased by an increase in customization costs, since
both of them choose lower levels of customization and enter a price competition.
Note that even in the presence of ﬁnes, vendor 2 chooses the maximum level of
customization (i.e., b∗= 0) when C2 = 0, considering that its cost of security
is proportional to its level of customization and S2 > S1. The reason for this is
that vendor 2 is reluctant to enter a price competition.
In Figure 4, we compare the equilibria in the presence and the absence of
a regulatory ﬁne, when consumers do not take into account security. Based on
Figure 4(c), vendor 1 chooses a lower level of customization when a ﬁne exists.
Figure 4(d) shows that vendor 2 chooses the same location in both cases as we
discussed earlier when C2 = 0. For C2 = 3, vendor 2 chooses a lower level of
customization (i.e., higher value of b∗) compared to the case when there is no ﬁne.


## Page 15


0
1
2
3
4
5
6
7
C1
0
0.05
0.1
0.15
0.2
0.25
0.3
a
Vendor 1 Customization Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
(a) a∗
0
1
2
3
4
5
6
7
C1
0
0.05
0.1
0.15
0.2
0.25
b
Vendor 2 Customization Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
(b) b∗
0
1
2
3
4
5
6
7
C1
3
4
5
6
7
8
p1
Vendor 1 Price Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
C2=6
(c) p∗
1
0
1
2
3
4
5
6
7
C1
3
4
5
6
7
8
p2
Vendor 2 Price Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
C2=6
(d) p∗
2
Fig. 2. Equilibrium locations and prices of both vendor 1 and vendor 2 when consumers
do not take into account security, there is no ﬁne, and T = 8.
Consequently, the prices of both vendors are lower for higher customization costs
due to the fact that both vendors are moving closer to the AOSP baseline model.
Moreover, the existence of regulation and the ﬁne leads to higher values of a∗and
b∗(i.e., lower customization levels) for the same customization costs compared to
the case without a ﬁne, since each vendor tries to maximize its utility by avoiding
regulatory ﬁne through investing in the minimum level of security quality qmin.
Therefore, each vendor has to pay both the cost of customization as well as the
cost of security quality resulting from customization. To decrease these costs,
each vendor chooses a lower level of customization. Further, choosing higher
values of a∗and b∗(i.e., lower customization level) leads to lower prices for both
vendors. Therefore, the existence of a regulatory ﬁne leads to more secure
products at lower prices when consumers do not care about security.
To ﬁnd equilibrium locations and security qualities when consumers take into
account security but there is no ﬁne, we calculate each vendor’s best-response se-
curity quality and location for its opponent’s given location and security quality.
Then, the Nash equilibrium is the intersection of these best responses. Table 4
shows the equilibrium for various values of C1, where T = 1.6, β = 0.6, C2 = 1.3,
Q = 1, and S1 = S2 = 1. In this case, due to the consumers’ security consid-


## Page 16


0
1
2
3
4
5
6
7
C1
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
a
Vendor 1 Customization Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
(a) a∗
0
1
2
3
4
5
6
7
C1
0
0.05
0.1
0.15
0.2
0.25
b
Vendor 2 Customization Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
(b) b∗
0
1
2
3
4
5
6
7
C1
3
4
5
6
7
8
a
Vendor 1 Price Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
(c) p∗
1
0
1
2
3
4
5
6
7
C1
3
4
5
6
7
8
p2
Vendor 2 Price Nash Equilibrium
C2=0
C2=1.5
C2=3
C2=4.5
(d) p∗
2
Fig. 3. Equilibrium locations and prices for various values of C1 and C2. Here, con-
sumers are na¨ıve, but there is a regulatory ﬁne, and T = 8, S1 = 0.602, S2 = 1.54,
F = 10, and qmin = 0.4. For these values of C1 and C2 and choices of a and b, both
vendors invest in qmin set by the regulator.
eration, both vendors invest in security. For C1 = 0, vendor 1 maximizes its
diﬀerentiation from baseline AOSP. Because of the consumers’ security aware-
ness, vendor 1 invests in security, but at a lower level than Q. It is interesting
to see that vendor 2 does not diﬀerentiate its product from the baseline AOSP
version due to maximal diﬀerentiation of vendor 1 and consequently, it does not
have any security issues resulting from customization (i.e., q∗
2 = Q = 1).
It is noteworthy that both vendors invest in the maximum level of security
when both vendors’ customization costs are greater than zero. This observation
shows that if all consumers are capable of measuring security quality and it is one
of the factors aﬀecting their product choice, then vendors will invest in security.
Similar to the case where consumers do not take into account security, the higher
the customization cost is, the lower the customization level is. In other words,
increasing C1 results in higher values of a∗. Moreover, changing the value of C1,
while C2 is ﬁxed, results in little changes in b∗.


## Page 17


0
1
2
3
4
5
6
7
C1
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
a
Vendor 1 Customization Nash Equilibrium
C2=0, No Fine
C2=3, No Fine
C2=0, Fine
C2=3, Fine
(a) a∗
0
1
2
3
4
5
6
7
C1
0
0.05
0.1
0.15
b
Vendor 2 Customization Nash Equilibrium
C2=0, No Fine
C2=3, No Fine
C2=0, Fine
C2=3, Fine
(b) b∗
0
1
2
3
4
5
6
7
C1
4.5
5
5.5
6
6.5
7
7.5
8
p1
Vendor 1 Price Nash Equilibrium
C2=0, No Fine
C2=0, Fine
C2=3, No Fine
C2=3, Fine
(c) p∗
1
0
1
2
3
4
5
6
7
C1
4
5
6
7
8
p2
Vendor 2 Price Nash Equilibrium
C2=0, No Fine
C2=0, Fine
C2=3, No Fine
C2=3, Fine
(d) p∗
2
Fig. 4. Comparison between the presence and the absence of a ﬁne for na¨ıve consumers.
We have T = 8, S1 = 0.602, S2 = 1.54, F = 10, and qmin = 0.4.
8
Conclusion
Our model shows that vendors have to invest in security quality for security-
conscious consumers. Further, for na¨ıve consumers, our proposed model captures
the fact that vendors underinvest in security. To incentivize vendors to invest
in security for na¨ıve consumers, a regulator may assign a ﬁne to those vendors
that do not uphold a desired level of security, which is a well-motivated scenario
given Android-related FTC actions [8].
We show that the imposed ﬁne structure achieves the expected eﬀect in
addition to changes in the competitive landscape. First, the price of the product
decreases for the same cost of customization compared to the case without any
ﬁne. Second, a higher level of security quality imposed by the regulator leads to a
lower product price, if certain conditions are satisﬁed. Our ﬁndings suggest that
requiring higher baseline levels of security investments (as triggered by recent
FTC actions [8]) does not impose higher product prices on na¨ıve consumers,
which is important from a technology policy perspective. Moreover, increasing
consumers’ attention about security is substantiated by our analysis as a positive
and meaningful factor to address challenges related to informational market
power and neglected security eﬀorts.


## Page 18


C1
a∗
q∗
1
b∗
q∗
2
0
0
0.2612
0.5
1
0.3684 0.2888
1
0.3639 1
0.7368 0.3195
1
0.3638 1
1.1053 0.3452
1
0.3637 1
1.4737 0.3677
1
0.3636 1
Table 4. The vendors’ equilibrium prices and security qualities for various values of
C1. Here, we have S1 = S2 = 1, T = 1.6, β = 0.6, Q = 1, and C2 = 1.3.
Acknowledgments: We thank the anonymous reviewers for their com-
ments. The research activities of Jens Grossklags are supported by the German
Institute for Trust and Safety on the Internet (DIVSI). Aron Laszka’s work was
supported in part by the National Science Foundation (CNS-1238959) and the
Air Force Research Laboratory (FA 8750-14-2-0180).
References
1. Y. Aafer, X. Zhang, and W. Du, Harvesting inconsistent security conﬁgurations in
custom android roms via diﬀerential analysis, Usenix Security, 2016.
2. Android market share, Android market share, Available at: http://www.idc.com/
prodserv/smartphone-os-market-share.jsp.
3. H. Beales, R. Craswell, and S. C. Salop, The eﬃcient regulation of consumer in-
formation, The Journal of Law and Economics 24 (1981), no. 3, 491–539.
4. H. Cavusoglu and S. Raghunathan, Selecting a customization strategy under compe-
tition: mass customization, targeted mass customization, and product proliferation,
IEEE Transactions on Engineering Management 54 (2007), no. 1, 12–28.
5. C. d’Aspremont, J. Gabszewicz, and J.-F. Thisse, On Hotelling’s “Stability in com-
petition”, Econometrica 47 (1979), no. 5, 1145–1150.
6. R. Dewan, B. Jing, and A. Seidmann, Product customization and price competition
on the internet, Management Science 49 (2003), no. 8, 1055–1070.
7. Federal Trade Commission, FTC to study mobile device industry’s security update
practices, Available at: https://www.ftc.gov/news-events/press-releases/
2016/05/ftc-study-mobile-device-industrys-security-update-practices.
8.
,
HTC
America
settles
FTC
charges
it
failed
to
se-
cure
Millions
of
mobile
devices
shipped
to
consumers,
Available
at:
https://www.ftc.gov/news-events/press-releases/2013/02/
htc-america-settles-ftc-charges-it-failed-secure-millions-mobile.
9. GSMarena, HTC One X price, Available at: http://www.gsmarena.com/htc_one_
x-4320.php.
10.
, Samsung Galaxy S3 price, Available at: http://www.gsmarena.com/
samsung_i9300_galaxy_s_iii-4238.php.
11. D. Han, C. Zhang, X. Fan, A. Hindle, K. Wong, and E. Stroulia, Understanding
Android fragmentation with topic analysis of vendor-speciﬁc bugs, 19th Working
Conference on Reverse Engineering, 2012, pp. 83–92.
12. H. Hotelling, Stability in competition, The Economic Journal 39 (1929), no. 153,
41–57.
13. F. Kardes, Omission neglect, Encyclopedia of Social Psychology (R. Baumeister
and K. Vohs, eds.), vol. 1, Sage, 2007.


## Page 19


14. P. Mutchler, Y. Safaei, A. Doup´e, and J. Mitchell, Target fragmentation in Android
apps, IEEE Security and Privacy Workshops (SPW), 2016, pp. 204–213.
15. Singh,
S.,
An
analysis
of
Android
fragmentation,
Available
at:
http:
//www.tech-thoughts.net/2012/03/analysis-of-android-fragmentation.
html#.WA_OxoMrKUk.
16. D. Thomas, A. Beresford, and A. Rice, Security metrics for the Android ecosystem,
ACM CCS Workshop on Security and Privacy in Smartphones and Mobile Devices,
2015, pp. 87–98.
17. J. Tirole, The theory of industrial organization, MIT Press, 1988.
18. L. Wu, M. Grace, Y. Zhou, C. Wu, and X. Jiang, The impact of vendor customiza-
tions on Android security, ACM Conference on Computer & Communications Se-
curity, 2013, pp. 623–634.
19. X. Zhou, Y. Lee, N. Zhang, M. Naveed, and X. Wang, The peril of fragmentation:
Security hazards in Android device driver customizations, IEEE Symposium on
Security and Privacy, 2014, pp. 409–423.
A
Consumers Without Security Consideration
A.1
Consumers Without Security Consideration
In this section, we consider a special case of our model, where the consumers
do not take into account security. This means that, we have β = 0 and the
derivations to calculate the price and quality Nash Equilibrium follow directly.
The following two lemmas state their values.
Proposition 1 The unique price Nash equilibrium, which always exists, is
p∗
1 = T (1 −a −b)

1 + a −b
3

,
(21)
p∗
2 = T (1 −a −b)

1 + b −a
3

.
(22)
Proof. Proposition 1 can be derived by assigning β = 0 in Theorem 1. ⊓⊔
The following corollary represents the vendors’ lack of incentives to invest in
security-related eﬀorts when consumers cannot measure security quality.
Corollary 1 In any Nash equilibrium, both vendors invest zero in security, i.e.,
q∗
1 = q∗
2 = 0.
Proof. Note that when β = 0, the market share of each vendor does not
depend on security quality. In order to calculate q1, we have:
dπ1
dq1
= −2q1S1 (a −ZA)2 ,
(23)
which is decreasing for non-negative values of q1. Therefore, we have q∗
1 = 0.
In a similar way, for vendor 2 we have q∗
2 = 0. ⊓⊔
The following lemma represents vendor 1’s level of customization best re-
sponse, i.e., a, given the customization level of its opponent, i.e., b.


## Page 20


Lemma 4 For given b, vendor 1’s best response for location when the consumers
do not take security into account is as follows:
• C1 ≤
T
12ZA : Vendor 1 diﬀerentiates its product as much as possible, i.e.,
a∗(b) = 0.
• C1 ≥
T
9ZA : The positive root of the following quadratic equation in a is
called a2. In this case, for vendor 1 we have a∗(b) = min{a2, ZA}.
−3Ta2 + a (2Tb −10T −36C1) + T

b2 −2b −3

+ 36C1ZA = 0
(24)
•
T
12ZA < C1 <
T
9ZA and 0 ≤b ≤min{ZA, 1 −
q
4 −36C1
T
ZA}: Vendor 1
chooses its location as a∗(b) = min{a2, ZA}.
•
T
12ZA < C1 <
T
9ZA and 1 −
q
4 −36C1
T
ZA ≤ZA and 1 −
q
4 −36C1
T
ZA ≤
b ≤ZA: Vendor 1 diﬀerentiates its product the most, i.e., a∗(b) = 0.
The above lemma represents that if the cost of customization is lower than
a threshold, i.e., C1 ≤
T
12ZA , vendor 1 will diﬀerentiate its product the most
regardless of its opponent’s level of customization, i.e., a∗= 0. The reason is
that when the cost of customization is low, the vendor chooses a location in
order to increase the price, see Equation 21, and to prevent price competition.
By changing C1 to C2, S1 to S2, a to b, and ZA to (1 −ZA), in the above lemma,
we can derive the same results for vendor 2.
Proof of Lemma 4 is provided in Appendix B.5.
Proposition 2 When consumers do not take security into account, C1 ≤
T
12ZA ,
and C2 ≤
T
12(1−ZA) location Nash equilibrium is a∗= b∗= 0, i.e., maximal
diﬀerentiation.
Proof. The Nash equilibrium is the mutually best response. Based on Lemma 4
and its corresponding vendor’s 2 best response, for these cost of customizations,
both vendors’ best responses are equal to zero. ⊓⊔
For other values of C1 and C2, we calculate Nash equilibria numerically.
A.2
Price Equilibrium for Na¨ıve Consumers in the Presence of Fine
Corollary 2 The Nash equilibrium in prices, which always exists, is
p∗
1 = T (1 −a −b)

1 + a −b
3

+ 2f1
3
+ f2
3 ,
(25)
p∗
2 = T (1 −a −b)

1 + b −a
3

+ 2f2
3
+ f1
3 .
(26)


## Page 21


B
Proof
B.1
Price Nash Equilibrium without Fine
First, we take the partial derivative with respect to price for vendor 1 and have:
∂π1
∂p1
= D1 (a, b, p1, p2) + p1
∂D1 (a, b, p1, p2)
∂p1
=
p2 −p1
2T (1 −a −b) + a + 1 −a −b
2
+
β (q1 −q2)
2T (1 −a −b) + p1

−1
2T (1 −a −b)

,
(27)
the above equation is linear with respect to p1 and the coeﬃcient of p1 is
negative. To ﬁnd the utility-maximizing price, we set the above value equal to
zero, which gives us the following:
∂π1
∂p1
= 0
⇒
pcrit
1
= p2
2 + T
2 (1 −a −b) (1 + a −b) + β (q1 −q2)
2
.
(28)
Note that π1 is increasing in [0, pcrit
1
] and decreasing in [pcrit
1
, ∞], since the
coeﬃcient of p1 is negative in Equation 27. Therefore, vendor 1’s utility is max-
imized at p∗
1 = pcrit
1
. The value of p∗
1 depends on its location, its rival location,
security quality diﬀerences of two vendors, and vendor 2’s product price.
In a similar way, for vendor 2 we have:
∂π2
∂p2
= D2 (a, b, p1, p2)+p2
∂D2 (a, b, p1, p2)
∂p2
=
p1 −p2
2T (1 −a −b) +b+ 1 −a −b
2
+
β (q2 −q1)
2T (1 −a −b) + p2

−1
2T (1 −a −b)

.
(29)
This is linear in p2 and its coeﬃcient is negative. The critical point is:
∂π2
∂p2
= 0
⇒
pcrit
2
= p1
2 + T
2 (1 −a −b) (1 −a + b) + β (q2 −q1)
2T
.
(30)
It is straightforward to see that π2 is increasing in [0, pcrit
2
] and decreasing in
[pcrit
2
, ∞]. Therefore, pcrit
2
is local maximum.
By combining Equations 28 and 30, we can derive the Nash equilibrium in
prices which always exists. ⊓⊔
B.2
Optimization Problem with No Fine
First, we calculate best-response q1 by taking the derivative of Equation 3 with
respect to it and we have:
dπ1
dq1
= ∂π1
∂q1
+ ∂π1
∂p1
∂p1
∂q1
+ ∂π1
∂p2
∂p2
∂q1
.
(31)


## Page 22


Note that in the above equation, we are going to maximize π1 with respect
to q1 given that Equation 8 is satisﬁed. According to the envelope theorem,
vendor 1 maximizes its utility with respect to the price in the second stage,
where ∂π1
∂p1 = 0. Therefore, we have:
dπ1
dq1
= ∂π1
∂q1
+ ∂π1
∂p2
∂p2
∂q1
⇒
dπ1
dq1
= −2S1q1 (a −ZA)2 + p∗
1
∂D1
∂q1
+ p∗
1
∂D1
∂p2
∂p∗
2
∂q1
.
(32)
By using Equations 3, 8, and 9, we have:
dπ1
dq1
= −2S1q1 (a −ZA)2 + p∗
1

β
2T (1 −a −b)

−p∗
1

β
6T (1 −a −b)

= −2S1q1 (a −ZA)2 + p∗
1

β
3T (1 −a −b)

.
(33)
According to Equation 8, p∗
1 is also function of q1. By incorporating Equa-
tion 8 into the above equation, we have:
dπ1
dq1
= q1
 
−2S1 (a −ZA)2 +
β2
9T (1 −a −b)
!
+β
9

3 + a −b −
βq2
T (1 −a −b)

.
(34)
The above equation is linear in terms of q1. To make our analysis simpler,
we deﬁne the following parameters:
A1 = −2S1 (a −ZA)2+
β2
9T (1 −a −b), B1 = β
9

3 + a −b −
βq2
T (1 −a −b)

.
(35)
According to the sign of these two parameters, we have:
optq1 (a, b, q2) =











Q
if A1 ≥0 , B1 ≥0
min{ −B1
A1 , Q}
if A1 < 0 , B1 ≥0
arg maxq1∈{¯q1,Q} π1
if A1 ≥0 , B1 < 0
¯q1
if A1 < 0 , B1 < 0.
(36)
Where ¯q1 = q2 −T
β (1 −a −b) (3 + a −b). The reasons behind the above
formula are as follows:
– A1 ≥0 , B1 ≥0: In this case, π1 is increasing for any values q1 ≥0. Because
of our constraint, π1 is maximized at Q.


## Page 23


– A1 < 0 , B1 ≥0: π1 is increasing in [0, −B1
A1 ] and decreasing in [ −B1
A1 , ∞].
– A1 ≥0 , B1 < 0: π1 is decreasing in [0, −B1
A1 ] and increasing in [ −B1
A1 , ∞]. In
this case, two candidate points are 0 and Q. Note that when B1 < 0, q1 = 0
gives negative p1 which is not acceptable. Hence, vendor 1 chooses the lowest
value of q1 that gives non-negative p1. This consideration gives ¯q1 as one the
candidate points.
– A1 < 0 , B1 < 0: π1 is decreasing for all non-negative values of q1, but q1 = 0
gives negative p1. Similar to the previous case, π1 is maximized at ¯q1.
In a similar way for vendor 2 we have:
dπ2
dq2
= ∂π2
∂q2
+ ∂π2
∂p2
∂p2
∂q2
+ ∂π2
∂p1
∂p1
∂q2
.
(37)
According to the envelope theorem, vendor 2 maximizes its utility with re-
spect to the price in the second stage where ∂π2
∂p2 = 0. Therefore, we have:
dπ2
dq2
= ∂π2
∂q2
+ ∂π2
∂p1
∂p1
∂q2
⇒
dπ2
dq2
= −2S2q2 (1 −b −ZA)2 + p∗
2
∂D2
∂q2
+ p∗
2
∂D2
∂p1
∂p∗
1
∂q2
.
(38)
By using Equations 4, 8, and 9, we have:
dπ2
dq2
= −2S2q2 (1 −b −ZA)2 + p∗
2

β
2T (1 −a −b)

−p∗
2

β
6T (1 −a −b)

= −2S2q2 (1 −b −ZA)2 + p∗
2

β
3T (1 −a −b)

.
(39)
According to Equation 9, p∗
2 is also function of q2. By incorporating Equa-
tion 9 into the above equation, we have:
dπ2
dq2
= q2
 
−2S2 (1 −b −ZA)2 +
β2
9T (1 −a −b)
!
+ β
9

3 −a + b −
βq1
T (1 −a −b)

.
(40)
The above equation is linear in terms of q2. To make our analysis simpler,
we deﬁne the following parameters:
A2 = −2S2 (1 −b −ZA)2 +
β2
9T (1 −a −b),


## Page 24


B2 = β
9

3 −a + b −
βq1
T (1 −a −b)

.
(41)
According to the sign of these two parameters, we have:
optq2 (a, b, q1) =











Q
if A2 ≥0 , B2 ≥0
min{ −B2
A2 , Q}
if A2 < 0 , B2 ≥0
arg maxq2∈{¯q2,Q} π2
if A2 ≥0 , B2 < 0
¯q2
if A2 < 0 , B2 < 0.
(42)
Where ¯q2 = q1 −T
β (1 −a −b) (3 −a + b).
In order to calculate the optimal location of each player, we take the deriva-
tive with respect to location. First, we start with vendor 1 and we have:
dπ1
da = ∂π1
∂p1
∂p1
∂a + ∂π1
∂a + ∂π1
∂p2
∂p2
∂a .
(43)
Note that in the above equation, we are going to maximize π1 given that
Equation 8 is satisﬁed. According to the envelope theorem, vendor 1 maximizes
its utility with respect to the price in the second period where ∂π1
∂p1 = 0. Therefore,
we have:
∂π1
∂a = ∂π1
∂p2
∂p∗
2
∂a + ∂π1
∂a = −2C1 (a −ZA)
−2S1q2
1 (a −ZA) + p∗
1
∂D1
∂a + ∂D1
∂p2
∂p∗
2
∂a

.
(44)
By using Equations 6, 8, and 9, we get:
∂D1
∂a
= 1
2 + β (q1 −q2) + p∗
1 −p∗
2
2T (1 −a −b)2
=
3 −5a −b
6 (1 −a −b) +
β (q1 −q2)
6T (1 −a −b)2 .
(45)
The ﬁrst term in the above is called the demand eﬀect, i.e., the direct eﬀect
of a on D1 and π1. Note that this value can be either positive or negative based
on the values of a and b. Moreover, by using Equations 6, and 9, we have:
∂D1
∂p2
∂p∗
2
∂a
=

1
2T (1 −a −b)
  
T
−4 + 2a
3
!
=
a −2
3 (1 −a −b),
(46)
which is called the strategic eﬀect. It shows the indirect eﬀect through the change
in ﬁrm 2’s price on D1 and π1. Note that the above term is negative. By using
Equations 44, 45 and 46, we have:
dπ1
da = p∗
1
 
−1 −3a −b
6 (1 −a −b) +
β (q1 −q2)
6T (1 −a −b)2
!
−2C1 (a −ZA) −2S1q2
1 (a −ZA) .
(47)


## Page 25


Note that we restrict the values of a to be in the interval 0 ≤a ≤ZA. By
setting the above equation to zero, we ﬁnd the corresponding critical points,
and they also should satisfy condition 0 ≤a ≤ZA. In addition to these points,
we should also check the boundary points, i.e., 0 and ZA. As a result, we have
¯a = {0, ZA, a|0 ≤a ≤ZA, dπ1
da = 0}. This set introduces the potential solutions
for vendor’s 1 locations. Note that ¯a and optq1 (a, b, q2) give the potential best
responses. The one that gives the highest utility provides vendor 1’s best response
that is function of b and q2.
In a similar way, for vendor 2 we have:
dπ2
db = ∂π2
∂p2
∂p2
∂b + ∂π2
∂b + ∂π2
∂p1
∂p1
∂b .
(48)
According to the envelope theorem and ∂π2
∂p2 = 0 in step 2, we have:
dπ2
db = ∂π2
∂b + ∂π2
∂p1
∂p∗
1
∂b = 2C2 (1 −b −ZA)
+ 2S2q2
2 (1 −b −ZA) + p∗
2
∂D2
∂b + ∂D2
∂p1
∂p∗
1
∂b

.
(49)
By using Equations 7, 8, and 9 the demand eﬀect of vendor 2 is:
∂D2
∂b
= 1
2 + p∗
1 −p∗
2 + β (q2 −q1)
2T (1 −a −b)2
=
3 −5b −a
6 (1 −a −b) +
β (q2 −q1)
6T (1 −a −b)2 .
(50)
The strategic eﬀect of vendor 2 based on Equations 7 and 8 is equal to:
∂D2
∂p1
∂p∗
1
∂b
=

1
2T (1 −a −b)
  
T
−4 + 2b
3
!
=
b −2
3 (1 −a −b).
(51)
By using the demand eﬀect and the strategic eﬀect of vendor 2, we have:
dπ2
db = p∗
2
 
−1 −3b −a
6 (1 −a −b) +
β (q2 −q1)
6T (1 −a −b)2
!
+ 2C2 (1 −b −ZA) + 2S2q2
2 (1 −b −ZA) .
(52)
Note that we restrict the values of b to be in interval 0 ≤b ≤ZA. By
setting the above equation to zero, we ﬁnd the corresponding critical points,
and they also should satisfy condition 0 ≤b ≤ZA. In addition to these points,
we should also check the boundary points, i.e., 0 and ZA. As a result, we have
¯b = {0, ZA, b|0 ≤b ≤ZA, dπ2
db = 0}. This set introduces the potential solutions
for vendor’s 2 locations. Note that ¯b and optq2 (a, b, q1) give the potential best
responses. The one that gives the highest utility provides vendor 2’s best response
that is function of a and q1.


## Page 26


B.3
Proof of Lemma 1
According to a vendor’s security quality best responses, e.g., Equation 36, best
response security equality is not equal to zero unless B1 is equal to zero and A1 is
negative. If q2 = 0, B1 is positive regardless of the location choices. Therefore, we
have optq1 (a, b, q2) = Q or optq1 (a, b, q2) = min

−B1
A1 , Q

which are not equal
to zero. q1 = q2 = 0 is NE if B1 = B2 = 0 and A1, A2 < 0 are both satisﬁed.
B1 = B2 = 0 never happens unless 1−a −b = 0 which means that both vendors
are at the same location. If both vendors are at the same location as ZA, this
means that both of them have the quality Q. If they are at a diﬀerent location
than ZA, the utility of customization is negative which is not acceptable for both
vendors. Therefore, q1 = q2 = 0 is not NE. ⊓⊔
B.4
Price Nash Equilibrium with Fine
By taking the partial derivative with respect to price of ﬁrm 1, we have:
∂π1
∂p1
= D1 + (p1 −f1) ∂D1
∂p1
=
p2 −p1
2T (1 −a −b) + a
+ 1 −a −b
2
+
β (q1 −q2)
2T (1 −a −b) + (p1 −f1)

−1
2T (1 −a −b)

.
(53)
The above equation is linear in p1 and its coeﬃcient is negative. Setting the
above value to zero gives the following:
∂π1
∂p1
= 0 ⇒pcrit
1
= p2
2 + T
2 (1 −a −b) (1 + a −b) + β
2 (q1 −q2) + f1
2 .
(54)
Assuming that pcrit
1
≥0, π1 is increasing in [0, pcrit
1
] and decreasing in
[pcrit
1
, ∞]. Therefore, pcrit
1
is maximum.
In a similar way, for vendor 2 we have:
∂π2
∂p2
= D2 + (p2 −f2) ∂D2
∂p2
=
p1 −p2
2T (1 −a −b) + b
+ 1 −a −b
2
+
β (q2 −q1)
2T (1 −a −b) + (p2 −f2)

−1
2T (1 −a −b)

,
(55)
which is linear in p2 and its coeﬃcient is negative. By setting the above
equation to zero, we have:
∂π2
∂p2
= 0 ⇒pcrit
2
= p1
2 + T
2 (1 −a −b) (1 −a + b)
+ β
2 (q2 −q1) + f2
2 .
(56)


## Page 27


Assuming that pcrit
2
≥0,π2 is increasing in [0, pcrit
G ] and decreasing in [pcrit
G , ∞].
Hence, maximum is pcrit
2
.
Solving both Equations 54 and 56 provides the Nash equilibrium in price
being represented in Theorem 2. Note that this Nash equilibrium always exists.
⊓⊔
B.5
Proof of Lemma 4
In order to calculate a and b, based on Equations 47 and 52, we have:
dπ1
da = p∗
1
 −1 −3a −b
6 (1 −a −b)

−2C1 (a −ZA) ,
(57)
dπ2
db = p∗
2
 −1 −3b −a
6 (1 −a −b)

+ 2C2 (1 −b −ZA) ,
(58)
where p∗
1 and p∗
2 are equal to Equations 21 and 22, respectively. By assigning
p∗
1 and p∗
2 into the above equations, we have:
dπ1
da = 1
18(−3Ta2+a (2Tb −10T −36C1)+T

b2 −2b −3

+36C1ZA),
(59)
which is quadratic in terms of a.
dπ2
db = 1
18(−3Tb2 + b (2Ta −10T −36C2)
+ T

a2 −2a −3

+ 36C2(1 −ZA),
(60)
which is quadratic in terms of b.
In a quadratic function like Ax2 + Bx + C = 0, if ∆= B2 −4AC ≥0, that
equation has two roots, which we call x1 and x2. Further, we have x1 +x2 = −B
A
and x1x2 = C
A. If ∆< 0, the quadratic function does not reach zero and its sign
is the same as the sign of A.
By setting Equation 59, i.e., dπ1
da = 0, we have a quadratic function in a.
In this equation, we have A = −3T < 0, B = 2Tb −10T −36C1 < 0, and
C = T
 b2 −2b −3

+ 36C1ZA. If C ≤0, ∆can be both positive or negative. If
∆≤0, this means that dπ1
da is negative for any values of a. In other words, π1 is
decreasing in terms of a. Therefore, we have a∗= 0. If ∆> 0, this means that
dπ1
da = 0 has two roots, i.e., a1 and a2. Moreover, we have a1a2 = C
A > 0 and
a1 + a2 = −B
A
< 0. This means that both a1 and a2 are negative and for any
non-negative value of a, dπ1
da is negative. This gives that a∗= 0, In summary,
when C ≤0, we have a∗= 0.
For the case where C > 0, we have ∆> 0 and as result dπ1
da = 0 has two roots,
i.e., a1 and a2. One of them is negative, a1 < 0, and the other one is positive,
a2 > 0. Because, we have a1a2 = C
A < 0 and a1 + a2 = −B
A
< 0. Hence, π1 is


## Page 28


increasing in [0, a2]. Note that we have assumed that a ∈[0, ZA]. Therefore, we
have a∗= min{a2, ZA}. In summary, we have:
a∗=
(
0
if T
 b2 −2b −3

+ 36C1ZA ≤0
min{a2, ZA}
if T
 b2 −2b −3

+ 36C1ZA > 0.
The condition of the above equation is quadratic in b. Let’s call the root of
this quadratic function (if it exists), i.e., T
 b2 −2b −3

+ 36C1ZA = 0, as ¯b1
and ¯b2, where ¯b1 ≤¯b2. By doing a similar analysis, we can rewrite a∗as follows:
a∗=





















0
if C1 ≤
T
12ZA
min{a2, ZA}
if C1 ≥
T
9ZA
min{a2, ZA}
if
T
12ZA < C1 <
T
9ZA
& 0 ≤b ≤min{ZA,¯b1}
0
if
T
12ZA < C1 <
T
9ZA
& ¯b1 ≤ZA & ¯b1 ≤b ≤ZA,
where ¯b1 = 1 −
q
4 −36C1
T
ZA.
In a similar way, for vendor 2 we have:
b∗=
(
0
if T
 a2 −2a −3

+ 36C2(1 −ZA) ≤0
min{b2, ZA}
if T
 a2 −2a −3

+ 36C2(1 −ZA) > 0,
where b1 and b2 are two roots of dπ2
db = 0 in which b1 ≤b2. Note that the
condition of the above equation is quadratic in terms of a. Similar to vendor 1,
we have:
b∗=





















0
if C2 ≤
T
12(1−ZA)
min{b2, ZA}
if C2 ≥
T
9(1−ZA)
min{b2, ZA}
if
T
12(1−ZA) < C2 <
T
9(1−ZA)
& 0 ≤a ≤min{ZA, ¯a1}
0
if
T
12(1−ZA) < C2 <
T
9(1−ZA)
& ¯a1 ≤ZA & ¯a1 ≤a ≤ZA,
where ¯a1 = 1 −
q
4 −36C1
T
(1 −ZA).
B.6
Quality Nash Equilibrium with Fine
For quality calculation, we should take into account that the calculated price is a
function of quality. By taking the partial derivative of Equation 13 with respect
to quality, we have:
dπ1
dq1
= ∂π1
∂q1
+ ∂π1
∂p1
∂p1
∂q1
+ ∂π1
∂p2
∂p2
∂q1
.
(61)


## Page 29


Note that in the above equation, we are going to maximize π1 given that
Equation 15 is satisﬁed. According to the envelope theorem, vendor 1 maximizes
its utility with respect to the price in the second stage where ∂π1
∂p1 = 0. Therefore,
we have:
dπ1
dq1
= ∂π1
∂q1
+ ∂π1
∂p2
∂p2
∂q1
⇒
dπ1
dq1
= −2S1q1 (a −ZA)2
−D1
∂f1
∂q1
+ (p∗
1 −f1) ∂D1
∂q1
+ p∗
1
∂D1
∂p2
∂p∗
2
∂q1
.
(62)
By using Equations 6 and 16, we have:
∂D1
∂p2
∂p∗
2
∂q1
=

1
2T (1 −a −b)
 1
3
∂f1
∂q1
−β
3

.
(63)
Both the above equations show that we need to calculate ∂f1
∂q1 . By considering
Equation 12, we have:
∂f1
∂q1
=
(
−F
if qmin ≥q1
0
if qmin < q1.
(64)
Note that for q1 = qmin, ∂f1
∂q1 is not deﬁned. But, here, we assume that this
value is equal to −F. Therefore, for q1 ≤qmin, Equation 62 changes into:
∂π1
∂q1
= q1
 
−2S1 (a −ZA)2 +
(β + F)2
9T (1 −a −b)
!
+ β + F
9
 
3 + a −b + f2 −βq2 −Fqmin
T (1 −a −b)
!
.
(65)
The above equation is linear in q1. In a linear equation like cq1 + d in which
c, d ≥0, cq1 + d is positive for every nonnegative value of q1. If this condition is
satisﬁed for Equation 65, π1 is increasing in [0, qmin] and as a result, π1 (a, b, q) is
maximized at qmin in interval [0, qmin]. Here, in our analysis, we assume that the
consumers do not take security into account, i.e., β = 0. Hence, for q1 > qmin,
by considering Equations 12 and 64, Equation 62 is equal to the following:
∂π1
∂q1
= −2S1q1 (a −ZA)2 .
(66)
The above Equation is negative for all values of q1. This means that π1 is
decreasing in q1 and as a result, π1 is maximized at qmin in interval [qmin, Q].
Therefore, by considering both Equations 65 and 66, we have q∗
1 = qmin if the
following two conditions are satisﬁed:
F 2 −18TS1 (1 −a −b) (a −ZA)2 ≥0,
(67)


## Page 30


3 + a −b + f2 −Fqmin
T (1 −a −b) ≥0.
(68)
In a similar way, vendor 2 invests in q∗
2 = qmin if the following two conditions
are satisﬁed:
F 2 −18TS2 (1 −a −b) (1 −b −ZA)2 ≥0,
(69)
3 + a −b + f1 −Fqmin
T (1 −a −b) ≥0.
(70)
If both vendor 1 and vendor 2 invest in qmin level of security, we have f1 =
f2 = 0. If Equations 67 and 69 are satisﬁed in addition to the following equation,
both vendors will invest in qmin level of security.
3 + a −b −
Fqmin
T (1 −a −b) ≥0.⊓⊔
(71)
B.7
Proof of Lemmas 3
When consumers do not take security into account, i.e., β = 0, and q∗
1 = q∗
2 =
qmin, we have:
dπ1
da = p∗
1
 −1 −3a −b
6 (1 −a −b)

−2

C1 + S1

qmin2
(a −ZA) ,
(72)
dπ2
db
=
p∗
2
 −1 −3b −a
6 (1 −a −b)

+ 2

C2 + S2

qmin2
(1 −b −ZA) .
(73)
It is similar to the case where there is no ﬁne except that C1 and C2 change
into C1 + S1
 qmin2 and C2 + S2
 qmin2, respectively. ⊓⊔

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
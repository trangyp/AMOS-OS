---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.03533v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1801.03533v1_Selection_Problems_in_the_Presence_of_Implicit_Bias

> Source: 1801.03533v1_Selection_Problems_in_the_Presence_of_Implicit_Bias.pdf

> Pages: 38

---


## Page 1


Selection Problems in the Presence of Implicit Bias
Jon Kleinberg
Cornell University
Manish Raghavan
Cornell University
Abstract
Over the past two decades, the notion of implicit bias has come to serve as an important
component in our understanding of discrimination in activities such as hiring, promotion, and
school admissions. Research on implicit bias posits that when people evaluate others – for example,
in a hiring context – their unconscious biases about membership in particular groups can have
an eﬀect on their decision-making, even when they have no deliberate intention to discriminate
against members of these groups. A growing body of experimental work has pointed to the eﬀect
that implicit bias can have in producing adverse outcomes.
Here we propose a theoretical model for studying the eﬀects of implicit bias on selection decisions,
and a way of analyzing possible procedural remedies for implicit bias within this model. A canonical
situation represented by our model is a hiring setting: a recruiting committee is trying to choose a
set of ﬁnalists to interview among the applicants for a job, evaluating these applicants based on their
future potential, but their estimates of potential are skewed by implicit bias against members of one
group. In this model, we show that measures such as the Rooney Rule, a requirement that at least
one of the ﬁnalists be chosen from the aﬀected group, can not only improve the representation of
this aﬀected group, but also lead to higher payoﬀs in absolute terms for the organization performing
the recruiting. However, identifying the conditions under which such measures can lead to improved
payoﬀs involves subtle trade-oﬀs between the extent of the bias and the underlying distribution of
applicant characteristics, leading to novel theoretical questions about order statistics in the presence
of probabilistic side information.
1
Introduction
Over the past two decades, the notion of implicit bias [13] has come to provide on important perspective
on the nature of discrimination. Research on implicit bias argues that unconscious attitudes toward
members of diﬀerent demographic groups — for example, deﬁned by gender, race, ethnicity, national
origin, sexual orientation, and other characteristics — can have a non-trivial impact on the way in
which we evaluate members of these groups; and this in turn may aﬀect outcomes in employment
[2, 3, 21], education [22], law [14, 15], medicine [12], and other societal institutions.
In the context of a process like hiring, implicit bias thus shifts the question of bias and discrimina-
tion to be not just about identifying bad actors who are intentionally discriminating, but also about
the tendency of all of us to reach discriminatory conclusions based on the unconscious application of
stereotypes. An understanding of these issues also helps inform the design of interventions to mitigate
implicit bias — when essentially all of us have a latent tendency toward low-level discrimination, a set
of broader practices may be needed to guide the process toward the desired outcome.
A basic mechanism: The Rooney Rule.
One of the most basic and widely adopted mechanisms
in practice for addressing implicit bias in hiring and selection is the Rooney Rule [7], which, roughly
speaking, requires that in recruiting for a job opening, one of the candidates interviewed must come
from an underrepresented group. The Rooney Rule is named for a protocol adopted by the National
1
arXiv:1801.03533v1  [cs.CY]  4 Jan 2018


## Page 2


Football League (NFL) in 2002 in response to widespread concern over the low representation of
African-Americans in head coaching positions; it required that when a team is searching for a new
head coach, at least one minority candidate must be interviewed for the position. Subsequently the
Rooney Rule has become a guideline adopted in many areas of business [5]; for example, in 2015 then-
President Obama exhorted leading tech ﬁrms to use the Rooney Rule for hiring executives, and in
recent years companies including Amazon, Facebook, Microsoft, and Pinterest have adopted a version
of the Rooney Rule requiring that at least one candidate interviewed must be a woman or a member
of an underrepresented minority group [18]. In 2017, a much-awaited set of recommendations made
by Eric Holder and colleagues to address workplace bias at Uber advocated for the use of the Rooney
Rule as one of its key points [8, 19].
The Rooney Rule is the subject of ongoing debate, and one crucial aspect of this debate is the
following tension. On one side is the argument that implicit (or explicit) bias is preventing deserving
candidates from underrepresented groups from being fairly considered, and the Rooney Rule is pro-
viding a force that counter-balances and partially oﬀsets the consequences of this underlying bias. On
the other side is the concern that if a job search process produces a short-list of top candidates all
from the majority group, it may be because these are genuinely the strongest candidates despite the
underlying bias — particularly if there is a shortage of available candidates from other groups. In this
case, wholesale use of the Rooney Rule may lead ﬁrms to consider weaker candidates from underrep-
resented groups, which works against the elimination of unconscious stereotypes. Of course, there are
other reasons to seek diversity in recruiting that may involve broader considerations or longer time
horizons than just the speciﬁc applicants being evaluated; but even these lines of argument generally
incorporate the more local question of the eﬀect on the set of applicants.
Given the widespread consideration of the Rooney Rule from both legal and empirical perspectives
[7], it is striking that prior work has not attempted to formalize the inherently mathematical question
that forms a crucial ingredient in these debates: given some estimates of the extent of bias and
the prevalence of available minority candidates, does the expected quality of the candidates being
interviewed by a hiring committee go up or down when the Rooney Rule is implemented? When the
bias is large and there are many minority candidates, it is quite possible that a hiring committee’s bias
has caused it to choose a weaker candidate over a stronger minority one, and the Rooney Rule may be
strengthening the pool of interviewees by reversing this decision and swapping the stronger minority
candidate in. But when the bias is small or there are few minority candidates, the Rule might be
reversing a decision that in fact chose the stronger applicant.
In this paper, we propose a formalization of this family of questions, via a simpliﬁed model of
selection with implicit bias, and we give a tight analysis of the consequences of using the Rooney Rule
in this setting. In particular, when selecting for a ﬁxed number of slots, we identify a sharp threshold
on the eﬀectiveness of the Rooney Rule in our model that depends on three parameters: not just the
extent of bias and the the prevalence of available minority candidates, but a third quantity as well
— essentially, a parameter governing the distribution of candidates’ expected future job performance.
We emphasize that our model is deliberately stylized, to abstract the trade-oﬀs as cleanly as possible.
Moreover, in interpreting these results, we emphasize a point noted above, that there are other reasons
to consider using the Rooney Rule beyond the issues that motivate this particular formulation; but
an understanding of the trade-oﬀs in our model seems informative in any broader debate about such
hiring and selection measures.
We now describe the basic ingredients of our model, followed by a summary of the main results.
2


## Page 3


1.1
A Model of Selection with Implicit Bias
Our model is based on the following scenario. Suppose that a hiring committee is trying to ﬁll an open
job position, and it would like to choose the k ≥2 best candidates as ﬁnalists to interview from among
a large set of applicants. We will think of k as a small constant, and indeed most of the subtlety of
the question already arises for the case k = 2, when just two ﬁnalists must be selected.
X-candidates and Y -candidates.
The set of all applicants is partitioned into two groups X and
Y , where we think of Y as the majority group, and X as a minority group within the domain that
may be subject to bias. For some positive real number α ≤1 and a natural number n, there are n
applicants from group Y and αn applicants from group X. If a candidate i belongs to X, we will
refer to them as an X-candidate, and if i belongs to Y , we will refer to them as a Y -candidate. (The
reader is welcome, for example, to think of the setting of academic hiring, with X as candidates from
a group that is underrepresented in the ﬁeld, but the formulation is general.)
Each candidate i has a (hidden) numerical value that we call their potential, representing their
future performance over the course of their career. For example, in faculty hiring, we might think
of the potential of each applicant in terms of some numerical proxy like their future lifetime citation
count (with the caveat that any numerical measure will of course be an imperfect representation). Or
in hiring executives, the potential of each applicant could be some measure of the revenue they will
bring to the ﬁrm.
We assume that there is a common distribution Z that these numerical potentials come from:
each potential is an independent draw from Z. (Thus, the applicants can have widely diﬀering values
for their numerical potentials; they just arise as draws from a common distribution.) For notational
purposes, when i is an X-candidate, we write their potential as Xi, and when j is a Y -candidate,
we write their potential as Yj. We note an important modeling decision in this formulation: we are
assuming that all Xi and all Yj values come from this same distribution Z. While it is also of interest
to consider the case in which the numerical potentials of the two groups X and Y are drawn from
diﬀerent group-speciﬁc distributions, we focus on the case of identical distributions for two reasons.
First, there are many settings where diﬀerences between the underlying distributions for diﬀerent
groups appear to be small compared to the bias-related eﬀects we are seeking to measure; and second,
in any formal analysis of bias between groups, the setting in which the groups begin with identical
distributions is arguably the ﬁrst fundamental special case that needs to be understood.
In the domains that we are considering — hiring executives, faculty members, athletes, performers
— there is a natural functional form for the distribution Z of potentials, and this is the family of
power laws (also known as Pareto distributions), with Pr [Z ≥t] = t−(1+δ) and support [1, ∞) for a
ﬁxed δ > 0. Extensive empirical work has argued that the distribution of individual output in a wide
range of creative professions can be approximated by power law distributions with small positive values
of δ [6]. For example, the distribution of lifetime citation counts is well-approximated by a power law,
as are the lifetime downloads, views, or sales by performers, authors, and other artists. In the last
part of the paper, we also consider the case in which the potentials are drawn from a distribution with
bounded support, but for most of the paper we will focus on power laws.
Selection with Bias.
Given the set of applicants, the hiring committee would like to choose k
ﬁnalists to interview. The utility achieved by the committee is the sum of the potentials of the k
ﬁnalists it chooses; the committee’s goal is to maximize its utility.1
1Since our goal is to model processes like the Rooney Rule, which apply to the selection of ﬁnalists for interviewing,
rather than to the hiring decision itself, we treat the choice of k ﬁnalists as the endpoint rather than modeling the
interviews that subsequently ensue.
3


## Page 4


If the committee could exactly evaluate the potential of each applicant, then it would have a
straightforward way to maximize the utility of the set of ﬁnalists: simply sort all applicants by po-
tential, and choose the top k as ﬁnalists. The key feature of the situation we would like to capture,
however, is that the committee is biased in its evaluations; we look for a model that incorporates this
bias as cleanly as possible.
Empirical work in some of our core motivating settings — such as the evaluation of scientists and
faculty candidates — indicates that evaluation committees often systematically downweight female
and minority candidates of a given level of achievement, both in head-to-head comparisons and in
ranking using numerical scores [23]. It is thus natural to model the hiring committee’s evaluations as
follows: they correctly estimate the potential of a Y -applicant j at the true value Yj, but they estimate
the potential of an X-applicant i at a reduced value ˜
Xi < Xi. They then rank candidates by these
values {Yj} and { ˜
Xi}, and they choose the top k according to this biased ranking.
For most of the paper, we focus on the case of multiplicative bias, in which ˜
Xi = Xi/β for a bias
parameter2 β > 1. This is a reasonable approximation to empirical data from human-subject studies
[23]; and moreover, for power law distributions this multiplicative form is in a strong sense the “right”
parametrization of the bias, since biases that grow either faster or slower than multiplicatively have a
very simple asymptotic behavior in the power law case.
In this aspect of the model, as in others, we seek the cleanest formulation that exposes the key
underlying issues; for example, it would be an interesting extension to consider versions in which the
estimates for each individual are perturbed by random noise. A line of previous work [4, 10, 11] has
analyzed models of ranking under noisy perturbations; while our scenario is quite diﬀerent in that the
entities being ranked are partitioned into a ﬁxed set of groups with potentially diﬀerent levels of bias
and noise, it would be natural to see if these techniques could potentially be extended to handle noise
in the context of implicit bias.
1.2
Main Questions and Results
This then is the basic model in which we analyze interventions with the structure of the Rooney Rule:
(i) a set of n Y -applicants and αn X-applicants each have an independent future potential drawn from
a power law distribution; (ii) a hiring committee ranks the applicants according to a sorted order in
which each X-applicant’s potential is divided down by β > 1, and chooses the top k in this ordering
as ﬁnalists; and (iii) the hiring committee’s utility is the sum of the potentials of the k ﬁnalists.
Qualitatively, the motivation for the Rooney Rule in such settings is that hiring committees are
either unwilling or unable to reasonably correct for their bias in performing such rankings, and therefore
cannot be relied on to interview X-candidates on their own. The diﬃculty in removing this skew from
such evaluations is a signature aspect of phenomena around implicit bias.
The decision to impose the Rooney Rule is made at the outset, before the actual values of the
potentials {Yj} and { ˜
Xi} are materialized. All that is known at the point of this initial decision to use
the Rule or not are the parameters of the domain: the bias β, the relative abundance of X-candidates
α, the power law exponent 1 + δ, and the number of ﬁnalists to be chosen k. The question is: as a
function of these parameters, will the use of the Rooney Rule produce a positive or negative expected
change in utility, where the expectation is taken over the random draws of applicant values? We note
that one could instead ask about the probability that the Rooney Rule produces a positive change in
utility as opposed to the expected change; in fact, our techniques naturally extend to characterize not
only the expected change, but the probability that this change is positive, as we will show in Section 2.
Our model lets us make precise the trade-oﬀin utility that underpins the use of the Rooney Rule. If
the committee selects an X-candidate on its own — even using its biased ranking — then their choice
2When β = 1, the ranking has no bias.
4


## Page 5


Figure 1: Fixing k = 2, the (α, β, δ) values for which the Rooney Rule produces a positive expected
change for suﬃciently large n lie above a surface (depicted in the ﬁgure) deﬁned by the function
φ2(α, β, δ) = 1.
already satisﬁes the conditions of the Rule. But if all k ﬁnalists are Y -candidates, then the Rooney
Rule requires that the committee replace the lowest-ranked of these ﬁnalists j with the highest-ranked
X-candidate i. Because i was not already a ﬁnalist, we know that ˜
Xi = Xi/β < Yj. But to see
whether this yields a positive change in utility, we need to understand which of Xi or Yj has a larger
expected value, conditional on the information contained in the committee’s decision, that Xi/β < Yj.
Our main result is an exact characterization of when the Rooney Rule produces a positive expected
change in terms of the four underlying parameters, showing that it non-trivially depends on all four.
For the following theorem, and for the remainder of the paper, we assume 0 < α ≤1, β > 1, and
δ > 0. We begin with the case where k = 2.
Theorem 1.1. For k = 2 and suﬃciently large n, the Rooney Rule produces a positive expected change
if and only if φ2(α, β, δ) > 1 where
φ2(α, β, δ) =
α1/(1+δ) h
1 −(1 + c−1)−δ/(1+δ) h
1 +
δ
1+δ(1 + c)−1ii
δ
1+δ(1 + c)−1−δ/(1+δ)
(1)
and c = αβ−(1+δ). Moreover, φ2(α, β, δ) is increasing in β, so for ﬁxed α and δ there exists β∗such
that φ2(α, β, δ) > 1 if and only if β > β∗.
Thus, we have an explicit characterization for when the Rooney Rule produces positive expected
change. The following theorem extends this to larger values of k.
5


## Page 6


Theorem 1.2. There is an explicit function φk(α, β, δ) such that the Rooney Rule produces a positive
expected change, for n suﬃciently large and k = O(ln n), if and only if φk(α, β, δ) > 1.
Interestingly, even for larger values of k, there are parts of the parameter space for which the
Rooney Rule produces a positive expected change and parts for which the Rooney Rule produces a
negative expected change, independent of the number of applicants n.
Figure 1 depicts a view of the function φ2, by showing the points in three-dimensional (α, β, δ)
space for which φ takes the value 1. The values for which the Rooney Rule produces a positive expected
change for suﬃciently large n lie above this surface.
The surface in Figure 1 is fairly complex, and it displays unexpected non-monotonic behavior. For
example, on certain regions of ﬁxed (α, β), it is non-monotonic in δ, a fact which is not a priori obvious:
there are choices of α and β for which the Rooney Rule produces a positive expected change at certain
“intermediate” values of δ, but not at values of δ that are suﬃciently smaller or suﬃciently larger.
Moreover, there exist (α, δ) pairs above which the surface does not exist. (One example in Figure 1
occurs at α ≈0.3 and δ ≈3). Characterizing the function φ and its level set φ = 1 is challenging,
and it is noteworthy that the complexity of this function is arising from our relatively bare-bones
formulation of the trade-oﬀin the Rooney Rule; this suggests the function and its properties are
capturing something inherent in the process of biased selection.
One monotonocity result we are able to establish for the function φ is the following, showing that
for ﬁxed (α, β, δ), increasing the number of positions can’t make the Rooney Rule go from beneﬁcial
to harmful.
Theorem 1.3. For suﬃciently large n and k = O(ln n), if the Rooney Rule produces a positive expected
change at a given number of ﬁnalists k, it also produces a positive expected change when there are k+1
ﬁnalists (at the same (α, β, δ)).
We prove these theorems through an analysis of the order statistics of the underlying power law
distribution. Speciﬁcally, if we draw m samples from the power law Z and sort them in ascending
order from lowest to highest, then the ℓth item in the sorted list is a random variable denoted Z(ℓ:m).
To analyze the eﬀect of the Rooney Rule, we are comparing Y(n−k+1:n) with X(αn:αn). Crucially, we
are concerned with their expected values conditional on the fact that the committee chose the kth-
ranked Y -candidate over the top-ranked X-candidate, implying as noted above that X(αn:αn)/β <
Y(n−k+1:n). The crucial comparison is therefore between E

Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)

and
E

X(αn:αn)|X(αn:αn) < βY(n−k+1:n)

. Order statistics conditional on this type of side information turn
out to behave in complex ways, and hence the core of the analysis is in dealing with these types of
conditional order statistics for power law distributions.
More generally, given the ubiquity of power law distributions [6], we ﬁnd it surprising how little
is known about how their order statistics behave qualitatively. In this respect, the techniques we
provide may prove to be independently useful in other applications. For example, we develop a tight
asymptotic characterization of the expectations of order statistics from a power law distribution that
to our knowledge is novel.
We also note that although our results are expressed for suﬃciently large n, the convergence to
the asymptotic behavior happens very quickly as n grows; to handle ﬁxed values of n, we need only
modify the bounds by correction terms that grow like

1 ± O

(ln n)2
n

. In particular, the errors in
the asymptotic analysis are small once n reaches 50, which is reasonable for settings in which a job
opening receives many applications.
Estimating the level of bias β.
The analysis techniques we develop for proving Theorem 1.2 can
also be used for related problems in this model. A speciﬁc question we are able to address is the
problem of estimating the amount of bias from a history of hiring decisions.
6


## Page 7


In particular, suppose that over m years the hiring committee makes one oﬀer per year; in N of the
m years this oﬀer goes to an X-candidate, and in m−N of the m years this oﬀer goes to a Y -candidate.
Which value of the bias parameter β maximizes the probability of this sequence of observations?
We provide a tight characterization of the solution to this question, ﬁnding again that it depends
not only on α (in this case, the sequence of α values for each year), but also on the power law exponent
1 + δ. The solution has a qualitatively natural structure, and produces β = 1 (corresponding to no
bias) as the estimate when the fraction of X-candidates hired over the m years is equal to the expected
number that would be hired under random selection.
Generalizations to other distributions.
Finally, at the end of the paper we consider how to adapt
our approach for classes of distributions other than power laws. A diﬀerent category of distributions
that can be motivated by the considerations discussed here is the set of bounded distributions, which
take values only over a ﬁnite interval.
Just as power laws are characteristic of the performance
of employees in certain professions, bounded distributions are appropriate when there are absolute
constraints on the maximum eﬀect a single employee can have.
Moreover, bounded distributions are also of interest because they contain the uniform distribution
on [0, 1] as a special case. We can think of this special case as describing an instance in which each
candidate is associated with their quantile (between 0 and 1) in a ranking of the entire population,
and the bias then operates on this quantile value, reducing it in the case of X-candidates.
For bounded distributions, we can handle much more general forms for the bias — essentially, any
function that reduces the values Xi strictly below the maximum of the distribution (for instance, a
bias that always prefers a Y -candidate to an X-candidate when they are within some ε of each other).
When k = 2 and there are equal numbers of X-candidates and Y -candidates, we show that for any
bounded distribution and any such bias, the Rooney Rule produces a positive expected change in
utility for all suﬃciently large n.
1.3
An Illustrative Special Case: Inﬁnite Bias
To illustrate some of the basic considerations that go into our analysis and its interpretation, we begin
with a simple special case that we can think of as “inﬁnite bias” — the committee deterministically
ranks every Y -candidate above every X-candidate. This case already exhibits structurally rich be-
havior, although the complexity is enormously less than the case of general β. We also focus here on
k = 2. In terms of Figure 1, we can visualize the inﬁnite bias case as if we are looking down at the
plot from inﬁnitely high up; thus, reasoning about inﬁnite bias amounts to determining which parts
of the (α, δ) plane are covered by the surface φ2(α, β, δ) = 1.
With inﬁnite bias, the committee is guaranteed to choose the two highest-ranked Y -candidates in
the absence of an intervention; with the Rooney Rule, the committee will choose the highest-ranked
Y -candidate and the highest-ranked X-candidate. As we discuss in the next section, for power law
distributions with exponent 1+δ, if z∗is the expected maximum of n draws from the distribution, then
(i) the expected value of the second-largest of the n draws is
δ
(1+δ)z∗; and (ii) the expected maximum
of αn draws from the distribution is asymptotically α1/(1+δ)z∗.
This lets us directly evaluate the utility consequences of the intervention. If there is no intervention,
the utility of the committee’s decision will be

1 +
δ
1+δ

z∗, and if the Rooney Rule is used, the utility
of the committee’s decision will be (1+α1/(1+δ))z∗. Thus, the Rooney Rule produces positive expected
change in utility if and only if α1/(1+δ) >
δ
(1+δ); that is, if and only if α >

δ
1+δ
1+δ
.
In addition to providing a simple closed-form expression for when to use the Rooney Rule in this
setting, the condition itself leads to some counter-intuitive consequences. In particular, the closed-
7


## Page 8


form expression for the condition makes it clear that for every α > 0, there exists a suﬃciently small
δ > 0 so that when the distribution of applicant potentials is a power law with exponent 1 + δ, using
the Rooney Rule produces the higher expected utility. In other words, with a power law exponent
close to 1, it’s a better strategy to commit one of the two oﬀers to the X-candidates, even though
they form an extremely small fraction of the population.
This appears to come perilously close to contradicting the following argument. We can arbitrarily
divide the Y -candidates into two sets A and B of n/2 each; and if α < 1/2, each of A and B is larger
than the set of all X-candidates. Let a∗be the top candidate in A and b∗be the top candidate in B.
Each of a∗and b∗has at least the expected value of the top X-candidate, and moreover, one of them
is the top Y -candidate overall. So how can it be that choosing a∗and b∗fails to improve on the result
of using the Rooney Rule?
The resolution is to notice that using the Rooney Rule still involves hiring the top Y -candidate. So
it’s not that the Rooney Rule chooses one of a∗or b∗at random, together with the top X-candidate.
Rather, it chooses the better of a∗and b∗, along with the top X-candidate. The real point is that
power law distributions have so much probability in the tail of the distribution that the best person
among a set of αn can easily have a higher expected value than the second-best person among a set
of n, even when α is quite small. This is a key property of power law distributions that helps explain
what’s happening both in this example and in our analysis.
1.4
A Non-Monotonicity Eﬀect
As noted above, much of the complexity in the analysis arises from working with expected values of
random variables conditioned on the outcomes of certain biased comparisons. One might hope that
expected values conditional on these types of comparisons had tractable properties that facilitated the
analysis, but this is not the case; in fact, these conditional expectations exhibit some complicated and
fairly counter-intuitive behavior. To familiarize the reader with some of these phenomena — both as
preparation for the subsequent sections, but also as an interesting end in itself — we oﬀer the following
example.
Much of our analysis involves quantities like E [X|X > βY ] — the conditional expectation of X,
given that it exceeds some other random variable Y multiplied by a bias parameter. (We will also
be analyzing the version in which the inequality goes in the other direction, but we’ll focus on the
current expression for now.) If we choose X and Y as independent random variables both drawn from
a distribution Z, and then view the conditional expectation as a function just of the bias parameter
β, what can we say about the properties of this function f(β) = E [X|X > βY ]?
Intuitively we’d expect f(β) to be monotonically increasing in β — indeed, as β increases, we’re
putting a stricter lower bound on X, and so this ought to raise the conditional expectation of X.
The surprise is that this is not true in general; we can construct independent random variables X
and Y for which f(β) is not monotonically increasing. In fact, the random variables are very simple:
we can have each of X and Y take values independently and uniformly from the ﬁnite set {1, 5, 9, 13}.
Now, the event X > 2Y consists of four possible pairs of (X, Y ) values: (5,1), (9,1), (13,1), and (13,5).
Thus, f(2) = E [X|X > 2Y ] = 10. In contrast, the event X > 3Y consists of three possible pairs of
(X, Y ) values: (5,1), (9,1), and (13,1). Thus, f(3) = 9, which is a smaller value, despite the fact that
X is required to be a larger multiple of Y .
The surprising content of this example has a fairly sharp formulation in terms of a story about
recruiting. Suppose that two academic departments, Department A and Department B, both engage
in hiring each year. In our stylized setting, each interviews one X-candidate and one Y -candidate
each year, and hires one of them. Each candidate comes from the uniform distribution on {1, 5, 9, 13}.
Departments A and B are both biased in their hiring: A only hires the X-candidate in a given year
8


## Page 9


if they’re more than twice as good as the Y -candidate, while B only hires the X-candidate in a given
year if they’re more than three times as good as the Y -candidate.
Clearly this bias hurts the average quality of both departments, B more so than A. But you might
intuitively expect that at least if you looked at the X-candidates that B has actually hired, they’d
be of higher average quality than the X-candidates that A has hired — simply because they had to
pass through a stronger ﬁlter to get hired. In fact, however, this isn’t the case: despite the fact that
B imposes a stronger ﬁlter, the calculations performed above for this example show that the average
quality of the X-candidates B hires is 9, while the average quality of the X-candidates A hires is 10.
This non-monotonicity property shows that the conditional expectations we work with in the
analysis can be pathologically behaved for arbitrary (even relatively simple) distributions. However,
we will see that with power law distributions we are able — with some work — to avoid these diﬃculties;
and part of our analysis will include a set of explicit monotonicity results.
2
Biased Selection with Power Law Distributions
Recall that for a random variable Z, we use Z(ℓ:m) to denote the ℓth order statistic in m draws from
Z: the value in position ℓwhen we sort m independent draws from Z from lowest to highest. Recall
also that when selecting k ﬁnalists, the Rooney Rule improves expected utility exactly when
E

X(αn:αn) −Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)

> 0.
Using linearity of expectation and the fact that Pr [A|B] Pr [B] = Pr [A · 1B], this is equivalent to
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
E
h
Y(n−k+1:n) · 1X(αn:αn)<βY(n−k+1:n)
i > 1.
(2)
We will show an asymptotically tight characterization of the tuples of parameters (k, α, β, δ) for which
this condition holds, up to an error term on the order of O

(ln n)2
n

. In order to better understand
the terms in (2), we begin with some necessary background.
2.1
Preliminaries
Fact 1. Let f(p:m) and F(p:m) be, respectively, the probability density function and cumulative dis-
tribution function of the pth order statistic out of m draws from the power law distribution with
parameter δ. Using deﬁnitions from [9],
f(p:m)(x) = (1 + δ)(m −p + 1)
 m
p −1
 
1 −x−(1+δ)p−1 
x−(1+δ)m−p+1
x−1
and
F(p:m)(x) =
m
X
j=p
m
j
 
1 −x−(1+δ)j 
x−(1+δ)m−j
.
Deﬁnition 2. We deﬁne
Γ(a) =
Z ∞
0
ta−1e−t dt.
Γ(·) is considered the continuous relaxation of the factorial, and it satisﬁes
Γ(a + 1) = aΓ(a).
If a is a positive integer, Γ(a + 1) = a!. Furthermore, Γ(a) > 1 for 0 < a < 1 and Γ(a) < 1 for
1 < a < 2.
9


## Page 10


2.2
The Case where k = 2
For simplicity, we begin with the case where we’re selecting k = 2 ﬁnalists. In this section, we will make
several approximations, growing tight with large n, that we treat formally in Appendices A and B.
This section is intended to demonstrate the techniques needed to understand the condition (2). In the
case where k = 2, always selecting an X-candidate increases expected utility if and only if
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−1:n)
i
E
h
Y(n−1:n) · 1X(αn:αn)<βY(n−1:n)
i > 1.
(3)
Theorems B.1 and B.2 in Appendix B give tight approximations to these quantities; here, we provide
an outline for how to ﬁnd them. For the sake of exposition, we’ll only show this for the denominator
in this section, which is slightly simpler to approximate. We begin with
E
h
Y(n−1:n) · 1X(αn:αn)<βY(n−1:n)
i
=
Z ∞
1
yf(n−1:n)(y)F(αn:αn)(βy) dy.
Letting c = αβ−(1+δ), we can use Lemma D.2 and some manipulation to approximate this by
(1 + δ)n(n −1)
Z ∞
1

1 −y−(1+δ)n(1+c)−2 
y−(1+δ)2
dy.
Conveniently, the function being integrated is (up to a constant factor) y · f(n(1+c)−1:n(1+c))(y), i.e.
y times the probability density function of the second-highest order statistic from n(1 + c) samples.
Since
E

Z(n(1+c)−1:n(1+c))

=
Z ∞
1
zf(n(1+c)−1:n(1+c))(z) dz
= (1 + δ)n(1 + c)(n(1 + c) −1)
Z ∞
1

1 −z−(1+δ)n(1+c)−2 
z−(1+δ)2
dz,
we have
E
h
Y(n−1:n) · 1X(αn:αn)<βY(n−1:n)
i
≈
1
(1 + c)2 E

Z(n(1+c)−1:n(1+c))

.
Then, we can use Lemmas D.10 and D.11 to get E

Z(n(1+c)−1:n(1+c))

≈(1 + c)1/(1+δ)E

Y(n−1:n)

,
meaning that
E
h
Y(n−1:n) · 1X(αn:αn)<βY(n−1:n)
i
≈(1 + c)−(1+δ/(1+δ))E

Y(n−1:n)

.
(4)
For the numerator of (3), a slightly more involved calculation yields
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−1:n)
i
≈E

X(αn:αn)
 
1 −(1 + c−1)−δ/(1+δ)

1 +
δ
1 + δ(1 + c)−1

.
(5)
By Lemmas D.10 and D.11, E

X(αn:αn)

≈Γ

δ
1+δ

(αn)1/(1+δ) and E

Y(n−1:n)

≈Γ

1 +
δ
1+δ

n1/(1+δ).
Recall that, up to the approximations we made, the Rooney Rule improves utility in expectation if
and only if the ratio between (5) and (4) is larger than 1. Therefore, the following theorem holds:
Theorem 2.1. For suﬃciently large n, the Rooney Rule with k = 2 improves utility in expectation if
and only if
α1/(1+δ) h
1 −(1 + c−1)−δ/(1+δ) h
1 +
δ
1+δ(1 + c)−1ii
δ
1+δ(1 + c)−1−δ/(1+δ)
> 1.
(6)
where c = αβ−(1+δ).
10


## Page 11


Note that in the limit as β →∞, c →0, and the entire expression goes to α1/(1+δ)(1 + δ)/δ, as
noted in Section 1.3. Although the full expression in the statement of Theorem 2.1 is complex, it
can be directly evaluated, giving a tight characterization of when the Rule yields increased utility in
expectation.
With this result, we could ask for a ﬁxed α and δ how to characterize the set of β such that the
condition in (6) holds. In fact, we can show that this expression is monotonically increasing in β.
Theorem 2.2. The left hand side of (6) is decreasing in c and therefore increasing in β. Hence for
ﬁxed α and δ there exists β∗such that (6) holds if and only if β > β∗.
Non-monotonicity in δ.
From Theorem 2.1, we can gain some intuition for the non-monotonicity
in δ shown in Figure 1. For α < e−1, we can show that even with inﬁnite bias, the Rooney Rule
has a negative eﬀect on utility for suﬃciently large δ. Intuitively, this is because the condition for
positive change with inﬁnite bias is α >

δ
1+δ
1+δ
, which can be written as α >
 1 −1
d
d for d = 1+δ.
Since this converges to e−1 from below, for suﬃciently large δ and α < e−1, we have α <

δ
1+δ
1+δ
.
On the other hand, as δ →0, the Rooney Rule has a more negative eﬀect on utility. For instance,
φ2(.3, 10, 1) > 1 but φ2(.3, 10, .5) < 1. Intuitively, this non-monotonicity arises from the fact that for
large δ and small α, the Rooney Rule always has a negative impact on utility, while for very small δ,
samples are very far from each other, meaning that the bias has less eﬀect on the ranking.
2.3
The General Case
We can extend these techniques to handle larger values of k. For k ∈[n], we deﬁne
rk(α, β, δ) = E

X(αn:αn)|X(αn:αn) < βY(n−k+1:n)

E

Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)
 =
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
E
h
Y(n−k+1:n) · 1X(αn:αn)<βY(n−k+1:n)
i.
We can see that the Rooney Rule improves expected utility when selecting k candidates if and only
if rk > 1. While rk depends on n, we will show that it is a very weak dependence: for small k, as n
increases, rk converges to a function of (α, β, δ, k) up to a 1 + O((ln n)2/n) multiplicative factor. To
make this precise, we deﬁne the following notion of asymptotic equivalence:
Deﬁnition 3. For nonnegative functions f(n) and g(n), deﬁne
f(n) ∼∼∼g(n)
if and only if there exist a > 0 and n0 > 0 such that
f(n)
g(n) ≤1 + a(ln n)2
n
and
g(n)
f(n) ≤1 + a(ln n)2
n
for all n ≥n0. In other words, f(n) = g(n)

1 ± O

(ln n)2
n

. When being explicit about a and n0,
we’ll write f(n) ∼∼∼a;n0 g(n).
Appendix C contains a series of lemmas establishing how to rigorously manipulate equivalences
of this form.
Now, we formally deﬁne a tight approximation to rk, which serves as an expanded
restatement of Theorem 1.2 from the introduction.
11


## Page 12


Theorem 2.3. For k ∈[n], deﬁne
φk(α, β, δ) = α1/(1+δ)cδ/(1+δ)(1 + c)k−1
 k−1−
1
1+δ
k−1


(1 + c−1)δ/(1+δ) −
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


(7)
where c = αβ−(1+δ). Note that φk does not depend on n. When (α, β, δ) are ﬁxed, we will simply write
this as φk. For k ≤((1 −c2) ln n)/2, we have
rk ∼∼∼φk,
and therefore the Rooney Rule improves expected utility for suﬃciently large n if and only if φk > 1.
This condition tightly characterizes when the Rooney Rule improves expected utility, and its
asymptotic nature in n becomes accurate even for moderately small n: for example, when n = 50, the
error between rk and φk is around 1% for reasonable choices of (α, β, δ).
Increasing k.
Consider the scenario in which we’re selecting k candidates, and for the given parame-
ter values, the Rooney Rule improves our expected utility. If we were to instead select k+1 candidates,
should we still be reserving a spot for an X-candidate? Intuitively, as k increases, the Rule is less
likely to change our selections, since we’re more likely to have already chosen an X-candidate; however,
it is not a priori obvious whether increasing k should make it better for us to use the Rooney Rule
(because we have more slots, so we’re losing less by reserving one) or worse (because as we take more
candidates, we stop needing a reserved slot).
In fact, we can apply Theorem 2.3 to understand how rk changes with k. The following theorem,
proven in Appendix B, is an expanded restatement of Theorem 1.3, showing that if the Rooney Rule
yields an improvement in expected quality when selecting k candidates, it will do so when selecting
k + 1 candidates as well.
Theorem 2.4. For k ≤((1 −c2) ln n)/2, we have φk+1 > φk, and therefore for suﬃciently large n,
we have rk+1 > rk.
Finally, using these techniques, we can provide a tight characterization of the probability that the
Rooney Rule produces a positive change. Speciﬁcally, we ﬁnd the probability that the Rooney Rule
has a positive eﬀect conditioned on the event that it changes the outcome.
Theorem 2.5.
Pr

X(αn:αn) > Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)
 ∼∼∼1 −
 
1 + αβ−(1+δ)
1 + α
!k
.
To determine whether the Rooney Rule is more likely than not to produce a positive eﬀect (con-
ditioned on changing the outcome), we can compare the right-hand side to 1/2.
Note that in the case of inﬁnite bias, the right-hand side becomes 1 −(1 + α)−k, and thus, the
Rooney Rule produces positive change with probability at least 1/2 if and only if α ≥
k√
2 −1. It is
interesting to observe that this means with inﬁnite bias, the condition is independent of δ; in contrast,
when considering the eﬀect on the expected value with inﬁnite bias, as we did in Section 1.3, the
expected change in utility due to the Rooney Rule did depend on δ.
12


## Page 13


2.4
Maximum Likelihood Estimation of β
The techniques established thus far make it possible to answer other related questions, including
the following type of question that we consider in this section: “Given some historical data on past
selections, can we estimate the bias present in the data?” For example, suppose that for the last m
years, a ﬁrm has selected one candidate for each year i out of a pool of αini X-candidates and ni
Y -candidates. If all applicants are assumed to come from the same underlying distribution, then it is
easy to see that the expected number of X-selections (in the absence of bias) should be
m
X
i=1
αi
1 + αi
,
regardless of what distribution the applicants come from. However, if there is bias in the selection
procedure, then this quantity now depends on the bias model and parameters of the distribution. In
particular, in our model, we can use Theorem B.3 to get
Pr

X(αn:αn) < βY(n:n)
 ∼∼∼
1
1 + αβ−(1+δ) .
This gives us the following approximation for the likelihood of the data D = (M1, . . . , Mm) given β,
where Mi is 1 if an X-candidate was selected in year i and 0 otherwise:
m
Y
i=1
(1 −Mi) ·
1
1 + αiβ−(1+δ) + Mi ·
αiβ−(1+δ)
1 + αiβ−(1+δ) .
Taking logarithms, this is
X
i:Mi=1
log(αiβ−(1+δ)) −
m
X
i=1
log(1 + αiβ−(1+δ)),
and maximizing this is equivalent to maximizing
X
i:Mi=1
log(β−(1+δ)) −
m
X
i=1
log(1 + αiβ−(1+δ)) = N log(β−(1+δ)) −
m
X
i=1
log(1 + αiβ−(1+δ))
where N is the number of X-candidates selected. Taking the derivative with respect to β, we get
−(1 + δ)Nβ−1 + (1 + δ)
m
X
i=1
αiβ−(2+δ)
1 + αiβ−(1+δ) .
Setting this equal to 0 and canceling common terms, we have
m
X
i=1
1
1 + α−1
i β1+δ = N
Since each 1/(1 + α−1
i β1+δ) is strictly monotonically decreasing in β, there is a unique ˆβ for which
equality holds, meaning that the likelihood is uniquely maximized by ˆβ, up to the 1 ± O((ln n)2/n)
approximation we made for Pr

X(αn:αn) < βY(n:n)

. In the special case where αi = α for i = 1, . . . , m,
then the solution is given by
ˆβ =
m
N −1

α
1/(1+δ)
.
13


## Page 14


3
Biased Selection with Bounded Distributions
In this section, we consider a model in which applicants come from a distribution with bounded
support. Qualitatively, one would expect diﬀerent results here from those with power law distributions
because in a model with bounded distributions, we expect that for large n, the top order statistics of
any distribution will concentrate around the maximum of that distribution. As a result, when there is
even a small amount of bias against one population, for large n the probability that any of the samples
with the highest perceived quality come from that population goes to 0. This means that the Rooney
Rule has an eﬀect with high probability, and the eﬀect is positive if the unconditional expectation of
the top X-candidate is larger than the unconditional expectation of the Y -candidate that it replaces.
We focus on the case when α = 1, meaning we have equal numbers of applicants from both
populations. We use the same order statistic notation as before. While all of our previous results have
modeled the bias as a multiplicative factor β, we can in fact show that in the bounded distribution
setting, for any model of bias ˜X(k:n) = b(X(k:n)) such that b(x) < T for x ≥0, where T is strictly
less than the maximum of the distribution, the Rooney Rule increases expected utility. Unlike in the
previous section the following theorem and analysis are by no means a tight characterization; instead,
this is an existence proof that for bounded distributions, there is always a large enough n such that the
Rooney Rule improves utility in expectation. We prove our results for continuous distributions with
support [0, 1], but a simple scaling argument shows that this extends to any continuous distribution
with bounded nonnegative support – speciﬁcally, we scale a distribution such that infx:f(x)>0 = 0 and
supx:f(x)>0 = 1.
Theorem 3.1. If f is a continuous probability density function on [0, 1] such that supx:f(x)>0 = 1 and
˜X(n:n) = b(X(n:n)) is never more than T < 1, then for large enough n,
E

X(n:n) −Y(n−1:n)|b(X(n:n)) < Y(n−1:n)

> 0.
While we the defer the full proof to Appendix E, the strategy for the proof is as follows:
1. With high probability, X(n:n) and Y(n−1:n) are both large.
2. Whenever X(n:n) and Y(n−1:n) are large, X(n:n) is signiﬁcantly larger than Y(n−1:n).
3. The gain from switching from Y(n−1:n) to X(n:n) when X(n:n) and Y(n−1:n) are both large outweighs
the loss when at least one of them is not large.
4
Conclusion
In this work we have presented a model for implicit bias in a selection problem motivated by settings
including hiring and admissions, and we analyzed the Rooney Rule, which can improve the quality
of the resulting choices. For one of the most natural settings of the problem, when candidates are
drawn from a power-law distribution, we found a tight characterization of the conditions under which
the Rooney Rule improves the quality of the outcome. In the process, we identiﬁed a number of
counter-intuitive eﬀects at work, which we believe may also help provide insight into how we can
reason about implicit bias. Our techniques also provided a natural solution to an inference problem
in which we estimate parameters of a biased decision-making process. Finally, we performed a similar
type of analysis on general bounded distributions.
There are a number of further directions in which these issues could be investigated. One intriguing
direction is to consider the possible connections to the theory of optimal delegation (see e.g. [1]).3
3We thank Ilya Segal for suggesting this connection to us.
14


## Page 15


In the study of delegation, a principal wants a task carried out, but this task can only be performed
by an agent who may have a utility function that is diﬀerent from the principal’s. In an important
family of these models, the principal’s only recourse is to impose a restriction on the set of possible
actions taken by the agent, creating a more constrained task for the agent to perform, in a way that
can potentially improve the quality of the eventual outcome from the principal’s perspective. Our
analysis of the Rooney Rule can be viewed as taking place from the point of view of a principal who
is trying to recruit k candidates, but where the process must be delegated to an agent whose utilities
for X-candidates and Y -candidates are diﬀerent from the principal’s, and who is the only party able
to evaluate these candidates’ potentials. The Rooney Rule, requiring that the agent select at least one
X-candidate, is an example of a mechanism that the principal could impose to restrict the agent’s set
of possible actions, potentially improving the quality of the selected candidates as measured by the
principal. More generally, it is interesting to ask whether there are other contexts where such a link
between delegation and this type of biased selection provides insight.
Our framework also makes it possible to naturally explore extensions of the basic model. First, the
model can be generalized to include noisy observations, potentially with a diﬀerent level of noise for
each group. It would also be interesting to analyze generalizations of the Rooney Rule; for example,
if we were to deﬁne the ℓth-order Rooney Rule to be the requirement that at least ℓof k ﬁnalists must
be from an underrepresented group, we could ask which ℓproduces the greatest increase in utility for
a given set of parameters. Finally, we could beneﬁt from a deeper undestanding of the function φ that
appears in our main theorems. For example, while we showed in Theorem 1.3 that φ is monotone in β
for k = 2, Figure 1 shows that φ is clearly not monotone in δ. A better understaning of the function
φ may lead to new insights into our model and into the phenomena it seeks to capture.
Acknowledgements
We thank Eric Parsonnet for his invaluable technical insights. This work was
supported in part by a Simons Investigator Grant and an NSF Graduate Fellowship.
References
[1] Ricardo Alonso and Niko Matouschek.
Optimal delegation.
Review of Economic Studies,
75(1):259–293, January 2008.
[2] Marianne Bertrand and Sendhil Mullainathan. Are Emily and Greg more employable than Lakisha
and Jamal? A ﬁeld experiment on labor market discrimination. American Economic Review,
94(4):991–1013, September 2004.
[3] Iris Bohnet, Alexandra van Geen, and Max Bazerman. When performance trumps gender bias:
Joint vs. separate evaluation. Management Science, 62(5):1225–1234, 2016.
[4] Mark Braverman and Elchanan Mossel.
Sorting from noisy information.
arXiv preprint
arXiv:0910.1191, 2009.
[5] Marilyn Cavicchia. How to ﬁght implicit bias? With conscious thought, diversity expert tells
NABE. American Bar Association: Bar Leader, 40(1), 2015.
[6] Aaron Clauset, Cosma R. Shalizi, and Mark E. J. Newman. Power-law distributions in empirical
data. SIAM Review, 51(4):661–703, 2009.
[7] Brian W. Collins. Tackling unconscious bias in hiring practices: The plight of the Rooney Rule.
NYU Law Review, 82(3), 2007.
15


## Page 16


[8] Covington and Burling. Recommendations to Uber, 13 June 2017.
[9] H. A. David and H. N. Nagaraja. Basic Distribution Theory, pages 9–32. John Wiley & Sons,
Inc., 2005.
[10] Uriel Feige, Prabhakar Raghavan, David Peleg, and Eli Upfal. Computing with noisy information.
SIAM Journal on Computing, 23(5):1001–1018, 1994.
[11] Qiang Fu and Jingfeng Lu. Micro foundations of multi-prize lottery contests: a perspective of
noisy performance ranking. Social Choice and Welfare, 38(3):497–517, 2012.
[12] Alexander R. Green, Dana R. Carney, Daniel J. Pallin, Long H. Ngo, Kristal L. Raymond, Lisa I.
Iezzoni, and Mahzarin R. Banaji. Implicit bias among physicians and its prediction of thrombolysis
decisions for black and white patients. Journal of General Internal Medicine, 22(9):1231–1238,
2007.
[13] Anthony G. Greenwald and Mahzarin R. Banaji. Implicit social cognition: attitudes, self-esteem,
and stereotypes. Psychological Review, 102(1):4–27, 1995.
[14] Anthony G. Greenwald and Linda Hamilton Krieger. Implicit bias: Scientiﬁc foundations. Cali-
fornia Law Review, 94:945–967, 2006.
[15] Christine Jolls and Cass R. Sunstein. The law of implicit bias. California Law Review, 94:969–996,
2006.
[16] Manuel Lopez and James Marengo. An upper bound for the expected diﬀerence between order
statistics. Mathematics Magazine, 84(5):365–369, 2011.
[17] Henrick John Malik. Exact moments of order statistics from the pareto distribution. Scandinavian
Actuarial Journal, 1966(3-4):144–157, 1966.
[18] Christina Passariello. Tech ﬁrms borrow football play to increase hiring of women. Wall Street
Journal, 27 September 2016.
[19] Hamza Shaban. What is the “Rooney Rule” that Uber just adopted? Washington Post, 13 June
2017.
[20] Francesco Giacomo Tricomi and Arthur Erd´elyi. The asymptotic expansion of a ratio of gamma
functions. Paciﬁc J. Math, 1(1):133–142, 1951.
[21] Eric Luis Uhlmann and Geoﬀrey L. Cohen. Constructed criteria: Redeﬁning merit to justify
discrimination. Psychological Science, 16(6):474–480, 2005.
[22] Linda van den Bergh, Eddie Denessen, Lisette Hornstra, Marinus Voeten, and Rob W. Holland.
The implicit prejudiced attitudes of teachers: Relations to teacher expectations and the ethnic
achievement gap. American Education Research Journal, 47(2):497–527, 2010.
[23] Christine Wenneras and Agnes Wold. Nepotism and sexism in peer-review. Nature, 387:341–343,
1997.
16


## Page 17


A
Missing Proofs for Section 2
Proof of Theorems 2.1 and 2.3. We can expand the statement in Theorem B.1 to
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
∼∼∼E

X(αn:αn)


1 −(1 + c−1)−δ/(1+δ)
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


∼∼∼(αn)1/(1+δ)Γ

δ
1 + δ
 
1 −(1 + c−1)−δ/(1+δ)
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


(By Lemma D.10)
This gives us a ratio
rk(α, β, δ) =
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
E
h
Y(n−k+1:n) · 1X(αn:αn)<βY(n−k+1:n)
i
∼∼∼
(αn)1/(1+δ)Γ

δ
1+δ
 h
1 −(1 + c−1)−δ/(1+δ) Pk−1
j=0
 j−
1
1+δ
j

(1 + c)−ji
(1 + c)−(k−1/(1+δ)) Γ(k−
1
1+δ)
Γ(k)
n1/(1+δ)
(Using Theorem B.2)
=
α1/(1+δ)Γ(k)Γ

δ
1+δ

(1 + c)k−1/(1+δ)
Γ

k −
1
1+δ


1 −(c−1(1 + c))−δ/(1+δ)
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


=
α1/(1+δ)cδ/(1+δ)Γ(k)Γ

δ
1+δ

(1 + c)k−1
Γ

k −
1
1+δ


(1 + c−1)δ/(1+δ) −
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


= α1/(1+δ)cδ/(1+δ)(1 + c)k−1
 k−1−
1
1+δ
k−1


(1 + c−1)δ/(1+δ) −
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


Proof of Theorem 2.2. Since the only inﬂuence of β is through c and c is decreasing in β, it is suﬃcient
to show that
α1/(1+δ) h
1 −(1 + c−1)−δ/(1+δ) h
1 +
δ
1+δ(1 + c)−1ii
δ
1+δ(1 + c)−1−δ/(1+δ)
is decreasing in c. Ignoring constants, this is
∝cδ/(1+δ)(1 + c)

(1 + c−1)δ/(1+δ) −1 −
δ
1 + δ(1 + c)−1

= (1 + c)1+δ/(1+δ) −cδ/(1+δ)(1 + c) −
δ
1 + δcδ/(1+δ)
= (1 + c)1+δ/(1+δ) −c1+δ/(1+δ) −

1 +
δ
1 + δ

cδ/(1+δ)
17


## Page 18


This has derivative
δ
dc(1 + c)1+δ/(1+δ) −c1+δ/(1+δ) −

1 +
δ
1 + δ

cδ/(1+δ)
=

1 +
δ
1 + δ

(1 + c)δ/(1+δ) −

1 +
δ
1 + δ

cδ/(1+δ) +

δ
1 + δ
 
1 +
δ
1 + δ

c−1/(1+δ),
which is negative if and only if
(1 + c)δ/(1+δ) < cδ/(1+δ) +
δ
1 + δc−1/(1+δ)
⇐⇒(1 + c)δ/(1+δ)c−δ/(1+δ) < 1 +
δ
1 + δc−1
⇐⇒(1 + c−1)δ/(1+δ) < 1 +
δ
1 + δc−1.
This is true by Lemma D.9, which proves the theorem.
Proof of Theorem 2.4. By Theorem 2.3,
φk(α, β, δ) =
α1/(1+δ)cδ/(1+δ)Γ(k)Γ

δ
1+δ

(1 + c)k−1
Γ

k −
1
1+δ


(1 + c−1)δ/(1+δ) −
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


We use the fact that for a, b ∈Z and s ∈R
Γ(s −a + 1)
Γ(s −b + 1) = (−1)b−a Γ(b −s)
Γ(a −s).
If the summation went to ∞, it would be
∞
X
j=0
j −
1
1+δ
j

(1 + c)−j =
∞
X
j=0
(1 + c)−j
Γ

j +
δ
1+δ

Γ

δ
1+δ

Γ(j + 1)
=
∞
X
j=0
(1 + c)−j(−1)j
Γ

1 −
δ
1+δ

Γ

−j + 1 +
δ
1+δ

Γ(j + 1)
=
∞
X
j=0
−
δ
1+δ
j

(−(1 + c)−1)j
= (1 −(1 + c)−1)−δ/(1+δ)
= (1 + c−1)δ/(1+δ)
Therefore,
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j = (1 + c−1)δ/(1+δ) −
∞
X
j=k
j −
1
1+δ
j

(1 + c)−j.
Plugging this in,
φk(α, β, δ) =
α1/(1+δ)cδ/(1+δ)Γ(k)Γ

δ
1+δ

(1 + c)k−1
Γ

k −
1
1+δ

∞
X
j=k
j −
1
1+δ
j

(1 + c)−j
=
α1/(1+δ)cδ/(1+δ)Γ(k)Γ

δ
1+δ

Γ

k −
1
1+δ

(1 + c)
∞
X
j=0
j + k −
1
1+δ
j + k

(1 + c)−j
18


## Page 19


With this, we can take
φk+1(α, β, δ) −φk(α, β, δ)
=
α1/(1+δ)cδ/(1+δ)Γ

δ
1+δ

(1 + c)


Γ(k + 1)
Γ

k +
δ
1+δ

∞
X
j=0
j + k + 1 −
1
1+δ
j + k + 1

(1 + c)−j
−
Γ(k)
Γ

k −
1
1+δ

∞
X
j=0
j + k −
1
1+δ
j + k

(1 + c)−j


=
α1/(1+δ)cδ/(1+δ)Γ(k)Γ

δ
1+δ

Γ

k −
1
1+δ

(1 + c)


k
k −
1
1+δ
∞
X
j=0
j + k + 1 −
1
1+δ
j + k + 1

(1 + c)−j
−
∞
X
j=0
j + k −
1
1+δ
j + k

(1 + c)−j


=
α1/(1+δ)cδ/(1+δ)Γ(k)Γ

δ
1+δ

Γ

k −
1
1+δ

(1 + c)
∞
X
j=0
(1 + c)−j
"
k
k −
1
1+δ
j + k + 1 −
1
1+δ
j + k + 1

−
j + k −
1
1+δ
j + k
#
Thus, to show that φk+1 > φk, it is suﬃcient to show that for j ≥0,
k
k −
1
1+δ
j + k + 1 −
1
1+δ
j + k + 1

−
j + k −
1
1+δ
j + k

> 0
k
k −
1
1+δ
Γ

j + k + 1 +
δ
1+δ

Γ(j + k + 2)Γ

δ
1+δ
 −
Γ

j + k +
δ
1+δ

Γ(j + k + 1)Γ

δ
1+δ
 > 0
k
k −
1
1+δ
j + k +
δ
1+δ
j + k + 1
−1 > 0
(Γ(x + 1) = xΓ(x))
k −
1
1+δ + (j + 1)
k + (j + 1)
>
k −
1
1+δ
k
The last inequality holds by Lemma D.4. As a result a result, φk+1 > φk, proving the theorem.
Proof Theorem 2.5. We want to ﬁnd
Pr

X(αn:αn) > Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)

,
or equivalently,
Pr

X(αn:αn) < Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)

.
This can be written as
Pr

X(αn:αn) < Y(n−k+1:n) ∩X(αn:αn) < βY(n−k+1:n)

Pr

X(αn:αn) < βY(n−k+1:n)

= Pr

X(αn:αn) < Y(n−k+1:n)

Pr

X(αn:αn) < βY(n−k+1:n)
.
(8)
By Theorem B.3, the numerator can be approximated by (1 + α)−k while the denominaotr is approx-
imately (1 + αβ−(1+δ))−k. Thus, we have
Pr

X(αn:αn) < Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)
 ∼∼∼
(1 + αβ−(1+δ))k
(1 + α)k
=
 
1 + αβ−(1+δ)
1 + α
!k
,
19


## Page 20


and therefore
Pr

X(αn:αn) > Y(n−k+1:n)|X(αn:αn) < βY(n−k+1:n)
 ∼∼∼1 −
 
1 + αβ−(1+δ)
1 + α
!k
.
B
Additional Theorems for Power Laws
Theorem B.1.
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
∼∼∼E

X(αn:αn)


1 −(1 + c−1)−δ/(1+δ)
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j


where c = αβ−(1+δ).
Proof. First, observe that
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
= E

X(αn:αn)

−E
h
X(αn:αn) · 1X(αn:αn)≥βY(n−k+1:n)
i
.
Next, we use the fact that
E
h
X(αn:αn) · 1X(αn:αn)≥βY(n−k+1:n)
i
=
Z ∞
β
xf(αn:αn)(x)F(n−k+1:n)
x
β

dx.
We know that
Z ∞
β
xf(αn:αn)(x)F(n−k+1:n)
x
β

dx =
Z ( αn
ln n)
1/(1+δ)
β
xf(αn:αn)(x)F(n−k+1:n)
x
β

dx
+
Z ∞
( αn
ln n)
1/(1+δ) xf(αn:αn)(x)F(n−k+1:n)
x
β

dx,
(9)
and
Z ( αn
ln n)
1/(1+δ)
β
xf(αn:αn)(x)F(n−k+1:n)
x
β

dx ≤
 αn
ln n
1/(1+δ)
F(αn:αn)
 αn
ln n
1/(1+δ)
≤
 αn
ln n
1/(1+δ)
· 1
n
by Lemma D.6. The second term of (9) is
(1 + δ)αn
Z ∞
( αn
ln n)
1/(1+δ)(1 −x−(1+δ))αn−1x−(1+δ)
k−1
X
j=0
n
j
  
1 −
x
β
−(1+δ)!n−j x
β
−j(1+δ)
dx
= (1 + δ)αn
k−1
X
j=0
n
j

βj(1+δ)
Z ∞
( αn
ln n)
1/(1+δ)(1 −x−(1+δ))αn−1 
x−(1+δ)j+1
 
1 −
x
β
−(1+δ)!n−j
dx
Next, we show that for x ≥
  αn
ln n
1/(1+δ),
 
1 −
x
β
−(1+δ)!n−j
∼∼∼(1 −x−(1+δ))β1+δn−j.
20


## Page 21


We begin with
 
1 −
x
β
−(1+δ)!n−j
∼∼∼(1 −x−(1+δ))β1+δ(n−j) = (1 −x−(1+δ))β1+δn−j(1 −x−(1+δ))−j(β1+δ−1).
Note that (1 −x−(1+δ))−j(β1+δ−1) ≥1, and by Lemma D.5,
(1 −x−(1+δ))−j(β1+δ−1) = 1 + j(β1+δ −1)x−(1+δ) + O
 1
n

∼∼∼1.
because j ≤ln n. Thus, (1−x−(1+δ))β1+δn−j(1−x−(1+δ))−j(β1+δ−1) ∼∼∼(1−x−(1+δ))β1+δn−j. Therefore,
this becomes
(1 + δ)αn
k−1
X
j=0
n
j

βj(1+δ)
Z ∞
( αn
ln n)
1/(1+δ)

1 −x−(1+δ)β1+δn(1+c)−j−1 
x−(1+δ)j+1
dx.
We’ll now try to relate the jth term in this summation to the order statistic Z(β1+δn(1+c)−j:β1+δn(1+c)).
We know that
E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
=
Z ∞
1
zf(β1+δn(1+c)−j:β1+δn(1+c))(z) dz
= (1 + δ)(j + 1)
β1+δn(1 + c)
j + 1
 Z ∞
1

1 −z−(1+δ)β1+δn(1+c)−j−1 
z−(1+δ)j+1
dz.
Using this, we have
Z ∞
( αn
ln n)
1/(1+δ) xf(αn:αn)(x)F(n−k+1:n)
x
β

dx ∼∼∼
k−1
X
j=0
αnβj(1+δ) n
j

(j + 1)
 β1+δn(1+c)
j+1

h
E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
−
Z ( αn
ln n)
1/(1+δ)
1
zf(β1+δn(1+c)−j:β1+δn(1+c))(z) dz


We’ll show that this last multiplicative term is approximately E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
. Observe
that
Z ( αn
ln n)
1/(1+δ)
1
zf(β1+δn(1+c)−j:β1+δn(1+c))(z) dz
≤
 αn
ln n
1/(1+δ) Z ( αn
ln n)
1/(1+δ)
1
f(β1+δn(1+c)−j:β1+δn(1+c))(z) dz
=
 αn
ln n
1/(1+δ)
F(β1+δn(1+c)−j:β1+δn(1+c))
 αn
ln n
1/(1+δ)
≤
 αn
ln n
1/(1+δ) √
k
n
21


## Page 22


by Lemma D.3. This means
k−1
X
j=0
αnβj(1+δ) n
j

(j + 1)
 β1+δn(1+c)
j+1
E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
≥
k−1
X
j=0
αnβj(1+δ) n
j

(j + 1)
 β1+δn(1+c)
j+1

"
E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
−
 αn
ln n
1/(1+δ) √
k
n
#
∼∼∼
k−1
X
j=0
αnβj(1+δ) n
j

(j + 1)
 β1+δn(1+c)
j+1
E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
(by Lemma D.7)
Next, we deal with the nβj(1+δ) n
j

/((j + 1)
 β1+δn(1+c)
j+1

) terms. These are
nβj(1+δ) n
j

(j + 1)
 β1+δn(1+c)
j+1
 =
n(n −1) · · · (n −j + 1)
β1+δn(1 + c)(β1+δn(1 + c) −1) · · · (β1+δn(1 + c) −j + 1) ·
nβj(1+δ)
β1+δn(1 + c) −j .
(10)
Each term (n −ℓ)/(β1+δn(1 + c) −ℓ) is between 1/(β1+δ(1 + c)) and 1/(β1+δ(1 + c)) · (1 −ℓ/n). This
means
1
(β1+δ(1 + c))j ≥
jY
ℓ=0
n −ℓ
β1+δn(1 + c) −ℓ≥
jY
ℓ=0
1
β1+δ(1 + c)

1 −ℓ
n

≥

1 −j2
n

∼∼∼
1
(β1+δ(1 + c))j
since j ≤k ≤((1 −c2)/2) ln n. Multiplying by the second term in (10), which is
nβj(1+δ)
β1+δn(1 + c) −j
∼∼∼
β(j−1)(1+δ)
1 + c
,
we have
nβj(1+δ) n
j

(j + 1)
 β1+δn(1+c)
j+1
 ∼∼∼
1
β1+δ(1 + c)j+1 .
As a result,
Z ∞
( αn
ln n)
1/(1+δ) xf(αn:αn)(x)F(n−k+1:n)
x
β

dx ∼∼∼
k−1
X
j=0
α
β1+δ(1 + c)j+1 E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
=
k−1
X
j=0
c
(1 + c)j+1 E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
(11)
Finally, note that
E
h
Z(β1+δn(1+c)−j:β1+δn(1+c))
i
= E
h
Z(nβ1+δ(1+c):β1+δn(1+c))
i
Γ(j + δ/(1 + δ))
Γ(δ/(1 + δ))Γ(j + 1)
∼∼∼(β1+δn(1 + c))1/(1+δ) Γ(j + δ/(1 + δ))
Γ(j + 1)
= β(1 + c)1/(1+δ)n1/(1+δ) Γ(j + δ/(1 + δ))
Γ(j + 1)
=
β
α1/(1+δ) (1 + c)1/(1+δ)(αn)1/(1+δ) Γ(j + δ/(1 + δ))
Γ(j + 1)
∼∼∼c−1/(1+δ)(1 + c)1/(1+δ)E

X(αn:αn)

Γ(j + δ/(1 + δ))
Γ(δ/(1 + δ))Γ(j + 1)
22


## Page 23


Substituting back to (11),
Z ∞
( αn
ln n)
1/(1+δ) xf(αn:αn)(x) ∼∼∼E

X(αn:αn)

cδ/(1+δ)
k−1
X
j=0
(1 + c)−(j+δ/(1+δ))
Γ(j + δ/(1 + δ))
Γ(δ/(1 + δ))Γ(j + 1)
Going back to (9),
E
h
X(αn:αn) · 1X(αn:αn)>βY(n−k+1:n)
i
∼∼∼E

X(αn:αn)

cδ/(1+δ)
k−1
X
j=0
(1 + c)−(j+δ/(1+δ))
Γ(j + δ/(1 + δ))
Γ(δ/(1 + δ))Γ(j + 1)
+
Z ( αn
ln n)
1/(1+δ)
β
xf(αn:αn)(x)F(n−k+1:n)
x
β

dx
≤E

X(αn:αn)

cδ/(1+δ)
k−1
X
j=0
(1 + c)−(j+δ/(1+δ))
Γ(j + δ/(1 + δ))
Γ(δ/(1 + δ))Γ(j + 1)
+
 αn
ln n
1/(1+δ) (ln n)2
n
∼∼∼E

X(αn:αn)

cδ/(1+δ)
k−1
X
j=0
(1 + c)−(j+δ/(1+δ))
Γ(j + δ/(1 + δ))
Γ(δ/(1 + δ))Γ(j + 1)
Therefore,
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
∼∼∼E

X(αn:αn)


1 −cδ/(1+δ)
k−1
X
j=0
(1 + c)−(j+δ/(1+δ))
Γ

j +
δ
1+δ

Γ

δ
1+δ

Γ(j + 1)

.
We can simplify this to
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
∼∼∼E

X(αn:αn)


1 −(1 + c−1)−δ/(1+δ)
k−1
X
j=0
(1 + c)−j
Γ

j +
δ
1+δ

Γ

δ
1+δ

Γ(j + 1)

.
Using the deﬁnition
a
b

=
Γ(a + 1)
Γ(b + 1)Γ(a −b + 1),
this is
E
h
X(αn:αn) · 1X(αn:αn)<βY(n−k+1:n)
i
∼∼∼E

X(αn:αn)


1 −(1 + c−1)−δ/(1+δ)
k−1
X
j=0
j −
1
1+δ
j

(1 + c)−j

.
Theorem B.2.
E
h
Y(n−k+1:n) · 1X(αn:αn)<βY(n−k+1:n)
i
∼∼∼(1 + αβ−(1+δ))−(k−1/(1+δ))E

Y(n−k+1:n)

23


## Page 24


Proof. We begin with
E
h
Y(n−k+1:n) · 1X(αn:αn)<βY(n−k+1:n)
i
=
Z ∞
1
yf(n−k+1:n)(y)F(αn:αn)(βy) dy.
Let c = αβ−(1+δ). Break this up into
Z ∞
1
yf(n−k+1:n)(y)F(αn:αn)(βy) dy =
Z ( cn
ln n)
1/(1+δ)
1
yf(n−k+1:n)(y)F(αn:αn)(βy) dy
+
Z ∞
( cn
ln n)
1/(1+δ) yf(n−k+1:n)(y)F(αn:αn)(βy) dy.
(12)
The ﬁrst term is
Z ( cn
ln n)
1/(1+δ)
1
yf(n−k+1:n)(y)F(αn:αn)(βy) dy
≤F(αn:αn)

β
 cn
ln n
1/(1+δ) Z ( cn
ln n)
1/(1+δ)
1
yf(n−k+1:n)(y) dy
≤F(αn:αn)

β
 cn
ln n
1/(1+δ)
E

Y(n−k+1:n)

≤E

Y(n−k+1:n)

n
by Lemma D.6.
For the second term in (12), we have
Z ∞
( cn
ln n)
1/(1+δ)yf(n−k+1:n)(y)F(αn:αn)(βy) dy
= (1 + δ)k
n
k
 Z ∞
( cn
ln n)
1/(1+δ)

1 −y−(1+δ)n−k 
y−(1+δ)k 
1 −(βy)−(1+δ)αn
dy
By Lemma D.2, for all y ≥(cn/ ln n)1/(1+δ),

1 −(βy)−(1+δ)αn ∼∼∼

1 −y−(1+δ)cn
.
Therefore,
Z ∞
( cn
ln n)
1/(1+δ)yf(n−k+1:n)(y)F(αn:αn)(βy) dy
∼∼∼(1 + δ)k
n
k
 Z ∞
( cn
ln n)
1/(1+δ)

1 −y−(1+δ)n−k+cn 
y−(1+δ)k
dy
= (1 + δ)k
n
k
 Z ∞
( cn
ln n)
1/(1+δ)

1 −y−(1+δ)n(1+c)−k 
y−(1+δ)k
dy.
We’ll now try to relate this to the order statistic Z(n(1+c)−k+1:n(1+c)). We know that
E

Z(n(1+c)−k+1:n(1+c))

=
Z ∞
1
zf(n(1+c)−k+1:n(1+c))(z) dz
= (1 + δ)k
n(1 + c)
k
 Z ∞
1

1 −z−(1+δ)n(1+c)−k 
z−(1+δ)k
dz.
24


## Page 25


Using this, we have
Z ∞
( cn
ln n)
1/(1+δ)yf(n−k+1:n)(y)F(αn:αn)(βy) dy
∼∼∼
 n
k

 n(1+c)
k


E

Z(n(1+c)−k+1:n(1+c))

−
Z ( cn
ln n)
1/(1+δ)
1
yf(n(1+c)−k+1:n(1+c))(y) dy

.
(13)
From here, we’ll show that the term being subtracted is only a
√
ln n
n
fraction of E

Z(n(1+c)−k+1:n(1+c))

.
To do so, note that
Z ( cn
ln n)
1/(1+δ)
1
yf(n(1+c)−k+1:n(1+c))(y) dy ≤
 cn
ln n
1/(1+δ) Z ( cn
ln n)
1/(1+δ)
1
f(n(1+c)−k+1:n(1+c))(y) dy
=
 cn
ln n
1/(1+δ)
F(n(1+c)−k+1:n(1+c))
 cn
ln n
1/(1+δ)
≤
 cn
ln n
1/(1+δ)
 √
k
n
!
By Lemma D.1. Lemma D.7 gives us
E

Z(n(1+c)−k+1:n(1+c))

≥E

Z(n(1+c)−k+1:n(1+c))

−
Z ( cn
ln n)
1/(1+δ)
1
yf(n(1+c)−k+1:n(1+c))(y) dy
≥E

Z(n(1+c)−k+1:n(1+c))

−
 cn
ln n
1/(1+δ)
 √
k
n
!
≥E

Z(n(1+c)−k+1:n(1+c))

 
1 −
√
k
n
!
∼∼∼E

Z(n(1+c)−k+1:n(1+c))

Combining with (13), Lemma C.6 yields
Z ∞
( cn
ln n)
1/(1+δ) yf(n−k+1:n)(y)F(αn:αn)(βy) dy ∼∼∼
 n
k

 n(1+c)
k
E

Z(n(1+c)−k+1:n(1+c))

(14)
By Lemma D.8,
 n
k

 n(1+c)
k
 ∼∼∼
1
(1 + c)k .
Putting this into (14),
Z ∞
( cn
ln n)
1/(1+δ) yf(n−k+1:n)(y)F(αn:αn)(βy) dy ∼∼∼
1
(1 + c)k E

Z(n(1+c)−k+1:n(1+c))

.
25


## Page 26


Finally, note that
E

Z(n(1+c)−k+1:n(1+c))

= E

Z(n(1+c):n(1+c))
 Γ(k −1/(1 + δ))
Γ(δ/(1 + δ))Γ(k)
∼∼∼(n(1 + c))1/(1+δ) Γ(k −1/(1 + δ))
Γ(k)
= (1 + c)1/(1+δ)n1/(1+δ) Γ(k −1/(1 + δ))
Γ(k)
∼∼∼(1 + c)1/(1+δ)E

Y(n:n)
 Γ(k −1/(1 + δ))
Γ(δ/(1 + δ))Γ(k)
= (1 + c)1/(1+δ)E

Y(n−k+1:n)

Substituting into (12),
E
h
Y(n−k+1:n) · 1X(αn:αn)≤βY(n−k+1:n)
i
∼∼∼E

Y(n−k+1:n)
 
(1 + c)−(k−1/(1+δ)) + 1
n

∼∼∼E

Y(n−k+1:n)

(1 + αβ−(1+δ))−(k−1/(1+δ))
since c = aβ−1(1+δ), proving the theorem.
Theorem B.3.
Pr

X(αn:αn) < βY(n−k+1:n)
 ∼∼∼(1 + c)−k.
Proof. Begin with
Pr

X(αn:αn) < βY(n−k+1:n)

=
Z ∞
1
f(n−k+1:n)(y)F(αn:αn)(βy) dy
=
Z ( cn
ln n)
1/(1+δ)
1
f(n−k+1:n)(y)F(αn:αn)(βy) dy
+
Z ∞
( cn
ln n)
1/(1+δ) f(n−k+1:n)(y)F(αn:αn)(βy) dy
(15)
Observe that
Z ( cn
ln n)
1/(1+δ)
1
f(n−k+1:n)(y)F(αn:αn)(βy) dy ≤F(αn:αn)

β
 cn
ln n
1/(1+δ)
F(n−k+1:n)
 cn
ln n
1/(1+δ)
≤F(αn:αn)

β
 cn
ln n
1/(1+δ)
≤

1 −β−(1+δ)
ln n
cn
αn
≤exp

−αβ−(1+δ) ln n
cn

= 1
n
Next, we have
Z ∞
( cn
ln n)
1/(1+δ) f(n−k+1:n)(y)F(αn:αn)(βy) dy =
Z ∞
( cn
ln n)
1/(1+δ)(1 −(βy)−(1+δ))αnf(n−k+1:n)(y) dy
26


## Page 27


By Lemma D.2, for y ≥(cn/ ln n)1/(1+δ),

1 −(βy)−(1+δ)αn ∼∼∼

1 −y−(1+δ)cn
,
so
Z ∞
( cn
ln n)
1/(1+δ)f(n−k+1:n)(y)F(αn:αn)(βy) dy
∼∼∼
Z ∞
( cn
ln n)
1/(1+δ)(1 −y−(1+δ))cnf(n−k+1:n)(y) dy
= (1 + δ)k
n
k
 Z ∞
( cn
ln n)
1/(1+δ)(1 −y−(1+δ))n(1+c)−k(y−(1+δ))ky−1 dy
=
 n
k

 n(1+c)
k

Z ∞
( cn
ln n)
1/(1+δ) f(n(1+c)−k+1:n(1+c)) dy
From Lemma D.1, we have
F(n(1+c)−k+1:n(1+c))
 cn
ln n
1/(1+δ)
≤
√
k
n ,
so
Z ∞
( cn
ln n)
1/(1+δ) f(n(1+c)−k+1:n(1+c)) dy = 1 −F(n(1+c)−k+1:n(1+c))
 cn
ln n
1/(1+δ)
≥1 −
√
k
n
≈1.
Therefore,
Z ∞
( cn
ln n)
1/(1+δ) f(n−k+1:n)(y)F(αn:αn)(βy) dy ∼∼∼
 n
k

 n(1+c)
k
 ∼∼∼
1
(1 + c)k
by Lemma D.8. By (15), this means
Pr

X(αn:αn) < βY(n−k+1:n)
 ∼∼∼(1 + c)−k.
C
Lemmas for the Equivalence Deﬁnition
Lemma C.1 (Transitivity). If f(n) ∼∼∼a1;n1 g(n) and g(n) ∼∼∼a2;n2 h(n), then f(n) ∼∼∼h(n).
Proof.
f(n)
h(n) = f(n)
g(n) · g(n)
h(n)
≤

1 + a1(ln n)2
n
 
1 + a2(ln n)2
n

≤1 + (a1 + a2)(ln n)2
n
+ a1a2(ln n)4
n2
≤1 + (a1 + a2 + a1a2)(ln n)2
n
27


## Page 28


for all n ≥max(n1, n2), since n ≥(ln n)2.
A symmetric argument holds for h(n)/f(n).
Thus,
f(n) ∼∼∼a1+a2+a1a2;max(n1,n2) h(n).
Lemma C.2 (Linearity). If f1(n) ∼∼∼a1;n1 g1(n) and f1(n) ∼∼∼a2;n2 g2(n), then bf1(n) + cf2(n) ∼∼∼
bg1(n) + cg2(n).
Proof. By Lemma C.7,
bf1(n) + cf2(n)
bg1(n) + cg2(n) ≤max
f1(n)
g1(n), f2(n)
g2(n)

≤max(a1, a2)(ln n)2
n
for n ≥max(n1, n2). A symmetric argument holds for the reciprocal. Therefore,
bf1(n) + cf2(n) ∼∼∼max(a1,a2);max(n1,n2) bg1(n) + cg2(n).
Lemma C.3 (Integrals). If f(x, n) ∼∼∼a;n0 g(x, n), then
Z
f(x, n) dx ∼∼∼
Z
g(x, n) dx
Proof.
R
f(x, n) dx
R
g(x, n) dx =
R
g(x, n)f(x,n)
g(x,n) dx
R
g(x, n) dx
≤
R
g(x, n)

1 + a(ln n)2
n

dx
R
g(x, n) dx
≤1 + a(ln n)2
n
for n ≥n0. A symmetric argument holds for the repciprocal, proving the lemma.
Lemma C.4. If f1(n) ∼∼∼a1;n1 g1(n) and f2(n) ∼∼∼a2;n2 g2(n), then
f1(n)f2(n) ∼∼∼g1(n)g2(n).
Proof.
f1(n)f2(n)
g1(n)g2(n) = f1(n)
g1(n) · f2(n)
g2(n)
≤

1 + a1(ln n)2
n
 
1 + a2(ln n)2
n

≤1 + (a1 + a2)(ln n)2
n
+ a1a2(ln n)4
n2
≤1 + (a1 + a2 + a1a2)(ln n)2
n
for all n ≥max(n1, n2), since n ≥(ln n)2. A symmetric argument holds for the reciprocal. Thus,
f1(n)f2(n) ∼∼∼a1+a2+a1a2;max(n1,n2) g1(n)g2(n).
Lemma C.5. If f(n) ∼∼∼a;n0 g(n), then
1
f(n) ∼∼∼
1
g(n).
28


## Page 29


Proof.
1/f(n)
1/g(n) = g(n)
f(n) ≤1 + a(ln n)2
n
for n ≥n0. A symmetric argument holds for the reciprocal.
Lemma C.6. If g1(n) ≤f(n) ≤g2(n), g1(n) ∼∼∼h(n), and g2(n) ∼∼∼h(n), then f(n) ∼∼∼h(n).
Proof.
f(n)
h(n) ≤g2(n)
h(n)
and
h(n)
f(n) ≤h(n)
g1(n),
proving the lemma by deﬁnition.
Fact 4. For all x ≥1, ln x ≤x and (ln x)2 ≤x.
Lemma C.7. For a, b, c, d > 0, if a
b ≤c
d, then
a
b ≤a + c
b + d ≤c
d.
Proof. Since a
b ≤c
d, d
b ≤c
a. Therefore,
a + c
b + d = a
b · 1 + c/a
1 + d/b ≥a
b · 1 + d/b
1 + d/b = a
b .
Similarly,
a + c
b + d = c
d · 1 + a/c
1 + b/d ≤c
d · 1 + b/d
1 + b/d = c
d.
Lemma C.8.
a −(ln n)2/n
b
∼∼∼
a
b
Proof.
a−(ln n)2/n
b
a
b
= 1 −(ln n)2
n
≤1
a
b
a−(ln n)2/n
b
=
1
1 −(ln n)2
an
= 1 +
(ln n)2
an
1 −(ln n)2
an
≤1 + 2(ln n)2
an
for n ≥16/a4.
29


## Page 30


D
Lemmas for Appendix B
Lemma D.1. For k ≤(1 −c) ln n,
F(n(1+c)−k+1:n(1+c))
 cn
ln n
1/(1+δ)
≤
√
k
n .
Proof. We can write
F(n(1+c)−k+1:n(1+c))
 cn
ln n
1/(1+δ)
=
k−1
X
j=0
n(1 + c)
j
 
1 −ln n
cn
n(1+c)−j ln n
cn
j
≤
k−1
X
j=0
(n(1 + c))j
j!
exp

−
ln n
cn

(n(1 + c) −j)
 ln n
cn
j
=
k−1
X
j=0
1
j!
(1 + c) ln n
c
j
exp

−ln n

1 + c−1

1 −j
n

= 1
n
k−1
X
j=0
1
j!
 (1 + c−1) ln n
j
 1
n
c−1(1−j
n)
≤1
n2 + 1
n
k−1
X
j=1
1
√2πj
e(1 + c−1) ln n
j
j  1
n
c−1(1−j
n)
(16)
by Stirling’s approximation. The term
e(1 + c−1) ln n
j
j
is increasing whenever it’s natural log,
j
 1 + ln(1 + c−1) + ln ln n −ln j

,
is increasing. This has derivative
1 + ln(1 + c−1) + ln ln n −ln j −1 = ln(1 + c−1) + ln ln n −ln j ≥ln ln n −ln j.
Thus, it is increasing for j ≤ln n. For j ≤(1 −c) ln n, we have
e(1 + c−1) ln n
j
j
≤
e(1 + c−1) ln n
(1 −c) ln n
(1−c) ln n
=
e(1 + c−1)
1 −c
(1−c) ln n
= exp
 1 + ln(1 + c−1) −ln(1 −c)
(1−c) ln n
= exp (ln n)(1+ln(1+c−1)−ln(1−c))(1−c)
= n(1+ln(1+c−1)−ln(1−c))(1−c)
≤n(1+c−1+c+c2)(1−c)
= n1+c−1+c+c2−c−1−c2−c3
= nc−1−c3
≤nc−1(1−j/n)
30


## Page 31


for suﬃciently large n, since j ≤(1 −c) ln n. Combining this with (16), we have
F(n(1+c)−k+1:n(1+c))
 cn
ln n
1/(1+δ)
≤1
n2 +
1
n
√
2π
k−1
X
j=1
1
√j
≤1
n2 +
1
n
√
2π

1 +
Z k
1
1
√j dj

≤1
n2 +
√
k
n
√
2π
≤
√
k
n
Lemma D.2. For y ≥(cn/ ln n)1/(1+δ),

1 −(βy)−(1+δ)αn ∼∼∼

1 −y−(1+δ)cn
,
Proof. We know that 1 −(βy)−(1+δ) ≥(1 −y−(1+δ))β−(1+δ) from the Taylor expansion, giving us

1 −(βy)−(1+δ)αn
≥

(1 −y−(1+δ))β−(1+δ)αn
= (1 −y−(1+δ))cn.
On the other hand, for y ≥(cn/ ln n)1/(1+δ),

1 −(βy)−(1+δ)αn
≤exp

−cy−(1+δ)n

≤
 1 −y−(1+δ)cn
1 −cny−2(1+δ) ≤
 1 −y−(1+δ)cn
1 −(ln n)2
cn
∼∼∼

1 −y−(1+δ)cn
.
Lemma D.3. For k ≤((1 −c2) ln n)/2,
F(β1+δn(1+c)−j:β1+δn(1+c))
 αn
ln n
1/(1+δ)
≤
√
k
n ,
Proof. We begin with
F(β1+δn(1+c)−j:β1+δn(1+c))
 αn
ln n
1/(1+δ)
=
j
X
ℓ=0
β1+δn(1 + c)
ℓ
 
1 −ln n
αn
β1+δn(1+c)−ℓln n
αn
ℓ
≤
j
X
ℓ=0
(β1+δn(1 + c))ℓ
ℓ!
exp

−
ln n
αn

(β1+δn(1 + c) −ℓ)
 ln n
αn
ℓ
=
j
X
ℓ=0
1
ℓ!
β1+δ(1 + c) ln n
c
ℓ
exp

−ln n

1 + c−1

1 −ℓ
n

= 1
n
j
X
ℓ=0
1
ℓ!

β1+δ(1 + c−1) ln n
ℓ 1
n
c−1(1−ℓ
n)
≤1
n2 + 1
n
j
X
ℓ=1
1
√
2πℓ
eβ1+δ(1 + c−1) ln n
ℓ
ℓ 1
n
c−1(1−ℓ
n)
(17)
31


## Page 32


We apply a similar argument as in Lemma D.1, showing that for ℓ≤((1 −c2)/2) ln n,
eβ1+δ(1 + c−1) ln n
ℓ
ℓ
≤
ec−1(1 + c−1) ln n
(1 −c) ln n
((1−c2)/2) ln n
=
ec−1(1 + c−1)
1 −c
(1−c) ln n
= exp
 1 + ln c−1 + ln(1 + c−1) −ln(1 −c)
((1−c2)/2) ln n
= exp (ln n)(1+ln c−1+ln(1+c−1)−ln(1−c))((1−c2)/2)
= n(1+ln c−1+ln(1+c−1)−ln(1−c))((1−c2)/2)
≤n(1+(c−1−1)+c−1+c+c2)((1−c2)/2)
= n(2c−1+c+c2)((1−c2)/2)
≤n(2c−1+2c)((1−c2)/2)
(c ≤1)
= nc−1(1+c2)(1−c2)
= nc−1(1−c4)
≤nc−1(1−ℓ/n)
for suﬃciently large n. This gives us
F(β1+δn(1+c)−j:β1+δn(1+c))
 αn
ln n
1/(1+δ)
≤1
n2 + 1
n
j
X
ℓ=1
1
√
2πℓ
≤
√
k
n ,
Lemma D.4. For 0 < a < b and c > 0,
a + c
b + c > a
b
Proof.
a + c
b + c = a(1 + c/a)
b(1 + c/b) > a(1 + c/b)
b(1 + c/b) = a
b
Lemma D.5. For 0 ≤y ≤a1 · ln n
n
and |z| ≤a2 ln n,
|(1 −y)z −(1 −yz)| = O
 1
n

Proof. By Taylor’s theorem,
f(y) = (1 −y)z = 1 −yz ± f′′(ε)
2
y2
for some 0 ≤ε ≤y. Note that
f′′(ε) = z(z −1)(1 −ε)z−2 ≤|z(z −1)| exp(−ε(z −2)) ≤|z(z −1)| exp(ε|z −2|).
32


## Page 33


Since ε ≤y ≤a1 · ln n
n
and |z| ≤a2 ln n,
|z(z −1)| exp(ε|z −2|) ≤a2
2(ln n)2n−2na1|z−2|/n.
This gives us
f′′(ε)
2
y2 ≤a2
2(ln n)2n−2na1|z−2|/n
2
a2
1(ln n)2n−2 ≤a2
1a2
2(ln n)4n−(2−a1(a2 ln n+2)/n).
Using ln n = nln ln n/ ln n, this is
a2
1a2
2
n n−(1−a1(a2 ln n+2)/n−4 ln ln n/ ln n).
For suﬃciently large n, a1(a2 ln n + 2)/n + 4 ln ln n/ ln n ≤1, so
a2
1a2
2
n n−(1−a1(ln n+2)/n−4 ln ln n/ ln n) ≤a2
1a2
2
n
= O(1/n),
which proves the lemma.
Lemma D.6.
F(an:an)

b
 cn
ln n
1/(1+δ)
≤n−ab−(1+δ)/c
Proof.
F(an:an)

b
 cn
ln n
1/(1+δ)
=

1 −b−(1+δ) ln n
cn
an
≤exp
 
−ab−(1+δ)
c
ln n
!
= n−ab−(1+δ)/c
Lemma D.7.
E

Z(Cn−ln n+1:Cn)

≥
 Cn
ln n
1/(1+δ)
for C ≥1 and suﬃciently large n.
33


## Page 34


Proof.
E

Z(Cn−ln n+1:Cn)

= E

Z(Cn:Cn)
 ln n−1
Y
j=1

1 −
1
(1 + δ)j

= E

Z(Cn:Cn)
 ln n−1
Y
j=1
(1 + δ)j −1
(1 + δ)j

= E

Z(Cn:Cn)
 ln n−1
Y
j=1
j −1/(1 + δ)
j

= E

Z(Cn:Cn)
 Γ(ln n −1/(1 + δ))
Γ(δ/(1 + δ))Γ(ln n)
≥Γ

δ
1 + δ

(Cn)1/(1+δ) Γ(ln n −1/(1 + δ))
Γ(δ/(1 + δ))Γ(ln n)
(by Lemma D.10)
= (Cn)1/(1+δ) Γ(ln n −1/(1 + δ))
Γ(ln n)
≥
 Cn
ln n
1/(1+δ)  
1 +
1
1+δ · 1+2δ
1+δ
ln n
−O

1
(ln n)2
!
(by [20])
≥
 Cn
ln n
1/(1+δ)
(for suﬃciently large n)
Lemma D.8. For k = O(ln n),
 n
k

 n(1+c)
k
 ∼∼∼
1
(1 + c)k .
Proof.
 n
k

 n(1+c)
k
 =
n(n −1) · · · (n −k + 1)
n(1 + c)(n(1 + c) −1) · · · (n(1 + c) −k + 1).
Each term (n −j)/(n(1 + c) −j) is between 1/(1 + c) and (1 −j/n)/(1 + c). Therefore, the entire
product is at least
k−1
Y
j=0
1
1 + c

1 −j
n

=
1
(1 + c)k
k−1
Y
j=0

1 −j
n

≥
1
(1 + c)k

1 −k2
n

and at most 1/(1 + c)k. This means that
1
(1 + c)k ≥
 n
k

 n(1+c)
k
 ≥
1
(1 + c)k

1 −(ln n)2
n

∼∼∼
1
(1 + c)k
Lemma D.9. For 0 < z < 1, and y ≥0,
(1 + y)z < 1 + yz.
34


## Page 35


Proof. Let w = z−1. Then, the lemma is true if and only if for w > 1,
1 + y <

1 + y
w
w
.
Note that for w = 1, we have equality. We will show that the function
f(w) =

1 + y
w
w
has nonnegative derivative for w ≥1. This is equivalent to showing the same for its log, which is
d
dw log f(w) = d
dww log

1 + y
w

= log

1 + y
w

+
w
1 + y
w
·

−y
w2

= log

1 + y
w

−
y
w
1 + y
w
Let x = 1 + y
w. Then, the lemma is true if for x > 1,
log(x) −x −1
x
> 0
x log(x) > x −1
Both are 0 at x = 1, but the left hand side has derivative 1 + log(x) while the right hand side has
derivative 1, so left hand side will be strictly larger than the right hand side for x > 1.
Lemma D.10.
E

Z(m:m)
 ∼∼∼Γ

δ
1 + δ

m1/(1+δ).
Also,
E

Z(m:m)

≥Γ

δ
1 + δ

m1/(1+δ).
Proof. From [17], we have
E

Z(m:m)

=
Γ(m + 1)Γ

1 −
1
1+δ

Γ

m +
δ
1+δ

.
By [20],
Γ(m + 1)
Γ

m +
δ
1+δ
 = m1/(1+δ)

1 +

1
1+δ
 
δ
1+δ

2m
+ O
 1
m2

≥m1/(1+δ)
This means
Γ

δ
1 + δ

m1/(1+δ) ≤E

Z(m:m)

≤Γ

δ
1 + δ

m1/(1+δ)

1 + O
 1
n

,
so
Γ

δ
1 + δ

m1/(1+δ) ∼∼∼E

Z(m:m)

.
Lemma D.11 ([17], Formula 1).
E

Z(m−k:m)

=

1 −
1
k(1 + δ)

E

Z(m−k+1:m)

35


## Page 36


E
Lemmas and Proofs for Section 3
Proof of Theorem 3.1. To proceed, we need some notation.
Let L be the event that X(n−1:n) ≥
T ∩Y(n−1:n) ≥T (the samples are “large”). Let G be the event that b(X(n:n)) < Y(n−1:n), meaning
G is the event that the policy has an eﬀect. Let D be the random variable X(n:n) −Y(n−1:n). We
want to show that E [D|G] > 0. To do so, we observe that by Lemma E.1, is suﬃcient to show that
E [D|L] >
Pr[L]
Pr[L] . By Lemma E.2, we know that Pr

L

≤2nF(T)n−1. To complete the proof, we need
to show that E [D|L] is large, which we do via Lemma E.3.
Since Pr [L] ≥1 −2nF(T)n−1, there exists N1 such that for all n ≥N1, Pr [L] ≥1/2. Using
Lemma E.3, if n ≥N1, it is suﬃcient to have
E [D|L] > Pr

L

1
2
K(F(T) + η)n−1 > 4nF(T)n−1

1 +
η
F(T)
n
> 4n
K
n log

1 +
η
F(T)

> log n + log
 4
K

√n log

1 +
η
F(T)

> 2
(n ≥4/K, using √n > log n)
n > 4

log

1 +
η
F(T)
−2
= N2
Thus, for n > max{N1, N2, 4/K}, E [D|L] >
Pr[L]
Pr[L] , which by Lemma E.3 implies that E [D|G] > 0.
This completes the proof of Theorem 3.1.
Lemma E.1. If L ⇒G and D ≥−1, then E [D|L] >
Pr[L]
Pr[L] implies E [D|G] > 0.
Proof.
E [D|G] = E [D · 1L|G] + E

D · 1L|G

= E [D · 1L · 1G] + E

D · 1L · 1G

Pr [G]
= E [D · 1L] + E

D · 1L · 1G

Pr [G]
(L ⇒G)
≥E [D · 1L] −E

1L · 1G

Pr [G]
(D ≥−1)
≥E [D · 1L] −E

1L

Pr [G]
(1G ≤1)
= E [D|L] Pr [L] −Pr

L

Pr [G]
36


## Page 37


E [D|L] Pr [L] −Pr

L

Pr [G]
> 0
⇐⇒E [D|L] Pr [L] −Pr

L

> 0
⇐⇒E [D|L] > Pr

L

Pr [L]
Lemma E.2. For X(n−1:n), Y(n−1:n) order statistics from a distribution with support on [0, 1],
Pr

X(n−1:n) ≥T ∩Y(n−1:n) ≥T

≤2nF(T)n−1.
Proof.
Pr

X(n−1:n) ≥T ∩Y(n−1:n) ≥T

= Pr

X(n−1:n) ≥T

Pr

Y(n−1:n) ≥T

= (1 −F(n−1)(T))2
= (1 −nF(T)n−1(1 −F(T)) −F(T)n)2
= (1 −nF(T)n−1 + (n −1)F(T)n)2
≥(1 −nF(T)n−1)2
≥1 −2nF(T)n−1
Pr

L

= 1 −Pr [L] ≤2nF(T)n−1
Lemma E.3. There exist constants η > 0 and K > 0 such that E [D|L] ≥K(F(T) + η)n−1
Proof. First, let fZ and FZ be the pdf and cdf respectively of Y |Y ≥T, i.e. FZ(x) = F(x)−F(T)
1−F(T)
and
fZ = F ′
Z. Note that
E [D|L] = E

X(n:n) −Y(n−1:n)|L

= E

X(n:n)|X(n−1:n) ≥T

−E

Y(n−1:n)|Y(n−1:n) ≥T

= E

Y(n:n)|Y(n−1:n) ≥T

−E

Y(n−1:n)|Y(n−1:n) ≥T

= E

Y(n:n) −Y(n−1:n)|Y(n−1:n) ≥T

Let M be a random variable corresponding to the number of samples from Y1, . . . , Yn that are larger
than T. We can rewrite this as
E [D|L] =
M
X
m=2
E

Y(n:n) −Y(n−1:n)|Y(n−1:n) ≥T, M = m

Pr

M = m|Y(n−1:n) ≥T

=
M
X
m=2
E

Y(n:n) −Y(n−1:n)|M = m

Pr

M = m|Y(n−1:n) ≥T

(M ≥2 =⇒Y(n−1:n) ≥T)
Conditioning on M = m, Y(n:n) and Y(n−1:n) have the same distributions as Z(m:m) and Z(m−1:m)
respectively, where Z(k:m) is the kth order statistic of random variables Z1, Z2, . . . , Zm drawn from the
37


## Page 38


distribution with cdf FZ. We will use FZ,(k:m) to denote the cdf of Z(k:m). Thus, E

Y(n:n) −Y(n−1:n)|M = m

=
E

Z(m:m) −Z(m−1:m)

. Using an analysis similar to that of [16],
E

Z(m:m) −Z(m−1:m)

=
Z 1
T
(1 −FZ,(m:m)(x)) −(1 −FZ,(m−1:m)(x)) dx
=
Z 1
T
FZ,(m−1:m) −FZ,(m:m)(x) dx
=
Z 1
T

m
m −1

FZ(x)m−1(1 −FZ(x)) dx
≥
Z 1
T
FZ(x)m−1(1 −FZ(x)) dx
Choose η ∈(0, 1 −F(T)) and η′ ∈(η, 1 −F(T)). Let r = F −1
Z (F(T) + η) and r′ = F −1
Z (F(T) + η′).
Note that T < r < r′ < 1 because otherwise FZ would have inﬁnite slope at r or r′, which is impossible
because fZ is continuous over a compact set and therefore has a ﬁnite maxmium. Moreover, it must
be the case that F(T) < 1 because by assumption, supx:f(x)>0 = 1. If F(T) were 1, this would imply
that supx:f(x)>0 = T < 1, which is a contradiction.
Z 1
T
FZ(x)m−1(1 −FZ(x)) dx ≥
Z 1
r
FZ(x)m−1(1 −FZ(x))
≥
Z 1
r
FZ(r)m−1(1 −FZ(x))
= (F(T) + η)m−1
Z 1
r
1 −FZ(x) dx
≥(F(T) + η)n−1
Z 1
r
1 −FZ(x) dx
≥(F(T) + η)n−1
Z r′
r
1 −FZ(x) dx
≥(F(T) + η)n−1
Z r′
r
1 −FZ(r′) dx
(FZ(x) ≤FZ(r′) for x ≤r′)
= (F(T) + η)n−1(r′ −r)(1 −(F(T) + η′))
= (F(T) + η)n−1[F −1
Z (F(T) + η′) −F −1
Z (F(T) + η)](1 −F(T) −η′)
= K(F(T) + η)n−1
where K = [F −1
Z (F(T)+η′)−F −1
Z (F(T)+η)](1−F(T)−η′). Since this is independent of m, we have
E [D|L] =
n
X
m=2
E

Y(n:n) −Y(n−1:n)|M = m

Pr

M = m|Y(n−1:n) ≥T

≥
n
X
m=2
K(F(T) + η)n−1 Pr

M = m|Y(n−1:n) ≥T

= K(F(T) + η)n−1
38

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1802.06721v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1802.06721v2_Segregation_in_Religion_Networks

> Source: 1802.06721v2_Segregation_in_Religion_Networks.pdf

> Pages: 11

---


## Page 1


arXiv:1802.06721v2  [physics.soc-ph]  21 Feb 2018
1
Segregation in Religion Networks
Jiantao Hu1, Qian-Ming Zhang2, Tao Zhou1,2,§
1 CompleX Lab, University of Electronic Science and Technology of China, Chengdu 611731, People’s
Republic of China
2 Big Data Research Center, University of Electronic Science and Technology of China, Chengdu
611731, People’s Republic of China
Corresponding to: § zhutou@ustc.edu
Religious beliefs could facilitate human cooperation [1–6], promote civic engagement
[7–10], improve life satisfaction [11–13] and even boom economic development [14–16]. On
the other side, some aspects of religion may lead to regional violence, intergroup conﬂict
and moral prejudice against atheists [17–23].
Analogous to the separation of races [24],
the religious segregation is a major ingredient resulting in increasing alienation, misunder-
standing, cultural conﬂict and even violence among believers of diﬀerent faiths [18, 19, 25].
Thus far, quantitative understanding of religious segregation is rare.
Here we analyze a
directed social network extracted from weibo.com (the largest directed social network in
China, similar to twitter.com), which is consisted of 6875 believers in Christianism, Bud-
dhism, Islam and Taoism. This religion network is highly segregative, with only 1.6% of
links connecting individuals in diﬀerent religions.
Comparative analysis shows that the
extent of segregation for diﬀerent religions is much higher than that for diﬀerent races and
slightly higher than that for diﬀerent political parties. The few cross-religion links play a
critical role in maintaining network connectivity, being remarkably more important than
links with highest betweennesses [26] or bridgenesses [27]. Further content analysis shows
that 46.7% of these cross-religion links are probably related to charitable issues. Our ﬁnd-
ings provide quantitative insights into religious segregation and valuable clues to encourage
cross-religion communications.
Religion is considered as a notable origin of interpersonal relations, as well as an eﬀective and eﬃcient
tool to organize a huge number of people towards some challenging targets. At the same time, a believer
prefers to make friend with other people of the same faith, and thus people of diﬀerent faiths tend to


## Page 2


2
form isolated and homogeneous communities [28]. Such religious segregation highly inﬂuences (usually
negatively) culture evolution, economic development, political pattern, and so on [29,30]. For example,
in addition to the prejudice against atheists [20–23], religious segregation results in increasing conﬂict
and prejudice between religions [18,31,32].
kout
100
101
102
103
p(kout  )
10-4
10-3
10-2
10-1
100
Religion Network
Į =2.93
kin
100
101
102
103
p(kin)
10-4
10-3
10-2
10-1
100
Religion Network
Į =2.47
(b)
(c)
(a)
Christianism
Buddhism
Islam
Taosim
Figure 1. Structure of the religion network. (a), Structural layout of the network neglecting the
directions of links, where blue, orange, green and red nodes denote Christians, Buddhists, Islamists and
Taoists, respectively. (b), The out-degree distribution in a log-log plot, with an estimated power-law
exponent α ≈2.93. (c), The in-degree distribution in a log-log plot, with an estimated power-law
exponent α ≈2.47.
To quantitatively understand the extent of segregation, we extract a subgraph G (V, E) from weibo.com,
where V and E denote the sets of nodes and links, respectively. Introduction about weibo.com and de-
tailed description of data preparation are shown in Supplementary Note 1. The node set V contains 6875
believers in four major religions in China, including 3153 Christians, 2791 Buddhists, 470 Islamists and
461 Taoists. The link set contains 76678 directed links, and the average degree is 11.15. Figure 1(a)
presents a visual layout of the network, from which one can see clearly that connections inside a religion
are dense while connections in-between diﬀerent religions are much sparser. As shown in Figure 1(b)
and Figure 1(c), both out-degree and in-degree distributions are approximately power-law, as p(k) ∼k−α
where k denotes the degree and α is the power-law exponent. The power-law exponents, estimated by the
maximum likelihood method [33], are α ≈2.93 and α ≈2.47 for out-degree and in-degree distributions,


## Page 3


3
Table 1. Mixing matrix of the religion network.
Religion
Christianism
Buddhism
Islam
Taoism
ai
Christianism
0.5594303
0.0028952
0.00010433
0.0002739
0.56270373
Buddhism
0.0017606
0.2971778
0.000091291
0.0048254
0.303855091
Islam
0.0001956
0.0005999
0.05676987
0.0001304
0.05769577
Taoism
0.0001695
0.0046167
0.000013042
0.070946
0.075745242
bi
0.561556
0.3052896
0.056978533
0.0761757
The number in ith row and jth column represent eij, the fraction of links from religion i to religion j.
respectively. Induced subgraph for each religion also exhibits scale-free property [34] (see Supplemen-
tary Figure S1), indicating the existence of leaders (with large in-degree) and enthusiasts (with large
out-degree).
Neglecting the directions of links, we can obtain an undirected version G′ (V, E′) from G, where
two nodes i and j are connected if either there is a link from i to j or there is a link from j to i.
In G′, there is in total 64712 links. G′ displays clustering feature as indicated by its high clustering
coeﬃcient [35] C = 0.37, and community structure with a high modularity [36] Q = 0.57 if we directly
treat individuals in one religion as one community. However, neither clustering coeﬃcient nor modularity
is enough to characterize the aggregation of believers in the same religion or the segregation of believers
in diﬀerent religions, since the former only considers local organization and the latter is very sensitive to
the community sizes [37]. Accordingly, we look into the detailed mixing pattern of the religion network.
Denote eij the fraction of links from religion i to religion j (i, j = 1, 2, 3, 4), ai = P
j
eij the fraction
of links from religion i, and bj = P
i
eij the fraction of links pointing to religion j, the corresponding
mixing matrix is shown in Table 1. Obviously, the religion network is highly assortative, with most links
connecting believers in the same religion. In fact, only 1.6% links are connecting believers of diﬀerent
faiths. We further calculate the assortativity coeﬃcient r [38] which lies in [-1,1] with r = 1 at the perfect
assortative mixing (see Methods). The assortativity coeﬃcient of the religion network is surprisingly high,
as r = 0.973. In comparison, it is even higher than some well-known social networks with remarkable
segregation, such as sexual partnerships mixed by races [39] (r = 0.621) and Twitter web of politicians
in democratic party and republican party [40] (r = 0.953).
We further compare the mixing matrix of the religion network G with its randomized counterpart
Gnull, which is obtained by the degree-preserved link-rewiring process [41] (see Methods). The mixing
matrix of the null network is shown in Supplementary Table S1. We deﬁne the connecting ratio from


## Page 4


4
Table 2. Connecting ratios of the religion network to the null network.
Religion
Christianism
Buddhism
Islam
Taoism
Christianism
1.7748355
0.0169946
0.00319361
0.0061584
Buddhism
0.010329
3.1417345
0.00538876
0.2206321
Islam
0.0059429
0.0339985
18.8441558
0.0316456
Taoism
0.0039442
0.2034483
0.00299401
12.420091
The number in ith row and jth column represent the ratio of links from religion i to
religion j in the religion network to those in the null network.
religion i to religion j of G to Gnull as ρij = eij/enull
ij , where enull
ij
is the fraction of links from religion i
to religion j (i, j = 1, 2, 3, 4) in the null network. Table 2 shows such ratios, from which one can observe
two remarkable phenomena: (i) Believers statistically tend to connect with others of the same faith as
indicated by ∀i, ρii > 1, while Islam and Taoism exhibit the highest level of homophily with ρ33 = 18.84
and ρ44 = 12.42; (ii) The ratios associated with Buddhism, say ρ2• and ρ•2, are all the largest one in
corresponding rows and columns excluded the diagonal elements, indicating that Buddhism plays the key
role in cross-religion communications in China.
0k
3k
0k
3k
0k
3k
6k
9k
12k
15k
18k
21k
0k
3k
6k
9k
12k
15k
18k
21k
24k
27k
30k
33k
0
0.2
0.4
0.6
0.8
1
Rgc
Cross edge
Betweenness
Bridgeness
Degree
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
ȡr
0
500
1000
1500
S
(a)
(b)
Figure 2. Quantifying the signiﬁcance of cross-religion links in maintaining network
connectivity.
(a), Circular plot of links within and between religions, with links’ directions being
neglected. Inter-religion links are all colored in light colors to emphasize cross-religion links. (b), Link
percolation processes by gradually remove cross-religion links in a random order (black circles), links
with largest betweennesses (red squares), links with largest bridgenesses (blue triangles), and links with
highest degrees (green diamonds), respectively. The upper and lower plots show the changes of giant
component size and normalized susceptibility as the increase of the fraction of removed links.
As indicated by the structural statistics, a tiny number of cross-religion links (i.e., links connecting
individuals in diﬀerent religions, see ﬁgure 2(a) for visualization) play a critical role in maintaining the
global connectivity of the religion network. To quantify the signiﬁcance of cross-religion links, we apply


## Page 5


5
the link percolation dynamics [42], where links are ranked by a certain criterion and then removed one
by one in order.
For convenience, we consider the undirected version G′, wherein there are in total
1124 cross-religion links. The global connectivity is intuitively measured by the ratio of nodes in the
giant component (i.e., the largest connected component) to the total number of nodes N, denoted by
RGC. Increasing ρr, the fraction of links being removed, the percolation dynamics may come across a
phase transition where the network suddenly breaks into many small fragments at the corresponding
critical point, accompanied by a sharp drop of RGC. To precisely locate the critical point ρc
r, we adopt
the normalized susceptibility eS=
P
s<smax
nss2
N
[43], where ns denotes the number of components with size
s. If there is a percolation phase transition, an obvious peak in the eS(ρr) curve can be observed that
corresponds to the critical point ρc
r, at which the network disintegrates. A set of links whose removal
leads to faster decay of RGC and smaller value of ρc
r is considered to be more signiﬁcant in maintaining
the network connectivity.
We compare the following four methods in identifying signiﬁcant links for connectivity maintaining:
(i) Removing the 1124 cross-religion links in a random order; (ii) Removing links in a descending order
of their betweennesses [26]; (iii) Removing links in a descending order of their bridgenesses [27]; (iv)
Removing links in a descending order of their degrees [44].
The explicit deﬁnitions of betweenness,
bridgeness and degree for an arbitrary link are presented in Methods. As shown in ﬁgure 2(b), as the
increasing of ρr, RGC decreases much faster when removing cross-religion links ﬁrst. Remarkable peaks
are observed only for the cross-religion links and the largest-betweenness-ﬁrst method, while the critical
point of the former (ρc
r = 1119) is one order of magnitude smaller than that of the latter (ρc
r = 14956). In a
word, cross-religion links play a remarkably more signiﬁcant role in maintaining the network connectivity
than links with highest betweennesses, bridgenesses or degrees.
To uncover the underlying mechanism in the creation of cross-religion links, we classify all nodes into 4
types: (i) nodes not associated with any cross-religion links, (ii) nodes associated with some cross-religion
out-links but none of cross-religion in-links, (iii) nodes associated with some cross-religion in-links but
none of cross-religion out-links, and (iv) nodes associated with both cross-religion out-links and in-links.
Table 3 shows the distribution of nodes of diﬀerent types in diﬀerent religions, as well as the average
out-degree and in-degree over nodes of diﬀerent types. Obviously, nodes without any cross-religion links
are statistically of smaller degrees than the entire average, while nodes following or being followed by
believers of other faiths are generally of higher out-degrees or in-degrees. In particular, the ones being


## Page 6


6
Table 3. Distribution and average degrees of nodes in diﬀerent types.
Type1
Type2
Type3
Type4
Christianism
2930
153
61 (1)
9 (1)
Buddhism
2475
170
78 (24)
68 (6)
Islam
417
41
5 (0)
7 (0)
Taoism
271
109
42 (0)
39 (1)
Average out-degree
9.1674
25.0085
22.7366
38.7236
Average in-degree
6.7857
9.3002
134.3978
48.2602
In each illustration plot, the black node is the ego under consideration and the white node(s) is (are) its
neighbor(s). The ﬁrst four rows show the distribution of nodes of diﬀerent types in diﬀerent religions. The
numbers in the brackets denote the number of charitable nodes. The average degree of the religion network is
11.15.
followed by but having not followed believers of other faiths (i.e., Type 3) are usually very popular, with
average in-degree more than 10 times larger than the entire average. We further look into the personal
descriptions and posted microblogs of nodes of type 3 and type 4. There are in total 309 nodes of type 3
or type 4, each of which has attracted at least one believer from another religion. By content analysis (see
Supplementary Note 2), we found 33 charitable nodes who introduce themselves as charity contributors
and/or representatives/members of some charity organizations, and have posted a considerable number
of charity-related microblogs. To our surprise, such charitable nodes (about 10.7% of the 309 nodes) have
attracted 46.7% of all cross-religion links, and most charitable nodes (30 of 33) are Buddhists.
In summary, though everybody has observed some evidences about religion segregation in daily life,
this paper provides quantitative analysis based on an extracted religion network from weibo.com. The
extent of networked segregation for diﬀerent religions, measured by the assortativity coeﬃcient, is even
higher than that for diﬀerent races or diﬀerent political parties. In fact, to our knowledge, the present
religion network exhibits the highest segregation among all previously reported social networks consisted
of several classes of people. Among the four religions under consideration, Buddhism plays the most
signiﬁcant role in promoting the cross-religion communications.
We still cannot make sure this is a
speciﬁc phenomenon in China as Buddhism itself is one of a few mainstays of the Chinese culture or a
universal phenomenon over the world since the Buddhist doctrines are very inclusive and tolerant. A
solid answer to this question asks for more data from twitter.com as well as other representative social
networks at national level. We have also found that the small-scale religions in China, namely Islam and
Taosim, show much higher level of cohesion (see Table 2), which probably reﬂects a general observation


## Page 7


7
that the subculture group of smaller size usually shows a higher level of homophily [45].
A tiny fraction of cross-religion links maintain the global connectivity, whose removal will lead to
much faster breakdown of the network in comparison with those links with highest betweennesses or
bridgenesses. Therefore we want to understand the underlying reasons of the generation of these cross-
religion links. To our surprise, about half links point to charitable nodes. This strong evidence suggests
that charity may be a common interest that can stride across the ideological barriers between religions.
Accordingly, encouraging and holding charity-related activities, and at the same time inviting participants
from diﬀerent religions, may be an eﬀective method to facilitate cross-religion communications.
In this paper, we demonstrate the eﬀectiveness and validity of the data-driven paradigm in the studies
of religious issues, and we believe it will turn to be the mainstream methodology in the near future [46,47].
However, the reported ﬁndings just provide a tiny and early step towards the comprehensive landscape
of communicating patterns between believers of diﬀerent faiths. Three open issues are left for further
studies. First of all, we would like to test the universality of the present observations based on data from
other countries. Secondly, we want to see the evolution of the connecting patterns of religion networks by
tracing the temporal data [48]. Lastly, it would be interesting to see the role of religious believers in the
whole social network, instead of the network containing only believers. This is of particular importance
for countries like China where theists are the minority and their social inclusion needs to be promoted.
Methods
Assortativity Coeﬃcient. Assortativity coeﬃcient is used to quantify whether and to which extent
links tend to connect nodes in the same type. It is deﬁned as [38] r =
P
i eii−P
i aibi
1−P
i aibi
where eii, ai and bi
are introduced in the main text. In the case of the perfect assortative mixing, all links connecting nodes
in the same type, leading to P
i eii = 1 and r = 1.
Degree-preserved link-rewiring process.
This process randomly reshuﬄes links while keeps the
out-degree and in-degree of each node unchanged [41]. At each time step, we randomly select two links
A →B and C →D. If the link A →D or C →B exists, we go back to reselect two links, otherwise
these two links A →B and C →D are replaced by A →D and C →B. We repeat such operation for
suﬃciently long time (106 steps in this paper) to obtain the randomized counterpart (called null network)
of the original network.


## Page 8


8
Benchmark link centralities.
Betweenness centrality of a link l is the fraction of shortest paths
between pairs of nodes passing through l [26], say BCl =
P
s,t∈V,s̸=t
σ(s,l,t)
σ(s,t) , where σ (s, t) is the number of
shortest paths between nodes s and t, and σ (s, l, t) is the number of those paths passing through link l.
The bridgeness of a link l is deﬁned as Bl=pSxSy

Sl [27], where x and y are the two endpoints of link
l. Sx and Sl are the sizes of the maximum cliques (i.e., complete subgraph) that contain node x and link
l, respectively. The degree of link l is deﬁned as Dl=kxky [44], where kx and ky are the degrees of the
two endpoints of l.
References
1. Sosis, R. & Alcorta, C. Signaling, solidarity, and the sacred: the evolution of religious behavior.
Evol. Anthropol. 12, 264-274 (2003).
2. Atkinson, Q. D. & Bourrat, P. Beliefs about God, the afterlife and morality support the role of
supernatural policing in human cooperation. Evol. Hum. Behav. 32, 41-49 (2011).
3. Xygalatas, D. et al. Extreme rituals promote prosociality. Psychol. Sci. 24, 1602-1605 (2013).
4. Baumard, N. & Boyer, P. Explaining moral religions. Trends Cogn. Sci. 17, 272-280 (2013).
5. Botero, C. A. et al. The ecology of religious beliefs. Proc. Natl. Acad. Sci. U.S.A. 111, 16784-16789
(2014).
6. Purzycki, B. G. et al. Moralistic gods, supernatural punishment and the expansion of human social-
ity. Nature 530, 327-330 (2016).
7. Wilson, J. & Musick, M. Who cares? Toward an integrated theory of volunteer work. Am. Sociol.
Rev. 62, 694-713 (1997).
8. Graham, J. & Haidt, J. Beyond beliefs: religions bind individuals into moral communities. Pers.
Soc. Psychol. Rev. 14, 140-150 (2010).
9. Lewis, V. A., MacGregor, C. A. & Putnam, R. D. Religion, networks, and neighborliness: The
impact of religious social networks on civic engagement. Soc. Sci. Res. 42, 331-346 (2013).


## Page 9


9
10. Power, E. A. Social support networks and religiosity in rural South India. Nat. Hum. Behav. 1,
0057 (2017).
11. Lim, C. & Putnam, R. D. Religion, social networks, and life satisfaction. Am. Sociol. Rev. 75,
914-933 (2010).
12. Okulicz-Kozaryn, A. Religiosity and life satisfaction across nations. Mental Health, Religion &
Culture 13, 155-169 (2010).
13. Ritter, R. S., Preston, J. L. & Hermandez, I. Happy tweets: Christians are happier, more socially
connected, and less analytical than atheists on Twitter. Soc. Psychol. Per. Sci. 5, 243-249 (2014).
14. Iannaccone, L. R. Introduction to the economics of religion. J. Eco. Literature 36, 1465-1496
(1998).
15. Barro, R. & McCleary, R. Religion and economic growth across countries. Am. Sociol. Rev. 68,
760-781 (2003).
16. Norenzayan, A. et al. The cultural evolution of prosocial religions. Behav. Brain Sci. 39, 1 (2016).
17. Appleby, S. R. The ambivalence of the sacred: Religion, violence, and reconciliation (Rowman &
Littleﬁeld Publishers, 1999).
18. Atran, S. & Ginges, J. Religious and sacred imperatives in human conﬂict. Science 336, 855-857
(2012).
19. Neuberg, S. L. et al. Religion and intergroup conﬂict ﬁndings from the Global Group Relations
Project. Psychol. Sci. 25, 198-206 (2014).
20. Edgell, P., Gerteis, J. & Hartmann, D. Atheists as ”other”: moral boundaries and cultural mem-
bership in American society. Am. Sociol. Rev. 71, 211-234 (2006).
21. Gervais, W. M., Shariﬀ, A. F. & Norenzayan, A. Do you believe in atheists? Distrust is central to
anti-atheist prejudice. J. Pers. Soc. Psychol. 101, 1189-1206 (2011).
22. Gervais, W. M. Everything is permitted? People intuitively judge immorality as representative of
atheists. PLoS ONE 9, e92302 (2014).


## Page 10


10
23. Gervais, W. M. et al. Global evidence of extreme intuitive moral prejudice against atheists. Nat.
Hum. Behav. 1, 0151 (2017).
24. Lewis, K. The limits of racial prejudice. Proc. Natl. Acad. Sci. U.S.A. 110, 18814-18819 (2013).
25. Kiernan, J. P. Where Zionists draw the line: a study of religious exclusiveness in an African
township. Afr. Stud. 33, 79-90 (1974).
26. Girvan, M. & Newman, M. E. J. Community structure in social and biological networks. Proc.
Natl. Acad. Sci. U.S.A. 99, 7821-7826 (2002).
27. Cheng, X. Q. et al. Bridgeness: a local index on edge signiﬁcance in maintaining global connectivity.
J. Stat. Mech. 2010, P10011 (2010).
28. McPherson, M., Smith-Lovin, L. & Cook, J. M. Birds of a feather: Homophily in social networks.
Annu. Rev. Sociol. 27, 415-444 (2001).
29. Ruse, M. A natural history of religion. Nature 439, 535-535 (2006).
30. Bok´anyi, E. et al. Race, religion and the city: twitter word frequency patterns reveal dominant
demographic dimensions in the United States. Palgrave Communications 2, 16010 (2016).
31. Adida, C. L., Laitin, D. D. & Valfort, M. A. Identifying barriers to Muslim integration in France.
Proc. Natl. Acad. Sci. U.S.A. 107, 22384-22390 (2010).
32. Lindley, J. Race or religion? The impact of religion on the employment and earnings of Britain’s
ethnic communities. J. Ethn. Migr. Stud. 28, 427-442 (2002).
33. Clauset, A., Shalizi, C. R. & Newman M. E. J. Power-Law Distributions in Empirical Data. SIAM
Rev. 51, 661-703 (2009).
34. Barab´asi, A. L. & Albert, R. Emergence of scaling in random networks. Science 286, 509-512
(1999).
35. Watts, D. J. & Strogatz, S. H. Collective dynamics of ’small-world’ networks. Nature 393, 440-442
(1998).
36. Newman, M. E. J. & Girvan, M. Finding and evaluating community structure in networks. Phys.
Rev. E. 69, 026113 (2004).


## Page 11


11
37. Fortunato, S. & Barth´elemy, M. Resolution limit in community detection. Proc. Natl. Acad. Sci.
U.S.A. 104, 36-41 (2007).
38. Newman, M. E. J. Mixing patterns in networks. Phys. Rev. E. 67, 026126 (2003).
39. Catania, J. A. et al. Condom use in multi-ethnic neighborhoods of San Francisco: the population-
based AMEN (AIDS in Multi-Ethnic Neighborhoods) Study. Am. J. Public. Health 82, 284-287
(1992).
40. Conover, M. et al. Political polarization on twitter. Proceedings of the Fifth International AAAI
Conference on Weblogs and Social Media (AAAI Press, 2011) pp. 89-96.
41. Maslov, S. & Sneppen, K. Speciﬁcity and Stability in Topology of Protein Networks. Science 296,
910-913 (2002).
42. Onnela, J.-P. et al. Structure and tie strengths in mobile communication networks. Proc. Natl.
Acad. Sci. U.S.A. 104, 7332-7336 (2007).
43. Aharony, A. & Stauﬀer, D. Introduction to percolation theory (Taylor & Francis, 2003).
44. Holme, P. et al. Attack vulnerability of complex networks. Phys. Rev. E. 65, 056109 (2002).
45. Gelder, K. Subcultures: Cultural Histories and Social Practice (Routledge, 2007).
46. Campbell, H. A. Religion and the Internet: A microcosm for studying Internet trends and impli-
cations. New Media & Society 15, 680-694 (2013).
47. Chen, L., Weber, I. & Okulicz-Kozaryn, A. U.S. religious landscape on Twitter. Proceedings of the
International Conference on Social Informatics (Springer, 2014) pp. 544-560.
48. Holme, P. & Saram¨aki, J. Temporal networks. Phys. Rep. 519, 97-125 (2012).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
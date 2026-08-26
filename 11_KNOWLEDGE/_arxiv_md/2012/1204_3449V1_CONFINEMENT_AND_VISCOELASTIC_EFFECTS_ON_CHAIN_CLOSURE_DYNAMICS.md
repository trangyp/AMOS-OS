---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1204.3449v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1204.3449v1_Confinement_and_Viscoelastic_effects_on_Chain_Closure_Dynamics

> Source: 1204.3449v1_Confinement_and_Viscoelastic_effects_on_Chain_Closure_Dynamics.pdf

> Pages: 29

---


## Page 1


CONFINEMENT AND VISCOELASTIC EFFECTS ON CHAIN CLOSURE 
DYNAMICS  
Pinaki Bhattacharyya, Rati Sharma and Binny J. Cherayil,# 
Dept. of Inorganic and Physical Chemistry, Indian Institute of Science, 
Bangalore-560012, INDIA 
ABSTRACT 
        Chemical reactions inside cells are typically subject to the effects both of the cell’s 
confining surfaces and of the viscoelastic behavior of its contents.  In this paper, we show 
how the outcome of one particular reaction of relevance to cellular biochemistry – the 
diffusion-limited cyclization of long chain polymers – is influenced by such confinement 
and crowding effects. More specifically, starting from the Rouse model of polymer 
dynamics, and invoking the Wilemski-Fixman approximation, we determine the scaling 
relationship between the mean closure time ct  of a flexible chain (no excluded volume or 
hydrodynamic interactions) and the length N  of its contour  under the following separate 
conditions: (a) confinement of  the chain to a sphere of radius D, and (b) modulation of 
its dynamics by colored Gaussian noise. Among other results, we find that in case (a) 
when D is much smaller than the size of the chain, 
2
c ~ ND
t
, and that in case (b),  
)
2
2
/(
2
c ~
H
N
t
−
, H  being a number between 1/2 and 1 that characterizes the decay of the 
noise correlations. H is not known à priori, but values of about 0.7 have been used in the 
successful characterization of protein conformational dynamics. At this value of H 
(selected for purposes of illustration), 
4.3
c ~ N
t
,  the high scaling exponent reflecting the  
slow relaxation of the chain in a viscoelastic medium.  
                                                 
# Corresponding author. Email: cherayil@ipc.iisc.ernet.in


## Page 2


2
1. INTRODUCTION 
             Despite their intrinsic stochasticity, molecular processes inside cells have 
somehow evolved to produce reaction pathways that seem exquisitely choreographed. 
How this is achieved in spaces that are typically only a few micrometers across and that 
are extremely congested is one of many unanswered questions that presently defines the 
limits of our understanding of living matter. We believe that a deeper appreciation of the 
effects of confinement and crowding on single-molecule reaction dynamics would go 
some way towards advancing our knowledge of life’s operations at the microscopic level. 
To this end, we attempt to show, in this paper, how such factors can influence the 
outcome of one particular reaction of considerable biological significance: chain 
cyclization.     
           The cyclization of biopolymers like DNA and RNA is significant for a number of 
reasons; it facilitates the interaction of  DNA-bound proteins with  distant target sites, 
thereby regulating gene expression;1 it leads to the formation of compact tertiary 
structures, which may be important in the packaging of genetic information;2 and it likely 
plays a role in mediating the long-range interactions that signal the start of replication at 
different locations on the polynucleotide backbone.3 The importance of the cyclization 
reaction is, of course, not confined to biopolymers alone, but extends to other polymeric  
systems as well, including many with industrial and commercial applications.4    
         Over the last several years, a great deal of  theoretical research  has therefore been 
devoted to the development of models of the dynamics of chain cyclization,5-19 with a 
special emphasis on understanding how the mean reaction time varies with chain 
properties, particularly the molecular weight. Because of the intrinsic many-body


## Page 3


3
character of the cyclization reaction in polymers (which in any realistic description 
requires a treatment of all the monomers in the chain, including their mutual excluded 
volume and hydrodynamic interactions), calculations of reaction times and similar 
quantities are generally non-trivial, and require numerous approximations. They are 
rendered even more non-trivial when boundaries are present, or when the medium is 
viscoelastic, and to the best of our knowledge, they have so far not been attempted at all 
under these conditions. But it is precisely these conditions that are generally encountered 
by long chain molecules inside cells, microfluidic devices, or other confined spaces. 
Fully extended DNA, for instance, can exceed by several orders of magnitude the size of 
the region to which it is typically confined; moreover, its dynamics inside the cell is 
mediated by a fluid  that likely contains a dense mixture of entangled polymeric chains, 
rendering its surroundings highly viscoelastic.  In these kinds of surroundings, which may 
also be met by polymers in non-biological contexts, molecular diffusion is often 
anomalous20 (meaning the center of mass motion varies sub-linearly with time), and this 
circumstance is likely to affect the cyclization reaction.     
           To what extent such circumstances  – confinement and crowding, specifically –  
affect the chain length dependence of  the mean reaction time is the question we shall 
attempt to address in this paper.  The confinement problem is considered by studying the 
cyclization reaction using a Rouse chain that moves inside a sphere. The crowding 
problem is considered by studying the reaction using an unconfined “renormalized” 
Rouse chain that moves through a complex fluid. In both studies, the actual calculations 
are carried out within the framework of an approach developed by Wilemski and 
Fixman5, and since used, in an important paper by Pastor, Szabo and Zwanzig10, to


## Page 4


4
determine the mean cyclization time of a polymer at the theta point as a function of 
various chain properties. The WF formalism has also been used to calculate the mean 
closure times for unconfined polymers with bending stiffness13 and with long-range 
excluded volume interactions,17, and is generally felt to provide a sensible approach to 
the study of cyclization dynamics.6,7,21 However, its utility in analyzing actual data may 
depend on how closely experimental conditions ensure that the closure reaction is 
diffusion limited. Experiments performed on synthetic DNA and RNA, for instance, often 
rely on  fluorescence quenching to measure reaction times, and in that case the kinetics of 
electron transfer, which introduce other timescales into the problem, may need to be 
accounted for. The WF approximation may then no longer be entirely trustworthy.8,14,19  It 
is therefore only when quenching is very efficient and its influence effectively negligible 
that the WF approximation can be assumed to hold good. In using this approximation in 
our calculations, therefore, we are assuming implicitly that diffusion-limited conditions 
do in fact prevail. .     
             The next section is a brief review of the WF formalism, highlighting the role of 
the time correlation function of the end-to-end distance in the evaluation of the mean 
closure time ct .  Section 3 discusses how this time correlation function is itself calculated 
for confined polymers and polymers in complex fluids. And finally, sec. 4 discusses the 
results of  these calculations, and their implications.


## Page 5


5
2. THEORETICAL BACKGROUND  
Consider, to begin with, a polymer of  n  monomers with reactive ends in an 
unbounded viscous fluid at temperature T. The configuration of the polymer at time t is 
specified by the set of monomer positions 
)
,
,
,
(
}
{
2
1
nr
r
r
r
…
≡
. If 
)
},
({
t
r
ψ
 denotes the 
probability density that the first monomer is between 
1r  and 
1
1
r
r
d
+
, the second between 
2r  and 
2
2
r
r
d
+
, and so on, the evolution of   
)
},
({
t
r
ψ
 is given by the following equation  
                         
)
},
({
})
({
)
},
({
)
},
({
t
S
t
t
t
r
r
r
r
ψ
λ
ψ
ψ
−
=
∂
∂
D
                                 (1) 
Here 
})
({r
S
 is a sink function (to be specified later), λ  is a reaction rate, and  
[
]
∑=
∇
⋅
∇
+
∇
≡
n
i
i
i
i
U
D
1
2
0
β
D
 is a generalized diffusion operator in which 
i
i
r
∂
∂
≡
∇
/
, 
ζ
/
0
T
k
D
B
≡
 is a diffusion coefficient, with ζ  a monomer friction coefficient and 
β
/
1
≡
T
kB
 the Boltzmann factor,  and 
})
({r
U
U =
is  the intermolecular potential.    
          As has been shown elsewhere5,10, for a chain whose dynamics are governed by Eq. 
(1) and for which 
})
({r
S
 is a function solely of the distance between one end of the chain 
and the other,  the mean cyclization time ct  is given by  
                                                        
∫
∞
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
∞
=
0
c
1
)
(
)
(
C
t
C
dt
t
                                                   (2) 
where 
                            
∫
∫
=
)
(
)
(
)
,
|
,
(
)
(
)
(
0
0
0
0
R
R
R
R
R
R
R
eq
S
t
t
G
S
d
d
t
C
ψ
,                           (3)  
R  and 
0
R  are, respectively, the end-to-end distances of the chain at time t and time 0, 
)
,
|
,
(
0 t
t
G
R
R
 is the conditional probability density that a chain with the end-to-end 
distance 
0
R  at 0 has the end-to-end distance R at time t, and 
)
(
0
R
eq
ψ
 is the initial


## Page 6


6
equilibrium distribution of end-to-end distances. This expression has been arrived at on 
the basis of the closure scheme introduced by Wilemski and Fixman5 in which the exact 
solution to Eq. (1) is replaced by an approximate expression involving the product of the 
equilibrium chain distribution and a self-consistently determined time-dependent 
correction. It has been further assumed that  
∞
→
λ
, which implies that the ends of the 
chain react instantaneously and irreversibly whenever they satisfy the distance constraint 
imposed by the sink function.                      
             The function  
)
,
|
,
(
0 t
t
G
R
R
 is central to the calculation of  
ct , but it is not 
known in general. However, if R is a Gaussian stochastic process, it is given explicitly 
by22   
             
[
]
⎥
⎥
⎦
⎤
⎢
⎢
⎣
⎡
−
−
−
−
⎟⎟
⎟
⎠
⎞
⎜⎜
⎜
⎝
⎛
=
))
(
1(
2
)
)
(
(
3
exp
)
(
1
1
2
3
)
0,
|
,
(
2
eq
2
2
0
2
/
3
2
2
/
3
eq
2
0
t
t
t
t
G
ϕ
ϕ
ϕ
π
R
R
R
R
R
R
          (4) 
where 
eq
2
/
)
0
(
)
(
)
(
R
R
R
⋅
≡
t
t
ϕ
  is the normalized time correlation function of the end-
to-end distance, the angular brackets denoting an ensemble average over chain 
configurations. In the present model of chain dynamics, excluded volume and 
hydrodynamic interactions are assumed to be absent, and R is therefore a sum of a large 
number of bonds whose random orientations are driven by white noise (or colored 
Gaussian noise in the case of diffusion through a viscoelastic medium.)  R  itself is 
therefore a Gaussian random variable, and Eq. (4) is a satisfactory description of  its 
time-dependent conditional probability density.   
           Making the further assumption that 
)
(R
S
 depends only on 
R
=
R
, one can carry 
out the angular integrations in Eq. (3) analytically,23  with the result that


## Page 7


7
     
     
[
]
∫
∫
∞
∞
−
⎟⎟
⎟
⎠
⎞
⎜⎜
⎜
⎝
⎛
=
0
0
0
2
0
0
2
2
/
3
2
3
eq
2
2
)
(
)
(
)
(
1
1
2
3
16
)
(
R
S
R
dR
R
S
dRR
t
R
t
C
ϕ
π
π
 
               
⎟⎟
⎟
⎠
⎞
⎜⎜
⎜
⎝
⎛
−
+
−
⎟⎟
⎟
⎠
⎞
⎜⎜
⎜
⎝
⎛
−
−
×
))
(
1(
2
)
(3
exp
))
(
1(
)
(
3
sinh
)
(
3
))
(
1(
2
eq
2
2
0
2
2
eq
2
0
0
2
eq
2
t
R
R
R
t
R
RR
t
RR
t
t
R
ϕ
ϕ
ϕ
ϕ
ϕ
           (5) 
Further simplification is possible if the sink function is chosen to correspond to the delta 
function, i.e.,  
)
(
)
(
a
R
R
S
−
= δ
.  It then follows that10  
                     
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
−
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
−
=
∞
)
(
1
)
(
2
exp
)
(
1
)
(
2
sinh
)
(
1
)
(
2
1
)
(
)
(
2
2
0
2
0
2
0
t
t
x
t
t
x
t
t
x
C
t
C
ϕ
ϕ
ϕ
ϕ
ϕ
ϕ
                     (6) 
where 
eq
2
2
0
2
/
3
R
a
x =
. This expression is singular at 
0
=
t
 where 
1
)
(
=
t
ϕ
,  but it can 
be rewritten in the more convenient form 
                                       
2
/
3
2
0
2
)
(
3
4
)
(
1
)
(
)
(
−
⎟
⎠
⎞
⎜
⎝
⎛
+
+
−
≈
∞
"
t
x
t
C
t
C
ϕ
ϕ
                                    (7) 
following the approach adopted by Pastor et al.10 whereby Eq. (6) is expanded in powers 
of 
0x  and then re-expressed in a resummed form that to the same order in 
0x  is identical 
to the original expansion. The above expression proves to be convenient for deriving 
analytic scaling results for ct .  
           The next two sections describe the treatment of polymer cyclization rates when the 
chain is confined to a sphere and when it moves through a viscoelastic continuum.


## Page 8


8
3.  CHAIN CYCLIZATION DYNAMICS IN A SPHERE 
 
A. Effective Rouse description 
 
To explore the influence of boundaries on chain cyclization rates we calculate, in 
this section, the mean first passage cyclization time of a simple Gaussian chain confined 
to a spherical cavity24 of radius D, with one end fixed at the center of the sphere. (No real 
loss of generality is entailed by imposing this constraint, but it does simplify the algebra.) 
Even this seemingly simple system presents a number of analytical challenges that can 
only be met by the introduction of several further approximations (going beyond those 
defined by the Wilemski-Fixman5 closure scheme.) Chief among these is an 
approximation for the treatment of polymer dynamics in the presence of boundaries. 
Although the equilibrium statistical mechanics of polymer-surface interactions is well 
developed,25  extensions of the methodology to the dynamical regime are in general non-
trivial. But a relatively simple approach to the problem, which is nevertheless systematic 
and well-controlled, has recently been introduced by Kalb and Chakraborty.26 It is based 
on the idea that the confined chain admits of a representation in terms of decoupled 
Rouse modes in which the geometry of the external surface is wholly incorporated into 
the relaxation times of the internal modes. These relaxation times can be expressed in 
terms of the equilibrium conformation of the chain under confinement, and can therefore 
be calculated rigorously.  
To implement this approach, we recall, first of all, that for a free Rouse chain, the 
equation of motion of individual monomers (in continuum notation) is given by27 
                                   
)
,
(
)
,
(
)
,
(
2
2
t
t
k
t
t
τ
τ
τ
τ
ζ
θ
r
r
+
∂
∂
=
∂
∂
                                          (8)


## Page 9


9
where 
)
,
(
t
τ
r
 is the spatial location, at time t, of the monomer at the point τ  on the chain 
backbone, 
2
/
3
b
T
k
k
B
≡
, b  being the Kuhn length of the chain, and 
)
,
(
t
τ
θ
 is a random 
force (acting on the monomer at τ )  whose statistical properties are entirely defined by 
the 
following 
correlations: 
0
)
,
(
=
t
τ
θα
 
and 
)
(
)
(
2
)
,
(
)
,
(
τ
τ
δ
δ
δ
ζ
τ
θ
τ
θ
αβ
β
α
′
−
′
−
=
′
′
t
t
T
k
t
t
B
. Equation (8) can be solved by expanding 
the variables 
)
,
(
t
τ
r
 in a set of independent normal modes 
)
(t
p
X
, using the relations  
0
,)
,
(
)
/
cos(
)
(
0
1
≥
=
∫
−
p
t
N
p
d
N
t
N
p
τ
πτ
τ
r
X
 and 
∑
∞
=
+
=
1
0
)
/
cos(
)
(
2
)
(
)
,
(
p
p
N
p
t
t
t
πτ
τ
X
X
r
, 
N  being the contour length of the chain. When this is done, Eq. (8) is transformed to the 
decoupled equations 
                                             
)
(
)
(
)
(
t
t
k
t
t
p
p
p
p
p
f
X
X
+
−
=
∂
∂
ζ
                                            (9) 
where 
ζ
ζ
N
=
0
, 
ζ
ζ
N
p
2
=
 
for
1
≥
p
, 
N
kp
k p
/
2
2
2
π
=
 
for 
0
≥
p
, 
and 
∫
=
N
p
N
p
t
d
t
f
0
)
/
cos(
)
,
(
2
)
(
πτ
τ
τθ
, 
with 
0
)
(
=
t
pf
 
and 
)
(
2
)
(
)
(
t
t
T
k
t
f
t
f
pq
B
p
q
p
′
−
=
′
δ
δ
δ
ζ
αβ
β
α
. Equation (9) is easily solved in closed form, the 
solution being 
∫
′
′
+
=
′
−
−
−
−
t
p
t
t
k
p
t
k
p
p
t
td
t
p
p
p
p
0
/)
(
1
/
)
(
e
e)
0
(
)
(
f
X
X
ζ
ζ
ζ
.   
          In terms of the above normal modes, the end-to-end vector 
)
(t
R
 is given by               
∑
−
=
odd
)
(
4
)
(
p
p t
t
X
R
, so the end-to-end correlation function is 
               
(
)
∑
∑
−
=
⋅
=
⋅
odd
odd
/
exp
3
16
)
0
(
)
(
16
)
0
(
)
(
p
p
p
B
p
p
p
t
k
T
k
t
t
τ
X
X
R
R
                      (10)


## Page 10


10
where the second equality follows from the solution of Eq. (9) and the properties of 
)
(t
pf
. The parameter 
p
τ  is the characteristic relaxation time of the mode p , which is  
given by 
2
1 / p
p
τ
τ
=
, 
1
τ  being the longest relaxation time, which itself is given by 
1
1
1
/ k
ζ
τ =
; 
1k , in turn, is given by the equilibrium average 
eq
2
1
1
/
3
X
T
k
k
B
=
.  
           Since Eq. (10) is a sum of rapidly decreasing exponentials, the time correlation 
function of the end-to-end vector is governed mainly by the first mode. To a reasonable 
approximation, therefore, 
                                  
(
)
1
1
eq
2
1
/
exp
16
)
0
(
)
(
ζ
t
k
t
−
≈
⋅
X
R
R
                                         (11) 
and so 
eq
2
1
2
16
)
0
(
X
R
≈
. Thus, if the chain is initially in equilibrium (and this 
assumption is necessary in the implementation of the Wilemski-Fixman method5), this 
means that 
                                        
(
)
eq
2
eq
2
/
24
exp
)
0
(
)
(
R
R
R
R
ζ
N
Tt
k
t
B
−
≈
⋅
                   (12) 
In the spirit of approximations that treat the dynamics of chains with excluded volume, 
hydrodynamic or monomer-surface interactions by means of a Rouse model with 
effective or scaled  parameters,26,27 we now assume that under confinement 
)
0
(
)
(
R
R
⋅
t
 
has exactly the structure of Eq. (12), and that all of the effects of  confinement are 
contained in the quantity  
eq
2
R
, which is amenable to calculation by standard 
equilibrium statistical mechanical methods. That calculation is described in the next 
section, but before discussing its details, it is useful to note that the approximations of 
Eqs. (10) – (12) reduce the function 
)
(t
ϕ
 that is needed in the evaluation of the 
cyclization time to the expression


## Page 11


11
                                                         
t
t
α
ϕ
−
= e
)
(
                                                              (13) 
where 
eq
2
/
24
R
ζ
α
N
T
kB
=
; Eq. (13) will be recognized as the defining relation of the 
so-called harmonic spring model,6  about which more will be said later.  
 
 
B. Equilibrium dimensions of a spherically confined Gaussian polymer 
         The mean square end-to-end distance 
eq
2
R
 of a free Gaussian polymer of contour 
length N, one end of which is located at the origin, is given in general by the relation 
                                               
)
,
(
1
0
2
0
eq
2
N
G
d
Z
R
R
R
R
∫
=
                                        (14) 
where 
∫
=
)
,
(
0
0
N
G
d
Z
R
R
, and 
)
,
(
0
N
G R
 is the chain propagator, defined formally by 
the path integral  
                         
⎥
⎥
⎦
⎤
⎢
⎢
⎣
⎡
⎟
⎠
⎞
⎜
⎝
⎛
∂
∂
−
=
∫
∫
=
=
N
N
d
l
D
N
G
0
2
2
)
(
)
0
(
0
)
(
2
3
exp
]
[
)
,
(
τ
τ
τ
r
r
R
R
r
0
r
                                     (15) 
which may be shown to satisfy the differential equation28 
                                         
)
(
)
(
)
,
(
6
0
2
2
R
R
R
δ
δ N
N
G
b
N
=
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
∇
−
∂
∂
                                   (16) 
whose solution is 
(
)
2
2
2
/
3
2
0
2
/
3
exp
)
2
/
3
(
)
,
(
Nb
Nb
N
G
R
R
−
=
π
. When the polymer is 
confined to a certain volume by a surface, such as the surface of a sphere, the 
corresponding propagator, 
)
,
(
N
G R
, may still be derived from Eq. (16), but it must now 
satisfy the boundary conditions appropriate to the nature of the confining geometry. As


## Page 12


12
shown in Appendix A, if this geometry is that of a sphere of radius D (requiring 
)
,
(
N
G R
 
to vanish at 
D
R
=
≡
|
| R
), 
)
,
(
N
G R
 is given by24   
     
[
]
2
2
2
0
0
2
/
1
0
1
0
2
2
/
3
2
/
1
2
/
5
2
/
3
6
/
exp
)
/
(
)
(
1
2
1
)
,
(
D
Nb
y
D
R
y
J
y
y
J
R
D
N
R
G
n
n
n
n
n
−
=
∑
∞
=
π
   (17) 
where 
)
(x
Jν
  is the Bessel function of order ν , and 
n
y0  is the nth zero of the Bessel 
function of order 1/2, i.e.,  
0
)
(
0
2
/
1
=
n
y
J
.   
            The calculation of  
eq
2
R
 using the analogue of Eq. (14), viz., 
)
,
(
2
1
eq
2
N
G
d
Z
R
R
R
R
∫
−
=
, 
where 
)
,
(
N
G
d
Z
R
R
∫
=
 
and 
∫
∫
∫
∫
=
π
π
θ
θ
φ
2
0
0
0
2
sin
D dRR
d
d
dR
 presents no special difficulties, though it is necessary to 
refer to tabulated results29 for values of integrals involving the Bessel functions. In this 
way, we find that 
                           
(
)
(
) ⎥
⎥
⎥
⎥
⎦
⎤
⎢
⎢
⎢
⎢
⎣
⎡
Λ
−
−
Λ
−
−
−
=
∑
∑
∞
=
+
∞
=
−
+
1
2
2
1
2
1
2
2
2
1
2
eq
2
exp
)1
(
exp
)1
(
6
1
n
n
n
n
n
n
n
D
R
π
π
π
                                 (18) 
where 
2
2 6
/ D
Nb
≡
Λ
. One may verify that in the limit 
1
>>
D
, 
2
2
eq
2
6
Nb
D
R
=
Λ
→
, 
and that in the limit 
1
<<
D
, 
)
/
6
1(
2
2
eq
2
π
−
→D
R
, independent of N. 
           This result, Eq. (18), together with Eq. (13) provide the ingredients for the 
determination of the cyclization time. Specifically, by substituting Eqs. (7) and  (13) into 
(2), we find that 
                                                 
)
(
48
0
1
2
c
x
Z
T
k
R
N
t
B
eq
ζ
=
                                                 (19a)


## Page 13


13
where 
                                        
∫
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
−
=
1
0
2
/
3
0
1
1
)
1(
1
1
)
(
y
y
dy
x
Z
σ
                                           (19b) 
with 
3
/
4
1
0x
−
=
σ
 and 
0x , as already defined, given by 
eq
2
2
0
2
/
3
R
a
x =
, a being the 
reaction radius. A discussion of these equations will be presented in Sec. 5.   
 
            
4.  CHAIN CYCLIZATION DYNAMICS IN A CROWDED ENVIRONMENT  
            In this section we turn our attention to the calculation of the mean closure time for 
a polymer in a fluid that by virtue of a high density of other macromolecular species in it 
is viscoelastic. The cyclization of a polymer in such fluids (of which the cytoplasm is 
clearly an example) is a many-chain problem, and is difficult to treat in complete 
generality. But as shown by Schweizer using a projection operator formalism applied to a 
polymer melt,30 the  problem  can be reduced to one involving just a single tagged chain 
whose monomer dynamics are described, approximately, by a generalized Langevin 
equation (GLE).31 All the effects of the other chains in the medium are then contained in 
the memory function of this GLE, which in Schweizer’s calculations was the object of 
primary interest, and the focus of efforts to develop theoretical models of. In the present 
calculations (as in some earlier ones32),  we take the GLE as the point of departure for 
exploring chain cyclization times in crowded environments, but no longer regard the 
memory function as a quantity to be determined rigorously from first principles;  instead, 
we fix its functional form at the outset by assuming – on the basis of earlier corroborative 
evidence from experiment,33  theory34 and numerical simulations35  – that the random


## Page 14


14
thermal forces that govern chain dynamics in a viscoelastic medium can be described by 
the stochastic process known as fractional Gaussian noise (fGn).36  Under this 
assumption, the memory function becomes a simple power law in time, and the resulting 
GLE then becomes amenable to analytic treatment, as we now show.  
          The general structure of the GLE obtained from Schweizer’s projection operator 
approach is, in the continuum notation of the previous section,   
                     
)
,
(
)
,
(
)
,
(
)
|,
(|
2
2
0
0
t
t
k
t
t
t
t
td
d
N
t
τ
τ
τ
τ
τ
τ
τ
ζ
F
r
r
+
∂
∂
=
′
∂
′
′
∂
′
−
′
−
Γ′
′
∫
∫
                       (20) 
Here 
)
,
(
t
τ
F
 is the random thermal referred to above, and at time t it acts on the monomer 
at the point τ ;  
)
|,
(|
t
t
′
−
′
−
Γ
τ
τ
 is the memory function, which is related  to 
)
,
(
t
τ
F
 by a 
fluctuation-dissipation theorem:31 
)
|,
(|
,
(
)
,
(
t
t
T
k
t
F
t
F
B
′
−
′
−
Γ
=
′
′
τ
τ
δ
ζ
τ
τ
αβ
β
α
; and 
2
/
3
b
T
k
k
B
≡
 is the spring constant introduced earlier. In deriving this equation, it has 
been assumed that inertial contributions are negligible, and that hydrodynamic 
interactions are screened out. By choosing 
)
,
(
t
τ
F
 to correspond to fGn, we see from the 
fluctuation-dissipation relation that 
2
2
−
′
−
∝
Γ
H
t
t
, where H, the Hurst index, is a number 
between 1/2 and 1 that characterizes the degree of correlation between force fluctuations 
at different instants of time.  
       Equation (20) may be solved by the same normal mode method that was used in the 
analysis of the Rouse model. That method yields the decoupled equation: 
                                  
)
(
)
(
)
(
)
(
0
t
t
N
k
t
t
t
t
td
p
p
t
p
p
p
p
F
X
X
+
−
=
′
∂
′
∂
′
−
Γ′
∫
ζ
                           (21)


## Page 15


15
where 
)
/
cos(
)
,
(
)
(
0
1
N
p
t
t
d
N
t
t
N
p
πτ
τ
τ
′
−
Γ
=
′
−
Γ
∫
−
 
and 
∫
−
=
N
p
N
p
t
d
N
t
0
1
)
/
cos(
)
,
(
2
)
(
πτ
τ
τ F
F
. From the properties of 
)
,
(
t
τ
F
, 
)
(t
p
F
 is 
characterized 
by 
these 
statistical 
correlations: 
 
0
)
(
=
t
p
F
 
and 
)
(
)
(
)
(
1
t
t
TN
k
t
F
t
F
p
pq
B
p
q
p
′
−
Γ
=
′
−
δ
δ
ζ
αβ
β
α
. The identification of 
)
,
(
t
τ
F
 with fGn 
means that 
2
2
1
|
|
)1
2
(
2
)
(
−
−
′
−
−
=
′
−
Γ
H
p
t
t
N
H
H
t
t
 (assuming no mode dependence of the 
memory function, an assumption largely justified by Schweizer’s calculations30)            
          As before, the key ingredient in the calculation of the cyclization time is the time 
correlation function of the end-to-end distance, which is obtained from the time 
correlation function of 
)
(t
p
X
. The latter is easily found from Eq. (21) using Laplace 
transforms. The result is  
                                   
(
)
[
]
H
RR
H
p
p
p
t
E
t
2
2
2
2
2
/
)
0
(
)
0
(
)
(
−
−
−
=
⋅
τ
X
X
X
                          (22) 
where 
∑
∞
=
+
Γ
≡
0
)1
(
/
)
(
k
k
a
ak
z
z
E
 is the Mittag-Leffler function,37 
RR
τ
 is  a characteristic 
relaxation time given by 
(
)
(
) (
)
H
p
p
RR
k
H
2
2
1
1
2
−
+
Γ
= ζ
τ
,  and 
)
0
(
2
p
X
  is 
p
B
k
T
k
/
3
 as 
before. From these results, using Eq. (10), we find that  
                  
(
)
[
]
∑
∑
−
−
−
−
−
=
⋅
≡
odd
1
odd
2
2
2
2
1
2
)
/
)
0
(
)
(
)
0
(
1
)
(
p
p
p
H
RR
H
p
k
t
E
k
t
t
τ
ϕ
R
R
R
 
                           
∑
∞
=
−
−
⎥
⎦
⎤
⎢
⎣
⎡
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
+
Γ
−
−
−
=
1
2
2
2
2
2
2
2
2
2
)1
2
(
)1
2
(
)1
2
(
1
8
p
H
H
H
N
t
k
p
E
p
ζ
π
π
                             (23) 
This function is shown in Fig.1. The curve corresponding to 
2
/
1
=
H
 describes 
simple exponential decay; the higher values of H describe chains that are increasingly


## Page 16


16
sluggish, which is the behavior expected in media that are very crowded, such as a 
polymer melt, or a concentrated polymer solution.  
             The cyclization time is now given by 
                                        
)
(
)1
2
(
2
2
1
0
2
)
2
2
/(
1
2
2
x
Z
k
H
N
H
t
H
c
−
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
+
Γ
−
=
π
ζ
                         (24a) 
where  
                                  
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
−
=
−
−
∞
∫
1
))
(
1(
1
)
(
2
/
3
2
)
2
2
/(
)
1
2
(
0
0
2
y
y
dy
x
Z
H
H
σϕ
                         (24b) 
with 
∑
∞
=
−
−
−
−
−
−
=
1
2
2
2
2
2
]
)1
2
(
[
)1
2
(
8
)
(
p
H
y
p
E
p
y
π
ϕ
.  
 
 
5. RESULTS AND DISCUSSION 
           The primary aim of these calculations has been to better understand how a reaction 
relevant to cellular biochemistry – chain cyclization – is affected by steric constraints.  
To this end, we have sought to determine the scaling relationship between the mean 
cyclization time 
ct  of a polymer having no excluded volume or hydrodynamic 
interactions and its contour length N when (a) the chain is confined to a spherical cavity, 
and (b) when it is placed in a viscoelastic fluid.  
 
A. Spherically confined polymers 
            For such polymers, the N-dependence of  
ct  is found from Eq. (19), which 
contains two N-dependent factors: 
eq
R
N
2
 and the integral 
)
(
0
1 x
Z
. The latter can


## Page 17


17
actually be evaluated in closed form, as described in Appendix B. The result, when 
substituted into Eq. (19a), yields   
⎥
⎥
⎥
⎦
⎤
⎢
⎢
⎢
⎣
⎡
⎪⎭
⎪⎬
⎫
⎪⎩
⎪⎨
⎧
⎟⎟
⎟
⎠
⎞
⎜⎜
⎜
⎝
⎛
−
+
⎟
⎟
⎟
⎠
⎞
⎜
⎜
⎜
⎝
⎛
+
−
−
−
−
=
eq
eq
eq
eq
B
eq
R
a
R
a
R
a
R
a
Ta
k
R
N
t
2
2
2
/
1
2
2
/
1
2
2
/
1
2
2
/
3
2
c
2
1
ln
/
2
1
/
2
1
ln
2
ln
2
2
2
1
2
24
ζ
 
                                                                                                                                         (25) 
This result exactly reproduces the scaling structure obtained by Doi6 for the harmonic 
spring model. But as noted by Doi himself, the conclusions drawn from this expression 
should be treated with caution, since they are based on an approximation in which the 
true dynamics of the polymer is represented by the dynamics of its first mode.  While this 
is not necessarily a poor approximation when considering such bulk properties as the 
viscosity, its application to chemical reactions can be more problematic, for the following 
reason.  The overall behavior of  
ct  is determined principally by the dynamics of the 
chain end-to-end vector, 
)
(t
R
, through the correlation function 
)
(t
ϕ
. 
)
(t
R
 itself is  
principally determined by the first Rouse mode, 
)
(
1 t
X
, but there are fluctuations around 
this value arising from the dynamics of the higher modes 
)
(
3 t
X
, 
)
(
5 t
X
, etc. As shown 
by Doi, their mean square amplitude, 
2
A ,  is roughly  
                             
N
R
t
t
A
~
2.1
))
(
)
(
(
eq
2
2
1
2
≈
−
=
X
R
                                         (26) 
so 
2
/
1
2
/
1
2
~
~
N
R
A
eq
. The fluctuations in 
)
(t
R
 can therefore be said to occur in a 
sphere of radius A centered on 
)
(
1 t
X
, and because motion of 
)
(t
R
 in this sphere is very 
fast, the cyclization reaction is expected to occur whenever 
A
t <
)
(
R
, suggesting that we


## Page 18


18
should actually use  A rather than a  in the expression for  
ct  [Eq. (25)].  When this is 
done, we find that the N dependence of  ct  is now determined principally by  
                                                            
eq
R
N
t
2
c ~
                                                       (27) 
which has the following two limiting behaviors: 
                                                              
2
c ~ N
t
,        
N
D >>
                                     (28a) 
and  
                                                              
2
c ~ ND
t
,       
D
N >>
                                   (28b) 
The first of these scaling results [Eq. (28a)] is consistent with known behavior in free 
space6,7,10,13 but the second is a new prediction that we believe it would be interesting to 
test  experimentally.  
              In arriving at these results, we have had to appeal to physical arguments to 
justify the replacement of the reaction radius a by A; however, a mathematical basis for 
this replacement can be suggested. Suppose the parameter σ  in Eq. (19b) is sufficiently 
small that the integrand there can be binomially expanded; then to leading order  
                                               
constant
~
2
/
3
1
σ
≈
Z
                                                      (29) 
Recalling the definition of σ  as 
3
/
4
1
0x
−
, we see that the requirement that σ  be small 
is satisfied only if 
2
2
0
2
/
3
eq
R
a
x ≡
 is of order 1, which means 
2
/
1
2
~
eq
R
a
, exactly the 
condition derived by Doi.


## Page 19


19
B. Polymers in viscoelastic media  
            The N-dependence of ct  for polymers in these conditions is now contained in Eqs. 
(24a) and (24b), but the integral 
)
(
0
2 x
Z
 can no longer be evaluated in closed form, and 
must be found numerically. However, if one were to treat the chain dynamics with the 
same “harmonic spring” approximation used earlier (i.e., retain only the lowest mode in 
the expression for the correlation function 
)
(t
ϕ
), and then similarly assume that σ  takes 
on a  small constant value, so that the integrand in 
)
(
0
2 x
Z
 can be binomially expanded to 
leading order, then ct  is given by   
                                                         
)
2
2
/(
2
3
c
H
N
BZ
t
−
=
                                                 (30a) 
where 
)
2
2
/(
1
2)
/)1
2
(
))(
4
4
/(
3
(
H
k
H
H
B
−
+
Γ
−
≡
π
ζ
σ
 and 
∫
∞
−
−
≡
0
2
)
2
2
/(
)
1
2
(
3
)
(y
dyy
Z
H
H
ϕ
, 
with 
)
(
)
(
2
2
y
E
y
H −
=
−
ϕ
. In this approximation, therefore, 
                                                         
)
2
2
/(
2
c ~
H
N
t
−
,                                                      (30b) 
and so 
2
c ~ N
t
 when 
2
/
1
=
H
, and 
4
c ~ N
t
 when 
4
/
3
=
H
. For these special values of 
H, the Mittag-Leffler function 
)
(
2
2
"
H
E −
 reduces to simpler special functions (an 
exponential in the case 
2
/
1
=
H
, and an error function in the case 
4
/
3
=
H
.) This makes 
it a simple matter to evaluate Eq. (24b) [i.e., the integral 
)
(
0
2 x
Z
] essentially exactly by 
numerical methods, and the numerical results confirm the scaling predictions of Eq. 
(30b).  We believe that Eq. (30b) holds for other values of H as well, although this 
remains to be confirmed.  So if 
H
α
  denotes the exponent 
)
2
2
/(
2
H
−
 in Eq. (30b), we 
can set down the following illustrative list of exponents: 
               
2
5.0
=
α
,     
5.2
6.0
=
α
,     
9.2
65
.0
=
α
,       
35
.3
7.0
=
α
,       
4
75
.0
=
α
             (31)


## Page 20


20
These results suggest that as H becomes larger and chain relaxation becomes 
slower (essentially because of increased viscoelasticity), the chain cyclization rate 
becomes slower too, as seems reasonable. But the exponents in Eq. (31), for 
6.0
≥
H
, are  
unexpectedly large. Most experimental studies of loop formation in polymers (usually 
carried out in dilute solution) have found exponent values in the range 2 (corresponding 
to chains at the theta point) to about 2.4 (corresponding to chains in good solvents.) 
Interestingly, a recent study (carried out at high viscosity under diffusion-limited 
conditions) of short (11 – 26 bases) segments of unstructured single-stranded DNA has 
found evidence that the cyclization time scales as the 3.85 power of the chain length.  
This unusually high exponent value has been attributed to electrostatic repulsion between 
the charged ends of the DNA.38   
Further experimental and theoretical work on cyclization dynamics under 
conditions of confinement and crowding would clearly be helpful in clarifying some of 
the issues raised by the present calculations.


## Page 21


21
APPENDIX A: PROPAGATOR OF A SPHERICALLY CONFINED POLYMER  
        The propagator 
)
,
(
N
G R
 of Eq. (17) is the solution of Eq. (16) satisfying the 
boundary condition
0
)
,
(
=
=
N
D
G R
. The solution is found by first transforming Eq. 
(16) to the spherical polar coordinates 
θ
,
R
 and φ ;  when 
0
≠
N
 and 
0
R ≠
, this yields 
                
N
G
b
G
R
R
R
R
R
∂
∂
=
⎥⎦
⎤
⎢⎣
⎡
∂
∂
+
∂
∂
∂
∂
+
∂
∂
+
∂
∂
2
2
2
2
2
2
2
2
6
sin
1
sin
sin
1
2
φ
θ
θ
θ
θ
θ
             (A.1) 
which can be converted to the equation     
      
N
F
b
F
R
R
R
R
R
R
∂
∂
=
⎥⎦
⎤
⎢⎣
⎡
∂
∂
−
+
∂
∂
−
∂
∂
+
−
∂
∂
+
∂
∂
2
2
2
2
2
2
2
2
2
2
6
)
1(
1
)
1(
1
4
1
1
φ
μ
μ
μ
μ
            (A.2) 
by introducing the change of variables 
θ
μ
cos
=
 and 
G
R
F =
. In this form, Eq. (A.2) 
is readily solved by writing F in terms of variable-separated functions, i.e., as 
)
(
)
(
)
(
)
(
)
,
,
,
(
φ
μ
φ
θ
Φ
Ψ
=
M
R
N
f
N
R
F
. The substitution of this proposed solution into Eq. 
(A.2)  leads to equations for 
M
f
,
,Ψ
 and Φ  that are either trivially solvable or that can 
be recognized as the differential equations of known special functions. A general solution 
of Eq. (A.2) (and from there of Eq. (A.1)) is obtained by linearly combining the solutions 
involving 
M
f
,
,Ψ
 and Φ . In this way, we find, after some algebra, that39  
  
)
6
/
exp(
e)
(
)
/
(
2
1
)
,
,
,
(
2
2
,
,
,
2
/
1
2
/
1
Nb
P
C
D
R
y
J
A
R
N
R
G
lmn
n
m
l
im
m
l
lm
n
l
l
lmn
λ
μ
π
φ
μ
φ
−
=
∑
+
−
 (A.3) 
where 
lmn
A
 is an as yet unknown expansion coefficient,  
2
lmn
λ
, 
2
m  and 
)1
( +
l
l
are 
constants 
of 
separation, 
with 
…
,2
,1
,0
±
±
=
m
 
and 
…
,2
,1
,0
=
l
,  
)!
(
2
/
)!
)(
1
2
(
m
l
m
l
l
Clm
+
−
+
=
, 
)
(
2
/
1
"
+
lJ
 is a Bessel function of order 
2
/
1
+
l
, 
n
ly ,  is


## Page 22


22
the nth zero of 
)
(
2
/
1
"
+
lJ
 (i.e., 
0
)
(
,
2
/
1
=
+
n
l
l
y
J
), and 
)
("
m
lP
 is an associated Legendre 
polynomial.  
          To determine the explicit form of the parameters 
lmn
λ
, we substitute Eq. (A.3) into 
Eq. (A.1) (after introducing the variable change 
θ
μ
cos
=
), and simplify the resulting 
expression by using the differential equations satisfied by the Bessel and associated 
Legendre functions. These steps lead to the identification 
                                                   
2
2
,
2
/ D
y n
l
lmn =
λ
                                                            (A.4) 
The parameters 
lmn
A
 are determined by requiring that the propagator G reduce to the 
function 
)
(
)
(
)
(
0
0
0
2
μ
μ
δ
φ
φ
δ
δ
−
−
−
−
R
R
R
 when 
0
=
N
, with 
0
0,φ
R
 and 
0
μ  some 
arbitrary initial values (which subsequently will be set to 0, 0, 0.) This requirement leads 
to 
                     
0
e)
(
)
/
(
2
)
(
1
0
0
,
2
/
1
0
,
2
2
/
3
2
φ
μ
π
im
m
l
n
l
l
lm
n
l
l
lmn
P
D
R
y
J
C
R
y
J
D
A
−
+
+
=
                (A.5) 
so the complete expression for the propagator is  
       
×
=
∑
+
+
+
n
m
l
n
l
l
n
l
l
n
l
l
lm
D
R
y
J
D
R
y
J
y
J
C
RR
D
N
G
,
,
0
,
2
/
1
,
2
/
1
,
2
2
/
3
2
0
2
0
)
/
(
)
/
(
)
(
1
)
|
,
(
π
R
R
 
                                       
(
)
2
2
,
2
)
(
0
6
/
exp
e
)
(
)
(
0
D
y
Nb
P
P
n
l
im
m
l
m
l
−
×
−φ
φ
μ
μ
                       (A.6) 
To pass to the limit 
0
R →
0
 in this expression, one separates the 
0
=
l
 contribution to 
the sum from the remaining terms, substitutes the general Bessel relation 
∑
∞
=
+
+
Γ
−
=
0
2
)1
(
!
/
)
2
/
(
)
2
/
(
)
(
k
k
k
k
z
z
z
J
ν
ν
ν
 into the result, and then sets 
0
0 =
R
, thus 
producing Eq. (17).


## Page 23


23
APPENDIX B. EVALUATION OF Z1(x0) [Eq. (19a)] 
        To evaluate 
)
(
0
1 x
Z
 in closed form, we first evaluate the indefinite integral 
∫
−
−
≡
−
−
]1
)
1
[(
)
(
2
/
3
1
0
)
(
1
y
dyy
x
Z I
σ
, and then find 
)
(
0
1 x
Z
 from  
                                             
1
0
)
(
1
0
0
1
)
(
lim
)
(
ε
ε
x
Z
x
Z
I
→
=
                                                    (B.1) 
One may verify by differentiation that 
)
(
0
)
(
1
x
Z I
 is given by 
                            
(
)
(
)
y
y
y
y
x
Z I
ln
1
1
ln
1
1
ln
1
2
)
(
0
)
(
1
−
−
+
−
−
−
+
−
=
σ
σ
σ
              (B.2) 
Hence,  
         
ε
σε
σε
σ
σ
σε
σ
ε
ln
1
1
1
1
ln
1
1
1
1
ln
1
1
1
1
2
)
(
1
0
)
(
1
+
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
+
−
−
−
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
+
−
−
+
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
−
−
=
x
Z I
    (B.3) 
In the limit 
0
→
ε
, this expression becomes 
    
)
(
ln
2
ln
)
2
/
ln(
ln
1
1
1
1
ln
1
1
1
2
)
(
1
0
)
(
1
ε
ε
σ
ε
σ
σ
σ
ε
O
x
Z I
+
+
+
−
−
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
+
−
−
+
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
−
=
  (B.4)  
which, after substitution in Eq. (B.1), leads to  
                                    
σ
σ
σ
σ
ln
1
1
1
1
ln
2
ln
2
2
1
2
)
(
0
1
−
⎟⎟
⎠
⎞
⎜⎜
⎝
⎛
−
+
−
−
+
+
−
−
=
x
Z
                (B.5) 
which in turn produces  
    
(
)
eq
eq
eq
eq
R
a
R
a
R
a
a
R
x
Z
2
2
2
/
1
2
2
/
1
2
2
/
1
2
0
1
/
2
1
ln
/
2
1
/
2
1
ln
2
ln
2
2
2
)
(
−
−
⎟
⎟
⎟
⎠
⎞
⎜
⎜
⎜
⎝
⎛
+
−
+
+
−
=
         (B.6) 
after putting in the definition of σ .


## Page 24


24
REFERENCES 
1 R. Schleif, Annu. Rev. Biochem. 61, 199 (1992); J. M, G Vilar and L. Saiz Curr. 
Opinion Genetics and Development 15, 136 (2005).  
2 D. Marenduzzo, C. Micheletti and E. Orlandini, J. Phys. Cond. Mat. 22, 283102 (2010).   
3 K. Rippe, Trends Biochem. Sci. 26, 733 (2001); L. Han, H. G. Garcia, S. Blumberg, K. 
B. Towles, J. F. Beausang, P. C. Nelson and R. Phillips, PLoS ONE 4, e5621 (2009). 
4 N. Hadjichristidis, A. Hirao, Y. Tezuka and F. Du Prez, (Eds.) Complex 
Macromolecular Architectures: Synthesis, Characterization and Self-Assembly, (Wiley, 
Singapore, 2011.). 
5 G. Wilemski and M. Fixman, J. Chem. Phys. 60, 866 (1974). 
6 M. Doi, Chem. Phys. 9, 455 (1975). 
7 M. Battezzati and A. Perico, J. Chem. Phys. 74, 4527 (1981); A. Perico and M. 
Battezzati, J. Chem. Phys. 75, 4430 (1981).   
8 G. H. Weiss, J. Chem. Phys. 80, 2880 (1984) 
9 B. Friedman and B. O’Shaughnessy, Phys. Rev. Lett. 60, 64 (1988); Macromolecules 
26, 4888 (1993). 
10 R. W. Pastor, R. Zwanzig and A. Szabo, J. Chem. Phys. 105, 3878 (1996). 
11 A. Podtelezhnikov and A. Vologodskii, Macromolecules 30, 6668 (1997). 
12 L. J. Lapidus, P. J. Steinbach, W. A. Eaton, A. Szabo, and J. Hofrichter, J. Phys. Chem. 
B 106, 11628 (2002). 
13 A. Dua and B. J. Cherayil, J. Chem. Phys. 116, 399 (2002). 
14 G. Srinivas, K. L. Sebastian and B. Bagchi, J. Chem. Phys. 116, 7276 (2002). 
15 J. J. Portman, J. Chem. Phys. 118, 2381 (2003).


## Page 25


25
16 I. M. Sokolov, Phys. Rev. Lett. 90, 080601 (2003). 
17 P. Debnath and B. J. Cherayil, J. Chem. Phys. 120, 2482 (2004). 
18 J. Z. Y. Chen, H.-K. Tsao and Y.-J. Sheng, Phys. Rev. E 72, 031804 (2005); N. M. 
Toan, G. Morrison, C. Hyeon and D. Thirumalai, J. Phys. Chem. B 112, 6094 (2008). 
19 R. R. Cheng, T. Uzawa, K. W. Plaxco and D. E. Makarov, J. Phys. Chem. B 113, 
14026 (2009).  
20 R. Shusterman, S. Alon, T. Gavrinyov and O. Krichevsky, Phys. Rev. Lett. 92, 048303 
(2004); M. Weiss, M. Elsner, F. Kartberg and T. Nilsson, Biophys. J. 87, 3518 (2004); D. 
S. Banks and C. Fradin, ibid.  89, 2960 (2005); I. Bronstein, Y. Israel, E. Kepten, S. Mai, 
Y. Shav-Tal, E. Barkai and Y. Garini, Phys. Rev. Lett. 103, 018102 (2009); J. T. Mika 
and B. Poolman, Curr. Opinion Biotech. 22, 117 (2011).  
21 S. Yang and J. Cao, J. Chem. Phys. 121, 572 (2004); C. Yeung and B. Friedman, J. 
Chem. Phys. 122, 214909 (2005).  
22  S. C. Chaturvedi, in Stochastic Processes: Formalism and Applications, Lecture Notes 
in Physics, Vol. 184, ed. by G. S. Agarwal and S. Dattagupta (Springer-Verlag, 
Berlin, 1983)  
23 The angular integrations are carried out by noting that the dot product 
0
R
R ⋅
 in Eq. (4) 
can be written as
ψ
cos
0
RR
, where ψ , the angle between the vectors R  and 
0
R , is a 
function of the angular variables 
0
,
,
θ
φ
θ
 and 
0
φ . The integral over these variables 
involves the function 
ψ
h
e
, h standing for some arbitrary coefficient. This function itself 
can be rewritten identically as 
)
,
(
)
,
(
)
(
2
/
4
e
0
0
*
.
0
,
2
/
1
φ
θ
φ
θ
π
π
ψ
m
l
l
l
l
m
m
l
l
h
Y
Y
h
I
h∑∑
∞
=
−
=
+
=
, 
where 
)
(z
Iν
 is a modified Bessel function of order ν , and 
)
,
(
,
φ
θ
m
lY
 is a spherical


## Page 26


26
harmonic. Application of the formula 
0
,
0
,
0
2
0
,
4
)
,
(
sin
l
m
m
lY
d
d
δ
δ
π
φ
θ
φ
θ
θ
π
π
=
∫
∫
then 
selects out a single term corresponding to 
0
=
l
in the above double sum, and substitution 
of the result 
z
z
z
I
sinh
/
2
)
(
2
/
1
π
=
 then finally leads to Eq. (5). 
24 M. Muthukumar, Adv. Chem. Phys. 149, 129 (2012). 
25 Z. G.Wang, A. M. Nemirovsky, and K. F. Freed, J. Chem. Phys. 86, 4266 (1987); G. 
Morrison and D. Thirumalai,  ibid. 122, 194907 (2005); D. Chaudhuri and B. Mulder, 
Phys. Rev. E 83, 031803 (2011); K. F. Freed, J. Dudowicz, E. B. Stukalin and J. F. 
Douglas, J. Chem. Phys. 135, 144902 (2011).  
26  J. Kalb and B. Chakraborty, J. Chem. Phys. 130, 025103 (2009). 
27 M. Doi, S. Edwards, The Theory of Polymer Dynamics (Clarendon Press, Oxford, 
1986). 
28 K.F. Freed, Adv. Chem. Phys. 22, 1 (1972). 
29  I. S. Gradshteyn and  I. M. Ryzhik, Table of Integrals, Series, and Products,  Ed. by 
A. Jeffrey and D. Zwillinger (Academic, Burlington, 2007). 
30 K. S. Schweizer, J. Chem. Phys. 91, 5802 (1989). 
31 R. Zwanzig, Nonequilibrium Statistical Mechanics (Oxford, New York, 2001). 
32 R Sharma and B. J. Cherayil, Phys. Rev. E  81, 021804 (2010); S. C. Weber, J. A. 
Theriot and A. J. Spakowitz, Phys. Rev. E 82, 011913 (2010). 
33  H. Yang, G. Luo,  P. Karnchanaphanaruch, T. M. Louie, I. Rech, S. Cova, L.Y. Xun 
and X. S. Xie, Science 302, 262 (2003); O. Flomenbom, K. Velonia, D. Loos, S. Masuo, 
M. Cotlet, Y. Engelborghs, J. Hofkens, A. E. Rowan, R. J. M. Nolte, M. V. der 
Auweraer, F. C. de Schryver and J. Klafter, Proc. Nat. Acad. Sci. (USA)  102,  2368


## Page 27


27
(2005); W. Min, G. Luo, B. J. Cherayil, S. C. Kou and X. S. Xie, Phys. Rev. Lett. 94, 
198302 (2005). 
34 
 P. Debnath, W. Min, X. S. Xie, and B. J. Cherayil, J. Chem. Phys. 123, 204903 (2005); 
J. Tang and R. Marcus, Phys. Rev. E 73, 022102 (2006); S. Chaudhury and B. J. 
Cherayil, J. Chem. Phys. 125, 024904 (2006); S. C. Kou, Ann. Appl. Statist. 2, 501 
(2008).    
35  G.R. Kneller and K. Hinsen J. Chem. Phys. 121, 10278 (2004); W. Min and X. S. Xie, 
Phys. Rv. E 73, 010902(R) (2006); V. Calandrini, D. Abergel and G. R. Kneller, J. Chem. 
Phys. 133, 145101 (2010); Y. Cote, P. Senet, P. Delarue, G.G. Maisuradze and H. A. 
Scheraga, Proc. Natl. Acad. Sci. (USA) 107, 19844 (2010). 
36 B. Mandelbrot and J. van Ness, SIAM Rev. 10, 422 (1968); S. C. Lim and S. V. 
Muniandy, Phys. Rev. E 66, 021114 (2002); K. S. Fa and E. K. Lenzi, Phys. Rev. E 71, 
012101 (2005); I. Goychuk,  Adv. Chem. Phys. 150, 187 (2012). 
37  A. M. Mathai and H. J. Haubold, Special Functions for Applied Scientists (Springer-
Verlag, Berlin, 2008). 
38 T. Uzawa, R. R. Cheng, K. J. Cash, D. E. Makarov and K. W. Plaxco, Biophys. J. 97, 
205 (2009). 
39 M. N. Özişik, Heat Conduction  (Wiley, New York, 1993).


## Page 28


28
FIGURE CAPTIONS 
 
1. The normalized end-to-end distance correlation function 
( )t
ϕ
 as a function of the 
dimensionless time 
ζ
2
b
T
tkB
, as given by Eq. (23),  at the chain length 
100
=
N
 and  
the dimensionless reaction radius 
0.1
/
=
b
a
, for the following values of H: 0.5 (blue), 0.6 
(black), 0.65 (red), 0.7 (magenta) and 0.75 (green). .


## Page 29


29
 
 
 
 
 
 
 
 
 
 
 
 
 
FIGURE 1

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1202.4358v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1202.4358v1_Natural_Product_Xn_on_matrices

> Source: 1202.4358v1_Natural_Product_Xn_on_matrices.pdf

> Pages: 342

---


## Page 1


NATURAL PRODUCT  
n ON MATRICES  
 
 
 
 
 
W. B. Vasantha Kandasamy 
Florentin Smarandache 
 
 
 
 
 
   
 
 
 
 
 
 
  
2012


## Page 2


2
 
 
 
 
 
 
 
 
 
 
NATURAL PRODUCT  
n ON MATRICES


## Page 3


3
 
 
 
 
 
 
 
CONTENTS 
 
 
 
 
Preface 
    5 
 
 
Chapter One 
INTRODUCTION 
  
  7 
 
Chapter Two 
POLYNOMIALS WITH MATRIX COEFFICIENTS 
  
  11 
 
Chapter Three 
ALGEBRAIC COEFFICIENTS USING MATRIX  
COEFFICIENT POLYNOMIALS  
 
 
 
 
 
  
 
39 
 
Chapter Four  
NATURAL PRODUCT ON MATRICES 
  91 
 
Chapter Five  
NATURAL PRODUCT ON SUPERMATRICES 
 163


## Page 4


4
Chapter Six  
SUPERMATRIX LINEAR ALGEBRAS 
 225 
 
 
Chapter Seven  
APPLICATIONS OF THESE ALGEBRAIC  
STRUCTURES WITH NATURAL PRODUCT 
 295 
 
 
Chapter Eight 
SUGGESTED PROBLEMS 
 297 
 
 
FURTHER READING    
 337 
 
 
INDEX 
 339 
 
ABOUT THE AUTHORS 
 342


## Page 5


5
 
 
 
 
 
 
PREFACE 
 
 
 
 
In this book the authors introduce a new product on matrices called the 
natural product. We see when two row matrices of 1 × n order are 
multiplied, the product is taken component wise; for instance if X = (x1, 
x2, x3, …, xn) and Y = (y1, y2, y3, … , yn) then X × Y = (x1y1, x2y2, x3y3, 
…, xnyn) which is also the natural product of X with Y. But we cannot 
find the product of a n × 1 column matrix with another n × 1 column 
matrix, infact the product is not defined. Thus if  
 
X = 
1
2
n
x
x
x













  and  Y =  
1
2
n
y
y
y













 
under natural product  
X ×n Y = 
1
1
2
2
n
n
x y
x y
x y













. 
 
Thus by introducing natural product we can find the product of column 
matrices and product of two rectangular matrices of same order. Further


## Page 6


6
this product is more natural which is just identical with addition 
replaced by multiplication on these matrices.  
Another fact about natural product is this enables the product of any 
two super matrices of same order and with same type of partition. We 
see on supermatrices products cannot be defined easily which prevents 
from having any nice algebraic structure on the collection of super 
matrices of same type.   
This book has eight chapters. The first chapter is introductory in 
nature. Polynomials with matrix coefficients are introduced in chapter 
two. Algebraic structures on these polynomials with matrix coefficients 
is defined and described in chapter three. Chapter four introduces 
natural product on matrices. Natural product on super matrices is 
introduced in chapter five. Super matrix linear algebra is introduced in 
chapter six. Chapter seven claims only after this notion becomes popular 
we can find interesting applications of them. The final chapter suggests 
over 100 problems some of which are at research level.  
We thank Dr. K.Kandasamy for proof reading and being extremely 
supportive. 
 
 
W.B.VASANTHA KANDASAMY 
FLORENTIN SMARANDACHE


## Page 7


7
 
 
 
 
Chapter One 
 
 
 
 
INTRODUCTION 
 
 
 
 
 
 
In this chapter we only indicate as reference of those the 
concepts we are using in this book.  However the interested 
reader should refer them for a complete understanding of this 
book.   
In this book we define the notion of natural product in 
matrices so that we have a nice natural product defined on 
column matrices, m × n (m ≠ n) matrices.  This extension is the 
same in case of row matrices. 
 
We make use of the notion of semigroups and Smarandache 
semigroups refer [13]. 
 
Also the notion of semirings, Smarandache semirings, semi 
vector spaces and semifields are used, please refer [16]. 
Likewise S-rings, S-ideals, S-subrings are also used, refer  
[18].


## Page 8


8
The concept of polynomials with matrix coefficients are 
used.  That is if  
p(x) = 
i
i
i 0
a x
∞
=∑
 
 
where x is an indeterminate and if ai is a matrix (a square matrix 
or a row matrix of a column matrix or a m × n matrix m ≠ n), 
then p(x) is a polynomial in the variable x with matrix 
coefficients (‘or’ used in the mutually exclusive sense). 
Suppose  
 
p(x) = 
3
2
0
1










−


 + 
2
3
1
5
−












x + 
0
1
0
2






x3 + 
7
0
1
0






x5 
 
is a polynomial with column matrix coefficients. 
 
 
We also introduce polynomial matrix coefficient semiring.  
We call usual matrices as simple matrices.   
 
The super matrix concepts are used.  If X = (a1 a2 | a3 a4 | a5), ai 
∈ R (or Q or Z) then X is a super row matrix [8, 19]. 
 
 
If  
Y = 
1
2
3
4
5
6
a
a
a
a
a
a




















, ai ∈ R (or Q or Z)


## Page 9


9
 
then Y is a super column matrix.  
 
Let  
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x














 
 
with xi ∈ R (or Q or Z);  1 ≤ i ≤ 16 be a super square matrix.  
 
 
P = 
1
4
7
10
13
16
2
5
8
11
14
17
3
6
9
12
15
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a










  
is a super row vector. 
 
 
S = 
1
2
3
4
5
6
7
8
9
10
11
16
17
18
19
24
25
26
27
32
a
a
a
a
a
a
a
a
a
a
a
...
...
...
...
a
a
a
a
...
...
...
...
a
a
a
a
...
...
...
...
a












 
 
is a super 4 × 8 matrix (vector). 
 
Likewise


## Page 10


10
B = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a






















 with ai ∈ R (or Q or Z) 
 
is a super column vector [8, 19].   
 
 
Also we use the notion of vector spaces, Smarandache 
vector spaces and Smarandache linear algebra [17].


## Page 11


11
 
 
 
 
 
Chapter Two 
 
 
 
 
POLYNOMIALS WITH MATRIX  
COEFFICIENTS 
 
 
 
 
 
In this chapter we define polynomials in the variable x with 
coefficients from the collection of matrices of same order.  We 
call such polynomials as matrix coefficient polynomials or 
polynomials with matrix coefficients.  We first give some 
examples before we define operations on them. 
 
Example 2.1:  Let p(x) = (5, 3, 0, –3, 2) + (0, 1, 2, 3, 4)x + (7, 
0, 1, 0, 1)x2 + (–7, –9, 10, 0, 0)x5 – (3, 2, 1, 2, 1)x7; we see p(x) 
is a polynomial in the variable x with row matrix coefficients. 
 
Example 2.2:  Let m(x) = 
1
2
3
0
0








 +  
1
2
3
4
5
−




−












x +
6
0
1
2
0








x2 + 
1
1
2
2
3




−






−






x5 be a 
column matrix coefficient polynomial or a polynomial with 
column matrix coefficients.


## Page 12


12
Example 2.3:  Let  
 
p(x) = 
3
0
1
2




−


 + 1
0
0
2






x2 + 0
1
0
3






x3 + 1
0
4
0






x5 + 
 
1
4
0
0






x8 + 0
0
1
2






x9 + 0
1
5
0






x10 
 
be a square matrix coefficient polynomial. 
 
Example 2.4:  Let  
 
T(x) = 
2
1
0
1
5
2










 + 
1
0
1
1
1
0










x + 
1
2
0
3
4
0










x3 + 
9
1
0
2
6
0










x7 
 
be a polynomial with 3 × 2 matrix coefficient.   
 
Now we define some operations on the collection. 
 
DEFINITION 2.1:  Let  
VR = 
∞
=

∑
i
i
i 0
a x  ai = (x1,…, xn) 
are 1 × n row matrices, xi ∈ R (or Q or Z); 1 ≤ i ≤ n} be the 
collection of all row matrix coefficient polynomials.  VR is a 
group under addition. 
 
 
For if p(x) = 
∞
=∑
i
i
i 0
a x  and q(x) = 
∞
=∑
j
j
j 0
b x  then  
we define p(x) + q(x) =
∞
=∑
i
i
i 0
a x  + 
∞
=∑
j
j
j 0
b x   
 
= 
∞
=
+
∑
i
i
i
i 0
( a
b )x


## Page 13


13
 
0 = (0,…,0) + (0,…,0)x + … + (0,… ,0)xn (n ∈ N) is 
defined as the row matrix coefficient zero polynomial. 
 
Let p(x) =
∞
=∑
i
i
i 0
a x  now –p(x) = 
∞
=
−
∑
i
i
i 0
a x  is defined as 
the inverse of the row matrix coefficient polynomial. Thus (VR, 
+) is an abelian group of infinite order. 
 
 
Example 2.5:  Let  
 
VR = 
i
i
i 0
a x
∞
=

∑
 ai = (x1, x2, x3, x4) with xj ∈ Q; 1 ≤ j ≤ 4} 
 
be the collection of row matrix coefficient polynomials VR is a 
group under addition.   
 
For if p(x) = (0, 2, 1, 0) + (7, 0, 1, 2)x + (1, 1, 1, 1)x3 +  
(0, 1, 2, 0)x5 and  
 
q(x) =  (7, 8, 9, 10) + (3, 1, 0, 7)x + (3,0,1, 4)x3 – (4, 2, 3, 
4)x4 + (7, 1, 0, 0)x5 + (1, 2, 3, 4)x8 are in VR then  
 
p(x) + q(x) = ((0, 2, 1, 0) + (7, 8, 9, 10)) + ((7, 0, 1, 2) + (3, 
1, 0, 7))x + ((1, 1, 1, 1) + (3, 0, 1, 4))x3 + ((0, 0, 0, 0) – (4, 2, 3, 
4))x4 + ((0, 1, 2, 0) + (7, 1, 0, 0))x5 + (1, 2, 3, 4)x8  
 
= (7, 10, 10, 10) + (10, 1, 1, 9)x + (4, 1, 2, 5)x3 – (4, 2, 3, 
4)x4 + (7, 2, 2, 0)x5 + (1, 2, 3, 4)x8. 
 
We see –p(x) = (0, –2, –1, 0) + (–7, 0, –1, –2)x + (–1, –1,  
–1, –1)x3 + (0, –1, –2, 0)x5 acts as the additive inverse of p(x).


## Page 14


14
Example 2.6:  Let  
 
VR = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, x3); xj ∈ Z12; 1 ≤ j ≤ 3} 
 
be the collection of all row coefficient polynomials.  VR is a 
group under modulo addition 12. 
 
Example 2.7:  Let  
 
VR = 
10
i
i
i 0
a x
=


∑
 ai = (d1, d2) with dj ∈ Q; 1 ≤ j ≤ 2} 
 
be the row coefficient polynomial.  VR is a group under 
addition. 
 
Example 2.8:  Let  
 
VR = 
5
i
i
i 0
a x
=


∑
 ai = (x1, x2); x1, x2 ∈ Z10} 
be the row coefficient polynomial.  VR is a finite group under 
addition. 
 
 
We now can define other types of operations on VR. 
 
 
We see if (1,1,1,1)x3 – (0, 0, 8, 27) = p(x) then (1,1,1,1)x3 – 
(0, 0, 2, 3)3 = p(x) 
 
= [(1, 1, 1, 1)x – (0, 0, 2, 3)] [(1, 1, 1, 1)x2 + (0, 0, 2, 3)x + 
(0, 0, 4, 9)]. 
 
 
For this we have to define another operation on VR called 
product. 
 
 
Throughout this book VR will denote polynomial with row 
matrix coefficient in the variable x.


## Page 15


15
 
We know VR is a group under addition. 
 
 
Now we can define product on VR as follows: 
 
 
Let p(x) = (0,1,2) + (3,4,0)x + (2,1,5)x2 + (3,0,2)x3  and  
 
q(x) = (6,0,2) + (0,1,4)x + (3,1,0)x2 + (1,2,3)x4 be in VR. 
 
 
We define product of p(x) with q(x) as follows. 
 
 
p(x) × q(x)  
 
=  [(0,1,2) + (3,4,0)x+ (2,1,5)x2 + (3,0,2)x3] × [(6,0,2) + 
(0,1,4)x + (3,1,0)x2 + (1,2,3)x4]  
 
= 
(0,1,2) (6,0,2) + (3,4,0) (6,0,2)x+(2,1,5) (6,0,2)x2 + 
(3,0,2) (6,0,2)x3 + (0,1,2) (0,1,4)x + (3,4,0) (0,1,4)x2 + 
(2,1,5) (0,1,4)x3 + (3,0,2) (0,1,4)x4 + (0,1,2) (3,1,0)x2 + 
(3,4,0) (3,1,0)x3 + (2,1,5) (3,1,0)x4 + (3,0,2) (3,1,0)x5 + 
(0,1,2) (1,2,3)x4 + (3,4,0) (1,2,3)x5 + (2,1,5) (1,2,3)x6 + 
(3,0,2) (1,2,3)x7  
 
=  (0,0,4) + (18,0,0)x + (12,0,10)x2 + (18,0,4)x3 + (0,1,8)x 
+ (0,4,0)x2 + (0,1,20)x3 + (0,0,8)x4 + (0,1,0)x2 + 
(9,4,0)x3 + (6,1,0)x4 + (9,0,0)x5 + (0,2,6)x4 + (3,8,0)x5 
+(2,2,15)x6 + (3,0,6)x7  
 
= 
(0,0,4) + (18,1,8)x + (12,5,10)x2 + (27,5,24)x3 + 
(6,3,14)x4 + (12,8,0)x5 + (2,2,15)x6 + (3,0,6)x7. 
 
 
Now we see with componentwise product we see VR under 
product is a commutative semigroup.  
 
 
We see VR has zero divisors.  
 
 
Now we proceed onto give one or two examples.


## Page 16


16
 
Example 2.9:  Let  
 
VR = 
5
i
i
i 0
a x
=


∑
 ai = (x1, …, x8); xi ∈ Q; 1 ≤ i ≤ 8} 
be a semigroup of row matrix polynomials.  VR is a monoid 
under product.  
 
 
Now we see (VR, +, ×) is a commutative ring of 
polynomials with row matrix coefficients.   
 
We give examples of them. 
 
Example 2.10:  Let  
 
VR = {p(x) = 
i
i
i 0
a x
∞
=∑
; aj = (x1, x2…, x18); xi ∈ R; 1 ≤ i ≤ 18} 
be a ring of polynomials with row matrix coefficients. 
 
 
Now we have shown examples of polynomial row matrix 
coefficients in the variable x. 
 
 
Example 2.11:  Let  
VC = 
i
i
i 0
a x
∞
=


∑
 aj =
1
2
3
4
5
x
x
x
x
x
















with xi ∈ Z; 1 ≤ i ≤ 5}, 
VC is a group under addition.  
 
p(x)  = 
3
0
1
0
2








 + 
1
0
0
2
0








x + 
0
1
2
3
0








x2 and


## Page 17


17
 
q (x) = 
4
2
1
4
0










−






 + 
2
3
4
5
0








x + 
2
3
1
4
5








x2 +
2
1
1
0
4




−












x3 + 
2
1
2
3
0




−












x4 be in VC. 
 
 
p(x) + q(x) = 
3
0
1
0
2








+
4
2
1
4
0










−






 + 
1
2
0
3
x
0
4
2
5
0
0








+








+
2
0
2
1
3
x
2
1
3
4
0
5
















+
















  
 
+ 
2
1
1
0
4




−












x3 + 
2
1
2
3
0




−












x4 
 
 
= 
7
3
2
3
x
2
4
4
7
2
0












+
+



−









2
4
3
7
5








x2 + 
2
1
1
0
4




−












x3 + 
2
1
2
3
0




−












x4 is in VC.   
 
Thus VC is a commutative group under addition.  
 
We see on VC we cannot define product for it is not defined.


## Page 18


18
Thus  
 
VC = 
i
i
i 0
a x
∞
=


∑
 ai =
1
2
n
x
x
x













; xi ∈ Q (or R or Z) ; 1 ≤ i ≤ n} 
is an abelian group under addition with polynomials whose 
coefficients are column matrices.   
 
Now Vn×m denotes the collection of all polynomials whose 
coefficients are n×m matrices.  Vn×m is a group under addition. 
 
Now if m ≠ n then on Vn×m we cannot define product.  We 
will illustrate this situation by an example. 
 
Example 2.12:  Let  
 
V5×3 = 
i
i
i 0
a x
∞
=


∑
 aj =
1
6
11
2
7
12
3
8
13
4
9
14
5
10
15
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
















where xi ∈ R; 1 ≤ i ≤ 15} 
be the group of polynomials under addition whose coefficients 
are 5×3 matrix. 
 
  
Example 2.13:  Let  
 
V2×4 = 
i
i
i 0
a x
∞
=


∑
 ai =
1
2
3
4
5
6
7
8
y
y
y
y
y
y
y
y






 
 
where yi ∈ R; 1 ≤ i ≤ 8} 
 
be the group of polynomials under addition whose coefficients 
are 2 × 4 matrices (aij ∈ R; 1 ≤ i ≤ n, 1 ≤ j ≤ m).


## Page 19


19
Thus we can say  
Vn×m = 
i
i
i 0
a x
∞
=


∑
ai = 
11
12
1m
21
22
2m
n1
n2
nm
a
a
...
a
a
a
...
a
a
a
...
a















} 
is the group of polynomials in the variable x with coefficients  
as n × m matrices.  Clearly if n ≠ m we cannot define product on 
Vn×m. 
 
 
Now we can define product on Vn×n, that is when n = m. We 
first illustrate this by an example. 
 
Example 2.14:  Let  
Vn×n = 
i
i
i 0
a x
∞
=


∑
 ai =
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a















 
 
where aij ∈ R; 1 ≤ i, j ≤ n} 
 
be the group of polynomials under addition with n × n square 
matrix coefficients.  We see on Vn×n, one can define product. 
Vn×n is only a semigroup which is non commutative.   
 
We will illustrate this situation by examples. 
 
Example 2.15:  Let  
 
V3×3 = 
i
i
i 0
a x
∞
=


∑
 ai =
1
2
3
4
5
6
7
8
9
x
x
x
x
x
x
x
x
x










where xi ∈ Q; 1 ≤ i ≤ 9} 
 
be the group of polynomials in the variable x with coefficients 
from 3 × 3 matrices.


## Page 20


20
 
We will show how addition in V3×3 is carried out.  
 
 
Let p(x) = 
0
3
2
1
0
0
0
0
4
−










 + 
2
1
0
3
0
2
1
2
3










x2 + 
0
1
2
1
2
0
2
1
0










x3  
 
and  
 
q(x) = 
1
2
1
0
1
3
6
1
2








−


 + 
1
2
3
0
1
5
5
0
1








−


x + 
1
2
3
2
3
1
3
2
1
−




−




−


x2 +  
 
0
1
0
9
0
1
0
2
3










x3 be in V3×3. 
 
 
p(x) + q(x)  = 
0
3
2
1
0
0
0
0
4
−










+
1
2
1
0
1
3
6
1
2








−


+ 
1
2
3
0
1
5
5
0
1








−


x  
 
+ 
2
1
0
1
2
3
3
0
2
2
3
1
1
2
3
3
2
1


−










+ −












−






x2 
 
+ 
0
1
2
0
1
0
1
2
0
9
0
1
2
1
0
0
2
3












+


















x3 
 
= 
1
5
1
1
1
3
6
1
6
−








−


 + 
1
2
3
0
1
5
5
0
1








−


x +


## Page 21


21
1
3
3
1
3
3
2
4
4








−


x2 + 
0
2
2
10
2
1
2
3
3










x3. 
 
We see V3×3  is an abelian group under addition. 
 
Example 2.16:  Let  
 
V2×2 = 
i
i
i 0
a x
∞
=


∑
 ai =
1
2
3
4
x
x
x
x






; xi ∈ R; 1 ≤ i ≤ 4} 
be the semigroup of polynomials in the variable x with 
coefficients from the collection of all 2 × 2 matrices under 
product.  
 
p(x) = 1
2
0
4






 + 0
1
2
3






x + 1
2
3
0






x2 and 
 
q(x) = 0
1
2
0






 + 1
0
2
3






x + 1
2
3
4






x3 be in V3×3. 
 
 
 
Now  
p(x) . q(x) = 1
2
0
4






 0
1
2
0






 + 0
1
2
3






1
0
2
0






x + 
 
1
2
3
0






0
1
2
0






x2 + 1
2
0
4






 1
2
2
3






 x 
 
+ 0
1
2
3






1
0
2
3






x2 + 1
2
3
0






1
0
2
3






x3 
 
+ 1
2
0
4






 1
2
3
4






x3 + 0
1
2
3






 1
2
3
4






x4


## Page 22


22
 
+ 1
2
3
0






1
2
3
4






 x5 + 4
1
8
0






 + 2
0
6
2






x 
 
+ 4
1
0
3






x2 + 5
6
8
12






x + 2
3
8
9






x2 
 
+ 5
6
3
0






x3 + 
7
10
12
16






x3 + 
3
4
11 16






x4 + 7
10
3
6






x5 
 
= 4
1
8
0






 + 
7
6
14
14






 x + 6
4
8
12






x2 + 12
16
15
16






x3 +  
 
3
4
11 16






x4 + 7
10
3
6






x5. 
 
 
This is the way product is defined. Thus V2×2 is a semigroup 
under multiplication.  
 
 
V2×2 is a monoid and infact V2×2 has zero divisors. 
 
 
This is a polynomial ring. 
 
Example 2.17:  Let  
V4×4 = 
i
i
i 0
a x
∞
=


∑
 ai =
11
12
13
14
21
22
23
24
31
32
33
34
41
42
43
44
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a












 
 
where aij ∈ R; 1 ≤ i, j ≤ 4} 
 
be a group of polynomials in the variable x with 4 × 4 matrices 
as coefficients.


## Page 23


23
 
V4×4 is a group under addition and V4×4 is a semigroup under 
product (V4×4, +, ×) is a ring which is non commutative.  This 
ring has zero divisors and units and all p(x) of degree greater 
than or equal to one have no inverse. 
 
Example 2.18:  Let  
 
V2×2 = 
i
i
i 0
a x
∞
=


∑
 ai =
11
12
21
22
a
a
a
a






;aij ∈ R; 1 ≤ i, j ≤ 2} 
 
be the ring of polynomials with 2×2 matrix coefficients in the 
variable x. V2×2 is non commutative and has zero divisors and 
no p(x) ∈V2×2, of degree greater than one has inverse.  We 
cannot have idempotent in them.   
 
 
We can differentiate and integrate these polynomials with 
matrix coefficients apart from finding roots in them.   
 
Now we first illustrate this situation by some examples.  
 
Example 2.19:  Let  
 
p(x) = 3
0
1
2






 + 2
6
1
5






x + 7
0
0
8






x2 – 3
1
0
0






x3  
 
+ 8
1
0
1






x4 – 
0
4
2
0




−


x5 
 
be a polynomial in matrix coefficients or matrix coefficient 
polynomial. 
 
 
To find the derivative of p(x).


## Page 24


24
 
dp(x)
dx
 = 0 + 2
6
1
5






 + 2 7
0
0
8






x – 3 3
1
0
0






x2 
 
+ 4 8
1
0
1






x3 – 5 
0
4
2
0




−


x4 
 
= 2
6
1
5






 + 14
0
0
16






x – 9
3
0
0






x2 
 
+ 32
4
0
4






x3 – 
0
20
10
0




−


x4. 
 
We see dp(x)
dx
 is again a matrix coefficient polynomial in 
the variable x. 
 
 
We can find the second derivative of p(x).   
 
Consider  
 
2
d p(x)
dx
 = 14
0
0
16






 – 2 9
3
0
0






x 
 
+ 3 32
4
0
4






x2 – 4
0
20
10
0




−


x3 
 
= 14
0
0
16






 – 18
6
0
0






x + 96
12
0
12






x2 – 
0
80
40
0




−


x3. 
 
 
Clearly 
2
d p(x)
dx
 also belongs to the collection of 2 × 2 
matrix coefficient polynomials.


## Page 25


25
Example 2.20:  Let  
 
V2×4 =
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
x
x
x
x
x
x
x
x






 
 
where xi ∈ R; 1 ≤ i ≤ 8} 
 
be the 2 × 4 matrix coefficient polynomial. 
 
Let p(x) = 1
0
2
4
0
3
0
5






 + 3
1
5
2
0
4
0
5






x 
 
+ 
3
4
2
4
0
0
0
3
−






x3 + 1
1
0
2
2
0
2
0
−




−


x4 
 
be a 2 × 4 matrix coefficient polynomial.  To find the derivative 
of p(x). 
 
dp(x)
dx
 = 3
1
5
2
0
4
0
5






 + 3
3
4
2
4
0
0
0
3
−






x2 
 
+ 4 1
1
0
2
2
0
2
0
−




−


x3 
 
= 3
1
5
2
0
4
0
5






 + 
9
12
6
12
0
0
0
9
−






 
 
+ 4
4
0
8
8
0
8
0
−




−


x3. 
 
 
Clearly dp(x)
dx
 is in V2×4.


## Page 26


26
Consider  
 
2
2
d p(x)
dx
 = 2 
9
12
6
12
0
0
0
9
−






x + 3 4
4
0
8
8
0
8
0
−




−


x2 
 
= 
18
24
12
24
0
0
0
18
−






x + 12
12
0
24
24
0
24
0
−




−


x2. 
 
 
We see 
2
2
d p(x)
dx
 ∈ V2×4. 
 
 
If we consider the third derivative of p(x);  
 
3
3
d p(x)
dx
 = 
18
24
12
24
0
0
0
18
−






 + 
 
2 12
12
0
24
24
0
24
0
−




−


x 
 
= 
18
24
0
24
0
0
0
18
−






 + 24
24
0
48
48
0
48
0
−




−


x. 
 
 
We see 
3
3
d p(x)
dx
 ∈ V2×4. 
 
 
Further the forth derivative. 
 
4
4
d p(x)
dx
 = 24
24
0
48
48
0
48
0
−




−


 ∈V2×4. 
 
 
However the fifth derivative 
5
5
d p(x)
dx
is zero.


## Page 27


27
 
Example 2.21:  Let  
 
VR =
i
i
i 0
a x
∞
=


∑
 ai = (x1, …, x6); xi ∈ Z; 1 ≤ i ≤ 6} 
 
be a row matrix coefficient polynomial.   
 
p(x) =  (2,0,1,0,1,5) + (3,2,1,0,0,0)x + (0,1,0,2,0,4)x2  
+ (0,–2,–3,0,0,0)x3 + (8,0,7,0,1,0)x5 be in VR.   
 
To find the derivative of  
 
p(x) = dp(x)
dx
  
 
= 0 + (3,2,1,0,0,0) + 2(0,1,0,2,0,4)x + 3(0,–2,–3,0,0,0)x2 + 
5(8,0,7,0,1,0)x4 
 
 
= (3,2,1,0,0,0) + (0,2,0,4,0,8)x + (0,–6,–9, 0,0,0)x2 + 
(40,0,35,0,5,0)x4. 
 
 
We see dp(x)
dx
 is in VR. 
 
2
2
d p(x)
dx
=    (0,2,0,4,0,8) + 2 (0, –6,–9,0,0,0)x  
      + 4 (40,0,35,0,5,0)x3 
 
 
= (0,2,0,4,0,8) + (0,–12,–18,0,0,0)x + (160,0,140,0,20,0)x3. 
 
 
Clearly 
2
2
d p(x)
dx
 ∈ VR.


## Page 28


28
Example 2.22:  Let  
 
VC = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
x
x
x
x












 where xi ∈ Q; 1 ≤ i ≤ 4} 
 
be a 4 × 1 column matrix coefficient polynomial. 
 
 
Let p(x) = 
2
0
4
0






 + 
3
2
1
4










−


x + 
0
1
2
3






x3 + 
4
5
2
1






x6 belongs to VC.  
 
dp(x)
dx
 = 
3
2
1
4










−


 + 3 
0
1
2
3






x2 + 6 
4
5
2
1






x5   
 
= 
3
2
1
4










−


 + 
0
3
6
9






x2 + 
24
30
12
6












 x5 ∈ VC. 
 
2
2
d p(x)
dx
 = 2
0
3
6
9






x + 5 
24
30
12
6












 x4


## Page 29


29
 
 
 
 
 
 
= 
0
6
12
18












x + 
120
150
60
30












x4 ∈ VC. 
 
  
3
3
d p(x)
dx
 = 
0
6
12
18












 + 4
120
150
60
30












x3  
 
 
 
= 
0
6
12
18












 + 
480
600
240
120












x3 ∈ VC. 
 
 
4
4
d p(x)
dx
 = 3
480
600
240
120












 x2 = 
1440
1800
720
360












x2 ∈ VC. 
 
Thus we see VC, Vm×n, Vn×n and VR are such that the first 
derivative and all higher derivatives are in VC, Vm×n, Vn×n and 
VR. 
 
Now we discuss about the integration of matrix coefficient 
polynomials.


## Page 30


30
Example 2.23:  Let  
 
p(x) = 
3
0
1
5
6
0
1
0
8










 + 
0
2
1
6
1
0
1
2
6










x  
 
+ 
8
0
0
0
7
0
0
0
11










x2 + 
0
0
2
0
9
0
10
0
0










x3. 
 
 
To integrate p(x) . ∫p(x)dx = 
3
0
1
5
6
0
1
0
8










x + ½ 
0
2
1
6
1
0
1
2
6










x2 +  
 
1/3 
8
0
0
0
7
0
0
0
11










x3 + 1/4 
0
0
2
0
9
0
10
0
0










 x4 + 
 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a










3
0
1
5
6
0
1
0
8










x + 
0
1
1/ 2
3
1/ 2
0
1/ 2
1
3










x2 + 
 
8/3
0
0
0
7/3
0
0
0
11/3










x3 + 
0
0
1/ 2
0
9/ 4
0
5/ 2
0
0










x4 + 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a










. 
 
Example 2.24: Let  
 
p(x) = (1,2,3,4,5) + (0,1,0,3,–1)x + (5,0,8,1,7)x2  
+ (1,2,0,4,5)x3 + (–2, 1,4,3,0)x4 
 
be a row matrix coefficient polynomial.


## Page 31


31
To integrate p(x), ∫p(x)dx  
=  (1,2,3,4,5)x + ½ (0,1,0,3,–1)x2 + 1/3(5,0,8,1,7)x3  
    + 1/4 (1,2,0,4,5)x4 + 1/5(–2,1,4,3,0)x5 + (a1,a2,a3,a4,a5)  
    ai ∈ Q; 1 ≤ i ≤ 5. 
 
 
=  (1,2,3,4,5) + (0,1/2,0,3/2, -1/2)x2 + (5/3,0,8/3,1/3,7/3)x3  
    + (1/4,1/2,0,1,5/4)x4 + (–2/5, 1/5,4/5,3/5,0)x5  
    + (a1,a2,a3,a4,a5). 
 
Example 2.25:  Let  
 
p(x) = 
3
0
1
2
4
5










 + 
0
1
2
0
4
8










x + 
1
0
9
8
7
0
−








−












x3 + 
7
8
9
10
3
7




















x4 + 
8
2
4
5
5
10




















x5 
 
be a column matrix polynomial. 
 
 
∫p(x)dx = 
3
0
1
2
4
5










x + 1/2
0
1
2
0
4
8










x2 + 1/4
1
0
9
8
7
0
−








−












x4  
 
+ 1/5 
7
8
9
10
3
7




















x5 + 1/6 
8
2
4
5
5
10




















x6 + 
1
2
3
4
5
6
a
a
a
a
a
a






















## Page 32


32
 
 
= 
3
0
1
2
4
5










x + 
0
1/ 2
1
0
2
4




















x2 + 
1/ 4
0
9/ 4
2
7/ 4
0
−








−












x4 + 
7 /5
8/5
9/5
2
3/5
7 /5




















x5 + 
4/3
1/3
2/3
5/ 6
5/ 6
5/3




















x6 + 
1
2
3
4
5
6
a
a
a
a
a
a




















. 
 
 
Example 2.26:  Let  
 
p(x) = 0
2
1
4
6
0
1
0






 + 3
6
2
9
0
2
1
7






x + 0
2
4
4
2
0
1
2






x3 
 
+ 2
1
0
0
0
0
1
2






x4 + 0
1
2
0
6
0
0
3






x5. 
 
 
We find the integral of p(x). 
 
∫p(x)dx = 0
2
1
4
6
0
1
0






x + 1/2 3
6
2
9
0
2
1
7






x2 
 
+ 1/4 0
2
4
4
2
0
1
2






x4 + 1/5 2
1
0
0
0
0
1
2






x5 
 
+ 1/6 0
1
2
0
6
0
0
3






x6 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a






  
 
= 0
2
1
4
6
0
1
0






x + 3/ 2
3
1
9/ 2
0
1
1/ 2
7 / 2






x2


## Page 33


33
+ 
0
1/ 2
1
1
1/ 2
0
1/ 4
1/ 2






x4 + 2/5
1/5
0
0
0
0
1/5
2/5






x5 
 
+ 0
1/6
1/3
0
1
0
0
1/ 2






x6 + 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a






. 
 
 
We see VC, VR, Vn×m and Vn×n under integration is closed, 
provided the entries of the coefficient matrices take their values 
from Q or R.  If they take the from Z they are not closed under 
integration only closed under differentiation.   
 
We will illustrate this situation by a few examples. 
 
Example 2.27:  Let  
 
p(x) = (3, 8, 4, 0) + (2, 0, 4, 9)x + (1, 2, 1, 1)x2 + (1, 0, 1, 
1)x3 + (3, 4, 8, 9)x5 where the coefficients are 1 × 4 row 
matrices with entries from Z.   
We find integral of p(x).  
∫p(x)dx =  (3, 8, 4, 0)x + 1/2(2, 0, 4, 9)x2 + 1/3(1, 2, 1, 1)x3  
    + 1/4(1, 0, 1, 1)x4 + 1/6(3, 4, 8, 9)x6. 
 
 
We see (1, 0, 2, 9/4), (1/3, 2/3, 1/3, 1/3), (1/4, 0, 1/4, 1/4), 
(1/2, 2/3, 4/3, 3/2) ∉ Z × Z × Z × Z.  Thus we see integral of 
matrix coefficient polynomials with matrix entries from Z are 
not closed under intervals that is ∫p(x)dx ∉ VC or VR or Vn×n or 
Vm×n if the entries are in Z. 
 
Example 2.28:  Let  
 
p(x) = 
2
3
4
0






 + 
1
2
3
4






x + 
0
0
1
1






x2 + 
0
1
0
3






x3 + 
3
0
0
4






x4 where 
1
2
3
4
a
a
a
a












 
are 4 × 1 column matrix with entries from Z; that is ai ∈ Z;  
1 ≤ i ≤ 4.


## Page 34


34
 
∫p(x) dx =  
2
3
4
0






 x + 1/2 
1
2
3
4






x2 +1/3 
0
0
1
1






x3  
 
+ 1/4
0
1
0
3






x4 + 1/5 
3
0
0
4






x5 + 
1
2
3
4
a
a
a
a












 
 
= 
2
3
4
0






 x + 
1/ 2
1
3/ 2
2












x2 +
0
0
1/3
1/3












x3 + 
0
1/ 4
0
3/ 4












x4 
 
+ 
3/5
0
0
4/5












x5 + 
1
2
3
4
a
a
a
a












. 
 
 
Clearly these column matrices do not take their entries from 
Z. 
 
Example 2.29:  Let  
 
p(x) = 3
0
1
1
6
6
0
0






 + 1
2
0
0
0
1
0
2






x + 3
0
0
1
0
2
2
0






x2  
 
+ 2
1
1
0
0
2
0
1






x3 + 1
0
1
0
0
1
0
1






x4 
 
where the coefficient of these are 2 × 4 matrices and they take 
their values from Z.


## Page 35


35
 
∫p(x)dx = 3
0
1
1
6
6
0
0






x + 1/2 1
2
0
0
0
1
0
2






x2 
 
+ 1/3 3
0
0
1
0
2
2
0






x3 + 1/4 2
1
1
0
0
2
0
1






x4 
 
+ 1/5 1
0
1
0
0
1
0
1






x5 + 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a






 ai ∈ Z; 1 ≤ i ≤ 8. 
 
 
∫ p(x)dx = 3
0
1
1
6
6
0
0






x + 1/ 2
1
0
0
0
1/ 2
0
1






x2  
 
+ 1
0
0
1/3
0
2/3
2/3
0






x3 +  1/ 2
1/ 4
1/ 4
0
0
1/ 2
0
1/ 4






x4  
 
+ 1/5
0
1/5
0
0
1/5
0
1/5






x5 + 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a






. 
 
In view of this we have the following theorems. 
 
 
THEOREM 2.1:  Let VR (or VC or Vn×m or Vm×m) be the matrix 
coefficient polynomials with matrix entries from C or Z or R or 
Q.  The derivatives of every polynomial in VR (or VC or Vn×m or 
Vm×m) is in VR (or VC or Vn×m or Vm×m). 
 
 
The proof is simple and hence is left as an exercise to the 
reader. 
 
THEOREM 2.2:  Let VR (or VC or Vn×m or Vm×m) be the matrix 
coefficient polynomial with matrix entries from Z.  The integrals 
of every matrix coefficient polynomial need not be in VR.


## Page 36


36
COROLLARY 1:  If in theorem, Z is replaced by Q or R or C 
then every integral of the matrix coefficient polynomial is in VR 
(or VC or Vn×m or Vm×m). 
 
 
Now we find or show some polynomial identities true in 
case of matrix coefficient polynomials. 
 
 
Consider (1, 1, 1, 1, 1)x2 – (4, 9, 16, 25, 81) = (0) in VR = 
i
i
i 0
a x
∞
=


∑
 a = (x1, x2, x3, x4, x5) with xi ∈ Z or Q or C or R; 1 ≤ i 
≤ 5}. Given (1, 1, 1, 1, 1)x2 – (4, 9, 16, 25, 81) = (0). 
 
 
((1, 1, 1, 1, 1)x – (2, 3, 4, 5, 9)) ×((1, 1, 1, 1, 1)x + (2, 3, 4, 
5, 9)) = (0) 
 
 
Thus x = (2,3,4,5,9) or – (2,3,4,5,9). 
 
 
Take the matrix coefficient polynomial  
(1,1,1)x3 – (27,8,125) = (0) 
 
 
We can factorize (1,1,1)x3 – (27,8,125) = 0 as  
[(1,1,1)x – (3,2,5)] [(1,1,1)x2 + (3,2,5)x + (9,4,25)]. 
 
 
Take (1,1,1,1)x4 – (16,81,625,16) = (0) 
 
 
We can factorize this polynomial as [(1,1,1,1)x2 + 
(4,9,25,4)] [(1,1,1,1)x2 – (4,9,25,4)] = (0,0,0,0) 
 
 
x2 = – (4,9,25,4) 
 
and x2 = (4,9,25,4), we see now x2 = (4,9,25,4) can be yet 
solved as x = + (2,3,5,2), we see however x2 = – (4,9,25,4) gives 
a imaginary value for x.  If VR is defined over R or Z or Q we 
see the solution does not exist; that is the equation is not linearly 
solvable over R or Z or Q but linearly solvable over VC.


## Page 37


37
 
Now we see yet another equation  
p(x) = (1,1,1,1)x2 + (4,4,4,4)x + (4,4,4,4) = (0) where p(x) is 
a matrix coefficient polynomial in the variable x over Z. 
 
x = 
2
(4,4,4,4)
(4,4,4,4)
4
(1,1,1,1)(4,4,4,4)
(2,2,2,2)




 
 
= 
(4,4,4,4)
(0)
(2,2,2,2)


 
 
= 
(4,4,4,4)
(2,2,2,2)

 = – (2,2,2,2). 
 
 
Thus p(x) has coincident roots. 
 
 
Consider (1,1,1)x3 – (6,3,9)x2 + (12,3,27)x + (8,1,27)  
 
 
= p(x) = (0,0,0) be a matrix coefficient polynomial.  
 
 
To find the roots of p(x). 
 
p(x)  = (1,1,1)x3 – 3(2,1,3)x2 + 3(4,1,9)x – (8,1,27) 
 
= ((1,1,1)x – (2,1,3))3. 
 
Thus x = (2,1,3), (2,1,3) and (2,1,3).  
 
Now p(2,1,3) = (1,1,1) (2,1,3)3 – 3(2,1,3) (2,1,3)2 + 3(2,1,3)2 
(2,1,3) – (2,1,3)3 
 
 
= (0,0,0). 
 
 
We can also find equation with matrix coefficient 
polynomials as follows:


## Page 38


38
Consider  
 
1
0
2
1
x
0
1
0
2






−












 
1
0
3
7
x
0
1
0
1






+












 = p(x). 
 
 
Clearly p 2
1
0
2






 = (0) and p 3
7
0
1






 = (0). 
 
 
We can consider any product of linear polynomial with 
matrix coefficients.  However we see it is difficult to solve 
equations in the matrix coefficients as even solving equations in 
usual polynomials is not an easy problem. 
 
 
Now having seen the properties of matrix coefficients 
polynomials we now proceed onto discuss other properties 
associated with it.


## Page 39


39
 
 
 
 
 
Chapter Three 
 
 
 
 
ALGEBRAIC STRUCTURES USING MATRIX 
COEFFICIENT POLYNOMIALS 
 
 
 
 
 
In this chapter we introduce several types of algebraic 
structures on these matrix coefficient polynomials and study 
them.  
 
 
Throughout this chapter VR denotes the collection of all row 
matrix coefficient polynomials.  VR = 
i
i
i 0
a x
∞
=


∑
 ai = (y1, …, yn) 
where yi ∈ R (or Q or C or Z); 1 ≤ i ≤ n and x an 
indeterminate}. 
 
 
VC denotes the collection of all column matrix coefficient 
polynomials; that is VC = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
m
x
x
x













; xj ∈ R (or Q or 
C or Z) 1 ≤ j ≤ m}.


## Page 40


40
 
Now Vn×m = 
i
i
i 0
a x
∞
=


∑
 ak = 
11
1m
21
2m
n1
nm
a
...
a
a
...
a
a
...
a















aij ∈ R (or Q or 
Z or C); 1 ≤ i ≤ n; 1 ≤ j ≤ m} denotes the collection of all n × m 
matrix coefficient polynomial. 
 
 
Finally Vn×n = 
i
i
i 0
a x
∞
=


∑
 ak = 
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a















 with aij 
∈ R (or Q or Z or C); 1 ≤ i, j ≤ n} denotes the collection of all  
n × n matrix coefficient polynomial. 
 
 
We give algebraic structures on them. 
 
THEOREM 3.1:  VR, VC, Vn×m and Vn×n (m ≠ n) are groups under 
addition. 
 
THEOREM 3.2:  VR and Vn×n are semigroups (monoid) under 
multiplication. 
 
THEOREM 3.3: VR and Vn×n are rings 
 
 
(i) VR is a commutative ring. 
 
(ii) Vn×n is a non commutative ring.  
 
 
The proof of all these theorems are simple and hence left as 
an exercise to the reader. 
 
THEOREM 3.4:  Both VR and Vn×n have zero divisors. 
 
THEOREM 3.5:  Both VR and Vn×n have no idempotents which 
are not constant matrix coefficient polynomials.


## Page 41


41
 
We give examples of zero divisors. 
 
Example 3.1:  Let VR[x] =
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, x3, x4, x5); xj ∈ 
Q or R or Z, 1 ≤ j ≤ 5} be a matrix coefficient polynomial ring. 
 
 
Take p(x) =  (3,2,0,0,0) + (6,3,0,0,0)x  
 + (7,0,0,0,0)x2 + (8,1,0,0,0)x4   and  
 
   q(x) = (0,0,1,2,3) + (0,0,0,4,2)x2 + (0,0,0,1,4)x3  
       + (0,0,0,3,4)x4 + (0,0,0,5,2)x7  
be elements in VR.   
 
p(x) q(x) = (0,0,0,0,0). 
 
 
Thus VR has zero divisors. 
 
 
Consider  
a(x)   = (5,0,0,0,2) + (3,0,0,0,0)x + (0,0,0,0,7)x2  
      + (2,0,0,0,-1)x3 + (6,0,0,0,0)x5 and  
 
b(x)   = (0,1,2,3,0) + (0,0,1,2,0)x + (0,1,0,0,0)x4  
      + (0,1,0,7,0)x3 + (0,2,0,4,0)x8 in VR.   
 
We see (a(x)) × (b(x)) = (0,0,0,0,0).  We see if q(x) is not a 
constant polynomial certainly (q(x))2  ≠ q(x) for if deg q(x) = n 
then deg ((q(x). q(x)) = n2. 
 
 
We show that VR and Vn×n have several non trivial ideals. 
 
Example 3.2:  Let VR be a ring.  Consider the ideal generated 
by p(x) = (2,3,1,5,7,8)x3 + (4,2,0,1,5,7) in VR.  Clearly I = 〈p(x)〉 
is a two sided ideal.  Since VR is commutative every ideal is two 
sided.  Infact VR has infinite number of ideals.


## Page 42


42
Example 3.3:  Let Vn×n be a ring.   
 
Take p(x) = 3
1
6
2






x3 + 2
1
5
7






x2 + 1 be in Vn×n.   
 
Clearly 〈p(x)〉 generates a two sided ideal. 
 
 
But p(x)Vn×n generates only one sided ideal.  Similarly 
(Vn×n) (p(x)) is not a two sided ideal.  Thus Vn×n has infinite 
number of right ideals which are not left ideal and two sided 
ideals.  Further Vn×n has left ideals which are not right ideals. 
 
Example 3.4:  Let  
 
V4×4[x] = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
x
x
x
x






 where xj ∈ Q; 1 ≤ j ≤ 4} 
be the matrix coefficient polynomial ring.  Let 
 
P = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
x
x
x
x






 where xj ∈ Z; 1 ≤ j ≤ 4} ⊆ V4×4; 
P is only a subring of V4×4 and is not an ideal of V4×4. 
 
THEOREM 3.6:  Let VR and Vn×n be matrix coefficient 
polynomial rings.  Both VR and Vn×n have subrings which are 
not ideals.  We see if p(x) ∈ VR or Vn×n; degree of p(x) as in case 
of usual polynomials is the highest power of x which has non 
zero coefficient. 
 
 
Consider  
p(x) = (2,3,4) + (0, –1,2)x + (7,2,5)x3 + (0,1,0)x7 ∈ VR. 
 
 
The degree of p(x) is even.


## Page 43


43
p(x) = 
3
1
2
0
1
5
0
0
1










 + 
7
2
1
0
5
7
6
1
2










x2 + 
2
0
1
0
7
4
0
1
0










x4 
 
+ 
2
1
5
6
7
8
0
1
2










x8. 
The degree of p(x) is 8. 
 
 
Now in case of usual polynomials if their coefficients are 
from a field then every polynomial p(x) can be made monic. 
 
 
However the same does not hold good in case of both VR 
and Vn×n. 
 
 
Consider  
p(x) = (0,3,0,0)x4 + (1,2,3,4)x3 + (2,0,0,1)x + (1,2,0,5) in 
VR.  Clearly p(x) cannot be made into a monic matrix 
coefficient polynomial for (0,3,0,0) has no inverse with respect 
to multiplication.  
 
 
Let q(x) = (5,7,8, –4)x5 + (1,2,3,0)x3 + (7,0,1,5)x + (8,9,0,2) 
be in VR.  Now q(x) can be made as a monic matrix coefficient 
polynomial.  For multiply q(x) by  
 
 
t = (1/5, 1/7, 1/8, –1/4).  Now tq(x) = (1,1,1,1)x5 + (1/5, 2/7, 
3/8, 0)x3 + (7/5,0,1/8, – 5/4)x + (8/5, 9/7, 0, –2/4) is a monic 
matrix coefficient polynomial of degree five. 
 
 
Let p(x) = 3
0
1
0






x7 + 2
1
5
7






x3 + 8
1
0
5






x2 + 18
7
0
2






x 
+ 1
2
3
4






 be a matrix coefficient polynomial in V2×2.  We see 
the coefficient of the highest power of p(x) is 3
0
1
0






.


## Page 44


44
 
 
Clearly 3
0
1
0






 has no inverse or the matrix 3
0
1
0






 is non 
invertible. 
 
 
Hence p(x) cannot be made into a monic matrix coefficient 
polynomial in V2×2.  Consider  
 
p(x) = 7
0
0
8






x5 + 1
8
7
5






x4 
 
+ 0
1
2
0






x3 + 0
1
1
0






x2 + 1
0
2
5






 in V2×2. 
 
 
We see p(x) can be made into a monic polynomial. 
 
 
A = 1/7
0
0
1/8






 is such that  
 
1/7
0
0
1/8






7
0
0
8






 = 1
0
0
1






. 
Thus  
 
1/7
0
0
1/8






 p(x) = 1
0
0
1






 x5 +  1/7
0
0
1/8






 1
8
7
5






x4  
 
+ 1/7
0
0
1/8






0
1
2
0






x3 + 1/7
0
0
1/8






0
1
1
0






x2 
 
+ 1/7
0
0
1/8






1
0
2
5








## Page 45


45
= 0
1
1
0






 x5 + 1/7
8/7
7 /8
5/8






x4 + 
0
1/7
1/ 4
0






x3 
 
+ 
0
1/7
1/8
0






x2 + 1/7
0
1/ 4
5/8






 
has been made into a monic polynomial. 
 
 
We have shown only some of the matrix coefficient 
polynomials can be made and not all matrix coefficient 
polynomials as the collection of row matrices or collection of 
n×n matrices are not field just a ring with zero divisors. 
 
 
Thus we have seen some of the properties of matrix 
coefficient polynomials.  Unlike the number system which are 
not zero divisors, we cannot extend, all the results as these 
matrix coefficients can also be zero divisors. 
 
 
Thus we can say a matrix coefficient polynomial p(x) ∈ VR 
(or Vn×n) divides another matrix coefficient polynomial q(x) ∈ 
VR (or Vn×n) if q(x) = p(x) b(x) where deg (b(x)) < deg q(x) and 
deg p(x) < deg q(x). 
 
 
We illustrate this by some examples. Suppose  
 
p(x) = ((3,2,1) + (7,–1,9)x) ((1,1,2) + (1,1,1)x) ((9,2,1)  
      – (2,5,1)x)   and  
 
q(x) =  ((7,–1,9)x + (3,2,1)) ((1,1,1)x + (1,1,2)) ((9,2,1)  
  – (2,5,1)x)) ((2,4,6)x2 + (3,1,2)x + (1,3,6)) are in VR.   
 
It is easily verified p(x)/q(x) and deg (p(x)) = 3 and  
deg q(x) = 5.   
 
However it is very difficult to derive all results in case of 
matrix coefficient polynomials; we have to define the concept of 
prime row matrix.


## Page 46


46
 
Suppose X = (a1, a2, …, an) is a row matrix with ai ∈ Z, 1 ≤ i 
≤ n; we say X is a prime row vector or row matrix if each ai is a 
prime and none of the ai is zero.  Thus (3,5,11,13), (7,5,2,19, 
23,31) and (11,23,29,43,41,53,59,47,7,11) are prime row 
matrices. 
 
 
We say or define the row matrix (a1, …, an) divides the row 
matrix (b1, b2, …, bn) if none of the ai’s are zero for i=1,2,…,n 
and ai/bi for every i, 1 ≤ i ≤ n. That is we say (a1, …, an) / (b1, b2, 
…, bn) if (b1/a1, …, bn/an) = (c1, …, cn) and ci ∈Z; 1 ≤ i ≤ n  
(ai ≠ 0; i = 1, 2, …, n). 
 
 
We will illustrate this situation by some examples. 
 
 
Let (5,7,2,8) = x and y = (10,14,8,8) we say x/y and y/x = 
(10/5, 14/7, 8/2, 8/8) = (2,2,4,1). 
 
 
Now if x = (0,2,3,5,7,8) and y = (5,4,6,10,21,24) then x \ y 
or y/x is not defined. 
 
 
So when matrix coefficient polynomials are dealt with it is 
very very difficult to define division in VR. 
 
 
Clearly if x = (a1, …, an) with ai ≠ 0 and ai primes for all i, 
then we see there does not exist any y = (b1, …, bn) with bi ≠ 0 
and bi ≠ 1 dividing x, (1 ≤ i ≤ n).  Thus the only divisors of x = 
(a1, …, an) are y = (1,1,…, 1) and y = (a1, a2, …, an) only.  Since 
we face a lot of problems in dealing with matrix multiplication 
and however we only multiply the two row matrices of same 
order x = (a1, a2, …, an) with y = (b1, b2, …, bn) as x.y = (a1, a2, 
…, an) (b1, b2, …, bn) as x.y = (a1b1, a2b2, …, anbn) we wish to 
extend this sort of multiplication for all matrices only criteria 
being that they should be of same order.  
 
 
We call such multiplication or product of matrices of same 
order as natural multiplication of matrices.  Thus we define 
natural multiplication or product of two n × 1 column matrices


## Page 47


47
as follows; if x = 
1
2
n
a
a
a













 and y = 
1
2
n
b
b
b













 then the natural product of 
x with y denoted by x ×n y = 
1
2
n
a
a
a













×n 
1
2
n
b
b
b













 = 
1
1
2
2
n
n
a b
a b
a b













.   
 
This product is defined as natural product of two n×1 
column matrices and the natural product operation is denoted by 
×n. 
 
Example 3.5: Let x = 
7
2
0
1
5








 and y = 
1
3
5
2
7








.  
Now the natural product of x with y is x ×n y = 
7
2
0
1
5








×n 
1
3
5
2
7








 
= 
7.1
2.3
0.5
1.2
5.7
















 = 
7
6
0
2
35
















. 
 
We see the natural product is both associative and 
commutative.


## Page 48


48
Now if x = 
1
1
1






  and y =
1
2
n
a
a
a













 be any two n × 1 column 
matrices when x ×n y = y ×n x = y. 
Thus x = 
1
1
1






  acts as the natural product identity.  We see 
infact any n × 1 collection of column vectors is a semigroup 
under natural multiplication or natural product and is a monoid 
and is a commutative monoid. 
 
THEOREM 3.7:  Let  
 
V = 














1
2
n
a
a
a
 ai ∈ Q (or Z or R); 1 ≤ i ≤ n} 
be the collection of all n × 1 column matrices.  V is a 
commutative 
semigroup 
under 
natural 
product 
(or 
multiplication) of column matrices. 
 
 
Proof is direct and hence is left as an exercise to the reader. 
 
Example 3.6:  Let  
x = 
1
2
3
0
0
0










 and y = 
0
0
0
0
1
2










 
be 6 × 1 column matrices.


## Page 49


49
We see x ×n y = 
1
2
3
0
0
0










 ×n 
0
0
0
0
1
2










 = 
0
0
0
0
0
0










. 
 
Thus x is a zero divisor. Inview of this we have the 
following result. 
 
THEOREM 3.8:  Let  
 
V = 














1
2
n
a
a
a
 ai ∈ Z (or Q or R); 1 ≤ i ≤ n} 
be the semigroup under natural multiplication ×n.  V has zero 
divisors. 
 
 
This proof is also very simple. 
 
 
Example 3.7:  Let  
V = 
1
2
n
a
a
a














 ai ∈ Z; 1 ≤ i ≤ 6} 
be a semigroup under natural product.


## Page 50


50
Take  
W =
1
2
6
a
a
a














 ai ∈ 3Z; 1 ≤ i ≤ 6} ⊆ V; 
W is a subsemigroup of V. Infact W is an ideal of the semigroup 
V. Thus we have several ideals for V. 
 
Example 3.8:  Let  
V = 
1
2
10
a
a
a














 ai ∈ Q; 1 ≤ i ≤ 10} 
be the semigroup under natural product.   
 
Consider  
W = 
1
2
10
a
a
a














 ai ∈ Z; 1 ≤ i ≤ 10} ⊆ V; 
 
W is only a subsemigroup of V and is not an ideal of V. 
 
 
Take  
S = 
1
2
a
a
0
0


















 ai ∈ Q; 1 ≤ i ≤ 10} ⊆ V; 
S is a subsemigroup of V under usual product.  Also S is an 
ideal of V.


## Page 51


51
 
From this example we see a subsemigroup in general is not 
an ideal. 
 
 
Inview of this we give the following result the proof of 
which is simple. 
 
THEOREM 3.9:  Let  
 
V = 














1
2
n
a
a
a
 ai ∈ Q (or R); 1 ≤ i ≤ n} 
 
be a semigroup under natural product.  V has subsemigroups 
which are not ideals.  However every ideal is a subsemigroup.   
 
Proof is left as an exercise for the reader.  
 
 
Now we have the concept of Smarandache semigroups.  We 
will illustrate this situation by an example. 
 
Example 3.9: Let  
 
V = 
1
2
8
a
a
a














 ai ∈ Q; 1 ≤ i ≤ 8} 
be the semigroup under natural multiplication.   
 
 
Consider  
M = 
1
2
8
a
a
a














 ai ∈ Q \ {0}; 1 ≤ i ≤ 8} ⊆ V;


## Page 52


52
M is a subring as well as a group under natural product.  Further 
we see M is not an ideal of V.  Thus V is a Smarandache 
semigroup.   
 
Inview of this we can easily prove the following theorem. 
 
THEOREM 3.10:  Let  
 
V = 














1
2
n
m
m
m
 mi ∈ Q (or R); 1 ≤ i ≤ n} 
be a semigroup under natural product.  V is a Smarandache 
semigroup.  
 
Proof:  For take  
 
M = 
1
2
m
a
a
a














 ai ∈ Q \ {0} or (ai ∈ R \ {0}); 1 ≤ i ≤ m} ⊆ V, 
M is a group under natural product as every element in M is 
invertible, hence the theorem.  
 
 
Now we proceed onto give an example or two. 
 
Example 3.10:  Let  
M = 
1
2
3
a
a
a











 ai ∈ Z; 1 ≤ i ≤ 3} 
be a semigroup under natural product.


## Page 53


53
Consider the set  
 
P = 
1
1
1
1
1 ,
1 ,
1 , 1 ,
1
1
1
1

−
−








−
−








−
−





1
1
1
1
1 , 1 , 1 ,
1
1
1
1
1

−
−











−
−











−
−





 ⊆ M 
 
is a group under product.  Thus Z is a Smarandache semigroup.   
 
Infact B = 
1
1
1 ,
1
1
1


−






−








−




 ⊆ M is also a group.  Thus P is a 
Smarandache semigroup as B ⊆ P. 
 
 
Now we wish to prove the following theorem. 
 
THEOREM 3.11:   Let  
 
M = 














1
2
n
a
a
a
 ai ∈ Z (or Q or R); 1 ≤ i ≤ n} 
 
be a semigroup under natural product.  If M has a 
Smarandache subsemigroup then M is a Smarandache 
semigroup.  However even if M is a Smarandache semigroup, 
every subsemigroup of M need not be a Smarandache 
subsemigroup.   
 
Proof:  Suppose we have a proper subsemigroup under natural 
product for M say W.  W is a Smarandache subsemigroup of M; 
then W has a proper subset X such that X is a group under 
natural product; X ⊆ W. 
 
 
Now X ⊆ W ⊆ M; that is X ⊆ M so M is a Smarandache 
semigroup.  Hence the claim.


## Page 54


54
 
We prove the other part of the theorem by an example. 
 
 
Consider  
Y = 
1
2
n
x
x
x














xi ∈ Z; 1 ≤ i ≤ n} 
 
be a semigroup under natural product.


## Page 55


55
Y is a Smarandache semigroup as  
 
P = 
1
1
1
1
1
1
1
1
,
1
1
1
1
1
1
1
1


−






−








−




−








−






−






−






−






 ⊆ Y 
 
is a group under natural multiplication.  Hence Y is a S-
semigroup.   
 
 
Take  
W = 
1
2
7
a
a
a














ai ∈ 3Z; 1 ≤ i ≤ 7} ⊆ Y; 
W is only a subsemigroup of Y and is not a Smarandache 
subsemigroup of Y.  Hence even if Y is a S-semigroup.  Y has 
subsemigroups whch are not Smarandache subsemigroup.  
Hence the theorem. 
 
 
Now we have seen ideals and subsemigroups and S-
subsemigroups about column matrix semigroups under natural 
product. 
 
 
Now we define natural product on m × n matrix semigroups 
(m ≠ n).


## Page 56


56
DEFINITION 3.1:  Let  
 
M = 
















11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a
aij ∈ Z (or Q or R);  
1 ≤ i ≤ m  and  1 ≤ j ≤ n}  
 
be the collection of all m × n (m ≠ n) matrices.  M under natural 
multiplication / product ×n is a semigroup. 
 
If X = 















11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a
 and Y = 















11
12
1n
21
22
2n
m1
m2
mn
b
b
...
b
b
b
...
b
b
b
...
b
 
 
be any two m × n matrices in M. 
 
We define X ×m Y = 















11 11
12
12
1n 1n
21 21
22
22
2n
2n
m1 m1
m2
m2
mn
mn
a b
a b
...
a b
a b
a b
...
a b
a b
a b
...
a b
. 
 
 
Clearly X ×m Y is in M.  (M, ×n) is defined as the semigroup 
under natural product. 
 
 
We give examples of them. 
 
Example 3.11:  Let  
 
X = 
2
1
0
5
1
0
3
1
2
5
1
4
3
0
1








−


 and Y = 
3
2
0
1
3
4
0
1
5
7
0
1
2
0
5












## Page 57


57
be any two 3 × 5 matrices.  We find the natural product of X 
with Y. 
 
X ×n Y = 
2
1
0
5
1
0
3
1
2
5
1
4
3
0
1








−


 ×n 
3
2
0
1
3
4
0
1
5
7
0
1
2
0
5










 
 
= 
6
2
0
5
3
0
0
1
10
35
0
4
6
0
5










. 
 
Example 3.12:  Let  
 
S = 
1
2
3
4
5
6
28
29
30
a
a
a
a
a
a
a
a
a
















ai ∈ Z; 1 ≤ i ≤ 30} 
 
be the semigroup under natural product.  S is a commutative 
semigroup with identity.  S has infinite number of ideals and 
subsemigroups which are not ideals.  
 
Example 3.13:  Let  
 
S = 
1
2
3
4
11
12
a
a
a
a
a
a















ai ∈ Q; 1 ≤ i ≤ 12} 
be the semigroup under natural product.


## Page 58


58
Take  
I = 
1
2
3
4
a
a
0
0
0
0
0
0
a
a



























ai ∈ Q; 1 ≤ i ≤ 4}. 
 
It is easily verified I is an ideal of P under natural product 
×n.   
 
Consider the subsemigroup  
 
S =
1
2
3
4
5
6
a
a
a
a
0
0
0
0
a
a



























ai ∈ Q; 1 ≤ i ≤ 6} ⊆ P 
under natural product.  Clearly S is an ideal of P. 
 
 
Suppose  
T =   
1
2
3
4
11
12
a
a
a
a
a
a















ai ∈ Z; 1 ≤ i ≤ 12} ⊆ P, 
 
T is only a subsemigroup of P under natural product and is not 
an ideal of P. 
 
 
We can as in case of usual semigroups define in case of 
these semigroups under natural product the concept of 
Smarandache-ideals, Smarandache zero divisors and so on.  By


## Page 59


59
our natural product we are able to define some form of product 
on column matrices and rectangular matrices.  Now we proceed 
onto define natural product on usual square matrices. 
 
 
Let A = (aij)n×n and B = (bij)n×n be square matrices; aij, bij ∈ Z 
(or Q or R); 1 ≤ i, j ≤ n.  We define the natural product  
 
A ×n B as A ×n B  =  (aij)n×n  (bij)n×n 
 
 
 
 
 
= (aij bij)n×n 
 
 
 
 
 
= (cij)n×n. 
 
We will illustrate this by few examples.  
 
Example 3.14:  Let  
 
A = 
6
1
2
0
3
4
2
1
0










 and B = 
3
0
1
2
1
0
0
1
2










 
be two 3 × 3 matrices.  To find the natural product of A with B.   
 
A ×n B = 
6
1
2
0
3
4
2
1
0










 
3
0
1
2
1
0
0
1
2










 = 
18
0
2
0
3
0
0
1
0










. 
 
 
Now the usual matrix product of A with B is  
 
A.B = 
6
1
2
0
3
4
2
1
0










3
0
1
2
1
0
0
1
2










 
 
= 
20
3
10
6
7
8
8
1
2










.


## Page 60


60
 
We see A.B ≠ A ×n B in general.  Further we see the 
operation ‘.’ the usual matrix multiplication is non commutative 
where as the natural product ×n is commutative. 
 
 
We just consider the following examples. 
 
Example 3.15:  Let  
 
M = 3
4
2
0






 and N = 1
2
0
1






 
 
be any two 2 × 2 matrices.  
 
M.N  = 3
4
2
0






1
2
0
1






 = 3
10
2
4






 
 
and N.M = 1
2
0
1






3
4
2
0






 = 7
4
2
0






. 
 
 
We see M.N ≠ N.M.   
 
However M ×n N = 3
4
2
0






×n 1
2
0
1






 
 
= 3
8
0
0






 and 
 
N ×n M = 1
2
0
1






× 3
4
2
0






 = 3
8
0
0






. 
 
Thus N ×n M = M ×n N.


## Page 61


61
Example 3.16:  Let  
 
M = 
7
0
0
0
0
8
0
0
0
0
2
0
0
0
0
4












 and N = 
1
0
0
0
0
2
0
0
0
0
3
0
0
0
0
4












. 
 
We find M.N = 
7
0
0
0
0
8
0
0
0
0
2
0
0
0
0
4












1
0
0
0
0
2
0
0
0
0
3
0
0
0
0
4












 
 
= 
7
0
0
0
0
16
0
0
0
0
6
0
0
0
0
16












. 
 
 
Also  
N.M = 
1
0
0
0
0
2
0
0
0
0
3
0
0
0
0
4












7
0
0
0
0
8
0
0
0
0
2
0
0
0
0
4












 = 
7
0
0
0
0
16
0
0
0
0
6
0
0
0
0
16












. 
 
 
Now consider M ×n N = 
7
0
0
0
0
8
0
0
0
0
2
0
0
0
0
4












 ×n 
1
0
0
0
0
2
0
0
0
0
3
0
0
0
0
4














## Page 62


62
= 
7
0
0
0
0
16
0
0
0
0
6
0
0
0
0
16












.  We see M.N = M ×n N. 
 
 
In view of this we have the following theorem. 
 
THEOREM 3.12:  Let  
 
M = 






















1
2
3
n
a
0
0
0
...
0
0
a
0
0
...
0
0
0
a
0
...
0
0
0
0
0
...
a
ai ∈ Q (or Z or R or C);   
 
1 ≤ i ≤ n} 
 
be the collection of all n × n diagonal matrices.  M is a 
semigroup under natural product and M is also a semigroup 
under usual product of matrices and both the operations are 
identical on M. 
 
Proof:  Let  
 
A = 
1
2
3
4
n
a
0
0
0
...
0
0
a
0
0
...
0
0
0
a
0
...
0
0
0
0
a
0
...
0
0
0
0
...
a



























## Page 63


63
and 
1
2
3
4
n
b
0
0
0
...
0
0
b
0
0
...
0
0
0
b
0
...
0
0
0
0
b
0
...
0
0
0
0
...
b

























 be two matrices from M. 
 
 
Now let us consider the natural product of  
 
A ×n B = 
1
1
2
2
3
3
4
4
n
n
a b
0
0
0
...
0
0
a b
0
0
...
0
0
0
a b
0
...
0
0
0
0
a b
0
...
0
0
0
0
...
a b

























. 
 
 
Consider the matrix product;  
 
A.B = 
1
1
2
2
3
3
4
4
n
n
a b
0
0
0
...
0
0
a b
0
0
...
0
0
0
a b
0
...
0
0
0
0
a b
0
...
0
0
0
0
...
a b

























. 
 
It is easily verified A.B = A ×n B.  Thus both the operations are 
identical as diagonal matrices. 
 
THEOREM 3.13: Let  
M = {(aij)n×n | aij ∈ R (or Q or Z or C); 1 ≤ i, j ≤ n} 
be the collection of all n × n matrices, M is a semigroup under 
natural product and M is a semigroup under matrix


## Page 64


64
multiplication.  Both the operations on M are distinct in 
general.  
 
 
The proof is direct and hence left as an exercise to the 
reader. 
 
THEOREM 3.14:  Let  
M = {(aij) | aij ∈ Z (or Q or R or C); 1 ≤ i, j ≤ n} 
be a semigroup under natural product.  M is a Smarandache 
semigroup. 
 
Proof:  Let P = {(aij) | aij ∈ Z \ {0}, (R] {0} or Q] {0} or C \ 
{0})  1 ≤ i ≤ n} ⊆ M be a group under natural multiplication.  
So M is a S-semigroup. 
 
 
It is pertinent to mention here that these semigroups have 
ideals subsemigroups, zero divisors and idempotents and their 
Smarandache analogue. 
 
 
Now we proceed onto give more structures using this 
product. 
 
DEFINITION 3.2:  Let  
 
M = 














1
2
m
a
a
a
ai ∈ Q (or Z or R or C);  1 ≤ i ≤ m} 
 
be the collection of all m × 1 column matrices.  M is a ring 
under usual matrix addition and natural product ×n.


## Page 65


65
Example 3.17: Let  
 
M = 
1
2
3
4
a
a
a
a













ai ∈ R (or Q or Z);  1 ≤ i ≤ 4} 
be a ring under + and ×n.  The reader can easily verify that  
A ×n (B+C) = A ×n B + A ×n C where A, B and C are n × 1 
column matrices.  
 
Consider A = 
1
2
n
a
a
a













 , B = 
1
2
n
b
b
b













 and C = 
1
2
n
c
c
c













; 
 
A ×n (B+C) = 
1
2
n
a
a
a













 ×n 
1
1
2
2
n
n
b
c
b
c
b
c


















+






















 
 
= 
1
2
n
a
a
a













 ×n 
1
1
2
2
n
n
b
c
b
c
b
c
+




+






+



 = 
1
1
1
2
2
2
n
n
n
a (b
c )
a (b
c )
a (b
c )
+




+






+



 
 
= 
1
1
1 1
2
2
2
2
n
n
n
n
a b
a c
a b
a c
a b
a c
+




+






+



 =
1
1
1 1
2
2
2
2
n
n
n
n
a b
a c
a b
a c
a b
a c












+














.


## Page 66


66
Now consider A ×n B + A ×n C 
 
= 
1
2
n
a
a
a













 ×n 
1
2
n
b
b
b













 + 
1
2
n
a
a
a













 ×n 
1
2
n
c
c
c













 
 
= 
1
1
1 1
2
2
2
2
n
n
n
n
a b
a c
a b
a c
a b
a c












+














 = 
1
1
1 1
2
2
2
2
n
n
n
n
a b
a c
a b
a c
a b
a c
+




+






+



. 
 
 
Thus we see ×n distributes over addition.  Now consider the 
collection of all m × n matrices (m ≠ n) with entries taken from 
Z or Q or C or R.  We see this collection also under matrix 
addition and natural product is a ring.  Let  
 
M = {(aij)m×n | m ≠ n; aij ∈ R (or Z or Q or C); 
1 ≤ i ≤ m and 1 ≤ j ≤ n}; 
 
M is a ring infact a commutative ring. 
 
 
However M is not a ring under matrix addition and matrix 
product.  
 
Example 3.18:  Let  
 
M = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













ai ∈ Q (or Z or R or C);  1 ≤ i ≤ 8} 
 
be a ring under matrix addition and natural product.


## Page 67


67
M is a commutative ring with unit 
1 1
1 1
1 1
1 1












. 
 
 
M has units, zero divisors, subrings and ideals. 
 
Take a = 
3
4
5
8
1
9
4
7












 and b = 
1/3
1/ 4
1/5
1/8
1
1/9
1/ 4
1/7












; 
 
clearly ab  = ba = 
1 1
1 1
1 1
1 1












. 
 
Consider a = 
1
2
3
4
0
0
a
a
a
a
0
0












 and b = 
1
2
3
4
a
a
0
0
0
0
a
a












 ∈ M. 
 
 
Clearly ab = 
0
0
0
0
0
0
0
0












 is a zero divisor in M.


## Page 68


68
 
Take  
P = 
1
2
3
4
a
0
a
0
a
0
a
0













ai ∈ Q;  1 ≤ i ≤ 4} ⊆ M; 
P is an ideal of M.   
 
Consider  
 
T = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













ai ∈ Z; 1 ≤ i ≤ 8} ⊆ M; 
 
clearly T is only a subring of M and is not an ideal of M.  Thus 
M has subrings which are not ideals.  We can find several 
subrings which are not ideals.  
 
Example 3.19:  Let  
 
N = 
1
2
3
4
5
6
a
a
a
a
a
a







ai ∈ Z;  1 ≤ i ≤ 6} 
 
be the ring under matrix addition and natural product.  We see 
M has no units.   
 
1 1 1
1 1 1






 is the identity with the natural product ×n in N.   
 
Consider  
P = 
1
2
3
4
5
6
b
b
b
b
b
b







bi ∈ 3Z;  1 ≤ i ≤ 6} ⊆ N 
is an ideal of N.


## Page 69


69
 
Example 3.20:  Let  
 
M = 
1
2
3
4
5
6
31
32
33
a
a
a
a
a
a
a
a
a
















ai ∈ Q;  1 ≤ i ≤ 33} 
be a ring under matrix addition and natural product.  M is a S-
ring.   
 
For consider  
P = 
1
2
3
4
5
6
31
32
33
b
b
b
b
b
b
b
b
b
















bi ∈ 3Z; 1 ≤ i ≤ 33} ⊆ M; 
 
P is not an ideal of M.  M has units, zero divisors, subrings and 
ideals.   
 
 
Take  
W =  
1
2
3
4
5
6
a
a
a
0
0
0
0
0
0
a
a
a




















ai ∈ Q;  1 ≤ i ≤ 6} ⊆ M, 
W is an ideal of M.


## Page 70


70
Consider  
 
S = 
1
2
3
a
a
a
0
0
0
0
0
0
















ai ∈ Z;  1 ≤ i ≤ 3} ⊆ M 
is only a subring and not an ideal.  
 
Example 3.21:  Let  
 
M = 
1
2
3
4
21
22
a
a
a
a
a
a















ai ∈ Q;  1 ≤ i ≤ 22} 
be a ring M is commutative ring with 
1 1
1 1
1 1













  as unit with 
respect to natural multiplication.  M is not an integral domain.  
M has zero divisors and every element M is torsion free. 
 
For consider x = 
1
2
3
4
21
22
a
a
a
a
a
a














 ∈ M. 
 
x2 = 
2
2
1
2
2
2
3
4
2
2
21
22
a
a
a
a
a
a
















 and so on.  xn = 
n
n
1
2
n
n
3
4
n
n
21
22
a
a
a
a
a
a
















. 
Thus every x ∈ M is such that xn ≠ [1] for any positive n.


## Page 71


71
 
Example 3.22:  Let  
 
P =  
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q (or Z or R or C);  1 ≤ i ≤ 9} 
 
be a commutative ring with unit under natural product. 
 
M =  
1
2
3
4
5
6
a
a
a
0
a
a
0
0
a











ai ∈ Z;  1 ≤ i ≤ 6} ⊆ P; 
M is a subring but M has no unit.  M is not an ideal.  M is of 
infinite order. 
 
Example 3.23:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
a
a
a
a
0
a
a
a
0
0
a
a
0
0
0
a













ai ∈ Z;  1 ≤ i ≤ 10} 
 
be a ring M is a commutative ring with no identity. 
 
P = 
1
2
3
4
a
0
0
0
0
a
a
0
0
0
0
a
0
0
0
0













ai ∈ Z;  1 ≤ i ≤ 4} ⊆ M; 
 
P is a subring and an ideal of M.


## Page 72


72
Example 3.24:  Let  
 
P = 
1
2
3
4
5
6
31
32
33
a
a
a
a
a
a
a
a
a
















ai ∈ Z;  1 ≤ i ≤ 33} 
be a ring P has no units.  P has ideals.  P has subrings which are 
not ideals.  P has no idempotents or nilpotents.   
 
Every element x in P is such that for no n ∈ Z+,  
 
xn = 
1 1 1
1 1 1
1 1 1














 . 
 
 
THEOREM 3.15:  Let  
 
M = 
















11
1n
21
2n
m1
mn
a
...
a
a
...
a
a
...
a
aij ∈ Q;  1 ≤ i ≤ m; 1 ≤ j ≤ n} 
 
be a ring M is a S-ring. 
 
Proof:  Consider  
 
P = 
b
0
...
0
0
0
...
0
0
0
...
0

















b ∈ Q} ∈ M; 
P is a field.  So M is a S-ring.


## Page 73


73
 
COROLLARY 2:  Every matrix ring under natural product is a 
S-ring. 
 
 
If Q is replaced by Z in the theorem and corollary then the 
matrix ring is not a S-ring. 
 
Example 3.25:  Let  
 
S = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a













ai ∈ Z;  1 ≤ i ≤ 12} 
be a ring, S is a S-ring. 
 
Example 3.26:  Let  
 
M = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













ai ∈ Q; 1 ≤ i ≤ 8} 
be a ring.  M is a S-ring.  For M has 8 subfields given by  
 
F1 = 
1a
0
0
0
0
0
0
0













a1 ∈ Q} ⊆ M is a field. 
 
F2 = 
1
0
a
0
0
0
0
0
0













a1 ∈ Q} ⊆ M is a field.


## Page 74


74
F3 = 
1
0
0
a
0
0
0
0
0













a1 ∈ Q} ⊆ M is a field. 
 
F4 = 
1
0
0
0
a
0
0
0
0













a1 ∈ Q} ⊆ M is a field. 
 
F5 = 
1
0
0
0
0
a
0
0
0













a1 ∈ Q} ⊆ M is a field. 
 
F6 = 
1
0
0
0
0
0
a
0
0













a1 ∈ Q} ⊆ M is a field. 
 
F7 = 
1
0
0
0
0
0
0
a
0













a1 ∈ Q} ⊆ M is a field and 
 
F8 = 
1
0
0
0
0
0
0
0
a













a1 ∈ Q} ⊆ M is a field.   
Thus M has only 8 fields.


## Page 75


75
 
N = 
1
2
a
0
0
a
0
0
0
0













a1, a2 ∈ Q} ⊆ M; 
N is a subring and an ideal and not a field.  Thus M has only 8 
fields.  M is a S-ring.  N also is a S-subring.  However all 
subrings of M are not S-subrings.   
 
For consider  
 
S = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













ai ∈ Z;  1 ≤ i ≤ 8} ⊆ M; 
 
S is only a subring and clearly S is not a S-subring.  Infact M 
has infinite number of subrings which are not S-subrings. 
 
 
Example 3.27:  Let  
 
W =  
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q;  1 ≤ i ≤ 9} 
be a ring under usual multiplication of matrices. W is a non 
commutative ring. However W is also a S-ring.  W is a 
commutative ring under natural matrix multiplication, (W, +, 
×n) is also a S-ring.  Both have zero divisors. 
 
 
It is interesting to recall that by the natural matrix 
multiplication we are in a position to extend all the properties of 
reals into these matrix rings, (R, +, ×n); the only difference 
being that these rings have zero divisors.  So as blocks they do 
not loose any of the properties over which they are defined.


## Page 76


76
Further we can get compatability of natural product for both 
column and rectangular matrices.  Hence we see these matrices 
under natural product can serve better purpose for they almost 
behave like the real numbers or complex number or rationals or 
integers on which they are built. Now we give more algebraic 
structure on them.  Consider the set of all row matrices M = 
{(x1, …, xn) | xi ∈ R+ ∪ {0} (or Q+ ∪ {0} or Z+ ∪ {0}); 1 ≤ i ≤ 
n},  M under + is a commutative semigroup with (0, 0, …, 0) as 
its additive identity. 
 
 
M under ×n is also semigroup.  Thus (M, +, ×n) is a 
semiring.  We see this semiring is a commutative semiring with 
zero divisors. 
 
 
Suppose  
 
S = {(x1, …, xn) | xi ∈ R+ ∪ {0} (or Z+ or Q+); 1 ≤ i ≤ n}.   
 
Now {S ∪ {(0, 0, …, 0)} = T, +, ×n} is a semifield. 
 
 
It is easily verified T has no zero divisors and that T is a 
strict semiring for a = (x1, x2, …, xn) and b = (y1, y2, …, yn) is 
such that x+y = 0 implies a = (0) = b = (0, 0, …, 0).  Now we 
will give examples of them before we proceed onto define and 
describe more properties.  
 
Example 3.28:  Let  
 
M = {(a1, a2, a3) where ai ∈ Z+ ∪ {0}; 1 ≤ i ≤ 3}; (M, +, ×n) 
 
is a semiring.  M is not a semifield as a = (3, 0, 4) and b = (0, 7, 
0) in M are such that a.b = (3, 0, 4) (0, 7, 0) = (0, 0, 0).  
However M is a strict commutative semiring which is not a 
semifield.


## Page 77


77
Example 3.29:  Let  
 
 
T = 
1
2
3
4
5
6
a
a
a
a
a
a

























ai ∈ Q+ ∪ {0};  1 ≤ i ≤ 6} 
 
be a semiring under + and ×n. 
 
We see if x = 
0
3
1
0
2
5










 and y = 
1
0
0
2
0
0










 are in T then 
 
 
x ×n y = 
0
3
1
0
2
5










 ×n 
1
0
0
2
0
0










 = 
0
0
0
0
0
0










. 
 
 
Thus T is only a commutative strict semiring and is not a 
semifield.


## Page 78


78
Example 3.30:  Let  
 
M = 
1
2
3
4
5
6
13
14
15
a
a
a
a
a
a
a
a
a
















ai ∈ R+ ∪ {0};  1 ≤ i ≤ 15} 
 
be a semiring under + and ×n.  Clearly M is commutative and is 
a strict semiring.  However M does contain zero divisor, for if T 
= 
1
2
3
4
5
6
a
a
a
0
0
0
0
0
0
0
0
0
a
a
a
















 and N = 
1
2
3
4
5
6
7
8
9
0
0
0
a
a
a
a
a
a
a
a
a
0
0
0
















 with ai ∈ R+ ∪ {0} are 
in M then  
 
T ×n N = 
1
2
3
4
5
6
a
a
a
0
0
0
0
0
0
0
0
0
a
a
a
















 ×n 
1
2
3
4
5
6
7
8
9
0
0
0
a
a
a
a
a
a
a
a
a
0
0
0
















 = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















. 
 
 
Thus M is not a semifield. 
 
Example 3.31:  Let  
 
J = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q+ ∪ {0};  1 ≤ i ≤ 9} 
be a semiring under + and ×n.  J is a commutative strict 
semiring.  However J is not a semifield.


## Page 79


79
For take a = 
1
2
3
4
5
6
0
0
a
0
a
a
a
a
a










 and b = 
1
2
3
b
b
0
b
0
0
0
0
0










 in J,  
 
 
we see a.b = 
1
2
3
4
5
6
0
0
a
0
a
a
a
a
a










1
2
3
b
b
0
b
0
0
0
0
0










 = 
0
0
0
0
0
0
0
0
0










. 
 
 
Thus J is only a strict commutative semiring and is not a 
semifield, we show how we can build semifields.   
 
First we will illustrate this situation by some examples. 
 
Example 3.32:  Let  
 
M = {(0,0,0,0), (x1, x2, x3, x4) | xi ∈ Q+; 1 ≤ i ≤ 4}; (M, +, ×n) 
 
be a semifield.  For we see (M, +) is a commutative semigroup 
with additive identity (0,0,0,0). 
 
 
Further (M, ×n) is a commutative semigroup with (1,1,1,1) 
as its multiplicative identity.  
 
 
Also M is a strict semiring for (a,b,c,d) + (x,y,z,t)  
 
 
= (a + x, b + y, c + z, t + d) 
 
 
= (0,0,0,0) if and only if each of a,b,c,d,x,y,z and t is zero. 
 
 
Also for any x = (a1, a2, a3, a4) and y = (b1, b2, b3, b4) in M.  
We see x.y = (a1, a2, a3, a4)  (b1, b2, b3, b4) = (a1b1, a2b2, a3b3, 
a4b4) where aibi are in Q+; 1 ≤ i ≤ 4 so x.y ≠ (0,0,0,0).  Thus (M, 
×n) is a semifield.  Thus we can get many semifields.


## Page 80


80
Example 3.33: Let  
 
M = 
1
2
9
10
a
a
a
a


















 where ai ∈ R+, 1 ≤ i ≤ 10} and 
 
P = M ∪ 
0
0
0
0



























; (P, +, ×n) is a semifield. 
 
 
Example 3.34:  Let  
 
S = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















 where ai ∈ R+, 1 ≤ i ≤ 20} 
 
and P = S ∪ 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0


































; (P, +, ×n) is a semifield.


## Page 81


81
Example 3.35:  Let  
 
T = 
1
2
3
4
a
a
a
a







ai ∈ Z+, 1 ≤ i ≤ 4} and 
 
P = T ∪ 
0
0
0
0
















; (P, +, ×n) is a semifield. 
 
 
We see by defining natural product on matrices we get 
infinite number of semifields apart from R+ ∪ {0}, Q+ ∪ {0} 
and Z+ ∪ {0}.  We proceed onto give examples of Smarandache 
semirings.  Recall a semiring S is a Smarandache semiring if S 
contains a proper subset T such that T under the operations of S 
is a semifield. 
 
Example 3.36:  Let  
M = {(a1, a2, …, a10) | ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 10} 
be a semiring under + and ×n.  Take  
 
T = {(0,a,0,…,0) | a ∈ Q+ ∪ {0}} ⊆ M; 
T is a subsemiring of M.  T is strict and T has no zero divisors, 
so T is a semifield under + and ×n.  Hence M is a Smarandache 
semiring. 
 
Example 3.37:  Let  
T = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a



























 where ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 8} 
be a semiring under + and ×n.


## Page 82


82
 
 
 
 
Consider  
 
P = 
0
0
0
a










a ∈ Z+ ∪ {0}} ⊆ T. 
 
P is a subsemiring of T which is strict and has no zero divisors.  
Thus T is a Smarandache semiring.  
 
Example 3.38:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a











 where ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 12} 
 
be a semiring under + and ×n. 
 
 
V is a Smarandache semiring as  
 
 
P = 
a
0
0
0
0
0
0
0
0
0
0
0











a ∈ Z+ ∪ {0}} ⊆ V; 
 
is a semifield.


## Page 83


83
Example 3.39:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















  
 
where ai ∈ R+ ∪ {0},  1 ≤ i ≤ 25} 
 
be a semiring under + and ×n. 
 
 
Consider  
 
S = 
1
0
0
0
0
0
0
0
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

















a ∈ Z+ ∪ {0}} ⊆ M 
 
is a semiring as well as a semifield under + and ×n.   Hence M is 
a Smarandache semiring.   
 
We can now define subsemirings and Smarandache 
subsemirings.  These definitions are a matter of routine and 
hence left as an exercise to the reader.  We however provide 
some examples of them. 
 
Example 3.40:  Let  
 
P = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a











 where ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 12} 
be a semiring under + and ×n.


## Page 84


84
 
 
 
 
Consider  
 
X = 
1
2
3
4
a
a
a
a
0
0
0
0
0
0
0
0











a ∈ 3Z+ ∪ {0}; 1 ≤ i ≤ 4} ⊆ P; 
 
x under + and ×n is a subsemiring of P.  However x is not a 
Smarandache subsemiring.   
 
But we see P is a Smarandache semiring for  
 
V =  
d
0
0
0
0
0
0
0
0
0
0
0











d ∈ Z+ ∪ {0}} ⊆ P 
 
is a semiring as well as a semifield under + and ×n. 
 
Example 3.41:  Let  
 
P = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 where ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 16} 
 
be a semiring under + and ×n.


## Page 85


85
 
P is a Smarandache semiring for take  
 
W = 
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0













a ∈ Z+ ∪ {0}} ⊆ P 
is a semifield under + and ×n.  Hence P is a Smarandache 
semiring. However P has infinitely many subsemirings which 
are not Smarandache subsemirings.  
 
 
Consider  
 
Pn = 
1
2
3
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0













a ∈ nZ; 1 ≤ i ≤ 3; n ≥ 2} ⊆ P; 
 
Pn is a subsemiring of P but is not a Smarandache subsemiring 
of P. Thus we see in general all subsemirings of a Smarandache 
semiring need not be a Smarandache subsemiring.  But if S be a 
semiring which has a Smarandache subsemiring then S is also a 
Smarandache semiring. 
 
 
Inview of this we have the following theorem. 
 
THEOREM 3.16:  Let S, be a semiring of n × m matrices with 
entries from R+ ∪ {0} (or Q+ ∪ {0} or Z+ ∪ {0}).  If S has a 
subsemiring which is a Smarandache subsemiring then S is a 
Smarandache semiring.  However if S is a Smarandache 
semiring then in general a subsemiring of S need not be a 
Smarandache subsemiring. 
 
Proof:  Let S be a semiring and P ⊆ S be a proper subsemiring 
of S, which is a Smarandache subsemiring of S.  Since P is a 
Smarandache subsemiring of S we have a proper subset X ⊆ P 
(X ≠ φ and X ≠ P) such that X is a semifield.  Now we see P ⊆ S


## Page 86


86
and X ⊆ P so X ⊆ P ⊆ S that is X is a proper subset of S and X 
is a semifield, so S is a Smarandache semiring. 
 
 
To show every subsemiring of a Smarandache semiring 
need not be a Smarandache subsemiring, we give an example. 
 
 
Consider  
 
P = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a







 where ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 8} 
 
be a semiring under + and ×n. 
 
 
If is easily verified P is a Smarandache semiring as  
 
X = 
a
0
0
0
0
0
0
0







a ∈ Z+ ∪ {0}} ⊆ P; 
 
is a semifield under + and ×n; so P is a Smarandache semiring. 
 
 
 
Consider a subsemiring  
 
T = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a







 where ai ∈ 5Z+ ∪ {0}, 1 ≤ i ≤ 8} ⊆ P; 
 
clearly T is a subsemiring of P; however T is not a Smarandache 
subsemiring of P, but we know P is a Smarandache semiring. 
Hence the result.  
 
 
We will show the existence of zero divisors in semirings.


## Page 87


87
Example 3.42: Let  
 
P = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















 where ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 15} 
 
be a semiring and + and ×n. 
 
 
To show M has zero divisors.  
 
Consider x = 
1
2
3
4
5
6
0
0
0
a
a
a
0
0
0
a
a
a
0
0
0
















 and y = 
1
2
3
4
5
6
7
8
9
a
a
a
0
0
0
a
a
a
0
0
0
a
a
a
















in M. 
 
We see x ×n y = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















. 
 
Thus M has zero divisors.  Infact M has infinitely many 
zero divisors. 
For take a = 
1
2
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
















 where a1, a2 ∈ 10Z+ and


## Page 88


88
b = 
1
2
0
0
0
b
b
0
0
0
0
0
0
0
0
0
0
















where b1, b2 ∈ 3Z+ in M, 
 
we see a.b = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















. 
 
Thus we can get any number of zero divisors in M.  
 
M has no idempotents other than elements of the form  
 
 x = 
1
1
1
0
0
0
1
1
1
0
0
0
0
0
0
















 ∈ M, we see x2 = x or 
 
y = 
0
0
0
1
0
0
0
1
0
0
0
1
0
1
1
















 ∈ M is such that y2 = y and so on. 
Inview of this we have the following nice theorem. 
 
THEOREM 3.17:  Let S = {(aij)m×n | aij ∈ Z+ ∪ {0} (or Q+ ∪ {0} 
or R+ ∪ {0}); 1 ≤ i ≤ m; 1 ≤ j ≤ n} be a semiring under + and 
×n.  All elements in S of the form T = {(aij)m×n | aij ∈ {0, 1}} ⊆ S 
are collection of idempotents.


## Page 89


89
The proof is direct hence left as an exercise to the reader. 
 
 
We call all these idempotents only as trivial or {1, 0} 
generated idempotents; apart from this these matrix semiring 
with natural product do not contain any other idempotents. 
 
Example 3.43:  Let M = {(a, b) | a, b ∈ Z+ ∪ {0}} be a semiring 
under + and ×n.  The only trivial idempotents of M are (0, 0), (0, 
1), (1, 0) and (1, 1). 
 
Example 3.44:  Let P = 
a
b
c
d







a, b, c, d ∈ Z+ ∪ {0}} be a 
semiring under + and ×n.   
 
The trivial idempotents of P are  
 
0
0
1
0
0
1
0
0
0
0
1
0
1
1
,
,
,
,
,
,
,
0
0
0
0
0
0
1
0
0
1
1
0
0
0

























 
 
0
0
0
1
1 1
1
0
,
,
,
,
1
1
0
1
1 1
1
1














 
 
0
1
1
1
1
1
1
0
0
1
,
,
,
,
1
1
1
0
0
1
0
1
1
0



















 = I ⊆ P  
 
we see I under natural product ×n is a semigroup.  However I is 
not closed under +. 
 
THEOREM 3.18:  Let  
 
M ={(aij) | aij ∈ Z+ ∪ {0}; 1 ≤ i ≤ m; 1 ≤ j ≤ n} 
 
be the collection of m × n matrices.  The collection of all trivial 
idempotents forms a semigroup under ×n and the number of 
such trivial idempotents is 2m×n.


## Page 90


90
 
The 
proof 
involves 
only 
simple 
number 
theoretic 
techniques, hence left as an exercise to the reader. 
 
Example 3.45:  Let  
 
M = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a







 where ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 8} 
 
be a semiring under + and ×n. 
 
 
I = 
0
0
0
0
1
0
0
0
0
1
0
0
,
,
,
0
0
0
0
0
0
0
0
0
0
0
0













  
 
0
0
1
0
0
0
0
1
,
0
0
0
0
0
0
0
0









,  
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
,
,
,
,
1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
1














 
 
1
1
0
0
0
1
1
0
0
0
1
1
1
0
0
0
,
,
,
,...,
0
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0















 
 
1 1 1
1
1 1 1 1
,
1 1 1
0
1 1 1 1










 ⊆ M;  
 
is the collection of all trivial idempotents.  Clearly they form a 
semigroup under product.  However I is not closed under 
addition.  Further the number of elements in I is 28. 
 
 
Further the semigroup I has zero divisors and 1 1 1 1
1 1 1 1






 
acts as the multiplicative identity.


## Page 91


91
x = 1
1
0
0
0
0
0
0






 and y = 0
0
1 1
1
1
1 1






 is such that 
 
x ×n y = 0
0
0
0
0
0
0
0






. 
 
Each element in I \ 
1 1 1 1
1 1 1 1
















 can generate in ideal of 
the semigroup.  
 
For consider x = 1
1
1
1
0
0
0
0






 ∈ I; 
 
〈x〉 =  
 
0
0
0
0
1
1
1
1
0
1
0
1
0
0
0
1
,
,
,
,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















 
 
1
0
0
0
0
0
1
0
0
0
1
1
0
1
0
0
,
,
,
,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0















 
 
1
1
0
0
0
1
1
0
1
0
1
0
1
0
0
1
,
,
,
,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0















 
 
1
1
1
0
0
1
1
1
1
1
0
1
1
0
1
1
,
,
,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















⊆I 
 
 is an ideal of the semigroup and order of the ideal generated by 
〈x〉 is 16. 
J = 
1 1 1
0
x
1 1 1
0


= 





## Page 92


92
0
0
0
0
1
0
0
0
0
0
0
0
0
0
1
0
,
,
,
,
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0






= 










 
 
0
0
0
0
0
1
0
0
0
0
0
0
1
1
0
0
,
,
,
,
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0















 
 
0
1
1
0
1
0
1
0
0
0
0
0
0
0
0
0
,
,
,
,
0
0
0
0
0
0
0
0
1
1
0
0
0
1
1
0















 
 
0
0
0
0
1
0
0
0
0
1
0
0
0
0
1
0
,
,
,
,
1
0
1
0
1
0
0
0
0
1
0
0
0
0
1
0















 
 
0
0
1
0
1
0
0
0
0
1
0
0
0
1
0
0
,
,
,
,
0
0
1
0
0
1
0
0
1
0
0
0
0
0
1
0















 
 
1
0
0
0
0
0
1
0
0
0
1
0
,
,
0
0
1
0
1
0
0
0
0
1
0
0












  
 
and so on}. 
 
We see order J is 26.  Thus every singleton other than {0} 
and identity generate an ideal in the trivial idempotent 
semigroup.   
 
Infact {0} generates {0} the trivial zero ideal and 
1 1 1 1
1 1 1 1






 generates the totality of the semigroup. 
 
Now having seen the collection of trivial idempotents we 
proceed onto define other properties. Using the semifields we 
can build semivector spaces.  More properties like zero divisors 
and Smarandache zero divisors are left as an exercise to the 
reader.


## Page 93


93
 
 
 
 
 
Chapter Four 
 
 
 
 
NATURAL PRODUCT ON MATRICES 
 
 
 
 
In this chapter we construct semivector space over 
semifields and vector spaces over fields using these collection 
of matrices under natural product.  
 
DEFINITION 4.1:  Let V be the collection of all n × m matrices 
with entries from Q (or R) or C.  (V, +) is an abelian group.  V 
is a vector space over Q (or R) according as V takes its entries 
from Q (or R).  If V takes its entries from Q; V is not a vector 
space over R however if V takes its entries from R, V is a vector 
space over Q as well as vector spaces over R.  We see all vector 
spaces  V (m ≠ n) are also linear algebras for using the natural 
product we get the linear algebra.   
 
 
We first illustrate this situation by some examples. 
 
Example 4.1:  Let V = {(x1, …, x5) | xi ∈ Q; 1 ≤ i ≤ 5} be a 
vector space over Q.  Infact V is a linear algebra over Q.  
Clearly dimension of V is five and a basis for V is  
 
{(1,0,0,0,0) (0,1,0,0,0) (0,0,1,0,0), (0,0,0,0,1), (0,0,0,1,0)}.


## Page 94


94
 
Example 4.2:  Let  
M = 
1
2
3
4
5
6
7
8
9
10
a
a
a
a
a
a
a
a
a
a

















ai ∈ R; 1 ≤ i ≤ 10} 
be a vector space over Q.  Clearly M is of infinite dimension. 
 
 
 
Example 4.3:  Let  
 
P = 
1
2
3
4
a
a
a
a







ai ∈ R; 1 ≤ i ≤ 4} 
be a vector space over R.  Clearly dimension of P over R is four.  
 
Example 4.4:  Let  
M = 
1
2
20
a
a
a














ai ∈ Q; 1 ≤ i ≤ 20} 
be a vector space over R. Clearly M is not a vector space over 
R.  Clearly dimension of M over Q is 20. 
 
Example 4.5:  Let  
 
T = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 9} 
 
be a vector space of dimension nine over Q.  We see T is a 
linear algebra over Q under natural product as well as under the 
usual matrix product.


## Page 95


95
 
The concept of subspace is a matter of routine and hence is 
left as an exercise to the reader.  
 
 
However we give examples of them. 
 
Example 4.6:  Let  
 
M = 
1
2
3
4
5
6
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 6} 
be a vector space over Q. 
 
 
Consider  
 
T = 
1
2
3
a
0
0
a
a
0











ai ∈ Q; 1 ≤ i ≤ 3} ⊆M; 
it is easily verified T is a subspace of M over Q. 
 
 
Consider  
 
P = 
1
2
3
a
0
a
0
a
0











ai ∈ Q; 1 ≤ i ≤ 3} ⊆ M; 
 
P is also a subspace of M over Q.  Now we consider P ∩ T (the 
intersection) of these two subspaces, 
 
P ∩ T = 
1
3
a
0
0
0
a
0











ai ∈ Q; i=1,3} ⊆ M; 
 
P ∩ T is also a subspace of M over Q.


## Page 96


96
Example 4.7:  Let  
 
P = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 9} 
 
be a vector space Q.  
 
 
Consider  
 
M1 = 
1
2
3
a
a
0
0
0
0
0
0
a











ai ∈ Q; 1 ≤ i ≤ 3} ⊆ P, 
M1 is a subspace of P over Q.  
 
 
Consider  
M2 = 
1
2
0
0
a
0
a
0
0
0
0











a1, a2 ∈ Q} ⊆ P 
 
is also a subspace of P over Q.  
 
 
However we see M1 ∩ M2 = 
0
0
0
0
0
0
0
0
0










. 
 
 
Consider  
 
M3 = 
1
2
3
0
0
0
a
0
a
0
a
0











ai ∈ Q; 1 ≤ i ≤ 3}  ⊆ P, 
M3 is a subspace of P over Q.


## Page 97


97
 
 
 
Take  
M4 = 
1
0
0
0
0
0
0
a
0
0











ai ∈ Q}  ⊆ P 
is also a subspace of P over Q. 
 
We see P = M1 + M2 + M3 + M4 and Mi ∩ Mj = 
0
0
0
0
0
0
0
0
0










 
if i ≠ j.  Thus we can write P as a direct sum of subspaces of P. 
 
Example 4.8:  Let  
 
P = 
1
2
12
a
a
a














ai ∈ Q; 1 ≤ i ≤ 12} 
 
be a vector space over Q.  
 
 
Consider  
X1 =
1
2
a
a
0
0


















a1, a2 ∈ Q} ⊆ P, 
 
X1 is a subspace of P over Q.


## Page 98


98
X2 =
1
2
3
0
a
a
a
0
0
























ai ∈ Q; 1 ≤ i ≤ 3} ⊆ P 
 
is again a subspace of P over Q. 
 
 
 Take   
 
X3 =
1
2
3
4
0
0
a
a
a
a
0
0
0
0
0



































ai ∈ Q; 1 ≤ i ≤ 4} ⊆ P 
 
is again a subspace of P over Q.


## Page 99


99
Consider  
X4 =
1
2
3
4
5
0
0
0
0
0
a
a
a
a
a

































ai ∈ Q; 1 ≤ i ≤ 5} ⊆ P 
is a subspace of P over Q. 
We see Xi ∩ Xj ≠ 
0
0
0
0
0










  if i ≠ j. 
Thus P is not a direct sum. However we see  
 
P ⊆ X1 + X2 + X3 + X4, thus we say P is only a pseudo 
direct sum of subspaces of P over Q. 
 
Thus we have seen examples of direct sum and pseudo 
direct sum of subspaces.  Interested reader can supply with more 
examples of them. Our main motivation is to define 
Smarandache strong vector spaces. 
 
It is important to mention that usual matrix vector space 
over the fields Q or R are not that interesting except for the fact 
if V is set of n × 1 column matrices then V is a vector space 
over Q or R but V is never a linear algebra under matrix 
multiplication, however V is a linear algebra under the natural


## Page 100


100
matrix product ×n.  This is the vital difference and importance of 
defining natural product ×n of matrices of same order. 
 
Now we define special strong Smarandache vector space. 
 
DEFINITION 4.2:  Let  
 
M = 












1
n
a
a
ai ∈ Q; 1 ≤ i ≤ n}. 
 
We define M as a natural Smarandache special field of 
characteristic zero under usual addition of matrices and the 
natural product ×n.  Thus {M, +, ×n} is natural Smarandache 
special field.  
 
We give an example or two. 
 
Example 4.9:  Let  
V = 
1
2
7
a
a
a














ai ∈ Q; 1 ≤ i ≤ 7} 
 
is a natural Smarandache special field of characteristic zero.  
 
 
Consider  
x = 
1
7
9
2
7
4








−






−






 ∈ V then x-1 = 
1
1/7
1/9
1/ 2
1/7
1/ 4








−






−






 ∈ V and x.x-1 = 
1
1
1
1
1
1
1











.


## Page 101


101
 
Thus 
1
1
1
1
1
1
1











 acts as the multiplicative identity. 
 
Example 4.10:  Consider the collection of 7 × 1 column 
matrices V with entries from Q.   
 
We see 
a
0
0








 a ∈ Q} = P is a proper subset of V which is a 
field hence natural S-special field. 
 
Example 4.11:  Let  
 
M = 
1
2
3
4
5
a
a
a
a
a

















 ai ∈ Q; 1 ≤ i ≤ 5} 
be a natural S-special field of characteristic zero.  M is a column 
matrix of natural Smarandache special field.  
 
 
Now if we consider  
S = {(x1, x2, …, xn) | xi ∈ Q (or R) 1 ≤ i ≤ n}. 
S under usual addition of row matrices and natural matrix 
product ×n is a natural Smarandache special field called the 
special 
rational 
natural 
Smarandache 
special 
field 
of 
characteristic zero.


## Page 102


102
 
Example 4.12:  Let V = {(x1, x2, x3, x4, x5) | xi ∈ R, 1 ≤ i ≤ 4} 
be the special real natural Smarandache special field of column 
matrices of characteristic zero.  
 
Example 4.13:  Let V = {(x1, x2) | xi ∈ R, 1 ≤ i ≤ 2} be special 
row matrix natural Smarandache special field of characteristic 
zero. 
 
 
All these fields are non prime natural Smarandache special 
fields for they have several natural S-special subfields.  
 
 
Now we can define the natural Smarandache special field of 
m × n matrices (m ≠ n). 
 
 
Let  
 
V = 
11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a
















aij ∈ R, 1 ≤ i ≤ m, 1 ≤ j ≤ n} 
 
 
V is the special m × n matrix of natural Smarandache 
special field of characteristic zero.  
 
Example 4.14: Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















aij ∈ R, 1 ≤ i ≤ 5, 1 ≤ j ≤ 4} 
 
be the special 5 × 4 matrix of natural Smarandache special field 
of characteristic zero.


## Page 103


103
 
Example 4.15: Let  
 
M = 
1
2
3
4
21
22
a
a
a
a
a
a















ai ∈ R, 1 ≤ i ≤ 22} 
 
be the 11 × 2 matrix of natural Smarandache special field of 
characteristic zero.  
 
Example 4.16: Let  
 
M = 
1
2
16
17
18
32
a
a
...
a
a
a
...
a







ai ∈ R, 1 ≤ i ≤ 32} 
 
be the 2 × 16 matrix of natural Smarandache special field.  
 
 
Now having seen natural S-special fields of m × n matrices 
(m ≠ n). We now proceed onto define the notion of natural 
special Smarandache field of square matrices. 
 
 
Let  
 
P = 
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a
















aij ∈ R, 1 ≤ i, j ≤ n} 
 
be a square matrix natural Smarandache special field of 
characteristic zero. 
 
 
We give examples of them.


## Page 104


104
Example 4.17: Let  
 
M = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ R, 1 ≤ i ≤ 9} 
 
be the 3 × 3 square matrix of natural special Smarandache field.  
 
Example 4.18: Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a


















ai ∈ R, 1 ≤ i ≤ 25} 
 
be the 5 × 5 square matrix of natural special Smarandache field 
of characteristic zero. 
 
 
Now having seen and defined the concept of matrix natural 
special Smarandache field we are in a position to define natural 
Smarandache special strong matrix vector spaces. 
 
DEFINITION 4.3:  Let 
  
V =  {(x1, x2, …, xn) | xi ∈ Q (or R), 1 ≤ i ≤ n} 
be an additive abelian group.   
 
FR = {(a1, …, an) | ai ∈ Q, 1 ≤ i ≤ n} 
be the natural special row matrix Smarandache special field.  
We see for every x = (a1, …, an) ∈ FR and v = (x1, …,  xn) ∈ V.  
xv = vx ∈ V; Further (x+y)v = xv + yv and x (v+u) = xv + xu 
for all x, y ∈ FR and v, u ∈ V. 
 
 
Finally (1, 1, …, 1)v = v ∈ V for (1, 1, …, 1) multiplicative 
identity under the natural product ×n.  Thus V is a Smarandache 
vector space over FR known as the Smarandache special strong


## Page 105


105
row vector space over the natural row matrix Smarandache 
special field FR. 
 
 
First we proceed onto give a few examples of them. 
 
Example 4.19:  Let M = {(x1, x2, x3, x4) | xi ∈ Q; 1 ≤ i ≤ 4} be a 
Smarandache special strong row vector space over the natural 
Smarandache special row matrix field  
 
FR = {(x1, x2, x3, x4) | xi ∈ Q; 1 ≤ i ≤ 4}. 
 
Example 4.20:  Let P = {(x1, x2, x3, …, x10) | xi ∈ R; 1 ≤ i ≤ 10} 
be a Smarandache special strong row vector space over the 
natural special row matrix Smarandache field  
 
FR = {(x1, x2, …, x10) | xi ∈ Q; 1 ≤ i ≤ 10}. 
 
Example 4.21:  Let T = {(x1, x2, x3, …, x7) | xi ∈ R; 1 ≤ i ≤ 10} 
be a Smarandache special strong row vector space over the 
natural special row matrix Smarandache field  
 
FR = {(x1, x2, …, x7) | xi ∈ Q; 1 ≤ i ≤ 10}. 
 
 
Now we proceed onto define natural S-special strong 
column matrix vector space over the special column matrix 
natural S-special field FC. 
 
DEFINITION 4.4:  Let  
 
V = 














1
2
n
x
x
x
xi ∈ Q (or R), 1 ≤ i ≤ n} 
be an addition abelian group. Let


## Page 106


106
FC = 
1
2
n
a
a
a














ai ∈ Q (or R), 1 ≤ i ≤ n} 
 
be the special column matrix natural S-field.  Clearly V is a S-
vector space over the natural Smarandache special field FC, we 
define V as a S-special strong column matrix vector space over 
the special column matrix natural S-field FC. 
 
 
We will illustrate this situation by some examples. 
 
Example 4.22:  Let  
 
V = 
1
2
10
x
x
x














xi ∈ Q, 1 ≤ i ≤ 10} 
 
is a S-special strong column matrix vector space over the 
special column matrix natural S-field  
 
FC = 
1
2
10
x
x
x














xi ∈ Q (or R), 1 ≤ i ≤ 10}.


## Page 107


107
Example 4.23:  Let  
 
V = 
1
2
3
4
5
a
a
a
a
a

















 ai ∈ R; 1 ≤ i ≤ 5} 
 
be a S-special strong column matrix vector space over the 
special column matrix natural S-field  
 
FC = 
1
2
3
4
5
x
x
x
x
x

















 xi ∈ R; 1 ≤ i ≤ 5}. 
 
 
Example 4.24:  Let  
 
V = 
1
2
x
x







xi ∈ R; 1 ≤ i ≤ 2} 
be a S-special strong column matrix vector space over the 
special column matrix natural S-field  
 
FC = 
1
2
x
x







 x1 , x2 ∈ Q}. 
 
 
Now we proceed onto define the notion of Smarandache 
special strong m × n (m ≠ n) matrix vector space over the 
special m × n matrix natural Smarandache special field Fm×n  
(m ≠ n).


## Page 108


108
 
Let  
M = 
11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a
















aij ∈ Q (or R), 
 
1 ≤ i ≤ m, 1 ≤ j ≤ n; m ≠ n} 
 
be a group under matrix addition. Define 
 
Fm×n (m≠n) =  
11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a
















 
aij ∈ Q (or R), 1 ≤ i ≤ m, 1 ≤ j ≤ n} 
 
to be special m × n matrix natural S-special field.  Now we see 
M is a vector space over Fm×n called the S-special strong m × n 
matrix vector space over the special m × n matrix natural S-
special field Fm×n. 
 
 
We will illustrate this situation by an example or two. 
 
Example 4.25:  Let  
 
P = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

























ai ∈ Q; 1 ≤ i ≤ 18} 
be a S-special strong 6 × 3 matrix vector space over the special 
6 × 3 matrix natural special S-field


## Page 109


109
 
F6×3 = 
1
2
3
4
5
6
16
17
18
a
a
a
a
a
a
a
a
a
















 ai ∈ Q; 1 ≤ i ≤ 18}. 
 
Example 4.26:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ R;  
 
1 ≤ i ≤ 24} 
 
be a S-special strong 3 × 8 matrix vector space over the special 
3 × 8 natural special matrix S-field  
 
F3×8 = 
1
2
8
9
10
16
17
18
24
a
a
...
a
a
a
...
a
a
a
...
a











 ai ∈ Q; 1 ≤ i ≤ 24}. 
 
Example 4.27:  Let  
 
V = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













ai ∈ R; 1 ≤ i ≤ 8} 
be a S-special strong 4 × 2 matrix vector space over the special 
4 × 2 matrix natural special S-field


## Page 110


110
F4×2 = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













 ai ∈ R; 1 ≤ i ≤ 8}. 
 
Now finally we define the S-special strong square matrix 
vector space over the special square matrix natural special S-
field Fn×n. 
 
 
Fn×n = 
11
1n
21
2n
n1
nn
a
...
a
a
...
a
a
...
a















 aij ∈ R (or Q); 1 ≤ i, j ≤ n}. 
 
 
We just define this structure. 
 
 
Let M = 
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a
















aij ∈ Q (or R), 1 ≤ i, j ≤ n}   
 
be the group under addition of square matrices.   
 
Let  
Fn×n = 
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a
















aij ∈ R, 1 ≤ i, j ≤ n} 
 
be the S-special square matrix field M is a vector space over 
Fn×n.  M is defined as the S-strong special square n×n matrix 
vector space over the special square matrix natural special S-
field Fn×n.


## Page 111


111
 
 
We will illustrate this situation by some simple examples.  
 
Example 4.28:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 9} 
 
be a special strong square 3 × 3 matrix S-vector space over the 
special 3 × 3 square matrix natural special S-field. 
 
F3×3 = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 9}. 
 
Example 4.29: Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a


















ai ∈ R, 1 ≤ i ≤ 25} 
 
be a S-special strong 5 × 5 square matrix vector space over the 
special 5 × 5 natural special Smarandache field. 
 
F5×5 = 
1
2
3
4
5
6
7
8
9
10
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a


















ai ∈ R, 1 ≤ i ≤ 25}.


## Page 112


112
Example 4.30:  Let  
 
A = 
1
2
3
4
a
a
a
a







ai ∈ R; 1 ≤ i ≤ 4} 
 
be a S-special strong 2×2 square matrix vector space over the 
special 2×2 square matrix natural special S-field  
 
F2×2 = 
1
2
3
4
a
a
a
a







ai ∈ Q; 1 ≤ i ≤ 4}. 
 
 
Now seen various types of S-special vector spaces; we now 
proceed onto define S-subspaces over natural special S-fields.  
 
DEFINITION 4.5:  Let V be a S-strong special row matrix (or 
column matrix or m × n matrix (m≠n) or square matrix) vector 
space over the special row matrix natural S-field FR (or FC or 
Fn×n (n ≠ m) or Fn×n). 
 
 
Consider W ⊆ V (W a proper subset of V); if W itself is a S-
strong special row matrix (or column matrix or m × n matrix (m 
≠ n) or square matrix) S-vector space over FR (or FC or Fm×n or 
Fn×n) then we define W to be a S-special strong row matrix 
(column matrix or m × n matrix or square matrix) vector space 
of V over FR (or FC or Fm×n or Fn×n). 
 
 
We will illustrate this situation by some simple examples. 
 
Example 4.31:  Let V = {(a1, a2, a3) | ai ∈ Q; 1 ≤ i ≤ 3} be a S-
special row matrix vector space over  
 
FR = {(x1, x2, x3) | xi ∈ Q, 1 ≤ i ≤ 3} the natural special S-
row field.  Consider M = {(a1, 0, 0) | a1 ∈ Q} ⊆ V; M is a S-
special strong row matrix vector subspace of V over FR.


## Page 113


113
 
Example 4.32:  Let  
 
V =  
1
2
6
a
a
a














ai ∈ R; 1 ≤ i ≤ 6} 
be a S-special strong vector space over the S-field;  
 
FC = 
1
2
6
a
a
a














ai ∈ Q; 1 ≤ i ≤ 6}. 
 
 
Consider  
M = 
1
2
3
a
0
a
0
a
0

























ai ∈ R; 1 ≤ i ≤ 3} ⊆ V; 
M is a Smarandache special strong vector subspace of V over 
the S-field FC. 
 
 
Take  
P =  
1
2
a
a
0
0
0
0

























a1, a2 ∈ R} ⊆ V;


## Page 114


114
P is a Smarandache special strong vector subspace of V over the 
S-field FC. 
 
Example 4.33:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 12} 
 
be a S-special strong vector space over the S-field  
 
F3×4 = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 12} ⊆ M,  
P is a S-special strong vector subspace of M over the S-field 
F3×4. 
 
Example 4.34:  Let V = {(a1, a2, …, a9) | ai ∈ R; 1 ≤ i ≤ 9} be a 
Smarandache special strong vector space over the S-field,  
FR = {(a1, a2, …, a9) | ai ∈ Q; 1 ≤ i ≤ 9}. 
 
 
Consider M1 = {(a1, 0, a2, 0, …, 0) | a1, a2 ∈ R} ⊆ V, M1 is a 
S-special strong vector subspace of V over the S-field FR.  
 
 
Consider  
 
M2 = {(0, a1, 0, a2, 0, …, 0) | ai ∈ R; 1 ≤ i ≤ 2} ⊆ V,  
M2 is a again a S-special strong vector subspace of V over FR. 
 
 
M3 = {(0, 0, 0, 0, a1, a2, 0, 0, 0) | a1, a2 ∈ R} ⊆ V, M3 is a 
again a S-special strong vector subspace of V over FR. 
 
 
M4 = {(0, 0, 0, 0, 0, 0, a1, a2, a3) | ai ∈ R; 1 ≤ i ≤ 3} ⊆ V, M4 
is again a S-special strong vector subspace of V over FR.


## Page 115


115
It is easily verified Mi ∩ Mj = (0, 0, 0, …, 0) if i ≠ j, 1 ≤ i,  
j ≤ 4 and V = M1 + M2 + M3 + M4.  Thus V is the direct sum of 
S-strong vector subspaces.  
 
Example 4.35:  Let  
 
M = 
1
2
11
12
a
a
a
a


















ai ∈ Q; 1 ≤ i ≤ 12} 
 
be a S-special strong vector space over the S-field,  
 
FC = 
1
2
11
12
a
a
a
a


















ai ∈ Q; 1 ≤ i ≤ 12}. 
 
Clearly dimension of M is also 12.  Consider the following S-
special strong vector subspaces.  
 
P1 =  
1
2
a
0
0
a


















ai ∈ Q; 1 ≤ i ≤ 2} ⊆ M, 
a S-strong vector subspace of M.


## Page 116


116
P2 =  
1
2
0
a
0
0
a
0
























ai ∈ Q; 1 ≤ i ≤ 2} ⊆ M, 
 
a S-strong vector subspace of M over FC.  
 
P3 =  
1
2
3
4
0
0
a
a
a
a
0
0






























ai ∈ Q; 1 ≤ i ≤ 4} ⊆ M, 
 
is a S-strong special vector subspace of V over FC.


## Page 117


117
P4 =  
1
2
0
0
0
0
0
0
a
a
0
0
0
0







































ai ∈ Q; 1 ≤ i ≤ 2} ⊆ M, 
is again a S-strong special vector subspace of V over FC and 
 
P5 =  
1
2
0
0
0
0
0
0
0
0
a
a
0
0







































ai ∈ Q; 1 ≤ i ≤ 2} ⊆ M 
 
is again a S-strong special vector subspace of V over FC.


## Page 118


118
We see Pi ∩ Pj = 
0
0
0
0








  if i ≠ j; 1 ≤ i, j ≤ 5 and  
V = P1 + P2 + P3 + P4 + P5.  
 
Thus V is a direct sum of S-special strong vector subspaces. 
 
Example 4.36:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a













ai ∈ R; 1 ≤ i ≤ 12} 
 
be a S-strong special vector space over the S-field,  
 
F4×3 = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a













ai ∈ R; 1 ≤ i ≤ 12}. 
 
Let B1 = 
1
2
3
4
a
a
0
0
0
0
0
0
0
0
a
a













ai ∈ R; 1 ≤ i ≤ 4} ⊆ M 
 
be a S-strong special subvector space of M over F4×3 .


## Page 119


119
B2 =  
1
2
3
4
a
0
a
0
a
a
0
0
0
0
0
0













ai ∈ R; 1 ≤ i ≤ 4} ⊆ M 
be a S-strong special vector subspace of M over F4×3.  
 
B3 = 
1
2
3
a
0
0
a
0
0
a
0
0
0
0
0













ai ∈ R; 1 ≤ i ≤ 3} ⊆ M 
is a S-strong special vector subspace of M over F4×3.  
 
 
Finally  
B4 = 
1
2
3
4
a
0
0
0
0
0
0
a
a
a
0
0













ai ∈ R; 1 ≤ i ≤ 4} ⊆ M 
is again a S-strong special vector subspace of V over F4×3. 
 
 
We see Bi ∩ Bj ≠ 
0
0
0
0
0
0
0
0
0
0
0
0












; even if i ≠ j, 1 ≤ i, j ≤ 4.  
 
But V ⊆ B1 + B2 + B3 + B4; so we define V to be the pseudo 
direct sum of the S-special strong vector subspaces of V.  Now 
we have seen examples of direct sum and pseudo direct sum of 
S-special strong vector subspaces of a S-special strong vector 
space over a S-field. 
 
 
The main use of this structure will be found as and when 
this sort of study becomes familiar and in due course of time


## Page 120


120
they may find applications in all places where the result is not a 
real number (or a rational number) but an array of numbers. 
 
 
We can define orthogonal vectors of S-special strong matrix 
vector spaces also. 
 
 
First we see how orthogonal vector matrices are defined 
when they are defined over R or Q or C.  
 
 
Let VR = {(a1, …, an) | ai ∈ Q; 1 ≤ i ≤ n} be a row matrix 
vector space defined over the field Q. 
 
 
We define for any x = (a1, …, an) and y = (b1, …, bn) in VR, 
x is perpendicular to y if x ×n y = (0).   
 
Thus if VR = {(x1, x2, x3, x4, x5) | xi ∈ R; 1 ≤ i ≤ 5} be a row 
matrix vector space defined over Q and if x = (0, 4, -5, 0, 7) and 
y = (1, 0, 0, 8, 0) are in VR.  We see x ×n y = (0) so x is 
orthogonal with y. 
 
 
VC =  
1
n
a
a












ai ∈ Q, (or R); 1 ≤ i ≤ n} be the vector space 
of column matrices over Q (or R) respectively. 
 
 
 
We say two elements x = 
1
2
n
x
x
x













 and y = 
1
2
n
y
y
y













 in VC are 
orthogonal if x ×n y = 
1
2
n
x
x
x













 ×n 
1
2
n
y
y
y













 = (0).


## Page 121


121
 
For instance if x = 
2
1
0
0
0
7




−
















 and y = 
0
0
1
2
3
0










 then  
 
x ×n y =
2
1
0
0
0
7




−
















 ×n  
0
0
1
2
3
0










 = 
0
0
0
0
0
0










. 
 
Now we can define, unlike in other matrix vector space in 
case of these vector spaces Vm×n (m ≠ n) and Vn×n the 
orthogonality under natural product.  This is a special feature 
enjoyed only by vector spaces on which natural product can be 
defined.  
 
 
We just illustrate this situation by some examples. 
 
Example 4.37:  Let  
 
V5×3 = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















ai ∈ R; 1 ≤ i ≤ 15} 
 
be a 5 × 3 matrix linear algebra (vector space) over Q.


## Page 122


122
Now let  
 
x = 
3
2
0
0
1
5
1
1
0
2
0
7
0
1
8
















 and y = 
0
0
7
9
0
0
0
0
9
0
8
0
4
0
0
















 be in V5×3, 
 
we see x ×n y = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















 thus we say x is orthogonal to y 
under natural product in V5×3. 
 
 
It is pertinent to mention here that we can have several y’s 
in V5×3 such that for a given x in V5×3.  x ×n y = (0). 
 
 
Now we see all elements in V5×3 are orthogonal under 
natural product to the zero 5 × 3 matrix 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















. 
Example 4.38:  Let  
 
V2×6 = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a







ai ∈ Q; 1 ≤ i ≤ 12} 
 
be a vector space over Q.  Under natural product defined on 
V2×6 we can get orthogonal elements.


## Page 123


123
Take x = 
1
3
5
2
4
6
a
a
a
0
0
0
a
a
a
0
0
0






 and 
 
y = 
1
3
2
4
0
0
0
a
0
a
0
0
0
a
0
a






 in V2×6. ai ∈ Q; 1 ≤ i ≤ 6. 
 
We see x ×n y = 0
0
0
0
0
0
0
0
0
0
0
0






. 
 
 
Thus x is orthogonal with y.  Infact we have several such 
y’s which are orthogonal with x. 
 
Example 4.39:  Let  
 
V = 
1
2
3
4
a
a
a
a







ai ∈ R; 1 ≤ i ≤ 4} 
be a 2 × 2 matrix vector space over the field R. ×n be the natural 
product on V. 
 
 
We define two matrices in V to be orthogonal if  
 
x ×n y = 0
0
0
0






 for y, x ∈ V.  We see x = 
1
2
a
0
0
a






, 
 
then y = 
1
0
b
0
0






 is orthogonal with x.   
 
Also 
1
0
0
b
0






 = a is such that x ×n a = (0).


## Page 124


124
Further 
1
2
0
b
b
0






 = b, is orthogonal with x under natural 
product as x ×n b = 0
0
0
0






. 
 
 
Now x⊥ = 
1
1
2
1
0
b
0
0
0
0
0
b
,
,
,
b
0
b
0
0
0
0
0


































.  Clearly 
x⊥ is additively closed and also ×n product also is closed; infact 
x⊥ is a proper subspace of V defined as a subspace 
perpendicular with x. 
 
 
Consider x = 0
a
b
0






 in V; now the elements perpendicular 
with x are 
0
0
t
0
0
0
t
0
,
,
,
0
0
0
0
0
u
0
u

























.   
 
We see this is also a subspace of V.   
 
Infact if  
 
B = 
0
0
t
0
0
0
x
0
,
,
,
0
0
0
0
0
u
0
y

























 ⊆ V  
 
and 
 
C = 
0
0
0
a
0
0
0
a
,
,
,
0
0
0
0
b
0
b
0

























 ⊆ V 
are such that they are orthogonal subspaces under product.   
 
For B ×n C = 
0
0
0
0
















.


## Page 125


125
Example 4.40:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q; 1 ≤ i ≤ 9} 
be a 3 × 3 vector space over the field Q.  Consider an element, 
 
x = 
a
b
c
0
0
0
0
0
d










 in M. 
 
The elements perpendicular to x be denoted by  
x⊥ = B =  
 
1
2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0 , 0
0
a
, a
0
0 , 0
b
0 ,
0
0
0
0
0
0
0
0
0
0
0
0


























 
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0 , 0
0
0 , a
b
0 , a
0
b , 0
a
b ,
d
0
0
0
e
0
0
0
0
0
0
0
0
0
0






























 
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a , 0
0
a , a
0
0 , a
0
0 , 0
a
0 ,
b
0
0
0
b
0
b
0
0
0
b
0
b
0
0






























 
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
0 , 0
0
0 , a
b
c , a
b
0 , a
b
0 ,
0
b
0
a
b
0
0
0
0
c
0
0
0
c
0
































## Page 126


126
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
b , 0
a
b , a
0
b , a
0
b , a
0
0 ,
c
0
0
0
c
0
c
0
0
0
c
0
b
c
0






























 
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
0 , 0
0
a , a
b
c , a
b
c , a
b
c ,
b
c
0
b
c
0
d
b
0
d
0
0
0
d
0






























 
 
0
0
0
0
0
0
0
0
0
0
a
b , a
0
b , a
b
0
c
d
0
d
c
0
d
c
0






















 ⊆ M 
 
is again a subspace orthogonal with x. 
 
Inview of this we have the following theorem. 
 
THEOREM 4.1:  Let V be a matrix vector space over a field F.  
Let 0 ≠ x ∈ V.  The elements orthogonal to x under natural 
product ×n is a subspace of V over F. 
 
Proof:  Let 0 ≠ x ∈ V.  Suppose x⊥ = B = {y ∈ V | y ×n x = 0}, 
to show B is a subspace of V. 
 
 
Clearly B ⊆ V, by the very definition of orthogonal element 
of x.  Further (0) ∈ V is such that x ×n (0) = (0) so (0) is 
orthogonal with x.  Now let z, y ∈ B be orthogonal with x under 
×n.  To show y + z  is orthogonal to x.  Given x ×n y = (0) and  
x ×n z = (0).  Now consider 
 
x ×n (y+z) = x ×n y + x ×n z 
 
 
 
 
 
= (0) + (0) 
 
 
 
 
 
= (0);


## Page 127


127
 
so y + z ∈ B.  Also if y ∈ B is such that x ×n y = 0 then x ×n (–y) 
= 0 so if y ∈ B then –y ∈ B.  Finally let a ∈ F and y ∈ B to 
show ay ∈ B.  Consider x ×n ay = a (x ×n y) = a.0 = 0. 
 
 
Thus B ⊆ V is a vector subspace of V. 
 
 
Now we can define orthogonality of two elements in matrix 
vector spaces under natural product, we now derive various 
properties associated with orthogonal natural product. 
 
Example 4.41:  Let  
 
W = 
a
b
c
d
e
f
g
h
i











a, b, c, d, e, f, g, h, i ∈ Q} 
 
be a vector space over Q.   
 
 
Consider x⊥ = B =  
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0 , 0
0
0 , 0
0
0 , 0
0
0 ,
0
0
0
a
0
0
0
b
0
0
0
c


























  
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0 , 0
0
0 , 0
0
0 , 0
0
0
a
b
0
a
0
b
0
a
b
a
b
c



























 ⊆ W 
 
is a subspace of V.  Consider the complementary space of B.


## Page 128


128
B⊥=
0
0
0
a
0
0
0
b
0
0
0
c
0
0
0 , 0
0
0 , 0
0
0 , 0
0
0 ,
0
0
0
0
0
0
0
0
0
0
0
c


























 
 
0
0
0
0
0
0
0
0
0
0
0
0
a
b
0
0
0
0 , d
0
0 , 0
e
0 , 0
0
f , 0
0
0 ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
0
a
b
a
0
b
a
0
0
0
0
0
0
0
0
0
0
0 , 0
0
0 , b
0
0 , a
b
0 , a
0
c ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
0
0
0
a
0
0
a
0
0
0
a
0
0
a
0
0
a
b , 0
b
0 , 0
0
b , b
0
0 , 0
b
0 ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
0
a
0
0
0
a
0
0
a
0
0
a
a
b
c
0
0
b , b
0
0 , 0
b
0 , 0
0
b , 0
0
0 ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
0
0
0
a
0
0
a
0
0
a
0
b
a
0
0
a
b
c , 0
b
c , b
c
0 , 0
c
0 , b
0
c ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
a
0
b
a
0
b
a
0
0
a
0
0
a
0
0
c
0
0 , 0
0
c , b
c
0 , 0
b
c , b
0
c ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
0
a
0
0
a
0
0
a
0
0
0
a
0
0
a
b
c
0 , 0
b
c , b
0
c , b
c
0 , b
0
c ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
































## Page 129


129
 
0
0
a
0
a
b
0
a
b
0
a
b
a
b
c
0
b
c , c
0
0 , 0
c
0 , 0
0
c , 0
0
0 ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
a
b
c
a
b
c
0
a
b
0
a
b
0
a
b
0
d
0 , 0
0
d , d
0
c , d
c
0 , 0
d
c ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
a
0
0
0
a
0
0
0
a
a
b
0
a
0
d
b
c
d , b
c
d , b
c
d , c
d
0 , b
0
c ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
a
0
b
a
0
b
a
b
0
a
b
c
a
b
c
0
c
d , c
d
0 , c
0
d , 0
d
e , d
e
0 ,
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






























 
 
0
a
b
a
b
0
a
0
b
a
b
c
c
d
e , c
d
e , d
e
c , d
e
f
0
0
0
0
0
0
0
0
0
0
0
0



























 
 
 
We see B⊥ ⊕ B = W.   
 
 
Thus we have the following theorem. 
 
THEOREM 4.2:  Let V be a matrix vector space over a field F.  
Suppose 0 ≠ x ∈ V and let W be the subspace of V 
perpendicular to V then the complement of W denoted by W⊥ is 
such that for every a ∈ W and b ∈ W⊥   a ×n b = (0).  Further V 
= W⊥ ⊕ W. 
 
 
The proof is simple hence left as an exercise to the reader.


## Page 130


130
COROLLARY 4.1:  Let V be a matrix vector space over the field 
F.  {0} ∈ V; the space perpendicular to V under natural product 
×n is V, that is {0}⊥ = V. 
 
COROLLARY 4.2:  Let V be a matrix vector space over the field 
F.  The space perpendicular to V under natural product is {0} 
that is {V}⊥ = {0}. 
 
 
Example 4.42:  Let  
 
V = 
1
2
3
4
5
6
a
a
a
a
a
a







ai ∈ Q; 1 ≤ i ≤ 6}  
 
be a vector space over Q.   
 
Now consider x = 
1
2
3
4
0
a
a
0
a
a






 be the element of V.  The 
vectors perpendicular or orthogonal to x are given by  
 
a
0
0
0
0
0
a
0
0
0
0
0
,
,
,
0
0
0
a
0
0
b
0
0
0
0
0

























 = B. 
 
 
Now take y = a
0
0
b
0
0






 ∈ B, the vectors perpendicular to 
y are y⊥ =  
 
1
3
2
0
0
0
0
0
0
0
0
0
0
a
0
0
0
a
,
,
,
,
,
0
0
a
0
a
0
0
0
0
0
0
0
0
0
0

























 
 
1
1
2
1
2
2
0
0
0
0
a
0
0
a
a
0
0
x
0
0
a
,
,
,
,
,
0
a
a
0
a
0
0
0
0
0
0
y
0
b
c


























## Page 131


131
0
a
0
0
0
c
0
a
b
0
a
b
0
a
0
0
a
b
,
,
,
,
,
0
0
b
0
d
0
0
c
0
0
0
b
0
b
c
0
c
d






















 
 
We see x ∈ y⊥ under natural product.  Now 〈x⊥〉 = {y ∈ V | 
x ×n y = (0)} and 〈y⊥〉 = {x ∈ V | x ×n y = {0}} are not only 
subspaces of V but are such that 〈x⊥〉 ∪ 〈y⊥〉 = V and 〈x⊥〉 ∩ 〈y⊥〉 
= {(0)}.   
 
Further x = 0
a
b
0
c
d






 is in 〈y⊥〉. 
 
Suppose z⊥ = a
0
0
0
0
0






 ∈ B is taken 
 
z⊥ = {m ∈ V | m ×n z = (0)}. 
 
= 
0
0
0
0
a
0
0
0
b
0
0
0
0
0
0
,
,
,
,
,
0
0
0
0
0
0
0
0
0
x
0
0
0
y
0



















 
 
0
0
0
0
a
b
0
b
0
0
a
0
0
a
0
,
,
,
,
,
0
0
t
0
0
0
a
0
0
0
b
0
0
0
b


















 
 
0
0
a
0
0
a
0
0
a
0
0
0
0
0
0
,
,
,
,
,
b
0
0
0
b
0
0
0
b
a
b
0
a
0
b


















 
 
0
0
0
0
a
b
0
a
b
0
a
b
0
a
0
,
,
,
,
,
0
a
b
c
0
0
0
c
0
0
0
c
b
c
0


















 
 
0
a
0
0
a
0
0
0
a
0
0
a
0
0
a
,
,
,
,
,
b
0
c
0
b
c
b
c
0
b
0
c
0
b
c




















## Page 132


132
0
0
0
0
a
b
0
a
b
0
a
b
0
0
a
,
,
,
,
,
a
b
c
0
c
d
c
0
d
c
d
0
b
c
d


















 
 
0
a
0
0
a
b
,
b
c
d
d
c
x










 = T. 
 
We see though z ∈ B still 〈z⊥〉 ≠ 〈y⊥〉. 
 
Further every element in T is not perpendicular to x under 
the natural product ×n. 
 
For consider m = 0
a
0
b
c
d






 in T and  
 
x ×n m = 0
a
b
0
c
d






 ×n 0
a
0
b
c
d






 
 
= 
1
1
1
0
x
0
0
y
z






 ≠ 0
0
0
0
0
0






. 
 
Thus we can say for any x ∈ V we have one and only one y 
in V such that x is the complement of y with respect to natural 
product ×n.  
 
We say complement, if x⊥ generates the space B and y⊥ 
generates another space say C. 
 
Thus for x = 0
a
b
0
c
d






 we say, y = m
0
0
n
0
0






  
 
to be the main complement; a, b, c, d, m, n ∈ Q \ {0}.  We say y 
is also the main complement of x with respect to natural product 
×n.


## Page 133


133
THEOREM 4.3:  Let V be a matrix vector space over the field Q 
(or R).  Let ×n be the natural product defined on V.  If for x in V, 
y is the main complement of V and vice versa, then 〈x⊥〉 + 〈y⊥〉 = 
V and 〈x⊥〉 ∩ 〈y⊥〉 = (0). 
 
(1) However for no other element t in 〈y⊥〉 t will be the 
main complement of x. 
 
(2) Also no element in 〈x⊥〉 will be the main 
complement of y only x will be the main 
complement of y.   
 
The proof is left as an exercise.  However we illustrate this 
situation by some example. 
 
 
Example 4.43:  Let  
 
M = 
a
b
c
d







a, b, c, d ∈ Q} 
be the vector space of 4 × 4 matrices over the field F = Q. 
 
 
Take p = x
0
y
0






 ∈ M, now the complements of p under 
natural product in M are 
0
0
0
a
0
a
,
,
,
0
0
0
b
0
0













 
0
0
0
b






a, b ∈ Q} = T. 
 
 
The main complement of p under natural product ×n is  
 
q = 0
a
0
b






 ∈ T.


## Page 134


134
 
Now the complements of q under natural product ×n in  
M are 
0
0
a
0
a
0
0
0
,
,
,
0
0
b
0
0
0
a
0
















a, b ∈ Q}. 
 
 
We see V + T = M and V ∩ T = 0
0
0
0






. 
 
 
Now x = 0
a
0
0






 is in T.  We find the elements orthogonal 
to x in M under the natural product ×n. 
 
〈x⊥〉 = 
0
a
0
0
⊥






 =  
0
0
a
0
0
0
0
0
,
,
,
,
0
0
0
0
b
0
0
c
















 
 
a
0
a
0
0
0
a
0
,
,
,
b
0
0
c
b
c
b
c
















. 
 
 
The main complement of x in M is a
0
b
c






 others are just 
complements. 
 
 
Consider  
 
a
0
b
0






 ∈
a
0
b
0
⊥






 = 
0
0
0
0
0
b
0
a
,
,
,
0
0
0
a
0
0
0
b

























. 
 
 
The main complement of 
a
0
b
0






 is 
0
a
0
b






; other 
elements being just complements.


## Page 135


135
Example 4.44:  Let  
 
V = 
1
2
8
a
a
a














ai ∈ Q; 1 ≤ i ≤ 8} 
 
be a vector space of column matrices over the field Q.   
 
Consider the element a = 
1
2
3
a
a
0
0
0
0
0
a


























 in V.   
 
To find complements or elements orthogonal to  
 
〈a〉⊥ = 
1
2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
0
0
a
0
0
0
a
,
,
,
,
,
,
a
0
a
0
0
0
0
0
0
a
0
0
0
0
0
a
0
0
0
0
0
0

















1
2
0
0
a
0
,
,
a
0
0
0











































## Page 136


136
1
1
1
1
1
1
2
2
2
2
2
2
0
0
0
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
a
a
a
,
,
,
,
,
0
0
a
a
0
0
a
0
a
0
a
0
0
a
0
0
0
a
0
0
0
0
0
0














































































1
1
2
2
0
0
0
0
0
0
0
0
,
,
,
a
0
0
a
a
a
0
0















































 
 
1
1
1
1
1
1
2
2
2
3
2
2
3
3
2
3
3
3
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a
a
a
a
0
0
0
,
,
,
,
,
a
0
0
a
0
a
0
a
0
a
a
0
0
0
a
0
a
a
0
0
0
0
0














































































1
1
2
3
2
3
0
0
0
0
0
0
a
a
,
,
,
a
0
a
a
0
a
0
0
0




















































 
 
1
1
1
1
2
2
1
2
1
3
3
2
2
2
4
3
3
3
4
4
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
0
a
0
a
a
0
a
,
,
,
,
,
a
a
a
a
a
a
0
a
a
0
a
a
a
0
a
a
0
0
0
0
0














































































1
2
3
3
4
4
5
0
0
a
a
, a
a
a
a
a
0
0












































.


## Page 137


137
 
The main complement of 
1
2
3
a
a
0
0
0
0
0
a


























 is 
1
2
3
4
5
0
0
a
a
a
a
a
0


























.  
 
 
Certainly this type of study will be a boon to algebraic 
coding theory as in case of algebraic coding theory we mainly 
use only matrices which are m × n (m ≠ n) as parity check 
matrix and generator matrix. 
 
 
Now we define other related properties of these matrices 
with natural product on them.  Suppose S is a subset of a matrix 
vector space defined on R or Q we can define  
 
S⊥ = {x ∈ V | x ×n s = (0) for every s ∈ S}. 
 
 
We will illustrate this situation by some simple example. 
 
Example 4.45:  Let  
 
V = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













ai ∈ Q; 1 ≤ i ≤ 8} 
 
be a vector space of 4 × 2 matrices defined over the field V. V is 
a linear algebra under the natural product.


## Page 138


138
Consider  
 
S =
a
b
0
0
0
0
0
0
,
0
0
0
0
0
0
c
d



















a, b, c, d ∈ Q} ⊆ V. 
 
To find S⊥ . S⊥ = 
0
0
0
0
0
0
0
0
0
0
a
b
a
0
0
a
,
,
,
,
0
0
d
e
0
0
0
0
0
0
0
0
0
0
0
0































 
 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
b
,
,
,
,
b
0
0
d
a
b
0
0
0
0
0
0
0
0
0
0






























 
 
0
0
0
0
0
0
0
0
a
0
a
0
0
a
0
b
,
,
,
,
0
b
b
0
0
b
a
0
0
0
0
0
0
0
0
0






























 
 
     
0
0
0
0
0
0
0
0
a
b
a
b
0
a
a
0
,
,
,
c
0
0
c
b
c
b
d
0
0
0
0
0
0
0
0
































 ⊆ V 
 
is the orthogonal complement S⊥.


## Page 139


139
We see S⊥ is a subspace of V.  Further the main 
complement of x = 
a
b
0
0
0
0
0
0












 and 
0
0
0
0
0
0
b
c












 = y are not in S⊥ for the 
main complement of x is 
0
0
a
b
c
d
e
f












 and that of y is 
a
b
c
d
e
f
0
0












 but 
the main complement of x is not orthogonal with y; for y ×n x⊥. 
 
= 
0
0
0
0
0
0
b
c












 
0
0
a
b
c
d
e
f












 = 
0
0
0
0
0
0
be
cf












 ≠ 
0
0
0
0
0
0
0
0












. 
 
 
Similarly the main complement of 
0
0
0
0
0
0
a
b












, that is 
a
b
c
d
e
f
0
0












 
is not orthogonal with 
a
b
0
0
0
0
0
0












 under natural product as  
 
 
a
b
0
0
0
0
0
0












 ×n 
1
1
a
b
c
d
e
f
0
0












 = 
1
1
a a
bb
0
0
0
0
0
0












 ≠ 
0
0
0
0
0
0
0
0












.


## Page 140


140
 
We can define as in case of usual vector spaces define linear 
transformation for matrix vector spaces.  However it is meaning 
less to define linear transformation in case of S-special strong 
vector spaces defined over the S-field.  However in that case 
only linear operators can be defined.  The definition properties 
etc in case of the former vector space is a matter of routine and 
we see no difference with usual spaces.  However in case of 
latter S-special strong vector spaces over a S-field we can define 
only linear operators. 
 
We just illustrate this situation by an example. 
 
Example 4.46:  Let  
 
V = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













ai ∈ R; 1 ≤ i ≤ 8} 
 
be a S-special super vector space over the S-field.   
 
F4×2 = 
a
b
c
d
e
f
g
h













a, b, c, d, e, f, g, h ∈ Q}. 
 
Now we define a map η : V → V as  
 
η
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a


























 = 
1
2
3
4
a
0
0
a
a
0
0
a












.


## Page 141


141
It is easily verified η is a linear operator on V. 
 
We can find kernel η = 
a
b
a
b
c
d
c
d
V
(0)
e
f
e
f
g
h
g
h

















∈
η
=




















 
   = 
0
a
b
0
0
c
d
0













a, b, c, d ∈ Q} 
is a subspace of V.  Now interested reader can work with linear 
operators on S-special strong vector spaces over the S-field.   
 
 
Thus all matrix vector spaces are linear algebras under the 
natural product.  Now as in case of usual vector spaces we can 
for the case of matrix vector spaces also define the notion of 
linear functional.  But in case of S-strong special matrix vector 
spaces we can not define only Smarandache linear functional as 
matter of routine as it needs more modifications and changes.  
 
 
Now we have discussed some of properties about vector 
spaces.  We now define n - row matrix vector space over a field 
F. 
 
DEFINITION 4.6:  Let 
  
V = {(a1, …, am) | ai = (x1, …, xn);  xj ∈ Q; 
1 ≤ i ≤ m, 1 ≤ j ≤ n}; 
 
V is a vector space over Q defined as the n-row matrix 
structured vector space over Q. 
 
 
We will illustrate this situation by some examples.


## Page 142


142
Example 4.47:  Let V = {(a1, a2, a3, a4) | aj = (x1, x2, x3, x4, x5) 
where xi ∈ Q, 1 ≤ i ≤ 5 and 1 ≤ j ≤ 4} be a 5-row matrix 
structured vector space over Q. 
 
 
We will just show how addition and scalar multiplication is 
performed on V. 
 
 
Suppose x = ((3, 0, 2, 4, 5), (0, 0, 0, 1, 2), (1, 1, 1, 3, 0), (2, 
0, 1, 0, 5)) ∈ V and a = 7 then 7x = ((21, 0, 14, 28, 35), (0, 0, 0, 
7, 14), (7, 7, 7, 21, 0), (14, 0, 7, 0, 35)) ∈ V. 
 
 
Let y = ((4, 0, 1, 1, 1), (0, 1, 0, 1, 2), (1, 0, 1, 1, 1), (2, 0, 0, 
0, 1)) ∈ V then x + y = ((7, 0, 3, 5, 6), (0, 1, 0, 2, 4), (2, 1, 2, 4, 
1), (4, 0, 1, 0, 6)) ∈ V.  We see V is a row matrix structured 
vector space over Q. 
 
Example 4.48:  Let  
 
P = {(a1, a2, a3) | ai = (x1, x2, …, x15) xj ∈ Q; 
1 ≤ i ≤ 3; 1 ≤ j ≤ 15} 
 
a row matrix structured vector space over Q.  We can define 
row matrix structured subvector space as in case of usual vector 
space.  On P we can always define the natural product hence P 
is always a row matrix structured linear algebra under the 
natural product ×n. 
 
Example 4.49:  Let  
 
V = {(a1, …, a10) | ai = (x1, x2, x3); xj ∈ Q; 1 ≤ j ≤ 3; 1 ≤ i ≤ 10} 
 
be a row matrix structured vector space over Q.  Consider H = 
{(a1, a2, a3, 0, 0, 0, 0, 0, 0, 0) | ai = (x1, x2, x3); xj ∈ Q; 1 ≤ i ≤ 3} 
⊆ V; H is a row matrix structured vector subspace of V over Q.  
Also  
 
P = {(a1, a2, …, a10) | ai = (x1, 0, x2) 
with x1, x2 ∈ Q; 1 ≤ i ≤ 10} ⊆ V


## Page 143


143
is a row matrix structured vector subspace of V over Q.  The 
reader can see the difference between the subspaces P and H. 
 
 
Let V = {(x1, …, xn) | xi ∈ R+ ∪ {0}, 1 ≤ i ≤ n} be a 
semigroup under addition.  V is a semivector space over the 
semifield R+ ∪ {0} or Q+ ∪ {0} or Z+ ∪ {0}. 
 
 
Likewise M =
1
2
m
x
x
x














xi ∈ Q+ ∪ {0}, 1 ≤ i ≤ m} be a 
semigroup under addition.  M is a semivector space over the 
semifield Z+ ∪ {0} or Q+ ∪ {0}.  M is not a  semivector space 
over R+ ∪ {0}.   
 
P = 
11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a
















aij ∈ Z+ ∪ {0}, 
1 ≤ i ≤ m, 1 ≤ j ≤ n} 
 
is a semivector space over the semifield Z+ ∪ {0}. 
 
T = 
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a
















aij ∈ Q+ ∪ {0}, 1 ≤ i, j ≤ n} 
is a semivector space over the semifield Q+ ∪ {0}.  M, P T and 
V are also semilinear algebras over the respective semifields 
under the natural product ×n. 
 
 
We will illustrate these situations by some examples.


## Page 144


144
 
 
Example 4.50:  Let  
V = {(x1, x2, x3, x4, x5, x6) | xi ∈ 3Z+ ∪ {0}; 1 ≤ i ≤ 6} 
 
be the semivector space over the semifield S = Z+ ∪ {0}. 
 
 
V is also a semilinear algebra over the semifield S. 
 
Example 4.51:  Let  
V1 = {(x1, x2, x3, x4, x5, x6) where xi ∈ R+ ∪ {0}; 1 ≤ i ≤ 6} 
 
be the semivector space over the semifield S = Z+ ∪ {0}. 
 
 
It is interesting to compare V and V1 for V1 is finite 
dimensional where as V2 is of infinite dimension. 
 
Example 4.52:  Let  
 
V = 
1
2
3
4
5
6
7
8
x
x
x
x
x
x
x
x



























xi ∈ Z+ ∪ {0}, 1 ≤ i ≤ 8} 
 
be a semivector space over the semifield S = Z+ ∪ {0}.  V is a 
semilinear algebra over S. 
 
 
Dimension of V over S is eight.


## Page 145


145
Example 4.53:  Let  
 
M = 
1
2
3
4
5
6
7
8
x
x
x
x
x
x
x
x



























xi ∈ Q+ ∪ {0}, 1 ≤ i ≤ 8} 
 
be a semivector space over the semifield S = Z+ ∪ {0}.  Clearly 
dimension of M over S is infinite. 
 
Example 4.54:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

































ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 40} 
 
be a semivector space over the semifield S = Z+ ∪ {0}.  Clearly 
V is not defined over the semifield T = Q+ ∪ {0} or R+ ∪ {0}.  
Dimension of V over S in 40.


## Page 146


146
Example 4.55:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 9} 
 
be a semivector space over the semifield S = Z+ ∪ {0} = S. 
 
 
Take  
P = 
1
2
3
4
5
6
a
a
a
a
0
a
a
0
0











ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 9}, 
 
P is a semivector subspace of V over S = Z+ ∪ {0}. 
 
Example 4.56:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

























ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 18} 
be a semivector space over the semifield S = Q+ ∪ {0}. 
 
M1 = 
1
2
3
a
a
a
0
0
0
0
0
0
















ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 3} ⊆ M 
is a semivector subspace of M over S = Q+ ∪ {0}, the 
semivector space.


## Page 147


147
M2 = 
1
2
3
4
5
6
0
0
0
a
a
a
a
a
a
0
0
0
0
0
0
0
0
0

























ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 6} ⊆ M 
is a semivector subspace of M over S = Q+ ∪ {0}. 
  
M3 = 
1
2
3
4
5
6
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a
0
0
0

























ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 6} ⊆ M 
is a semivector subspace of M over S = Q+ ∪ {0} and  
 
M4 = 
1
2
3
4
5
6
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a

























ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 6} ⊆ M 
is the semivector subspace of M over S.   
We see M = M1 + M2 + M3 + M4 and Mi ∩ Mj = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0




















 
if i ≠ j, 1 ≤ i, j ≤ 4.


## Page 148


148
 
Thus  M is the direct sum of semivector subspaces of M 
over S. 
 
Example 4.57:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 15} 
be a semivector space over the semifield S = Z+ ∪ {0}. 
 
 
Consider  
 
P1 = 
1
2
3
a
0
0
0
0
a
0
0
0
0
a
0
0
0
0











ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 3} ⊆ V 
be a semivector subspace of V over S.  
 
 
Let  
 
P2 = 
4
1
2
3
a
a
a
0
0
0
0
a
0
0
0
0
0
0
0











ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 4} ⊆ V 
be a semivector subspace of V over S.   
 
Consider  
 
P3 = 
1
2
4
3
a
0
a
0
0
0
a
a
0
0
0
0
0
0
0











ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 4} ⊆ V, 
a semivector subspace of V over S.


## Page 149


149
Further  
 
P4 = 
1
2
3
4
a
0
a
0
0
0
0
0
0
0
a
0
a
0
0











ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 4} ⊆ V, 
is a semivector subspace of V over S.  
 
P5 = 
1
3
4
2
5
a
0
0
a
a
0
0
0
a
0
0
a
0
0
0











ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 5} ⊆ V 
is a semivector subspace of V over S. 
 
P6 = 
1
5
2
3
4
a
0
0
0
0
0
0
0
0
a
0
0
a
a
a











ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 5} ⊆ V, 
is a semivector subspace of V over S. 
 
We see Pi ∩ Pj ≠ 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0










 if i ≠ j, 1 ≤ i, j ≤ 6. 
We see V ⊆ P1 + P2 + P3 + P4 + P5 + P6; thus V is a pseudo 
direct sum of semivector subspaces. 
 
 
Now we have seen examples of direct sum and pseudo 
direct sum of semivector subspaces over the semifield S = Z+ ∪ 
{0}.  Now we can as in case of other semivector spaces define 
linear transformation and linear operator.   
 
We give examples of semivector space with polynomial 
matrix coefficient elements.


## Page 150


150
Example 4.58:  Let  
 
V = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, x3, x4) | xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 4} 
be a semivector space of infinite dimension over S = Z+ ∪ {0}.  
 
 
Clearly V is also a semilinear algebra over S under the 
natural product ×n. 
 
Example 4.59:  Let  
 
M = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
10
x
x
x
x

















 where xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 10} 
be a semivector space of infinite dimension over S = Z+ ∪ {0}.  
 
Example 4.60:  Let  
 
P = 
i
i
i 0
d x
∞
=


∑
 di = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a












 
where ai ∈ Q+ ∪ {0}; 1 ≤ i ≤ 16} 
 
be a semivector space of infinite dimension over S = Q+ ∪ {0}.  
 
 
Example 4.61:  Let  
 
M = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
10
11
12
20
21
22
30
d
d
...
d
d
d
...
d
d
d
...
d










 
where di ∈ Z+ ∪ {0}; 1 ≤ i ≤ 30}


## Page 151


151
 
be a semivector space of infinite dimension over S = Z+ ∪ {0}.  
 
 
Example 4.62:  Let  
S = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
10
11
12
20
81
82
90
d
d
...
d
d
d
...
d
d
d
...
d















 
 
with di ∈ Z+ ∪ {0}; 1 ≤ i ≤ 9} 
 
be a semivector space of infinite dimension over S = Z+ ∪ {0}.  
 
Example 4.63:  Let  
 
T = 
i
i
i 0
a x
∞
=


∑
 aj = 
1
2
n
n 1
n 2
2n
2n 1
2n 2
3n
7n 1
7n 2
8n
d
d
...
d
d
d
...
d
d
d
...
d
d
d
...
d
+
+
+
+
+
+



















 
 
with di ∈ Z+ ∪ {0}; 1 ≤ i ≤ 8n} 
 
be a semivector space over the semifield of infinite dimension 
over Z+ ∪ {0}.   
 
Now having seen such examples we now proceed onto 
define other properties of these semivector spaces. 
 
 
All these are also semilinear algebras over the semifields.  
 
 
Now if the natural product is defined we can speak of 
complements of the semivector subspaces (semilinear algebras).   
 
 
We will illustrate this situation by some simple examples.


## Page 152


152
 
Example 4.64:  Let  
 
V = 
1
2
3
4
5
a
a
a
a
a

















 with ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 5} 
 
be a semivector space over the semifield S = Z+ ∪ {0}.   
 
Consider  
 
M1 = 
1
2
0
0
a
a
0

















 with ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 2} ⊆ V 
be a semivector subspace of V over S. 
 
     M2 = 
1
2
3
a
a
0
0
a

















 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 3} ⊆ V, 
be a semivector subspace of V over S.   Clearly every x ∈  
M1 and y ∈ M2 are such that x ×n y = (0). 
 
 
We see V = M1 ⊕ M2; M1 ∩ M2 = (0). 
 
Example 4.65:  Let V = {(a1, a2, …, a10) | ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 
10} be a semivector space over the semifield S = Z+ ∪ {0}.


## Page 153


153
 
Consider P1 = {(0, 0, 0, a1, 0, 0, 0, 0, 0, a7) | ai ∈ Z+ ∪ {0},  
1 ≤ i ≤ 7} ⊆ V be a semivector subspace of V over S.  
 
 
P2 = {(a1, a2, 0,0, …, 0) | a1, a2 ∈ Z+ ∪ {0}, 1 ≤ i ≤ 7} ⊆ V 
be a semivector subspace of V over S.  
 
P3 = {(0, 0, a1, 0, a2, a3, 0,0,0,0) | ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 3} ⊆ V 
be a semivector subspace of V over S.  
 
P4 = {(0, 0, 0, 0, 0, 0, a1, a2, a3, 0) | ai ∈ Z+∪ {0}, 1 ≤ i ≤ 3}⊆ V 
is again a semivector subspace of V over S. 
 
 
We see every vector in Pi is orthogonal with every other 
vector in P if i ≠ j; 1 ≤ i, j ≤ 4. 
 
 
Further V = P1 + P2 + P3 + P4 and Pi ∩ Pj = (0) if i ≠ j. 
 
Example 4.66:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 15} 
be a semivector space over the semifield S = Z+ ∪ {0}.   
 
Take  
 
P1 = 
1
2
3
4
5
6
0
0
0
a
a
a
0
0
0
a
a
a
0
0
0

















ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 6} ⊆ M, 
is a semivector subspace of M over S = Z+ ∪ {0}.


## Page 154


154
P2 = 
1
2
3
4
5
6
7
8
9
a
a
a
0
0
0
a
a
a
0
0
0
a
a
a

















ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 9} ⊆ M, 
is a semivector subspace of M over S = Z+ ∪ {0}. 
 
 
We see for every x ∈ P1 we have x ×n y = (0) for every y ∈ 
P2. 
 
 
Thus M = M1 + M2 and P1 ∩ P2 = (0). We say the space P1 
is orthogonal with the space P2 of M. 
 
 
However if  
 
P3 = 
1
2
3
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a

















ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 3} ⊆ M, 
we see P1 and P3 are such that for every x ∈ P1 we have x ×n y = 
(0) for every y ∈ P3; however we do not call P3 the 
complementary space of P1 as M ≠ P1 + P3.  
 
Example 4.67:  Let  
 
P = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 16} 
be a semivector space over the semifield Z+ ∪ {0} = S.


## Page 155


155
 
Consider  
 
M1 =  
1
2
3
4
a
a
0
0
a
a
0
0
0
0
0
0
0
0
0
0













ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 4} ⊆ P; 
M1 is a semivector subspace of P over S. 
 
M2 =  
1
2
3
4
0
0
a
a
0
0
a
a
0
0
0
0
0
0
0
0













ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 4} ⊆ P; 
M2 is a semivector subspace of P over S. 
 
Consider  
 
M3 =  
1
2
3
4
0
0
0
0
0
0
0
0
a
a
0
0
a
a
0
0













ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 4} ⊆ P; 
M3 is a semivector subspace of P over S. 
 
Now  
M4 =  
1
2
3
4
0
0
0
0
0
0
0
0
0
0
a
a
0
0
a
a













ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 4} ⊆ P 
is a semivector subspace of P over S. 
 
We see P = M1 + M2 + M3 + M4, Mi ∩ Mj = (0) if i ≠ j;  
1 ≤ i, j ≤ 4.


## Page 156


156
 
Example 4.68:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 15} 
be a semivector space over the semifield S = {0} ∪ Z+. 
 
 
So we can define as in case of other spaces complements in 
case of semivector space of polynomials with matrix 
coefficients also.  We will only illustrate this situation by some 
examples. 
 
Example 4.69:  Let  
 
V = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, x3, x4, x5, x6) | 
xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 6} 
 
be a semivector space over the semifield S = Z+ ∪ {0}. 
 
 
Consider  
 
M = 
i
i
i 0
a x
∞
=


∑
 ai = (0, 0, 0, x1, x2, x3)  
with xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V, 
 
M is a semivector subspace of V over S.


## Page 157


157
 
Take  
 
N = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, x3, 0,0,0,0) 
 
with xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V, 
 
N is a semivector subspace of V over S.  We see  M+N = V and 
infact M is the orthogonal complement of N and vice versa.  
That is M⊥ = N and N⊥ = M and M ∩ N = (0). 
 
Example 4.70: Let  
 
V = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
















; dj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 15} 
 
be a semivector space define over the semifield S = Z+ ∪ {0}. 
 
 
Now  
W1 = 
i
i
i 0
a x
∞
=


∑
 xi = 
1
2
3
4
5
6
7
8
9
x
x
x
0
0
0
x
x
x
0
0
0
x
x
x
















 
where  xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 9} ⊆ V 
 
is a semivector subspace of V over S.   
 
We see the complement of W;


## Page 158


158
1
W⊥= 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
0
0
0
y
y
y
0
0
0
y
y
y
0
0
0
















 
where  yj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 6} ⊆ V. 
 
We see 
1
W⊥ + W1 =  V and W1 ∩ 
1
W⊥ = (0). 
 
 
Suppose  
M1 = 
i
i
i 0
a x
∞
=


∑
 xi = 
1
2
3
0
0
0
0
0
0
0
0
0
x
x
x
0
0
0
















with  xj ∈ Z+ ∪ {0};  
 
1 ≤ j ≤ 3} ⊆ V 
 
be another semivector subspace of V; we see M1 is not the 
orthogonal complement of W1 but however W1 ∩ M1 = (0).  But 
W1 + M1 ⊆ V.  Hence we can have orthogonal semivector 
subspaces but they do not serve as the orthogonal complement 
of W1. 
 
Example 4.71:  Let  
 
V = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
9
d
d
d
d
d
d
d
d
d










; dj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 9} 
be a semivector space over the semifield S = Z+ ∪ {0}.


## Page 159


159
Consider  
 
P1 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
d
d
0
d
0
0
0
0
0










with dj ∈ Z+ ∪ {0};  
 
1 ≤ j ≤ 3} ⊆ V 
 
a semivector subspace of V over S.  We see the complement of  
 
P1 is P2 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
0
0
d
0
d
d
d
d
d










with dj ∈ Z+ ∪ {0};  
 
1 ≤ j ≤ 6} ⊆ V. 
 
 
We see P1 + P2 = V and P1 ∩ P2 = {0}.  We call P2 the 
orthogonal complement of P1 and vice versa. 
 
 
However if  
 
N = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
d
0
0
d
0
0
d










 
 
with dj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V; 
 
N is also a semivector subspace of V over S and N is orthogonal 
with P1 however N is not the orthogonal complement of P1 as P1 
+ N ≠ V only properly contained in V. 
 
 
Thus a given semivector subspace can have more than one 
orthogonal semivector subspace but only one orthogonal 
complement.


## Page 160


160
For  
 
T = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
d
0
d
d
0










 
 
with dj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V 
 
is such that T is a semivector subspace of V and T is also 
orthogonal with P1 but is not the orthogonal complement of P1 
as T + P1  ⊂ V.  Thus we see there is a difference between a 
semivector subspace orthogonal with a semivector subspace and 
an orthogonal complement of a semivector subspace. 
 
 
Now having seen examples of complement semivector 
subspace and orthogonal complement of a semivector subspace 
we now proceed onto give one or two examples of pseudo direct 
sum of semivector subspaces. 
 
Example 4.72:  Let  
 
V  = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, …, x8)  
 
where xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 8} 
 
be a semivector space over the semifield S = Z+ ∪ {0}.   
 
Take  
 
W1 = 
i
i
i 0
a x
∞
=


∑
 ai = (0, 0, x1, x2, x3, 0,0,0)  
 
where xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V 
 
be a semivector subspace of V over S.


## Page 161


161
 
 
Consider  
 
W2 =  
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, x3, 0,0,0,0,0) 
 
with xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V; 
 
another semivector subspace of V. 
 
 
Take  
 
W3 = 
i
i
i 0
a x
∞
=


∑
 ai = (0, 0, d1, 0, 0, d2, 0,0)  
 
with dj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 2} ⊆ V 
 
another semivector subspace of V over S. 
 
 
Finally let 
 
W4 = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, 0, 0, x2, 0,0, x3, x4) 
 
with xj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 4} ⊆ V, 
 
a semivector subspace of V over S.  We see V ⊆ W1 + W2 + W3 
+ W4 and Wi ∩ Wj ≠ (0) if i ≠ j.  Thus V is a pseudo direct sum 
of semivector subspace of V over the semifields.


## Page 162


162
Example 4.73:  Let  
V = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
x
x
x
x
x
x
x
x


























 where xj ∈ Q+ ∪ {0}; 1 ≤ j ≤ 8} 
be a semivector space over the semifield S = Q+ ∪ {0}. 
 
 
Take  
W1 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
x
x
x
0
0





















 where xj ∈ Q+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V 
be a semivector subspace of V over S. 
 
 
Consider  
W2 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
x
x
x
0
0
0


























 where xj ∈ Q+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V 
be a semivector subspace of V over S.


## Page 163


163
W3 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
x
x
x
0


























 where xj ∈ Q+ ∪ {0}; 1 ≤ j ≤ 3}⊆ V  
be a semivector subspace of V over S and  
 
W4 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
0
x
x
x


























 where xj ∈ Q+ ∪ {0}; 1 ≤ j ≤ 3} ⊆ V 
 
be a semivector subspace of V over S, the semifield.  
 
 
We see Wi ∩ Wj = (0); i ≠ j.  But V ⊆ W1 + W2 + W3 + W4; 
1 ≤ i, j ≤ 4.  Thus V is the pseudo direct sum of semivector 
subspaces of V over S. 
 
Example 4.74:  Let  
 
V = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d












  
 
where dj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 16}


## Page 164


164
 
be a semivector space over the semifield S = Z+ ∪ {0}. 
 
 
Take  
M1 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
d
d
d
0
0
0
0
0
0
0
0
0
0
0
0
0












  
 
where d1, d2, d3 ∈ Z+ ∪ {0}}⊆ V, 
 
M2 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
d
d
d
0
0
0
0
0
0
0
0
0
0
0












  
 
where d1, d2, d3 ∈ Z+ ∪ {0}} ⊆ V, 
 
M3 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
d
d
d
0
0
0
0
0
0
0
0
0












 
 
where d1, d2, d3 ∈ Z+ ∪ {0}}⊆ V, 
 
 
M4 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
0
0
d
d
d
0
0
0
0
0
0
0












  
 
where d1, d2, d3 ∈ Z+ ∪ {0}}⊆ V,


## Page 165


165
M5 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
0
0
0
0
d
d
d
0
0
0
0
0












 
 
where d1, d2, d3 ∈ Z+ ∪ {0}}⊆ V, 
 
 
 
M6 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
0
0
0
0
0
d
d
d
0
0
0
0












 
 
where d1, d2, d3 ∈ Z+ ∪ {0}} ⊆ V, 
 
M7 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
0
0
0
0
0
0
0
d
d
d
0
0












 
 
where d1, d2, d3 ∈ Z+ ∪ {0}} ⊆ V, 
 
and  
M8 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
0
0
0
0
0
0
0
0
0
0
0
0
0
d
d
d












 
where d1, d2, d3 ∈ Z+ ∪ {0}} ⊆ V 
 
be semivector subspaces of V over the semifield S. 
 
 
Clearly V ⊆ M1 + M2 + … + M8, Mi ∩ Mj ≠ (0) if i ≠ j,  
1 ≤ j, i ≤ 8.


## Page 166


166
 
 
Example 4.75:  Let  
 
V = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d












 
 
where dj ∈ Z+ ∪ {0}; 1 ≤ j ≤ 24} 
be a semivector space over the semifield S = Z+ ∪ {0}. 
 
 
Consider  
P1 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
d
d
d
d
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0












 
 
where d1 , d2, d3, d4 ∈ Z+ ∪ {0}} ⊆ V, 
 
P2 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
0
0
0
d
d
d
d
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0












 
 
with d1 , d2, d3, d4 ∈ Z+ ∪ {0}} ⊆ V, 
 
P3 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
0
0
0
0
0
0
d
d
d
d
0
0
0
0
0
0
0
0
0
0
0
0
0
0












 
 
with d1 , d2, d3, d4 ∈ Z+ ∪ {0}} ⊆ V,


## Page 167


167
P4 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
0
0
0
0
0
0
0
0
0
d
d
d
d
0
0
0
0
0
0
0
0
0
0
0












 
 
with d1 , d2, d3, d4 ∈ Z+ ∪ {0}} ⊆ V, 
 
 
P5 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
0
0
0
0
0
0
0
0
0
0
0
0
d
d
d
d
0
0
0
0
0
0
0
0












 
 
with d1 , d2, d3, d4 ∈ Z+ ∪ {0}} ⊆ V, 
 
P6 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
d
d
d
d
0
0
0
0
0












; 
 
d1 , d2, d3, d4 ∈ Z+ ∪ {0}} ⊆ V, 
 
P7 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
d
d
d
d
0
0












 
 
with d1 , d2, d3, d4 ∈ Z+ ∪ {0}} ⊆ V 
 
and


## Page 168


168
P8 = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
d
d
d
d
d












 
 
with d1 , d2, d3, d4, d5 ∈ Z+ ∪ {0}} ⊆ V 
 
be semivector subspaces of V over S = Z+ ∪ {0}.  We see V ⊆ 
P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8; and Pi ∩ Pj ≠ {0} if i ≠ j, 1 
≤ i, j ≤ 8.  Thus V is only a pseudo direct sum of semivector 
subspaces.


## Page 169


169
 
 
 
 
 
Chapter Five 
 
 
 
 
NATURAL PRODUCT ON SUPERMATRICES 
 
 
 
 
In this chapter we define the new notion of natural product 
in supermatrices.  Products in supermatrices are very different 
from usual product on matrices and product on super matrices. 
 
 
Throughout this chapter  
 
S
R
F  = {(a1 a2 a3 | a4 a5 | … | an-1  an) | ai ∈ Q or R or Z} that is 
collection of 1 × n super row matrices with same type of 
partition in it. 
  
S
C
F  = 
1
2
3
4
5
m
a
a
a
a
a
a
























 ai ∈ Z or Q or R; 1 ≤ i ≤ m}


## Page 170


170
denotes the collection of all m × 1 super column matrices with 
same type of partition on it.  
 
S
m n
F ×  (m≠n) = 
11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a



















 aij ∈ Q or R or Z; 
 
1 ≤ i ≤ m; 1 ≤ j ≤ n} 
 
denotes the collection of all m × n super matrices with same 
type of partition on it. 
 
S
n n
F ×  = 
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a



















 aij ∈ Q or Z or R; 
 
1 ≤ i, j ≤ n} 
 
denotes the collection of n × n super matrices with same type of 
partition on it. 
 
 
We will first illustrate this situation before we proceed onto 
give any form of algebraic structure on them. 
 
Example 5.1:  Let  
 
M = {(x1 x2 | x3 | x4 x5) where xi ∈ Z  or  Q or R; 1 ≤ i ≤ 5} 
 
be the collection of 1 × 5 row super matrices with same type of 
partition on it M = 
S
R
F .


## Page 171


171
Example 5.2:  Let  
 
S
R
F  = {(x1 | x2  x3 | x4 x5 x6 | x7 x8 x9 x10 | x11 x12) | xi ∈ R; 
1 ≤ i ≤ 10} 
 
be again a collection of 1 × 10 super row matrices with same 
type of partition on it.  
 
Example 5.3:  Let  
 
P = {(x1 x2 | x3 x4 x5) where xi ∈ Q or R or Z; 1 ≤ i ≤ 5} 
 
be again a collection of 1 × 5 super row super matrices of same 
type.   
 
Now we will see examples of column super matrices of 
same type. 
 
Example 5.4:  Let  
 
S
C
F  = 
1
2
3
4
5
6
7
x
x
x
x
x
x
x























 xi ∈ R; 1 ≤ i ≤ 7} 
 
be the 7 × 1 column super matrices of same type.


## Page 172


172
Example 5.5:  Let  
S
C
F  = 
1
2
3
4
5
6
7
8
9
x
x
x
x
x
x
x
x
x





























 xi ∈ R; 1 ≤ i ≤ 9} 
 
be the 9 × 1 column super matrix of same type. 
 
Example 5.6:  Let  
S
C
F  = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a



























 ai ∈ Q; 1 ≤ i ≤ 8} 
 
be the 8 × 1 column super matrix of same type.   
 
Now we proceed onto give examples of 
S
m n
F ×  (m ≠ n).


## Page 173


173
Example 5.7:  Let  
 
S
3 5
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











 ai ∈ Q; 1 ≤ i ≤ 15} 
be the 3 × 5 super matrix of same type.   
 
Example 5.8:  Let  
 
S
7 4
F ×  = 
1
2
3
4
5
6
7
8
25
26
27
28
a
a
a
a
a
a
a
a
a
a
a
a



















 ai ∈ Z; 1 ≤ i ≤ 28} 
 
be a 7 × 4 super matrix of same type.   
 
 
 
Example 5.9:  Let  
 
S
6 7
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
31
32
33
34
35
36
37
38
39
40
41
42
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a























 ai ∈ Q; 1 ≤ i ≤ 42} 
 
be a 6 × 7 super matrix of same type.   
 
 
Now we proceed onto give examples of 
S
n n
F ×  square super 
matrices of same type.


## Page 174


174
Example 5.10:  Let  
 
S
4 4
F ×  = M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ Q; 1 ≤ i ≤ 16} 
 
be a square super matrix of same type. 
 
Example 5.11:  Let  
 
S
4 4
F ×  =  
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ Q; 1 ≤ i ≤ 16} 
 
be a square super matrix of same type. 
 
Example 5.12:  Let  
 
S
4 4
F ×  =  
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ Q; 1 ≤ i ≤ 16} 
 
be a square super matrix of same type. 
 
Example 5.13:  Let  
 
S
3 3
F ×  = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











 ai ∈ Z; 1 ≤ i ≤ 9} 
be a square super matrix of same order.


## Page 175


175
 
 
Now we can define 
S
S
S
C
R
m n
F ,F ,F ×  (m ≠ n) and 
S
n n
F ×  the usual 
matrix addition and natural product ×n. 
 
 
Under usual matrix addition 
S
S
S
C
R
m n
F ,F ,F ×  (m ≠ n) and 
S
n n
F ×  
are abelian (commutative) groups. 
 
 
How under natural product 
S
S
S
C
R
m n
F ,F ,F ×  (m ≠ n) and 
S
n n
F ×  are 
semigroups with unit. 
 
 
Suppose  
 
x = (x1 x2  x3 | x4 x5 | x6 x7) and y = (y1 y2  y3 | y4 y5 | y6 y7) 
be two super row matrices of same type  
 
x + y = (x1 + y1, x2 + y2, x3 + y3 | x4 + y4, x5 + y5 | x6  
       + y6 x7 + y7).  Thus 
S
R
F  is closed under ‘+’. 
 
 
Likewise if x = 
1
2
3
4
5
6
7
8
x
x
x
x
x
x
x
x


























 and y = 
1
2
3
4
5
6
7
8
y
y
y
y
y
y
y
y


























  are two super column


## Page 176


176
matrices of same type then x + y = 
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
x
y
x
y
x
y
x
y
x
y
x
y
x
y
x
y
+




+




+


+




+


+




+


+




.   
 
 
We see 
S
C
F  is closed under ‘+’ and infact a group under ‘+’. 
 
 
 
Consider x = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
















 and  
 
 
y =
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
















 
 
be two 5 × 7 super matrices in 
S
5 7
F × .


## Page 177


177
 
Now x + y =  
 
1
1
2
9
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
11
11
12
12
13
13
14
14
15
15
16
16
17
17
18
18
19
19
20
20
21
17
22
22
23
23
24
24
25
25
26
26
27
27
28
28
29
29
30
30
31
31
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+
32
32
33
33
34
34
35
35
b
a
b
a
b
a
b














+
+
+
+


 
 is in 
S
5 7
F × . 
 
 
Thus addition can be performed on 
S
m n
F ×  (m ≠ n) and infact 
S
m n
F ×  is a group under addition.   
 
Now we give examples of addition of square super matrices 
S
n n
F × . 
 
Let x = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
















 
 
and y = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b


















## Page 178


178
x+y = 
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
11
11
12
12
13
13
14
14
15
15
16
16
17
17
18
18
19
19
20
20
21
21
22
22
23
23
24
24
25
25
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
a
b
+
+
+
+
+




+
+
+
+
+




+
+
+
+
+


+
+
+
+
+




+
+
+
+
+


  
∈ 
S
5 5
F × . 
 
 
Infact 
S
5 5
F ×  is a group under addition.  
 
 
Now we proceed onto define natural product ×n on 
S
S
S
C
R
n m
F ,F ,F ×  (n ≠ m) and 
S
n n
F × . 
 
 
Consider x = (a1 a2 a3 | a4 a5 | a6 a7 a8 a9) and y = (b1 b2 b3 | b4 
b5 | b6 b7 b8 b9) ∈ 
S
R
F . 
 
 
x ×n y = (a1b1 a2b2 a3b3 | a4b4 a5b5 | a6b6 a7b7 a8b8 a9b9) ∈
S
R
F .  
S
R
F  under product is a semigroup infact 
S
R
F  has zero divisors 
under natural product ×n. 
 
 
Suppose x = (0 0 0 | 2 1 0 | 92 | 3) and y = (3 9 0 | 0 0 7 | 0 0 
| 0) be in 
S
R
F .  x ×n y = (0 0 0| 0 0 0 | 0 0 | 0).  Thus we see 
S
R
F  
has zero divisors.  
Consider x = 
2
0
3
1
2
0
0
0
4
5
















 and y = 
0
1
0
0
0
1
2
3
0
0
















 in 
S
C
F ;


## Page 179


179
 
we see under the natural product x ×n y =
0
0
0
0
0
0
0
0
0
0
















. 
 
 
 
Take 
S
3 5
F × , 
S
3 5
F ×  under natural product, they have zero 
divisors.  Infact 
S
3 5
F ×  under natural product ×n is a semigroup. 
 
Consider x = 
9
0
2
0
1
0
1
0
5
0
1
0
0
2
0










 and 
 
y = 
0
7
0
8
0
9
0
2
0
7
0
7
9
0
2










 in 
S
3 5
F × ; 
 
we see x ×n y =
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0










. 
 
 
Now 
S
n n
F × also has zero divisors.


## Page 180


180
Consider x = 
7
8
0
9
4
2
0
1
2
5
7
8
1
2
3
0
1
0
5
7
0
9
2
0
1
2
3
0
2
3
0
8
7
0
5
4




















 and 
 
      y = 
0
0
9
0
0
0
7
0
0
0
0
0
0
0
0
6
0
8
0
0
6
0
0
2
0
0
0
6
0
0
5
0
0
7
0
0




















 ∈ 
S
6 6
F × . 
 
x ×n y    =  
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0




















 ∈ 
S
6 6
F × . 
 
 
Thus 
S
n n
F ×  is a semigroup under ×n and has zero divisors and 
ideals.  We will now give the following theorems the proofs of 
which are simple. 
 
THEOREM 5.1:   
 
S
R
F  = {(x1 x2 | … | xn) | xi ∈ Q or R; 1 ≤ i ≤ n} 
 
is  a group under ‘+’.


## Page 181


181
THEOREM 5.2:   
 
S
C
F  = 
−

























1
2
3
m 1
m
x
x
x
x
x
 | xi ∈ Q or R or C or Z; 1 ≤ i ≤ m} 
is the group under ‘+’. 
 
THEOREM 5.3 :   
 
×
S
3 3
F
 (m ≠ n) = 


















11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a
| aij ∈ Q or R or C or Z; 
 
1 ≤ i ≤ m; 1 ≤ j ≤ n} 
 
is a group under ‘+’. 
 
THEOREM 5.4:  (
×
S
n n
F
, +) is a group. 
 
THEOREM 5.5:  (
S
R
F , ×n) is a semigroup and has zero divisors, 
ideals and subsemigroups which are not ideals.  
 
THEOREM 5.6:  (
S
C
F , ×n) is a semigroup with unit and has zero 
divisors, units, ideals, and subsemigroups. 
 
THEOREM 5.7:  (
×
S
m n
F
(m ≠ n), ×n) is a semigroup with zero 
divisors and units.


## Page 182


182
THEOREM 5.8:  (
×
S
n n
F
, ×n) is a commutative semigroup and has 
zero divisors units and ideals. 
 
 
We will now give examples of zero divisors units and ideals 
of 
S
m n
F × (m ≠ n), 
S
S
S
C
R
n m
F ,F ,F ×  (n ≠ m) and 
S
n n
F × . 
 
Example 5.14:  Let  
 
S
R
F = {(x1 | x2 x3 | x4) where xi ∈ Z; 1 ≤ i ≤ 4} 
 
be a commutative semigroup under natural product.  (1 | 1 1 | 1) 
is the unit of 
S
R
F  under ×n. 
 
 
P = {(x1 | x2 x3 | x4) | xi ∈ 3Z; 1 ≤ i ≤ 4} ⊆ 
S
R
F  is an ideal of 
S
R
F . 
 
 
Infact 
S
R
F  has infinite number of ideals under the natural 
product ×n.  Further 
S
R
F  has zero divisors. 
 
 
Consider x = (x1 | 0 0 | x2) ∈ 
S
R
F , y = (0 | y1 y2 | 0) in 
S
R
F  is 
such that x ×n y = (0 | 0 0 | 0).  Also P = (x1 | 0 0 | x2) | xi ∈ Z, 1 
≤ i ≤ 2} ⊆ 
S
R
F  is also an ideal. 
 
Example 5.15:  Let  
S
R
F  = {(x1 | x2 x3 | x4 x5 x6) where xi ∈ Q; 1 ≤ i ≤ 6} 
be a semigroup under ×n.   
 
S = {(a1 | a2 a3 | a4 a5 a6) | ai ∈ Z, 1 ≤ i ≤ 6} ⊆ 
S
R
F ; S is a 
subsemigroup of 
S
R
F  under ×n.  Clearly S is not an ideal of 
S
R
F . 
 
 
Consider P = {(a1 | a2 a3 | 0 0 0) | ai ∈ Q, 1 ≤ i ≤ 3} ⊆ 
S
R
F , is 
an ideal of 
S
R
F .  If Q in P is replaced by Z that is


## Page 183


183
T = {(a1 | a2 a3 | 0 0 0) | ai ∈ Z, 1 ≤ i ≤ 3} ⊆ 
S
R
F , then T is 
only a subsemigroup of 
S
R
F  and is not an ideal of 
S
R
F .  Thus 
S
R
F  
has subsemigroups which are not ideals. 
 
 
Take    M = {(a | b c | 0 0 0) | a, b, c ∈ Q} ⊆ 
S
R
F  and  
N = {(0 | 0 0 | a b c) | a, b, c ∈ Q} ⊆ 
S
R
F .   
 
M ×n N = (0 | 0 0 | 0 0 0) or M ∩ N = (0 | 0 0 | 0 0 0). 
 
 
S
R
F  = M + N. 
 
 
Suppose M1 = {(a | b 0 | 0 0 0) | a, b ∈ Q} ⊆ 
S
R
F  and  
 
N1 = {(0 | 0 0 | a b 0) | a, b ∈ Q} ⊆ 
S
R
F , we see 
 
M1 ×n N1 = {(0 | 0 0 | 0 0 0)|.  Also M1 ∩ N1 = {(0 | 0 0 | 0 0 
0)} but N1 + M1 
≠⊂ 
S
R
F ; and N1 + M1 ≠ 
S
R
F .  We see that some 
special properties are enjoyed by M and N that are not true in 
case M1 and N1. 
 
 
Now we give an example in case of (
S
C
F , ×n). 
 
Example 5.16:  Let  
 
S
C
F  = 
1
2
3
4
5
6
7
a
a
a
a
a
a
a























 ai ∈ Q, 1 ≤ i ≤ 7} 
be a semigroup under natural product ×n.


## Page 184


184
 
 
Consider  
P = 
1
2
3
4
a
a
a
a
0
0
0























 ai ∈ Q, 1 ≤ i ≤ 4} ⊆
S
C
F  
 
is a subsemigroup of 
S
C
F  and is not an ideal of 
S
C
F . 
 
 
Take  
M = 
1
2
3
0
0
0
0
a
a
a























 ai ∈ Z, 1 ≤ i ≤ 3} ⊆ 
S
C
F , 
M is a subsemigroup of 
S
C
F . 
 
 
Clearly if x ∈ P and y ∈ M then  
 
x ×n y = 
0
0
0
0
0
0
0





































.


## Page 185


185
Now take  
S = 
1
2
3
4
5
6
7
a
a
a
a
a
a
a























 ai ∈ Z, 1 ≤ i ≤ 7} ⊆ 
S
C
F , 
 
S is a subsemigroup of 
S
C
F  but is not an ideal of 
S
C
F . 
 
 
Suppose  
 
J =  
1
2
3
4
a
0
0
0
a
a
a























 ai ∈ Q, 1 ≤ i ≤ 4} ⊆ 
S
C
F , 
 
J is a subsemigroup as well as an ideal of 
S
C
F .   
 
Now we give yet another example.


## Page 186


186
Example 5.17:  Let  
 
S
C
F  = 
1
2
3
4
5
6
7
a
a
a
a
a
a
a























 ai ∈ Q, 1 ≤ i ≤ 7} 
be a semigroup under natural product ×n. 
 
 
Take  
P = 
1
2
3
0
a
0
a
0
a
0























 ai ∈ Q, 1 ≤ i ≤ 3} ⊆ 
S
C
F  
is a subsemigroup as well as an ideal of 
S
C
F . 
 
 
Take  
M = 
1
2
3
0
a
0
a
0
a
0























 ai ∈ 3Z, 1 ≤ i ≤ 3} ⊆ 
S
C
F  
is a subsemigroup of 
S
C
F  and is not an ideal of 
S
C
F .  M ⊆ P;  
M is a subsemigroup of P also.


## Page 187


187
 
Now take  
T = 
1
2
3
4
a
0
a
0
a
0
a























 ai ∈ Q, 1 ≤ i ≤ 4} ⊆ 
S
C
F , 
T is a subsemigroup of 
S
C
F  also an ideal of 
S
C
F .  We see for 
every x ∈ P and for every y ∈ T, x ×n y = (0). 
 
 
Now we give examples of zero divisors and ideals in 
S
n m
F ×  
(n ≠ m). 
 
Example 5.18:  Let  
 
S
5 3
F ×  =  
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











 ai ∈ Q, 1 ≤ i ≤ 15} 
 
be a semigroup of 5 × 3 super matrices under natural 
multiplication. 
 
If x = 
1
2
3
4
5
9
8
7
6
5
0
1
2
7
1










 and y = 
0
1
2
3
5
9
0
1
3
4
7
2
3
1
2










 
 
 
are in 
S
5 3
F × ;


## Page 188


188
then x ×n y = 
0
2
6
12
25
81
0
7
18
20
0
2
6
7
2










. 
 
 
Now consider P = 
a
b
c
d
e
0
0
0
0
0
0
0
0
0
0











 a, b, c, d, e ∈ Q} ⊆ 
S
5 3
F × ; P is an ideal of 
S
5 3
F × . 
 
We see for a = 
0
0
0
0
0
x
y
a
b
z
0
0
c
d
m










 ∈
S
5 3
F ×  is such that 
 
a ×n x = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0










 for every x ∈ P. 
 
Take  
 
M = 
0
0
e
f
0
a
b
0
0
g
c
d
0
0
h











 a, b, c, d, e, f, g, h ∈ Z} ⊆ 
S
5 3
F × ;  
 
clearly M is only a subring of 
S
5 3
F × ; and is not an ideal of 
S
5 3
F × . 
 
 
Further if  
 
y = 
a
b
0
0
p
0
0
e
f
0
0
0
g
h
0










 ∈ 
S
5 3
F × .  We see y ×n m = (0) 
 
for every m ∈ M.


## Page 189


189
 
Example 5.19:  Let  
 
 
S
7 3
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a























 ai ∈ Q, 1 ≤ i ≤ 21} 
 
be a 7 × 3 super matrix semigroup under natural product.   
 
 
Consider  
 
 
P = 
1
2
3
4
5
6
0
0
0
0
0
0
a
a
a
0
0
0
0
0
0
0
0
0
a
a
a























 ai ∈ Z, 1 ≤ i ≤ 6} ⊆ 
S
7 3
F × ; 
 
P is a subsemigroup under natural product, how ever P is not an 
ideal of 
S
7 3
F × .


## Page 190


190
 
Now take  
 
x = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
0
0
0
a
a
a
a
a
a
a
a
a
0
0
0






















 ∈ 
S
7 3
F × . 
 
Clearly x ×n p = (0) for every p ∈ P. 
 
 
Thus we have a collection of zero divisors in the semigroup 
under natural product.   
 
Now consider the set  
 
 
T = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
0
0
0
a
a
a
a
a
a
0
0
0
0
0
0
a
a
a























 ai ∈ Q, 1 ≤ i ≤ 12} ⊆ 
S
7 3
F × ; 
 
 
T is an ideal of 
S
7 3
F × .


## Page 191


191
 
Further  
m = 
1
2
3
4
5
6
7
8
9
0
0
0
a
a
a
0
0
0
0
0
0
a
a
a
a
a
a
0
0
0






















 ∈ 
S
7 3
F ×  
is such that m ×n t = (0) for every t ∈ T.  Thus 
S
7 3
F × has several 
zero divisors and has ideals. 
 
Example 5.20:  Let  
 
S
3 7
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











 
ai ∈ Q, 1 ≤ i ≤ 21} 
 
be 3 × 7 matrix semigroup under natural product. 
 
 
Take  
 
P = 
1
4
7
2
5
8
3
6
9
0
a
0
a
0
a
0
0
a
0
a
0
a
0
0
a
0
a
0
a
0











 ai ∈ Q, 1 ≤ i ≤ 9} ⊆ 
S
3 7
F × ; 
 
P is an ideal of 
S
3 7
F × .   
 
x = 
1
4
7
10
2
5
8
11
3
6
9
12
a
0
a
0
a
0
a
a
0
a
0
a
0
a
a
0
a
0
a
0
a










 ∈ 
S
3 7
F ×  
is such that x ×n p = (0) for every p in P.


## Page 192


192
 
 
Thus 
S
3 7
F ×  has several zero divisors.  
 
 
Take  
 
Y = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











 ai ∈ Q, 1 ≤ i ≤ 21} 
⊆
S
3 7
F × , Y is only a subsemigroup and not an ideal of 
S
3 7
F × . 
 
Example 5.21:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a















 ai ∈ Q, 1 ≤ i ≤ 16} 
 
be a semigroup under natural product ×n. 
 
 
Consider  
 
P = 
1
2
3
5
4
6
7
8
0
a
a
0
a
0
0
a
a
0
0
a
0
a
a
0















 ai ∈ Z, 1 ≤ i ≤ 8} ⊆ 
S
4 4
F ×  = M; 
P is a subsemigroup under ×n. However P is not an ideal of 
S
4 4
F × .


## Page 193


193
 
Let  
 
X = 
1
2
5
6
7
8
3
4
a
0
0
a
0
a
a
0
0
a
a
0
a
0
0
a















 ai ∈ Q, 1 ≤ i ≤ 8} ⊆
S
4 4
F × ; 
 
X is an ideal of 
S
4 4
F × .  Further every x ∈ P and m ∈ X.  x ×n m = 
(0).  Thus 
S
4 4
F ×  has zero divisors and subsemigroups which are 
not ideals. 
 
 
Now consider another example. 
 
Example 5.22:  Let  
 
S
3 3
F ×  = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











 ai ∈ Z, 1 ≤ i ≤ 9} 
 
be a 3 × 3 super matrix semigroup under natural product.  It is 
important to observe 
S
3 3
F ×  is not compatible with usual matrix 
product.  Also no type of product on square super matrices can 
be defined on elements in 
S
3 3
F × .   
 
Take  
X =  
1
2
3
0
0
0
a
a
a
0
0
0











 ai ∈ Z, 1 ≤ i ≤ 3} ⊆ 
S
3 3
F × , 
X is a subsemigroup as well as an ideal of 
S
3 3
F × .


## Page 194


194
Take  
 
M = 
1
2
3
4
5
6
a
a
a
0
0
0
a
a
a











 ai ∈ Z, 1 ≤ i ≤ 6} ⊆ 
S
3 3
F × . 
 
M is a subsemigroup as well as an ideal of 
S
3 3
F × .  We see for 
every x ∈ X and m ∈ M,  x ×n m = (0).  
 
 
Now we describe the unit element of 
S
S
S
C
R
m n
F ,F ,F ×  (m ≠ n) 
and 
S
n n
F × . 
 
 
 
 
In 
S
C
F , 
1
1
1
1
1
1












 acts as the supercolumn unit under the natural 
product ×n. 
 
 
For 
S
R
F ; (1 1 | 1 1 1 | 1 … | 1 1) acts as the super row unit 
element under the natural product ×n.


## Page 195


195
 
For 
S
7 3
F × ; 
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1






















 acts as the super 7 × 3 unit under the 
natural product ×n. 
 
 
For 
S
4 4
F × , 
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1














 acts as the 4 × 3 super unit under 
product. 
 
 
Take x  = (1 | 1 1 | 1 1 1 | 1 1) (7 | 3 2 | 5 7 -1) | 2 0)  
= (7 | 3 2 | 5 7 -1 | 2 0). 
 
 
 
Likewise for x = 
3
2
1
0
3
1
7
0
2








−




















, 
1
1
1
1
1
1
1
1
1














 act as the multiplicative super


## Page 196


196
8 × 1 identity for, 
3
2
1
0
3
1
7
0
2








−




















 ×n 
1
1
1
1
1
1
1
1
1














 = 
3
2
1
0
3
1
7
0
2








−




















. 
 
For x = 
3
7
2
5
1
0
1
7
0
8
0
1
2
3
4
5
6
7
8
9
0
3
4
0
1
0
7
0
1
1
4
0
2
1
0
2
0
4
0
0
−














 
 
 
I = 
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1














 
 
acts as the super identity under ×n. For x ×n I = I ×n x = x. 
 
 
Consider  
 
I = 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
















 and y = 
0
2
3
0
1
1
0
0
4
0
1
2
6
1
3
0
0
5
0
7
1
4
1
2
0








−
−
−






−
−
−


 
 
are such that I ×n y = y ×n I = y.


## Page 197


197
 
 
Now having seen how the units look like we now proceed 
onto see how inverse of an element look under natural product 
×n. 
 
 
Let  
x = 
7
3
1
1
2
9
8
5
1
4
7
2
−












, 
 
if x takes its entries either from Q or from R and if no entry in x 
is zero then alone inverse exists otherwise inverse of x does not 
exist. 
 
Take y = 
1/7
1/3
1
1
1/ 2
1/9
1/8
1/5
1
1/ 4
1/7
1/ 2
−












 then we see 
 
x ×n y = 
1 1 1
1 1 1
1 1 1
1 1 1












. 
 
Let  
 
x = 
0
0
1
3
4
5
8
9
1
1
0
1












 
 
clearly for this x we do not have a y such that


## Page 198


198
x ×n y = 
1 1 1
1 1 1
1 1 1
1 1 1












. 
 
 
Consider x = (1/8 | 7 5 | 3 2 4 –1) then the inverse for x is y 
= (8 | 1/7 1/5 | 1/3 1/2 1/4 –1) we x ×n y = (1 | 1 1 | 1 1 1 1). 
 
Consider  
 
x = 
8
1
3
5
1 1/7
8
4
1
1
3
2








−


−




−


−




 then y = 
1/8
1
1/3
1/5
1
7
1/8
1/ 4
1
1
1/3
1/ 2








−


−




−


−




 
 
is such that  
x ×n y = 
1 1
1 1
1 1
1 1
1 1
1 1




















. 
 
 
Now having seen inverse and unit we just give the statement 
of a theorem, the proof is left as an exercise to the reader.  
 
THEOREM 5.9:  Let 
S
C
F  (or 
S
R
F  or 
×
S
m n
F
 (m ≠ n) or 
×
S
n n
F
) be the 
super matrix semigroup under natural product.  No super 
matrix other than those super matrices with entries from {1, –1} 
have inverse if 
S
C
F  (or 
S
R
F  or 
×
S
m n
F
 (m ≠ n) or 
×
S
n n
F
)take its 
entries from Z.


## Page 199


199
 
 
 
 
THEOREM 5.10:  Let 
S
C
F  (or 
S
R
F  or 
×
S
m n
F
 (m ≠ n) or 
×
S
n n
F
) be 
the super matrix semigroup under natural product, with entries 
from Q or R.  Every super matrix M in which no element of M 
takes 0 has inverse. 
 
 
The proof of this theorem is also left as an exercise to the 
reader. 
 
 
Consider x = (1 –1 | 1 1 –1 | –1 –1) ∈ 
S
R
F  = {(a1 a2 | a3 a4 a5 | 
a6 a7) | ai ∈ Z, 1 ≤ i ≤ 7}; clearly x = (1 –1 | 1 1 –1 | –1 –1) acts 
as its inverse that is x ×n x = (1 1 | 1 1 1 | 1 1). 
 
 
Consider  
 
y = 
1
1
1
1
1
1
1
1
1
−








−






−






−






−


 ∈ 
S
C
F  = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a





























 where ai ∈ Z; 1 ≤ i ≤ 9}.


## Page 200


200
Now  
y2 = 
1
1
1
1
1
1
1
1
1














; 
 
all y whose entries are from Z \ {1, -1} does not have inverse 
under natural product.  
 
Take  
y = 
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
−
−




−
−




−
−
−


−




−
−
−


 
 
we see y2 = 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
















. 
 
 
Consider x = 
0
1
2
3
0
3
4
1
2




−






 we see x-1 does not exist. 
 
 
Take x = (1 0 | 5 7 2 | 1 5 7 –1 2), x-1 does not exist.


## Page 201


201
Consider y = 
1
0
2
3
5
7
0
2
1
4
−














−


















; 
 
clearly y-1 does not exist. 
 
Consider  
x = 7
1
0
2
3
4
0
3
1
0
0
2
1
0
7
0
1
0
5
1
−
−






. 
 
Clearly x-1 does not exist.   
 
Now we have seen inverse of a super matrix under natural 
product and the condition under which the inverse exists.  
 
 
Now we proceed onto discuss the operation ‘+’ on 
S
C
F  or 
S
R
F  
or 
S
m n
F ×  (m ≠ n) or 
S
n n
F × , which is stated as the following 
theorems. 
 
THEOREM 5.11: (
S
C
F , +) is an additive abelian group of super 
column matrices. 
 
THEOREM 5.12: (
S
R
F , +) is an additive abelian group of super 
row matrices.  
 
THEOREM 5.13: (
×
S
m n
F
 (m ≠ n), +) is an additive abelian group 
of super m × n (m ≠ n) matrices.


## Page 202


202
 
THEOREM 5.14: (
×
S
n n
F
, +) is an additive abelian group of super 
square matrices.   
 
We can define subgroups.  All subgroups are normal as 
these groups are abelian.  We will just give some examples.  
 
Example 5.23:  Let   
S
R
F = {(a1 a2 a3 a4 | a5 a6 | a7 a8 | a9) | ai ∈ Q; 1 ≤ i ≤ 9} 
be an abelian group of super row matrices under addition. 
 
Example 5.24:  Let  
 
S
2 3
F ×  = 
1
2
3
4
5
6
a
a
a
a
a
a










 where ai ∈ Q; 1 ≤ i ≤ 6} 
be an additive abelian group of 2 × 3 super matrices. 
 
Example 5.25:  Let  
 
S
C
F  = 
1
2
3
4
5
6
7
8
9
10
11
a
a
a
a
a
a
a
a
a
a
a













































 ai ∈ Q, 1 ≤ i ≤ 11} 
be an abelian group of column super matrices.


## Page 203


203
Example 5.26:  Let  
 
S
4 4
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ R, 1 ≤ i ≤ 16} 
be an additive abelian group of 4 × 4 super matrices.   
 
Now we can define {
S
R
F , +, ×n} as the ring of super row 
matrices, (
S
C
F , +, ×n) as the ring of super column matrices, 
{
S
m n
F ×  (m ≠ n), ×n, +} is the ring of super m × n matrices and 
{
S
n n
F × , ×n, +} be the ring of super n × n matrices.   
 
We describe properties associated with them. 
 
Example 5.27:  Let  
S
C
F  = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a



























 ai ∈ Q, 1 ≤ i ≤ 8} 
 
be the 8 × 1 super column matrix ring under ‘+’ and ‘×n’. 
 
Example 5.28:  Let  
 
S
R
F  = {(a1 | a2 a3 | a4 a5) where ai ∈ Q, 1 ≤ i ≤ 5, +, ×n} 
 
be the ring of super row matrices.


## Page 204


204
Example 5.29:  Let  
 
S
3 4
F ×  = 
1
4
7
10
2
5
8
11
3
6
9
12
a
a
a
a
a
a
a
a
a
a
a
a











 ai ∈ Q, 1 ≤ i ≤ 12, +, ×n} 
 
be the ring of 3 × 4 supermatrices. 
 
Example 5.30:  Let  
 
S
3 4
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ Z, 1 ≤ i ≤ 4} 
 
be the ring of  square supermatrices. 
 
Example 5.31:  Let  
 
S
9 3
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a































 ai ∈ Q, 1 ≤ i ≤ 27, +, ×n} 
 
be a ring of column supervectors.


## Page 205


205
Example 5.32:  Let  
 
S
3 10
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











 
 
ai ∈ Q, 1 ≤ i ≤ 30, +, ×n} 
 
be a ring of super row vectors.   
 
All these rings are commutative have zero divisor and have 
unit.  However we will give examples of ring of super matrices 
which have no unit. 
 
Example 5.33:  Let  
 
S
R
F  = {(x1 | x2 x3 x4 | x5 x6 | x7 x8 x9 x10) | xi ∈ 3Z ; 
1 ≤ i ≤ 10, +, ×n} 
 
be the ring of super row matrices.  Clearly 
S
R
F  does not contain 
the unit (1 | 1 1 1 | 1 1 | 1 1 1 1). 
 
Example 5.34:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
a
a
a
a
a
a
a
a
a
a

































 ai ∈ 7Z, 1 ≤ i ≤ 10, +, ×n}


## Page 206


206
 
be the ring of super column matrices.  Clearly this ring has no 
super identity. 
 
Example 5.35: Let  
 
S
3 4
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ 10Z; 1 ≤ i ≤ 16, +, ×n} 
 
be a ring of 4 × 4 super matrices.   
 
Clearly the super unit 
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1












 ∉ M. 
 
Example 5.36: Let 
S
3 4
F ×  =  
 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x











 
 
 xi ∈ 5Z; 1 ≤ i ≤ 36, +, ×} 
 
be a ring of super row vector.  Clearly P does not contain the 
super identity  
 
I = 
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1










.


## Page 207


207
Example 5.37: Let  
 
V =
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a



























aj ∈ 15Z; 1 ≤ j ≤ 32} 
 
be a ring of super column vectors which has no unit. 
 
 
Now we proceed onto study super matrix structure using R+ 
∪ {0} or Q+ ∪ {0} or Z+ ∪ {0}. 
 
 
Let 
R
S+  = {(x1 x2 x3 | x4 … | xn-1 xn) | xi ∈ R+ ∪ {0} or Q+ ∪ 
{0} or Z+ ∪ {0}} denotes the collection of all super row 
matrices of same type from R+ ∪ {0} or Q+ ∪ {0} or Z+ ∪ {0}.  
This notation will be used throughout this book. 
 
C
S+  = 
1
2
3
m
a
a
a
a


















aj ∈ Z+ ∪ {0} or R+ ∪ {0} 
or Q+ ∪ {0}; 1 ≤ i ≤ m} 
 
denotes the collection of all column super matrices of same type 
with entries from R+ ∪ {0} or Q+ ∪ {0} or Z+ ∪ {0}.


## Page 208


208
 
 
m n
S+
×  (m ≠ n) = 
11
12
1n
21
22
2n
m1
m2
mn
a
a
...
a
a
a
...
a
a
a
...
a


















aij ∈ Q+ ∪ {0} 
 
or Z+ ∪ {0} or R+ ∪ {0}; 1 ≤ i ≤ m, 1 ≤ j ≤ n} 
 
denotes the collection of all m × n super matrices of same type 
with entries from Q+ ∪ {0} or  Z+ ∪ {0} or R+ ∪ {0}. 
 
n n
S+
×  = 
11
12
1n
21
22
2n
n1
n2
nn
a
a
...
a
a
a
...
a
a
a
...
a


















aij ∈ Z+ ∪ {0} 
 
or Q+ ∪ {0} or R+ ∪ {0}; 1 ≤ i, j ≤ n} 
 
denotes the collection of all n × n super matrices of same type 
with entries from R+ ∪ {0} or  Q+ ∪ {0} or Z+ ∪ {0}.   
 
We will first illustrate these situations by some examples. 
 
Example 5.38:  Let  
 
R
S+  = {(x1 x2 | x3 x4  x5 | x6 x7 | x8) | xi ∈ Q+ ∪ {0}, 1 ≤ i ≤ 8} 
 
be the super row matrices of same type with entries from Q+ ∪ 
{0}.


## Page 209


209
Example 5.39: Let 
R
S+  = 
 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
25
25
26
27
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











 
 
ai ∈ Z+ ∪ {0}; 1 ≤ i ≤ 27} 
 
be the set of all super row vectors of same type with entries 
from Z+ ∪ {0}. 
 
 
Example 5.40: Let  
 
C
S+  =
1
2
3
4
5
6
7
8
9
10
11
a
a
a
a
a
a
a
a
a
a
a













































ai ∈ Q+ ∪ {0}; 1 ≤ i ≤ 11} 
 
denote the collection of super column matrices of same type 
with entries from Q+ ∪ {0}.


## Page 210


210
Example 5.41: Let  
 
C
S+  =
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a







































ai ∈ R+ ∪ {0}; 1 ≤ i ≤ 36} 
 
denote the collection  of all super column vectors of same type 
with entries from R+ ∪ {0}. 
 
 
Example 5.42: Let  
 
3 4
S+
×  =
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ R+ ∪ {0}; 1 ≤ i ≤ 12} 
 
be the collection of all 3 × 4 super matrices of same type with 
entries from R+ ∪ {0}.


## Page 211


211
 
 
Example 5.43: Let  
 
5 5
S+
×  =
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















ai ∈ R+ ∪ {0}; 1 ≤ i ≤ 25} 
 
be the collection of 5 × 5 super matrices of same type with 
entries from R+ ∪ {0}. 
 
 
Now we proceed onto give all possible algebraic structures 
on 
C
F+  , 
R
F+  or 
m n
F+
×  (m ≠ n) and 
n n
F+
× .  
 
 
Consider 
C
F+  the collection of all super column matrices of 
same type with entries from Q+ ∪ {0} or R+ ∪ {0} or Z+ ∪ {0}; 
C
S+  is a semigroup under ‘+’ usual addition.  Infact it has the 
additive identity and (
C
S+ , +) is a commutative semigroup.  
Likewise 
R
F+  or 
m n
F+
×  (m ≠ n) and 
n n
F+
×  are all abelian 
semigroups with respect to addition.  Infact all of them are 
monoids.   
 
We will illustrate this by some examples.


## Page 212


212
Example 5.44:  Let  
 
C
S+  = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a



























 ai ∈ Z+ ∪ {0}; 1 ≤ i ≤ 8} 
be a commutative semigroup of super column matrices with 
entries from Z+ ∪ {0}. 
 
 
Example 5.45:  Let  
 
m n
S+
×  = 
1
8
15
22
2
9
16
23
3
10
17
24
4
11
18
25
5
12
19
26
6
13
20
27
7
14
21
28
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a























ai ∈ Q+ ∪ {0}; 1 ≤ i ≤ 28} 
 
 
be the semigroup of super 7 × 4 matrices under addition with 
entries from Q+ ∪ {0}.


## Page 213


213
Example 5.46:  Let  
 
4 4
S+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a















ai ∈ R+ ∪ {0}; 1 ≤ i ≤ 16} 
 
be the semigroup of super 4 × 4 super matrices with entries 
from R+ ∪ {0}. 
 
Example 5.47:  Let  
 
3 9
S+
×  = 
1
4
7
10
13
16
19
22
25
2
5
8
11
14
17
20
23
26
3
6
9
12
15
18
21
24
27
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











 
 
ai ∈ Q+ ∪ {0}; 1 ≤ i ≤ 27} 
 
be the semigroup of super row vector under addition with 
elements from Q+ ∪ {0}. 
 
Example 5.48:  Let  
10 9
S+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

































ai ∈ Q+ ∪ {0}; 1 ≤ i ≤ 40}


## Page 214


214
be the semigroup of super column vector under addition. 
 
 
Now we proceed onto define natural product on 
C
S+ , 
R
S+ ,
n n
S+
×   and 
m n
S+
×  (m ≠ n).  Clearly 
C
S+  , 
R
S+ ,
n m
S+
×   (m ≠ n) and 
m m
S+
×  are semigroups under the natural product ×n. 
 
 
Depending on the set from which they take their entries they 
will be semigroups with multiplicative identity or otherwise.   
 
 
We will illustrate this situation by some examples. 
 
Example 5.49:  Let 
R
S+  = {(a1 | a2 a3 | a4 a5 a6 | a7 a8 a9 a10 | a11 | 
a12) | ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 12} be a semigroup of super row 
matrices under the natural product ×n. 
 
Example 5.50:  Let  
 
C
S+  = 
1
2
3
4
5
6
7
8
9
10
11
x
x
x
x
x
x
x
x
x
x
x













































 xi ∈ Z+ ∪ {0}, 1 ≤ i ≤ 11} 
 
be a semigroup of super column matrices under the natural 
product ×n. Infact 
C
S+  has units and zero divisors.


## Page 215


215
Example 5.51:  Let  
 
C
S+  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a







 
 
ai ∈ R+ ∪ {0}, 1 ≤ i ≤ 20} 
 
be the semigroup of super row vector under the natural product 
×n. 
2 10
S+
×  has identity elements, units and zero divisors. 
 
Example 5.52:  Let  
8 3
S+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a



























 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 24} 
 
be a semigroup of super column vectors under natural product 
×n.  
 
Clearly
8 3
S+
×  has identity I = 
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1


























 but no element in 
8 3
S+
×  
has units but has several zero divisors.


## Page 216


216
 
Example 5.53:  Let  
 
2 2
S+
×  = 
1
2
3
4
a
a
a
a









 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 2} 
be the semigroup of super square matrices under natural product 
×n.  Clearly 
1 1
1 1








 is the identity element of 
2 2
S+
× , but has no 
units, that is no element in 
2 2
S+
×  has inverse.  Further 
2 2
S+
×  has 
zero divisors.  For take x = 
1
2
0
0
a
a








 in 
2 2
S+
×  then y1 = 
1
2
a
a
0
0








 and y3 = 
1
0
a
0
0








 are all zero divisors in 
2 2
S+
× . 
 
Example 5.54:  Let  
 
8 4
S+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a



























 ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 32} 
 
be the semigroup of 8 × 4 super matrices with entries from Q+ ∪ 
{0}.


## Page 217


217
8 4
S+
×  is a semigroup with unit I = 
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1


























 and has zero  
 
divisors and inverses.  Now we can find ideals, subsemigroups, 
zero divisors and units in semigroups under the natural product 
×n.  These will be only illustrated by some examples. 
 
Example 5.55:  Let  
 
C
S+  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

































 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 30} 
 
be the semigroup of super column vectors.   
 
This has units and zero divisors.


## Page 218


218
Take P = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a
0
0
0
0
0
0

































 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 12} ⊆ 
C
S+  
 
is an ideal of 
C
S+  under natural product ×n.   
 
Now  
 
M = 
1
2
3
4
5
6
7
8
9
0
0
0
a
a
a
a
a
a
0
0
0
0
0
0
0
0
0
a
a
a
0
0
0
0
0
0
0
0
0

































 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 9} ⊆ 
C
S+  
 
is an ideal of 
C
S+  under natural product.


## Page 219


219
 
Take x = 
1
2
3
4
5
6
7
8
9
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0
































 and y = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
a
a
a
a
a
0
0
0
0
0
0
0
0
0
a
a
a
0
0
0
0
0
0
0
0
0
































 in 
C
S+ ,   
 
we see x ×n y = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
































.  No element in 
C
S+  has inverse. 
 
Example 5.56:  Let 
R
S+  =  
 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ Q+ ∪ {0},  
 
1 ≤ i ≤ 32}


## Page 220


220
be  the semigroup of super row vectors under the natural 
product ×n.  
 
Take I = 
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1












 be the unit in 
R
S+ . 
 
 
Consider X = 
1
5
9
13
2
6
10
14
3
7
11
15
4
8
12
16
a
0
0
a
a
a
0
0
a
0
0
a
a
a
0
0
a
0
0
a
a
a
0
0
a
0
0
a
a
a
0
0













  
 
ai ∈ 5Z+ ∪ {0}, 1 ≤ i ≤ 16} ⊆ 
R
S+ ; 
 
× is only a subsemigroup under ×n.  X has no identity.  Further 
X is not an ideal of 
R
S+ .  However X has zero divisors.  
 
 
Take  
 
Y = 
1
2
9
10
3
4
11
12
5
6
13
14
7
8
15
16
0
a
a
0
0
0
a
a
0
a
a
0
0
0
a
a
0
a
a
0
0
0
a
a
0
a
a
0
0
0
a
a













 ai ∈ Q+ ∪ {0}, 
1 ≤ i ≤ 16} ⊆ 
R
S+ ; 
 
Y is an ideal of 
R
S+ .  It is still interesting to note that every 
element x in X is such that x ×n y = (0) for every y ∈ Y.  
However X + Y ≠ 
R
S+ .


## Page 221


221
Example 5.57:  Let  
 
4 4
S+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















 ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 32} 
 
be  the semigroup of super square matrices under the natural 
product ×n.  
 
I = 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
















 
acts as the identity with respect to the natural product ×n. 
 
 
Consider  
P = 
1
2
3
4
5
6
7
8
10
11
9
12
13
a
0
0
a
a
0
a
a
0
0
0
a
a
0
0
a
0
0
a
a
a
0
0
a
a

















 ai ∈ Z+ ∪ {0}, 
1 ≤ i ≤ 13} ⊆ 
4 4
S+
× . 
 
P is only a subsemigroup and not an ideal of 
4 4
S+
× .


## Page 222


222
 
 
Consider  
 
M = 
1
2
3
5
6
4
7
8
9
10
10
11
11
12
12
13
0
a
a
0
0
a
0
0
a
a
a
0
0
a
a
0
a
a
a
a
0
a
a
a
a

















 ai ∈ Q+ ∪ {0},  
1 ≤ i ≤ 12} ⊆ 
4 4
S+
× ; 
 
M is an ideal of 
4 4
S+
× . Every element p in P is such that p ×n m = 
(0) for every m ∈ M. 
 
Inview of this we have the following theorem. 
 
THEOREM 5.15:  Let 
C
S +  (or 
R
S +  or 
m n
S +
×   (m ≠ n) or 
n n
S +
× ) be a 
semigroup under the natural product.  Every ideal I in 
C
S +  (or 
R
S+  or 
n m
S+
×   (m ≠ n) or 
n n
S +
× ) is a subsemigroup of 
C
S +    (or 
R
S +  
or 
n m
S +
×   (m ≠ n) or 
n n
S+
× ) but however every subsemigroup of 
C
S +  (or 
R
S +  or 
n m
S +
×   (m ≠ n) or 
n n
S +
× ) need not in general be an 
ideal of 
C
S +  (or 
R
S +  or 
n m
S +
×   (m ≠ n) or 
n m
S +
× ).   
 
The proof is simple and direct hence left as an exercise to 
the reader. 
 
 
Now having seen all these we now proceed onto give two 
binary operations on 
R
S+  (or 
C
S+  or 
m n
S+
×   (m ≠ n) or 
n n
S+
× ) so 
R
S+  
(or 
C
S+  or 
m n
S+
×   (m ≠ n) or 
n n
S+
× ), so that 
R
S+  is the semiring with 
respect to addition and natural product.  
 
 
Consider (
C
S+ , +, ×n) = 
C
P+ , it is easily verified 
C
P+  is a 
semiring which is a strict semiring of super column matrices


## Page 223


223
and is not a semifield as it has zero divisors under the product 
×n. 
 
 
Likewise 
R
P+  = {
R
S+ , +, ×n} is a semiring of super row 
matrices which is not a semifield, infact a strict commutative 
semiring. 
 
 
m n
P+
×  (m ≠ n) = {
m n
S+
× (m ≠ n), +, ×n} is a strict commutative 
semiring of m × n super matrices.  Finally 
n n
P+
×  = {
n n
S+
× , +, ×n} 
is a strict commutative semiring of super square matrices. 
 
 
Now throughout this book 
C
P+  will denote the semiring of 
super column matrices, 
R
P+  will denote the semiring of super 
row matrices,  
m n
P+
×  (m ≠ n) will denote the semiring of m × n 
super matrices and 
n n
P+
×  will denote the semiring of square 
super matrices.   
 
Now having seen the notation we proceed onto give 
examples of them. 
 
Example 5.58:  Let  
 
C
P+  = 
1
2
3
4
5
6
7
8
9
10
a
a
a
a
a
a
a
a
a
a

































ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 10, +, ×n}


## Page 224


224
be the semiring of super column matrices; 
C
P+  is not a semifield 
as it has zero divisors. 
 
 
Further 
C
P+  has subsemirings for take  
 
M = 
1
2
3
4
5
6
a
a
a
a
0
0
0
a
a
0

































ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 6, +, ×n} ⊆ 
C
P+  
is a subsemiring of 
C
P+  and is not an ideal of 
C
P+ .   
 
However 
C
P+  has ideals for consider  
 
N = 
1
2
3
4
0
0
0
0
a
a
a
0
0
a

































ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 4, +, ×n} ⊆ 
C
P+


## Page 225


225
is an ideal of 
C
P+ . 
 
 
We see for every x ∈ M is such that  
 
x ×n y = 
0
0
0
0
0
0
0
0
0
0
















 for every y ∈ N. 
 
Thus 
C
P+  has infinitely many zero divisors so is not a semifield.   
 
Finally 
1
1
1
1
1
1
1
1
1
1
















 acts as the identity with respect to ×n. 
 
Example 5.59:  Let 
R
P+  = {(a1 | a2 a3 | a4 a5 a6 | a7 a8 a9 | a10) | ai ∈ 
3Z+ ∪ {0}, 1 ≤ i ≤ 10, +, ×n} be a strict semiring of super row 
matrices.  Clearly (1 | 1 1 | 1 1 1 | 1 1 1 | 1) ∉ 
R
P+ .  We see 
R
P+


## Page 226


226
has zero divisors for take x = (4 | 0 3 | 2 0 1 | 0 3 9 | 0) and y = 
(0 | 7 0 | 0 8 0 | 9 0 0 | 1 0) in 
R
P+ .  Clearly x ×n y = (0 | 0 0 | 0 0 
0 | 0 0 0 | 0).  So 
R
P+  is a semiring which is not a semifield and 
has no identity. 
 
Example 5.60:  Let  
 
3 4
P+
×  = 
1
12
23
2
13
24
3
14
25
4
15
26
5
16
27
6
17
28
7
18
29
8
19
30
9
20
31
10
21
32
11
22
33
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a



































 ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 33, +, ×n} 
 
be the semiring of super column vectors.  
3 11
P+
×  has zero 
divisors, units, ideals and subsemirings which are not ideals.  
However 
3 11
P+
×  is not a semifield. 
 
Example 5.61:  Let 
12 2
P+
×  =  
 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a







 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 24, +, ×n} 
 
be a semiring, 
12 2
P+
×  has unit element, however no element in 
12 2
P+
×  has inverse.  Further 
12 2
P+
×  has zero divisors so not a


## Page 227


227
semifield.  Has ideals.  Thus 
12 2
P+
× is a super row vector 
semiring. 
 
Example 5.62:  Let  
 
4 4
P+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a















 ai ∈ R+ ∪ {0}, 1 ≤ i ≤ 16, +, ×n} 
 
be the semiring of square super matrices.  
4 4
P+
×  has zero divisors 
units, subsemirings which are not ideals and ideals. 
 
 
Clearly 
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1














 = I is the unit of 
4 4
P+
×  .   
 
S = 
1
2
3
4
5
6
7
a
0
0
0
a
0
0
0
a
0
0
0
a
a
a
a















 ai ∈ R+ ∪ {0}, 1 ≤ i ≤ 7, +, ×n} 
is a subsemiring  which is also an ideal of 
4 4
P+
× . 
 
 
 
Consider  
 
L = 
1
2
3
4
5
6
7
8
9
0
a
a
a
0
a
a
a
0
a
a
a
0
0
0
0















 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 9, +, ×n} ⊆ 
4 4
P+
× ;


## Page 228


228
 
L is a subsemiring of 
4 4
P+
×  which is not an ideal of 
4 4
P+
× .  Finally 
for every x ∈ S and y ∈ L we have x ×n y = 0 for every y ∈ L. 
 
Example 5.63:  Let  
 
6 4
P+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
























 ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 24, +, ×n} 
 
be a semiring of 6 × 4 super matrices.   
 
I = 
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1




















 is the unit of 
6 4
P+
×  under natural product. 
 
Further  
 
S = 
1
3
5
4
7
8
9
10
11
12
5
6
a
0
0
a
a
0
0
a
0
a
a
0
0
a
a
0
0
a
a
0
a
0
0
a
























 ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 12, +, ×n} 
⊆ 
6 4
P+
×  is only a subsemiring of 
6 4
P+
×  and is not an ideal of 
6 4
P+
× .


## Page 229


229
 
 
Now  
 
T = 
9
10
11
12
1
6
2
7
3
8
4
5
0
a
a
0
0
a
a
0
a
0
0
a
a
0
0
a
a
0
0
a
0
a
a
0
























 ai ∈ Q+ ∪ {0}, 
1 ≤ i ≤ 12, +, ×n} ⊆ 
6 4
P+
×  
 
is a subsemiring as well as an ideal of 
6 4
P+
× .  Now we see for 
every x ∈ S we have every y ∈ T are such that x ×n y = (0).  
Thus 
6 4
P+
×  is only a semiring and not a semifield. 
 
 
Now we proceed onto define semifields of super matrices. 
 
 
Let 
R
J+  = {(x1 x2 | x3 x4 x5 | … | xn) | xi ∈ R+ (or Q+ or Z+),  
1 ≤ i ≤ n}  ∪ {(0 0 | 0 0 0 | … | 0)}, ×, +n} be the semifield of 
super row matrices.  
 
 
For 
R
J+  has no zero divisors with respect to ×n and 
R
J+  is a 
strict commutative semiring.


## Page 230


230
 
Now  
 
C
J+  = 
1
2
3
4
n 1
n
m
m
m
m
m
m
−





























 mi ∈ Z+ (or Q+ or R+), 1 ≤ i ≤ n} ∪ 
0
0
0
0
0
0















, +, ×n} 
 
is the semifield of super column matrices. 
 
 
n m
J+
×  (m ≠ n) = 
11
12
1m
21
22
2m
n1
n2
nm
a
a
...
a
a
a
...
a
a
a
...
a


















 aij ∈ R+  
 
(or Z+ or Q+), 1 ≤ i ≤ n; 1 ≤ j ≤ m}  ∪ 
0
0
...
0
0
0
...
0
0
0
...
0
















 , +, ×n} is 
the semifield of n × m super matrices.  
 
n n
J+
× = 
11
12
13
1n
21
22
23
2n
n1
n2
n3
nn
a
a
a
...
a
a
a
a
...
a
a
a
a
...
a



















 aij ∈ Z+ (or Q+ or R+),  
1 ≤ i, j ≤ n}


## Page 231


231
∪ 
0
0
0
...
0
0
0
0
...
0
0
0
0
...
0

















 , ×n, +} 
 
is the semifield of square super matrices.   
 
Now we just give some examples of them. 
 
Example 5.64:  Let  
 
C
J+  = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a





























 ai ∈ Z+; 1 ≤ i ≤ 9} ∪ 
0
0
0
0
0
0
0
0
0














, ×n, +} 
 
be the semifield of super column matrices.  This has no proper 
subsemifields.  
 
Example 5.65:  Let 
R
J+  = {(a1 a2 | a3 a4 a5 a6 a7 | a8 a9 a10 | a11) | ai 
∈ Q+; 1 ≤ i ≤ 11} ∪ (0 0 | 0 0 0 0 0 | 0 0 0 | 0), ×n, +} be the 
semifield of super row matrices.


## Page 232


232
Example 5.66:  Let  
 
5 5
J+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a


















 ai ∈ R+; 1 ≤ i ≤ 25} 
 
∪ 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















, ×n, +} 
 
is the semifield of super square matrices.  This semifield has 
subsemifields.  
 
Example 5.67:  Let  
 
8 4
J+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a




























 ai ∈ Q+; 1 ≤ i ≤ 32}


## Page 233


233
∪
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0


























, ×n, +} 
 
is a semifield of super 8 × 4 matrices.  This semifield has 
subsemifields. 
 
Example 5.68:   
 
9 3
J+
×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a












 
ai ∈ R+; 1 ≤ i ≤ 27}  
 
∪ 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0










, +, ×n} 
 
is the semifield of super row vectors.  This has subsemifields.


## Page 234


234
Example 5.69:  Let  
 
J+ = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a


































 ai ∈ Z+; 1 ≤ i ≤ 20} ∪ 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
































, +, ×n} 
 
be the semifield of super column vectors.  This has no 
subsemifields but has subsemirings.


## Page 235


235
 
 
 
 
 
Chapter Six 
 
 
 
 
SUPERMATRIX LINEAR ALGEBRAS 
 
 
 
 
 
In this chapter we introduce the notion of super matrix 
vector space (linear algebra) and super matrix, polynomials with 
super matrix coefficients.  Several properties enjoyed by them 
are defined, described and discussed. 
 
 
Let V = {(x1 x2 | x3 … | xm-1 xn) | xi  Q (or R); 1  i  n} be 
the collection of super row vectors of same type under addition.  
V is a vector space over Q (or R).  Now we can define the 
natural product on V so that V is a super linear algebra of super 
row matrices or linear algebras of super row matrices or super 
row matrices linear algebras. 
 
 
We will illustrate this by some simple examples. 
 
Example 6.1:   Let V = {(x1 x2 x3 | x4 | x5 x6) | xi  R; 1  i  6} 
be a super vector space over the field F = R. 
 
 
V is also a super linear algebra under the natural product n.


## Page 236


236
 
For x = (x1 x2 x3 | x4 | x5 x6) and y = (y1 y2 y3 | y4 | y5 y6) we 
have x n y = (x1y1  x2y2  x3y3 | x4y4 | x5y5  x6y6). 
 
Example 6.2:  Let  
 
V = {(x1 x2 | x3 | x4 x5 x6 | x7 x8 | x9) | xi  Q; 1  i  9} 
 
be a linear algebra of super row matrices over the field Q, with 
natural product n. 
 
 
Consider P1 = {(x1 x2 | 0 | 0 0 0 | 0 0 | 0) | x1, x2  Q}  V; 
P2 = {(0 0 | a1 | 0 0 0 | a2 a3 | 0) | a1, a2, a3  Q}  V and P3 = {(0 
0 | 0 | a1 a2 a3 | 0 0 | a4) | ai  Q; 1  i  4}  V be linear 
subalgebras of V over the field Q.   
 
Clearly V = P1 + P2 + P3  and Pi  Pj = (0 0 | 0 | 0 0 0 | 0 0 | 
0) if i  j; 1  i, j  3, so V is a direct sum of P1, P2 and P3. 
 
Example 6.3:  Let  
 
V = {(x1 | x2 x3 | x4 x5 | x6 x7 x8 x9 x10) | xi  Q; 1  i  10} 
be a super row matrix linear algebra over the field Q.  Consider 
M1 = {(a1 | 0 | 0 | 0 0 | 0 0 0 a2 a3) | a1, a2,  a3  Q}  V, M2 = 
{(0 | a1 | 0 | 0 0 | a2 0 0 0 a3) | a1, a2, a3  Q}  V, M3 = {(0 | 0 | 
a1 | a2 0 | 0 0 0 0 a3) | a1, a2, a3  Q}  V, M4 = {(0 | 0 | 0 | 0 a1 | 
0 a2 0 0 a3) | a1, a2, a3  Q}  V and M5 = {(0 | 0 | 0 | 0 0 | 0 0 a1 
a2 a3) | a1, a2, a3  Q}  V be a super sublinear algebras of V 
over Q.   
 
Clearly Mi  Mj  (0 | 0 | 0 | 0 0 | 0 0 0 0 a) if i  j for 1  i, 
j  5.  Thus V  M1 + M2 + M3 + M4 + M5; so V is not a direct 
sum only a pseudo direct sum. 
 
Example 6.4:  Let  
 
V = {(x1 x2 x3 | x4 | x5 | x6 x7 x8) | xi  Q; 1  i  8} 
 
be a linear algebra of super row matrices.


## Page 237


237
 
Consider X = (x1 x2 x3 | 0 | 0 | 0 0 x4) where xi  Q; 1  i  
4}  V and Y = {(0 0 0 | x1 | x2 | x3 x4 0) | xi  Q; 1  i  4}  V 
be two linear subalgebras of super row matrices, we see for 
every x  X and y  Y, x n y = (0 0 0 | 0 | 0 | 0 0 0).  Thus we 
see X = Y and Y = X.  Further V = X+Y and X  Y = (0 0 0 | 
0 | 0 | 0 0 0).   
 
We have seen examples of super linear algebras of super 
row matrices. 
 
Example 6.5:  Let  
 
V = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a



























 ai  Q; 1  i  8} 
 
be a super column linear algebra over the field Q.  Dimension of 
V over Q is eight. Consider  
 
x = 
1
2
3
0
0
a
a
a
0
0
0


























 in V then y = 
1
2
3
x
y
0
0
0
a
a
a




























## Page 238


238
in V is such that  
x n y = 
0
0
0
0
0
0
0
0













. 
 
Now we can find sublinear algebras of V. 
 
Example 6.6:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
a
a
a
a
a
a
a
a
a
a
a













































 ai  Q; 1  i  11} 
 
be a linear algebra of super column matrices under the natural 
product n.


## Page 239


239
Consider  
M1 = 
1
2
a
a
0
0
0
0
0
0
0
0
0













































 a1 , a2  Q}  V, 
 
M2 = 
1
2
3
0
0
a
a
a
0
0
0
0
0
0













































 a1, a2, a3  Q}  V,


## Page 240


240
M3 = 
1
2
0
0
0
0
0
a
a
0
0
0
0













































 a1 , a2  Q}  V 
 
and   
M4 = 
1
2
3
4
0
0
0
0
0
0
0
a
a
a
a













































 ai  Q; 1  i  4}  V 
 
be linear subalgebras of super column matrices.


## Page 241


241
 
Clearly Mi  Mj = 
0
0
0
0
0
0
0
0
0
0
0


















 if i  j, 1  i, j  4.   
 
Also V = M1 + M2 + M3 + M4; thus V is a direct sum of linear 
subalgebras of V over Q.   
 
 
We see for every x  M1 every y  M2 is such that x n y = 
(0).  Likewise for every x  M1, every z  M3 is such that x n z 
= (0) and for every x  M1, every t  M4 is such that x n t = 
(0).   
 
Hence we can say for every x  Mj every element in Mi (i  
j)  (i=1 or 2 or 3 or 4) is orthogonal with x; however 
j
m is not 
Mi for i  j, i = 1 or 2 or 3 or 4.   
 
Thus we see 
1
m = (M2 + M3 + M4); similarly for M2 = M1 
+ M3 + M4 and so on.  These subspaces are not complements of 
each other.


## Page 242


242
Example 6.7:  Let  
 
P = 
1
2
3
4
5
6
7
x
x
x
x
x
x
x























xi  Q; 1  i  7} 
be a super linear algebra of super column matrices under the 
natural product n. 
 
 
Consider  
M1 = 
1
2
3
0
x
x
0
0
0
x























xi  Q; 1  i  7}  P 
and  
M2 = 
1
2
3
4
x
0
0
x
x
x
0























xi  Q; 1  i  4}  P 
 
be two super linear subalgebras of P over Q.


## Page 243


243
We see M1  M2 = 
0
0
0
0
0
0
0











 and P = M1 + M2. 
 
Further the complementary subspace of M1 is M2 and vice 
versa.  We see every element in M1 is orthogonal with every 
element in M2 under orthogonal product. 
 
Example 6.8:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a















ai  Q; 1  i  16} 
 
be a super linear algebra of square super matrices under natural 
product n. 
 
 
We see for  
 
x = 
1
2
3
4
5
6
0
a
a
a
0
0
0
0
0
a
a
a
0
0
0
0














 in V, y = 
1
2
5
6
7
3
4
5
6
7
x
0
0
0
x
x
x
x
x
0
0
0
x
x
x
x














 
 
in V is such that


## Page 244


244
x n y =
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0














 in V 
 
take y1 =  
1
2
3
0
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0














 in V 
 
we see x n y1 = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0














. 
 
Thus we call y1 as a partial complement, only y is the real or 
total complement of x.   
 
We can have more than one partial complement but one and 
only one total complement.  
 
Example 6.9: Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















ai  Q; 1  i  25} 
 
be a super linear of square super matrices under natural product 
n.  We can have the following subspaces of M.


## Page 245


245
 
 
Consider  
 
P1 = 
1
3
4
2
5
6
a
0
0
a
a
a
0
0
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

















ai  Q; 1  i  6}  M, 
 
P2 = 
4
5
1
6
2
7
3
8
0
0
0
a
0
0
0
0
a
0
a
0
0
0
a
a
0
0
0
a
a
0
0
0
a

















ai  Q; 1  i  8}  M,  
 
P3 = 
1
2
5
3
4
6
0
a
a
a
0
0
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

















ai  Q; 1  i  6}  M,  
 
P4 = 
5
6
1
6
2
7
3
8
0
0
0
a
0
0
0
0
a
0
0
a
0
a
0
0
a
0
a
0
0
a
0
a
0

















ai  Q; 1  i  8}  M and


## Page 246


246
P5 = 
4
5
1
2
3
0
0
0
a
0
0
0
0
a
0
0
0
a
0
0
0
0
a
0
0
0
0
a
0
0

















ai  Q; 1  i  5}  M  
 
are super linear subalgebras of super square matrices over Q.   
 
We see V  P1 + P2 + P3 + P4 + P5 and  
 
Pi  Pj = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















; 
if  i  j; 1  i, j  5. 
 
 
Thus V is only a pseudo direct sum of linear subalgebras 
and is not a direct sum of linear subalgebras.  
 
Example 6.10:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai  Q; 1  i  9} 
 
be a super linear algebra of square super matrices over Q.    
 
Consider  
P1 = 
1
2
3
4
0
0
0
a
a
0
a
a
0











ai  Q; 1  i  4}  V


## Page 247


247
and  
P2 = 
1
2
3
4
5
a
a
a
0
0
a
0
0
a











ai  Q; 1  i  5}  V 
be super linear subalgebras of V over Q.  Clearly the space 
orthogonal with P1 is P2 and vice versa.  No other space of V 
can be orthogonal (complement) of P1 in V.   
 
Further V = P1 + P2 and P1  P2 = 
0
0
0
0
0
0
0
0
0










. 
Example 6.11:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a























ai  Q; 1  i  21} 
 
be a super linear algebra of super column vector under natural 
product n.  Consider  
 
P1 = 
1
2
3
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0























ai  Q; 1  i  3}  M,


## Page 248


248
 
P2 = 
1
2
3
4
5
6
0
0
0
a
a
a
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0























ai  Q; 1  i  6}  M, 
 
P3 = 
1
2
3
4
5
6
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a























ai  Q; 1  i  6}  M  
and 
P4 = 
1
2
3
4
5
6
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a
0
0
0
0
0
0























 ai  Q; 1  i  6}  M 
 
be super linear subalgebras of super column vectors over the 
field Q.


## Page 249


249
We see P1 + P2 + P3 + P4 = V and Pi  Pj = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






















, i  j;  
1  i, j  4.  
 
 
Example 6.12:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a





























ai  Q; 1  i  36} 
 
be a super linear algebra of super column vectors.  Take


## Page 250


250
P1 = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
a
0
0
0
0
a
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a





























 ai  Q; 1  i  12}  M; 
 
P2 = 
1
2
3
4
5
6
7
8
9
10
11
12
0
0
0
0
a
a
a
a
0
0
0
0
a
a
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a





























 ai  Q; 1  i  12}  M,  
 
P3 = 
1
2
3
4
5
6
7
8
9
10
11
12
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a
a
a
0
0
0
0
0
0
0
0
a
a
a
a





























 ai  Q; 1  i  12}  M  
and


## Page 251


251
P4 = 
1
2
3
4
5
6
7
8
9
10
11
12
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
a
a
a
a
a
a
a
a
a
a





























 ai  Q; 1  i  12}  M  
be super linear subalgebras M over the field Q.   
Clearly Pi  Pj  
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0




























; if i  j; 1  i, j  4. 
 
 
Further V  P1 + P2 + P3 + P4; thus V is only a pseudo 
direct sum of super linear subalgebras of super column vectors 
over Q. 
 
Example 6.13:  Let M =  
 
1
5
9
13
17
21
25
26
27
28
29
2
6
10
14
18
22
30
31
32
33
34
3
7
11
15
19
23
35
36
37
38
39
4
8
12
16
20
24
40
41
42
43
44
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 
ai  Q; 1  i  44}


## Page 252


252
 
be the super linear algebra of super row vectors over Q.   
Consider 
  
P1 = 
1
5
2
6
3
7
4
8
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0













 
 
ai  Q; 1  i  8}  M, 
 
P2 = 
1
5
2
6
3
7
4
8
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0













 
  
ai  Q; 1  i  8}  M, 
 
P3 =
1
5
2
6
3
7
4
8
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0













 
 
ai  Q; 1  i  8}  M, 
 
P4 =
1
2
3
4
5
6
7
8
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0
0
0
a
a
0
0
0













 ai  Q;  
 
1  i  8}  M


## Page 253


253
and 
 
P5 =
1
2
3
4
5
6
7
8
9
10
11
12
0
0
0
0
0
0
0
0
a
a
a
0
0
0
0
0
0
0
0
a
a
a
0
0
0
0
0
0
0
0
a
a
a
0
0
0
0
0
0
0
0
a
a
a













 ai  Q;  
 
1  i  12}  M,  
 
be super linear subalgebras of V of super row vectors over Q. 
 
 
Clearly Pi  Pj = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0












 if 
i  j and 1  i, j  5. 
 
 
M = P1 + P2 + P3 + P4 + P5 so M is the direct sum of super 
linear subalgebras of super row vectors over the field Q. 
 
Example 6.14:  Let V =   
 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a







 ai  Q;  
1  i  20} 
 
be a super linear algebra of super row vectors over Q. 
 
 
Consider  
H1 = 
1
3
2
4
a
a
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
0







 ai  Q;  
1  i  4}  V,


## Page 254


254
H2 = 
2
3
1
4
0
a
a
0
0
0
0
0
0
0
a
a
0
0
0
0
0
0
















 V, 
 
H3 = 
1
3
2
4
0
a
0
a
0
0
0
0
0
0
a
0
a
0
0
0
0
0
















  V, 
 
H4 = 
1
3
2
4
0
a
0
0
a
0
0
0
0
0
a
0
0
a
0
0
0
0
















  V , 
 
H5 = 
1
3
2
4
0
a
0
0
0
a
0
0
0
0
a
0
0
0
a
0
0
0
















  V, 
H6 = 
1
3
2
4
0
a
0
0
0
0
a
0
0
0
a
0
0
0
0
a
0
0
















  V, 
 
H7 = 
1
3
2
4
0
a
0
0
0
0
0
a
0
0
a
0
0
0
0
0
a
0
















  V,   
 
H8 =
1
3
2
4
0
a
0
0
0
0
0
0
a
0
a
0
0
0
0
0
0
a







 ai  Q; 1  i  4} V 
are  super  linear  subalgebras of super  row vector over the  
field Q. 
 
 
Clearly  
 
Hi  Hj  
1
2
0
a
0
0
0
0
0
0
0
0
a
0
0
0
0
0
0
0







 ai  Q; 1  i  4} 
 
if i  j, 1  i, j  8.  We see V  H1 + H2 + H3 + H4 + H5 + H6 + 
H7 + H8 is only a pseudo direct sum of the sublinear algebras of 
V over Q.


## Page 255


255
Example 6.15:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

























 ai  Q; 1  i  30} 
 
be a super linear algebra of 6  5 super matrices over the field Q 
under the natural product n. 
 
 
Consider  
 
M = 
1
2
3
4
a
0
0
0
0
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
0
0

























 ai  Q; 1  i  4}  V, 
 
M2 = 
1
2
3
4
0
0
0
0
0
0
0
0
0
0
a
0
0
0
0
a
0
0
0
0
a
0
0
0
0
a
0
0
0
0

























 ai  Q; 1  i  4}  V,


## Page 256


256
M3 = 
1
2
3
4
0
a
a
0
0
0
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

























 ai  Q; 1  i  4}  V,  
 
M4 = 
1
2
3
4
5
6
0
0
0
0
0
0
0
0
0
0
0
a
a
0
0
0
a
a
0
0
0
a
a
0
0
0
0
0
0
0
























 ai  Q; 1  i  4}  V,  
M5 = 
1
2
3
4
0
0
0
a
a
0
0
0
a
a
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

























 ai  Q; 1  i  4}  V,  
 
M6 = 
1
2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a

























 ai  Q; 1  i  4}  V,   
 
and


## Page 257


257
M7 = 
1
2
3
4
5
6
0
0
0
0
0
0
0
0
0
0
0
0
0
a
a
0
0
0
a
a
0
0
0
a
a
0
0
0
0
0

























 ai  Q; 1  i  4}  V  
 
be super linear subalgebra of super matrices over Q under the 
natural product n.   
Clearly  Mi  Mj = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0




















 if i  j, 1  i, j  7.   
We see V = M1 + M2 + M3 + M4 + M5 + M6 + M7, that is V 
is the direct sum of sublinear algebras of V. 
 
 
Now 
we 
proceed 
onto 
give 
examples 
of 
linear 
transformation and linear operators on super linear algebra of 
super matrices with natural product n. 
 
Example 6.16:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











 ai  Q; 1  i  9} 
 
be a super linear algebra of square super matrices over the field 
Q under the natural product n.


## Page 258


258
Let  
P = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a





























 ai  Q; 1  i  9} 
 
be a super linear algebra of super column matrices over the field 
Q under the natural product n.  
 
 
Define  : M  P by 
 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a




















 = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a




























; 
 
it is easily verified  is a linear transformation of super linear 
algebras.


## Page 259


259
Example 6.17:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

























 ai  Q; 1  i  18} 
 
be a super linear algebra of super matrices over the field Q 
under the natural product n.   
 
Let  
P = 
1
3
5
6
7
11
13
15
17
2
4
8
9
10
12
14
16
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a







 ai  Q; 
1  i  18} 
 
be a super linear algebra of super matrices over the field Q 
under natural product n. 
 
 
 
Define  : M  P by 
 
(
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a




















) =  
 
1
3
5
6
7
11
13
15
17
2
4
8
9
10
12
14
16
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a








## Page 260


260
 
 is a linear transformation from M to P. 
 
 
We now proceed onto define linear operator of super linear 
algebras of super matrices over the field F under natural product 
n. 
 
 
Example 6.18:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















 ai  Q; 1  i  20} 
 
be a super linear algebra of super matrices under the natural 
product n. 
 
 
Consider  : V  V defined by  
 
 (
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
















) = 
1
2
3
4
5
6
7
8
0
a
a
0
0
a
a
0
0
a
a
0
0
a
a
0
0
0
0
0
































. 
 
 is easily verified to be a linear operator on V.  Consider  
: V  V defined by  
 
 (
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
















) = 
1
11
2
10
3
9
4
8
5
6
7
7
a
0
0
a
a
0
0
a
a
0
0
a
a
0
0
a
a
a
a
a
































.


## Page 261


261
 is also a linear operator on V. 
 
Example 6.19:  Let  
 
V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a























 ai  Q; 1  i  21}  
 
be a super linear algebra of super column vectors defined over 
the field Q, under the natural product n. 
 
 
Define  : V  V 
 
by  (
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a






















) = 
1
2
3
4
5
6
7
8
9
10
11
12
a
a
a
0
0
0
a
a
a
0
0
0
a
a
a
0
0
0
a
a
a






















. 
 
 
 is a linear operator on V.   
 
We can also define linear function which is a matter of 
routine.  However we give examples of them. 
 
Example 6.20:  let V = {(x1 x2 | x3 | x4 x5 x6) | xi  Q; 1  i  6} 
be a super linear algebra of super row matrices over the field Q.  
Define f : V  Q such that f ((x1 x2 | x3 | x4 x5 x6)) = x1 + x2 + x6 
is a linear functional on V.


## Page 262


262
 
Example 6.21:  Let  
 
M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a























 ai  Q; 1  i  28} 
 
be a super linear algebra of super matrices over the field Q 
under the natural product n. 
 
 
Define f : M  Q by 
 
f  (
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a






















) = a1 + 3a3 + 9a27, 
 
f is a linear functional on M.   
 
Interested reader can develop other related properties as all 
properties can be derived with appropriate modifications 
provided the situation is feacible.  We can define super matrix 
coefficients polynomials  
 
 
Let 
S
R
F [x] = 
i
i
i 0
a x





ai  (x1 | x2 x3 | … | xn-1 xn)  M = 
{collection of all super row matrices of same type with entries


## Page 263


263
from Q or Z or R}.
S
R
F  [x] is defined as the super row matrix 
coefficient polynomials or polynomials in the variable x with 
row super matrix coefficients.   
 
We will illustrate this situation by an example. 
 
Example 6.22:  Let  
S
R
F [x] = 
i
ia x



ai  (x1 | x2 x3 | x4 x5 x6 | x7)  M 
 
= {all super row matrices of the type (x1 | x2 x3 | x4 x5 x6 | x7) 
with xj  R, 1  j  7}} be the polynomials with super row 
matrix coefficients. 
 
Example 6.23:  Let   
S
R
F  [x] = 
i
ia x



ai  (x1 | x2 | x3 | x4)  P = 
 
{all super row matrices of the form (x1 | x2 | x3 | x4) with xj  Z, 
1  j  4}} be the super row matrix coefficient polynomials.  
 
 
We will illustrate how a polynomial looks like, its degree 
and operations on them with super row matrix coefficients. 
 
 
Let p(x) = (3 | 2 | –7 | 2 0) + (7 | –4 | 0 | 3 1)x3 + (0 | 0 | 2 |  
–7 –9)x5 be a super row matrix coefficient polynomial.  Clearly 
degree of p(x) is 5.  
 
 
q(x) = (3 | 2 0) + (–7 | –2 9) x + (9 | 0 0)x2 + (0 | 3 1)x3 + (1 | 
1 1)x4 is a super row matrix coefficient polynomial in the 
variable x and degree of q(x) is four.  
 
 
Clearly 0(x) = (0 | 0 0) + (0 | 0 0)x + (0 | 0 0)x2 + … + (0 | 0 
0)xn.


## Page 264


264
 
Now we can add two polynomial with super row matrices if 
and only if all the coefficients are from the same type of super 
row matrices.  
 
 
Clearly we cannot add p(x) with q(x).  However q(x) + 0(x) 
can be added and q(x) + 0(x) = q(x). 
 
 
We will illustrate addition of two super matrix polynomials. 
 
 
Let m(x) = (1 1 | 0 2 3| 7 5 0 1) + (0 1 | 2 0 1 | 0 0 1 1) x + (0 
x | 1 0 0 | 8 0 0 5)x2 + (0 0 | 0 0 1 | 20 1 2)x3 and n(x) = (0 1 | 2 2 
2 | 3 1 2 0) + (6 2 | 0 0 0 | 2 1 0 0)x + (0 1 | 1 0 1| 0 2 0 1)x2 + (0 
4 | 4 2 –1 | 0 7 2 1)x3 + (1 2 | 0 1 4 | 3 0 1 4)x4 be two super row 
matrix coefficient polynomials in the variable x. 
 
 
m(x) + (n(x)) = (1 2 | 2 4 5 | 1 0 6 2 1) + (6 3 | 2 0 1| 2 1 1 
1)x + (0 9 | 2 0 1 | 8 2 0 6)x2 + (0 4 | 4 2 0 | 2 7 3 3)x3 + (1 2 | 0 1 
4 | 3 0 1 4)x4.  Thus we see addition of two super row matrix 
coefficient polynomials is again a polynomial with super row 
matrices coefficients.  Infact the set of super row matrix 
coefficient polynomials under addition is a group.  Further it is a 
commutative group under addition.   
 
We will give examples of such groups. 
 
Example 6.24:  Let 
S
R
F = 
i
i
i 0
a x





ai = (x1 | x2 | x3 x4 x5 | x6 x7) 
 {to the collection of all super row matrices of same type with 
entries from R}, +} be an abelian group of infinite order.  This 
has subgroups. 
 
Example 6.25:  Let 
S
R
F = 
i
i
i 0
a x





ai = (x1 x2 x3  x4 | x5 x6)  N  
 
= {all super row matrices of the same type as (x1 x2 x3 x4 | x5 x6) 
with entries from R}, +} be a group under addition.


## Page 265


265
Now we proceed onto give examples of super column 
matrix coefficient polynomials. 
 
 
p(x) = 
3
2
0
1
1
4
5











 + 
0
1
2
0
1
4
0











x + 
7
0
8
5
0
1
8











x3 + 
8
0
7
0
0
1
9











x4 + 
1
0
0
0
0
9
2











x6 
 
is a super column matrix coefficient polynomial of degree six. 
 
 
Consider q(x) = 
3
1
1
1
8








 + 
0
2
3
4
0








x + 
9
2
3
1
8

















x2 + 
1
2
3
4
0








x3 + 
9
2
3
4
9








x8  
 
is a column matrix coefficient polynomial of degree 8 in the 
variable x. 
 
 
Now we show how addition of column matrix coefficient 
polynomials are carried out in case of same type of column 
matrices.  For if these column matrices are different type 
certainly we cannot add any two column matrix coefficient 
polynomials.


## Page 266


266
 
Let p(x) = 
3
2
1
0
1
5










 + 
0
1
2
3
4
7










 x + 
2
0
1
0
0
8





















x2 + 
0
1
2
0
7
9










x3 + 
9
2
0
1
1
8










x5 and  
 
q(x) = 
9
0
1
2
5
0










  + 
8
7
0
0
7
6










x + 
1
2
2
9
0
7










x3 + 
9
0
1
2
7
8










x5. 
 
p(x) + q(x) = 
3
2
1
0
1
5










 + 
9
0
1
2
5
0










 + 
0
1
2
3
4
7











+
8
7
0
0
7
6


















x 
 
+ 
2
2
0
1
x
0
0
8









































+
0
1
2
0
7
9











+
1
2
2
9
0
7


















x3 + 
9
2
0
1
1
8











+
9
0
1
2
7
8


















x5


## Page 267


267
 
 
= 
12
2
2
2
6
5




















 + 
8
8
2
3
12
13




















x + 
2
0
1
0
0
8





















 x2 + 
1
3
4
9
7
16




















x3 + 
18
2
1
3
8
16




















x5. 
 
This is the way addition of super column matrix coefficient 
polynomials are added.  Thus addition is performed.  Infact the 
collection of all super column matrix coefficient polynomials 
with same type of super column matrix coefficients is an abelian 
group under addition.   
 
We shall illustrate this situation by some simple examples. 
 
 
Example 6.26:  Let 
S
C
F [x] = 
1
2
3
i
4
i 0
5
6
7
a
a
a
a
x
a
a
a




































 with 
1
2
3
4
5
6
7
a
a
a
a
a
a
a






















  M  
 
 
= {collection of all super column matrices of the same type with 
ai  Z, 1  i  7}} be an abelian group of super column matrix 
coefficient polynomials in the variable x.


## Page 268


268
Example 6.27:  Let 
S
C
F [x] = 
i
i
i 0
a x





ai = 
1
2
3
4
5
6
x
x
x
x
x
x




















  M = {
1
2
3
4
5
6
x
x
x
x
x
x




















  
 
with xj  Z, 1  j  6}, +} be an abelian group under addition. 
 
Example 6.28:  Let  
 
S
3 5
F  = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d










  M = 
 
{all 3  5 matrices with entries from Z, dj  Z; 1  j  15}} be 
an abelian group under addition. 
 
Example 6.29:  Let 
S
4 4
F  = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x












  
 
with xj  Q; 1  j  16} be an abelian group under addition.  
Clearly we see 
S
4 4
F  has subgroups.   
 
P = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
p
p
p
p
p
p
p
p
p
p
p
p
p
p
p
p












 with pj  Z, 
 
1  j  16}


## Page 269


269
 
is a subgroup of G under addition. 
 
 
Now we proceed onto give the semigroup structure under 
the natural product n. 
Let 
S
C
F  = 
i
i
i 0
a x





ai = 
1
2
20
x
x
x















 with xj  Z, 1  j  20} 
 
be the collection of super column matrix coefficient polynomial.  
S
C
F  is a semigroup under the natural product n.   Infact 
S
C
F  is a 
commutative semigroup. 
 
 
Suppose  
 
p(x) = 
1
2
20
a
a
a















 + 
1
2
20
b
b
b















x + 
1
2
20
c
c
c















x3 and 
 
q(x) = 
1
2
20
d
d
d















 + 
1
2
20
e
e
e















x2 + 
1
2
20
m
m
m















x4 
 
are in 
S
C
F , then


## Page 270


270
p(x) n q(x) = 
1
1
2
2
20
20
a d
a d
a d















 + 
1
1
2
2
20
20
b d
b d
b d















 x + 
1 1
2
2
20
20
a e
a e
a e















x2 + 
1 1
2
2
20
20
b e
b e
b e















x3 
 
          + 
1
1
2
2
20
20
c d
c d
c d















x3 + 
1
1
2
2
20
20
a m
a m
a m















x4 + 
1 1
2
2
20
20
c e
c e
c e















x5 + 
1
1
2
2
20
20
c m
c m
c m















x7 
 
+ 
1
1
2
2
20
20
b m
b m
b m















x5 
 
= 
1
1
2
2
20
20
a d
a d
a d















 + 
1
1
2
2
20
20
b d
b d
b d















x + 
1 1
2
2
20
20
a e
a e
a e















x2 + 
1 1
1
1
2
2
2
2
m
m
m
m
b e
c d
b e
c d
b e
c d


















x3  
 
+ 
1
1
2
2
20
20
a m
a m
a m















x4 + 
1 1
1
1
2
2
2
2
20
20
20
20
c e
b m
c e
b m
c e
b m


















x5 + 
1
1
2
2
20
20
c m
c m
c m















x7 is in 
S
C
F . 
 
This way the natural product n is made on 
S
C
F .   
 
We illustrate this situation by some examples.


## Page 271


271
Example 6.30:  Let  
 
S
3 6
F  = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x










; xj  Z; 
1  j  18} 
 
be a super 3  6 matrix coefficient polynomial semigroup under 
the natural product n. 
 
Example 6.31:  Let  
 
S
3 3
F  = 
i
i
i 0
a x





ai = 
1
2
3
4
5
6
7
8
9
x
x
x
x
x
x
x
x
x










 where xj = Q; 1  j  9} 
 
be a suepr square matrix coefficient semigroup under natural 
product n. 
 
Let  
p(x) = 
3
2
0
1
0
1
0
2
3










 + 
7
5
1
0
1
2
0
0
3










x + 
1
2
3
0
0
7
0
1
2










x2 
 
+ 
0
0
9
1
0
3
2
7
2










x4 
and  
 
q(x) = 
4
0
2
1
5
6
7
0
2










 + 
1
2
3
4
5
6
7
8
9










x2 + 
0
3
1
2
1
0
3
4
5










x3


## Page 272


272
be in 
S
3 3
F . 
 
 
To find  
p(x) n q(x); p(x) n q(x) = 
3
2
0
1
0
1
0
2
3










 n 
4
0
2
1
5
6
7
0
2










 
 
+ 
3
2
0
1
0
1
0
2
3










 n 
1
2
3
4
5
6
7
8
9










x2 + 
3
2
0
1
0
1
0
2
3










 n 
0
3
1
2
1
0
3
4
5










x3 
 
+ 
7
5
1
0
1
2
0
0
3










 n 
4
0
2
1
5
6
7
0
2










x + 
7
5
1
0
1
2
0
0
3










 n 
1
2
3
4
5
6
7
8
9










x3 
 
+ 
7
5
1
0
1
2
0
0
3










n 
0
3
1
2
1
0
3
4
5










x4 + 
1
2
3
0
0
7
0
1
2










n
4
0
2
1
5
6
7
0
2










x2 
 
+ 
1
2
3
0
0
7
0
1
2










n 
1
2
3
4
5
6
7
8
9










x4 + 
1
2
3
0
0
7
0
1
2










n
0
3
1
2
1
0
3
4
5










x5  
 
+ 
0
0
9
1
0
3
2
7
2










 n 
4
0
2
1
5
6
7
0
2










x4 + 
0
0
9
1
0
3
2
7
2










n  
1
2
3
4
5
6
7
8
9










x6 
+ 
0
0
9
1
0
3
2
7
2










 n 
0
3
1
2
1
0
3
4
5










 n x7


## Page 273


273
 
= 
12
0
0
1
0
6
0
0
6










 + 
3
4
0
4
0
6
0
16
27










x2 + 
0
6
0
2
0
0
0
8
15










x3 
 
+ 
28
0
2
0
5
12
0
0
6










x + 
7
10
3
0
5
12
0
0
27










x3 + 
0
15
1
0
1
0
0
0
15










x4 
 
+ 
1
4
9
0
0
42
0
8
18










x4 + 
0
6
3
0
0
0
0
4
10










x5 + 
0
0
18
1
0
18
14
0
4










x4 
 
+ 
0
0
27
4
0
18
14
56
18










x6 + 
0
0
9
2
0
0
6
28
10










x7 + 
4
0
6
0
0
42
0
0
4










x2 
 
 
= 
12
0
0
1
0
6
0
0
6










 + 
28
0
2
0
5
12
0
0
6










x + 
7
4
6
4
0
48
0
16
31










x2 +  
 
7
16
3
2
5
12
0
8
42










x3 + 
1
19
28
1
1
56
14
8
37










x4 + 
0
6
3
0
0
0
0
4
10










x5 
 
+ 
0
0
27
4
0
18
14
56
18










x6 + 
0
0
9
2
0
0
6
28
10










x7.


## Page 274


274
 
 
 
Thus we see 
S
3 3
F [x] under natural product n is a 
semigroup.  This semigroup has zero divisors and ideals.  We 
can derive all related properties of this semigroup as a matter of 
routine. 
 
 
Now we can also give these super matrix coefficient 
polynomials a ring structure.  We just recall if 
S
C
F [x] be a super 
column matrix polynomials, we know 
S
C
F [x] under addition is 
an abelian group and under the natural product n, 
S
C
F [x] is a 
semigroup.  Thus it is easily verified (
S
C
F [x], +, n) is a 
commutative ring known as the super column matrix coefficient 
ring.  
 
 
We will illustrate this situation by some simple examples.  
 
Example 6.32:  Let  
 
S
C
F  [x] = 
i
i
i 0
a x





ai = 
1
2
3
4
5
6
x
x
x
x
x
x




















 with xj  Z, 1  j  6} 
 
be the super column matrix coefficient polynomial ring under + 
and n.


## Page 275


275
Example 6.33:  Let (
S
C
F  [x], +, n) = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
d
d
d
d
d
d
d
d


























 with 
dj  Q; 1  j  8, +, n} be the super column matrix coefficient 
polynomial ring of infinite order.  
S
C
F [x] has subrings which are 
not ideals, has zero divisors and idempotents only of a very 
special form which are only constant polynomials.  
 
 
For instance  = 
1
0
0
1
1
1
0
1













   
S
C
F  [x] is such that 2 = . 
 
Similarly  = 
0
1
1
1
1
1
1
0













  
S
C
F  [x] is such that 2 = .


## Page 276


276
 
Further we see P = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
x
x
x
x
x
x
x
x


























 with xj  3Z,  
 
1  j  8, +, n}  
S
C
F [x] is a subring of super column matrix 
coefficient polynomial ring.  However P is not an ideal of 
S
C
F  
[x]. 
 
 
However 
S
C
F  [x] has infinite number of zero divisors.   
 
Example 6.34:  Let 
S
C
F  [x] = 
i
i
i 0
a x





 ai = 
1
2
3
d
d
d










 with dj  Zn, 
n, +, 1  j  3} be a super column matrix coefficient 
polynomial ring.   
 
Consider p(x) =  
1
2
0
a
a










 + 
1
2
0
b
b










x + 
1
2
0
c
c










x2, 
 
q(x) = 
1a
0
0










 + 
1b
0
0










x + 
1d
0
0










x3 + 
1x
0
0










x4  
S
C
F  [x].


## Page 277


277
Clearly p(x) n q(x) = 
0
0
0





. 
 
 
Further if  
P = 
i
i
i 0
a x





 ai = 
1
2
x
0
x










 with x1, x2  Z, +, n}  
S
C
F  [x] 
is a subring. 
 
Also T = 
i
i
i 0
a x





 ai = 
1
0
y
0










, y1  Z, +, n}  
S
C
F [x] 
 
is a subring.   
 
We see 
S
C
F  [x] =  
 
P + T and P  T =  
0
0
0





. 
 
Further for every   P we have every   T is such that  
 
 n  =  
0
0
0





. 
We see both P and T are also ideals of 
S
C
F . 
 
 
Now we proceed onto define super row matrix coefficient 
polynomial ring.  Consider {
S
R
F [x], +, n} is a super row matrix


## Page 278


278
coefficient polynomial ring which is commutative and of 
infinite order. 
 
 
We will give examples of it. 
 
Example 6.35:  Let R = {
S
R
F [x] = 
i
i
i 0
a x


; ai = (t1 t2 t3 | t4 | t5 t6); 
tj  Z, 1  j  6, +, n} be a super row matrix polynomial 
coefficient ring.  R has zero divisors, units, ideals and subrings. 
 
P = 
i
i
i 0
a x





 ai = (0 0 0 | d1 | d2 d3) d1, d2, d3  Z, +, n}  R 
is a subring  as well as an ideal of R. 
 
T = 
i
i
i 0
a x





 ai = (y1 y2 y3 | 0 | 0  0) y1, y2, y3  Z, +, n}  R 
is a subring as well as an ideal of R.  
 
 
We see every a  P and every b  T are such that a n b = 
(0 0 0 | 0 | 0 0). 
 
 
Also (1 –1 1 | –1 | –1 1) = p is such that p2 = (1 1 1 | 1 | 1 1), 
only units of this form are in R. 
 
Example 6.36:  Let 
S
R
F [x] = 
i
i
i 0
a x





 ai = (p1 p2 | p3 | p4 p5 | p6 
| p7 p8 | p9) with pj  Q; 1  j  9, +, n} be the super row matrix 
coefficient ring of polynomials.  Clearly 
S
R
F [x] has ideals, 
subrings which are not ideals and zero divisors. 
 
 
For take M = 
i
i
i 0
a x





 ai = (d4 0 | 0 | 0 0 | d5 | d1 d2 | d3) 
with dj  Q; 1  j  5, +, n}  
S
R
F [x]; M is an ideal.  Consider


## Page 279


279
T = 
i
i
i 0
a x





 ai = (y1 y2 | y3 | y4 y5 | y6 | y7 y8 y9) with yj  Z; 1 
 j  9, +, n}  
S
R
F [x]; T is a only a subring and not an ideal of 
S
R
F [x]. 
 
 
It is easily verified 
S
R
F [x] has zero divisors. 
 
Example 6.37:  Let 
S
R
F [x] = 
i
i
i 0
a x





 ai = (m1 | m2); m1, m2  
R, +, n} be a super row matrix coefficient polynomial ring.  
Clearly 
S
R
F [x] has units, zero divisors, idempotents all of them 
are only constant polynomials.  For  = (1 | –1) is a unit as 2 = 
(1 | 1) and  = (0 | 1) and b1 = (1 | 0) are all idempotents.  We 
also see P = 
i
i
i 0
a x





 ai = (t | s), t, s,  Z, +, n}  
S
R
F [x] is a 
subring and not an ideal of 
S
R
F [x]. 
 
 
Take M = 
i
i
i 0
a x





ai = (t | 0); t  R, +, n}  
S
R
F [x] is an 
ideal of 
S
R
F [x].  N = 
i
i
i 0
a x





 ai = (0 | s) s  R, +, n}  
S
R
R [x] is also an ideal of 
S
R
F [x].  Every  in M and every  in 
M are such that n = (0 | 0). 
 
 
Next we proceed onto describe the concept of super matrix 
coefficient polynomial rings. 
 
 
Let 
S
m n
F [x] = 
i
i
i 0
a x





 ai = (mij), m  n super matrices of 
same type of every ai and 1  i  m and 1  j  n with m  n and 
mij  Z (or Q or R), +, n} be the super matrix coefficient 
polynomial ring.


## Page 280


280
 
 
We will illustrate this by some examples. 
 
Example 6.38:  Let {
S
2 4
F [x], +, n} = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
d
d
d
d
d
d
d
d






 dj  z, 1  j  8, +, n} be the super row 
vector coefficient polynomial ring.  
S
2 4
F  has zero divisors, units, 
idempotents ideals and subrings. 
 
 
 = 
1
1
1
1
1 1
1
1










 is such that 2 = 1 1 1 1
1 1 1 1






 is a 
unit.   
 
Consider  = 1
0
1
1
0
1
0
0






 in 
S
2 4
F  [x].  We see 2 =  so 
 is an idempotent in 
S
2 4
F [x] only if it is a constant polynomial 
and the super row vector takes its entries only as 0 or 1. 
 
 
Similarly an element a  
S
2 4
F [x] is a unit only if a is a 
constant polynomial and all its entries are from the set {–1, 1}.  
Consider  
 
P = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
t
t
t
t
t
t
t
t






; tj  5Z, 
1  j  8, +, n} 
 
is a subring which is also an ideal of 
S
R
F [x].


## Page 281


281
Example 6.39:  Let  
{
S
5 3
F [x], +, n} = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
















 with yj  Q,  
 
1  j  15, n, +} 
 
be the super column vector coefficient polynomial ring.  
S
5 3
F [x] 
has subrings which are not ideals, ideals, units, zero divisors 
and idempotents. 
 
 
Consider M = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
















 with mj  
z, 1  j  15, +, n}  
S
5 3
F [x]  
 is only a subring and not an ideal of 
S
5 3
F [x].   
 
Take p = 
1
0
1
1
1
1
0
0
1
1
1
1
0
0
1
















 in 
S
5 3
F [x] is such that p2 = p, that is an 
idempotent.  All idempotents are only constant polynomials that 
is 5  3 super column vectors.


## Page 282


282
Consider t = 
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
























 in 
S
5 3
F  [x]. 
We see t2 = 
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
















 the unit; that t is a unit. 
 
Suppose y   
S
5 3
F  [x] is to be a unit then we see it should be 
a constant polynomial and the 5  3 matrix must take its entries 
from the set {1, –1}. 
 
Example 6.40:  Let  
 
S
5 4
F [x] = 
i
i
i 0
a x





 ai = 
1
6
11
16
2
7
12
17
3
8
13
18
4
9
14
19
5
10
15
20
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
















  
 
with mj  Z; 1  j  20; +, n} 
 
be the super matrix coefficient polynomial ring.


## Page 283


283
 
Take M = 
i
i
i 0
a x





 ai = 
1
6
11
16
2
7
12
17
3
8
13
18
4
9
14
19
5
10
15
20
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
















  
 
with mj  5Z, 1  j  20, +, n}  
S
5 4
F [x];  
M is an ideal of 
S
5 4
F [x].   
Suppose  
P = 
i
i
i 0
a x





ai = 
1
9
3
4
5
6
7
8
2
10
m
0
0
m
0
m
m
0
0
m
m
0
0
m
m
0
m
0
0
m
















  
 
with mj  3Z, 1  j  10, +, n}  
S
5 4
F [x] 
 
be an ideal of 
S
5 4
F [x]. 
 
Take T = 
i
i
i 0
a x





ai = 
4
5
1
7
2
8
3
9
10
6
0
m
m
0
m
0
0
m
m
0
0
m
m
0
0
m
0
m
m
0
















 mj  13Z; 
 
1  j  10, +, n}  
S
5 4
F [x] 
 
be an ideal, we see for every  in P is such that for every  in


## Page 284


284
T  n  = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















. 
 
 
However P  T = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















 but P  T  
S
3 4
F [x]. 
 
Example 6.41:  Let  
S
5 7
F [x] = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
















 with mj  Q;  
 
1  j  35, +, n} 
 
be the super matrix coefficient polynomial ring 
S
5 7
F [x] has zero 
divisors, units, idempotents, ideals and subrings which are not 
ideals.


## Page 285


285
 
m = 
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1































 in 
S
5 7
F [x]  
 
is such that  
 
m2 = 
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
















  
S
5 7
F [x].   
 
Further if p =
1
0
0
1
0
1
1
0
1
1
0
1
0
0
0
1
1
0
0
1
1
1
0
1
0
1
0
1
1
1
1
1
0
1
0
















  
S
5 7
F [x],  
 
then p2 = p is an idempotent of 
S
5 7
F [x].


## Page 286


286
 
Take  
P = 
i
i
i 0
a x





 ai = 
1
6
11
2
7
12
3
8
13
4
9
14
5
10
15
m
0
0
m
0
m
0
m
0
0
m
0
m
0
m
0
0
m
0
m
0
m
0
0
m
0
m
0
m
0
0
m
0
m
0
















 with  
 
mj  Z; 1  j  15, +, n} 
 
to be a subring and not an ideal of 
S
5 7
F [x]. 
 
 
Take  
S = 
i
i
i 0
a x





ai = 
1
2
11
16
3
4
12
17
5
6
13
18
7
8
14
19
9
10
15
20
0
m
m
0
m
0
m
0
m
m
0
m
0
m
0
m
m
0
m
0
m
0
m
m
0
m
0
m
0
m
m
0
m
0
m
















 
 
with mj  Q; 1  j  20, +, n} is an ideal of 
S
5 7
F  [x]. 
 
 
We see every polynomial p(x)  P is such that for every  
 
q(x)  S we have p(x) n q(x) = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
















. 
 
 
Now we describe the super square matrix coefficient 
polynomial ring.


## Page 287


287
 
Let 
S
m m
F [x] be the collection of a super square matrix 
coefficient polynomial ring under + and n.  We will illustrate 
this by some examples. 
 
Example 6.42: Let  
S
4 4
F [x] = 
i
i
i 0
a x





ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m












;  
 
mj  Z, 1  j  16, +, n} 
 
be the super square matrix coefficient polynomial ring.  
S
4 4
F  [x] 
has zero divisors units, idempotents, ideals and subrings. 
 
 
Take  = 
1
1 1
1
1
1
1
0
1
0
1
0
0
1
1
1















  
S
4 4
F [x], we see 2   and  
is not a unit.   
 
Take  = 
1 1
1
1
1 1
1
1
1
1
1
1
1
1
1
1

















  
S
4 4
F  [x]; 
 
2 = 
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1












.


## Page 288


288
 
Take p = 
1
0
1
1
0
1
0
1
1
0
1
0
1
1
0
0












 in 
S
4 4
F  [x]; we see p2 = p is an 
idempotent.   
 
 
Now S = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
d
0
d
0
0
d
0
d
d
0
d
0
0
d
0
d












, dj  Z,  
 
1  j  8}  
S
4 4
F  [x] is an ideal of 
S
4 4
F  [x]. 
 
 
M = 
i
i
i 0
a x





 ai = 
1
2
8
3
4
5
6
7
0
d
0
d
d
0
d
0
0
d
0
d
d
0
d
0












 with dj  Z; 1  j  
8, + , n}  
S
4 4
F [x] is also an ideal of 
S
4 4
F  [x].  We see every 
polynomial p(x) is S is such that for every polynomial q(x) in M  
 
we have p(x) n q(x) = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0












. 
 
 
Now we have the following theorems, the proofs of which 
are left as an exercise to the reader. 
 
THEOREM 6.1:  Let 
S
C
F  [x] (or 
S
R
F [x] or 

S
m n
F
[x] (m  n) or 

S
n n
F
[x]) be super matrix coefficient polynomial ring.


## Page 289


289
1. 
Every constant polynomial with entries from the set 
{1, –1} is a unit under n. 
2. 
Every constant polynomial with entries from the set 
{0, 1} is an idempotent under n. 
 
THEOREM 6.2:  Every super matrix coefficient polynomial ring 
has ideals. 
 
THEOREM 6.3:  Every super matrix coefficient polynomial ring 
over Q or R has subrings which are not ideals. 
 
THEOREM 6.4:  Every super matrix coefficient polynomial ring 
has infinite number of zero divisors. 
 
Now we can define super vector space of polynomials over 
R or Q. 
 
Suppose we take V = 
S
C
F [x] to be an abelian group under 
addition.  V is a vector space over the reals or rationals.   
 
We will give examples of them.  
 
Example 6.43:  Let  
V = {
S
C
F [x] = 
i
i
i 0
a x


 with ai = 
1
2
3
4
5
t
t
t
t
t
















; tj  Q, 1  j  5, +} 
 
be a vector space over Q.  V is called the super column matrix 
coefficient polynomial vector space or super polynomial vector 
space over Q.


## Page 290


290
Example 6.44:  Let  
 
V = {
S
C
F [x] = 
i
i
i 0
a x


 with ai = 
1
2
3
t
t
t










; tj  Q, 1  j  3, +} 
 
be an abelian group under ‘+’.  V is a super column matrix 
coefficient polynomial vector space over Q. 
 
P1 = 
i
i
i 0
a x





 ai = 
1t
0
0





; t1  Q, +}  V 
is a subspace of V over Q. 
 
P2 =  
i
i
i 0
a x





 ai = 
2
0
t
0










; t2  Q, +}  V 
 
is a subspace of V over Q. 
   P3 =  
i
i
i 0
a x





 ai = 
3
0
0
t










; t3  Q, +}  V 
is a subspace of V over Q. 
 
 
We see V = P1 + P2 + P3 and  
 
Pi  Pj = 
0
0
0





 if i  j; 1  i, j  3. 
 
 
Thus V is a direct sum of subspaces P1, P2 and P3 over Q.


## Page 291


291
 
Example 6.45:  Let  
 
M = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
m
m
m
m
m
m
m






















; mj  Q; 1  j  7, +} 
 
be a super column matrix coefficient polynomial group under 
‘+’. 
 
M is a super column matrix coefficient vector space over Q. 
 
Take  
      P1 = 
i
i
i 0
a x





 ai = 
1
2
3
m
m
0
0
0
0
m






















, m1, m2, m3  Q, +}  M, 
 
P2 = 
i
i
i 0
a x





 ai = 
1
2
3
4
m
0
m
m
0
0
m






















 with mj  Q, 1  j  4, +}  M 
and


## Page 292


292
P3 = 
i
i
i 0
a x





 ai = 
1
2
3
4
m
0
0
0
m
m
m






















 with mj  Q, 1  j  4}  M. 
 
 
Clearly M  P1 + P2 + P3 but Pi  Pj  
0
0
0
0
0
0
0











 if i  j,  
1  i, j  3.  P1, P2 and P3 are subspaces of M over Q.  Clearly M 
is the pseudo direct sum of vector subspaces of M.  
 
Example 6.46:  Let  
 
V = 
i
i
i 0
a x





  ai = (d1 | d2 | d3 d4 d5 d6 d7 | d8); dj  Q,  
1  j  8} 
 
be a super row matrix coefficient polynomial vector space over 
Q.   
 
Consider  
 
P1 = 
i
i
i 0
a x





 ai = (0 | 0 | d1, d2, 0, 0, 0 | 0), d1, d2  Q}  V,


## Page 293


293
P2 = 
i
i
i 0
a x





 ai = (d1 | d2 | 0, 0, 0, 0, 0 | 0), d1, d2  Q}  V, 
 
P3 = 
i
i
i 0
a x





 ai = (0 | 0 | 0 0 d1 d2 0 | 0); d1, d2  Q}  V 
 
and  
 
P4 = 
i
i
i 0
a x





 ai = (0 | 0 | 0 … 0 d1 | d2) with d1, d2  Q}  V 
 
be a super row matrix coefficient polynomials subvector space 
of V over Q. 
 
 
Clearly V = P1 + P2 + P3 + P4 and  
 
Pi  Pj = ( 0 | 0 | 0 0 0 0 0 | 0) if i  j, 1  i, j  4. 
 
 
Clearly V is a direct sum of subspaces. 
 
Example 6.47:  Let  
 
V = 
i
i
i 0
a x





 ai = (t1 t2 | t3 t4 | t5); tj  Q, 1  j  5} 
 
be the super row matrix coefficient polynomial vector space 
over Q.   
 
Take  
 
M1 = 
i
i
i 0
a x





 ai = (0 t1 | t2 0 | 0), t1, t2  Q}  V,


## Page 294


294
M2 = 
i
i
i 0
a x





 ai = (t1, t2 | 0 0 | 0), t1, t2  Q}  V, 
 
M3 = 
i
i
i 0
a x





 ai = (0 t1 | 0 t2 | 0), t1, t2  Q}  V 
and 
M4 = 
i
i
i 0
a x





 ai = (0 t1 | 0 0 | t2), t1, t2  Q}  V 
be super row matrix coefficient polynomial vector subspace of 
V over Q.  We see V  M1 + M2 + M3 + M4, however  
Mi  Mj  (0 0 | 0 0 | 0) if i  j; 1  i, j  4. 
 
 
Thus V is only a pseudo direct sum of vector subspaces 
over Q. 
 
Example 6.48:  Let  
 
V = 
i
i
i 0
a x





ai = (m1 | m2 m3 m4 | m5 m6 | m7)  
with mj  R; 1  j  7} 
 
be a super row matrix coefficient polynomial vector space over 
Q. 
 
 
Consider  
 
M1 = 
i
i
i 0
a x





 ai = (0 | m1 0 m2 | 0 m3 | 0)  
with m1, m2, m3  R}  V 
 
and  
M2  = 
i
i
i 0
a x





 ai = (m1 | 0 m2 0 | m3 0 | m4)  
with m1, m2, m3, m4  R}  V


## Page 295


295
 
to be super row matrix coefficient polynomial vector subspaces 
of V over Q. 
 
 
 
We see V = M1 + M2 and M1  M2 = ( 0 | 0 0 0 | 0 0 | 0). 
 
 
 
Infact we see every q(x)  M1 is orthogonal with every 
other p(x)  M2. 
 
 
 
Thus M1 is the orthogonal complement of M2 and vice 
versa. Now we give examples of super m  n matrix coefficient 
polynomial vector spaces over Q or R. 
 
 
 
Example 6.49:  Let  
 
V = 
i
i
i 0
a x





 ai = 
1
4
7
10
13
16
2
5
8
11
14
17
3
6
9
12
15
18
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d










 with dj  Q,.  
 
1  j  18} 
 
be the super 3  7 row vector coefficient polynomial vector 
space over Q.


## Page 296


296
 
 
Example 6.50:  Let  
W = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
































  
 
with mj  R, 1  j  40} 
 
be a super column vector coefficient polynomial vector space 
over Q. 
 
Example 6.51: Let  
V = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m






















 
 
with mj  Q, 1  j  35} 
 
be a super 7  5 matrix coefficient polynomial vector space over 
Q.


## Page 297


297
Now we see for all these one can easily find a basis 
subspaces etc.  
 
Example 6.52:  Let  
 
V = 
i
i
i 0
a x





 ai =  
 
1
8
15
22
29
36
43
50
2
9
16
23
30
37
44
51
3
10
17
24
31
38
45
52
4
11
18
25
32
39
46
53
5
12
19
26
33
40
47
54
6
13
20
27
34
41
48
55
7
14
21
28
35
42
49
56
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m






















 with  
 
mj  Q, 1  j  56} 
be a super 7  8 matrix coefficient polynomial vector space over 
Q.  Consider  
 
M1 = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
m
0
0
0
0
0
0
0
m
0
0
0
0
0
0
0
m
0
0
0
0
0
0
0
m
0
0
0
0
0
0
0
m
0
0
0
0
0
0
0
m
0
0
0
0
0
0
0
m
0
0
0
0
0
0
0






















  
 
with mj  Q, 1  j  7} V,


## Page 298


298
M2  = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0






















  
 
with mj  Q, 1  j  14}  V, 
 
M3 = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
0
0
0
m
m
m
0
0
0
0
0
m
m
m
0
0
0
0
0
m
m
m
0
0
0
0
0
m
m
m
0
0
0
0
0
m
m
m
0
0
0
0
0
m
m
m
0
0
0
0
0
m
m
m
0
0






















  
 
with mj  Q, 1  j  21}  V  
and 
M4 = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m
0
0
0
0
0
0
m
m






















  
 
with mj  Q, 1  j  14}  V. 
 
Clearly M1, M2, M3 and M4 are super matrix coefficient 
polynomial vector subspaces of V and M1 + M2 + M3 + M4 and


## Page 299


299
 
Mi  Mj = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0






















, 1  i, j  4.   
 
Thus V is the direct sum of subspaces. 
 
Example 6.53:  Let  
 
P = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m












  
 
with mi  R, 1  j  28} 
 
be a 4  7 super row vector matrix coefficient polynomial vector 
space over Q. 
Let B1 = 
i
i
i 0
a x





 ai = 
1
5
2
6
3
7
4
8
m
m
0
0
0
0
0
m
m
0
0
0
0
0
m
m
0
0
0
0
0
m
m
0
0
0
0
0












; 
 
mi  Q, 1  i  8}  P,


## Page 300


300
B2 = 
i
i
i 0
a x





 ai = 
1
5
2
6
3
7
4
8
m
0
m
0
0
0
0
m
0
m
0
0
0
0
m
0
m
0
0
0
0
m
0
m
0
0
0
0












;  
 
mi  Q, 1  i  8}  P, 
 
B3 = 
i
i
i 0
a x





 ai = 
1
5
2
6
3
7
4
8
m
0
0
m
0
0
0
m
0
0
m
0
0
0
m
0
0
m
0
0
0
m
0
0
m
0
0
0












;  
 
mi  Q, 1  i  8}  P, 
 
B4 = 
i
i
i 0
a x





 ai = 
1
5
2
6
3
7
4
8
m
0
0
0
m
0
0
m
0
0
0
m
0
0
m
0
0
0
m
0
0
m
0
0
0
m
0
0












;  
 
mi  Q, 1  i  8}  P, 
 
B5 = 
i
i
i 0
a x





 ai = 
1
5
2
6
3
7
4
8
m
0
0
0
0
m
0
m
0
0
0
0
m
0
m
0
0
0
0
m
0
m
0
0
0
0
m
0












;  
 
mi  Q, 1  i  8}  P  
and


## Page 301


301
B6 = 
i
i
i 0
a x





 ai = 
1
5
2
6
3
7
4
8
m
0
0
0
0
0
m
m
0
0
0
0
0
m
m
0
0
0
0
0
m
m
0
0
0
0
0
m












;  
 
mi  Q, 1  i  8}  P 
 
be super matrix coefficient polynomial subspaces of P over the 
field Q.  
 
 
Clearly Bi  Bj  0, if i  j, 1  i, j  6. 
 
 
Also P  B1 + B2 + … + B6 so P is a pseudo direct sum of 
vector subspaces B1, B2, …, B6.  
 
 
We can define orthogonal subspaces and orthogonal 
complements also. 
 
Example 6.54:  Let  
 
V = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
m
m
m
m
m
m
m
m


























 with mi  Q, 1  i  8} 
 
be a super column matrix coefficient polynomial vector space 
over the  field Q.


## Page 302


302
 
Consider  
M1 = 
i
i
i 0
a x





ai = 
1
2
m
m
0
0
0
0
0
0


























 with m1, m2  Q}  V 
 
is a vector subspace of V over Q. 
 
M2 =   
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
0
0
m
m
m
m
m
m


























 with mi  Q; 1  i  6}  V 
 
is a vector subspace of V over Q.  Clearly 
1
M = M2 and vice 
versa.


## Page 303


303
 
Consider  
M3 = 
i
i
i 0
a x





 ai = 
1
2
3
0
0
m
m
m
0
0
0


























, m1, m2, m3  Q}  V, 
 
M3 is also a vector subspace of V over Q and for every x  M1 
and for every y  M3 we see x n y = (0) however 
1
M  M3 for 
M1 + M3  V however M1 + M2 = V and 
1
M = M2 and 
2
M = 
M1. 
 
 
Thus we see we can have subspaces in V orthogonal to M1 
but they need not be the orthogonal complement of M, in V 
over Q. 
 
 
Now we proceed onto define semivector space of super 
matrix coefficient polynomials defined over the semifield Z+  
{0} or Q+  {0} or R+  {0}.   
 
We just describe them in the following.  
 
 
Let P = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
d
d
d
d
d
















 with dj  Z+  {0}; 1  j  5} 
be a semigroup under addition known as the super column 
matrix coefficient polynomial semigroup.  P is a semivector 
space over the semifield S = Z+  {0}.


## Page 304


304
 
W = 
i
i
i 0
a x





 ai = (m1 | m2 | m3 m4) with mj  Q+  {0},  
1  j  4} is a super column matrix coefficient polynomial 
semivector space over the semifield S = Q+  {0} (or Z+  
{0}). 
 
 
T = 
i
ia x



ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d






























 with dj  R+  {0},  
1  j  27}  is a super column vector coefficient polynomial 
semivector space over the semifield S = Z+  {0} (or Q+  {0} 
or R+  {0}). 
 
 
M = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
t
t
t
t
t
t
t
t
t
t
t
t
t
t
t
t
t
t
t
t
t










 ti  
Q+  {0}, 1  i  21} is the super row vector coefficient 
polynomial semivector space over the semifield S = Q+  {0} 
or Z+  {0}.  However M is not a semivector space over R+  
{0}. 
B = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y
y












  
 
yi  Z+  {0}, 1  i  32}


## Page 305


305
 
is a super 4  8 matrix coefficient polynomial semivector space 
over the semifield Z+  {0}. 
 
C = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m




















  
 
mj  Z+  {0}, 1  i  36} 
 
is a super square matrix coefficient polynomial semivector 
space over the semifield Z+  {0}.   
 
The authors by examples show how subsemivector space 
direct sum etc looks like. 
 
 
Example 6.55:  Let  
 
M = 
i
i
i 0
a x





ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m










  
mj  Q+  {0}, 1  i  24} 
 
be a super row vector polynomial coefficient semivector space 
defined over the semifield Z+  {0}.  M is a semilinear algebra 
under the natural product.


## Page 306


306
 
Consider  
p(x) = 
8
0
1
7
0
3
8
1
0
0
2
0
8
1
0
1
1
5
0
1
0
0
0
1










 +  
 
6
7
0
1
6
0
9
1
0
9
1
2
0
1
6
2
2
0
2
8
1
1
7
3










x +  
 
1
0
1
8
1
2
0
7
1
2
4
0
3
2
0
0
2
0
3
1
1
0
0
2










x2  
 
and 
 
q(x) =  
0
1
2
1
0
5
7
2
2
0
1
3
7
0
5
1
1
4
8
1
0
0
4
0










 +  
 
            
2
8
1
3
4
3
3
1
1
0
5
0
1
2
2
2
0
1
4
6
0
0
1
3










x2 +  
 
0
0
1
3
0
0
6
2
7
2
0
0
1
0
0
1
0
0
0
0
0
1
1
0










x3 be in M.  p(x).q(x)  M. 
 
T = 
i
i
i 0
a x





 ai = 
1
2
7
10
3
4
8
11
5
6
9
12
0
m
m
0
0
0
m
m
0
m
m
0
0
0
m
m
0
m
m
0
0
0
m
m










 
mi  Q+  {0}, 1  i  12}  M


## Page 307


307
and  
 
P = 
i
i
i 0
a x





 ai = 
1
4
5
6
2
7
8
9
3
10
11
12
m
0
0
m
m
m
0
0
m
0
0
m
m
m
0
0
m
0
0
m
m
m
0
0










 
mi  Q+  {0}, 1  i  12}  M, 
 
T and P are super row vector polynomial coefficient semivector 
subspace of M over the semifield Q+  {0};  
 
we see M = T + P with T  P = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0










. 
 
Further for every x  T we have a y  P;  
 
with x n y = 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0










. 
 
Example 6.56:  Let  
 
W = 
i
i
i 0
a x





 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d
d


























 dj  R+  {0}, 
1  i  32}


## Page 308


308
be a super column vector polynomial coefficient semivector 
space (linear algebra) over the semifield S =   Z+  {0}.  
 
 
Now we can define like wise semivector spaces of super 
matrices and study those structures.


## Page 309


309
 
 
 
 
 
Chapter Seven 
 
 
 
 
APPLICATIONS OF THESE ALGEBRAIC 
STRUCTURES WITH NATURAL PRODUCT 
 
 
 
 
 
 
We define natural product on matrices and that results in the 
compatability in column matrices and m × n (m ≠ n) matrices.  
 
 
Several algebraic structures using them are developed. 
 
 
The notion of super matrix coefficient polynomials are 
defined and described.  These new structures will certainly find 
nice and appropriate applications in due course of time.  Of 
course it is a very difficult thing to define products on super 
matrices in the way defined in [8, 19]; however because of this 
new ‘natural product’ we can define product on super matrices 
provided they are of the same type.


## Page 310


310
 
One has to find the uses of these new structures in eigen 
value problems, mathematical models, coding theory and finite 
element analysis methods. 
 
 
Further these natural product on matrices works like the 
usual product on the real line and the matrix product of row 
matrices.  If the concept of matrices is a an array of number than 
certainty the natural product seems to be appropriate so in due 
course of time researchers will find nice applications of them.


## Page 311


311
 
 
 
 
Chapter Eight 
 
 
 
 
SUGGESTED PROBLEMS 
 
 
 
In this chapter we suggest over 100 problems. Some of them 
can be taken up as research problems.  These problems however 
makes the reader to  understand these new notions introduced in 
this book.  
 
1. 
Find some interesting properties enjoyed by polynomials 
with matrix coefficients. 
 
2. 
For the row matrix coefficient polynomial semigroup  
    S[x] = 
i
i
i 0
a x
∞
=


∑
ai = (x1, x2, x3, x4) with xj ∈ R, 1 ≤ j ≤ 4} 
 
(i) Find zero divisors in S[x]. 
 
(ii) Can S[x] have ideals? 
 
(iii) Can S[x] have subrings which are not ideals? 
 
(iv) Can S[x] have idempotents? 
 
3. 
Let p(x) = (3, 2, 1, 5) + (–2, 0, 1, 3)x + (7, 8, 4, –6)x2 be a 
row matrix coefficient polynomial in the variable x. 
 
(i) 
Find roots of p(x). 
 
(ii) 
If α and β are roots of p(x) find a row matrix  
coefficient polynomial whose roots are α2 + β2 and  
α2 β2.


## Page 312


312
 
(iii) If the row matrix coefficients are from Z will α and  
β be in Z × Z × Z × Z? 
 
4. 
Give some nice properties enjoyed by the semigroup of 
square matrix coefficient polynomials.  
 
5. 
Solve the equation 1 1
1 1






x3  – 2
7
8
1
6
4






 = 0. 
 
6. 
Suppose p(x) = 
9
2
1
3
7








 – 
8
9
2
3
1














−


x + 
3
7
0
8
1








x2.  Solve for x. 
 
7. 
Let p(x) = (1, 2, 3)x3 – (2, 4, 5)x2 + (1, 0, 2)x – (3, 8, 1). 
 
Solve for x.   
Does q(x) = (1, 6, 9)x + (2, 1, 3) divide p(x)? 
 
8. 
Find the properties enjoyed by the group of square matrix 
coefficient polynomials in the variable x. 
 
9. 
Let p(x) = 2
1
0
1
5
6






 + 7
8
0
1
1
1






x2 + 3
1
2
0
1
5






x.   
 
Is p(x) solvable as a quadratic equation? 
 
10. 
Let p(x) = 
7
8
9
3






 + 
1
2
3
4






x2 + 
0
2
5
7






x3.  Find the derivatives,  
 
the coefficients are from Z. 
 
Can p(x) be integrated with respect to x?  Justify.


## Page 313


313
11. 
Suppose p(x) = 
9
i
i
i 0
a x
=∑
 where ai ∈ {V3×6 = {all 3 × 6 
matrices with coefficients from Z}, 0 ≤ i ≤ 9}; prove p(x) 
cannot be integrated and the resultant coefficients will not 
be in V3×6. 
 
12. 
Prove VR = {(a1, a2, …, a12) | ai ∈ R} has zero divisors 
under product. 
 
13. 
Prove V3×3 = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











 ai ∈ Z, 1 ≤ i ≤ 9} is a 
semigroup under multiplication.  
(i)   Is V3×3 a commutative semigroup? 
(ii)  Find ideals in V3×3. 
(iii) Can V3×3 have subsemigroups which are not ideals? 
 
14. 
Can VR [x] = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, …, x8) with xj ∈ Z,  
1 ≤ j ≤ 8}, a semigroup under product have zero divisors? 
 
(i)   Find ideals of VR [x]? 
 
(ii)   Find subsemigroups which are not ideals in VR [x]. 
(iii)  Can VR [x] be a S-semigroup? 
 
15. 
Let V7×7 [x] = 
i
i
i 0
a x
∞
=


∑
 ai’s are 7 × 7 matrices with 
entries from R} be a semigroup under the matrix 
multiplication. 
 
(i) 
Is V7×7 [x] a commutative semigroup? 
 
(ii) 
Find right ideals in V7×7 [x] which are not left ideals  
and vice versa. 
 
(iii) Find two sided ideals of V7×7 [x]. 
 
16. 
Distinguish between R [x] and V3×3 [x].


## Page 314


314
 
17. 
Distinguish between Q [x] and  
VR [x] = 
i
i
i 0
a x
∞
=


∑
 ai = (x1, x2, x3, x4); xj ∈ Q; 1 ≤ j ≤ 4}. 
 
18. 
What are the benefits of natural product in matrices? 
 
19. 
Prove Vn×n [x] under natural product is a commutative 
semigroup. 
 
20. 
Prove V3×7 [x] is a commutative semigroup under natural 
product ×n. 
 
21. 
Prove natural product ×n and the usual product of row 
matrices on VR [x] are identical. 
 
22. 
Show VC [x] under natural product is a semigroup with 
zero divisors. 
 
23. 
Obtain some nice properties enjoyed by  
VC = 
1
2
m
a
a
a














 ai ∈ Q; 1 ≤ i ≤ m} under the natural 
product, ×n. 
 
24. 
Show V5×2 = {all 5 × 2  matrices with entries from Q} 
under natural product ×n is a semigroup. 
 
(i) Find zero divisors in V5×2. 
(ii) Show all elements of V5×2 are not invertible in 
general. 
(iii) Show V5×2 has subsemigroups which are not ideals. 
(iv) Find ideals of V5×2.


## Page 315


315
(v) Can V5×2 have idempotents justify? 
 
25. 
Show (V3×3, ×n) and (V3×3, ×) are distinct as semigroups. 
 
(i) Can they be isomorphic? 
(ii) Find any other stricking difference between them. 
 
26. 
Can the set of 5 × 5 diagonal matrices with entries from Q 
under the natural product and the usual product be same? 
 
27. 
Prove (V2×2, +, ×n) is a commutative ring. 
 
28. 
Prove (V3×3, +, ×) is a non commutative ring with  
 
1
0
0
0
1
0
0
0
1










 as unit.  
 
29. 
Find the differences between a ring of matrices under 
natural product and usual matrix product.  
 
30. 
Prove (V2×7, +, ×n) is a commutative ring with identity. 
 
31. 
Let S = (V5×2, +, ×n) be a ring. 
(i) Find subrings of S. 
(ii) Is S a Smarandache ring? 
(iii) Can S have S-subrings? 
(iv) Can S have subrings which are not S-ring? 
(v) Find ideals in S. 
(vi) Find subrings in S which are not S-ideals. 
(vii) Find zero divisors in S.  
 
32. 
Find some special properties enjoyed by (VC, +, ×n).


## Page 316


316
33. 
Distinguish between (VR, +, ×n) and (VR, +, ×).  
 
34. 
Find the difference between the rings (V3×3, +, ×) and 
(V3×3, +, ×n). 
 
35. 
Let M = (
R
V+ , +, ×n) be a semiring where  
R
V+  = {(x1, x2, …, xn) | xi ∈ R+ ∪ {0}, 1 ≤ i ≤ n}. 
 
(i) Is M a semifield? 
(ii) Is M a S-semiring? 
(iii) Find subsemiring in M. 
(iv) Show every subsemiring need not a be S-subsemiring. 
(v) Find zero divisors in M. 
(vi) Can M have idempotents? 
 
36. 
Let P = {VC = 
1
2
3
4
5
a
a
a
a
a

















ai ∈ Q+ ∪ {0}; 1 ≤ i ≤ 5} be a 
semiring under + and ×n. 
 
(i) Find ideals of P. 
(ii) Is P a S-semiring? 
(iii) Can P have S-subsemiring? 
(iv) Find S-ideals if any in P. 
(v) Find zero divisors in P. 
 
37. 
Obtain some special properties enjoyed by the semiring of 
7 × 1 column matrices with entries from R+ ∪ {0}.


## Page 317


317
38. 
Mention some of the special features enjoyed by the 
semiring of 5 × 8 matrices with + and ×n; the entries are 
from R+ ∪ {0}. 
 
39. 
Is P = 
1
2
3
4
5
x
x
x
x
x

















xi ∈ R+; 1 ≤ i ≤ 5} ∪ 
0
0
0
0
0


























 a semifield  
 
under + and ×n? 
 
40. 
Can M = 
1
1
1
1
1
a
b
c
d
e
a
b
c
d
e







a1, b1, c1, d1, e1, a, b, c,  
 
d, e ∈ Q+} ∪ 
0
0
0
0
0
0
0
0
0
0
















, +, ×n} be a semifield? 
 
41. 
Find for S = 
1
2
3
4
5
6
7
8
a
a
a
a
a
a
a
a













 ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 8, +, ×n}  
 
the semiring. 
 
(i) 
Ideals which are not S-ideals. 
(ii) 
Subsemirings which are not S-semirings.  
(iii) Zero divisors. 
(iv) Subsemirings which are not ideals. 
(v) 
Is S a S-semiring?


## Page 318


318
42. 
Let P = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













 ai ∈ Q+ ∪ {0},  
 
1 ≤ i ≤ 16} be a semiring under + and natural product ×n. 
 
 
(i) 
Is P a S-ring? 
 
(ii) 
Can P have zero divisors? 
 
(iii) Show P is commutative.  
 
 
(iv) If ×n replaced by usual matrix product will P be a  
semiring?  Justify your claim. 
 
(v) 
Find S-ideals in P. 
 
(vi) Find subsemirings which are not S-subsemirings.  
 
 
43. 
Let V = {(x1, x2, …, xn) | xi ∈ R, 1 ≤ i ≤ n} be a vector 
space over F.  Find Hom (V, V). 
 
44. 
Let P = 
1
2
10
x
x
x














xi ∈ Q; 1 ≤ i ≤ 10} be a linear algebra 
over Q. 
(i) Find dimension of P over Q.  
(ii) Find a basis of P over Q. 
(iii) Write P as a direct sum of subspaces. 
(iv) Write P as a pseudo direct sum of subspaces. 
(v) Find a linear operator on P which is invertible. 
 
45. 
Give an example of a natural Smarandache special field.


## Page 319


319
46. 
What is the difference between a natural Smarandache 
special field and the field? 
 
47. 
Obtain the special properties enjoyed by S-special strong 
column matrix linear algebra. 
 
48. 
Obtain the special and distinct features of S-special strong 
3 × 3 matrix linear algebra. 
 
49. 
Find differences between Smarandache vector spaces and 
Smarandache special strong vector spaces. 
 
50. 
Let P = 
1
2
3
4
a
a
a
a







ai ∈ R, 1 ≤ i ≤ 4} be the 3 × 3 square 
matrix of natural special Smarndache field. 
 
(i) What are the special properties enjoyed by P? 
(ii) Can P have zero divisors? 
 
51. 
Obtain some interesting properties about S-special strong 
column matrix vector spaces constructed over R. 
 
52. 
Find some applications of S-special strong m × n (m ≠ n) 
linear algebras constructed over Q. 
 
53. 
Define some nice types of inner products on vector spaces 
using the natural product ×n. 
 
54. 
Can linear functionals be defined on S-special super n × 
m (m ≠ n) matrix vector spaces? 
 
55. 
Let V = 
1
2
12
13
14
24
25
26
36
a
a
...
a
a
a
...
a
a
a
...
a











 ai ∈ Q, 1 ≤ i ≤ 36} be a  
 
S-special strong vector space over the S-field.


## Page 320


320
F3×12 = 
1
2
12
13
14
24
25
26
36
x
x
...
x
x
x
...
x
x
x
...
x











 xi ∈ Q, 1 ≤ i ≤ 36}.  
 
(i) 
Find a basis for V. 
(ii) 
What is the dimension of V over F3×12? 
(iii) Write V as a direct sum of subspaces.  
(iv) Write V as a pseudo direct sum of subspaces. 
 
56. 
Let V be a S-special strong vector space of n × n matrices 
over the S-field FC of n × n matrices with elements from 
the field Q. 
 
(i) 
Find a basis for V. 
 
(ii) 
Write V as a direct sum of subspaces.  
 
(iii) Write V as a pseudo direct sum of subspaces. 
 
(iv) Find a linear operator on V. 
 
(v) 
Does every subspace W of V have W⊥? 
 
(vi) Write V as W + W⊥; 
 
57. 
Obtain some interesting properties about orthogonal 
subspaces. 
 
58. 
Find some interesting properties related with S-special 
row matrix linear algebras.  
 
59. 
Study the special properties enjoyed by S-special strong 
m × n matrix linear algebras (m ≠ n). 
 
60. 
Let S = 
1
2
3
4
5
a
a
a
a
a

















ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 5} be a semivector  
 
space of column matrices over the semifield F = Z+ ∪ 
{0}.


## Page 321


321
 
(i)  Find basis for S. 
(ii)  Write S as a direct sum of subsemivector spaces. 
(iii)  Write S as a pseudo direct sum of subsemivector  
spaces. 
(iv)   Can S be a semilinear algebra? 
 
61. 
Obtain some interesting properties enjoyed by semivector 
space of column matrices V over the semifield S = Q+ ∪ 
{0}. 
 
62. 
Enumerate the special properties enjoyed by the 
semivector space of m × n matrices (m ≠ n) over the 
semifield F = Q+ ∪ {0}. 
 
63. 
Bring out the differences between the semivector space of 
column matrices over Q+ ∪ {0} and vector space of 
column matrices over Q. 
 
64. 
Find some special properties enjoyed by semivector space 
of m × n matrices over the semifield Z+ ∪ {0} = S. 
 
65. 
Let V = 
1
2
3
4
5
6
7
10
11
12
15
16
17
20
a
a
a
a
a
a
a
...
...
a
a
a
...
...
a
a
a
...
...
a













ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 
20} be a semivector space over the semifield S = Z+ ∪ 
{0}. 
 
(i) Can V be made into a semilinear algebra over S? 
(ii) Find a basis for V. 
(iii) Find semivector subspaces of V so that V can be  
     
   written as a direct sum of semivector subspaces. 
(iv) Write V as a pseudo direct sum of semivector    
    subspaces.


## Page 322


322
(v) Write V = W ⊕ W⊥, W⊥ the orthogonal complement  
   of W. 
 
66. 
Let 
S
C
F  = 
1
2
3
4
5
6
a
a
a
a
a
a
























ai ∈ Q, 1 ≤ i ≤ 6, ×n} be a semigroup. 
 
(i) Find ideals in 
S
C
F . 
(ii) Can 
S
C
F  have subsemigroups which are not ideals? 
(iii) Prove 
S
C
F  has zero divisors. 
(iv) Find units in 
S
C
F . 
(v) Is 
S
C
F  a S-semigroup? 
 
67. 
Let 
S
R
F  = {(a1 a2 | a3 a4 | a5) | ai ∈ Z, 1 ≤ i ≤ 5, ×n} be a 
semigroup. 
 
(i) 
Find subsemigroups which are not ideals in 
S
R
F  
(ii) 
Find zero divisors in 
S
R
F . 
(iii) Can 
S
R
F  have units? 
(iv) Is x = (1, –1 | 1 –1 | –1) a unit in 
S
R
F . 
 
68. 
Let 
S
5 3
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

















ai ∈ Q, 1 ≤ i ≤ 15, ×n} be a  
 
semigroup of super matrices.


## Page 323


323
 
(i) 
Find units in 
S
5 3
F × . 
(ii) 
Is 
S
5 3
F ×  a S-semigroup? 
(iii) Can 
S
5 3
F ×  have S-subsemigroups? 
(iv) Can 
S
5 3
F ×  have S-ideals? 
(v) 
Does 
S
5 3
F ×  have S-zero divisors/ 
(vi) Can 
S
5 3
F ×  have S-idempotents? 
(vii) Show 
S
5 3
F ×  have only finite number of idempotents. 
 
69. 
Let 
S
4 4
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













ai ∈ Q, 1 ≤ i ≤ 16} be a  
 
semigroup of super square matrices.   
 
(i) Find zero divisors in 
S
4 4
F × . 
(ii) Can 
S
4 4
F ×  have S-zero divisors? 
(iii) Can 
S
4 4
F ×  have S-idempotents? 
(iv) Find the main complement of 
3
0
1
2
1
0
0
5
0
3
15
7
0
1
0
0












. 
(v) Is 
S
4 4
F ×  a S-semigroup? 
 
70. 
Let 
S
3 7
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ Z, 
 
 1 ≤ i ≤ 21, ×n} be a super row vector semigroup.


## Page 324


324
 
(i) 
Find ideal of 
S
3 7
F × . 
 
(ii) 
Is 
S
3 7
F ×  a S-semigroup? 
 
(iii) Can 
S
3 7
F ×  have S-ideals? 
 
(iv) Show 
S
3 7
F ×  can have only finite number of  
idempotents. 
 
(v) 
Show 
S
3 7
F ×  has no units. 
 
71. 
Obtain some interesting properties about (
S
C
F , ×n). 
 
72. 
Find some applications of the semigroup (
S
m m
F × ; m ≠ n, 
×n).  
 
73. 
Find the difference between (
S
n n
F × , ×) and (
S
n n
F × , ×n). 
 
74. 
Find some special and distinct features enjoyed by 
S
9 8
F × . 
 
75. 
Prove {
S
n m
F × , n ≠ m, +, ×n} is a commutative ring of 
infinite order. 
 
76. 
Let 
S
2 5
F ×  = 
1
2
3
4
5
6
7
8
9
10
a
a
a
a
a
a
a
a
a
a







ai ∈ Q, 1 ≤ i ≤ 10, +, 
×n} be a ring of super row vectors. 
 
(i) Find ideals in 
S
2 5
F × . 
(ii) Is 
S
2 5
F ×  a S-ring? 
(iii) Prove 
S
2 5
F ×  has ideals. 
(iv) Can 
S
2 5
F ×  have S-ideals? 
(v) Can 
S
2 5
F ×  have S-zero divisors and S-idempotents?


## Page 325


325
77. 
Let 
S
8 3
F ×  = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a



























ai ∈ Q, 1 ≤ i ≤ 24, +, ×n} be 
a super column vector ring. 
(i) Prove 
S
8 3
F ×  has zero divisors. 
(ii) Prove 
S
8 3
F ×  has units. 
(iii) Can 
S
8 3
F ×  have S-units? 
(iv) Is 
S
8 3
F ×  a S-ring? 
(v) Prove 
S
8 3
F ×  has idempotents? 
 
78. 
Let 
S
C
F  = 
1
2
3
4
5
6
7
8
9
10
a
a
a
a
a
a
a
a
a
a

































ai ∈ R, 1 ≤ i ≤ 10, +, ×n} be a super 
column matrix ring. 
 
(i) Find the number of idempotents in 
S
C
F . 
(ii) Show 
S
C
F  has infinite number of zero divisors but only  
 
finite number of idempotents.


## Page 326


326
(iii) Can 
S
C
F  have S-idempotents? 
(iv) Can 
S
C
F  have S-units? 
 
79. 
Let 
S
3 3
F ×  = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q, 1 ≤ i ≤ 8, +, ×n} be a 
square super matrix ring. 
 
(i) 
Prove 
S
3 3
F ×  is a commutative ring. 
 
(ii) 
Find ideals in 
S
3 3
F × . 
(iii) Is 
S
3 3
F ×  a S-ring? 
(iv) Show 
S
3 3
F ×  has only finite number of idempotents. 
(v) Can 
S
3 3
F ×  have S-ideals? 
 
80. 
Enumerate some special features enjoyed by super matrix 
rings 
S
C
F  (or 
S
R
F  or 
S
n n
F ×  or 
S
n m
F × ; m ≠ n). 
 
81. 
Find some applications of the rings mentioned in problem 
(80). 
 
82. 
Prove R = {(a1 | a2 | … | an) | ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ n} is a 
semigroup under +. 
 
 
(i) 
Can R have ideals? 
 
(ii) 
Can R have S-zero divisors? 
 
83. 
Let P = {(a1 | a2 | a3 a4 a5 | a6 a7) | ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 7} 
be a semigroup under ×n.  Find the special properties 
enjoyed by these semigroups.


## Page 327


327
84. 
Let T = 
1
2
3
4
5
a
a
a
a
a

















ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 5, ×n} be a 
semigroup under ×n. 
 
(i) 
Prove T is a commutative semigroup. 
 
(ii) 
Can T have S-zero divisors? 
(iii)   Show T can have only finite number of  
idempotents. 
 
(iv) Show T can have no units. 
 
(v) 
Can T have S-ideals? 
 
 
85. 
Let W = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ Q+ ∪ {0}, 1 ≤ i 
≤ 15, ×n} be a semigroup. 
 
(i)  Find the number of idempotents in W. 
 
(ii) Is W a S-semigroup? 
(iii) Find units in W. 
    (iv) Show all elements are not units in W. 
 
86. 
Let M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
18
19
20
24
25
26
30
a
a
a
a
a
a
a
a
a
a
a
a
a
a
...
...
...
a
a
a
...
...
...
a
a
a
...
...
...
a

















ai ∈ Q+ ∪ {0}, 
1 ≤ i ≤ 30, ×n} be a semigroup. 
(i) Is M a S-semigroup?


## Page 328


328
(ii) Does M contain S-zero divisors? 
(iii) Prove M has only finite number of idempotents. 
(iv) Can M have S-idempotents? 
(v) Can M have S-units? 
 
87. 
Let M = 
S
2 3
F ×  = 
1
2
3
4
5
6
a
a
a
a
a
a







ai ∈ Z+ ∪ {0}, 1 ≤ i ≤ 6, 
+,  ×n} be a semiring. 
 
 
(i) Prove M is not a semifield. 
 
(ii) Find subsemirings in M. 
 
88. 
Obtain some interesting properties enjoyed by column 
super matrix semirings with entries from Q+ ∪ {0}. 
 
89. 
Distinguish between a super square matrix ring and a 
super square matrix semiring. 
 
90. 
Let P = 
1
6
2
7
3
8
4
9
5
10
a
a
a
a
a
a
a
a
a
a

















ai ∈ R+ ∪ {0}, 1 ≤ i ≤ 10, +,  ×n} be a 
semiring. 
 
(i) Find subsemirings of P. 
(ii) Is P a S-semiring? 
(iii) Can P have S-ideals? 
(iv) Can P have S-idempotents? 
(v) Can P have S-zero divisors?


## Page 329


329
91. 
Let T = 
1
2
3
4
5
6
7
8
9
14
15
16
21
22
23
28
29
30
35
36
37
42
43
44
49
a
a
a
a
a
a
a
a
a
...
...
...
...
a
a
a
...
...
...
...
a
a
a
...
...
...
...
a
a
a
...
...
...
...
a
a
a
...
...
...
...
a
a
a
...
...
...
...
a























ai ∈ Z+ ∪ 
{0}, 1 ≤ i ≤ 49, +,  ×n} be a semiring. 
 
(i) Show T has only finite number of idempotents in it. 
(ii) Find zero divisors of T. 
(iii) Find idempotents of T. 
(iv) Can T have S-zero divisors? 
(v) Is T a S-semiring? 
 
92. 
Find some interesting properties of super matrix 
semirings. 
 
93. 
Let M = {
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a












 ∪ 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0












where  
 
ai ∈ Q+, 1 ≤ i ≤ 16, +,  ×n}. 
 
 
(i) 
Is M a semifield? 
 
(ii) 
Is M a S-semiring?


## Page 330


330
94. 
Can P = 
1
2
3
4
5
6
a
a
a
a
a
a
























 ∪
0
0
0
0
0
0










 where ai ∈ Q+, 1 ≤ i ≤ 6, +,  ×n} be 
a semifield? 
 
95. 
Is T = {(a1 | a2 a3 | a4 a5 a6) ∪ (0 | 0 0 | 0 0 0) | ai ∈ Q+, 1 ≤ 
i ≤ 6, +,  ×n} a semifield? 
 
 
Can T have subsemifields? 
 
96. 
Let W = 
1
2
3
4
5
6
7
8
9
12
13
16
17
20
21
24
25
28
29
32
33
36
a
a
a
a
a
a
a
a
a
.
.
a
a
.
.
a
a
.
.
a
a
.
.
a
a
.
.
a
a
.
.
a
a
.
.
a





























 ∪ 
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0




























where  
 
ai ∈ R+, 1 ≤ i ≤ 36, +,  ×n} be a semifield of super column 
vectors.  Find subsemifield of W.  Can W have 
subsemirings? 
 
97. 
Find applications of matrices with natural product. 
 
98. 
Prove super matrices of same type under natural product 
is a semigroup with zero divisors.


## Page 331


331
99. 
Let X = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a













where ai ∈ R+ ∪ {0}, 1 ≤ i 
≤ 16} be a super square matrix linear algebra over the 
semifield S = R+ ∪ {0}. 
 
(i) Find a basis of X over S. 
(ii) Is X finite dimensional? 
(iii) Write X as a direct sum of semivector subspaces. 
(iv) Write X as a pseudo direct sum of semivector 
subspaces. 
(v) Let V ⊆ X be a subspace find V⊥ so that X = V + V⊥ 
a complement? 
 
100. Let V = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Q+ ∪ {0}, 1 ≤ i ≤ 9} be a 
super matrix semivector space over the semifield S = Z+ 
∪ {0}. 
 
 
(i) 
Can W = 
1
2
3
4
5
6
7
8
9
a
a
a
a
a
a
a
a
a











ai ∈ Z+ ∪ {0},  
 
  
1 ≤ i ≤ 9} ⊆ V have a orthogonal complement  
 
  
space? Justify your claim.


## Page 332


332
101. Let V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a















ai ∈ Q+ ∪ {0}, 
1 ≤ i ≤ 24} be a super matrix semilinear algebra over S = 
Z+ ∪ {0}. 
 
(i) Is V finite dimensional? 
(ii) Find subspaces of V so that V can be written as a 
direct sum of super matrix semivector subspaces. 
(iii) Write V as a pseudo direct sum of super matrix 
semilinear algebra. 
(iv) Let M = 
1
6
7
8
2
9
10
11
3
12
13
14
4
5
a
0
0
a
a
a
a
0
0
a
a
a
a
0
0
a
a
a
0
a
a
0
0
0















ai ∈ Q+ ∪ 
{0}, 1 ≤ i ≤ 14} ⊆ V be a super matrix semilinear 
subalgebra of V. 
a) How many complements exists for M? 
b) Write down the main complement of M. 
 
 
102. Let V = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a











ai ∈ Q+ ∪ {0}, 
1 ≤ i ≤ 18} be a super row vector semilinear algebra over 
the semifield S = Q+ ∪ {0}. 
 
(i) Find the dimension of V over S. 
(ii) Can V have more than one basis over S?


## Page 333


333
(iii) Can V have linearly independent elements whose 
number (cardinality) is greater than that of cardinality 
of the basis of V over S? 
 
103. Let M = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a

































 where ai ∈ Z+ ∪ {0}, 1 ≤ 
i ≤ 40} be a super column vector semilinear algebra over 
the semifield S = Z+ ∪ {0}. 
 
(i) Find a basis for M over S. 
(ii) Write M as a pseudo direct sum of super column 
vector semilinear subalgebra over S. 
(iii) Write M as a direct sum of super column vector 
semilinear subalgebras over S.  
(iv) Write M = W + W⊥ where W⊥ is the orthogonal 
complement of W. 
 
104. Let P = 
i
i
i 0
a x
∞
=


∑
ai = (m1 m2 | m3 m4 m5 | m6 m7 | m8) 
where mi ∈ Q+ ∪ {0}, 1 ≤ i ≤ 8} be a super row matrix 
semilinear algebra over the semifield S = Z+ ∪ {0}. 
 
(i) Write P as a direct sum of semilinear subalgebras.


## Page 334


334
(ii) Let M = 
i
i
i 0
a x
∞
=


∑
 ai = (0 0 | m1 m2 m3 | 0 0 | 0) m1, 
m2, m3 ∈ Q+ ∪ {0}} ⊆ P be a super row matrix semi 
linear subalgebra over S.  Find M⊥ so that P = M + 
M⊥. 
(iii) Let T =  
i
i
i 0
a x
∞
=


∑
ai = (d1 d2 | 0 0 0 | d3 d4 | 0), dj ∈ 
Z+ ∪ {0}, 1 ≤ j ≤ 4} ⊆ P be a semi sublinear algebra 
of P over S.  Can we find a orthogonal complement of 
T of P over S so that T + T⊥ = P? 
 
105. Let S = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
9
10
11
d
d
d
d
d
d
d
d
d
d
d




































 dj ∈ Z+ ∪ {0}, 1 ≤ j ≤ 11} be 
a super column matrix semilinear algebra over the 
semifield F = Z+ ∪ {0}. 
 
(i) Find a basis for S over F. 
(ii) Write S as a direct sum of linear sbalgebras. 
(iii) Write S as P + P⊥ so that for every x ∈ P we have  
 
every y ∈ P⊥ with x ×n y = (0).


## Page 335


335
106. Let T = 
i
i
i 0
a x
∞
=


∑
 ai = 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m
m




































 mi ∈ Z+ ∪ {0}, 
1 ≤ i ≤ 33} be a super column vector semilinear algebra 
over S = Z+ ∪ {0}. 
 
(i)   Find a basis for T over S. 
 
(ii)   Can T have more than one basis? 
 
(iii)  Write T as direct sum. 
   (iv)   Write T as pseudo direct sum. 
 
107. Let M =
i
i
i 0
d x
∞
=


∑
 di =  
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a




















 ai ∈ Z+ ∪ 
{0}, 1 ≤ i ≤ 24} be a super matrix semilinear algebra over 
the semifield S = Z+ ∪ {0}. 
 
(i) Find a basis of M over S. 
(ii) Prove M has subspaces which are complements to  
 
each other in m.


## Page 336


336
 
108. Obtain some unique properties enjoyed by super matrix 
coefficient polynomial rings. 
 
109. Find some special features of super matrix coefficient 
polynomial semivector spaces over the semifield S = Z+ ∪ 
{0}. 
 
110. Describe any special feature enjoyed by super matrix 
coefficient 
polynomial 
semivector 
space 
over 
the 
semifield S = Z+ ∪ {0}. 
 
111. Give some applications of super matrix coefficient 
polynomial semilinear algebras defined over a semifield.


## Page 337


337
 
 
 
 
 
 
FURTHER READING  
 
 
 
 
1. 
Abraham, R., Linear and Multilinear Algebra, W. A. 
Benjamin Inc., 1966. 
2. 
Albert, A., Structure of Algebras, Colloq. Pub., 24, Amer. 
Math. Soc., 1939.  
3. 
Gel'fand, I.M., Lectures on linear algebra, Interscience, 
New York, 1961. 
4. 
Greub, W.H., Linear Algebra, Fourth Edition, Springer-
Verlag, 1974. 
5. 
Halmos, P.R., Finite dimensional vector spaces, D Van 
Nostrand Co, Princeton, 1958.  
6. 
Harvey E. Rose, Linear Algebra, Bir Khauser Verlag,  
2002.  
7. 
Herstein I.N., Abstract Algebra, John Wiley,1990. 
8. 
Horst P., Matrix Algebra for social scientists, Hot, Rinehart 
and Winston inc, 1963. 
9. 
Jacob Bill, Linear Functions and Matrix Theory , Springer-
Verlag, 1995. 
10. 
Kostrikin, A.I, and Manin, Y. I., Linear Algebra and 
Geometry, Gordon and Breach Science Publishers, 1989. 
11. 
Lay, D. C., Linear Algebra and its Applications, Addison 
Wesley, 2003.


## Page 338


338
12. 
Rorres, C., and Anton H., Applications of Linear Algebra, 
John Wiley & Sons, 1977. 
13. 
Vasantha Kandasamy, W.B., Smarandache Semigroups, 
American Research Press, Rehoboth, NM, (2002).  
14. 
Vasantha Kandasamy, W. B., Groupoids and Smarandache 
Groupoids, American Research Press, Rehoboth, NM, 
(2002). 
15. 
Vasantha 
Kandasamy, 
W.B., 
Smarandache 
Loops, 
American Research Press, Rehoboth, NM, (2002). 
16. 
Vasantha Kandasamy, W. B., Smarandache Semirings and 
semifields and semivector spaces, American Research Press, 
Rehoboth, NM, (2002). 
17. 
Vasantha 
Kandasamy, 
W.B., 
Linear 
Algebra 
and 
Smarandache Linear Algebra, Bookman Publishing, 2003. 
18. 
Vasantha Kandasamy, W. B., Smarandache Rings, 
American Research Press, Rehoboth, NM, (2002). 
19. 
Vasantha Kandasamy, W.B., and Smarandache, Florentin, 
Super Linear Algebra, Infolearnquest, Ann Arbor, 2008.


## Page 339


339
 
 
 
 
 
INDEX  
 
 
 
 
 
D 
 
Derivatives of matrix coefficient polynomials, 21-9 
 
I 
 
Integral of matrix coefficient polynomials, 26-33 
 
L 
 
Linear algebra of super column matrices, 225-9 
Linear algebra of super row matrices, 225-9 
Linear algebra under natural product of matrices, 91-7 
 
M 
 
Matrix coefficient polynomials, 8 
Natural Smarandache special field, 97-103 
 
N 
 
Natural special row matrix Smarandache special field, 102-3 
n-row matrix structured vector space, 137-9 
 
O 
 
Orthogonal complement of a semivector subspace, 151-5


## Page 340


340
P 
 
Polynomial with matrix coefficients, 8 
Polynomials with column matrix coefficients, 11-35 
Polynomials with row matrix coefficients, 11-35 
 
R 
 
Ring of column matrices under natural product, 63-8 
Ring of row matrix coefficient polynomials, 16-9 
 
S 
 
Semifield of matrices under natural product, 76-9 
Semifields, 7 
Semigroup of row matrix coefficient polynomials, 16-8 
Semigroup of super column vector, 198-204 
Semigroup of super row vectors, 198-200 
Semiring of matrices under natural product, 75-80 
Semirings, 7 
Semivector spaces, 7 
S-ideal, 7 
Smarandache linear algebra, 10 
Smarandache semigroup under natural product, 42-9 
Smarandache semigroup, 7 
Smarandache semiring, 77-83 
Smarandache subsemigroup, 46-53 
Smarandache subsemiring, 77-83 
Smarandache vector spaces, 10 
Special column matrix S-field, 100-4 
S-ring of matrices under natural product, 70-5 
S-rings, 7 
S-Special strong column matrix vector space, 103-7 
S-Special strong matrix vector space, 105-7 
S-strong special row matrix, 109-112 
S-strong special vector subspaces, 112-6 
S-subring of matrices under natural product, 71-5 
S-subrings, 7 
Super column matrix coefficient polynomials, 255-9 
Super column matrix, 9, 163-9 
Super column vector coefficient polynomial vector space, 280-4 
Super column vector semiring, 212-7 
Super linear algebra of super matrices, 245-9


## Page 341


341
Super matrix semigroup under natural product, 182-190 
Super row matrix coefficient polynomials, 252-5 
Super row matrix, 8-9, 163-6 
Super row vector semiring, 212-6 
Super row vector, 9, 163-8 
Super square matrix semiring, 212-7 
Super square matrix, 9, 163-9


## Page 342


342
ABOUT THE AUTHORS 
 
 
Dr.W.B.Vasantha Kandasamy is an Associate Professor in the 
Department of Mathematics, Indian Institute of Technology 
Madras, Chennai. In the past decade she has guided 13 Ph.D. 
scholars in the different fields of non-associative algebras, 
algebraic coding theory, transportation theory, fuzzy groups, and 
applications of fuzzy theory of the problems faced in chemical 
industries and cement industries. She has to her credit 646 
research papers. She has guided over 68 M.Sc. and M.Tech. 
projects. She has worked in collaboration projects with the Indian 
Space Research Organization and with the Tamil Nadu State AIDS 
Control Society. She is presently working on a research project 
funded 
by 
the 
Board 
of 
Research 
in 
Nuclear 
Sciences, 
Government of India. This is her 63rd book. 
On 
India's 
60th 
Independence 
Day, 
Dr.Vasantha 
was 
conferred the Kalpana Chawla Award for Courage and Daring 
Enterprise by the State Government of Tamil Nadu in recognition 
of her sustained fight for social justice in the Indian Institute of 
Technology (IIT) Madras and for her contribution to mathematics. 
The award, instituted in the memory of Indian-American 
astronaut Kalpana Chawla who died aboard Space Shuttle 
Columbia, carried a cash prize of five lakh rupees (the highest 
prize-money for any Indian award) and a gold medal. 
She can be contacted at vasanthakandasamy@gmail.com  
Web Site: http://mat.iitm.ac.in/home/wbv/public_html/  
or http://www.vasantha.in  
 
 
Dr. Florentin Smarandache is a Professor of Mathematics at 
the University of New Mexico in USA. He published over 75 books 
and 200 articles and notes in mathematics, physics, philosophy, 
psychology, rebus, literature. In mathematics his research is in 
number theory, non-Euclidean geometry, synthetic geometry, 
algebraic 
structures, 
statistics, 
neutrosophic 
logic 
and 
set 
(generalizations of fuzzy logic and set respectively), neutrosophic 
probability (generalization of classical and imprecise probability).  
Also, 
small 
contributions 
to 
nuclear and particle physics, 
information fusion, neutrosophy (a generalization of dialectics), 
law of sensations and stimuli, etc. He got the 2010 Telesio-Galilei 
Academy of Science Gold Medal, Adjunct Professor (equivalent to 
Doctor Honoris Causa) of Beijing Jiaotong University in 2011, and 
2011 Romanian Academy Award for Technical Science (the 
highest in the country). Dr. W. B. Vasantha Kandasamy and Dr. 
Florentin Smarandache got the 2011 New Mexico Book Award for 
Algebraic Structures. He can be contacted at smarand@unm.edu

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
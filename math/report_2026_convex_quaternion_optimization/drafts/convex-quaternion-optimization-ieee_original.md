# Convex Quaternion Optimization for Signal Processing: Theory and Applications (IEEE)

- Source PDF: `C:\Users\Projects\research\manager-agent\math\report_2026_convex_quaternion_optimization\Convex_Quaternion_Optimization_for_Signal_Processing_Theory_and_Applications.pdf`
- Extraction: `pdftotext` reading-order text
- Verification status: unverified draft

> This file is an extraction aid. Check headings, paragraph order, hyphenation, equations, tables, figure captions, references, and numeric values against the PDF before treating it as accurate.

---

4106

IEEE TRANSACTIONS ON SIGNAL PROCESSING, VOL. 71, 2023

Convex Quaternion Optimization for Signal Processing: Theory and Applications
Shuning Sun , Qiankun Diao , Dongpo Xu , Pauline Bourigault , and Danilo P. Mandic , Fellow, IEEE

Abstract—Convex optimization methods have been extensively used in communications and signal processing. However, the theory of quaternion optimization is currently not as fully developed and systematic as that of complex and real optimization. To this end, we establish the convex optimization theory in quaternion variables based on the generalized Hamilton-real (GHR) calculus. This is achieved in a way that conforms with traditional complex and real optimization theory. We present several discriminant theorems for convex quaternion functions analogous to their complex counterparts. We also provide several discriminant criteria for strongly convex functions by the theorems of convex quaternion functions. Furthermore, we prove that the quaternion Newton method can converge in one step for positive deﬁnite quadratic quaternion functions and provide two applications in quaternion signal processing. These results provide a solid theoretical foundation for convex quaternion optimization and open avenues for further developments in quaternion signal processing applications.
Index Terms—Convex quaternion functions, strongly convex quaternion functions, discriminant criterion, quaternion signal processing, GHR calculus.
I. INTRODUCTION
Q UATERNIONS were ﬁrst introduced by William Hamilton in 1843 as an associative but non-commutative
algebra over the real numbers [1]. Over the years, quaternions have become a powerful tool in various ﬁelds, including image processing [2], [3], signal processing [4], [5], [6], and machine learning [7], [8], [9]. Examples include the work by Jia et al. [3], who introduced a robust method for quaternion matrix completion that can be used to reconstruct large-scale color images. Flamant et al. [10] demonstrated the efﬁciency of the Quaternion Fourier Transform in processing bivariate
Manuscript received 24 April 2023; revised 30 August 2023 and 24 October 2023; accepted 24 October 2023. Date of publication 30 October 2023; date of current version 9 November 2023. This work was supported in part by the Natural Science Foundation of Jilin Province, in part by the National Natural Science Foundation of China under Grant 62176051, and in part by the Fundamental Research Funds for the Central Universities of China under Grant 2412022ZD054. The associate editor coordinating the review of this manuscript and approving it for publication was Ms. Irène Waldspurger. (Corresponding author: Dongpo Xu.)
Shuning Sun, Qiankun Diao, and Dongpo Xu are with the Academy for Advanced Interdisciplinary Studies, Northeast Normal University, Changchun 130024, China, and also with the Key Laboratory for Applied Statistics of MOE, School of Mathematics and Statistics, Northeast Normal University, Changchun 130024, China (e-mail: xudp100@nenu.edu.cn).
Pauline Bourigault and Danilo P. Mandic are with the Department of Electrical and Electronic Engineering, Imperial College London, London SW7 2AZ, U.K. (e-mail: d.mandic@imperial.ac.uk).
Digital Object Identiﬁer 10.1109/TSP.2023.3328053

signals. Ogunfunmi et al. [11] presented a kernel adaptive ﬁlter for quaternion data. Moreover, Mengüç et al. [12] designed quaternion-valued second-order Volterra adaptive ﬁlters for nonlinear 3-D and 4-D signal processing. Xia et al. [13] established an estimation framework for processing quaternionvalued Gaussian data. Finally, Zhang et al. [7] discussed a new method for reducing the computation cost of quaternion signal estimation, while Enshaeifar et al. [14] introduced the quaternion-valued singular spectrum analysis for multichannel electroencephalogram analysis.
The theory of real-valued and complex-valued convex optimization is well-established. It has been widely used in the areas of communications [15], machine learning [16], [17], [18] and signal processing [19], [20], [21]. In recent years, convex quaternion optimization has also attracted interest. For example, Qi et al. [2] studied ﬁrst-order and second-order derivatives of real-valued functions of quaternion variables over their real and imaginary i, j, and k parts. However, this complicates the proof and computational process in quaternion optimization. Flamant et al. [22] and Liu et al. [23] provided the ﬁrst-order characterization of convex quaternion functions by the GHR calculus [24]:

f (q) f (p) + 4Re ∇p∗ f (p)H (q − p) ,

(1)

where f (q) : C → R, C ⊂ Hn is convex, and ∇p∗ f (p)

T

∂f ∂p∗

is deﬁned in [25]. This motivates us to strengthen fur-

ther the discriminant criteria of convex quaternion functions and

strongly convex quaternion functions, especially their second-

order characterization.

The main challenge in extending real optimization theory to

the quaternion ﬁeld involves two aspects: i) quaternion mul-

tiplication is non-commutative; ii) many theories of convex

quaternion optimization rely on quaternion gradients and Hes-

sian matrices, which have only recently been deﬁned within

the framework of the GHR calculus [24], [25], [26]. The GHR

calculus is a natural extension of Wirtinger calculus from the

complex domain to the quaternion ﬁeld [27], [28]. Before

the introduction of the GHR calculus, the quaternion pseudo-

derivative was used for calculating the gradient, which trans-

forms the quaternion optimization problem into a lengthy and

complicated real optimization problem; the solution is then

found by using real-valued optimization algorithms [29], [30].

Flamant et al. [5], [22] demonstrated that the GHR calcu-

lus is a powerful theory in quaternion signal processing and

1053-587X © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

SUN et al.: CONVEX QUATERNION OPTIMIZATION FOR SIGNAL PROCESSING: THEORY AND APPLICATIONS

4107

Fig. 1. Derivation process of quaternion optimization theory. (23) – (26) give the expressions of the gradient and Hessian matrix in R, H, and Hn.

function. Section IV introduces the discriminant theorems for strongly convex quaternion functions and the proof of quadratic termination. In Section V, we provide two practical applications in quaternion signal processing. Finally, this paper concludes with Section VI.

non-negative matrix factorization. Mengüç et al. [12], [31] established that the GHR calculus paves the way for the theory and applications of quaternion-valued adaptive ﬁlters. Took and Xia [32] proposed a multichannel quaternion least-mean-square based on the GHR calculus for adaptive ﬁltering. Parcollet et al. [33] further emphasized the signiﬁcance of the GHR calculus as a recent breakthrough in the ﬁeld.
The convex quaternion optimization theory has gradually attracted attention due to its promising applications in signal processing and optimization. Our work aims to develop the convexity theory of quaternion functions using the GHR calculus [24]. To this end, we make use of the duality of the augmented quaternion vector qH qT, qiT, qjT, qkT T (see (3)) and the augmented real vector qR qaT, qTb , qcT, qdT T, where the quaternion vector q = qa + qbi + qcj + qdk ∈ Hn [25]. Next, we employ the relationships between augmented quaternion gradient and augmented real gradient, as well as between the augmented quaternion Hessian matrix and augmented real Hessian matrix, as shown in [25]. This allows us to establish the discriminant criteria for convexity, from the real ﬁeld R to the augmented quaternion space H, and then to the quaternion ﬁeld Hn, where the sets R and H are deﬁned in (5) and (6), as illustrated in Fig. 1. Furthermore, we develop several discriminant theorems for strong convexity based on the discriminant criteria of convex quaternion functions. Finally, we prove the quadratic termination of the quaternion Newton method for positive deﬁnite quadratic quaternion functions and provide two illustrative applications in the ﬁeld of quaternion signal processing, including quaternion collaborative representation-based classiﬁcation (QCRC) and quaternion binary logistic regression (QBLR). Numerical experiments also support our theoretical results.
This work establishes the theory of convex optimization in the quaternion ﬁeld, whereby:
• By using the GHR calculus, we establish several discriminant theorems for convex functions in the quaternion ﬁeld. These theorems include gradient monotonicity and second-order characterization.
• We provide several discriminant criteria for strongly convex quaternion functions based on the theorems of convex functions. These are consistent with the real and complex correspondence criteria.
• We prove that the quaternion Newton method can converge in one step for positive deﬁnite quadratic functions. Additionally, we provide two applications of convex quaternion optimization to support theoretical analysis.
This paper is organized as follows. Section II gives an overview of quaternion algebra and the GHR calculus. Section III presents several discriminant theorems for convex quaternion functions, covering gradient monotonicity, secondorder characterization, and an example of a convex quaternion

II. PRELIMINARIES

A. Quaternion Algebra A quaternion q, can be expressed as

q = qa + qbi + qcj + qdk,

(2)

where qa, qb, qc, qd ∈ R, and the imaginary units i, j and k satisfy i2 = j2 = k2 = ijk = −1, ij = −ji = k, jk = −kj =

i, ki = −ik = j. The set of quaternions is deﬁned as H

{q = qa + qbi + qcj + qdk | qa, qb, qc, qd ∈ R}. Owing to the

properties of the imaginary units, the multiplication of two

quaternions in H is noncommutative. The real part of q

is denoted by Re {q} = qa, whereas the imaginary part

is Im {q} = qbi + qcj + qdk. The conjugate of q is q∗ =

Re {q} deﬁned

− Im as | q

{|=q}√=qqqa∗

− qb . If q

i − qcj − qdk. The = 0, the inverse of

modulus of q is

q

is

q−1

=

q∗ |q|2

.

The rotation of a quaternion q is deﬁned as [34]

qμ μqμ−1

(3)

where μ is a nonzero quaternion. For any p, q ∈ H, and ∀ν, μ ∈ H, the following holds [26]

c(pq)μ = pμqμ, qμν = (qν )μ ,

qμ∗ (q∗)μ = (qμ)∗ q∗μ.

(4)

Consider a quaternion vector q = qa + qbi + qcj + qdk ∈

Hn where qa, qb, qc, qd ∈ Rn. Deﬁne its augmented real vec-

tor as qR

qTa

,

qTb ,

qcT,

q

T d

T∈R

[4],

[35]

and

the

aug-

mented quaternion vector as qH qT, qiT, qjT, qkT T ∈ H

[25], where the set of augmented real vectors and the set of

augmented quaternion vectors are deﬁned as

R

qR =

qTa ,

q

T b

,

qTc

,

qTd

T | q ∈ Hn

= R4n,

(5)

H qH = qT, qiT, qjT, qkT T | q ∈ Hn ⊂ H4n. (6)

By deﬁnition, there exists a one-to-one mapping between Hn,

R and H [22]. The 2-norms of q, qR and qH are deﬁned as

q2

qHq, qR 2

qTRqR, and qH 2

qHH qH.

The relationship between the augmented quaternion vector

qH and the augmented real vector qR is given by [25]

qH = JnqR

⇔

qR

=

1 4

J

H n

qH,

(7)

where

⎛

⎞

In iIn jIn kIn

J n = ⎜⎜⎝

In In

iI n −iI n

−j I n jIn

−kI n −kI n

⎟⎠⎟ ∈ H4n×4n,

(8)

In −iIn −jIn kIn

and

J HnJ n

=

4I 4n ,

In

is

the

n

×

n

identity

matrix,

and

J

H n

is

the conjugate transpose of J n.

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

4108

IEEE TRANSACTIONS ON SIGNAL PROCESSING, VOL. 71, 2023

Proposition 2.1: For any p, q ∈ Hn, their augmented real
vectors are pR, qR ∈ R, and their augmented quaternion vectors are pH, qH ∈ H. Then

(a) pHT qH = 4Re pTq ;

(9)

(b) 4pRT qR = pHH qH = 4Re pHq ;

(10)

(c) 2 pR 2 = pH 2 = 2 p 2;

(11)

(d)

p+q

2 2

=

p

2 2

+

2Re

pHq

+

q

2 2

.

(12)

Proof: By the relationship of q, qR, and qH, we have

(a) pHT qH =

pμTqμ (=4)

pTq μ

μ∈{1,i,j,k}

μ∈{1,i,j,k}

(=7) 4Re pTq ;

(13)

(b)

4pRT qR

=

4pHRqR

(=7)

pHH J n

1 4

J

H n

qH

=

pHHqH

(=9) 4Re pHq ;

(14)

(c) 4

pR

2 2

=

4pTRpR

(1=0)

pHHpH

=

pH

2 2

(1=0) 4Re pHp = 4pHp = 4 p 22;

(15)

(d)

p+q

2 2

=

(p

+

q)H

(p

+

q)

= pHp + pHq + qHp + qHq

=

p

2 2

+

2Re

pHq

+

q 22.

(16)

For a real-differentiable function f (q) : Hn → R, the aug-

mented real gradient and the augmented quaternion gradient are

respectively deﬁned as ∇Rf

T

∂f ∂qR

and

⎛⎞

∇q f

∇Hf

∂f ∂qH

T

=

⎝⎜⎜∇∇qqji

f f

⎠⎟⎟,

(23)

∇qk f

where ∇qf

T

∂f ∂q

[25]. Their relationship is given by [37]

1 ∇H∗ f = 4 J n∇Rf

⇔

∇Rf = J nH∇H∗ f,

(24)

where ∇H∗ f = (∇Hf )∗. If f (q) is also second-order contin-

uous real-differentiable, the augmented real Hessian matrix,

and the augmented quaternion Hessian matrix are respectively

T

deﬁned as HRR

∂

∂f

∂qR ∂qR

, and

∂

∂f T

HHH∗ ⎛∂qH ∂q∗H

Hqq∗ Hqiq∗

= ⎜⎝⎜

H qqi∗ H qqj∗

H qiqi∗ H qiqj∗

H H qqk∗

qi qk∗

H qj q∗ H qj qi∗ H qj qj∗ H qj qk∗

⎞

H qk q∗

H qkqi∗ H qk qj∗

⎟⎠⎟,

(25)

H qkqk∗

This completes the proof.

T

where Hqq∗

∂ ∂f ∂q ∂q∗

. Their relationship is that [25]

B. GHR Calculus
A quaternion function f (q) = fa (qa, qb, qc, qd) + fb (qa, qb, qc, qd) i + fc (qa, qb, qc, qd) j + fd (qa, qb, qc, qd) k is called real-differentiable, if fa, fb, fc, fd are differentiable as functions of the real variables qa, qb, qc, qd [36].
Deﬁnition 2.1: (GHR derivatives [24]). If f : H → H is realdifferentiable, then the left GHR derivatives of the function f with respect to qμ and qμ∗(μ = 0, μ ∈ H) are deﬁned as

∂f 1 ∂qμ = 4

∂f − ∂f iμ − ∂f jμ − ∂f kμ

∂qa ∂qb

∂qc

∂qd

∈ H,

(17)

∂f 1 ∂qμ∗ = 4

∂f + ∂f iμ + ∂f jμ + ∂f kμ

∂qa ∂qb

∂qc

∂qd

∈ H,

(18)

where q = qa + qbi + qcj + qdk, qa, qb, qc, qd ∈ R, and

∂f ∂qa

,

∂f ∂qb

,

∂f ∂qc

,

∂f ∂qd

∈H

are

the

partial

derivatives

of

f

with

respect to qa, qb, qc, qd.

If f : H → R, g : H → R, the following rules hold [24]

∂(f g) ∂g ∂f ∂qμ = f ∂qμ + ∂qμ g,

∂f (g(q))

∂g

∂qμ = f (g) ∂qμ ,

∂f ν ∂f ∂qμ = ∂qνμ ,

∂f ∗ ∂f ∂qμ = ∂qμ∗ ,

∂(f g) ∂g ∂f ∂qμ∗ = f ∂qμ∗ + ∂qμ∗ g; (19)

∂f (g(q))

∂g

∂qμ∗ = f (g) ∂qμ∗ ; (20)

∂f ν ∂f

∂qμ∗ = ∂qνμ∗ ;

(21)

∂f ∗ ∂f

∂qμ∗ = ∂qμ .

(22)

H HH∗

=

1 16

J

n

H

RR

J

H n

⇔

H RR

=

J

H n

H

HH∗

J

n

.

(26)

Since (26) and HRR is symmetric, HHH∗ is Hermitian. Remark 1: Notice that we can also deﬁne two other
quaternion Hessian matrices Hq∗q and Hq∗q∗ , but for these it is difﬁcult to obtain the relationship between the augmented
quaternion Hessian matrix and its real counterpart (see (26)).
So they are omitted. Proposition 2.2: If the quaternion function f (q) : Hn → R
is real-differentiable, then ∀p, q ∈ Hn we have

(a) ∇Rf (pR)T qR = ∇H∗ f (pH)H qH

= 4Re ∇p∗ f (p)H q ;

(27)

(b) ∇Rf (pR)T ∇Rf (qR) = 4∇H∗ f (pH)H ∇H∗ f (qH)

= 16Re ∇p∗ f (p)H ∇q∗ f (q) ;

(28)

(c) ∇Rf (pR) 2 = 2 ∇Hf (pH) 2 = 4 ∇pf (p) 2. (29)

Proof:

By

(7),

(24),

J

H n

J

n

=

4I 4n ,

and

∇Rf

∈

Rn,

we

have

(a) ∇Rf (pR)T qR = ∇Rf (pR)H qR

(7)=(24)

∇H∗ f

(pH)H

Jn

1 4

J nHqH

= ∇H∗ f (pH)H qH

=

∇p∗ f (p)μH qμ

μ∈{1,i,j,k}

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

SUN et al.: CONVEX QUATERNION OPTIMIZATION FOR SIGNAL PROCESSING: THEORY AND APPLICATIONS

4109

(=4)

∇p∗ f (p)H q μ

where the set CR ⊂ R is convex. Therefore, we have

μ∈{1,i,j,k}

∇Rf (pR) − ∇Rf (qR) T (pR − qR)

(7)
= 4Re

∇p∗ f (p)H q

;

(30)

(2=7)4Re ∇p∗ f (p) − ∇q∗ f (q) H (p − q) .

(36)

(b) ∇Rf (pR)T ∇Rf (qR) = ∇Rf (pR)H ∇Rf (qR)

(2=4)

∇H∗

f

(pH)H

J

n

J

H n

∇H∗

f

(qH)

= 4∇H∗ f (pH)H ∇H∗ f (qH)

=4

∇p∗ f (p)μH ∇q∗ f (q)μ

μ∈{1,i,j,k}

(7)
= 16Re

∇p∗ f (p)H ∇q∗ f (q)

;

(31)

(c) Let q = p in (28).

III. DISCRIMINANT THEOREMS FOR CONVEX QUATERNION FUNCTIONS

This section aims to introduce several discriminant criteria for convex quaternion functions, including gradient monotonicity and second-order characterization. An example illustrates how these criteria are applied in practice.

Upon substituting (36) into (35), the proof follows. Since the following two theorems do not involve the inter-
change of products, quaternion gradients, or Hessian matrices, these can be easily derived using the methods from the real domain, as in Section 3.1 of [38] and Section 3.1 of [39].
Deﬁnition 3.1: (Epigraph). For the quaternion generalized real-valued function f (q) : Hn → R ∪ {±∞}, the set

epif = (q, t) ∈ Hn+1 | f (q) t, t ∈ R

(37)

is called the epigraph of f (q).
Theorem 3.2: The quaternion generalized real-valued function f (q) : C ⊂ Hn → R ∪ {±∞} is convex, iff epif is a
convex set. Theorem 3.3: The quaternion function f (q) : C ⊂ Hn → R
is convex iff ∀q ∈ C, v ∈ Hn, g : S → R, the function

g(t) = f (q + tv)

(38)

is convex, where S {t ∈ R | q + tv ∈ C} ⊂ R.

A. Convex Set and Convex Function
We begin by introducing the fundamental concepts, such as those of a convex set and convex function, as in Section 2.1 of [38]. The set C is called convex, if ∀x, y ∈ C, ∀θ ∈ [0, 1], θx + (1 − θ) y ∈ C. The set C can be a subset of Hn, R or H. The sets C ⊂ Hn, CR qR = qaT, qTb , qTc , qdT T | q ∈ C ⊂ R = R4n, and CH qH = qT, qiT, qjT, qkT T | q ∈ C ⊂ H ⊂ H4n are related as follows [22]
C is convex ⇔ CR is convex ⇔ CH is convex. (32)
A function f is said to be convex, if the domain of f (domf ) is convex, and ∀x, y ∈ domf , ∀θ ∈ [0, 1],
f θx + (1 − θ) y θf (x) + (1 − θ) f (y) . (33)
The range of function f is the real domain R, and domf can be a subset of Hn, R or H.

B. First-Order Characterization of Discriminant Theorems for Convex Quaternion Functions

A popular ﬁrst-order characterization was given in [22], [23]
and in (1). The other is gradient monotonicity, as follows.
Theorem 3.1: (Gradient monotonicity). Consider a convex set C ⊂ Hn and a real-differentiable quaternion function f (q) : C → R. Then, f (q) is convex if and only if (shortened to iff) ∀p, q ∈ C,

Re ∇p∗ f (p) − ∇q∗ f (q) H (p − q) 0.

(34)

Proof: From (32), C is convex iff CR is convex. We already

know from Section 2.1 of [38] that for a differentiable real

function, f (qR) is convex iff ∀pR, qR ∈ CR,

∇Rf (pR) − ∇Rf (qR) T (pR − qR) 0,

(35)

C. Second-Order Characterization of Discriminant Theorems for Convex Quaternion Functions

Before introducing the second-order characterization of con-
vex quaternion functions, we must deﬁne positive deﬁnite
quaternion matrices. Deﬁnition 3.2: (Positive deﬁnite matrix). The matrix A ∈
Hn×n is called positive deﬁnite, if

Re xHAx > 0, ∀x ∈ Hn, x = 0,

(39)

and is denoted by A O, where O is n × n zero matrix. Similarly, the matrix A ∈ Hn×n is called positive semi-
deﬁnite, if

Re xHAx 0, ∀x ∈ Hn, x = 0,

(40)

and is denoted by A O. Theorem 3.4: If the matrix A ∈ Hn×n satisﬁes AH = A,
then A is positive deﬁnite (positive semi-deﬁnite) iff

xHAx > 0 (xHAx 0), ∀x ∈ Hn, x = 0.

(41)

Proof: This is straightforward to prove by applying

Deﬁnition 3.2.

If a quaternion function f (q) is second-order continuous

real-differentiable, the Hessian matrix can be used to discrim-

inate its convexity, as shown below.

Theorem 3.5: (Second-order characterization). Consider

a convex set C ⊂ Hn and a second-order continuous real-

differentiable quaternion function f (q) : C → R. Then, the

following three statements are equivalent:

(a) f (q) is convex;

(b) HHH∗ O;

(c)

Re xHH qν q∗ xν

ν∈{1,i,j,k}

0, ∀x ∈ Hn, x = 0.

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

4110

IEEE TRANSACTIONS ON SIGNAL PROCESSING, VOL. 71, 2023

Proof: We ﬁrst show that (a) is equivalent to (b). From (32), the set C is convex iff the set CR is convex. We already know from Section 2.1 of [38] that for a second-order continuous differentiable function, f (qR) is convex iff

HRR O, ∀qR ∈ CR,

(42)

where CR ⊂ R is convex. Then, ∀xH ∈ H, xH = 0, we have

xHH H HH∗

xH

(2=6)

1 16

xHHJ

nH RRJ

nHxH

1 =
16

H
J Hn xH H RR

J

H n

xH

(=7) xRH H RRxR.

(43)

Since HHH∗ is a Hermitian matrix, we have

HHH∗ O ⇔ HRR O,

(44)

TABLE I
SEVERAL DERIVATIVES PERFORMED BY THE GHR CALCULUS FROM TABLE IV OF [26], ∀A ∈ Hn×n, ∀a ∈ Hn, ∀b ∈ Hn,
∀α ∈ H, ∀β ∈ H

f (q) or f (q) aTqβ αqHb Aqβ qHAq

∂f ∂q

or

∂f ∂q

aTRe{β}

−

1 2

αbH

ARe {β}

qHA

−

1 2

(Aq)H

∂f ∂q∗

or

∂f ∂q∗

−

1 2

aT

β∗

αRe bT

−

1 2

Aβ

∗

−

1 2

qHA

+

Re

(Aq)T

Theorem 3.6: Consider a convex set C ⊂ Hn and a secondorder continuous real-differentiable quaternion function f (q) : C → R. If f (q) is convex, then

which concludes that (a) equals (b). Next, to show that (b) is equivalent to (c), ∀xH ∈ H, xH = 0,
we have

xHH⎛HxHH⎞∗Hx⎛H H qq∗

= ⎜⎜⎝xxji ⎟⎟⎠

⎜⎜⎝

H qqi∗ H qqj∗

xk

H qqk∗

H qiq∗ H qiqi∗ H qiqj∗ H qiqk∗

H qj q∗ H qj qi∗ H qj qj∗ H qj qk∗

=

xμHH qν qμ∗ xν

μ,ν∈{1,i,j,k}

(=7) 4

Re xHH qν q∗ xν .

ν∈{1,i,j,k}

⎞⎛ ⎞

H qk q∗

x

H qkqi∗ H qk qj∗

⎟⎟⎠⎝⎜⎜xxji ⎟⎟⎠

H qkqk∗

xk

(45)

Since HHH∗ is a Hermitian matrix, we obtain

Hqq∗ O.

(49)

Proof: Upon applying Theorem 3.5, together with the convexity of f (q), we have HHH∗ O. By (25) and Lemma 3.1, we ﬁnally obtain Hqq∗ O.

D. An Example of Convex Quaternion Function
We next provide a basic example to determine the convexity of a quaternion function. In this example, we use certain GHR derivatives presented in Table IV of [26], which are included in Table I here.
Example 3.1: If f (q) = Aq − b 22, ∀q ∈ Hn, A ∈ Hm×n, b ∈ Hm, then f (q) is convex.
Proof: (First-order characterization criterion) By the definition of 2-norm, we have

Re xHH qν q∗ xν
ν∈{1,i,j,k}
⇔ H HH∗

0, ∀x ∈ Hn, x = 0

O.

(46)

This concludes that (b) equals (c).
From Theorem 3.5, we obtain the following result. Corollary 3.1: Consider a convex set C ⊂ Hn and a secondorder continuous real-differentiable quaternion function f (q) : C → R. If

Hqq∗ O, and Hqνq∗ = O, ν ∈ {i, j, k} , (47)

then f (q) is convex.
Proof: Since Hqq∗ O, and Hqνq∗ = O, ν ∈ {i, j, k}, we have ∀x ∈ Hn, x = 0,

Re xHHqν q∗ xν = Re xHHqq∗ x
ν∈{1,i,j,k}

0. (48)

By Theorem 3.5, f (q) is convex. Lemma 3.1: The quaternion matrix A ∈ Hn×n is positive
deﬁnite (positive semi-deﬁnite), iff all principal submatrices of A are positive deﬁnite (positive semi-deﬁnite).
Proof: The proof follows the same steps as its counterpart in the real ﬁeld in Section 7.1 of [40].
Upon applying Lemma 3.1, we can obtain a necessary condition for convex quaternion functions.

f (q) =

Aq − b

2 2

= (Aq − b)H (Aq − b)

= qHAHAq − qHAHb − bHAq + bHb.

(50)

Upon using the ﬁrst, the second, and the fourth rows of Table I, we take the gradient of f (q) with respect to q∗ to yield

∇q∗ f (q)

∂f ∂q∗

T
(2=2)

∂f H ∂q

= 1 AHAq + 1 AHb − AHb

2

2

= 1 AH (Aq − b) .

(51)

2

Next, ∀p, q ∈ Hn, we obtain

f (q) − f (p) − 4Re ∇p∗ f (p)H (q − p)

= (Aq − b)H (Aq − b) − (Ap − b)H (Ap − b)

− 2Re

AH (Ap − b)

H
(q − p)

= qHAHAq + pHAHAp − pHAHAq − qHAHAp

= (q − p)H AHA (q − p)

=

A (q − p)

2 2

0.

(52)

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

SUN et al.: CONVEX QUATERNION OPTIMIZATION FOR SIGNAL PROCESSING: THEORY AND APPLICATIONS

4111

Then, by (1), the quaternion function f (q) is convex. (Gradient monotonicity criterion) ∀p, q ∈ Hn, we have

Re (∇p∗ f (p) − ∇q∗ f (q))H (p − q)

1 = Re

H
AH (Ap − b) − AH (Aq − b) (p − q)

2

1 = Re

(p − q)H AHA (p − q)

2

= 1 (p − q)H AHA (p − q) 2

1 =
2

A (q − p)

2 2

0.

(53)

From Theorem 3.1, we know that f (q) is convex. (Second-order characterization criterion) Using the third
row of Table I, we have

H qq∗

∂ ∂q

∂f ∂q∗

T = ∂∇q∗ f (q) ∂q

∂ 1 AH (Aq − b)

(5=1)

2

= 1 AHA O,

(54)

∂q

2

and for any ν ∈ {i, j, k},

H qν q∗

∂ ∂qν

∂f ∂q∗

T

=

∂∇q∗ f (q) ∂qν

∂ (5=1)

1 AH (Aq − b) 2
∂qν

(1=9)

1 2

AH

A

∂q ∂qν

= O.

(55)

By Corollary 3.1, we know that f (q) is convex.

IV. DISCRIMINANT THEOREMS FOR STRONGLY CONVEX QUATERNION FUNCTIONS

We shall now discuss the discriminant criteria for strongly

convex quaternion functions, building upon the theorems for

convexity. These criteria will be helpful for designing optimiza-

tion algorithms.

Deﬁnition 4.1: (Strongly convex function). The quaternion function f (q) : C ⊂ Hn → R is called strongly convex, if ∀p,

q ∈ C, ∀θ ∈ [0, 1], ∃σ > 0,

f θp+(1−θ)q

θf

(p)+(1−θ)f

(q)−

σ 2

θ(1−θ)

p−q

22,

(56)

where σ is the strongly convex parameter. For convenience,

f (q) is also called σ-strongly convex.

We obtain the following equivalence theorem based on the

deﬁnition of strongly convex functions. Theorem 4.1: The quaternion function f (q) : C ⊂ Hn → R

is σ-strongly convex, iff ∃σ > 0, s.t. the function

g (q)

f (q) − σ 2

q

2 2

(57)

is convex.

Similar to convex quaternion functions, strongly convex

quaternion functions also have ﬁrst-order characterization, gra-

dient monotonicity, and second-order characterization.

Theorem 4.2: (First-order characterization). Consider a convex set C ⊂ Hn and a real-differentiable quaternion function f (q) : C → R. Then, f (q) is σ-strongly convex iff ∀p, q ∈ C,

f (q)

f (p) + 4Re

∇p∗ f (p)H (q − p)

σ +
2

q−p

2 2

.

(58)

Proof: From Theorem 4.1, f (p) is strongly convex iff g (p) =

f

(p)

−

1 2

σ

p

2 2

is

convex.

By

(1),

∀p,

q

∈

C,

g (q) g (p) + 4Re ∇p∗ g (p)H (q − p) . (59)

Using the fourth row of TABLE I, ∇p∗ g (p) = ∇p∗ f (p) −

1 4

σp.

(59)

becomes

f (q) − σ 2

q

2 2

f

(p)

−

σ 2

p

2 2

+

4Re

∇p∗ f (p) −

σ p
4

H (q − p)

.

(60)

Upon substituting

σ 2

q

2 2

−

σ 2

p

2 2

+

4Re

∇p∗ f (p) −

σ p
4

H (q − p)

= 4Re

∇p∗ f (p)H (q − p)

− σRe

pHq

+σ

p

2 2

σ +
2

q

2 2

−

σ 2

p

2 2

(1=2) 4Re

∇p∗ f (p)H (q − p)

σ +
2

q−p

2 2

(61)

into (60), we obtain (58).
Theorem 4.3: (Gradient monotonicity). Consider a convex set C ⊂ Hn and a real-differentiable quaternion function f (q) : C → R. Then, f (q) is σ-strongly convex iff ∀p, q ∈ C,

Re ∇p∗ f (p)−∇q∗ f (q) H (p − q)

σ 4

p−q

2 2

.

(62)

Proof: From Theorem 4.1, f (q) is strongly convex

iff

g

(q)

=

f

(q)

−

1 2

σ

q

2 2

is

convex.

Upon

applying

Theorem 3.1, we have

Re (∇p∗ g (p) − ∇q∗ g (q))H (p − q) 0, ∀p, q ∈ C. (63)

Using the fourth row of TABLE I, we have ∇q∗ g (q) =

∇q∗ f

(q)

−

1 4

σq.

Then

(63)

becomes

Re

∇p∗ f (p) −

σ 4 p − ∇q∗ f (q) +

σ q
4

H (p − q)

0.

(64)

After rearranging the terms in (64), we obtain (62).

Theorem 4.4: (Second-order characterization). Consider

a convex set C ⊂ Hn and a second-order continuous real-

differentiable quaternion function f (q) : C → R. Then, the fol-

lowing three statements are equivalent:

(a) f (q) is σ-strongly convex;

(b) HHH∗

1 4

σI

4n;

(c)

Re xHH qν q∗ xν

ν∈{1,i,j,k}

x = 0.

−

1 4

σ

x

2 2

0, ∀x ∈ Hn,

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

4112

IEEE TRANSACTIONS ON SIGNAL PROCESSING, VOL. 71, 2023

Proof: We ﬁrst show that (a) is equivalent to (b).

Deﬁne

g (q)

f (q) −

1 2

σ

q

2 2

,

h(q)

2

q

2 2

=

2qHq

=

2 qHq μ (=4) 2qμHqμ, μ ∈ {1, i, j, k}. From the fourth row of

TABLE I, we have

∂h ∂qμ∗

T
= qμ,

μ ∈ {1, i, j, k} .

(65)

Then, ∀μ ∈ {1, i, j, k},

∂ ∂qμ

∂h ∂qμ∗

T

(6=5)

∂qμ ∂qμ

= In,

(66)

and ∀μ, ν ∈ {1, i, j, k}, μ = ν,

∂ ∂qν

∂h ∂qμ∗

T

(6=5)

∂qμ ∂qν

=

O.

(67)

By (25), the augmented quaternion Hessian matrix of h is I4n.

Therefore, the augmented quaternion Hessian matrix of g is

H HH∗

−

1 4

σI

4n.

By

Theorem

3.5,

we

conclude

that

(a)

is

equivalent to (b).

Next, to show that (b) is equivalent to (c), ∀xH ∈ H, xH = 0,

we have

xHH

σ H HH∗ − 4 I4n

xH

=

xHH H HH∗ xH

−

σ 4

xHH xH

(1=1)

xμHH qν qμ∗ xν − σxHx

μ,ν∈{1,i,j,k}

(=7) 4

Re xHHqν q∗ xν − σ x 22.

ν∈{1,i,j,k}

(68)

Since

H HH∗

is

a

Hermitian

matrix,

H HH∗

−

1 4

σI

4n

is

also

a

Hermitian matrix. ∀x ∈ Hn, x = 0,

Re

xHH qν q∗ xν

−σ 4

x

2 2

0,

ν∈{1,i,j,k}

σ ⇔ HHH∗ − 4 I4n O.

(69)

This concludes that (b) is equivalent to (c).

From Theorem 4.4, we obtain the following result.

Corollary 4.1: Consider a convex set C ⊂ Hn and a second-

order continuous real-differentiable quaternion function f (q) :

C → R. If

σ

Hqq∗ 4 In, and Hqνq∗ = O, ν ∈ {i, j, k} ,

(70)

then f (q) is σ-strongly convex. By Theorem 4.4 and Lemma 3.1, we can obtain a necessary
condition for σ-strongly convex quaternion functions. Theorem 4.5: Consider a convex set C ⊂ Hn and a second-
order continuous real-differentiable quaternion function f (q) : C → R. If f (q) is σ-strongly convex, then

σ

Hqq∗ 4 In.

(71)

Proof: Note that f (q) is σ-strongly convex, and upon

applying Theorem 4.4, we have HHH∗

1 4

σI 4n .

By

(25)

and

Lemma 3.1, we ﬁnally obtain Hqq∗

1 4

σI

n.

Theorem 4.6: (Quadratic termination). For the positive definite quadratic function f (q) = qH Aq + Re{bH q} + c, b ∈ Hn, c ∈ R, and the matrix A ∈ Hn×n is Hermitian and positive deﬁnite. Then, the quaternion Newton (QN) method converges
with one step.
Proof: From (51), (54), and (55), it is straightforward to
compute the gradient of f (q)

1

1

∇q∗ f

(q)

=

Aq 2

+

b, 4

(72)

and the Hessian matrices of f (q)

H qq∗

=

∂∇q∗ f ∂q

(q)

=

1 A,
2

(73)

for any ν ∈ {i, j, k},

H qν q∗

=

∂∇q∗ f (q) ∂qν

=

O.

(74)

By setting ∇q∗ f (q) = 0 as per (72), we can obtain the closedform solution

qopt

=

−

1 2

A−1b.

(75)

By (74), the update rule of QN [25] is expressed as

q1

=

q0

−

H

−1 qq∗

∇q∗

f

q0

= q0 − A−1

Aq0

+

1 b

2

= − 1 A−1b 2

(7=5) qopt,

(76)

where q0 is initial vector. Therefore, the QN method reaches the optimal solution within one iteration for the positive deﬁnite quadratic function, i.e., quadratic termination.

V. APPLICATIONS OF CONVEX QUATERNION OPTIMIZATION IN SIGNAL PROCESSING

This section analyzes and solves two representative applications using the proposed convex quaternion optimization theory in this paper.
Application 5.1: (QCRC). The quaternion collaborative representation-based classiﬁcation (QCRC) effectively captures the structural correlation among color channels in color images [41], [42]. The QCRC model can be expressed as

min f (q) =
q∈Hn

Aq − b

2 2

+

λ

q

22,

(77)

where A ∈ Hm×n is a matrix consisting of input features, b ∈ Hm is a vector comprising labels, and λ > 0. By (51), (54), and
(55), the gradient of f (q) is

∇q∗ f

(q)

=

1 AH 2

(Aq

−

b)

+

1 λq,
2

(78)

and the Hessian matrices of f (q) are

H qq∗

=

∂∇q∗ f ∂q

(q)

=

1 AHA 2

+

1 2 λIn,

(79)

and

H qν q∗

=

∂∇q∗ f (q) ∂qν

= O,

ν ∈ {i, j, k} .

(80)

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

SUN et al.: CONVEX QUATERNION OPTIMIZATION FOR SIGNAL PROCESSING: THEORY AND APPLICATIONS

4113

Fig. 2. Numerical validation of quaternion gradient descent (QGD) algorithm and quaternion Newton (QN) method for QCRC, over a range of parameters. Observe that the QN method (blue line) converges to f (qopt) (solid black line) in one step.

Since AHA O, we have Hqq∗

1 2

λI

n.

According

to

Corol-

lary 4.1, f (q) is 2λ-strongly convex. By setting ∇q∗ f (q) = 0

as per (78), we obtain the closed-form solution

−1

qopt = AHA + λIn AHb.

(81)

Next, we aim to test the convergence performance of the quaternion iteration algorithms for solving the QCRC problem. In particular, the QN method can converge in one step, so its computational cost is equivalent to (81). However, many optimization problems are too complex to have closed-form solutions, so iterative algorithms will have to be used. By the strong convexity of f (q), we can employ the quaternion gradient descent (QGD) algorithm and the QN method [25] to ﬁnd the optimal solution to problem (77). The update rule of QGD is

qt+1 = qt − 4η∇q∗ f qt

= qt − 2η AH(Aqt − b) + λqt ,

(82)

where η > 0 is the step size. By (80), the update rule of QN can be expressed as

qt+1

=

qt

−

H

−1 qq∗

∇q∗

f

qt

= qt − AHA + λIn −1 AH(Aqt − b) + λqt . (83)

All algorithms employed the same data matrix A, vector b, initial vector q0 = 0, and 2λ = 0.1, where λ can be optimized
by grid search [42], and we follow 3D Basis Pursuit Denoising [22] to set λ = 0.05. We generated a matrix A ∈ H10×1000 and a vector b ∈ H10, where the four real parts of A are i.i.d. sampled
from a unit Gaussian distribution and b is normalized with
2-norm, in Fig. 2(a). In Fig. 2(b) and (c), A and b were generated in the same way, but with different scales: A ∈ H1000×10 and b ∈ H1000 are in (b); A ∈ H1000×1000 and b ∈ H1000 are in
(c). The numerical experiments of this application and subse-
quent experiments were completed using the Quaternion Toolbox for Matlab1 (QTFM).
The performance curves of the objective function for 30 iterations are plotted in Fig. 2. We can clearly see that f (qk)
converges to f (qopt), but f (qopt) = 0 in Fig. 2(b) because it is underdetermined. Larger step sizes result in a faster descent

1QTFM: https://sourceforge.net/projects/qtfm/

in the QGD algorithm, but the performance of the QN method is the best. Compared with the closed-form solution, the QGD algorithm has lower computational cost per step because there is no matrix inversion operation. The QN method converges in one step, consistent with Theorem 4.6, so its calculation cost is the same as the closed-form solution. QN can also solve optimization problems without closed-form solutions.
Application 5.2: (QBLR). Logistic regression is the most fundamental linear classiﬁcation model. We considered a quaternion binary logistic regression (QBLR) model

min
q∈Hm

1 (q) =
n

n

ln(1 + exp(−biRe{aHi q})) + λ

q

2 2

.

i=1

(84)

where the provided data pairs {ai, bi}in=1 are independent and identically distributed, ai ∈ Hm, bi ∈ {1, −1}, and λ > 0. It can be showed that

∇q∗

(q)

1 =
2n

n i=1

1

exp(−biRe{aiHq}) + exp(−biRe{aiHq})

(−biai)

+

1 λq
2

1n

1

=− 2n

(1

−

gi(q))

biai

+

λq, 2

(85)

i=1

1 where gi(q) = 1 + exp(−biRe{aiHq}) . Further, the Hessian matrices of (q) are

1 Hqq∗ = 2n

n

biai

∂gi (q) ∂q

+

1 2 λIm

i=1

1n

= 4n

bi

i=1

exp(−biRe{aHi q}) 1 + exp(−biRe{aHi q})

2 biaiaiH

+

λ 2 Im

1 =
4n

n

(1

−

gi(q))

gi(q)aiaHi

+

λ 2 Im,

(86)

i=1

and for any ν ∈ {i, j, k},

Hqν q∗ = O.

(87)

Since aiaiH

O in (86), we know Hqq∗

1 2

λI m .

By

Corol-

lary 4.1, we conclude that (q) is 2λ-strongly convex.

Using the matrix notation, we can express the above

results in a more compact form. By deﬁning the matrix

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

4114

IEEE TRANSACTIONS ON SIGNAL PROCESSING, VOL. 71, 2023

Fig. 3. Numerical validation of QGD and QN for QBLR.

A = (a1, a2, . . . , an) ∈ Hm×n,

the

vector

b=

(b1, b2, . . . , bn)T, and g(q) = (g1(q), g2(q), . . . , gn(q))T,

the gradient and the Hessian matrix of (q) can be rewritten as

1

1

∇q∗

(q) = − A(b − b 4n

g(q)) + λq, 2

(88)

Hqq∗

=

1 AW (q)AH 4n

+

1 2 λIm,

(89)

where denotes the Hadamard product, and W (q) is a diagonal matrix generated by {gi(q) (1 − gi(q))}in=1.
We next solve the optimization problem (84) using the QGD
algorithm and the QN method [25]. The update rule of the QGD
algorithm is given by

qt+1 = qt − 4η∇q∗ qt

= qt

+

η A(b

−

b

g(qt)) − 2ηλqt,

(90)

n

where η > 0 is the step size. From (87), the update rule of the QN method can be expressed as

qt+1

=

qt

−

H

−1 qq∗

∇q∗

qt = qt

+ AW (qt)AH+2λnIm −1 A(b−b

g(qt))−2λnqt . (91)

We selected a dataset of ECG sequence2, split the available 5000 data into a training set of 4500 data and a test set of 500 data, and combined 140 real features into 35 quaternion features. Different combinations may slightly affect classiﬁcation performances, but do not affect the veriﬁcation of convergence results. The results of numerical experiments for 30 iterations are plotted in Fig. 3 with 2λ = 0.1. Observe that the training loss of QN and QGD gradually decreased as k increased. Since the objective function of QBLR is not quadratic, QN did not converge within one step, but it still exhibited better convergence than QGD. The test accuracy of QN gradually approached 96% as k increased, and QN ﬁnally reached the highest test accuracy, as shown in Fig. 3.

VI. CONCLUSION We have established the theory of convex optimization in quaternion variables. This has been achieved based on the
2ECG sequence: https://www.kaggle.com/datasets/salsabilahmid/ecgtxt

GHR calculus, an enabling methodology in quaternion signal processing and machine learning. This has resulted in the development of several discriminant theorems for convex functions in the quaternion ﬁeld, utilizing (7), (23), (24), (25), and (26). Furthermore, we have provided several discriminant criteria for strongly convex functions of quaternions by employing the results for convex quaternion functions. In addition, we have proven that the quaternion Newton method can converge in a single step for positive deﬁnite quadratic functions. The analysis has been supported by two signal processing applications using the proposed convex quaternion optimization theories, which have enriched the theory of convex quaternion optimization and established a theoretical foundation for quaternion signal processing. While the convexity of non-differentiable quaternion functions by the GHR calculus remains an open problem, our work has provided a foundation and an avenue for further research in this direction.
ACKNOWLEDGMENT
The authors would like to thank the three anonymous reviewers for their expert and constructive comments and suggestions, which have led to important improvements.
REFERENCES
[1] W. R. Hamilton, “On a new species of imaginary quantities, connected with the theory of quaternions,” in Proc. Roy. Irish Acad. (1836-1869), vol. 2. Ireland: JSTOR, 1840, pp. 424–434.
[2] L. Qi, Z. Luo, Q. Wang, and X. Zhang, “Quaternion matrix optimization: Motivation and analysis,” J. Optim. Theory Appl., vol. 193, nos. 1–3, pp. 621–648, 2022.
[3] Z. Jia, Q. Jin, M. K. Ng, and X. Zhao, “Non-local robust quaternion matrix completion for large-scale color image and video inpainting,” IEEE Trans. Image Process., vol. 31, pp. 3868–3883, 2022.
[4] C. C. Took and D. P. Mandic, “Augmented second-order statistics of quaternion random signals,” Signal Process., vol. 91, no. 2, pp. 214– 224, 2011.
[5] J. Flamant, S. Miron, and D. Brie, “Quaternion non-negative matrix factorization: Deﬁnition, uniqueness, and algorithm,” IEEE Trans. Signal Process., vol. 68, pp. 1870–1883, 2020.
[6] C. C. Took and D. P. Mandic, “A quaternion widely linear adaptive ﬁlter,” IEEE Trans. Signal Process., vol. 58, no. 8, pp. 4427–4431, Aug. 2010.
[7] H. Zhang, Z. Wang, D. Chen, S. Zhu, and D. Xu, “Quaternion extreme learning machine based on real augmented representation,” IEEE Signal Process. Lett., vol. 30, pp. 175–179, 2023.

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.

SUN et al.: CONVEX QUATERNION OPTIMIZATION FOR SIGNAL PROCESSING: THEORY AND APPLICATIONS

4115

[8] S. Walia, K. Kumar, and M. Kumar, “Unveiling digital image forgeries using Markov based quaternions in frequency domain and fusion of machine learning algorithms,” Multimedia Tools Appl., vol. 82, no. 3, pp. 4517–4532, 2023.
[9] B. C. Ujang, C. C. Took, and D. P. Mandic, “Quaternion-valued nonlinear adaptive ﬁltering,” IEEE Trans. Neural Netw., vol. 22, no. 8, pp. 1193–1206, Aug. 2011.
[10] J. Flamant, N. Le Bihan, and P. Chainais, “Time-frequency analysis of bivariate signals,” Appl. Comput. Harmon. Anal., vol. 46, no. 2, pp. 351–383, 2019.
[11] T. Ogunfunmi and C. Safarian, “The quaternion stochastic information gradient algorithm for nonlinear adaptive systems,” IEEE Trans. Signal Process., vol. 67, no. 23, pp. 5909–5921, Dec. 2019.
[12] E. C. Mengüç, “Design of quaternion-valued second-order Volterra adaptive ﬁlters for nonlinear 3-D and 4-D signals,” Signal Process., vol. 174, 2020, Art. no. 107619.
[13] Y. Xia, S. Tao, Z. Li, M. Xiang, W. Pei, and D. P. Mandic, “Full mean square performance bounds on quaternion estimators for improper data,” IEEE Trans. Signal Process., vol. 67, no. 15, pp. 4093–4106, Aug. 2019.
[14] S. Enshaeifar, S. Kouchaki, C. C. Took, and S. Sanei, “Singular spectrum analysis of electroencephalogram with application in sleep analysis,” IEEE Trans. Neural Syst. Rehabil., vol. 24, no. 1, pp. 57–67, Jan. 2016.
[15] Z. Luo and W. Yu, “An introduction to convex optimization for communications and signal processing,” IEEE J. Sel. Areas Commun., vol. 24, no. 8, pp. 1426–1438, Aug. 2006.
[16] S. Sra, S. Nowozin, and S. J. Wright, Optimization for Machine Learning. Cambridge, MA, USA: MIT Press, 2012.
[17] M. Jaggi, “Sparse convex optimization methods for machine learning,” Ph.D. dissertation, ETH Zürich, Zürich, Switzerland, 2011.
[18] N. Krejic´, N. K. Jerinkic´, and T. Ostojic´, “An inexact restorationnonsmooth algorithm with variable accuracy for stochastic nonsmooth convex optimization problems in machine learning and stochastic linear complementarity problems,” J. Comput. Appl. Math., vol. 423, 2023, Art. no. 114943.
[19] Y. Xia and D. P. Mandic, “Complementary mean square analysis of augmented CLMS for second-order noncircular Gaussian signals,” IEEE Signal Process. Lett., vol. 24, no. 9, pp. 1413–1417, Sep. 2017.
[20] Y. Xia and D. P. Mandic, “A full mean square analysis of CLMS for second-order noncircular inputs,” IEEE Trans. Signal Process., vol. 65, no. 21, pp. 5578–5590, Nov. 2017.
[21] A. B. Gershman, N. D. Sidiropoulos, S. Shahbazpanahi, M. Bengtsson, and B. Ottersten, “Convex optimization-based beamforming,” IEEE Signal Process. Mag., vol. 27, no. 3, pp. 62–75, May 2010.
[22] J. Flamant, S. Miron, and D. Brie, “A general framework for constrained convex quaternion optimization,” IEEE Trans. Signal Process., vol. 70, pp. 254–267, 2022.
[23] Y. Liu, Y. Zheng, J. Lu, J. Cao, and L. Rutkowski, “Constrained quaternion-variable convex optimization: A quaternion-valued recurrent neural network approach,” IEEE Trans. Neural Netw. Learn. Syst., vol. 31, no. 3, pp. 1022–1035, Mar. 2020.

[24] D. Xu, C. Jahanchahi, C. C. Took, and D. P. Mandic, “Enabling quaternion derivatives: The generalized HR calculus,” Roy. Soc. Open Sci., vol. 2, no. 8, 2015, Art. no. 150255.
[25] D. Xu, Y. Xia, and D. P. Mandic, “Optimization in quaternion dynamic systems: Gradient, Hessian, and learning algorithms,” IEEE Trans. Neural Netw. Learn. Syst., vol. 27, no. 2, pp. 249–261, Feb. 2016.
[26] D. Xu and D. P. Mandic, “The theory of quaternion matrix derivatives,” IEEE Trans. Signal Process., vol. 63, no. 6, pp. 1543–1556, Mar. 2015.
[27] W. Wirtinger, “Zur formalen theorie der funktionen von mehr komplexen veränderlichen,” Mathematische Annalen, vol. 97, no. 1, pp. 357– 375, 1927.
[28] D. Brandwood, “A complex gradient operator and its application in adaptive array theory,” Proc. Inst. Elect. Eng. H, vol. 130, no. 1, pp. 11–16, 1983.
[29] P. Arena, L. Fortuna, G. Muscato, and M. G. Xibilia, “Multilayer perceptrons to approximate quaternion valued functions,” Neural Netw., vol. 10, no. 2, pp. 335–342, 1997.
[30] M. Yoshida, Y. Kuroe, and T. Mori, “A model of Hopﬁeld-type quaternion neural networks and its energy function,” in Proc. Int. Conf. Neural Inf. Process., Berlin, Heidelberg: Springer, 2004, pp. 110–115.
[31] E. C. Mengüç, “Novel quaternion-valued least-mean kurtosis adaptive ﬁltering algorithm based on the GHR calculus,” IET Signal Process., vol. 12, no. 4, pp. 487–495, 2018.
[32] C. C. Took and Y. Xia, “Multichannel quaternion least mean square algorithm,” in Proc. IEEE Int. Conf. Acoust., Speech Signal Process., 2019, pp. 8524–8527.
[33] T. Parcollet, M. Morchid, and G. Linarès, “A survey of quaternion neural networks,” Artif. Intell. Rev., vol. 53, pp. 2957–2982, 2020.
[34] J. Ward, Quaternions and Cayley Numbers: Algebra and Applications. Dordrecht, The Netherlands: Springer Science, 1997.
[35] J. Vía, D. Ramírez, and I. Santamaría, “Properness and widely linear processing of quaternion random vectors,” IEEE Trans. Inf. Theory, vol. 56, no. 7, pp. 3502–3515, Jul. 2010.
[36] A. Sudbery, “Quaternionic analysis,” Proc. Math. Cambridge Philos. Soc., vol. 85, no. 2, pp. 199–225, 1979.
[37] D. P. Mandic, C. Jahanchahi, and C. C. Took, “A quaternion gradient operator and its applications,” IEEE Signal Process. Lett., vol. 18, no. 1, pp. 47–50, Jan. 2011.
[38] Y. Nesterov, Lectures on Convex Optimization. Cham, Switzerland: Springer, 2018.
[39] S. Boyd and L. Vandenberghe, Convex Optimization. New York, NY, USA: Cambridge Univ. Press, 2004.
[40] R. A. Horn and C. R. Johnson, Matrix Analysis. New York, NY, USA: Cambridge Univ. Press, 2012.
[41] C. Zou, K. I. Kou, and Y. Wang, “Quaternion collaborative and sparse representation with application to color face recognition,” IEEE Trans. Image Process., vol. 25, no. 7, pp. 3287–3302, Jul. 2016.
[42] S. Lazendic, H. De Bie, and A. Pizurica, “On extending the ADMM algorithm to the quaternion algebra setting,” in Proc. IEICE Inf. Commun. Technol. Forum, vol. 64. IEICE Europe Section, 2021, pp. 1–4.

Authorized licensed use limited to: Tokyo University of Agriculture and Technology. Downloaded on July 29,2026 at 09:23:23 UTC from IEEE Xplore. Restrictions apply.


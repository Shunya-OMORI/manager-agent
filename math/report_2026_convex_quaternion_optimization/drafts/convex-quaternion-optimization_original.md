# Convex Quaternion Optimization for Signal Processing: Theory and Applications

- Source PDF: `C:\Users\Projects\research\manager-agent\math\report_2026_convex_quaternion_optimization\paper.pdf`
- Extraction: `pdftotext` reading-order text
- Verification status: unverified draft

> This file is an extraction aid. Check headings, paragraph order, hyphenation, equations, tables, figure captions, references, and numeric values against the PDF before treating it as accurate.

---

1
Convex Quaternion Optimization for Signal Processing: Theory and Applications
Shuning Sun, Qiankun Diao, Dongpo Xu, Pauline Bourigault and Danilo P. Mandic, Fellow, IEEE

arXiv:2305.06879v1 [math.OC] 9 May 2023

Abstract—Convex optimization methods have been extensively used in the ﬁelds of communications and signal processing. However, the theory of quaternion optimization is currently not as fully developed and systematic as that of complex and real optimization. To this end, we establish an essential theory of convex quaternion optimization for signal processing based on the generalized Hamilton-real (GHR) calculus. This is achieved in a way which conforms with traditional complex and real optimization theory. For rigorous, We present ﬁve discriminant theorems for convex quaternion functions, and four discriminant criteria for strongly convex quaternion functions. Furthermore, we provide a fundamental theorem for the optimality of convex quaternion optimization problems, and demonstrate its utility through three applications in quaternion signal processing. These results provide a solid theoretical foundation for convex quaternion optimization and open avenues for further developments in signal processing applications.
Keywords—Convex quaternion functions, strongly convex quaternion functions, convex quaternion optimization, quaternion signal processing.
I. INTRODUCTION
Q UATERNIONS were ﬁrst introduced by William Hamilton in 1843 as an associative but non-commutative algebra over the real numbers [1]. Since then, they have become a powerful tool in many ﬁelds, including image processing [2, 3], signal processing [4–6], and machine learning [7–9]. Examples include the work by Jia et al. [3], who introduced a robust method for quaternion matrix completion, that can be used to reconstruct large-scale color images. Flamant et al. [10] demonstrated the efﬁciency of Quaternion Fourier Transform (QFT) in processing bivariate signals. Ogunfunmi et al. [11] presented a kernel adaptive ﬁlter for quaternion data. Moreover, Mengu¨c¸ et al. [12] designed quaternion-valued second-order Volterra adaptive ﬁlters for nonlinear 3-D and 4D signal processing. Xia et al. [13] established an estimation framework for processing quaternion-valued Gaussian data. Finally, Zhang et al. [7] discussed a new method for reducing the computation cost of quaternion signal estimation. Enshaeifar et al. [14] introduced quaternion-valued singular spectrum analysis for multichannel electroencephalogram analysis.
This work was funded in part by the National Natural Science Foundation of China (No. 62176051), in part by National Key R&D Program of China (No. 2021YFA1003400), and in part by the Fundamental Research Funds for the Central Universities of China (No. 2412020FZ024). (Corresponding author: Dongpo Xu)
Shuning Sun, Qiankun Diao and Dongpo Xu are with the Key Laboratory for Applied Statistics of MOE, School of Mathematics and Statistics, Northeast Normal University, Changchun, 130024, China. (e-mail: xudp100@nenu.edu.cn)
Pauline Bourigault and Danilo P. Mandic are with the Department of Electrical and Electronic Engineering, Imperial College London, London SW7 2AZ, UK. (e-mail: d.mandic@imperial.ac.uk)

The theory of real-valued and complex-valued convex optimization is well-established and has seen widely used in the areas of communications [15], machine learning [16–18] and signal processing [19–21]. In recent years, convex quaternion optimization has also attracted interest. For example, Qi et al. [2] studied ﬁrst-order derivatives and second-order partial derivatives of real-valued functions of quaternion variables over their real and imaginary i, j, k parts. However, this complicates the proof and computational process in quaternion optimization. Flamant et al. [22] and Liu et al. [23] provided ﬁrst-order characterization of quaternion functions by generalized Hamilton-real (GHR) calculus [24]. However, these useful attempts lack the discussion of gradient monotonicity and second-order characterization for convex quaternion function, a pre-requisite for practical applications.

To ﬁll this void, we have systematically address the theory of convex optimization in the quaternion domain. For rigorous, this is achieved based on the GHR calculus [24], a generalization of Wirtinger-calculus [25–27] from the complex domain to the quaternion ﬁeld. Before the introduction of the GHR calculus, the quaternion pseudo-derivative was used for calculating the gradient, which transforms the quaternion optimization problem into a lengthy and complicated real optimization problem; the solution is then found by using real-valued optimization algorithms [28, 29]. Flamant et al. [5, 22] demostrated that the GHR calculus is a powerful theory in quaternion signal processing and non-negative matrix factorization. Mengu¨c¸ et al. [12, 30] established that the GHR calculus paves the way for the theory and applications of quaternion-valued adaptive ﬁlters. Took and Xia [31] proposed a multichannel quaternion least-mean-square based on the GHR calculus for the adaptive ﬁltering. Parcollet et al. [32] further emphasized the signiﬁcance of the GHR calculus as a recent breakthrough in the ﬁeld.

The theory of convex optimization in the quaternion ﬁeld

has gained attention due to its promising applications in signal

processing and optimization. The aim of this work is to

develop the convexity theory of quaternion function using the

GHR calculus [24]. To this end, we make use of the duality of

the augmented quaternion vector qH qT, qiT, qjT, qkT T

and the augmented real vector qR

qaT, qbT, qcT, qdT T

[33]. Next, we employ the relationships between augmented

quaternion gradient and augmented real gradient, as well

as between the augmented quaternion Hessian matrix and

augmented real Hessian matrix, as shown in [33]. Based on

these results, we extend the discriminant criteria for convexity

from the real ﬁeld to the augmented quaternion space, H, and

2

then to the quaternion ﬁeld Hn, as illustrated in Figure 1. Moreover, we deﬁne and present four discriminant theorems for strong convexity, by employing the discriminant criteria of convex quaternion functions. Finally, we present a fundamental theorem for the optimality of convex quaternion problems and provide three illustrative applications in the ﬁeld of signal processing, including quaternion linear mean-square error ﬁlter, quaternion projection on afﬁne equality constraint, and quaternion minimum variance beamforming.

(20)(26)(27)

R

H

(23)(25) Hn

Fig. 1. The derivation process of quaternion optimization theory, with the sets R and H deﬁned by (18), (19).
This work makes three signiﬁcant contributions to the theory of convex optimization in the quaternion ﬁeld:
• By using the GHR calculus, we establish ﬁve discriminant theorems for convex functions in the quaternion ﬁeld. These theorems include gradient monotonicity and second-order characterization.
• We provide a clear deﬁnition and four discriminant criteria for strongly convex functions in the quaternion ﬁeld; these are consistent with their counterpart real and complex convexity theorems.
• A fundamental theorem is proposed for the optimality of convex quaternion problems, together with some practical applications of convex quaternion optimization in communications and signal processing.
This paper is organized as follows. In Section II, we give an overview of quaternion algebra, the GHR calculus, and some equivalence relationships. Section III presents ﬁve discriminant theorems for convex quaternion functions, covering ﬁrst-order characterization, second-order characterization and some examples of convex quaternion functions. Section IV introduces the deﬁnition and discriminant theorems for strongly convex quaternion functions. In Section V, we propose a fundamental theorem for convex quaternion optimization problems and provide three practical applications in signal processing. Finally, this paper concludes with Section VI.

II. PRELIMINARIES A. Quaternion Algebra
A quaternion, q, can be expressed as

q = qa + qbi + qcj + qdk,

(1)

where qa, qb, qc, qd ∈ R, and the imaginary units i, j and k satisfy i2 = j2 = k2 = ijk = −1, ij = −ji = k, jk = −kj = i, ki = −ik = j. The set of quaternions is deﬁned as H {q = qa + qbi + qcj + qdk | qa, qb, qc, qd ∈ R}. Owing
to the properties of the imaginary units, the multiplication of
two quaternions in H is noncommutative. The real part of q is denoted by Re {q} = qa, whereas the imaginary part (pure quaternion) is Im {q} = qbi + qcj + qdk. The conjugate of q is q∗ = Re {q} − Im {q} = qa − qbi − qcj − qdk. The modulus

of a quaternion is deﬁned as | q |= √qq∗. Deﬁne also qµ, as it is used in Deﬁnition 2.1.
Deﬁnition 2.1 (Quaternion rotation [34]): For any quaternion, q, and a nonzero quaternion µ, the transformation

qµ µqµ−1

(2)

describes a rotation of q. In particular, if µ in (2) is a pure unit quaternion, then the
quaternion rotation in (2) becomes quaternion involution [35], such as

qi = −iqi = qa + iqb − jqc − kqd,

(3)

qj = −jqj = qa − iqb + jqc − kqd,

(4)

qk = −kqk = qa − iqb − jqc + kqd.

(5)

Property 2.1 (Properties of quaternion rotation [36]): For any p, q ∈ H, and ∀ν, µ ∈ H, the following holds

(pq)µ = pµqµ, qµν = (qν )µ , qµ∗ (q∗)µ = (qµ)∗ q∗µ.

(6)

B. The GHR Calculus

Deﬁnition 2.2 (Real-differentiability [37]): A quaternion function f : H → H, given by f (q) = fa (qa, qb, qc, qd) + ifb (qa, qb, qc, qd) + jfc (qa, qb, qc, qd) + kfd (qa, qb, qc, qd) is called real differentiable, if fa, fb, fc, fd are differentiable as functions of the real variables qa, qb, qc, qd.
Deﬁnition 2.3 (GHR derivatives [24]): If f : H → H is real-
differentiable, then the left GHR derivatives of the function f with respect to qµ and qµ∗ (µ = 0, µ ∈ H) are deﬁned as

∂f 1 ∂qµ = 4

∂f − ∂f iµ − ∂f jµ − ∂f kµ

∂qa ∂qb

∂qc

∂qd

∈ H,

(7)

∂f 1 ∂qµ∗ = 4

∂f ∂qa

+

∂f iµ ∂qb

+

∂f jµ ∂qc

+

∂f kµ ∂qd

∈ H,

(8)

where q = qa + qbi + qcj + qdk, qa, qb, qc, qd ∈ R, and

∂f ∂qa

,

∂f ∂qb

,

∂f ∂qc

,

∂f ∂qd

∈ R are the partial derivatives of f

with

respect to qa, qb, qc, qd.

Property 2.2 (Properties of the GHR derivatives [24]): If

f : H → H, g : H → H, then

Product rule:

∂(f g) ∂qµ

=

f

∂g ∂qµ

+

∂f ∂qgµ g,

∂(f g) ∂ q µ∗

∂g = f ∂qµ∗

∂f + ∂qgµ∗ g

(9)

Chain rule:

∂f (g(q)) ∂qµ =

∂f ∂gν ∂gν ∂qµ ,

(10)

ν∈{1,i,j,k}

∂f (g(q))

∂f ∂gν∗

∂qµ∗ =

∂gν∗ ∂qµ∗

(11)

ν∈{1,i,j,k}

Rotation rule:

∂f ν ∂fν

∂f ν ∂fν

∂qµ = ∂qνµ ,

∂qµ∗ = ∂qνµ∗

(12)

Conjugate rule: If f : H → R,

∂f ∗ ∂f

∂f ∗ ∂f

∂qµ = ∂qµ∗ ,

∂qµ∗ = ∂qµ .

(13)

3

Deﬁnition 2.4 (Quaternion gradient [33]): The quaternion gradient and its conjugate gradient of a function f : Hn → R
are deﬁned as

∇q f

∂f T =

∂f , . . ., ∂f

T
∈ Hn,

∂q

∂q1

∂qn

(14)

∇q∗ f

∂f T ∂q∗ =

∂f

∂f

∂q1∗ , . . . , ∂qn∗

T
∈ Hn,

(15)

where

∂f ∂q

T

is

the

transpose

of

∂f ∂q

.

Deﬁnition 2.5 (Quaternion Hessian [33]): Let f : Hn → R,

then the two quaternion Hessian matrices are deﬁned as

Hqq

∂ ∂f T ∂q ∂q

 ∂2f · · · ∂2f 

 ∂q1∂q1

∂qn∂q1 

 =


...

...

...

  ∈ Hn×n, (16) 

 

∂2f

···

∂2f

 

∂q1∂qn

∂qn∂qn

H qq∗

∂ ∂f T ∂q ∂q∗

 ∂2f  ∂q1∂q1∗

···

∂2f  ∂qn∂q1∗ 



=

 

...

...

...

  ∈ Hn×n. (17) 

 

∂2f

∂q1∂qn∗

···

∂2f

 

∂qn∂qn∗

C. The Relationship of Augmented Quaternion and the Aug-

mented Real Vector, Gradient, and Hessian Matrix

Consider a quaternion vector q = qa +qbi+qcj +qdk ∈ Hn

where qa, qb, qc, qd ∈ Rn. Deﬁne its augmented real vector

as qR qaT, qbT, qcT, qdT T ∈ R [4, 38] and the augmented

quaternion vector as qH

qT, qiT, qjT, qkT T ∈ H [33],

where the set of augmented real vectors and the set of

augmented quaternion vectors are deﬁned as

R

qR = qaT, qbT, qcT, qdT T | q ∈ Hn = R4n,

(18)

H

qH = qT, qiT, qjT, qkT T | q ∈ Hn ⊂ H4n. (19)

By deﬁnition, there exists a one-to-one mapping between Hn, R and H [22].
Proposition 2.1 ([33]): The relationship between the augmented quaternion vector, qH, and the augmented real vector, qR, is given by

qH = JnqR

⇔

qR

=

1 4

JnH qH ,

(20)

where

 In iIn jIn kIn 

Jn

=

 



In In

iIn −iIn

−jIn jIn

−kIn −kIn

 

∈

H4n×4n,



(21)

In −iIn −jIn kIn

and JnHJn = 4I4n, while In is the n × n identity matrix, with JnH as the conjugate transpose of Jn.
From (20), the quaternion function f (q) : Hn → R can be viewed in three equivalent forms [33], as follows

f (q) ⇔ f (qR) f (qa, qb, qc, qd) ⇔ f (qH) f q, qi, qj, qk .

(22)

Note that these three functions are equivalent but have different

forms, denoted as f for simplicity. Here, the variables of the

functions f (q), f (qR), and f (qH) are quaternion vectors, augmented real vectors, and augmented quaternion vectors,

respectively. They are referred to as quaternion function,

augmented real function, and augmented quaternion function,

respectively. For f (qR) : R → R, its augmented real gradient

is deﬁned as ∇Rf

∂f ∂qR

T
and the augmented real Hessian

matrix as HRR

∂ ∂qR

∂f ∂qR

T
. For f (qH) : H → R, the

augmented quaternion gradient and its conjugate gradient are

deﬁned as [39]

∇Hf

∂f ∂qH

T

=

 ∇qf ∇qi f ∇qj f


  

,

(23)

∇qk f

∇H∗ f

∂f ∂ qH∗

T

=

 ∇q∗ f 

 ∇q i∗ ∇qj∗

f f

  

,

(24)

∇qk∗ f

and the augmented quaternion Hessian matrix is deﬁned as

H HH∗

∂

∂f T

∂qH ∂qH∗

 Hqq∗ Hqiq∗

=

 



H qqi∗ H qqj∗

H qiqi∗ H qiqj∗

H H qqk∗

qiqk∗

H qj q∗ H qj qi∗ H qjqj∗ H qjqk∗

(25)

Hqkq∗ 

H qkqi∗ H qkqj∗

 

.



H qkqk∗

Proposition 2.2 ([39]): The relationship between the aug-
mented quaternion gradient, ∇H∗ f , and the augmented real gradient, ∇Rf , is given by

∇H∗ f

=

1 4

Jn

∇R

f

⇔

∇Rf = JnH∇H∗ f.

(26)

Proposition 2.3 ([33]): The relationship between the augmented quaternion Hessian matrix, HHH∗, and the augmented real Hessian matrix, HRR, is given by

H HH∗

=

1 16

Jn

H

RR

JnH

⇔

HRR = JnHHHH∗ Jn

(27)

where HHH∗

∂ ∂qH

∂f ∂ qH ∗

T
, HRR

∂ ∂qR

∂f ∂qR

T
.

Corollary 2.1: The augmented quaternion Hessian matrix,

HHH∗ , is a Hermite matrix, that is

H

H HH∗

=

HHH∗ ,

(28)

where

H

H HH∗

is

the

conjugate

transpose

of

HHH∗ .

Proof: This is straightforward to demonstrate by using

(27) and the fact that HRR is a Hermitian matrix.

4

Proposition 2.4: For any p, q ∈ Hn, their augmented real vectors are pR, qR ∈ R, and their augmented quaternion vectors are pH, qH ∈ H. Then

(a) pTHqH = 4Re pTq ;

(29)

(b) 4pRT qR = pHH qH = 4Re pHq ;

(30)

(c) 2 pR 2 = pH 2 = 2 p 2;

(31)

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

q 22.

(32)

Proof: By the relationship of q, qR, and qH, we have

(a) pHT qH =

pµTqµ (=6)

pTq µ

µ∈{1,i,j,k}

µ∈{1,i,j,k}

(=20) 4Re pTq ;

(33)

(b)

4pRT qR

=

4pHRqR

(=20)

pHH Jn

1 4

JnH qH

=

pHHqH

(34)

(=29) 4Re pHq ;

(c) 4

pR

2 2

=

4pTRpR

(=30)

pHH pH

=

pH

2 2

(35)

(=30) 4Re pHp = 4pHp = 4 p 22;

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

=pHp + pHq + qHp + qHq

(36)

=

p

2 2

+

2Re

pHq

+

q 22.

This completes the proof.
Proposition 2.5: If the quaternion function f (q) : Hn → R is real-differentiable, then ∀p, q ∈ Hn we have

(b) ∇Rf (pR)T∇Rf (qR) = ∇Rf (pR)H ∇Rf (qR)

(=26) ∇H∗ f (pH)H JnJnH∇H∗ f (qH) = 4∇H∗ f (pH)H ∇H∗ f (qH)

=4

∇p∗ f (p)µH ∇q∗ f (q)µ (41)

µ∈{1,i,j,k}

(=6) 4

∇p∗ f (p)H ∇q∗ f (q) µ

µ∈{1,i,j,k}

(=20) 16Re ∇p∗ f (p)H ∇q∗ f (q) ;

(c) Let q = p in (38).

This completes the proof.

III. DISCRIMINANT THEOREMS FOR CONVEX QUATERNION FUNCTIONS
The objective of this section is to introduce ﬁve discriminant criteria for convex quaternion functions, including the ﬁrstorder characterization and the second-order characterization. An example is presented to illustrate how these criteria can be applied in practice.

A. Convex Set and Convex Quaternion Function
We begin by introducing the fundamental concepts, such as convex set and convex function [40, 41].
Deﬁnition 3.1 (Convex set): The set C is called convex, if ∀x, y ∈ C, ∀0 θ 1, θx + (1 − θ) y ∈ C. The set C can be a subset of Hn, R or H.
Deﬁnition 3.2 (Convex function): A function f is said to be convex, if domf is convex, and ∀x, y ∈ domf , 0 θ 1,
f θx + (1 − θ) y θf (x) + (1 − θ) f (y) . (42)

(a) ∇Rf (pR)T qR =∇H∗ f (pH)H qH

=4Re ∇p∗ f (p)H q ;

(37)

(b) ∇Rf (pR)T ∇Rf (qR) = 4∇H∗ f (pH)H ∇H∗ f (qH)

=16Re ∇p∗ f (p)H ∇q∗ f (q) ;

(38)

(c) ∇Rf (pR) 2 = 2 ∇Hf (pH) 2 = 4 ∇pf (p) 2. (39)

Proof: By the relationship of q, qR, and qH, and the relationship of ∇q∗ f , ∇Rf , and ∇H∗ f , we have

(a) ∇Rf (pR)T qR = ∇Rf (pR)H qR

(20=)(26)

∇H∗ f

(pH)H

Jn

1 4

JnHqH

= ∇H∗ f (pH)H qH

=

∇p∗ f (p)µH qµ

µ∈{1,i,j,k}

(=6)

∇p∗ f (p)H q µ

µ∈{1,i,j,k}

(=20) 4Re ∇p∗ f (p)H q ;

(40)

The range of the function f is R, and the deﬁnition ﬁeld domf can be a subset of Hn, R or H.
Example 3.1: Consider a quaternion matrix, A ∈ Hm×n, and a quaternion vector, b ∈ Hm, then the set D {q ∈ Hn | Aq = b} is convex.
Proof: ∀p, q ∈ D, Ap = b, Aq = b, ∀0 θ 1,
A (θp + (1 − θ)q) = θAp + (1 − θ)Aq = θb + (1 − θ)b = b. (43)
Therefore, θp + (1 − θ)q ∈ D, that is the set D is convex. Example 3.2: If the quaternion function f (q) is convex, then
the set E {q ∈ Hn | f (q) 0} is also convex. Proof: ∀p, q ∈ E, f (p) 0, f (q) 0. Since f (q) is
convex, ∀0 θ 1,
f θp + (1 − θ)q θf (p) + (1 − θ)f (q) 0. (44)
Therefore, θp + (1 − θ)q ∈ E, that is the set E is convex.

B. First-order Characterization of Discriminant Theorems for Convex Quaternion Functions

We shall now introduce four discriminant theorems for

convex quaternion functions, including the ﬁrst-order charac-

terization and gradient monotonicity.

Theorem 3.1: Consider the three sets C ⊂ Hn,

CR

qR = qaT, qbT, qcT, qdT T | q ∈ C ⊂ R = R4n,

5

CH

qH = qT, qiT, qjT, qkT T | q ∈ C ⊂ H ⊂ H4n.

Then, C is convex ⇔ CR is convex ⇔ CH is convex. Proof: Using the deﬁnition of C, CR, CH, and that of
convex set, the proof following.

A straightforward method to discriminate the convexity of

a quaternion function is to conﬁne it to a line segment and

determine whether the resulting one-dimensional function is

convex, as in the following theorem. Theorem 3.2: The quaternion function f (q) : C ⊂ Hn → R
is convex if and only if (shortened to iff) ∀q ∈ C, v ∈ Hn,

g : S → R,

g(t) = f (q + tv)

(45)

is convex, where S {t ∈ R | q + tv ∈ C} ⊂ R. Proof: The proof follows the same steps as its counterpart
in the real ﬁeld [40, 41]. For real-differentiable quaternion functions, we can also use
their gradient information to discriminate their convexity, as stated in the following theorem.
Theorem 3.3 (First-order characterization [22]): Consider a convex set C ⊂ Hn and a real-differentiable quaternion function f (q) : C → R. Then f (q) is convex iff ∀p, q ∈ C,

f (q) f (p) + 4Re ∇p∗ f (p)H (q − p) , (46)

where ∇p∗ f (p) is deﬁned in (15). Another commonly used ﬁrst-order characterization is gra-
dient monotonicity, as shown below.
Theorem 3.4 (Gradient monotonicity): Consider a convex set C ⊂ Hn and a real-differentiable quaternion function f (q) : C → R. Then, f (q) is convex iff ∀p, q ∈ C,

Re ∇p∗ f (p) − ∇q∗ f (q) H (p − q) 0,

(47)

where ∇p∗ f (p) is deﬁned in (15). Proof: From Theorem 3.1, C is convex iff CR is con-
vex. We already know [40, 41] that for a differentiable real function, f (qR) is convex iff ∀pR, qR ∈ CR,

∇Rf (pR) − ∇Rf (qR) T (pR − qR) 0,

(48)

where the set CR ⊂ R is convex. Hence from (37), we have

∇Rf (pR) − ∇Rf (qR) T (pR − qR) =4Re ∇p∗ f (p) − ∇q∗f (q) H (p − q) . (49)

Upon substituting (49) into (48), the proof follows. In addition, we can also use the epigraph to discriminate
the convexity of f (q), as shown below. Deﬁnition 3.3 (Epigraph): For the quaternion generalized
real-valued function f (q) : Hn → R ∪ {±∞}, the set

epif = (q, t) ∈ Hn+1 | f (q) t, t ∈ R

(50)

is called the epigraph of f (q). Theorem 3.5: The quaternion generalized real-valued func-
tion f (q) : C ⊂ Hn → R ∪ {±∞} is convex, iff epif is a convex set.
Proof: The proof follows the same steps as its counterpart in the real ﬁeld [40, 41].

C. Second-order Characterization of Discriminant Theorems for Convex Quaternion Functions

Before introducing the second-order characterization of
convex quaternion functions, we ﬁrst need to deﬁne positive
deﬁnite quaternion matrices. Deﬁnition 3.4 (Positive deﬁnite matrix): The matrix A ∈
Hn×n is called positive deﬁnite, if

Re xHAx > 0, ∀x ∈ Hn, x = 0,

(51)

and is denoted by A ≻ O, where O is the n × n zero matrix. Similarly, the matrix A ∈ Hn×n is called positive
semi-deﬁnite, if

Re xHAx 0, ∀x ∈ Hn, x = 0,

(52)

and is denoted by A O. Theorem 3.6: If the matrix A ∈ Hn×n satisﬁes AH = A,
then A is positive deﬁnite iff

xHAx > 0, ∀x ∈ Hn, x = 0.

(53)

Similarly, the matrix A is positive semi-deﬁnite iff

xHAx 0, ∀x ∈ Hn, x = 0.

(54)

Proof: This is straightforward to prove, by applying

Deﬁnition 3.4.

If the quaternion function f (q) is second-order continuous

real-differentiable, we can use the Hessian matrix to discrim-

inate its convexity, as shown below.

Theorem 3.7 (Second-order characterization): Consider a convex set C ⊂ Hn and a second-order continuous real-

differentiable quaternion function f (q) : C → R. Then f (q)

is convex iff

H HH∗ O.

(55)

where HHH∗ is deﬁned in (25). Proof: Applying Theorem 3.1, the set C is convex iff the
set CR is convex. We already know [40, 41] that for a secondorder continous differentiable function, f (qR) is convex iff

H RR O, ∀qR ∈ CR,

(56)

where the set CR ⊂ R is convex. By Corollary 2.1, HHH∗ is a Hermite matrix. Then ∀xH ∈ H, xH = 0, we have

xHHH HH∗ xH

(=27)

1 16

xHH

JnH

RRJnH

xH

1 = 16

JnHxH H HRR

JnH xH

(=20)xRH HRRxR.

(57)

Therefore,

H HH∗ O ⇔ H RR O,

(58)

which concludes the proof. Corollary 3.1: Consider a convex set C ⊂ Hn and a second-
order continuous real-differentiable quaternion function f (q) : C → R. Then, the following three propositions are equivalent:
(a) f (q) is convex; (b) HHH∗ O;

6

(c)

Re xHHqν q∗ xν

ν∈{1,i,j,k}

0, ∀x ∈ Hn, x = 0.

Proof: From Theorem 3.7, (a) is equivalent to (b), so we

only need to prove that (b) is equivalent to (c). From Corollary

2.1, we know that HHH∗ is a Hermite matrix. Then ∀xH ∈ H,

xH = 0, we have

TABLE I
SEVERAL DERIVATIVES PERFORMED BY THE GHR CALCULUS FROM TABLE IV OF [36], ∀A ∈ Hn×n , ∀a ∈ Hn, ∀b ∈ Hn, α ∈ H, β ∈ H.

f (q) or f (q)

∂f ∂q

or

∂f ∂q

∂f ∂q∗

or

∂f ∂q∗

xHH H HH∗ xH

 x H  H qq∗

=

 xi xj

  

 H qqi∗

 

H qqj∗

xk

H qqk∗

H qiq∗ H qiqi∗ H qiqj∗ H qiqk∗

=

xµHH qν qµ∗ xν

µ,ν∈{1,i,j,k}

H qj q∗ H qj qi∗ H qjqj∗ H qjqk∗

Hqkq∗   x 

Hqkqi∗  xi 

H qk qj∗

 

xj

 

H qkqk∗

xk

aTqβ αq H b Aqβ q H Aq

aTRe{β}

−

1 2

αbH

ARe {β}

qHA

−

1 2

(Aq)H

−

1 2

aT

β∗

αRe bT

−

1 2

Aβ∗

−

1 2

qH

A

+

Re

(Aq)T

(=20)4

Re xHH qνq∗ xν .

ν∈{1,i,j,k}

(59) Upon using the ﬁrst, the second and the fourth rows of TABLE I, we take the gradient of f (q) with respect to q∗ to gield

Therefore,

Re
ν∈{1,i,j,k}

xHH qνq∗ xν ⇔ HHH∗

0, ∀x ∈ Hn, x = 0 (60)
O.

This completes the proof. Lemma 3.1: The matrix A ∈ Hn×n is positive deﬁnite
(positive semi-deﬁnite), iff all principal submatrices of A are positive deﬁnite (positive semi-deﬁnite).
Proof: The follows the same steps as its counterpart in the real ﬁeld [42].
Applying Lemma 3.1, we can obtain a necessary condition for convex quaternion functions.
Theorem 3.8: Consider a convex set C ⊂ Hn and a secondorder continuous real-differentiable quaternion function f (q) : C → R. If f (q) is convex, then

Hqq∗ O,

(61)

where Hqq∗ is the quaternion Hessian matrix, deﬁned in (17). Proof: Upon applying Theorem 3.7, together with the
convexity of f (q), we have HHH∗ O. By (25) and Lemma 3.1, we ﬁnally obtain Hqq∗ O.

D. Examples of Convex Quaternion Function

We next provide a basic example to determine the convexity of quaternion functions. In this example, we make use of certain GHR derivatives presented in TABLE IV of [36], which are included in TABLE I here.
Example 3.3: If the quaternion function f (q) = Aq − b 22, ∀q ∈ Hn, A ∈ Hm×n, b ∈ Hm, then f (q) is convex.
Proof: (First-order characterization criterion) By the deﬁnition of the 2-norm, we have

f (q) =

Aq − b

2 2

= (Aq − b)H (Aq − b)

(62)

=qHAHAq − qHAHb − bHAq + bHb.

∇q∗ f (q)

∂f ∂q∗

T
(=13)

∂f H ∂q

= 1 AHAq + 1 AHb − AHb

(63)

2

2

= 1 AH (Aq − b) . 2

Then ∀p, q ∈ Hn, we obtain

f (q) − f (p) − 4Re ∇p∗ f (p)H (q − p)

= (Aq − b)H (Aq − b) − (Ap − b)H (Ap − b)

−2Re AH (Ap − b) H (q − p)

=qHAHAq + pHAHAp − pHAHAq − qHAHAp (64)

= (q − p)H AHA (q − p)

=

A (q − p)

2 2

0.

Therefore, from Theorem 3.3 we know that f (q) is convex. (Gradient monotonicity criterion) ∀p, q ∈ Hn, we have

Re (∇p∗ f (p) − ∇q∗ f (q))H (p − q)

= 1 Re AH (Ap − b) − AH (Aq − b) H (p − q) 2

= 1 Re (p − q)H AHA (p − q)

2

(65)

= 1 (p − q)H AHA (p − q)

2

=1 2

A (q − p)

2 2

0.

Therefore, from Theorem 3.4 we know that f (q) is convex.

7

(Second-order characterization criterion) Using the third row of TABLE I, we get

Hqq∗

∂ ∂q

∂f ∂q∗

T = ∂∇q∗ f (q) ∂q

∂ 1 AH (Aq − b)

(66)

(=63)

2

= 1 AHA,

∂q

2

and for any ν ∈ {i, j, k},

H qν q∗

∂ ∂qν

∂f ∂q∗

T

=

∂∇q∗f (q) ∂qν

∂ (=63)

1 AH (Aq − b) 2
∂qν

(=9)

1 2

AH

A

∂q ∂qν

= O.

(67)

Then ∀x ∈ Hn, x = 0, it follows that

Re xHHqνq∗ xν

ν∈{1,i,j,k}

1 = Re
2

xHAHAx

= 1 xHAHAx = 1

2

2

Ax

2 2

(68) 0.

Therefore, by Corollary 3.1, we know that f (q) is convex.

IV. STRONGLY CONVEX QUATERNION FUNCTION: DEFINITION AND DISCRIMINANT THEOREMS

We shall now discuss the discriminant criteria for strongly

convex quaternion functions, building upon the theorems for

convexity. These criteria will be useful in designing optimiza-

tion algorithms.

Deﬁnition 4.1 (Strongly convex function): The quaternion function f (q) : C ⊂ Hn → R is called strongly convex, if
∃σ > 0, ∀p, q ∈ C, ∀θ ∈ (0, 1),

f θp+(1−θ)q

θf (p)+(1−θ)f (q)− σ θ(1−θ) 2

p−q

22,

(69)

where σ is the strongly convex parameter. For convenience,

f (q) is also called σ-strongly convex.

Based on the deﬁnition of strongly convex functions, we

obtain the following equivalence theorem. Theorem 4.1: The quaternion function f (q) : C ⊂ Hn → R
is σ-strongly convex, iff ∃σ > 0, s.t. the function

g (q)

f

(q)

−

σ 2

q

2 2

(70)

is convex. Proof: This is straightforward to prove, by applying
Deﬁnition 3.2 and Deﬁnition 4.1. Similar to convex quaternion functions, strongly convex
quaternion functions also have ﬁrst-order characterization, gradient monotonicity, and second-order characterization.
Theorem 4.2 (First-order characterization): Consider a convex set C ⊂ Hn and a real-differentiable quaternion function f (q) : C → R. Then, f (q) is σ-strongly convex iff ∀p, q ∈ C,

f (q) f (p) + 4Re ∇p∗ f (p)H (q − p) where ∇p∗ f (p) is deﬁned in (15).

σ +2

q−p

22,

(71)

Proof: From Theorem 4.1, f (p) is strongly convex iff

g (p)

=

f (p) −

1 2

σ

p

2 2

is

convex.

Then,

upon

applying

Theorem 3.3, ∀p, q ∈ C,

g (q) g (p) + 4Re ∇p∗ g (p)H (q − p) . (72)

Using the fourth row of TABLE I, ∇p∗ g (p) = ∇p∗ f (p) −

1 4

σp.

Then,

∀p,

q

∈

C,

f

(q)

−

σ 2

q

2 2

f (p) − σ 2

p

2 2

+

4Re

(73)

∇p∗ f

(p) −

σ p
4

H (q − p)

.

Since

σ 2

q

2 2

−

σ 2

p

2 2

+

4Re

=4Re ∇p∗ f (p)H (q − p)

σ +
2

q

2 2

−

σ 2

p

2 2

(=32)4Re ∇p∗ f (p)H (q − p)

∇p∗ f

(p) −

σ p
4

H (q

− p)

− σRe

pHq

+σ

p

2 2

σ +
2

q−p

22.

(74)

Upon substituting (74) into (73), the proof follows.
Theorem 4.3 (Gradient monotonicity): Consider a convex set C ⊂ Hn and a real-differentiable quaternion function f (q) : C → R. Then, f (q) is σ-strongly convex iff ∀p, q ∈ C,

Re ∇p∗ f (p) − ∇q∗ f (q) H (p − q)

σ 4

p−q

22,

(75)

where ∇p∗ f (p) is deﬁned in (15).

Proof: From the Theorem 4.1, f (q) is strongly convex

iff

g (q)

=

f (q) −

1 2

σ

q

2 2

is

convex.

Then,

after

applying

Theorem 3.4, we have

Re (∇p∗ g (p) − ∇q∗g (q))H (p − q) 0, ∀p, q ∈ C.

(76)

Using the fourth row of TABLE I, we have ∇q∗ g (q) =

∇q∗ f

(q)

−

1 4

σq,

then

∀p,

q

∈

C,

Re

∇p∗ f (p) −

σ 4

p

−

∇q∗

f

(q)

+

σq 4

H (p − q)

0.

(77)

Upon rearranging the terms in (77), we obtain (75).

Theorem 4.4 (Second-order characterization): Consider a convex set C ⊂ Hn and a second-order continuous realdifferentiable quaternion function f (q) : C → R. Then, f (q) is σ-strongly convex, iff

σ

HHH∗ 4 I4n,

(78)

where HHH∗ is deﬁned in (25).

Proof: Deﬁne g (q)

f

(q)

−

1 2

σ

q

22, h(q)

2

q

2 2

=

2qHq = 2 qHq µ (=6) 2qµHqµ, µ ∈ {1, i, j, k}. Upon applying

the fourth row of TABLE I, we have

∂h ∂ q µ∗

T
= qµ,

µ ∈ {1, i, j, k} .

(79)

Then, ∀µ ∈ {1, i, j, k},

∂ ∂qµ

∂h ∂ q µ∗

T

(=79)

∂qµ ∂qµ

= In,

(80)

8

and ∀µ, ν ∈ {1, i, j, k}, µ = ν,

∂ ∂qν

∂h ∂ q µ∗

T

(=79)

∂qµ ∂qν

= O.

(81)

By (25), the augmented quaternion Hessian matrix of h is

I4n. Therefore, the augmented quaternion Hessian matrix of

g

is

H HH∗

−

1 4

σI4n.

From

Theorem

4.1,

f (q)

is

strongly

convex iff g (q) is convex. Then upon applying Theorem 3.7,

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

is convex iff HHH∗ −

1 4

σI4n

O.

Corollary 4.1: Consider a convex set C ⊂ Hn and a secondorder continuous real-differentiable quaternion function f (q) : C → R. Then, the following three propositions are equivalent:

(a) f (q) is σ-strongly convex;

(b) H HH∗ (c)

1 4

σI4n

;

Re xHH qνq∗ xν

ν∈{1,i,j,k}
Hn, x = 0.

−

1 4

σ

x

2 2

0, ∀x ∈

Proof: According to Theorem 4.4, (a) is equivalent to

(b), so we only need to prove that (b) is equivalent to (c). By

Corollary

2.1,

H HH∗

is

a

Hermite

matrix,

so

H HH∗ −

1 4

σI4n

is also Hermite matrix. Then, ∀xH ∈ H, xH = 0, we have

xHH

σ H HH∗ − 4 I4n

xH

=

xHHH HH∗ xH

−

σ 4

xHH xH

(=31)

xµHH qνqµ∗ xν − σxHx

(82)

µ,ν∈{1,i,j,k}

(=20) 4

Re xHHqνq∗ xν − σ x 22.

ν∈{1,i,j,k}

Therefore, ∀x ∈ Hn, x = 0,

Re

xHH qνq∗ xν

−σ 4

x

2 2

0,

ν∈{1,i,j,k}

⇔

H HH∗

−

σ 4 I4n

O.

(83)

This completes the proof.
Upon applying Lemma 3.1, we can obtain a necessary condition for σ-strongly convex quaternion functions.
Theorem 4.5: Consider a convex set C ⊂ Hn and a secondorder continuous real-differentiable quaternion function f (q) : C → R. If f (q) is σ-strongly convex, then

σ

Hqq∗ 4 In,

(84)

where Hqq∗ is the quaternion Hessian matrix, deﬁned in (17).

Proof: Note that f (q) is σ-strongly convex, and upon

applying Theorem 4.4, we have HHH∗

1 4

σI4n

.

By

(25)

and Lemma 3.1, we ﬁnally obtain Hqq∗

1 4

σIn

.

V. CONVEX QUATERNION OPTIMIZATION PROBLEMS AND THEIR APPLICATIONS IN SIGNAL PROCESSING
We now proceed to introduce the convex quaternion problem and its fundamental theorem. This is followed by several applications of convex quaternion optimization in communications, highlighting its practical signiﬁcance.

A. Convex Quaternion Optimization Problems
Similar to convex real and complex optimization problems, convex quaternion optimization problems generally have a structure which consist of the minimization of a convex quaternion function subject to (shortened to s.t.) quaternion afﬁne equality constraints and inequality constraints deﬁned by convex quaternion functions, as follows

min f0(q)
q∈Hn

s.t. Aq = b,

(85)

fi(q) 0, i = 1, . . . , P

where fi : Hn → R, i = 0, 1, . . . , P is convex, A ∈ Hm×n,

b ∈ Hm. The problem ﬁeld is F

P i=0

domfi,

and

feasi-

ble set is C {q ∈ F | fi(q) 0, i = 1, . . . , P, Aq = b}.

From Deﬁnition 3.2, Example 3.1 and Example 3.2, the

sets D {q ∈ Hn | Aq = b}, Ei {q ∈ Hn | fi(q) 0},

i = 1, . . . , P and domfi, i = 0, 1, . . . , P are convex.

Therefore, the set C = D

P i=1

Ei

F is also convex.

When studying the convexity of quaternion functions, we

utilized the augmented quaternion vectors and augmented real

vectors. Similarly, when studying the properties of quaternion

convex optimization problems, we also need to utilize the

augmented quaternion and the augmented real convex opti-

mization settings.

The convex augmented quaternion optimization problem of

(85) is given by [22]

min f0(qH)
qH∈H

s.t. AHqH = bH,

(86)

fi(qH) 0, i = 1, . . . , P

where fi : H → R, i = 0, 1, . . . , P is convex, AH diag A, Ai, Aj , Ak ∈ H4m×4n, A ∈ Hm×n, and bH bT, biT, bjT, bkT T ∈ H4m.
The convex augmented real convex optimization problem of
(85) is given by [22]

min f0(qR)
qR∈R

s.t. ARqR = bR,

(87)

fi(qR) 0, i = 1, . . . , P

where fi : R → R, i = 0, 1, . . . , P is convex, together

with AR

1 4

JmH

AH

Jn

∈

R4m×4n,

AH

∈

H4m×4n,

and

bR

1 4

JmH bH

∈

R4m.

Lemma 5.1 ([22]): The convex quaternion optimization

problem in (85), the convex augmented quaternion opti-

mization problem in (86), and the convex augmented real

optimization problem in (87) are equivalent.

Theorem 5.1: For the convex quaternion optimization prob-

lem in (85), any local optimal solution is also the global

optimal solution.

Proof: We already know [43] that for the real con-

vex optimization problem in (87), any local optimal solu-

tion, for example q¯R, is also the global optimal solution. Then, from Lemma 5.1, the local optimal solution q¯H q¯T, q¯iT, q¯jT, q¯kT T = Jnq¯R is also global, in the augmented

9

convex quaternion optimization problem in (86). Therefore, where λ ∈ Hp denotes the set of Lagrange multipliers. Finding

the local optimal solution, q¯, is also global, in the convex the gradient of L (x, λ) with respect to x∗ in the same way

quaternion optimization problem in (85).

as in (63) and setting the result to 0, we have

B. Applications of Convex Quaternion Optimization in Signal Processing

Application 5.1 (Quaternion linear mean-square error ﬁlter): The quaternion minimum mean-square error (MSE) ﬁlter can be speciﬁed as

min J (w) E |e(n)|2 = E |d(n) − y(n)|2 , (88)
w∈Hn
where y(n) = wHx(n), x(n) ∈ Hn is the input vector, w ∈ Hn is the ﬁlter weight vector, and d(n) ∈ H is the desired sequence. By the deﬁnition of the modulus, we have

J (w) =E |d(n) − wHx(n)|2 =E d(n) − wHx(n) d(n) − wHx(n) ∗

=wHE{x(n)xH(n)}w − E{d(n)xH(n)}w (89) −wHE{x(n)d∗(n)} + E{d(n)d∗(n)} =wHRw − pHw − wHp + σd2,

where R = E{x(n)xH(n)} denotes the quaternion-valued input correlation matrix, p = E{x(n)d∗(n)} is the crosscorre-
lation vector between the desired response and the input signal, σd2 = E{d(n)d∗(n)} is the power of the desired response. By (62) in Example 3.3, we know that J (w) is convex. Similarly to (63), we take the gradient of J (w) with respect to w∗,
and set the result to 0 to obtain

∇w∗ J (w) =

∂J H = 1 Rw − 1 p = 0.

∂w

2

2

(90)

Using (90) and Theorem 5.1, we arrive at gives the closedform optimal solution

w¯ = R−1p.

(91)

Application 5.2 (Quaternion projection on afﬁne equality

constraint): The quaternion projection problem can be de-

scribed as

min
x∈Hn

x−y

2 2

(92)

s.t. Ax = b

where y ∈ Hn, b ∈ Hp, A ∈ Hp×n and rank(A) = p < n.

Applying Example 3.3, f (x) =

x−y

2 2

is

convex,

and

Ax

=

b is an afﬁne equality constraint. Therefore, the quaternion

optimization problem in (92) is convex.

Using the methed of Lagrange multipliers [22, 36], we have

L(x, λ)

=

x−y

2 2

+

Re

λH(Ax − b)

=(x − y)H(x − y) + 1 λH(Ax − b) + 2

1 (Ax − b)Hλ 2

(93)

=xHx + 1 λHA − yH x + xH 1 AHλ − y

2

2

+yHy − 1 λHb − 1 bHλ,

2

2

∇x∗ L(x, λ) =

∂L ∂x

H

= 1 x + 1 λHA − yH H − 1

2

2

2

= 1 x − 1 y + 1 AHλ 224

=0,

1 AHλ − y 2
(94)

which leads to

x = y − 1 AHλ.

(95)

2

A combinition of (95) with the constraint Ax = b yields

A y − 1 AHλ = b

2

(96)

⇒ λ = 2 AAH −1 (Ay − b).

Substituting (96) into (95) and applying Theorem 5.1, we obtain the following optimal solution

x¯ = y + AH AAH −1 (b − Ay).

(97)

Application 5.3 (Quaternion minimum variance beamforming): The problem of quaternion variance beamforming minimization can be described as

min f (w) wHRw

w∈Hn

(98)

s.t. wHa = 1,

where w ∈ Hn is the beamformer weight vector, a ∈ Hn is the steering vector, and RH = R ∈ Hn×n is positive deﬁnite.
We will next prove that the problem in (98) is a convex quaternion optimization problem. Using the fourth row of TABLE I, we have

∇w∗ f (w) =

∂f H =
∂w

wHR − 1 (Rw)H H = 1 Rw.

2

2

(99)

Then, ∀v, w ∈ Hn,

Re ∇v∗ f (v) − ∇w∗f (w) H (v − w)
= 1 Re (Rv − Rw)H (v − w) 2
= 1 (v − w)H R (v − w) 2 0.

(100)

From Theorem 3.4, it follows that f (w) is convex, and wHa = 1 is an afﬁne equality constraint. Therefore, the problem in (98) is a convex quaternion optimization problem.
The Lagrangian of problem in (98) is given by [22, 36]
L (w, λ) = wHRw + λ wHa − 1 , λ ∈ R, (101)

10

which is a real-valued function of w ∈ Hn. Using the second and the fourth rows of TABLE I, and setting ∇w∗L (w, λ) = 0, we have

∇w∗L (w, λ) =

∂L ∂w

H = 1 Rw − 1 λa = 0

2

2

⇒ w = λR−1a.

(102)

Upon substituting (102) into aHw = 1, we obtain

λaHR−1a = 1

⇒

λ

=

1 aHR−1

a

.

(103)

Therefore, upon applying Theorem 5.1, the closed-form optimal solution is obtained as

R−1a w¯ = aHR−1a .

(104)

VI. CONCLUSIONS
We have established the theory of convex quaternion optimization based on the GHR calculus, which is an enabling methodology in the ﬁeld of quaternion optimization and its applications in quaternion signal processing and machine learning. Our study has resulted in the development of ﬁve discriminant theorems for convex functions in the quaternion ﬁeld, utilizing (20), (23), (25), (26), and (27). Furthermore, we have provided the deﬁnition and four discriminant criteria for strongly convex functions by employing the results for convex quaternion functions. In addition, we have presented a fundamental theorem for the optimality of convex quaternion optimization problems and three applications in signal processing, which have both enriched the theory of convex quaternion optimization and provided a theoretical foundation for quaternion signal processing. However, the convexity of non-differentiable quaternion functions by the GHR calculus still remains an open area, and this work provides a foundation and an avenue for further research in this direction.

REFERENCES
[1] W. R. Hamilton, “On a new species of imaginary quantities, connected with the theory of quaternions,” in Proceedings of the Royal Irish Academy (1836-1869), vol. 2. JSTOR, 1840, pp. 424–434.
[2] L. Qi, Z. Luo, Q. Wang, and X. Zhang, “Quaternion matrix optimization: Motivation and analysis,” Journal of Optimization Theory and Applications, vol. 193, no. 1-3, pp. 621–648, 2022.
[3] Z. Jia, Q. Jin, M. K. Ng, and X. Zhao, “Non-local robust quaternion matrix completion for large-scale color image and video inpainting,” IEEE Transactions on Image Processing, vol. 31, pp. 3868–3883, 2022.
[4] C. C. Took and D. P. Mandic, “Augmented secondorder statistics of quaternion random signals,” Signal Processing, vol. 91, no. 2, pp. 214–224, 2011.
[5] J. Flamant, S. Miron, and D. Brie, “Quaternion nonnegative matrix factorization: Deﬁnition, uniqueness, and algorithm,” IEEE Transactions on Signal Processing, vol. 68, pp. 1870–1883, 2020.

[6] C. C. Took and D. P. Mandic, “A quaternion widely linear adaptive ﬁlter,” IEEE Transactions on Signal Processing, vol. 58, no. 8, pp. 4427–4431, 2010.
[7] H. Zhang, Z. Wang, D. Chen, S. Zhu, and D. Xu, “Quaternion extreme learning machine based on real augmented representation,” IEEE Signal Processing Letters, vol. 30, pp. 175–179, 2023.
[8] S. Walia, K. Kumar, and M. Kumar, “Unveiling digital image forgeries using Markov based quaternions in frequency domain and fusion of machine learning algorithms,” Multimedia Tools and Applications, vol. 82, no. 3, pp. 4517–4532, 2023.
[9] B. C. Ujang, C. C. Took, and D. P. Mandic, “Quaternionvalued nonlinear adaptive ﬁltering,” IEEE Transactions on Neural Networks, vol. 22, no. 8, pp. 1193–1206, 2011.
[10] J. Flamant, N. Le Bihan, and P. Chainais, “Timefrequency analysis of bivariate signals,” Applied and Computational Harmonic Analysis, vol. 46, no. 2, pp. 351–383, 2019.
[11] T. Ogunfunmi and C. Safarian, “The quaternion stochastic information gradient algorithm for nonlinear adaptive systems,” IEEE Transactions on Signal Processing, vol. 67, no. 23, pp. 5909–5921, 2019.
[12] E. C. Mengu¨c¸, “Design of quaternion-valued secondorder Volterra adaptive ﬁlters for nonlinear 3-D and 4-D signals,” Signal Processing, vol. 174, p. 107619, 2020.
[13] Y. Xia, S. Tao, Z. Li, M. Xiang, W. Pei, and D. P. Mandic, “Full mean square performance bounds on quaternion estimators for improper data,” IEEE Transactions on Signal Processing, vol. 67, no. 15, pp. 4093–4106, 2019.
[14] S. Enshaeifar, S. Kouchaki, C. Cheong Took, and S. Sanei, “Quaternion singular spectrum analysis of electroencephalogram with application in sleep analysis,” IEEE Transactions on Neural Systems and Rehabilitation, vol. 24, no. 1, pp. 57–67, Jan. 2016.
[15] Z. Luo and W. Yu, “An introduction to convex optimization for communications and signal processing,” IEEE Journal on Selected Areas in Communications, vol. 24, no. 8, pp. 1426–1438, 2006.
[16] S. Sra, S. Nowozin, and S. J. Wright, Optimization for Machine Learning. MIT Press, 2012.
[17] M. Jaggi, “Sparse convex optimization methods for machine learning,” Ph.D. dissertation, ETH Zu¨rich, 2011.
[18] N. Krejic´, N. K. Jerinkic´, and T. Ostojic´, “An inexact restoration-nonsmooth algorithm with variable accuracy for stochastic nonsmooth convex optimization problems in machine learning and stochastic linear complementarity problems,” Journal of Computational and Applied Mathematics, vol. 423, p. 114943, 2023.
[19] Y. Xia and D. P. Mandic, “Complementary mean square analysis of augmented CLMS for second-order noncircular Gaussian signals,” IEEE Signal Processing Letters, vol. 24, no. 9, pp. 1413–1417, 2017.
[20] Y. Xia and D. P. Mandic, “A full mean square analysis of CLMS for second-order noncircular inputs,” IEEE Transactions on Signal Processing, vol. 65, no. 21, pp. 5578–5590, 2017.
[21] A. B. Gershman, N. D. Sidiropoulos, S. Shahbazpanahi,

11

M. Bengtsson, and B. Ottersten, “Convex optimizationbased beamforming,” IEEE Signal Processing Magazine, vol. 27, no. 3, pp. 62–75, 2010. [22] J. Flamant, S. Miron, and D. Brie, “A general framework for constrained convex quaternion optimization,” IEEE Transactions on Signal Processing, vol. 70, pp. 254–267, 2022. [23] Y. Liu, Y. Zheng, J. Lu, J. Cao, and L. Rutkowski, “Constrained quaternion-variable convex optimization: A quaternion-valued recurrent neural network approach,” IEEE Transactions on Neural Networks and Learning Systems, vol. 31, no. 3, pp. 1022–1035, 2019. [24] D. Xu, C. Jahanchahi, C. C. Took, and D. P. Mandic, “Enabling quaternion derivatives: The generalized HR calculus,” Royal Society Open Science, vol. 2, no. 8, p. 150255, 2015. [25] A. Hjørungnes, Complex-valued Matrix Derivatives: With Applications in Signal Processing and Communications. Cambridge University Press, 2011. [26] W. Wirtinger, “Zur formalen theorie der funktionen von mehr komplexen vera¨nderlichen,” Mathematische Annalen, vol. 97, no. 1, pp. 357–375, 1927. [27] D. Brandwood, “A complex gradient operator and its application in adaptive array theory,” in IEE Proceedings H (Microwaves, Optics and Antennas), vol. 130, no. 1. IET Digital Library, 1983, pp. 11–16. [28] P. Arena, L. Fortuna, G. Muscato, and M. G. Xibilia, “Multilayer perceptrons to approximate quaternion valued functions,” Neural Networks, vol. 10, no. 2, pp. 335– 342, 1997. [29] M. Yoshida, Y. Kuroe, and T. Mori, “A model of hopﬁeldtype quaternion neural networks and its energy function,” in Neural Information Processing. Springer, 2004, pp. 110–115. [30] E. C. Mengu¨c¸, “Novel quaternion-valued least-mean kurtosis adaptive ﬁltering algorithm based on the GHR calculus,” IET Signal Processing, vol. 12, no. 4, pp. 487– 495, 2018. [31] C. C. Took and Y. Xia, “Multichannel quaternion least mean square algorithm,” in IEEE International Conference on Acoustics, Speech and Signal Processing, 2019, pp. 8524–8527. [32] T. Parcollet, M. Morchid, and G. Linare`s, “A survey of quaternion neural networks,” Artiﬁcial Intelligence Review, vol. 53, pp. 2957–2982, 2020. [33] D. Xu, Y. Xia, and D. P. Mandic, “Optimization in quaternion dynamic systems: Gradient, Hessian, and learning algorithms,” IEEE Transactions on Neural Networks and Learning Systems, vol. 27, no. 2, pp. 249–261, 2015. [34] J. Ward, Quaternions and Cayley Numbers: Algebra and Applications. Springer Science, 1997. [35] T. A. Ell and S. J. Sangwine, “Quaternion involutions and anti-involutions,” Computers & Mathematics with Applications, vol. 53, no. 1, pp. 137–143, 2007. [36] D. Xu and D. P. Mandic, “The theory of quaternion matrix derivatives,” IEEE Transactions on Signal Processing, vol. 63, no. 6, pp. 1543–1556, 2015. [37] A. Sudbery, “Quaternionic analysis,” in Mathematical

Proceedings of the Cambridge Philosophical Society, vol. 85, no. 2. Cambridge University Press, 1979, pp. 199–225. [38] J. V´ıa, D. Ram´ırez, and I. Santamar´ıa, “Properness and widely linear processing of quaternion random vectors,” IEEE Transactions on Information Theory, vol. 56, no. 7, pp. 3502–3515, 2010. [39] D. P. Mandic, C. Jahanchahi, and C. C. Took, “A quaternion gradient operator and its applications,” IEEE Signal Processing Letters, vol. 18, no. 1, pp. 47–50, 2011. [40] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge University Press, 2004. [41] Y. Nesterov, Lectures on Convex Optimization. Springer, 2018. [42] R. A. Horn and C. R. Johnson, Matrix Analysis. Cambridge university press, 2012. [43] C. Chi, W. Li, and C. Lin, Convex Optimization for Signal Processing and Communications: From Fundamentals to Applications. CRC Press, 2017.


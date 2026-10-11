# From pulse construction to exact robustness cost

This guide connects one external reading to the repository's results. The
route is **closed oscillator trajectories → linear constraints → a phase
eigenproblem → independent forces → an exact robustness cost**. It is aimed
at a reader comfortable with basic quantum mechanics who wants to reproduce
the argument with pencil and paper.

## One source and a reading route

**R. Blümel et al., *Power-optimal, stabilized entangling gate between
trapped-ion qubits* (2021),
[arXiv:1905.09292v2, paper and supplement together](https://arxiv.org/pdf/1905.09292v2).**
This is a research article with detailed derivations, used here as a tutorial
anchor. The supplement is part of the same source.

| Read in order | Extract this idea |
|---|---|
| Main construction through §II, Eqs. (3)–(6) | Closure constraints, projected phase optimization, displacement derivatives |
| S2–S4 | Gate conventions, pulse symmetry, coefficient-space construction |
| S8 | Frequency derivatives become extra linear constraints |
| S14–S15 | Displacement and angle stabilization are different requirements |
| S16, Eqs. (S82)–(S83) | Independent pulses give bilinear phase and derivative constraints |

S16 constructs one pulse after choosing the other. The bridge below develops
our joint optimum for one oscillator and one static error. The source's
multimode, higher-order problem has a different scope; see
[the matched comparison](RELATED_WORK.md#blümel-et-al-independently-stabilized-pulses).

Useful prerequisites are Pauli operators, oscillator ladder operators,
unitary evolution, complex inner products, orthogonal projection, and the
spectral theorem for Hermitian matrices. The displacement-operator dynamics
are derived in [Theory §2](THEORY.md#2-exact-dynamics-and-the-physical-derivative).
The cost proof in §4 is constructive; prior knowledge of the equality S-lemma
is not required. Numerical-range convexity enters only for the full budget
frontier, where its use is stated explicitly.

## Translate the conventions first

| Source notation | Repository convention |
|---|---|
| $`\tau`$ | Duration $`T`$ |
| $`\sigma_x^i\sigma_x^j`$ | $`Z_1Z_2`$ after a fixed local basis rotation |
| $`\chi_{ij}`$ | Gate-phase parameter; our $`\chi`$ instead means $`\partial_\delta\Theta(0)`$ |
| Phase matrices $`D,S,R`$ | Our phase matrix is $`K`$; our $`D`$ is the positive trajectory-overlap matrix |

Source Eq. (2) gives, under that basis rotation,

```math
\Theta=-\frac{\theta_{ij}}2=-2\chi_{ij}.
```

Fix the unwrapped target angle before comparing resources. In this repository
the Hamiltonian and cost are

```math
H_\delta(t)=\delta a^\dagger a+
\sum_{j=1}^2 Z_j[f_j(t)a^\dagger+f_j(t)^*a],
\qquad
E=\int_0^T(|f_1(t)|^2+|f_2(t)|^2)\,dt.
```

The forces are independent complex functions, fixed before the unknown
error is realized. A physical pulse must be translated into the coefficient
of $`a^\dagger`$ in this Hamiltonian, with its coupling factors and rotating
frame included. Its raw control coefficients need not have the same norm as
the effective force. The [sideband mapping](CONTROL_ACCESS.md) makes this
translation explicit. A real pulse family need not grant every direction in
a complex force space.

Our error is positive **oscillator-number detuning** $`+\delta a^\dagger a`$.
Its interaction-picture force is $`f_j(t)e^{i\delta t}`$. A laser-detuning
offset defined with the opposite sign reverses the angle derivative. Obtain
the sign from the Hamiltonian before translating a slope; a zero-slope
condition alone cannot reveal a sign error.

## Linear conditions define the force space

Start from a finite family of candidate functions and impose homogeneous
linear conditions on their coefficients. Nominal closure is

```math
\int_0^T f(t)\,dt=0.
```

With $`\alpha(t)=-i\int_0^t f(u)\,du`$, the first displacement derivative
vanishes precisely when

```math
m:=\int_0^T\alpha(t)\,dt
=i\int_0^Tt f(t)\,dt=0,
\qquad
\beta(T;\delta)=-i\delta m+O(\delta^2).
```

The surviving nullspace is the allowed force space $`V`$. Include the first
moment when displacement robustness is required; closure alone does not
include it. The same space and duration must be granted to nominal and
angle-robust competitors.

Choose an orthonormal basis of $`V`$ under
$`\langle f,g\rangle=\int_0^T f^*g\,dt`$. For a nonorthonormal basis with
Gram matrix $`G`$, first whiten its coefficients using $`G^{1/2}`$ and its
quadratic-form matrices using $`G^{-1/2}`$ on both sides. Otherwise a
Euclidean coefficient norm changes the declared resource.

## Two matrices carry the physics

Let $`(Af)(t)=\int_0^t f(u)\,du`$ and let $`P_V`$ be orthogonal projection.
Restricted to $`V`$, define

```math
K=P_V\frac{A^\dagger-A}{2i}P_V,
\qquad D=P_VA^\dagger AP_V.
```

For the two force coefficient vectors $`c_1,c_2`$,

```math
\Theta=2\operatorname{Re}(c_1^\dagger Kc_2),\qquad
\chi=-2\operatorname{Re}(c_1^\dagger Dc_2),\qquad
E=\|c_1\|^2+\|c_2\|^2.
```

Here $`K`$ is Hermitian and $`D`$ is positive definite on nonzero $`V`$:
$`\langle f,Df\rangle=\|Af\|^2`$, which can vanish only for zero force.
The two matrices measure different features of the same trajectories:
oriented area determines phase, while cross-trajectory overlap determines
its static slope. [Theory §§2–3](THEORY.md#2-exact-dynamics-and-the-physical-derivative)
derives both identities and their parity-occupation interpretation.

For a common force $`c_1=c_2=c`$, phase per unit cost is the Rayleigh quotient
$`c^\dagger Kc/\|c\|^2`$. An extreme phase eigenvector, with an appropriate
relative sign between the forces, attains the nominal minimum

```math
E_{\mathrm{nom}}=\frac{|\Theta_0|}{\|K\|}.
```

Common nonzero forces, however, have $`\chi=-2c^\dagger Dc<0`$. Their
displacement derivatives may vanish while their angle derivative remains.
Independent forces replace that positive quadratic form by a bilinear
overlap that can cancel.

## From a feasible pair to the joint optimum

Set $`x=(c_1+c_2)/\sqrt2`$ and $`y=(c_1-c_2)/\sqrt2`$. Angle robustness is
$`x^\dagger Dx=y^\dagger Dy`$, so every real scalar $`\zeta`$ gives

```math
|\Theta_0|
=\left|x^\dagger(K-\zeta D)x-y^\dagger(K-\zeta D)y\right|
\leq\|K-\zeta D\|E.
```

Minimizing the matrix norm produces the strongest bound of this form:

```math
r=\min_{\zeta\in\mathbb R}\|K-\zeta D\|,
\qquad E_{\mathrm{angle}}=\frac{|\Theta_0|}{r}.
```

For $`r>0`$, equality is attained. At the unique minimizing $`\zeta_*`$, the extreme
eigenvalues of $`K-\zeta_*D`$ are $`+r,-r`$. Their eigenvectors supply
$`x,y`$, weighted to balance their $`D`$ expectations. The explicit forces
and proof are in [Theory §4](THEORY.md#4-exact-joint-minimum-and-attaining-forces).
The multiplier is a mathematical variable with frequency units; no estimate
or reversal of the unknown error is involved.

A zero denominator means that the nonzero target is infeasible. In
particular, $`r=0`$ precisely when $`K`$ is a real scalar multiple of $`D`$.
For a nominally feasible space, angle robustness has no extra cost precisely
when the extreme eigenvalues of $`K`$ are balanced about zero. These statements compare joint optima in
the same specified space.

## Worked check: two positive tones

Use dimensionless time, $`T=2\pi`$, and the orthonormal basis
$`u_n(t)=e^{int}/\sqrt{2\pi}`$ for $`n=1,2`$. Both tones close at $`T`$.
Their primitives and resulting matrices are

```math
Au_n(t)=\frac{e^{int}-1}{in\sqrt{2\pi}},\qquad
K=\begin{pmatrix}1&0\\0&1/2\end{pmatrix},\qquad
D=\begin{pmatrix}2&1/2\\1/2&1/2\end{pmatrix}.
```

The constant terms in the primitives produce the off-diagonal overlap in
$`D`$. For $`\Theta_0=1`$, the nominal coefficients
$`c_1=c_2=(1,0)^T/\sqrt2`$ give $`E=1`$, $`\Theta=1`$, and $`\chi=-2`$.
To obtain the robust optimum, center the two eigenvalues:

```math
\operatorname{tr}(K-\zeta D)=\frac32-\frac52\zeta=0
\quad\Longrightarrow\quad
\zeta_*=\frac35,\qquad
K-\zeta_*D=
\begin{pmatrix}-1/5&-3/10\\-3/10&1/5\end{pmatrix}.
```

Its eigenvalues are $`\pm\sqrt{13}/10`$. Therefore

```math
E_{\mathrm{nom}}=1,\qquad
E_{\mathrm{angle}}=\frac{10}{\sqrt{13}}.
```

This is the existing [two-tone frontier example](SENSITIVITY_FRONTIER.md#a-physical-two-tone-example-where-the-old-certificate-is-strict).
It also supplies an attaining pair at an intermediate budget. The example
imposes closure only: its slope does not by itself specify full thermal
gate error. Trace centering works here because the matrix is two-dimensional;
in higher dimensions one centers the two extreme eigenvalues instead.

## Where the result goes next

| Question after the worked check | Read |
|---|---|
| How are optimal forces constructed, and when is robustness free? | [Theory §§4–5](THEORY.md#4-exact-joint-minimum-and-attaining-forces) |
| What slope is unavoidable below the robust budget? | [Exact sensitivity frontier](SENSITIVITY_FRONTIER.md), which optimizes all supporting multipliers |
| When does the whole thermal gate have quartic-or-better error? | [Theory §6](THEORY.md#6-full-thermal-gate-error-and-its-exact-minimum): both displacement moments and the angle slope must vanish |
| Can the cost ratio grow without bound? | [Spectral restriction and four-tone family](SPECTRAL_RESTRICTION.md) |
| Which controls grant conjugate force directions? | [Physical control access](CONTROL_ACCESS.md) |
| How can the calculations be reproduced? | [Verification instructions](../REPRODUCIBILITY.md) |

## Check your understanding

1. **Why does a closed trajectory still have angle error?** Closure fixes
   its endpoint. The angle slope depends on the integrated overlap of two
   trajectories, which need not vanish.
2. **Why project out displacement moments before optimizing full-gate cost?**
   The thermal error has positive contributions from both displacement
   derivatives and the angle slope. Its exact coefficient and moment-kernel
   optimization are in [Theory §6](THEORY.md#6-full-thermal-gate-error-and-its-exact-minimum).
3. **Can a one-dimensional force space make a nonzero robust gate?** No.
   Both matrices are scalars with $`D>0`$, hence $`K=\zeta D`$ and $`r=0`$.
4. **Does a conjugation-invariant space make every robustness requirement
   free?** It makes angle robustness free within that space. Imposing
   displacement moments can first increase the nominal cost.
5. **Does the theorem optimize laboratory laser power or peak amplitude?**
   Its resource is the sum of integrated squared effective forces. Such
   comparisons require the corresponding control map and constraints.

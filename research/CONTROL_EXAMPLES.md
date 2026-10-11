# Four tones: joint cost, pulse selection, and individual peaks

One symmetric four-tone space illustrates three distinct statements: angle
robustness can be free at the joint integrated-force optimum; fixing one
pulse beforehand can increase that cost; and equal integrated costs can
require different individual peak amplitudes. All comparisons below use
the [same oscillator model and force normalization](THEORY.md#1-model-resource-and-requirements).

## The allowed space and its exact optimum

Fix $T>0$, put $\nu=2\pi/T$, and permit the full complex span of
$e^{in\nu t}$ for $n\in\{1,2,-1,-2\}$, subject to

$$
f(0)=f(T)=0,\qquad \int_0^T t f(t)\,dt=0.
$$

Nominal closure is automatic. In the indicated harmonic order, the two
independent coefficient constraints are $\sum_n c_n=0$ and
$\sum_n c_n/n=0$. The complete allowed space therefore has complex
dimension two, with real orthonormal basis

$$
u(t)=\sqrt{\frac{2}{5T}}\,[\sin\nu t-2\sin2\nu t],\qquad
v(t)=\frac{\cos\nu t-\cos2\nu t}{\sqrt T}.
$$

For force coefficient vectors $a,b$ in this basis, direct integration gives

$$
K=kJ,\qquad k=\frac{2}{\sqrt{10}\nu},\qquad
J=\begin{pmatrix}0&i\\-i&0\end{pmatrix},\qquad
D=\frac1{\nu^2}\begin{pmatrix}2/5&0\\0&5/8\end{pmatrix}.
$$

Thus $\Theta=2\mathrm{Re}(a^\dagger Kb)$,
$\chi=-2\mathrm{Re}(a^\dagger Db)$, and
$E=\|a\|^2+\|b\|^2$. The phase eigenvalues are $\pm k$, so the
[balanced-spectrum theorem](THEORY.md#5-free-costly-and-infeasible-robustness)
gives

$$
E_{\min}:=E_{\mathrm{nom}}=E_{\mathrm{angle}}
=\frac{|\Theta_0|}{k}
=\frac{\pi\sqrt{10}|\Theta_0|}{T}.
$$

Take $\Theta_0>0$ and $A=\sqrt{E_{\min}/2}$. A nominal common optimum is
$a=b=Ag$, where $g=(i,1)^T/\sqrt2$ and $Kg=kg$. The independent pair

$$a=A(i,0)^T,\qquad b=A(0,1)^T$$

has the same target and cost, with $\chi=0$. All forces in the space already
have zero first displacement derivative, so this pair also attains the
quartic-or-better thermal-infidelity minimum. For a negative target, reverse
one force; the costs and individual peaks are unchanged.

## The cost of fixing the first pulse

[Blümel et al., supplement S16](RELATED_WORK.md#blümel-et-al-independently-stabilized-pulses)
construct a stabilized second pulse after selecting a nominal optimal first
pulse. Adapt that prescription to the space above by fixing the first
direction to $g$. This is a matched calculation in the present effective-force
model; the source's multimode laboratory pulses use different constraints
and normalization.

Define

$$
Q_g=I-\frac{(Dg)(Dg)^\dagger}{\|Dg\|^2},\qquad
\kappa=\|Q_g g\|=\frac9{\sqrt{1762}}.
$$

To compute the restricted optimum, write $a=s g$, $s>0$. Robustness requires
$\mathrm{Re}[(Dg)^\dagger b]=0$. Since $g^\dagger Dg$ is real,
$Q_g g$ is also the projection of $g$ onto this constraint hyperplane under
the real inner product $\mathrm{Re}(z^\dagger w)$. Consequently

$$
\mathrm{Re}(g^\dagger b)
=\mathrm{Re}[(Q_g g)^\dagger b]
\leq\kappa\|b\|.
$$

This bound covers every complex second pulse satisfying the real robustness
constraint. Equality is attained in direction $Q_g g/\kappa$. Using
$Kg=kg$ and $2s\|b\|\leq s^2+\|b\|^2=E$ gives
$\Theta\leq k\kappa E$, with equality for equal force norms. Therefore

$$
\boxed{\frac{E_{\mathrm{fixed\ first}}}{E_{\min}}
=\frac1\kappa=\frac{\sqrt{1762}}9
=4.664020413736748\ldots.}
$$

The factor measures the restriction of freezing this particular first-pulse
direction. Joint selection admits the robust pair at cost $E_{\min}$ above.
It is not a universal performance ratio against the source's independent-pulse
method or a laboratory power comparison.

## Every robust cost-minimizer exceeds the nominal individual peak cap

The nominal common pair $a=b=Ag$ defines a per-qubit peak cap. To compare it
with all robust minimizers, first characterize equality in

$$
\Theta=2k\mathrm{Re}(a^\dagger Jb)
\leq 2k\|a\|\|b\|\leq kE.
$$

For the positive target and $E=E_{\min}$, equality requires equal force norms
and $b=Ja$. Write $D=\mathrm{diag}(d_1,d_2)$; then
$DJ+JD=(d_1+d_2)J$. Hence zero slope requires $a^\dagger Ja=0$.
Every such pair, up to a common phase, is

$$
a=A(\cos\vartheta,\sin\vartheta)^T,\qquad
b=iA(\sin\vartheta,-\cos\vartheta)^T.
$$

This is the complete family of robust integrated-cost minimizers. Set
$\tau=\nu t$ and define

$$
U(\tau)=\sqrt{2/5}\,(\sin\tau-2\sin2\tau),\qquad
V(\tau)=\cos\tau-\cos2\tau,
$$

so $u(t)=U(\nu t)/\sqrt T$ and $v(t)=V(\nu t)/\sqrt T$.
With $c=\cos\tau$,

$$
4-(U^2+V^2)=\frac{(c+1)^2(12c^2-20c+13)}5\geq0.
$$

The nominal common force $A(iu+v)/\sqrt2$ therefore has peak
$F_{\max}=\sqrt2 A/\sqrt T$, attained at $\tau=\pi$.
At this midpoint, $U=0$ and $V=-2$. Requiring both robust forces to obey
that same peak cap forces
$|\sin\vartheta|=|\cos\vartheta|=1/\sqrt2$.
But $U'(\pi)=-\sqrt{10}$ and $V'(\pi)=0$, where the primes denote
$\tau$ derivatives. At every permitted orientation, the first force has a
nonzero magnitude derivative at a nonzero value already equal to the cap.
Its magnitude must exceed the cap on one side of this interior point.

Thus **every robust pair at the exact minimum integrated cost violates the
nominal common pair's individual peak cap**. The conclusion concerns the
cost-minimizing family; individual-peak constraints specify a different
optimization problem.

# Control access and the effective-force resource

The [spectral-cost bound](SPECTRAL_RESTRICTION.md) concerns a prescribed
output-force space. A frequency direction absent from that space differs
fundamentally from one transmitted with a small nonzero gain. With unrestricted
input coefficients and cost measured at the effective force, attenuation alone
does not remove a direction. Completing a space with all its conjugates gives

$$E_{\mathrm{angle}}(V+\overline V)
=E_{\mathrm{nom}}(V+\overline V)\leq E_{\mathrm{nom}}(V),$$

provided the nominal nonzero target in $V$ is feasible. This is an elementary
consequence of the existing [balanced-spectrum theorem](CLAIMS.md#c2-when-the-angle-penalty-vanishes).
It specifies the control and resource assumptions needed to interpret a
positive-band penalty physically.

## From balanced sidebands to an effective force

Use one selected motional mode, the Lamb–Dicke and sideband rotating-wave
approximations, and balanced real red/blue Rabi envelopes $\Omega_j(t)$.
Let $\eta_j$ include the selected mode's real participation factor and put
$g_j=\eta_j\Omega_j/2$. A phase convention consistent with the standard
sideband decomposition in [Lee et al., Eqs. (28)–(30)](https://arxiv.org/pdf/quant-ph/0505203)
is

$$H_j=g_j\sigma_+^j
\left[a e^{i\Delta t-i\phi_r^j}
+a^\dagger e^{-i\Delta t-i\phi_b^j}\right]+\mathrm{h.c.}$$

$\Delta$ is a known nominal offset; it is distinct from the unknown oscillator
error $\delta$ in the project Hamiltonian. Define

$$\phi_s^j=\frac{\phi_b^j+\phi_r^j}{2},\qquad
\phi_m^j=\frac{\phi_b^j-\phi_r^j}{2},\qquad
\sigma_{\phi_s}=\sigma_+e^{-i\phi_s}+\sigma_-e^{i\phi_s}.$$

Collecting the coefficients of $a$ and $a^\dagger$ gives exactly

$$H_j=g_j\sigma_{\phi_s^j}
\left[a e^{i(\Delta t+\phi_m^j)}
+a^\dagger e^{-i(\Delta t+\phi_m^j)}\right].$$

For a time-independent spin axis, a fixed change of basis identifies
$\sigma_{\phi_s^j}$ with $Z_j$. The project force and cost are then

$$f_j(t)=\frac{\eta_j\Omega_j(t)}2e^{-i(\Delta t+\phi_m^j(t))},\qquad
E=\frac14\sum_j\eta_j^2\int_0^T\Omega_j(t)^2dt.$$

This is a squared effective-Rabi resource with fixed couplings. An equality
with total optical or RF energy requires a separate calibrated resource
model. Unbalanced sideband envelopes generally prevent this factorization.
A time-dependent spin axis falls outside the project's fixed commuting-spin
model, even when the instantaneous factorization holds.

Opposite changes of the sideband phases preserve $\phi_s$ and change
$\phi_m$; equal changes rotate the spin axis. At a fixed known $\Delta$,
the prescription

$$\phi_m'(t)=-\phi_m(t)-2\Delta t$$

produces $f_j^*(t)$ with the same envelope magnitude. Alternatively, reverse
the known offset and negate $\phi_m$. Negating $\phi_m$ alone at nonzero
fixed $\Delta$ is insufficient. These prescriptions are conditional on the
allowed phase/frequency range and waveform representation.

They do not use or reverse the unknown error. In the interaction picture of
$\delta a^\dagger a$, replacing the commanded force by $f_j^*$ gives the
coefficient $f_j^*e^{i\delta t}$ of $a^\dagger$, not
$f_j^*e^{-i\delta t}$. Thus the control remains error independent.

## Nonzero attenuation and conjugate completion

Let $v_1,\ldots,v_d$ span the already-admissible finite space $V$, and suppose
independent unrestricted inputs generate

$$W_\gamma=\left\{\sum_k x_kv_k+\sum_k\gamma_k y_k\overline{v_k}:
x_k,y_k\in\mathbb C\right\},\qquad\gamma_k\ne0.$$

Every desired conjugate coefficient $z_k$ is obtained by setting
$y_k=z_k/\gamma_k$. Hence

$$W_\gamma=V+\overline V=:W,\qquad \overline W=W.$$

Closure, zero first force moment, and zero endpoint values survive
conjugation and addition. More generally, common homogeneous real-weight
moment constraints survive. The phase spectrum on $W$ is balanced, so C2
gives $E_{\mathrm{angle}}(W)=E_{\mathrm{nom}}(W)$. Inclusion $V\subset W$
gives the opening inequality. Feasibility follows from feasibility in $V$.
With first moments already imposed, the robust cost is also the quartic
thermal-infidelity minimum in $W$.

The nominal optimum in this statement is recomputed in $W$. If a larger
space $S$ merely contains $W$, one can conclude
$E_{\mathrm{angle}}(S)\leq E_{\mathrm{nom}}(V)$, but equality between
$E_{\mathrm{angle}}(S)$ and $E_{\mathrm{nom}}(S)$ requires the appropriate
balanced-spectrum condition on $S$ itself.

For orthonormal raw harmonics with diagonal transfer gains $h_\ell$, the same
point is visible in $c_\ell=h_\ell u_\ell$:

$$E_{\mathrm{output}}=\sum_\ell|c_\ell|^2,
\qquad \sum_\ell|u_\ell|^2
=\sum_\ell\frac{|c_\ell|^2}{|h_\ell|^2}.$$

Every nonzero gain leaves the unrestricted output span unchanged. A fixed
nonzero output component needs input magnitude proportional to $1/|h_\ell|$.
An input cap or an input-norm objective would therefore matter, but is a
different admissible set or resource. An exact zero gain can remove a
direction. Uncontrolled leakage is not independently commandable access and
does not meet this lemma's assumptions.

### Worked comparison using the four-tone family

Let $V_N$ be the two-dimensional positive four-tone space in the
[spectral proof](SPECTRAL_RESTRICTION.md). Permit both its basis directions
and their independently commanded conjugates with gain $\varepsilon\ne0$.
The resulting space is $W_N=V_N+\overline{V_N}$, of dimension four. For
every such gain, its additional angle-robustness cost is zero, whereas the
ratio within $V_N$ grows as $2\sqrt5 N/3$.

These are different granted control spaces, not an improvement within $V_N$.
If instead all eight raw harmonics are granted and only the two combined
endpoint/moment constraints are imposed, the admissible dimension is six.
That space is also conjugation invariant, but has its own nominal optimum.

## What the QSCOUT example establishes

[Yale et al.](https://arxiv.org/html/2504.06259v1), Introduction and Eq. (2),
describe individually addressed two-tone controls and a multimode Hamiltonian.
Section II selects Gaussian shaping and mode balancing. Sections III–IV
describe saturation and optical coupling calibration. Selecting one mode
gives a conditional effective-force mapping, not an account of that complete
operating protocol.

[Clark et al.](https://arxiv.org/html/2104.00759v1), Section VI A, document
tone-resolved amplitude, phase, and frequency programming, together with
finite RF range, digital precision, spline, and memory constraints. Those
constraints do not by themselves impose a positive-harmonic output-force
space relative to one motional mode. Positive laboratory frequencies and
the two red/blue tones are not the signs of that output-force spectrum.

**Audit conclusion:** this documented candidate does not establish the hard
one-sided restriction required to interpret the spectral penalty as an
unavoidable device constraint. The phase dictionary identifies the control
to check; it does not prove every mirrored waveform satisfies the hardware's
limits. The attenuation lemma also does not establish that a real device has
unrestricted inputs or a conjugation-invariant feasible set.

A valid realization would additionally need the chosen offsets, modulation,
and required amplitudes to preserve the sideband and Lamb–Dicke approximations,
with the neglected modes under control. The checked mode-balancing protocol
does not certify that regime for the one-sided family. Assigning a numerical
operating window would therefore be unsupported. The exact restricted-space
cost theorem and its asymptotics remain unchanged.

import numpy as np
import matplotlib.pyplot as plt

# ── IVP: dy/dx = 2xy,  y(0)=1,  exact: y = e^{x^2} ──────────
def f(x, y):
    return 2 * x * y

y_exact_08 = np.exp(0.64)

# ── Generate "truth" data via RK4 at various step sizes ───────
def rk4_solve(h, x_end=0.8):
    N = int(x_end / h)
    x = np.zeros(N + 1)
    y = np.zeros(N + 1)
    y[0] = 1.0
    for n in range(N):
        k1 = f(x[n],       y[n])
        k2 = f(x[n]+h/2,   y[n]+h/2*k1)
        k3 = f(x[n]+h/2,   y[n]+h/2*k2)
        k4 = f(x[n]+h,     y[n]+h*k3)
        y[n+1] = y[n] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x[n+1] = x[n] + h
    return x, y

def ab4_predict(h):
    """Generate 4 starting values via RK4, then apply AB4 predictor."""
    x_rk, y_rk = rk4_solve(h, x_end=3*h + 1e-15)
    xv = x_rk[:4]
    yv = y_rk[:4]
    fv = f(xv, yv)  # Vectorized computation
    y_pred = yv[3] + (h/24)*(55*fv[3] - 59*fv[2] + 37*fv[1] - 9*fv[0])
    return 3*h + h, y_pred  # x_pred, y_pred

# ── Convergence study ─────────────────────────────────────────
step_sizes = [0.2, 0.1, 0.05, 0.025, 0.0125]
errors_ab4 = []

for hs in step_sizes:
    # We need 4 starting values from RK4, then predict with AB4
    # For a fair comparison, predict y at x = 4*h from x=0
    x_rk, y_rk = rk4_solve(hs, x_end=0.8)
    # Gather enough points for AB4
    if len(y_rk) >= 5:
        xv = np.array([i*hs for i in range(4)])
        yv = y_rk[:4]
        fv = f(xv, yv)  # Vectorized computation
        y_p = yv[3] + (hs/24)*(55*fv[3] - 59*fv[2] + 37*fv[1] - 9*fv[0])
        x_p = 4*hs
        y_e = np.exp(x_p**2)
        errors_ab4.append(abs(y_p - y_e))
    else:
        errors_ab4.append(np.nan)

# ── Plot: Error vs Step Size (log-log) ─────────────────────────
bg = '#0b1220'
curve_color = '#8fd3d1'
ref_color = '#f5e6a8'

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(bg)
ax.set_facecolor(bg)

ax.loglog(step_sizes, errors_ab4, 'o-', color=curve_color, lw=2, ms=8,
          label='AB4 predictor error')

# Reference line: O(h^4)
h_ref = np.array(step_sizes)
ref = (h_ref / step_sizes[0])**4 * errors_ab4[0]
ax.loglog(h_ref, ref, '--', color=ref_color, lw=1.5, label=r'$\mathcal{O}(h^4)$ reference')

ax.set_xlabel('Step size h', color='white', fontsize=12)
ax.set_ylabel('|Error|', color='white', fontsize=12)
ax.set_title('AB4 Predictor Error Convergence', color='white', fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor=bg, labelcolor='white', fontsize=11)
ax.grid(True, alpha=0.2, which='both')

plt.tight_layout()
plt.savefig('figs/error_convergence.png', dpi=150, facecolor=bg)
plt.show()

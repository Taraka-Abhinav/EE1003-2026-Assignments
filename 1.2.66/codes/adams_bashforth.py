import numpy as np
import matplotlib.pyplot as plt

# ── IVP: dy/dx = f(x,y) = 2xy,  y(0) = 1 ──────────────────────
def f(x, y):
    return 2 * x * y

# ── Given data points (step size h = 0.2) ──────────────────────
h = 0.2
x_vals = np.array([0.0, 0.2, 0.4, 0.6])
y_vals = np.array([1.0, 1.0408, 1.1735, 1.4333])

# ── Compute f_i = f(x_i, y_i) ─────────────────────────────────
f_vals = np.array([f(x_vals[i], y_vals[i]) for i in range(4)])
# f0 = 0,  f1 = 0.41632,  f2 = 0.9388,  f3 = 1.71996

# ── Adams–Bashforth 4-step predictor formula ───────────────────
#    y_{n+1} = y_n + (h/24)[55 f_n - 59 f_{n-1} + 37 f_{n-2} - 9 f_{n-3}]
n = 3   # predict y_4 = y(0.8)
y_pred = y_vals[n] + (h / 24) * (
    55 * f_vals[3] - 59 * f_vals[2] + 37 * f_vals[1] - 9 * f_vals[0]
)

print("="*55)
print("  Adams-Bashforth 4-Step Predictor for dy/dx = 2xy")
print("="*55)
for i in range(4):
    print(f"  x_{i} = {x_vals[i]:.1f},  y_{i} = {y_vals[i]:.4f},  f_{i} = {f_vals[i]:.5f}")
print("-"*55)
print(f"  Predicted y(0.8) = {y_pred:.4f}")
print(f"  Exact     y(0.8) = e^(0.64) = {np.exp(0.64):.4f}")
print(f"  Closest option: (c) 1.8890")
print("="*55)

# ── Exact solution: y(x) = e^{x^2} ────────────────────────────
x_exact = np.linspace(0, 1.0, 500)
y_exact = np.exp(x_exact**2)

# ── AB4 multi-step extension (using given + predicted) ─────────
x_ab = np.append(x_vals, 0.8)
y_ab = np.append(y_vals, y_pred)

# ── Plot ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_exact, y_exact, 'b-', lw=2.2, label=r'Exact: $y = e^{x^2}$')
ax.plot(x_ab, y_ab, 'ro--', ms=8, lw=1.5, label='Given data + AB4 prediction', zorder=5)
ax.axvline(0.8, color='gray', ls=':', lw=1, alpha=0.6)
ax.annotate(f'AB4 predicted\ny(0.8) = {y_pred:.4f}',
            xy=(0.8, y_pred), xytext=(0.55, 2.2),
            fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='red'))
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Adams–Bashforth 4-Step Predictor vs Exact Solution', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figs/ab4_predictor.png', dpi=150)
plt.show()

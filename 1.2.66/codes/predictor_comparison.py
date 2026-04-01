import numpy as np
import matplotlib.pyplot as plt

# ── IVP: dy/dx = 2xy,  y(0) = 1,  exact: y = e^{x^2} ────────
def f(x, y):
    return 2 * x * y

h = 0.2
x = np.array([0.0, 0.2, 0.4, 0.6])
y = np.array([1.0, 1.0408, 1.1735, 1.4333])
fv = np.array([f(x[i], y[i]) for i in range(4)])

y_exact_08 = np.exp(0.64)

# ── All Adams-Bashforth predictor orders ───────────────────────
# AB1 (Euler): y_{n+1} = y_n + h*f_n
y_ab1 = y[3] + h * fv[3]

# AB2: y_{n+1} = y_n + (h/2)(3f_n - f_{n-1})
y_ab2 = y[3] + (h / 2) * (3 * fv[3] - fv[2])

# AB3: y_{n+1} = y_n + (h/12)(23f_n - 16f_{n-1} + 5f_{n-2})
y_ab3 = y[3] + (h / 12) * (23 * fv[3] - 16 * fv[2] + 5 * fv[1])

# AB4: y_{n+1} = y_n + (h/24)(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})
y_ab4 = y[3] + (h / 24) * (55 * fv[3] - 59 * fv[2] + 37 * fv[1] - 9 * fv[0])

methods = ['AB1\n(Euler)', 'AB2\n(2-step)', 'AB3\n(3-step)', 'AB4\n(4-step)', 'Exact\n$e^{0.64}$']
values  = [y_ab1, y_ab2, y_ab3, y_ab4, y_exact_08]
errors  = [abs(v - y_exact_08) for v in values]
colors  = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71', '#9b59b6']

print(f"AB1 (Euler) : y(0.8) = {y_ab1:.6f},  error = {abs(y_ab1 - y_exact_08):.6f}")
print(f"AB2 (2-step): y(0.8) = {y_ab2:.6f},  error = {abs(y_ab2 - y_exact_08):.6f}")
print(f"AB3 (3-step): y(0.8) = {y_ab3:.6f},  error = {abs(y_ab3 - y_exact_08):.6f}")
print(f"AB4 (4-step): y(0.8) = {y_ab4:.6f},  error = {abs(y_ab4 - y_exact_08):.6f}")
print(f"Exact       : y(0.8) = {y_exact_08:.6f}")

# ── Bar chart: predicted values ────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

bars = ax1.bar(methods, values, color=colors, edgecolor='black', lw=0.8)
ax1.axhline(y_exact_08, color='purple', ls='--', lw=1.5, label=f'Exact = {y_exact_08:.4f}')
for bar, v in zip(bars, values):
    ax1.text(bar.get_x() + bar.get_width()/2, v + 0.01, f'{v:.4f}',
             ha='center', va='bottom', fontweight='bold', fontsize=9)
ax1.set_ylabel('y(0.8)', fontsize=12)
ax1.set_title('Predicted y(0.8) by Method', fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(axis='y', alpha=0.3)

# ── Bar chart: errors ──────────────────────────────────────────
bars2 = ax2.bar(methods[:-1], errors[:-1], color=colors[:-1], edgecolor='black', lw=0.8)
for bar, e in zip(bars2, errors[:-1]):
    ax2.text(bar.get_x() + bar.get_width()/2, e + 0.002, f'{e:.4f}',
             ha='center', va='bottom', fontweight='bold', fontsize=9)
ax2.set_ylabel('|Error|', fontsize=12)
ax2.set_title('Absolute Error Comparison', fontsize=13, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figs/predictor_comparison.png', dpi=150)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# ── IVP: dy/dx = f(x,y) = 2xy,  y(0) = 1 ──────────────────────
def f(x, y):
    return 2 * x * y

# ── RK4 solver ─────────────────────────────────────────────────
h     = 0.01       # fine step size
x_end = 1.2
N     = int(x_end / h)

x_rk = np.zeros(N + 1)
y_rk = np.zeros(N + 1)
y_rk[0] = 1.0      # y(0) = 1

for n in range(N):
    k1 = f(x_rk[n],         y_rk[n])
    k2 = f(x_rk[n] + h/2,   y_rk[n] + h/2 * k1)
    k3 = f(x_rk[n] + h/2,   y_rk[n] + h/2 * k2)
    k4 = f(x_rk[n] + h,     y_rk[n] + h   * k3)
    y_rk[n+1] = y_rk[n] + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
    x_rk[n+1] = x_rk[n] + h

# ── Exact solution: y = e^{x^2} ───────────────────────────────
x_ex = np.linspace(0, x_end, 1000)
y_ex = np.exp(x_ex**2)

# ── AB4 data points ───────────────────────────────────────────
x_data = np.array([0.0, 0.2, 0.4, 0.6])
y_data = np.array([1.0, 1.0408, 1.1735, 1.4333])
fv = np.array([f(x_data[i], y_data[i]) for i in range(4)])
y_ab4 = y_data[3] + (0.2/24)*(55*fv[3] - 59*fv[2] + 37*fv[1] - 9*fv[0])
x_ab = np.append(x_data, 0.8)
y_ab = np.append(y_data, y_ab4)

# ── Plot ───────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Left: solution overlay
ax1.plot(x_ex, y_ex, 'b-', lw=2.2, label=r'Exact: $y = e^{x^2}$')
ax1.plot(x_rk, y_rk, 'g--', lw=1.5, label='RK4 (h = 0.01)')
ax1.plot(x_ab, y_ab, 'ro', ms=9, zorder=5, label='Given + AB4 predicted')
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('RK4 vs Exact Solution', fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Right: error
y_exact_at_rk = np.exp(x_rk**2)
error = np.abs(y_rk - y_exact_at_rk)
ax2.semilogy(x_rk, error, 'r-', lw=1.5)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('|Error|', fontsize=12)
ax2.set_title('RK4 Absolute Error (h = 0.01)', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('figs/rk4_verification.png', dpi=150)
plt.show()

# ── Print table ────────────────────────────────────────────────
print(f"{'x':>6} {'RK4 y':>12} {'Exact y':>12} {'Error':>14}")
print("-"*48)
for xi in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    idx = int(xi / h)
    ye = np.exp(xi**2)
    print(f"{xi:6.1f} {y_rk[idx]:12.6f} {ye:12.6f} {abs(y_rk[idx]-ye):14.2e}")

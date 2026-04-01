import numpy as np
import matplotlib.pyplot as plt

# ── Direction field for dy/dx = 2xy ────────────────────────────
def f(x, y):
    return 2 * x * y

x_grid = np.linspace(-0.2, 1.2, 20)
y_grid = np.linspace(0.0, 3.5, 20)
X, Y = np.meshgrid(x_grid, y_grid)
DY = f(X, Y)
DX = np.ones_like(DY)
norm = np.sqrt(DX**2 + DY**2)
DX /= norm
DY /= norm

# ── Exact solution curve ──────────────────────────────────────
x_ex = np.linspace(0, 1.1, 300)
y_ex = np.exp(x_ex**2)

# ── Given data + AB4 prediction ───────────────────────────────
x_data = np.array([0.0, 0.2, 0.4, 0.6, 0.8])
y_data = np.array([1.0, 1.0408, 1.1735, 1.4333, 1.8884])

# ── Plot ──────────────────────────────────────────────────────
bg = '#0b1220'
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor(bg)
ax.set_facecolor(bg)

ax.quiver(X, Y, DX, DY, color='#445566', alpha=0.5, scale=30)
ax.plot(x_ex, y_ex, color='#8fd3d1', lw=2.5, label=r'Exact: $y = e^{x^2}$')
ax.plot(x_data, y_data, 'o', color='#f5e6a8', ms=9, zorder=5,
        label='Given data + AB4 prediction')

for i, (xi, yi) in enumerate(zip(x_data, y_data)):
    label = f'({xi:.1f}, {yi:.4f})'
    ax.annotate(label, (xi, yi), textcoords="offset points",
                xytext=(10, -15 if i % 2 == 0 else 10),
                fontsize=8, color='white',
                bbox=dict(boxstyle='round,pad=0.2', fc=bg, ec='#8fd3d1', alpha=0.8))

ax.set_xlabel('x', color='white', fontsize=12)
ax.set_ylabel('y', color='white', fontsize=12)
ax.set_title(r"Direction Field: $\frac{dy}{dx} = 2xy$", color='white',
             fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor=bg, labelcolor='white', fontsize=10, loc='upper left')
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(0, 3.5)
ax.grid(True, alpha=0.15)

plt.tight_layout()
plt.savefig('figs/direction_field.png', dpi=150, facecolor=bg)
plt.show()

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

FIGS = Path(__file__).parent.parent / 'figs'

def f(x):
    return x**3 - 3*x + 2

def df(x):
    return 3*x**2 - 3

x0 = -3.0
x1 = x0 - f(x0)/df(x0)   # = -7/3

plt.style.use('dark_background')

# ── Figure 1: Newton-Raphson first iteration ──────────────────────
fig1, ax1 = plt.subplots(figsize=(8, 5))

x = np.linspace(-4, 2, 600)
ax1.plot(x, f(x), color='cyan', lw=2, label=r'$f(x)=x^3-3x+2$')

tangent = f(x0) + df(x0)*(x - x0)
ax1.plot(x, tangent, '--', color='yellow', lw=1.5, label='Tangent at $x_0=-3$')

ax1.axhline(0, color='white', lw=0.6)
ax1.axvline(0, color='white', lw=0.6)

ax1.scatter(x0, f(x0), color='red', zorder=5, s=60, label=f'$x_0={x0}$, $f(x_0)={f(x0):.0f}$')
ax1.scatter(x1, 0, color='lime', zorder=5, s=60, label=f'$x_1={x1:.4f}$')
ax1.plot([x0, x0], [0, f(x0)], '--', color='red', lw=1)

ax1.annotate(r'$x_1 = -\frac{7}{3}$', (x1, 0),
             textcoords='offset points', xytext=(10, 12),
             ha='left', color='lime', fontsize=12, fontweight='bold')
ax1.annotate(r'$x_0 = -3$', (x0, f(x0)),
             textcoords='offset points', xytext=(8, -18),
             ha='left', color='red', fontsize=11)

ax1.set_xlabel('x', color='white')
ax1.set_ylabel('f(x)', color='white')
ax1.set_title('Newton-Raphson: First Iteration', color='white', fontweight='bold')
ax1.legend(fontsize=9)
ax1.set_ylim(-5, 30)
ax1.set_xlim(-4, 2)
ax1.grid(True, alpha=0.25)

fig1.tight_layout()
fig1.savefig(FIGS / 'NR.png', dpi=150)
print("Saved NR.png")

# ── Figure 2: Zoomed view near root ──────────────────────────────
fig2, ax2 = plt.subplots(figsize=(8, 5))

x_zoom = np.linspace(-3.5, -1.5, 400)
ax2.plot(x_zoom, f(x_zoom), color='cyan', lw=2)
ax2.axhline(0, color='white', lw=0.6)

tangent_zoom = f(x0) + df(x0)*(x_zoom - x0)
ax2.plot(x_zoom, tangent_zoom, '--', color='yellow', lw=1.5)

ax2.scatter(x0, f(x0), color='red', zorder=5, s=60)
ax2.scatter(x1, 0, color='lime', zorder=5, s=60)
ax2.plot([x0, x0], [0, f(x0)], '--', color='red', lw=1)

ax2.annotate(r'$x_1 = -\frac{7}{3}$', (x1, 0),
             textcoords='offset points', xytext=(5, 12),
             ha='left', color='lime', fontsize=12, fontweight='bold')

ax2.set_xlabel('x', color='white')
ax2.set_ylabel('f(x)', color='white')
ax2.set_title('Zoomed View: Tangent Intersection', color='white', fontweight='bold')
ax2.grid(True, alpha=0.25)
fig2.tight_layout()
fig2.savefig(FIGS / 'Z.png', dpi=150)
print("Saved Z.png")

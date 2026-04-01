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
x1 = x0 - f(x0)/df(x0)

plt.style.use('dark_background')

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
ax2.set_title('Zoomed Newton-Raphson Step', color='white', fontweight='bold')
ax2.grid(True, alpha=0.25)
fig2.tight_layout()
fig2.savefig(FIGS / 'Z.png', dpi=150)
print("Saved Z.png (zoom_plot)")

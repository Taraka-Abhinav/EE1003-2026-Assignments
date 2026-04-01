import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

FIGS = Path(__file__).parent.parent / 'figs'

def f(x):
    return x**3 - 3*x + 2

plt.style.use('dark_background')

root_neg2 = -2.0
root_1 = 1.0

fig3, ax3 = plt.subplots(figsize=(8, 5))

x_full = np.linspace(-3.5, 2.5, 600)
ax3.plot(x_full, f(x_full), color='cyan', lw=2, label=r'$f(x)=x^3-3x+2$')
ax3.axhline(0, color='white', lw=0.6)
ax3.axvline(0, color='white', lw=0.6)

ax3.scatter([root_neg2, root_1], [0, 0], color='lime', zorder=5, s=70)
ax3.annotate(r'$x=-2$', (root_neg2, 0),
             textcoords='offset points', xytext=(5, 12),
             ha='left', color='lime', fontsize=12, fontweight='bold')
ax3.annotate(r'$x=1$', (root_1, 0),
             textcoords='offset points', xytext=(5, 12),
             ha='left', color='lime', fontsize=12, fontweight='bold')

ax3.set_xlabel('x', color='white')
ax3.set_ylabel('f(x)', color='white')
ax3.set_title(r'Graph of $f(x) = x^3 - 3x + 2$', color='white', fontweight='bold')
ax3.legend(fontsize=10)
ax3.set_ylim(-5, 10)
ax3.grid(True, alpha=0.25)

fig3.tight_layout()
fig3.savefig(FIGS / 'G.png', dpi=150)
print("Saved G.png")

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

true_root = -2.0   # NR from x0=-3 converges to -2

x = -3.0
errors = []
iterations = []

for i in range(8):
    errors.append(abs(x - true_root))
    iterations.append(i)
    if abs(df(x)) < 1e-12:
        break
    x = x - f(x)/df(x)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(iterations, np.log10(errors), 'o-', color='cyan', lw=2, markersize=7)
ax.grid(True, alpha=0.3)
ax.set_xlabel('Iteration', color='white')
ax.set_ylabel(r'$\log_{10}|e_n|$', color='white')
ax.set_title('Quadratic Convergence of Newton-Raphson', color='white', fontweight='bold')

fig.tight_layout()
fig.savefig(FIGS / 'QC.png', dpi=150)
print("Saved QC.png")
print("Errors:", errors)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

FIGS = Path(__file__).parent.parent / 'figs'

def f(z):
    return z**3 - 3*z + 2

def df(z):
    return 3*z**2 - 3

X, Y = np.meshgrid(np.linspace(-3, 3, 600), np.linspace(-3, 3, 600))
Z = X + 1j*Y

for _ in range(40):
    denom = df(Z)
    mask = np.abs(denom) > 1e-10
    Z[mask] = Z[mask] - f(Z[mask]) / denom[mask]

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(np.angle(Z), extent=[-3, 3, -3, 3],
          origin='lower', cmap='hsv', aspect='auto')
ax.set_title(r'Newton Fractal: $f(z)=z^3-3z+2$',
             color='white', fontweight='bold')
ax.set_xlabel('Re(z)', color='white')
ax.set_ylabel('Im(z)', color='white')
fig.tight_layout()
fig.savefig(FIGS / 'NF.png', dpi=150)
print("Saved NF.png")

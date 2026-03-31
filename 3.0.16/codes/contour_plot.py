"""
Contour plot of e^(-x^2 - y^2) in the first quadrant
"""

import numpy as np
import matplotlib.pyplot as plt

# Create mesh grid
x = np.linspace(0, 3, 200)
y = np.linspace(0, 3, 200)
X, Y = np.meshgrid(x, y)

# Gaussian function
Z = np.exp(-X**2 - Y**2)

# Create contour plot
fig, ax = plt.subplots(figsize=(10, 9))

# Filled contour
contourf = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.8)

# Contour lines
contour = ax.contour(X, Y, Z, levels=10, colors='black', alpha=0.3, linewidths=0.5)
ax.clabel(contour, inline=True, fontsize=8)

# Add circular level curves annotations
theta = np.linspace(0, np.pi/2, 100)
for r in [0.5, 1.0, 1.5]:
    x_circle = r * np.cos(theta)
    y_circle = r * np.sin(theta)
    ax.plot(x_circle, y_circle, 'r--', linewidth=1.5, alpha=0.6)

# Labels and title
ax.set_xlabel('x', fontsize=14, fontweight='bold')
ax.set_ylabel('y', fontsize=14, fontweight='bold')
ax.set_title(r'Contour Plot: $e^{-x^2-y^2}$ (First Quadrant)',
             fontsize=16, fontweight='bold')

# Colorbar
cbar = plt.colorbar(contourf, ax=ax)
cbar.set_label(r'$e^{-x^2-y^2}$', fontsize=12, fontweight='bold')

# Grid
ax.grid(True, alpha=0.3, linestyle='--')

# Aspect ratio
ax.set_aspect('equal')

# Add annotation
ax.text(0.98, 0.98, r'Integral = $\frac{\pi}{4}$',
        transform=ax.transAxes, fontsize=13,
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
        verticalalignment='top', horizontalalignment='right',
        fontweight='bold')

plt.tight_layout()
plt.savefig('../figs/contour_plot.png', dpi=300, bbox_inches='tight')
print("Contour plot saved to ../figs/contour_plot.png")

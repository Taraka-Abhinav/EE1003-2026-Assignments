"""
3D Surface plot of the Gaussian function e^(-x^2 - y^2)
Shows the surface over the first quadrant
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create mesh grid
x = np.linspace(0, 3, 100)
y = np.linspace(0, 3, 100)
X, Y = np.meshgrid(x, y)

# Gaussian function
Z = np.exp(-X**2 - Y**2)

# Create 3D plot
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8,
                       linewidth=0, antialiased=True, edgecolor='none')

# Add contour lines at the bottom
ax.contour(X, Y, Z, zdir='z', offset=0, cmap='viridis', alpha=0.5, levels=10)

# Labels and title
ax.set_xlabel('x', fontsize=12, fontweight='bold')
ax.set_ylabel('y', fontsize=12, fontweight='bold')
ax.set_zlabel(r'$e^{-x^2-y^2}$', fontsize=12, fontweight='bold')
ax.set_title(r'Surface: $z = e^{-x^2-y^2}$ (First Quadrant)',
             fontsize=14, fontweight='bold', pad=20)

# Add colorbar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Add annotation for the integral value
ax.text2D(0.05, 0.95, r'Volume = $\frac{\pi}{4} \approx 0.7854$',
          transform=ax.transAxes, fontsize=13,
          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
          verticalalignment='top', fontweight='bold')

# View angle
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('../figs/surface_plot.png', dpi=300, bbox_inches='tight')
print("Surface plot saved to ../figs/surface_plot.png")
print(f"Theoretical value: π/4 = {np.pi/4:.6f}")

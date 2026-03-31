"""
Method 2: Separation of Variables Visualization
Shows the product of two 1D Gaussian functions
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure with subplots
fig = plt.figure(figsize=(16, 5))

# Subplot 1: 1D Gaussian in x
ax1 = fig.add_subplot(131)
x = np.linspace(0, 4, 200)
fx = np.exp(-x**2)

ax1.fill_between(x, fx, alpha=0.5, color='blue', label=r'$e^{-x^2}$')
ax1.plot(x, fx, 'b-', linewidth=2)
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.set_xlabel('x', fontsize=12, fontweight='bold')
ax1.set_ylabel(r'$e^{-x^2}$', fontsize=12, fontweight='bold')
ax1.set_title(r'1D Gaussian: $f(x) = e^{-x^2}$' + '\n' +
              r'$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$',
              fontsize=11, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=10)

# Subplot 2: 1D Gaussian in y
ax2 = fig.add_subplot(132)
y = np.linspace(0, 4, 200)
fy = np.exp(-y**2)

ax2.fill_between(y, fy, alpha=0.5, color='red', label=r'$e^{-y^2}$')
ax2.plot(y, fy, 'r-', linewidth=2)
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.set_xlabel('y', fontsize=12, fontweight='bold')
ax2.set_ylabel(r'$e^{-y^2}$', fontsize=12, fontweight='bold')
ax2.set_title(r'1D Gaussian: $g(y) = e^{-y^2}$' + '\n' +
              r'$\int_0^\infty e^{-y^2} dy = \frac{\sqrt{\pi}}{2}$',
              fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=10)

# Subplot 3: 2D product
ax3 = fig.add_subplot(133, projection='3d')
x_3d = np.linspace(0, 3, 60)
y_3d = np.linspace(0, 3, 60)
X, Y = np.meshgrid(x_3d, y_3d)
Z = np.exp(-X**2) * np.exp(-Y**2)

surf = ax3.plot_surface(X, Y, Z, cmap='plasma', alpha=0.9,
                       linewidth=0, antialiased=True)

ax3.set_xlabel('x', fontsize=10, fontweight='bold')
ax3.set_ylabel('y', fontsize=10, fontweight='bold')
ax3.set_zlabel(r'$e^{-x^2-y^2}$', fontsize=10, fontweight='bold')
ax3.set_title(r'2D Product: $e^{-x^2} \cdot e^{-y^2}$' + '\n' +
              r'$= e^{-x^2-y^2}$',
              fontsize=11, fontweight='bold', pad=15)
ax3.view_init(elev=25, azim=45)

plt.suptitle(r'Method 2: Separation of Variables - $e^{-x^2-y^2} = e^{-x^2} \times e^{-y^2}$',
             fontsize=15, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('../figs/separation_variables.png', dpi=300, bbox_inches='tight')
print("Separation of variables plot saved to ../figs/separation_variables.png")

# Calculate and print the result
integral_1d = np.sqrt(np.pi) / 2
result = integral_1d ** 2

print("\nMethod 2 - Separation of Variables:")
print(f"∫₀^∞ e^(-x²) dx = √π/2 = {integral_1d:.6f}")
print(f"∫₀^∞ e^(-y²) dy = √π/2 = {integral_1d:.6f}")
print(f"Result: (√π/2)² = π/4 = {result:.6f}")

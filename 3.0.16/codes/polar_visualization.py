"""
Method 1: Polar Coordinates Visualization
Shows the transformation from Cartesian to polar coordinates
"""

import numpy as np
import matplotlib.pyplot as plt

# Create figure with subplots
fig = plt.figure(figsize=(16, 6))

# Subplot 1: Cartesian grid
ax1 = fig.add_subplot(131)
x = np.linspace(0, 3, 50)
y = np.linspace(0, 3, 50)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2)

contourf1 = ax1.contourf(X, Y, Z, levels=15, cmap='coolwarm', alpha=0.7)
ax1.set_xlabel('x', fontsize=12, fontweight='bold')
ax1.set_ylabel('y', fontsize=12, fontweight='bold')
ax1.set_title('Cartesian Coordinates\n' + r'$\int_0^\infty \int_0^\infty e^{-x^2-y^2} dx\,dy$',
              fontsize=11, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_aspect('equal')

# Subplot 2: Polar grid overlay
ax2 = fig.add_subplot(132)
contourf2 = ax2.contourf(X, Y, Z, levels=15, cmap='coolwarm', alpha=0.7)

# Draw polar grid
theta_lines = np.linspace(0, np.pi/2, 7)
r_max = 3
for theta in theta_lines:
    r_vals = np.linspace(0, r_max, 100)
    x_line = r_vals * np.cos(theta)
    y_line = r_vals * np.sin(theta)
    ax2.plot(x_line, y_line, 'k-', linewidth=1.5, alpha=0.6)

r_circles = np.linspace(0.5, 3, 6)
theta_vals = np.linspace(0, np.pi/2, 100)
for r in r_circles:
    x_circle = r * np.cos(theta_vals)
    y_circle = r * np.sin(theta_vals)
    ax2.plot(x_circle, y_circle, 'k-', linewidth=1.5, alpha=0.6)

ax2.set_xlabel('x = r cos θ', fontsize=12, fontweight='bold')
ax2.set_ylabel('y = r sin θ', fontsize=12, fontweight='bold')
ax2.set_title('Polar Grid Overlay\n' + r'$x^2 + y^2 = r^2$',
              fontsize=11, fontweight='bold')
ax2.set_aspect('equal')

# Subplot 3: Polar function
ax3 = fig.add_subplot(133, projection='polar')
theta = np.linspace(0, np.pi/2, 100)
r = np.linspace(0, 3, 100)
R, THETA = np.meshgrid(r, theta)

# Function in polar coordinates
Z_polar = np.exp(-R**2)

contourf3 = ax3.contourf(THETA, R, Z_polar, levels=15, cmap='coolwarm', alpha=0.7)
ax3.set_theta_zero_location('E')
ax3.set_theta_direction(1)
ax3.set_thetamin(0)
ax3.set_thetamax(90)
ax3.set_title('Polar Coordinates\n' + r'$\int_0^{\pi/2} \int_0^\infty e^{-r^2} r\,dr\,d\theta$',
              fontsize=11, fontweight='bold', pad=20)

plt.suptitle('Method 1: Polar Coordinates Transformation',
             fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('../figs/polar_visualization.png', dpi=300, bbox_inches='tight')
print("Polar visualization saved to ../figs/polar_visualization.png")

# Calculate and print the result
print("\nMethod 1 - Polar Coordinates:")
print("Angular integral: ∫₀^(π/2) dθ = π/2")
print("Radial integral: ∫₀^∞ r·e^(-r²) dr = 1/2")
print(f"Result: (π/2) × (1/2) = π/4 = {np.pi/4:.6f}")

"""
Method 3: Error Function Approach
Visualizes the error function and its convergence
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

# Create figure with subplots
fig = plt.figure(figsize=(16, 5))

# Subplot 1: Error function
ax1 = fig.add_subplot(131)
x = np.linspace(0, 4, 200)
y_erf = erf(x)

ax1.plot(x, y_erf, 'b-', linewidth=2.5, label='erf(x)')
ax1.axhline(y=1, color='r', linestyle='--', linewidth=2, label='Limit = 1')
ax1.fill_between(x, y_erf, alpha=0.3, color='blue')
ax1.set_xlabel('x', fontsize=12, fontweight='bold')
ax1.set_ylabel('erf(x)', fontsize=12, fontweight='bold')
ax1.set_title(r'Error Function: $\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt$',
              fontsize=11, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)
ax1.set_ylim([0, 1.1])

# Add annotation
ax1.annotate(r'$\lim_{x \to \infty} \mathrm{erf}(x) = 1$',
             xy=(3, 0.995), xytext=(2, 0.7),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=11, color='red', fontweight='bold')

# Subplot 2: Integral convergence
ax2 = fig.add_subplot(132)
x_vals = np.linspace(0.1, 5, 50)
integral_vals = []

for x_max in x_vals:
    # Numerical integration using trapezoidal rule
    x_int = np.linspace(0, x_max, 1000)
    y_int = np.exp(-x_int**2)
    integral = np.trapezoid(y_int, x_int)
    integral_vals.append(integral)

integral_vals = np.array(integral_vals)
theoretical = np.sqrt(np.pi) / 2

ax2.plot(x_vals, integral_vals, 'g-', linewidth=2.5, label=r'$\int_0^L e^{-x^2} dx$')
ax2.axhline(y=theoretical, color='r', linestyle='--', linewidth=2,
            label=r'$\frac{\sqrt{\pi}}{2}$')
ax2.fill_between(x_vals, integral_vals, theoretical, alpha=0.3, color='green')
ax2.set_xlabel('Upper limit L', fontsize=12, fontweight='bold')
ax2.set_ylabel('Integral value', fontsize=12, fontweight='bold')
ax2.set_title(r'Convergence: $\int_0^L e^{-x^2} dx \to \frac{\sqrt{\pi}}{2}$',
              fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=11)

# Subplot 3: 2D integral convergence
ax3 = fig.add_subplot(133)
L_vals = np.linspace(1, 8, 30)
integral_2d_vals = []

for L in L_vals:
    # 2D numerical integration
    x = np.linspace(0, L, 100)
    y = np.linspace(0, L, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-X**2 - Y**2)

    # Use trapezoidal rule for 2D
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    integral_2d = np.sum(Z) * dx * dy
    integral_2d_vals.append(integral_2d)

integral_2d_vals = np.array(integral_2d_vals)
theoretical_2d = np.pi / 4

ax3.plot(L_vals, integral_2d_vals, 'm-', linewidth=2.5,
         label=r'$\int_0^L \int_0^L e^{-x^2-y^2} dx\,dy$')
ax3.axhline(y=theoretical_2d, color='r', linestyle='--', linewidth=2,
            label=r'$\frac{\pi}{4}$')
ax3.fill_between(L_vals, integral_2d_vals, theoretical_2d, alpha=0.3, color='magenta')
ax3.set_xlabel('Upper limit L', fontsize=12, fontweight='bold')
ax3.set_ylabel('Integral value', fontsize=12, fontweight='bold')
ax3.set_title(r'2D Convergence $\to \frac{\pi}{4}$',
              fontsize=11, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.legend(fontsize=11)

plt.suptitle('Method 3: Error Function Approach and Convergence Analysis',
             fontsize=15, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('../figs/error_function.png', dpi=300, bbox_inches='tight')
print("Error function plot saved to ../figs/error_function.png")

# Calculate and print the result
print("\nMethod 3 - Error Function Approach:")
print(f"∫₀^∞ e^(-x²) dx = √π/2 · lim(x→∞) erf(x) = √π/2 · 1 = {np.sqrt(np.pi)/2:.6f}")
print(f"∫₀^∞ e^(-y²) dy = √π/2 · lim(y→∞) erf(y) = √π/2 · 1 = {np.sqrt(np.pi)/2:.6f}")
print(f"Result: (√π/2)² = π/4 = {np.pi/4:.6f}")

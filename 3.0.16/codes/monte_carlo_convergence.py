"""
Method 4: Monte Carlo Numerical Integration
Estimates the integral using random sampling
"""

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Monte Carlo simulation
def monte_carlo_integration(N, L=10):
    """
    Estimate the integral using Monte Carlo method
    N: number of random samples
    L: upper limit for x and y (should be large)
    """
    # Generate random points in [0, L] x [0, L]
    x_rand = np.random.uniform(0, L, N)
    y_rand = np.random.uniform(0, L, N)

    # Evaluate function at random points
    f_vals = np.exp(-x_rand**2 - y_rand**2)

    # Monte Carlo estimate
    estimate = L * L * np.mean(f_vals)

    return estimate

# Create figure with subplots
fig = plt.figure(figsize=(16, 5))

# Subplot 1: Convergence with number of samples
ax1 = fig.add_subplot(131)
N_values = np.logspace(2, 6, 50).astype(int)
estimates = []
std_devs = []

for N in N_values:
    # Run multiple trials
    trials = [monte_carlo_integration(N, L=8) for _ in range(10)]
    estimates.append(np.mean(trials))
    std_devs.append(np.std(trials))

estimates = np.array(estimates)
std_devs = np.array(std_devs)
theoretical = np.pi / 4

ax1.semilogx(N_values, estimates, 'b-', linewidth=2, label='Monte Carlo estimate')
ax1.fill_between(N_values, estimates - std_devs, estimates + std_devs,
                 alpha=0.3, color='blue', label='±1 std dev')
ax1.axhline(y=theoretical, color='r', linestyle='--', linewidth=2,
            label=r'True value: $\frac{\pi}{4}$')
ax1.set_xlabel('Number of samples (N)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Integral estimate', fontsize=12, fontweight='bold')
ax1.set_title('Convergence vs Sample Size',
              fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3, which='both')
ax1.legend(fontsize=10)

# Subplot 2: Sample distribution visualization
ax2 = fig.add_subplot(132)
N_vis = 2000
L_vis = 5
x_samples = np.random.uniform(0, L_vis, N_vis)
y_samples = np.random.uniform(0, L_vis, N_vis)
f_samples = np.exp(-x_samples**2 - y_samples**2)

# Create heatmap
x_grid = np.linspace(0, L_vis, 100)
y_grid = np.linspace(0, L_vis, 100)
X, Y = np.meshgrid(x_grid, y_grid)
Z = np.exp(-X**2 - Y**2)

ax2.contourf(X, Y, Z, levels=15, cmap='YlOrRd', alpha=0.6)
scatter = ax2.scatter(x_samples[:500], y_samples[:500], c=f_samples[:500],
                     cmap='viridis', s=20, alpha=0.6, edgecolors='black', linewidth=0.5)
ax2.set_xlabel('x', fontsize=12, fontweight='bold')
ax2.set_ylabel('y', fontsize=12, fontweight='bold')
ax2.set_title('Random Sample Points\n(first 500 shown)',
              fontsize=12, fontweight='bold')
ax2.set_aspect('equal')
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label(r'$e^{-x^2-y^2}$', fontsize=10, fontweight='bold')

# Subplot 3: Error analysis
ax3 = fig.add_subplot(133)
N_error = np.logspace(2, 6, 40).astype(int)
errors = []
theoretical_error = []

for N in N_error:
    trials = [monte_carlo_integration(N, L=8) for _ in range(20)]
    error = np.std(trials)
    errors.append(error)
    # Theoretical error scales as 1/sqrt(N)
    theoretical_error.append(0.2 / np.sqrt(N))

ax3.loglog(N_error, errors, 'go-', linewidth=2, markersize=6,
           label='Observed error (std dev)')
ax3.loglog(N_error, theoretical_error, 'r--', linewidth=2,
           label=r'Theoretical: $\propto 1/\sqrt{N}$')
ax3.set_xlabel('Number of samples (N)', fontsize=12, fontweight='bold')
ax3.set_ylabel('Standard deviation', fontsize=12, fontweight='bold')
ax3.set_title('Error Scaling: ' + r'$\sigma \propto N^{-1/2}$',
              fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3, which='both')
ax3.legend(fontsize=10)

plt.suptitle('Method 4: Monte Carlo Numerical Integration',
             fontsize=15, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('../figs/monte_carlo_convergence.png', dpi=300, bbox_inches='tight')
print("Monte Carlo convergence plot saved to ../figs/monte_carlo_convergence.png")

# Final estimate with large N
N_final = 1000000
estimate_final = monte_carlo_integration(N_final, L=10)

print("\nMethod 4 - Monte Carlo Integration:")
print(f"Number of samples: {N_final:,}")
print(f"Monte Carlo estimate: {estimate_final:.6f}")
print(f"True value: π/4 = {np.pi/4:.6f}")
print(f"Absolute error: {abs(estimate_final - np.pi/4):.6f}")
print(f"Relative error: {abs(estimate_final - np.pi/4) / (np.pi/4) * 100:.3f}%")

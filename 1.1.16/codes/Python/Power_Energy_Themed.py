import numpy as np
import matplotlib.pyplot as plt

# Parameters
t = np.linspace(0, 0.2, 1000)
V = 5
tau = 0.04
C = 4e-6

# Equations
Vc = V * (1 - np.exp(-t/tau))
ic = (V / 10000) * np.exp(-t/tau)

power_mW = (Vc * ic) * 1000 
energy_uJ = (0.5 * C * Vc**2) * 1e6 

# Theme
bg = '#0b1220'
power_color = '#8fd3d1'
energy_color = '#f5e6a8'

# Plot
fig, ax1 = plt.subplots(figsize=(8,5))
fig.patch.set_facecolor(bg)
ax1.set_facecolor(bg)

ax1.plot(t*1000, power_mW, color=power_color, linewidth=2)
ax2 = ax1.twinx()
ax2.plot(t*1000, energy_uJ, color=energy_color, linewidth=2, linestyle='--')

ax1.grid(True, linestyle='--', color='white', alpha=0.15)

plt.tight_layout()
plt.savefig("Power_Energy.png", dpi=300, facecolor=bg)
plt.show()

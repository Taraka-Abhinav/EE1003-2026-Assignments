import numpy as np
import matplotlib.pyplot as plt

# Parameters
t = np.linspace(0, 0.2, 1000)
V = 5
tau = 0.04

# State variables
Vc = V * (1 - np.exp(-t/tau))
dVc_dt = (V / tau) * np.exp(-t/tau)

# Theme
bg = '#0b1220'
curve = '#8fd3d1'
accent = '#f5e6a8'

# Plot
fig, ax = plt.subplots(figsize=(7,6))
fig.patch.set_facecolor(bg)
ax.set_facecolor(bg)

ax.plot(Vc, dVc_dt, color=curve, linewidth=2.5)
ax.fill_between(Vc, dVc_dt, color=curve, alpha=0.12)

ax.scatter([0], [125], color=accent, s=70)
ax.scatter([5], [0], color=accent, s=70)

ax.grid(True, linestyle='--', color='white', alpha=0.15)

plt.tight_layout()
plt.savefig("Phase_Portrait.png", dpi=300, facecolor=bg)
plt.show()

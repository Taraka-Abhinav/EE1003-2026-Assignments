"""
============================================================
  RC Circuit Transient Response Plotter
  Problem 1.1.16 | EC 2007
  
  Circuit:  10V source -- 20kΩ -- [20kΩ || 4µF]
  
  Results:
    Vc(t) = 5 (1 - e^{-25t})  V
    ic(t) = 0.50 e^{-25t}     mA
============================================================
"""

# ── STEP 1 : Import libraries ─────────────────────────────
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyArrowPatch
from matplotlib.ticker import AutoMinorLocator

# ── STEP 2 : Define circuit parameters ───────────────────
Vs   = 10          # Source voltage  (V)
R1   = 20e3        # Series resistor (Ω)
R2   = 20e3        # Shunt  resistor (Ω)
C    = 4e-6        # Capacitor       (F)

Rth  = (R1 * R2) / (R1 + R2)          # Thévenin resistance = 10 kΩ
Vinf = Vs * R2 / (R1 + R2)            # Steady-state voltage = 5 V
tau  = Rth * C                         # Time constant = 40 ms
Vc0  = 0                               # Initial capacitor voltage

print("=" * 48)
print("  RC Circuit — Computed Parameters")
print("=" * 48)
print(f"  Thévenin Resistance  R_th = {Rth/1e3:.1f} kΩ")
print(f"  Steady-State Voltage V∞   = {Vinf:.1f} V")
print(f"  Time Constant        τ    = {tau*1e3:.1f} ms")
print(f"  Decay exponent       1/τ  = {1/tau:.1f} s⁻¹")
print("=" * 48)

# ── STEP 3 : Generate time vector ────────────────────────
#    Plot for 5 time constants (captures ~99% of transient)
t_end = 5 * tau
t = np.linspace(0, t_end, 2000)

# ── STEP 4 : Compute Vc(t) and ic(t) ────────────────────
Vc = Vinf + (Vc0 - Vinf) * np.exp(-t / tau)   # V
ic = C * np.gradient(Vc, t) * 1e3              # mA  (numerical differentiation)
ic_exact = (Vinf / Rth) * np.exp(-t / tau) * 1e3  # mA  (analytical)

# ── STEP 5 : Set up the figure ───────────────────────────
plt.style.use('dark_background')

fig = plt.figure(figsize=(14, 9), facecolor='#0d1117')
fig.suptitle(
    "RC Circuit Transient Response  —  Problem 1.1.16 (EC 2007)",
    fontsize=16, fontweight='bold', color='white',
    y=0.97
)

gs = gridspec.GridSpec(
    2, 2,
    figure=fig,
    hspace=0.45, wspace=0.38,
    left=0.08, right=0.96,
    top=0.90, bottom=0.08
)

AX_COLOR   = '#161b22'
GRID_COLOR = '#30363d'
BLUE       = '#58a6ff'
ORANGE     = '#f78166'
GREEN      = '#3fb950'
GOLD       = '#d29922'
WHITE      = '#e6edf3'
TICK_COLOR = '#8b949e'

def style_ax(ax, title):
    ax.set_facecolor(AX_COLOR)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID_COLOR)
    ax.tick_params(colors=TICK_COLOR, labelsize=9)
    ax.xaxis.label.set_color(WHITE)
    ax.yaxis.label.set_color(WHITE)
    ax.set_title(title, color=WHITE, fontsize=11, fontweight='bold', pad=8)
    ax.grid(which='major', color=GRID_COLOR, linewidth=0.8, linestyle='--')
    ax.grid(which='minor', color=GRID_COLOR, linewidth=0.3, linestyle=':')
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))

t_ms = t * 1e3   # time in milliseconds for x-axis

# ─────────────────────────────────────────────────────────
#  PLOT 1 : Vc(t)
# ─────────────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, 0])
style_ax(ax1, "Capacitor Voltage  $V_C(t)$")

ax1.plot(t_ms, Vc, color=BLUE, linewidth=2.2, label=r'$V_C(t) = 5(1-e^{-25t})\ \mathrm{V}$')

# Asymptote line
ax1.axhline(Vinf, color=GOLD, linewidth=1.2, linestyle='--', alpha=0.7,
            label=f'$V_{{\\infty}} = {Vinf:.0f}$ V  (steady state)')

# Tau marker (63.2%)
Vc_tau = Vinf * (1 - np.exp(-1))
ax1.plot(tau * 1e3, Vc_tau, 'o', color=GREEN, markersize=8, zorder=5)
ax1.annotate(
    f'  $\\tau$ = {tau*1e3:.0f} ms\n  $V_C = {Vc_tau:.2f}$ V  (63.2%)',
    xy=(tau * 1e3, Vc_tau),
    xytext=(tau * 1e3 + 15, Vc_tau - 0.8),
    color=GREEN, fontsize=8.5,
    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2)
)

# 5-tau marker
ax1.plot(5 * tau * 1e3, Vc[-1], 's', color=ORANGE, markersize=7, zorder=5)
ax1.annotate(
    f'  $5\\tau$: $V_C \\approx {Vc[-1]:.2f}$ V\n  (99.3% charged)',
    xy=(5 * tau * 1e3, Vc[-1]),
    xytext=(5 * tau * 1e3 - 60, Vc[-1] - 1.2),
    color=ORANGE, fontsize=8.5,
    arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.2)
)

ax1.set_xlabel("Time  (ms)")
ax1.set_ylabel("$V_C$  (V)")
ax1.set_xlim(0, t_end * 1e3)
ax1.set_ylim(-0.3, 6.0)
ax1.legend(fontsize=8.5, facecolor='#161b22', edgecolor=GRID_COLOR,
           labelcolor=WHITE, loc='lower right')

# ─────────────────────────────────────────────────────────
#  PLOT 2 : ic(t)
# ─────────────────────────────────────────────────────────
ax2 = fig.add_subplot(gs[0, 1])
style_ax(ax2, "Capacitor Current  $i_c(t)$")

ax2.plot(t_ms, ic_exact, color=ORANGE, linewidth=2.2,
         label=r'$i_c(t) = 0.50\,e^{-25t}\ \mathrm{mA}$')

# Initial current marker
ax2.plot(0, ic_exact[0], 'o', color=GREEN, markersize=8, zorder=5)
ax2.annotate(
    f'  $i_c(0^+) = {ic_exact[0]:.2f}$ mA\n  (capacitor = short ckt)',
    xy=(0, ic_exact[0]),
    xytext=(25, ic_exact[0] - 0.08),
    color=GREEN, fontsize=8.5,
    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2)
)

# Tau marker
ic_tau = ic_exact[0] * np.exp(-1)
ax2.plot(tau * 1e3, ic_tau, 'o', color=BLUE, markersize=8, zorder=5)
ax2.annotate(
    f'  $i_c(\\tau) = {ic_tau:.4f}$ mA\n  (36.8%)',
    xy=(tau * 1e3, ic_tau),
    xytext=(tau * 1e3 + 12, ic_tau + 0.04),
    color=BLUE, fontsize=8.5,
    arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.2)
)

ax2.axhline(0, color=GOLD, linewidth=1.0, linestyle='--', alpha=0.6,
            label='$i_c(\\infty) = 0$ mA')

ax2.set_xlabel("Time  (ms)")
ax2.set_ylabel("$i_c$  (mA)")
ax2.set_xlim(0, t_end * 1e3)
ax2.set_ylim(-0.03, 0.58)
ax2.legend(fontsize=8.5, facecolor='#161b22', edgecolor=GRID_COLOR,
           labelcolor=WHITE, loc='upper right')

# ─────────────────────────────────────────────────────────
#  PLOT 3 : Both on same axes (overlay)
# ─────────────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[1, 0])
style_ax(ax3, "Overlay: $V_C(t)$ and $i_c(t)$")

color_Vc = BLUE
color_ic = ORANGE

lns1, = ax3.plot(t_ms, Vc, color=color_Vc, linewidth=2.2,
                 label=r'$V_C(t)$  [V]')
ax3.set_ylabel("$V_C$  (V)", color=color_Vc)
ax3.tick_params(axis='y', labelcolor=color_Vc)
ax3.set_xlabel("Time  (ms)")

ax3b = ax3.twinx()
ax3b.set_facecolor(AX_COLOR)
lns2, = ax3b.plot(t_ms, ic_exact, color=color_ic, linewidth=2.2,
                  linestyle='--', label=r'$i_c(t)$  [mA]')
ax3b.set_ylabel("$i_c$  (mA)", color=color_ic)
ax3b.tick_params(axis='y', labelcolor=color_ic)
for spine in ax3b.spines.values():
    spine.set_edgecolor(GRID_COLOR)

lines = [lns1, lns2]
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, fontsize=8.5, facecolor='#161b22',
           edgecolor=GRID_COLOR, labelcolor=WHITE, loc='center right')
ax3.set_xlim(0, t_end * 1e3)

# ─────────────────────────────────────────────────────────
#  PLOT 4 : Info panel — Circuit parameters summary
# ─────────────────────────────────────────────────────────
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor(AX_COLOR)
for spine in ax4.spines.values():
    spine.set_edgecolor(GRID_COLOR)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_title("Circuit Summary", color=WHITE, fontsize=11,
              fontweight='bold', pad=8)

info_lines = [
    ("Circuit",          "10V  —  20kΩ  —  [20kΩ ∥ 4µF]"),
    ("",                 ""),
    ("Initial Voltage",  "$V_C(0^+) = 0$ V"),
    ("Thévenin Voltage", "$V_{th} = 5$ V"),
    ("Thévenin Resist.", "$R_{th} = 10$ kΩ"),
    ("Time Constant",    "$\\tau = 40$ ms"),
    ("Decay Exponent",   "$1/\\tau = 25$ s⁻¹"),
    ("",                 ""),
    ("Capacitor Voltage","$V_C(t) = 5(1-e^{-25t})$ V"),
    ("Capacitor Current","$i_c(t) = 0.50\\,e^{-25t}$ mA"),
    ("",                 ""),
    ("Answer",           "Option (a)   ✔"),
]

y_pos = 0.95
for label, val in info_lines:
    if label == "":
        y_pos -= 0.04
        continue
    if label == "Answer":
        ax4.text(0.04, y_pos, f"{label}:", color=GREEN,
                 fontsize=9.5, fontweight='bold', transform=ax4.transAxes, va='top')
        ax4.text(0.42, y_pos, val, color=GREEN,
                 fontsize=9.5, fontweight='bold', transform=ax4.transAxes, va='top')
    elif label in ("Capacitor Voltage", "Capacitor Current"):
        ax4.text(0.04, y_pos, f"{label}:", color=GOLD,
                 fontsize=9, transform=ax4.transAxes, va='top')
        ax4.text(0.42, y_pos, val, color=GOLD,
                 fontsize=9, transform=ax4.transAxes, va='top')
    else:
        ax4.text(0.04, y_pos, f"{label}:", color=TICK_COLOR,
                 fontsize=9, transform=ax4.transAxes, va='top')
        ax4.text(0.42, y_pos, val, color=WHITE,
                 fontsize=9, transform=ax4.transAxes, va='top')
    y_pos -= 0.075

# ── STEP 6 : Save and show ────────────────────────────────
plt.savefig("rc_response.png", dpi=180, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print("\n  Plot saved as  rc_response.png")
plt.show()

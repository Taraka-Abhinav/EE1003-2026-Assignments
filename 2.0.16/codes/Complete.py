import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# DATA SETUP & ANALYSIS
# ==========================================
# Job Data definitions (Processing Time p, Due Date d)
jobs = {
    'P': {'p': 2, 'd': 5},
    'Q': {'p': 10, 'd': 6},
    'R': {'p': 3, 'd': 3},
    'S': {'p': 4, 'd': 7}
}

# Sequences to compare
seq_edd = ['R', 'P', 'Q', 'S']  # Earliest Due Date (Optimal for L_max)
seq_spt = ['P', 'R', 'S', 'Q']  # Shortest Processing Time
seq_lst = ['Q', 'R', 'S', 'P']  # Least Slack Time (Slack = d - p)

def analyze_sequence(seq):
    current_time = 0
    gantt = []
    abs_lateness = {}
    actual_lateness = {}
    cumulative_times = [0]

    for job in seq:
        p = jobs[job]['p']
        d = jobs[job]['d']
        start = current_time
        current_time += p

        gantt.append((job, start, p, d))
        abs_lateness[job] = abs(current_time - d)
        actual_lateness[job] = current_time - d  # Positive = Late, Negative = Early
        cumulative_times.append(current_time)

    return gantt, abs_lateness, actual_lateness, cumulative_times

# Process all sequences
gantt_edd, abs_lat_edd, act_lat_edd, cum_edd = analyze_sequence(seq_edd)
gantt_spt, abs_lat_spt, act_lat_spt, cum_spt = analyze_sequence(seq_spt)
gantt_lst, abs_lat_lst, act_lat_lst, cum_lst = analyze_sequence(seq_lst)

# Consistent color palette for jobs
colors = {'P': '#2ca02c', 'Q': '#d62728', 'R': '#1f77b4', 'S': '#ff7f0e'}

# ==========================================
# PLOT 1: Comprehensive Gantt Chart
# ==========================================
fig1, ax1 = plt.subplots(figsize=(12, 8))

def draw_gantt_row(ax, gantt_data, y_base, title):
    for job, start, p, d in gantt_data:
        # Draw block
        ax.broken_barh([(start, p)], (y_base, 6), facecolors=colors[job], edgecolor='black', alpha=0.8)
        ax.text(start + p/2, y_base + 3, f"{job}\n(p={p})", ha='center', va='center', color='white', fontweight='bold')

        # Draw Due Date marker
        ax.plot([d, d], [y_base + 6.5, y_base + 8], color='black', linestyle=':', linewidth=2)
        ax.text(d, y_base + 8.2, f"{job} due", ha='center', va='bottom', fontsize=8, color='black', style='italic')

# Draw the three schedules
draw_gantt_row(ax1, gantt_lst, 5, 'LST Schedule')
draw_gantt_row(ax1, gantt_spt, 20, 'SPT Schedule')
draw_gantt_row(ax1, gantt_edd, 35, 'EDD Schedule')

ax1.set_ylim(0, 50)
ax1.set_xlim(0, 21)
ax1.set_xlabel('Timeline (t)', fontweight='bold', fontsize=12)
ax1.set_yticks([8, 23, 38])
ax1.set_yticklabels(['LST Schedule\n(Max Dev: 14)', 'SPT Schedule\n(Max Dev: 13)', 'EDD Schedule\n(Max Dev: 12)'], fontweight='bold', fontsize=11)
ax1.set_title('Plot 1: 3-Way Gantt Chart Comparison with Due Dates', fontweight='bold', pad=20, fontsize=14)
ax1.set_xticks(range(0, 21, 1))
ax1.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('plot_1_comprehensive_gantt.png', dpi=300)

# ==========================================
# PLOT 2: Absolute Deviation Bar Chart
# ==========================================
fig2, ax2 = plt.subplots(figsize=(10, 6))

job_labels = ['P', 'Q', 'R', 'S']
x = np.arange(len(job_labels))
width = 0.25

edd_vals = [abs_lat_edd[j] for j in job_labels]
spt_vals = [abs_lat_spt[j] for j in job_labels]
lst_vals = [abs_lat_lst[j] for j in job_labels]

rects1 = ax2.bar(x - width, edd_vals, width, label='EDD', color='#1f77b4', edgecolor='black', alpha=0.9)
rects2 = ax2.bar(x, spt_vals, width, label='SPT', color='#ff7f0e', edgecolor='black', alpha=0.9)
rects3 = ax2.bar(x + width, lst_vals, width, label='LST', color='#2ca02c', edgecolor='black', alpha=0.9)

ax2.set_ylabel('Absolute Deviation |C_i - d_i|', fontweight='bold', fontsize=11)
ax2.set_title('Plot 2: Absolute Deviation by Heuristic', fontweight='bold', pad=15, fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(job_labels, fontweight='bold', fontsize=12)
ax2.legend()

ax2.bar_label(rects1, padding=3)
ax2.bar_label(rects2, padding=3)
ax2.bar_label(rects3, padding=3)

# Add line for max deviations
ax2.axhline(y=12, color='#1f77b4', linestyle=':', alpha=0.8)
ax2.text(-0.5, 12.2, 'Optimal Max (12)', color='#1f77b4', fontweight='bold', fontsize=9)

ax2.set_ylim(0, 16)
plt.tight_layout()
plt.savefig('plot_2_absolute_deviation.png', dpi=300)

# ==========================================
# PLOT 3: Actual Lateness (Early vs Late)
# ==========================================
fig3, ax3 = plt.subplots(figsize=(10, 6))

act_edd_vals = [act_lat_edd[j] for j in job_labels]
act_spt_vals = [act_lat_spt[j] for j in job_labels]
act_lst_vals = [act_lat_lst[j] for j in job_labels]

ax3.bar(x - width, act_edd_vals, width, label='EDD', color='#1f77b4', edgecolor='black')
ax3.bar(x, act_spt_vals, width, label='SPT', color='#ff7f0e', edgecolor='black')
ax3.bar(x + width, act_lst_vals, width, label='LST', color='#2ca02c', edgecolor='black')

ax3.axhline(0, color='black', linewidth=1.5)
ax3.set_ylabel('Actual Lateness (C_i - d_i)', fontweight='bold')
ax3.set_title('Plot 3: Early vs. Late Jobs (Negative = Early, Positive = Late)', fontweight='bold', fontsize=14)
ax3.set_xticks(x)
ax3.set_xticklabels(job_labels, fontweight='bold')
ax3.legend()

plt.tight_layout()
plt.savefig('plot_3_actual_lateness.png', dpi=300)

# ==========================================
# PLOT 4: Completion Time Trajectory
# ==========================================
fig4, ax4 = plt.subplots(figsize=(8, 5))
steps = [0, 1, 2, 3, 4]

ax4.step(steps, cum_edd, label=f'EDD ({",".join(seq_edd)})', marker='o', color='#1f77b4', where='post')
ax4.step(steps, cum_spt, label=f'SPT ({",".join(seq_spt)})', marker='s', color='#ff7f0e', where='post')
ax4.step(steps, cum_lst, label=f'LST ({",".join(seq_lst)})', marker='^', color='#2ca02c', where='post')

ax4.set_xlabel('Job Sequence Step', fontweight='bold')
ax4.set_ylabel('Cumulative Completion Time', fontweight='bold')
ax4.set_title('Plot 4: Trajectory of Makespan', fontweight='bold', fontsize=14)
ax4.set_xticks(steps)
ax4.set_xticklabels(['Start', 'Job 1', 'Job 2', 'Job 3', 'Job 4'])
ax4.grid(True, linestyle='--', alpha=0.6)
ax4.legend()

plt.tight_layout()
plt.savefig('plot_4_completion_trajectory.png', dpi=300)

# ==========================================
# PLOT 5: Job Characteristics Scatter (p vs d)
# ==========================================
fig5, ax5 = plt.subplots(figsize=(7, 5))

p_vals = [jobs[j]['p'] for j in job_labels]
d_vals = [jobs[j]['d'] for j in job_labels]
point_colors = [colors[j] for j in job_labels]

scatter = ax5.scatter(p_vals, d_vals, s=400, c=point_colors, edgecolor='black', zorder=5)

# Annotate points
for i, txt in enumerate(job_labels):
    ax5.annotate(f"{txt} (Slack={d_vals[i]-p_vals[i]})",
                 (p_vals[i], d_vals[i]),
                 xytext=(10, -10), textcoords='offset points',
                 fontweight='bold', zorder=6)

# Add y=x line (where processing time = due date, slack = 0)
lims = [0, 12]
ax5.plot(lims, lims, 'k--', alpha=0.5, label='Zero Initial Slack (p = d)')

ax5.set_xlim(0, 11)
ax5.set_ylim(0, 8)
ax5.set_xlabel('Processing Time (p)', fontweight='bold')
ax5.set_ylabel('Due Date (d)', fontweight='bold')
ax5.set_title('Plot 5: Job Characteristics (p vs d)', fontweight='bold', fontsize=14)
ax5.grid(True, linestyle='--', alpha=0.4)
ax5.legend(loc='upper right')

plt.tight_layout()
plt.savefig('plot_5_job_characteristics.png', dpi=300)

print("Visualizations successfully generated:")
print("1. plot_1_comprehensive_gantt.png")
print("2. plot_2_absolute_deviation.png")
print("3. plot_3_actual_lateness.png")
print("4. plot_4_completion_trajectory.png")
print("5. plot_5_job_characteristics.png")
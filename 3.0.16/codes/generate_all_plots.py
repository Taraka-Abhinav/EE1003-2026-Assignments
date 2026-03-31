"""
Master script to generate all plots for the Gaussian double integral assignment
Run this script to generate all visualization figures
"""

import subprocess
import sys
import os

# Change to the codes directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("Generating all plots for Gaussian Double Integral (Problem 3.0.16)")
print("=" * 70)
print()

scripts = [
    "surface_plot.py",
    "contour_plot.py",
    "polar_visualization.py",
    "separation_variables.py",
    "error_function.py",
    "monte_carlo_convergence.py"
]

for i, script in enumerate(scripts, 1):
    print(f"\n[{i}/{len(scripts)}] Running {script}...")
    print("-" * 70)
    try:
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errors:", result.stderr)
        print(f"✓ {script} completed successfully")
    except Exception as e:
        print(f"✗ Error running {script}: {e}")

print("\n" + "=" * 70)
print("All plots generated successfully!")
print("Check the ../figs/ directory for output images")
print("=" * 70)

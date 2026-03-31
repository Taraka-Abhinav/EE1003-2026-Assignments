# Problem 3.0.16 - Evaluating the Gaussian Double Integral

**Author:** CH. Taraka Abhinav (EE25BTECH11016)
**Course:** EE1003 - Mathematics and Engineering Optimization
**Problem:** Evaluate the double integral ∫₀^∞ ∫₀^∞ e^(-x²-y²) dx dy

## Problem Statement

Evaluate the Gaussian double integral:

```
I = ∫₀^∞ ∫₀^∞ e^(-x²-y²) dx dy
```

**Answer:** π/4 ≈ 0.7854

---

## Solution Methods

This assignment presents **FIVE** different methods to solve the Gaussian double integral:

### Method 0: Matrix Formulation (Standard Result)
- Uses the quadratic form representation: x² + y² = **x**ᵀ A **x**
- Applies the standard Gaussian integral theorem
- Exploits symmetry to restrict to first quadrant
- **Result:** π/4

### Method 1: Polar Coordinates (Classical Approach)
- Transform to polar coordinates: x = r cos θ, y = r sin θ
- Jacobian: dA = r dr dθ
- Separate the integral into angular and radial parts
- Angular: ∫₀^(π/2) dθ = π/2
- Radial: ∫₀^∞ r·e^(-r²) dr = 1/2
- **Result:** (π/2) × (1/2) = π/4

### Method 2: Separation of Variables
- Factor the integrand: e^(-x²-y²) = e^(-x²) · e^(-y²)
- Separate into product of independent integrals
- Use the 1D Gaussian integral: ∫₀^∞ e^(-x²) dx = √π/2
- **Result:** (√π/2)² = π/4

### Method 3: Error Function Approach
- Use the error function: erf(x) = (2/√π) ∫₀^x e^(-t²) dt
- Apply limit as x → ∞: lim erf(x) = 1
- Express integral in terms of error function
- **Result:** π/4

### Method 4: Monte Carlo Numerical Integration
- Generate random points in [0, L] × [0, L]
- Evaluate function at random points
- Average and multiply by area
- Converges to π/4 as N → ∞ and L → ∞
- **Estimated Result:** ~0.7829 (with N=1,000,000)

---

## Files Structure

```
3.0.16/
├── main.tex                    # LaTeX Beamer presentation
├── codes/
│   ├── requirements.txt        # Python dependencies
│   ├── generate_all_plots.py   # Master script to generate all plots
│   ├── surface_plot.py         # 3D surface visualization
│   ├── contour_plot.py         # Contour plot in first quadrant
│   ├── polar_visualization.py  # Polar coordinates transformation
│   ├── separation_variables.py # Separation of variables method
│   ├── error_function.py       # Error function approach
│   └── monte_carlo_convergence.py  # Monte Carlo simulation
└── figs/
    ├── surface_plot.png        # 3D plot of e^(-x²-y²)
    ├── contour_plot.png        # Level curves
    ├── polar_visualization.png # Polar grid transformation
    ├── separation_variables.png # Product of 1D Gaussians
    ├── error_function.png      # Error function convergence
    └── monte_carlo_convergence.png  # MC simulation results
```

---

## How to Generate Plots

### Prerequisites
Install required Python packages:
```bash
pip install -r codes/requirements.txt
```

or manually:
```bash
pip install numpy matplotlib scipy
```

### Generate All Plots
Run the master script:
```bash
cd codes
python3 generate_all_plots.py
```

### Generate Individual Plots
```bash
cd codes
python3 surface_plot.py
python3 contour_plot.py
python3 polar_visualization.py
python3 separation_variables.py
python3 error_function.py
python3 monte_carlo_convergence.py
```

---

## How to Compile LaTeX

### Prerequisites
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Required packages: beamer, amsmath, amssymb, tikz, xcolor

### Compile
```bash
pdflatex main.tex
pdflatex main.tex  # Run twice for proper references
```

or use:
```bash
latexmk -pdf main.tex
```

---

## Visualizations

### 1. Surface Plot
3D visualization of the Gaussian surface z = e^(-x²-y²) over the first quadrant.

### 2. Contour Plot
Level curves showing the circular symmetry of the function.

### 3. Polar Visualization
Three-panel comparison showing:
- Cartesian grid
- Polar grid overlay
- Pure polar representation

### 4. Separation of Variables
Shows how the 2D function factorizes into product of two 1D Gaussians.

### 5. Error Function
Demonstrates convergence using the error function and its limit properties.

### 6. Monte Carlo Convergence
Illustrates:
- Convergence vs sample size
- Random sample distribution
- Error scaling (σ ∝ N^(-1/2))

---

## Key Results

| Method | Key Technique | Result |
|--------|---------------|--------|
| Matrix Formulation | Gaussian integral theorem | π/4 |
| Polar Coordinates | Change of variables | π/4 |
| Separation of Variables | Product factorization | π/4 |
| Error Function | Special function limits | π/4 |
| Monte Carlo | Numerical simulation | ~0.7829 |

**Exact Value:** π/4 = 0.785398...

---

## Mathematical Insights

1. **Symmetry:** The function e^(-x²-y²) is radially symmetric about the origin
2. **Convergence:** The integral converges rapidly due to exponential decay
3. **Dimensionality:** The 2D integral reduces to simpler 1D problems
4. **Numerical Stability:** Monte Carlo converges as O(N^(-1/2))

---

## References

1. Gaussian integral - Wikipedia
2. Error function - NIST Digital Library
3. Monte Carlo integration - Numerical Recipes
4. [gadepall/ee1030-2025](https://github.com/gadepall/ee1030-2025) - Course repository

---

## License

This work is part of academic coursework for EE1003-2026.

---

**Date:** March 31, 2026

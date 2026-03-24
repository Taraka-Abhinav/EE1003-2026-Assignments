/*
 * ============================================================
 *  RC Circuit Transient Response — Data Generator
 *  Problem 1.1.16 | EC 2007
 *
 *  Circuit:  10V source -- 20kΩ -- [20kΩ || 4µF]
 *
 *  Results:
 *    Vc(t) = 5 * (1 - e^{-25t})   V
 *    ic(t) = 0.50 * e^{-25t}      mA
 *
 *  What this program does:
 *    1. Computes Vc(t) and ic(t) analytically
 *    2. Writes data to  rc_data.csv
 *    3. Writes a gnuplot script  rc_plot.gp
 *    4. Calls gnuplot to produce  rc_response.png
 *
 *  Compile:   gcc rc_plot.c -o rc_plot -lm
 *  Run:       ./rc_plot
 * ============================================================
 */

/* ── STEP 1 : Include required headers ─────────────────── */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/* ── STEP 2 : Define circuit constants ─────────────────── */
#define VS      10.0        /* Source voltage           (V)  */
#define R1      20000.0     /* Series resistor          (Ω)  */
#define R2      20000.0     /* Shunt  resistor          (Ω)  */
#define C_F     4e-6        /* Capacitance              (F)  */
#define VC0     0.0         /* Initial capacitor voltage(V)  */

#define N_POINTS 2000       /* Number of data points         */

/* ── STEP 3 : Derived quantities ───────────────────────── */
/* Thévenin resistance : R1 || R2 */
#define RTH     ( (R1 * R2) / (R1 + R2) )

/* Steady-state (final) capacitor voltage */
#define VINF    ( VS * R2 / (R1 + R2) )

/* Time constant τ = Rth * C */
#define TAU     ( RTH * C_F )

/* Initial capacitor current : Vc(0+) = 0 → cap is short */
#define IC0_MA  ( (VINF / RTH) * 1e3 )  /* in mA */

/* ── STEP 4 : Function prototypes ──────────────────────── */
double Vc(double t);
double ic_mA(double t);
void   write_csv(int n, double t_end);
void   write_gnuplot_script(double tau_ms, double vinf,
                            double t_end_ms);
void   print_summary(void);

/* ── STEP 5 : Main function ─────────────────────────────── */
int main(void)
{
    double t_end = 5.0 * TAU;       /* plot for 5τ           */

    printf("\n");
    printf("=============================================\n");
    printf("  RC Circuit Transient Response\n");
    printf("  Problem 1.1.16 | EC 2007\n");
    printf("=============================================\n");
    print_summary();

    /* Write CSV data */
    write_csv(N_POINTS, t_end);

    /* Write gnuplot script */
    write_gnuplot_script(TAU * 1e3, VINF, t_end * 1e3);

    /* Try to call gnuplot (optional — needs gnuplot installed) */
    printf("\n  Attempting to plot with gnuplot...\n");
    int ret = system("gnuplot rc_plot.gp 2>/dev/null");
    if (ret == 0)
        printf("  Plot saved as  rc_response.png\n");
    else
        printf("  gnuplot not found. Run manually:\n");
        printf("    gnuplot rc_plot.gp\n");

    printf("\n  Data saved to   rc_data.csv\n");
    printf("  Script saved to rc_plot.gp\n\n");
    return 0;
}

/* ── STEP 6 : Capacitor voltage equation ─────────────────
 *
 *   Vc(t) = V∞ + [Vc(0+) - V∞] * e^{-t/τ}
 *         = 5  + [0      -  5] * e^{-25t}
 *         = 5 * (1 - e^{-25t})   V
 */
double Vc(double t)
{
    return VINF + (VC0 - VINF) * exp(-t / TAU);
}

/* ── STEP 7 : Capacitor current equation ─────────────────
 *
 *   ic(t) = C * dVc/dt
 *         = C * d/dt [ V∞ (1 - e^{-t/τ}) ]
 *         = C * V∞/τ  * e^{-t/τ}
 *         = (V∞ / Rth) * e^{-25t}          A
 *         = 0.50 * e^{-25t}                mA
 */
double ic_mA(double t)
{
    return (VINF / RTH) * exp(-t / TAU) * 1e3;
}

/* ── STEP 8 : Write CSV data file ─────────────────────── */
void write_csv(int n, double t_end)
{
    FILE *fp = fopen("rc_data.csv", "w");
    if (!fp) { perror("fopen rc_data.csv"); exit(1); }

    /* Header row */
    fprintf(fp, "t_ms,Vc_V,ic_mA\n");

    double dt = t_end / (n - 1);
    for (int i = 0; i < n; i++) {
        double t  = i * dt;
        fprintf(fp, "%.6f,%.8f,%.8f\n",
                t * 1e3,        /* time in ms   */
                Vc(t),          /* Vc in V      */
                ic_mA(t));      /* ic in mA     */
    }
    fclose(fp);
    printf("\n  Written %d rows to rc_data.csv\n", n);
}

/* ── STEP 9 : Write gnuplot script ───────────────────── */
void write_gnuplot_script(double tau_ms, double vinf,
                          double t_end_ms)
{
    FILE *fp = fopen("rc_plot.gp", "w");
    if (!fp) { perror("fopen rc_plot.gp"); exit(1); }

    fprintf(fp,
        "# ── gnuplot script for RC circuit response ──\n"
        "set terminal pngcairo enhanced font 'Sans,11' "
        "size 1400,700 background '#0d1117'\n"
        "set output 'rc_response_c.png'\n"
        "\n"
        "# Dark theme colours\n"
        "set style line 101 lc rgb '#30363d' lt 1 lw 1\n"
        "set border lc rgb '#8b949e'\n"
        "set key textcolor rgb '#e6edf3'\n"
        "set tics textcolor rgb '#8b949e'\n"
        "\n"
        "# Layout: two plots side by side\n"
        "set multiplot layout 1,2 "
        "title 'RC Circuit Transient Response  —  "
        "Problem 1.1.16 (EC 2007)' "
        "font 'Sans Bold,13' textcolor rgb '#e6edf3'\n"
        "\n"
        "# ── LEFT: Vc(t) ──────────────────────────────\n"
        "set title 'Capacitor Voltage  V_C(t)' "
        "textcolor rgb '#e6edf3' font 'Sans Bold,11'\n"
        "set xlabel 'Time (ms)' textcolor rgb '#e6edf3'\n"
        "set ylabel 'V_C  (V)' textcolor rgb '#e6edf3'\n"
        "set grid ls 101\n"
        "set yrange [-0.3:6.0]\n"
        "set xrange [0:%.1f]\n"
        "set object 1 rect from graph 0,0 to graph 1,1 "
        "behind fc rgb '#161b22' fs solid\n"
        "\n"
        "# Tau annotation\n"
        "set arrow 1 from %.2f, 0 to %.2f, %.4f "
        "lc rgb '#3fb950' lw 1.5 dt 2 nohead\n"
        "set label 1 sprintf('τ = %.0f ms\\n%.4f V (63.2%%%%)',%.1f,%.4f) "
        "at %.2f, %.4f tc rgb '#3fb950' font 'Sans,9' left\n"
        "\n"
        "# Vinf dashed line\n"
        "set arrow 2 from 0, %.1f to %.1f, %.1f "
        "lc rgb '#d29922' lw 1.5 dt 2 nohead\n"
        "set label 2 'V_{∞} = %.0f V' "
        "at %.1f, %.3f tc rgb '#d29922' font 'Sans,9' right\n"
        "\n"
        "plot 'rc_data.csv' using 1:2 with lines "
        "lc rgb '#58a6ff' lw 2.5 title 'V_C(t) = 5(1 - e^{-25t})  V'\n"
        "\n"
        "unset arrow 1\nunset arrow 2\n"
        "unset label 1\nunset label 2\n"
        "unset object 1\n"
        "\n"
        "# ── RIGHT: ic(t) ─────────────────────────────\n"
        "set title 'Capacitor Current  i_c(t)' "
        "textcolor rgb '#e6edf3' font 'Sans Bold,11'\n"
        "set xlabel 'Time (ms)' textcolor rgb '#e6edf3'\n"
        "set ylabel 'i_c  (mA)' textcolor rgb '#e6edf3'\n"
        "set yrange [-0.03:0.58]\n"
        "set object 2 rect from graph 0,0 to graph 1,1 "
        "behind fc rgb '#161b22' fs solid\n"
        "\n"
        "set label 3 'i_c(0^+) = 0.50 mA' "
        "at 2, 0.51 tc rgb '#3fb950' font 'Sans,9' left\n"
        "\n"
        "plot 'rc_data.csv' using 1:3 with lines "
        "lc rgb '#f78166' lw 2.5 title 'i_c(t) = 0.50 e^{-25t}  mA'\n"
        "\n"
        "unset multiplot\n",

        /* xrange */   t_end_ms,
        /* arrow1 */   tau_ms, tau_ms, vinf * (1 - exp(-1.0)),
        /* label1 */   tau_ms, vinf * (1 - exp(-1.0)),
                       tau_ms, vinf * (1 - exp(-1.0)),
                       tau_ms + 4, vinf * (1 - exp(-1.0)) + 0.1,
        /* arrow2 */   vinf, t_end_ms, vinf,
        /* label2 */   vinf, t_end_ms - 2, vinf + 0.15
    );

    fclose(fp);
    printf("  Written gnuplot script to rc_plot.gp\n");
}

/* ── STEP 10 : Print parameter summary ─────────────────── */
void print_summary(void)
{
    printf("\n  Circuit Parameters\n");
    printf("  ------------------------------------------\n");
    printf("  Source Voltage     Vs   = %.1f V\n",  VS);
    printf("  Series Resistor    R1   = %.0f kΩ\n", R1 / 1e3);
    printf("  Shunt  Resistor    R2   = %.0f kΩ\n", R2 / 1e3);
    printf("  Capacitance        C    = %.0f µF\n",  C_F * 1e6);
    printf("  ------------------------------------------\n");
    printf("  Thévenin Resistance Rth = %.1f kΩ\n", RTH / 1e3);
    printf("  Steady-State Voltage V∞ = %.1f V\n",  VINF);
    printf("  Time Constant       τ   = %.1f ms\n", TAU * 1e3);
    printf("  Decay Exponent     1/τ  = %.1f s⁻¹\n",1.0 / TAU);
    printf("  ------------------------------------------\n");
    printf("  Vc(t) = %.0f(1 - e^{-25t}) V\n",     VINF);
    printf("  ic(t) = %.2f * e^{-25t}   mA\n",     IC0_MA);
    printf("  ------------------------------------------\n");
    printf("  Answer : Option (a)\n");
    printf("  ------------------------------------------\n");
}

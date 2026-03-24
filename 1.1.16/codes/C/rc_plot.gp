# ── gnuplot script for RC circuit response ──
set terminal pngcairo enhanced font 'Sans,11' size 1400,700 background '#0d1117'
set output 'rc_response_c.png'

# Dark theme colours
set style line 101 lc rgb '#30363d' lt 1 lw 1
set border lc rgb '#8b949e'
set key textcolor rgb '#e6edf3'
set tics textcolor rgb '#8b949e'

# Layout: two plots side by side
set multiplot layout 1,2 title 'RC Circuit Transient Response  —  Problem 1.1.16 (EC 2007)' font 'Sans Bold,13' textcolor rgb '#e6edf3'

# ── LEFT: Vc(t) ──────────────────────────────
set title 'Capacitor Voltage  V_C(t)' textcolor rgb '#e6edf3' font 'Sans Bold,11'
set xlabel 'Time (ms)' textcolor rgb '#e6edf3'
set ylabel 'V_C  (V)' textcolor rgb '#e6edf3'
set grid ls 101
set yrange [-0.3:6.0]
set xrange [0:200.0]
set object 1 rect from graph 0,0 to graph 1,1 behind fc rgb '#161b22' fs solid

# Tau annotation
set arrow 1 from 40.00, 0 to 40.00, 3.1606 lc rgb '#3fb950' lw 1.5 dt 2 nohead
set label 1 sprintf('τ = 40 ms\n3.1606 V (63.2%%)',40.0,3.1606) at 44.00, 3.2606 tc rgb '#3fb950' font 'Sans,9' left

# Vinf dashed line
set arrow 2 from 0, 5.0 to 200.0, 5.0 lc rgb '#d29922' lw 1.5 dt 2 nohead
set label 2 'V_{∞} = 5 V' at 198.0, 5.150 tc rgb '#d29922' font 'Sans,9' right

plot 'rc_data.csv' using 1:2 with lines lc rgb '#58a6ff' lw 2.5 title 'V_C(t) = 5(1 - e^{-25t})  V'

unset arrow 1
unset arrow 2
unset label 1
unset label 2
unset object 1

# ── RIGHT: ic(t) ─────────────────────────────
set title 'Capacitor Current  i_c(t)' textcolor rgb '#e6edf3' font 'Sans Bold,11'
set xlabel 'Time (ms)' textcolor rgb '#e6edf3'
set ylabel 'i_c  (mA)' textcolor rgb '#e6edf3'
set yrange [-0.03:0.58]
set object 2 rect from graph 0,0 to graph 1,1 behind fc rgb '#161b22' fs solid

set label 3 'i_c(0^+) = 0.50 mA' at 2, 0.51 tc rgb '#3fb950' font 'Sans,9' left

plot 'rc_data.csv' using 1:3 with lines lc rgb '#f78166' lw 2.5 title 'i_c(t) = 0.50 e^{-25t}  mA'

unset multiplot

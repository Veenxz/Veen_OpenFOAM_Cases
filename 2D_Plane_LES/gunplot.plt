set key default

set xlabel "Time (s)"

set ylabel "Residuals"

set logscale y

set format y "%.0e"

set grid

plot 'postProcessing/residuals/0/residuals.dat' u 1:2 w l linewidth"1.5" title"p", 'postProcessing/residuals/0/residuals.dat' u 1:3 w l linewidth"1.5" title"Ux", 'postProcessing/residuals/0/residuals.dat' u 1:4 w l linewidth"1.5" title"Uy", 'postProcessing/residuals/0/residuals.dat' u 1:5 w l linewidth"1.5" title"k", 'postProcessing/residuals/0/residuals.dat' u 1:6 w l linewidth"1.5" title"epsilon"

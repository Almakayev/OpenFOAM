#!/bin/bash

. $WM_PROJECT_DIR/bin/tools/RunFunctions

# Run meshing and calculation

# run()
# {
#     (
#         # cd ${1}
#         runApplication blockMesh
#         runApplication sonicFoam
#     )
# }

# Plot real-time
# foamMonitor postProcessing/probes/0/p

# Plot the pressure and save to the file 
cat << EOF | gnuplot -persist
set terminal postscript eps size 5,4 enhanced color
set xlabel "Time (s)"
set ylabel "Pressure at the piston (Pa)"
set output "piston_pressure.eps"
plot "postProcessing/probes/0/p" us 1:(\$2/109511.8) t "Pressure at the piston" w l
EOF

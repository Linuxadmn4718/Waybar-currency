#!/usr/bin/env python3

import subprocess
from os.path import expanduser

# Define paths
home = expanduser("~")
gnuplot_script_path = f"{home}/.config/hypr/waybar/scripts/Currency/plot_rates.gp"
image_path = f"{home}/.config/hypr/waybar/scripts/Currency/rates.png"

# Generate the plot using gnuplot
subprocess.run(['/usr/bin/gnuplot', gnuplot_script_path], check=True)

# Command to display the image using yad
subprocess.run(['/usr/bin/yad', '--size=FIT', '--picture', image_path], check=True)
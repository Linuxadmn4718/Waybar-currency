#!/bin/bash

# Generate the plot using gnuplot
/usr/bin/gnuplot $HOME/.config/hypr/waybar/scripts/Currency/plot_rates.gp

# Command to display the image
/usr/bin/yad --size=FIT --picture $HOME/.config/hypr/waybar/scripts/Currency/rates.png 

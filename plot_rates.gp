# plot_rates.gp
set terminal png size 800,600

set key textcolor rgb "white"

# Set title for the plot with white text
set title "Exchange Rate" textcolor rgb "white"  font ",16"

# Set the output type to a PNG image
set terminal pngcairo size 800,600 enhanced font 'Verdana,10'

set ylabel "Exchange Rate" textcolor rgb "white"

# Set x-tics with white text and smaller font size
set xtics textcolor rgb "white" font ",6"
set ytics textcolor rgb "white" font ",11"

   
# Set the output file
set output '~/.config/hypr/waybar/scripts/Currency/rates.png'
   
# Set titles and labels
set title 'Exchange Rate Graph'

set ylabel 'Exchange Rate (PHP)'

# Customize the grid and style
#set grid
#set style data linespoints

# Enable grid for better visualization with a less bright color
set grid lc rgb "#595959"

# Set graph background color to dark gray
set obj 1 rectangle from screen 0,0 to screen 1,1 behind
set obj 1 fillstyle solid 1.0 fillcolor rgb "#353535"

# Enable autoscaling initially
set autoscale y


# Plot the data from rate_history
plot '~/.config/hypr/waybar/scripts/Currency/rate_history' using 0:1 with lines linecolor rgb "green" title 'Rate' 

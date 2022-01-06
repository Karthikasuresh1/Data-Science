from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show
output_file("kar.html")
plot1 = figure(plot_width = 500, plot_height =500, title = "Scatter Markers")
plot1.line([1,2,3,4,5,6], [2,1,6,8,0], line_width=4, color="red")
show(plot1)

from bokeh.plotting import figure
from bokeh.plotting import output_file 
from bokeh.plotting import show
output_file("jtp.html")
graph1 = figure(title = "Pie Chart using Bokeh")
x=0
y=0
radius = 1
start_angle = [0, 1.2, 2.1, 3.3, 5.1]
end_angle=[1.2, 2.1, 3.3, 5.1, 0]
color1 = ["brown", "grey", "green", "orange", "red"]
graph1.wedge(x , y , radius , start_angle , end_angle , color = color1)
show(graph1)
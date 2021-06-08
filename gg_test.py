from ggplot_log import *

a=ggplot(mtcars,x="wt",y="mpg")
a=a+geom_line(color='red')
print(a)
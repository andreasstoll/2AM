from ggplot_log import *

print(mtcars.head())
a=ggplot(mtcars[:5],x="name", color="gear")
a=a+geom_bar()
print(a)
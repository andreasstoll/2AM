import logging
import plotnine as p9
from plotnine.data import *

logging.basicConfig(level=logging.WARNING, filename='wsggplot.log', filemode='a', format='%(asctime)s -%(levelname)s - %(message)s')

def logger(func):
    """Logt bei der Funktion func folgendes 'Name des Files:Name der Funktion(kwargs)"""
    def wrapper(*args, **kwargs):
        msg=str(kwargs)
        logging.warning(__name__+";"+func.__name__+"("+msg+")")
        return func(*args, **kwargs)
    return wrapper

@logger
def ggplot(data, *args, **kwargs):
    """Gibt ein ggplot-Objekt mit aes zurück und logt dieses gemäss Decorator logger"""
    return p9.ggplot(data,p9.aes(*args, **kwargs))

TO_LOG = [
    'geom_point',
    'geom_line',
    'geom_histogram',
    'geom_bar',
    'geom_boxplot'
]

#Wendet den Decorator logger auf alle Funktionen in TO_Log an
for name in TO_LOG: 
    globals()[name] = logger(getattr(p9, name))



if __name__ == "__main__":

    a=ggplot(mtcars,x="wt")
    a=a+geom_histogram(color='pink')
    print(a)

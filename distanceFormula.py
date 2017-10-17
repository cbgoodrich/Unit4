#Charlie Goodrich
#10/16/17
#distanceFormula.py - distance formula between two points

from math import sqrt

def distance(x1, y1, x2, y2):
    print(sqrt((x2-x1)**2 + (y2-y1)**2))
    
distance(0,0,1,1)
    

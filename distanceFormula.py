#Charlie Goodrich
#10/16/17
#distanceFormula.py - distance formula between two points

from math import sqrt

def distance(x1, y1, x2, y2):
    return (sqrt((x2-x1)**2 + (y2-y1)**2))

print(distance(3, 4, -5, 2))
    

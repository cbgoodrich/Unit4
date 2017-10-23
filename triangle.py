#Charlie Goodrich
#10/23/17
#triangle.py - prints the area of a triangle

from math import sqrt

def triangle(x1, y1, x2, y2, x3, y3):
    a = sqrt((x1-x2)**2 + (y1-y2)**2) #side a
    b = sqrt((x2-x3)**2 + (y2-y3)**2) #side b
    c = sqrt((x3-x1)**2 + (y3-y1)**2) #side c
    
    s = .5 * (a + b + C)
    
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area
    
print(triangle(1,2,3,4,5,6))

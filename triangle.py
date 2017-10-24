#Charlie Goodrich
#10/23/17
#triangle.py - prints the area of a triangle

from math import sqrt

#inputs
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

#finding the length of side a
def distance_a(x1, y1, x2, y2):
    return (sqrt((x2-x1)**2 + (y2-y1)**2))
a = distance_a(x1, y1, x2, y2)

#finding the length of side b
def distance_b(x2, y2, x3, y3): 
    return (sqrt((x3-x2)**2 + (y3-y2)**2))
b = distance_b(x2, y2, x3, y3)

#finding the length of side c
def distance_c(x1, y1, x2, y2): 
    return (sqrt((x1-x3)**2 + (y1-y3)**2))
c = distance_c(x1, y1, x3, y3)    

#finding s for computing the area
s = .5 * (a + b + c)

area = sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
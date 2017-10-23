#Charlie Goodrich
#10/23/17
#triangle.py - prints the area of a triangle

from math import sqrt

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

def distance_a(x1, y1, x2, y2):
    a = (sqrt((x2-x1)**2 + (y2-y1)**2))
    return a
def distance_b(x2, y2, x3, y3):
    b = (sqrt((x3-x2)**2 + (y3-y2)**2))
    return b
def distance_c(x1, y1, x2, y2):
    c = (sqrt((x1-x3)**2 + (y1-y3)**2))
    return c
s = .5 * (a + b + c)

area = sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
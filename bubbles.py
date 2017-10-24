#Charlie Goodrich
#10/24/17
#bubbles.py - prints out lots of bubbles when you click

from ggame import *
from random import randint

def mouseClick(event):
    radius = randint(1, 100)
    colorCode = randint(1, 3)
    x_pos = randint(0, 700)
    y_pos = randint(0, 500)

    
    if colorCode == 1:
        red = Color(0xFF0000, 1)
        bubble = CircleAsset(radius, LineStyle(1, red), red)
    elif colorCode == 2:
        green = Color(0x00FF00, 1)
        bubble = CircleAsset(radius, LineStyle(1, green), green)
    else:
        blue = Color(0x0000FF, 1)
        bubble = CircleAsset(radius, LineStyle(1, blue), blue)
    
    Sprite(bubble, (x_pos, y_pos))
    
App().listenMouseEvent("click", mouseClick)
App().run()

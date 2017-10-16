#Charlie Goodrich
#10/16/17
#colorChangeWindow.py - changes the window color after every click

from random import randint
from ggame import *

def mouseClick():
    num = randint(1,3)
    
    if num == 1:
        red = Color(0xFF0000, 1)
        redRect = RectangleAsset(1000, 1000, LineStyle(1, red), red)
        Sprite(redRect)
        
    elif num == 2:
        green = Color(0x00FF00, 1)
        greenRect = RectangleAsset(1000, 1000, LineStyle(1, green), green)
        Sprite(greenRect)

    else:
        blue = Color(0x0000FF, 1)
        blueRect = RectangleAsset(1000, 1000, LineStyle(1, blue), blue)
        Sprite(blueRect)

        
App().listenMouseEvent("click", mouseClick)
App().run()
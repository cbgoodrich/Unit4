#Charlie Goodrich
#10/26/17
#sunrise.py - creates a sunrise

from ggame import *

def moveSun():
    ball.x += data["direction x"]
    ball.y += data["direction y"]

if __name__ == "__main__":
    
    data = {}
    data["direction x"] = .25
    data["direction y"] = 1
    
    #colors
    blue = Color(0x33E9FF, 1)
    yellow = Color(0xFFFF00, 1)
    
    sky = RectangleAsset(1050, 600, LineStyle(1, blue), blue)
    yellowOrb = CircleAsset(50, LineStyle(1, yellow), yellow)
    
    Sprite(sky)
    sun = Sprite(yellowOrb, (525, 600))
    
    App().run(moveSun)
    

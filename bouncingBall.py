#Charlie Goodrich
#10/25/17
#bouncingBall.py - makes a ball move around the screen

from ggame import *

#CONSTANTS
WINDOW_X = 1000
WINDOW_Y = 525
PIXEL_MOVE = 25
RADIUS = 50



def moveBall():
    ball.x += data["direction x"]
    ball.y += data["direction y"]
    
def step():
    if ball.x < WINDOW_X and ball.y < WINDOW_Y:
        moveBall()
    elif ball.x >= WINDOW_X:
        data["direction x"] *= -1
        data["direction y"] += 0
    elif ball.y >= WINDOW_Y:
        data["direction y"] *= -1
        data["direction x"] += 0
    elif ball.x <= 0:
        data["direction x"] *= -1
        data["direction y"] += 0
    elif ball.y <= 0:
        data["direction y"] *= -1
        data["direction x"] += 0
        
    

if __name__ == "__main__":
    
    data = {}
    data["direction x"] = 25
    data["direction y"] = 25
    
    #Colors
    green = Color(0x00FF00, 1)
    greenOutline = LineStyle(1, green)
    black = Color(0x000000, 1)
    blackOutline = LineStyle(1, black)
    
    
    greenCircle = CircleAsset(RADIUS, greenOutline, green)
    background = RectangleAsset(WINDOW_X, WINDOW_Y, blackOutline, black)
    
    Sprite(background)
    ball = Sprite(greenCircle, (RADIUS, RADIUS))
    
    App().run(step)
    

    
    

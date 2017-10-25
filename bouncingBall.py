#Charlie Goodrich
#10/25/17
#bouncingBall.py - makes a ball move around the screen

from ggame import *

#CONSTANTS
WINDOW_X = 1000
WINDOW_Y = 600
PIXEL_MOVE = 25
RADIUS = 50



def moveBall():
    ball.x += PIXEL_MOVE
    ball.y += PIXEL_MOVE
    
def step():
    if ball.x < WINDOW_X and ball.y < WINDOW_Y:
        moveBall()
    else:
        PIXEL_MOVE = PIXEL_MOVE * (-1)
        moveBall()
    

if __name__ == "__main__":
    

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
    
    

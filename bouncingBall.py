#Charlie Goodrich
#10/25/17
#bouncingBall.py - makes a ball move around the screen

from ggame import *

#CONSTANTS
WINDOW_X = 1000
WINDOW_Y = 600
PIXEL_MOVE = 25

#ball starting coordinates
ball_x = 0
ball_y = 0

def moveBall():
    ball_x += PIXEL_MOVE
    ball_y += PIXEL_MOVE
    
def step():
    if ball_x < 1000 and ball_y < 600:
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
    
    ball = CircleAsset(50, greenOutline, green)
    background = RectangleAsset(1000, 600, blackOutline, black)
    
    Sprite(background)
    Sprite(ball, (ball_x, ball_y_))
    
    App().run()
    
    
